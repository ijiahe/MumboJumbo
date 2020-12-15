import makinganime
import generatingstars
import starmoving
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def savefig(number_of_stars, timediffraction,experiment_index, number_of_flips, theradius, sigmadistance, mass,
         minvelocity, maxvelocity):
    data = generatingstars.stardata(number_of_stars, theradius, sigmadistance, mass, minvelocity, maxvelocity)
    path=makinganime.thepath()
    for i in range(number_of_flips):
        plt.xlim(-theradius, theradius)
        plt.ylim(-theradius, theradius)
        for j in range(number_of_stars):
            plt.plot(data[j][0],data[j][1],'.')
        plt.savefig(path+'\\experiment{0}\\{1}.png'.format(experiment_index,i))
        print(i)
        plt.close()
        for j in range(100):
            data=starmoving.starmoving(data,timediffraction)


