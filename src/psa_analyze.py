"""
Statisitic analysis for the determiation of allosteric communiation

=====================================================================

Analysis tools for allosteric movements between protein blocks generated by
PBxplore, based on the same analyse do by GSA-tools with Gromacs related 
structural alphabet.

This part of the program target to parse fasta file from PBxplore and calculate the 
joint entropy, the mutual information and the expected error of this mutual information 
between two columns in the parse fasta. This three statistic parameters permit to calculate 
the normalized mutual information, and make an idea of the correlated local motion in a protein.

The principe of the calcul are explained in the artical of Pandini et al., 2012 in the
FASEB J., and they are detailed in the notebook present in psa_tool/doc.
"""

import numpy as np
import math
from Bio import SeqIO

def stats_analyze(frames_all): 
    """Calculate normalized mutual information and others needed parameters for it:

    - frames_all (numpy array): parsed fasta into Python (preferably transposed)

    return: normalized mutual information, mutual information, joint entropy, mutual information expected error
    """
    seq_size = len(frames_all[:,0])
    weight = 1 / seq_size 
    #initialization of matrixes
    mi = np.zeros((seq_size,seq_size)) 
    joint_entropy = np.zeros((seq_size,seq_size))
    eemi = np.zeros((seq_size,seq_size))
    normalized_mi = np.zeros((seq_size,seq_size))
    for i in range(0,len(frames_all)):
        for j in range(i,len(frames_all)):
            px = calculate_p(frames_all[i],weight) 
            py = calculate_p(frames_all[j],weight)
            pxy = calculate_pxy(frames_all[i],frames_all[j],weight)
            mi[i, j] = calulate_mi(px, py, pxy)
            joint_entropy[i, j] = calculate_joint_entropy(pxy)
            bx = np.count_nonzero(px)
            by = np.count_nonzero(py)
            bxy = np.count_nonzero(pxy)
            eemi[i, j] = calculate_eemi(bxy, bx, by, seq_size)
            if joint_entropy[i, j] != 0:
                normalized_mi[i, j] = (mi[i, j] - eemi[i, j])/joint_entropy[i, j]
            else:
                normalized_mi[i, j] = 0
            if i != j: #transpose the matrix
                mi[j, i]=mi[i, j]
                eemi[j, i]=eemi[i, j]
                joint_entropy[j, i]=joint_entropy[i, j]
                normalized_mi[j, i] = normalized_mi[i, j]
    return mi, eemi, joint_entropy, normalized_mi

def calculate_p(frame, weight): 
    """Calculate the probability of each letter in a PBs and integre it in list

    - frame (list): list of letter in a frame
    - weight (float): 1 divide by the lenght of sequences

    return (matrix): probability of each appear of letters in a fragment
    """
    matrix= np.zeros((16)) #initialization of matrix
    for i in range(0,len(frame)):
        index_row = ord(frame[i])-97 #discretisation of the alphabet in int number (based on ASCII coding)
        matrix[index_row] += weight
    return matrix


def calculate_pxy(frame_src, frame_target, weight):
    """Calculate the probability of each transition of letters in a frame

    frame_src (list): list of letters in the frame source
    frame_target (list): list of letters in the frame target
    weight (float): 1 divide by the lenght of sequences

    return (matrix): probability of transition between each frames
    """
    matrix= np.zeros((16,16)) #initialization of matrix
    for i in range(0,len(frame_src)):
        index_row = ord(frame_src[i])-97 #discretisation of the alphabet in int number (based on ASCII coding)
        index_col = ord(frame_target[i])-97
        matrix[index_row,index_col] += weight
    return matrix



def calulate_mi(px, py, pxy):
    """calculate the mutual information between to matrix:

    - px (matrix) : probability matrix for the i index
    - py (matrix): probalbity matrix or i+n index
    - pxy (matrix): probability 

    return (matrix): mutual information of probability matrixes
    """
    size = len(px)
    mi = 0
    for i in range(0,size):
        for j in range(0,size):
            if pxy[i,j] != 0: #exclude the division by 0
                mi += pxy[i,j] * math.log2(pxy[i,j]/(px[i]*py[j]))
    if mi > 0:
        return mi
    else:
        return 0            

def calculate_joint_entropy(pxy):
    """Calculate the joint entropy with the probability matrix:

    - pxy (matrix): probability

    return (matrix): joint entropy of probability 
    """
    size = len(pxy)
    joint_entropy = 0
    for i in range(0,size):
        for j in range(0,size):
            if pxy [i,j] !=0:
                joint_entropy -= pxy[i,j] * math.log2(pxy[i,j])
    if joint_entropy != 0: #exclude the division by 0
        return joint_entropy
    else:
        return 0

def calculate_eemi(bxy, bx, by, n):
    """Calculate the expected error of the mutual information
    - bxy (float): count of probability different to zero in matrix pxy
    - bx (float): count of probability different to zero in matrix pxy
    - bx (float): count of probability different to zero in matrix pxy
    - n (int): size of the matrix of probability, or number of fragments in the original sequence

    return (float): expected error of the mutual information
    """
    return (bxy - bx - by + 1)/(2 * n)


class Fasta:
    """Class of object fasta type

    Permit the parse of fasta into python (only the sequences) in the form of an matrix array 
    and the transposition of this matrix for have the frames in lines
    
    """
    def __init__(self, file_name):
        fasta_file = open(file_name)
        allSeqs = []
        for seq_record in SeqIO.parse(fasta_file, """fasta"""):
            allSeqs.append(seq_record.seq)
        self.pb_seq = np.array(allSeqs)

    def get_transpose(self):
        sequences = self.pb_seq.transpose()
        sequences = sequences[2:-2]
        return sequences
