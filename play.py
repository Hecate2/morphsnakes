#coding:utf-8
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from scipy.io import loadmat
import cv2

from arrayvideo import ArrayVideo

print(cm.get_cmap())

BW = loadmat("project_2_manual_segmentation.mat")['BW']
print(BW.shape)
shape=BW.shape
##for i in range(shape[2]):
##    frame=BW[:,:,i]
##    plt.imshow(frame, cmap=cm.jet)
##    plt.show()
##
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
ArrayVideo(BW).play01()#play_dilated(kernel=kernel)
