import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import imageio
from threading import Thread

def stardata(Number_of_Stars,theradius,sigmadistance,mass,minvelocity,maxvelocity,data=[]):
    for i in range(Number_of_Stars):
        j=0
        while j==0:
            xpos=float(np.random.normal(0,sigmadistance,1))
            ypos=float(np.random.normal(0,sigmadistance,1))
            if xpos>=0:
                xpos=theradius-xpos
            else:
                xpos=-theradius-xpos
            if ypos>=0:
                ypos=theradius-ypos
            else:
                ypos=-theradius-ypos
            if xpos**2+ypos**2<=theradius**2:
                position=[xpos,ypos]
                j=1
        x_velocity = random.randrange(minvelocity, maxvelocity)
        y_velocity = random.randrange(minvelocity, maxvelocity)
        data.append([position[0],position[1],x_velocity,y_velocity,mass])
    return (data)
'''
stardata=stardata(1000,100,60,1,1,100)
for i in range(1000):
    plt.plot(stardata[i][0],stardata[i][1],'.')
plt.show
'''