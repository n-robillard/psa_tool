"""
Main program of "psa_tool"

==============================================================================

Author : Robillard Nicolas, nicolas.robillard@ymail.com

In this program, we have the implementation of the calcul of trajectories by 
PBxplore and the statistic analyze provide by GSA-tools (Pandini et al, FACEBS J., 2012). This 
program need the specific environnment provide in /src/psa_tool_env.yml in 
the reprository on GitHub

This program was realized as part of master 2 Biology Informatic, dispense at 
the Univeristy Diderot, Paris, France.
"""

import os
from shutil import copyfile
import psa_analyze as psaa
import psa_vizu as psav
import numpy as np

#definition of criteria for PBxplore : the directory of datas, the time start, 
#the time end and the time between steps
dir_name = ""
while dir_name == "":
    temp = input("Name of the directory where sample are stored in \"data\" : ")
    if os.path.exists("./data/"+dir_name):
        dir_name = temp
    else:
        print("Directory doesn't exist !")

files = os.listdir("./data/"+dir_name)
pos = files[0].rfind("_") + 1
file_row = files[0][:pos]
start = int(input("Please enter the time where the analyse start : "))
end = 0
while end <= start:
    end = int(input("Please enter the time where the analyse end : "))
step = int(input("Please, enter the time between every steps : "))
current = start
while current <= end:
    file_name = file_row + str(current) + ".pdb"
    copyfile("./data/"+ dir_name +"/"+ file_name, "./data/temp/" + file_name)
    current += step

# use of PBassign from PBxplore for the calcul of trajectories and his assign
os.system('PBassign -p ./data/temp' + ' -o ./data/sequences')

print("Calculation of local motion correlation ...")
# application of the class Fasta to parse the fasta and transpose it
fasta = psaa.Fasta("./data/sequences.PB.fasta")
fasta_pbs = fasta.get_transpose()

#statistic analyze of the mutual information (mi), the expected error (eemi),
# the joint entropy and the normalized mutual information (normalized_mi)
mi, eemi, joint_entropy, normalized_MI = psaa.stats_analyze(fasta_pbs)

#vizualisation of the normalized mutual information
vizu_nmi = psav.matrix_plot(normalized_MI)

#export as .png of the heatmap
vizu_nmi.get_figure().savefig('./data/normalized_MI.png', bbox_inches='tight')

#export matrix in .txt
jt = np.matrix(joint_entropy)
with open('./data/joint_entropy_matrix.txt','wb') as f:
    for line in jt:
        np.savetxt(f, line, fmt='%.2f')

mim = np.matrix(mi)
with open('./data/mutual_information_matrix.txt','wb') as f:
    for line in mim:
        np.savetxt(f, line, fmt='%.2f')

eemi = np.matrix(eemi)
with open('./data/expected_error_MI_matrix.txt','wb') as f:
    for line in eemi:
        np.savetxt(f, line, fmt='%.2f')

nmim = np.matrix(normalized_MI)
with open('./data/normalized_MI_matrix.txt','wb') as f:
    for line in nmim:
        np.savetxt(f, line, fmt='%.2f')

print("Finish !")