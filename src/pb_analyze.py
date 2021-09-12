#TODO: change name of varaibles for make it more clear and explicate the code

import numpy as np
from scipy import stats
import math

def calculate_MI_global(frames_all):
    seq_size = len(frames_all[:,0])
    MI = np.zeros((seq_size,seq_size))
    eeMI = np.zeros((seq_size,seq_size))
    weight = 1 / seq_size
    for i in range(0,len(frames_all)):
        for j in range(i,len(frames_all)):
            px = calculate_px(frames_all[i],weight)
            py = calculate_px(frames_all[j],weight)
            pxy = calculate_pxy(frames_all[i],frames_all[j],weight)
            MI[i,j]=calulate_MI(px, py, pxy)
            eeMI[i,j]=calculate_eeMI(px, py, pxy)
            if i != j:
                MI[j,i]=MI[i,j]
                eeMI[j,i]=eeMI[i,j]
    return MI, eeMI

def calculate_px(frame, weight):
    matrix= np.zeros((16))
    for i in range(0,len(frame)):
        index_row = ord(frame[i])-97
        matrix[index_row] += weight
    return matrix


def calculate_pxy(frame_src, frame_target, weight):
    matrix= np.zeros((16,16))
    for i in range(0,len(frame_src)):
        index_row = ord(frame_src[i])-97
        index_col = ord(frame_target[i])-97
        matrix[index_row,index_col] += weight
    return matrix



def calulate_MI(px, py, pxy):
    size = len(px)
    MI = 0
    for i in range(0,size):
        for j in range(0,size):
            if pxy[i,j] != 0:
                MI += pxy[i,j] * math.log2(pxy[i,j]/(px[i]*py[j]))
    if MI > 0:
        return MI
    else:
        return 0            

def calculate_eeMI(px, py, pxy):
    return 0 #TODO: calculate expect error MI (number of value != 0 in px, py and pxy)

#TODO: make calculate of joint entropy : pxy[i,j] * log2(pxy[i,j])
