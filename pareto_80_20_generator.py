# -*- coding: utf-8 -*-

import numpy as np
import time
import math
import quantecon as qe
import matplotlib.pyplot as plt
from scipy.stats import pareto
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

np.random.seed(1)
N = 10000000
alpha = math.log(5, 4)
LOOP = N


mean, var, skew, kurt = pareto.stats(b = alpha, moments = 'mvsk')
print(alpha)
print(mean, var, skew, kurt)

main_data = pareto.rvs(size = N, b = alpha)
maximum = max(main_data)

def build(N):  
    data = main_data[:N]
    plt.plot(data, color = 'b')
    plt.hlines(y = mean, xmin = 0, xmax = N, linestyle = "dashed", colors = 'r')
    fig = plt.gcf()
    plt.xlim([0, LOOP])
    plt.title('The first ' + str(N) + ' samples of Pareto alpha ' + "%.2f" %(alpha))
    fig.savefig('samples\\pareto_alpha_' + "%.2f" %(alpha) + '_first_' + str(N) + '_samples.png', dpi = 100)
    plt.clf()
    
    
    sample_mean = []
    total = 0;
    for i in range(len(data)):
        total += data[i]
        sample_mean.append(total/(i+1))
        
    plt.plot(sample_mean, color = 'g')
    plt.hlines(y = mean, xmin = 0, xmax = N, linestyle = "dashed", colors = 'r')
    plt.plot(data/maximum*10, color = 'b')
    fig = plt.gcf()
    plt.xlim([0, LOOP])
    plt.ylim([0, 10])
    plt.title('The sample mean failed to converge after '+ str(N) +' samples')
    fig.savefig('mean\\sample_mean_after_' + str(N) + '_samples_alpha_' + "%.2f" %(alpha) + '.png', dpi = 100)
    plt.clf()

for i in range(0, LOOP-1, 50000):
    build(i)

import os
import imageio
from natsort import natsorted, ns

def make_gif(source, name):
    png_dir = source
    images = []
    for file_name in natsorted(os.listdir(png_dir)):
        if file_name.endswith('.png'):
            file_path = os.path.join(png_dir, file_name)
            #print(file_path)
            images.append(imageio.imread(file_path))
    imageio.mimsave(name, images, fps = 30)

make_gif('samples', 'samples_generated.gif')
make_gif('mean', 'sample_mean.gif')


