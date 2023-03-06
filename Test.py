import sys
sys.path.append(r"C:\Program Files (x86)\CST Studio Suite 2020\AMD64\python_cst_libraries")
import cst
import cst.interface
import cst.results
import numpy as np
import time
import shutil
import random
import math


arr=np.array([[0,0,1,1,0,1,0,1,0,1,0,1,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,1,1],
 [1,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,1,1,1,1,0,1],
 [0,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0],
 [0,0,0,0,1,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0],
 [1,1,1,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,0,0],
 [0,1,0,0,0,0,1,0,1,1,1,0,0,1,0,0,1,0,0,0,0,1,1,1,0,1,1,0,0],
 [0,1,1,0,1,1,1,1,0,1,0,0,1,0,1,0,0,0,1,1,0,0,0,0,0,1,1,1,0],
 [1,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,1,0,0,1,0,1,1,0,1,1,0,0,0],
 [1,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,1,0,0,0,1,0],
 [0,1,0,0,1,0,0,1,1,1,1,0,0,0,1,0,0,1,1,1,0,1,1,0,0,1,1,0,1],
 [1,1,1,1,1,1,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0,1,1,0],
 [0,1,0,0,0,1,1,0,1,0,0,1,1,0,0,1,1,0,1,1,0,0,1,0,1,0,0,0,0],
 [0,1,0,0,0,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,0,0,1,0,1,1,1,0,0],
 [1,0,0,1,0,1,1,0,0,1,0,1,1,1,0,0,1,1,1,1,0,0,1,0,0,0,1,0,0],
 [1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,0,0,0,0],
 [0,1,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0,0,1,1,0,0],
 [0,1,1,0,0,0,1,1,0,1,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1],
 [0,0,1,0,1,1,1,1,0,0,1,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1],
 [1,0,0,1,0,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,1,1,0,0,0,0,1,0],
 [1,1,0,1,1,1,1,0,1,1,1,1,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,0,0],
 [0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1]])

print(arr)