# This script opens and examines the files within:
#       /astro1/nicole/highresh258/orbitfiledata 

# Vanderbilt Univ.  -- VPAC40:  /astro1/nicole/highresh258/orbittesting.py
# N. Nicole Sanchez -- October 16, 2016 
import matplotlib.pyplot as plt
import pyfits as pyf
import numpy as np
import cPickle
import math
import gc

thing282 = pyf.getdata('orbitfiledata/43553282.fits')
print thing282.dtype.names

thing282['time']
print len(thing282['time'][0])




