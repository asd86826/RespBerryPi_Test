# Test threading

import time
import threading as td
import Queue as Q
import numpy as np

def Td (Na) :
  while(__name__ == '__main__'):
    Na = Na.get()
    if ( Na == 'c' ):
      time.sleep(1)
      print('true')
      break

Na = Q.Queue()
T = td.Thread(target = Td , args = ( Na,))
T.start()

while(__name__ == '__main__'):
  N =  raw_input('Stop:');
  print(N)
  Na.put(N)
  if ( N == 'Y' ):
    T.start()
  elif( N == 'N' ):
    break
