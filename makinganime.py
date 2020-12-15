import os
import numpy
import imageio
from matplotlib.animation import FuncAnimation

'''
这个程序啊，就是生成动画的。
你要在main里面改experimentnumber，这样就可以从不同的文件夹里面读取图片，然后在Anime文件夹里面可以找到gif动画
'''

def thepath():
    the_path=__file__.replace('\\',r'\\')
    the_path=the_path.replace(r'\\makinganime.py',r'\\')
    return the_path

def MakingAnimation(experiment_index,number_of_pix,thefps=40):
    gif_images=[]
    path=thepath()
    for i in range(number_of_pix):
        gif_images.append(imageio.imread(path+"experiment{0}\\{1}.png".format(experiment_index,i)))
        print('Reading... ',i)
    print('Generating Gif...')
    imageio.mimsave(path+"animates\\Anime{0}.gif".format(experiment_index),gif_images,fps=thefps)
    print('Video Is Successfully Generated')