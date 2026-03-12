import layout
import numpy as np
from math import factorial
from scipy.optimize import least_squares,minimize

class Triangulator:
    def __init__(self, layout :layout.Layout):
        self.layout = layout 

    def thinGlassApproximation(self, TDoA_array, reference_mic=1):
        reference_mic -= 1

        num_mics = len(self.layout.microphones)
        num_TDoA = num_mics*(num_mics-1)//2

        if len(TDoA_array) != num_TDoA:
            raise Exception("tdoa array does not match layout!")

        pairs = []
        index = 0
        for i in range(num_mics):
            for j in range(i+1, num_mics):
                pairs.append((i,j,TDoA_array[index]))
                index += 1

        refs = []
        for i,j,dt in pairs:
            if i == reference_mic:
                refs.append((j,dt))
            elif j == reference_mic:
                refs.append((i,-dt))

        ref_pos = self.layout.microphones[reference_mic]
        v = self.layout.c_inside

        def residuals(p):

            d_ref = np.linalg.norm(p - ref_pos)

            r = []
            for mic_i, dt in refs:

                pos = self.layout.microphones[mic_i]
                d_i = np.linalg.norm(p - pos)

                r.append(d_i - d_ref - v*dt)

            return r

        guess = np.mean(self.layout.microphones, axis=0)

        res = least_squares(residuals, guess)

        return res.x

    



            


        


