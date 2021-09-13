import os
from shutil import copyfile
import pb_analyze as pb
import pb_vizu as pbv
import numpy as np

dir_name = ""
while dir_name == "":
    temp = input("Name of the directory where sample are stored in \"data\" : ")
    if os.path.exists("../data/"+dir_name):
        dir_name = temp
    else:
        print("Directory doesn't exist !")

files = os.listdir("../data/"+dir_name)
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
    copyfile("../data/"+ dir_name +"/"+ file_name, "../data/temp/" + file_name)
    current += step

os.system('PBassign -p ../data/temp' + ' -o ../data/sequences')
fasta = pb.Fasta("../data/sequences.PB.fasta")
fasta_pbs = fasta.get_transpose()
MI, eeMI, joint_entropy, normalized_MI = pb.calculate_MI_global(fasta_pbs)
vizu_nMI = pbv.matrix_plot(normalized_MI,np.min(normalized_MI),np.max(normalized_MI))
vizu_nMI.get_figure().savefig('normalized_MI.png', bbox_inches='tight')