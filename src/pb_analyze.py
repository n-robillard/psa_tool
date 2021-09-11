#TODO: change name of varaibles for make it more clear and explicate the code

import numpy as np

def transition_count_(data):
    matrix_global=[]
    for i in range(0,len(data)):
        matrix_global.append(analyse_row(data[i]))
    return matrix_global

def analyse_row(row):
    matrix= np.zeros((16,16))
    for i in range(0,len(row)-1):
        index_row = ord(row[i])-97
        index_col = ord(row[i+1])-97
        matrix[index_row,index_col] += 1
    return matrix

def prorata_global(transition_matrix):
    transition_ratio = []
    for i in range(0,len(transition_matrix)):
        transition_ratio.append(prorata_sequence(transition_matrix[i]))
    return transition_ratio

def prorata_sequence(transition_item):
    result = np.zeros((3,3))
    for i in range(0,len(transition_item)):
        result[i] = prorata_row(transition_item[i])
    return result
    
def prorata_row(row):
    sum_row = row.sum()
    result= np.zeros((3))
    for i in range(0,len(row)):
        if sum_row > 0 :
            result[i]=row[i]/sum_row
    return result



#TODO : make this code in forms, check if this can work with a list of matrix

from numpy  import array, shape, where, in1d
import math
import time

class InformationTheoryTool:
    
    def __init__(self, data):
        """
        """
        # Check if all rows have the same length
        assert (len(data.shape) == 2)
        # Save data
        self.data = data
        self.n_rows = data.shape[0]
        self.n_cols = data.shape[1]
        
        
    def single_entropy(self, x_index, log_base, debug = False):
        """
        Calculate the entropy of a random variable
        """
        # Check if index are into the bounds
        assert (x_index >= 0 and x_index <= self.n_rows)
        # Variable to return entropy
        summation = 0.0
        # Get uniques values of random variables
        values_x = set(data[x_index])
        # Print debug info
        if debug:
            print('Entropy of')  
            print(data[x_index])
        # For each random
        for value_x in values_x:
            px = shape(where(data[x_index]==value_x))[1] / self.n_cols
            if px > 0.0:
                summation += px * math.log(px, log_base)
            if debug:
                print( '(%d) px:%f' % (value_x, px))
        if summation == 0.0:
            return summation
        else:
            return - summation
        
        
    def entropy(self, x_index, y_index, log_base, debug = False):
        """
        Calculate the entropy between two random variable
        """
        assert (x_index >= 0 and x_index <= self.n_rows)
        assert (y_index >= 0 and y_index <= self.n_rows)
        # Variable to return MI
        summation = 0.0
        # Get uniques values of random variables
        values_x = set(data[x_index])
        values_y = set(data[y_index])
        # Print debug info
        if debug:
            print('Entropy between')
            print(data[x_index])
            print(data[y_index])
        # For each random
        for value_x in values_x:
            for value_y in values_y:
                pxy = len(where(in1d(where(data[x_index]==value_x)[0], 
                                where(data[y_index]==value_y)[0])==True)[0]) / self.n_cols
                if pxy > 0.0:
                    summation += pxy * math.log(pxy, log_base)
                if debug:
                    print( '(%d,%d) pxy:%f' % (value_x, value_y, pxy))
        if summation == 0.0:
            return summation
        else:
            return - summation
        
        
        
    def mutual_information(self, x_index, y_index, log_base, debug = False):
        """
        Calculate and return Mutual information between two random variables
        """
        # Check if index are into the bounds
        assert (x_index >= 0 and x_index <= self.n_rows)
        assert (y_index >= 0 and y_index <= self.n_rows)
        # Variable to return MI
        summation = 0.0
        # Get uniques values of random variables
        values_x = set(data[x_index])
        values_y = set(data[y_index])
        # Print debug info
        if debug:
            print( 'MI between')
            print(data[x_index])
            print(data[y_index])
        # For each random
        for value_x in values_x:
            for value_y in values_y:
                px = shape(where(data[x_index]==value_x))[1] / self.n_cols
                py = shape(where(data[y_index]==value_y))[1] / self.n_cols
                pxy = len(where(in1d(where(data[x_index]==value_x)[0], 
                                where(data[y_index]==value_y)[0])==True)[0]) / self.n_cols
                if pxy > 0.0:
                    summation += pxy * math.log((pxy / (px*py)), log_base)
                if debug:
                    print('(%d,%d) px:%f py:%f pxy:%f' % (value_x, value_y, px, py, pxy))
        return summation

#TODO: write a code for calculate the expected error -> B(x,y) - Bx - By +1 / 2N where to B(x,y), Bx and By are the count of non zero in the variable x,y x&y ; and N the sample size
