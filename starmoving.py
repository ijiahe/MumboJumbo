'''
这个程序就是用来模拟行星运动的，也许可以用来模拟较大数据，但是估计很卡。
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import imageio

def starmoving(data,timediffraction):
    newdata=[]
    for i in range(len(data)):
        x_pos=data[i][0]
        y_pos=data[i][1]
        x_velocity=data[i][2]
        y_velocity=data[i][3]
        mass=data[i][4]
        netxF, netyF, net_int_xF, net_int_yF = [], [], 0, 0
        for j in range(len(data)):
            if i==j:
                continue
            x_tmp_pos=data[j][0]
            y_tmp_pos=data[j][1]
            tmp_mass=data[j][4]
            r=((x_pos-x_tmp_pos)**2+(y_pos-y_tmp_pos)**2)**0.5
            sin_value = (y_tmp_pos - y_pos) / r
            cos_value = (x_tmp_pos - x_pos) / r
            if r==0.01:
                continue
            xF = (((6.67e-11)*mass*tmp_mass)/(r**2))*cos_value
            yF = (((6.67e-11)*mass*tmp_mass)/(r** 2))*sin_value
            netxF.append(xF)
            netyF.append(yF)
        net_int_xF = sum(netxF)
        net_int_yF = sum(netyF)  # force
        net_x_accele = net_int_xF / mass
        net_y_accele = net_int_yF / mass  # acceleraction
        x_displacement = x_velocity * timediffraction + 0.5 * net_x_accele * timediffraction ** 2
        y_displacement = y_velocity * timediffraction + 0.5 * net_y_accele * timediffraction ** 2  # displacement
        new_x_velocity = x_velocity + net_x_accele * timediffraction
        new_y_velocity = y_velocity + net_y_accele * timediffraction  # newvelocity
        new_temp_prop = [x_pos + x_displacement, y_pos + y_displacement, new_x_velocity, new_y_velocity,
                         mass]  # new property for stars
        newdata.append(new_temp_prop)
    return (newdata)