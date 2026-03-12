import pygame 
import numpy as np
from layout import Layout

class Simulator:
    def __init__(self, layout : Layout, config):
        self.dt = 1/1000
        self.fps = int(1/self.dt)
        self.layout = layout
        self.resolution = (200,200)

        self.steps = 2*layout.max_x/self.resolution[0], 2*layout.max_y/self.resolution[1]
        xcoordinatesraw = np.linspace(-self.layout.max_x, self.layout.max_x, self.resolution[0],endpoint=False,dtype=np.float32)
        ycoordinatesraw = np.linspace(-self.layout.max_y,self.layout.max_y,self.resolution[1],endpoint=False,dtype=np.float32)
        self.xcoordinates, self.ycoordinates =  np.meshgrid(xcoordinatesraw,ycoordinatesraw)
        self.pressures = np.zeros((self.resolution[0],self.resolution[1]), dtype=np.float32)
        self.gradients = np.zeros((self.resolution[0],self.resolution[1]), dtype=np.float32)
        self.soundspeed = np.full((self.resolution[0],self.resolution[1]),layout.c_inside,dtype=np.float32)

        if layout.max_x > layout.width / 2:
            mask = np.abs(np.abs(self.xcoordinates + self.ycoordinates) + np.abs(self.ycoordinates - self.xcoordinates)-2*layout.width - layout.barrier_width) < layout.barrier_width
            self.soundspeed[mask]=self.layout.c_outside

    def pressure_color(self):
        image = np.zeros((self.resolution[0],self.resolution[1],3))

        mask = (self.pressures >= 0)
        red = 255 - 255*np.exp(-self.pressures)
        blue = 255 - 255 *np.exp(self.pressures)


        mask2 = ( self.soundspeed > self.layout.c_inside*0.9)& (np.abs(self.pressures) < 0.1)
        #image[..,,0] = np.where(mask2, 255,0)
        image[...,1] = np.where(mask2, 20,0)
        #image[...,2] = np.where(mask2, 255,0)

        
        image[...,0] = np.where(mask, red, 0)
        image[...,2] = np.where(~mask, blue, 0)


        return image

    def update_gradients(self):
        laplacianx = self.pressures[:,:-2] - 2*self.pressures[:, 1:-1] + self.pressures[:, 2:]
        laplacianx /= self.steps[0]**2
        laplaciany = self.pressures[:-2, :] - 2*self.pressures[1:-1, :] + self.pressures[2:, :]
        laplaciany /= self.steps[1]**2
        self.gradients[:,1:-1] += (laplacianx)*self.dt*(self.soundspeed[:,1:-1])**2
        self.gradients[1:-1,:] += laplaciany * self.dt * self.soundspeed[1:-1,:]**2

    def update_pressures(self):
        self.pressures += self.gradients * self.dt
        self.pressures *= 0.999* np.exp(-self.dt)

    
    def upd(self):
        self.update_gradients()
        self.update_pressures()