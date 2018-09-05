#Test daynamic Variable

import time
import numpy as np


def Job_DV (j):
  for i in range(1,j+1):
    locals()["Var%s"%i] = 0
    print ("Var%s = 0"%i )

if __name__ == '__main__' :
  J = raw_input('input:')
  Job_DV(int(J))
  print('End')
