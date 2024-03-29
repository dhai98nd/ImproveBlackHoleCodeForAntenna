import sys
sys.path.append(r"C:\Program Files (x86)\CST Studio Suite 2020\AMD64\python_cst_libraries")
import cst
import cst.interface
import cst.results
import numpy as np
import time
import shutil
import random
import Antenna_cross_pixel_multiband
import IBH_multiband 
#
# mycst = cst.interface.DesignEnvironment()
# myproject = cst.interface.DesignEnvironment.open_project(mycst,r'E:\Master\Python_code\ANTENNA\2_4.cst')


# % *************************** %
# % ** ALGORITHM’S VARIABLES ** %
# % *************************** %
np.set_printoptions(threshold=np.inf)

num_stars = 50 # size of population
# n=4     # dimension of problem 
max_iter = 10 # number of generations

#---------Boundary-------

pixel_max_x = 75
pixel_max_y = 45

ibh = IBH_multiband.ImprovedBlackHole(num_stars, pixel_max_x, pixel_max_y, max_iter)
best_value = ibh.run()
# % *********************** %
# % ** CREATE POPULATION ** %
# % *********************** %
print("Improved Black Hole Algorithm: Maximum Optimization")
# print("Max Location: %s" % (max_values_loc))
print("Best Star Location: " + str(best_value.location))
print("Best Star Fitness Value:" + (str(best_value.fitval)))
# print(ObjValue)