# Test threading

import time
import threading as td
import Queue as Q
import numpy as np

def Td (Na):
  while(1):
    while not Na.empty():
      Na = Na.get()
      print(Na, '!!')
      if (Na == 'c'):
        print('Td_End')
    time.sleep(1)
    print('Td_run')

if (__name__  == '__main__'):
  try:
    Na = Q.Queue()
    T = td.Thread(target = Td , args = (Na, ))
    T.setDaemon(True)
    T.start()

    while(__name__ == '__main__'):
      N =  raw_input('Stop:');
      print(N)
      Na.put(N)
      if (N == 'N'):
        break

  finally:
#    Na.put('c')
    print('End')
