from Bio import SeqIO
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pb_analyze as pb
from scipy import stats

pathToFile = open("./data/sequences.PB.fasta")

def parse_fasta(pathToFile):
    allSeqs = []
    for seq_record in SeqIO.parse(pathToFile, """fasta"""):
            allSeqs.append(seq_record.seq)
    pb_seq = np.array(allSeqs)
    return pb_seq

def transpose_fasta(sequences):
    sequences = sequences.transpose()
    return sequences


test = parse_fasta(pathToFile)
#print(f"la matrice original est celle-ci : \n {test}")
test1 = transpose_fasta(test)
#print(f"la matrice transposée est celle-ci : \n {test1}")
#shape_array = np.shape(test1)
#print(shape_array)
test2 = test1[2:-2]
#print(f"La matrice trim des 2 premier et 2 derniers éléments : \n {test2}")

MI,eeMI = pb.calculate_MI_global(test2)
print(MI)
print(eeMI)
print(np.shape(MI))