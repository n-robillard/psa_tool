from Bio import SeqIO
import numpy as np

pathToFile = open("./data/sequences.PB.fasta")

def parse_fasta(pathToFile):
    allSeqs = []
    for seq_record in SeqIO.parse(pathToFile, """fasta"""):
            allSeqs.append(seq_record.seq)
    pb_seq = np.array(allSeqs)
    return pb_seq

def transpose_fasta(sequences):
    pb_seq = pb_seq.transpose()
