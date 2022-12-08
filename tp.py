from itertools import cycle
from sklearn import datasets
from itertools import cycle
import matplotlib
import pylab as pl
irisData = datasets.load_iris()
print (irisData.data)
print (irisData.target)

def plot_2D(data, target, target_names):
    colors = cycle('rgbcmykw') # cycle de couleurs
    target_ids = range(len(target_names))
    pl.figure()
    for i, c, label in zip(target_ids, colors, target_names):
            pl.scatter(data[target == i, 0], data[target == i, 1], c=c, label=label)
            pl.legend()
            pl.show()

plot_2D(irisData.data,irisData.target,irisData.target_names)