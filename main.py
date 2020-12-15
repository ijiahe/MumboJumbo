'''
主程序，不多说
'''
import makinganime
import plot_method1
import generatingstars
import starmoving
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

number_of_stars = 1000
timediffraction = 0.1
experiment_index = 2
number_of_flips = 100
theradius = 400
sigmadistance = 300
mass = 10000
minvelocity = 0
maxvelocity = 2
timediffraction = 0.01

def main():
    plot_method1.savefig(number_of_stars, timediffraction,experiment_index, number_of_flips, theradius, sigmadistance, mass,
         minvelocity, maxvelocity)
    makinganime.MakingAnimation(experiment_index, number_of_flips)
if __name__ == "__main__":
    main()