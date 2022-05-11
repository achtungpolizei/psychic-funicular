# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 21:42:12 2022

@author: soenk
"""

import numpy as np
import matplotlib.pyplot as plt


def getNextValue(xNow,r):
    return xNow**2 + r #r*xNow*(1-xNow) 

def getbifurcationVals(r):
   
    calcRes = 50
    branchRes = 20
    xNow = 0
    
    fVal = []
    
    for n in np.arange(calcRes):
        xNow = getNextValue(xNow,r)
        fVal.append(xNow)
        
    bifurcationVals = fVal[calcRes-branchRes:]
    return bifurcationVals

def calcMandelbrotPixelColor(x0,y0):
    
    iteration = 0
    max_iteration = 100
    x2 = 0
    y2 = 0
    w = 0
    
    while (x2 + y2 <= 4) and (iteration < max_iteration):
        x = x2 - y2 + x0
        y = w - x2 - y2 + y0
        x2 = x*x
        y2 = y*y
        w = (x + y) * (x + y)
        iteration += 1
        color = iteration/max_iteration
        
    return color

startR=1

def plotxNowvsxNext(function):  
    xSpace = np.linspace(0,1,1000)
    r=1
    yVals = function(xSpace,r)
    fig, ax = plt.subplots()
    ax.plot(xSpace,yVals) 
    return fig, ax



xmin=-2
xmax=0.47
ymin=-1.12
ymax=1.12

res = 20000

spaceX = np.linspace(xmin,xmax,res)
spaceY = np.linspace(ymin,ymax,res)
imageSpace = np.zeros([len(spaceY),len(spaceX)])



#palette = [np.linspace(0,1,max_iteration),np.linspace(1,0,max_iteration),np.zeros(max_iteration)]

pixel = []

xVal=0
for x0 in spaceX:
    yVal=0
    for y0 in spaceY:            
        imageSpace[yVal][xVal] = calcMandelbrotPixelColor(x0, y0)
        yVal+=1
    
    xVal+=1
    progress = xVal*100/len(spaceX)
    print("Progress: {:3.2f}%".format(progress))
    
fig, ax = plt.subplots()

ax.imshow(imageSpace)
print("Start saving to .png")
fig.savefig("mandelbrot.png", dpi = 2000, bbox_inches='tight')
print("Finished!")