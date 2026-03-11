# I am making this class to basically encode the "global" data 
# we need to communicate to the program the chamber's properties
# everything is in SI units (m, m/s)
import math

ARGON_SPEED = 323
GLASS_SPEED = 5640

CONFIG_MIC_OUTSIDE = 0
CONFIG_MIC_INSIDE = 1

class Layout:
    def __init__(self, config):
        self.width = 0.1
        self.height = 0.1
        self.barrier_width = 0.005
        self.c_inside = ARGON_SPEED # speed of sound in argon
        self.c_outside= GLASS_SPEED # for now

        # coordinate system from [-max_x,max_x] for x and [-max_y,max_y] for y
        self.max_x, self.max_y = self.width/2, self.height/2
        if config == CONFIG_MIC_OUTSIDE:
            self.max_x += self.barrier_width
            self.max_y += self.barrier_width
    

        self.microphones = [(-self.max_x, -self.max_y), 
                       (-self.max_x,self.max_y), 
                       (self.max_x,self.max_y),
                       (self.max_x, -self.max_y)]



