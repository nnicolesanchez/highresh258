# This script reads in the positions of the halos and the distances
# of what we think are our possible main BHs. We want to determine 
# which BH to trace before timestep 360 (at which point BH282 is 
# clearly the main BH in Halo 1) by seeing which BH remains the most 
# central and/or most massive. 

# Important notes:
# filename.shrinkcenter files hold the positional data for halos
# bh.sav holds positional data for BHs


# Vanderbilt Univ.  -- VPAC40:  
#           /astro1/nicole/highresh258/latez_closestbh_BH282orBH283.py 
# N. Nicole Sanchez -- January 27, 2016
import matplotlib.pyplot as plt
import pynbody as pyn
import pyfits  as pyf
import numpy   as np
import scipy.io 

#dKpcUnit = 50000.

# For BH282
filein    = np.loadtxt('haloid.43553282.dat',dtype='str',unpack=True)
timesteps = filein[0]
ts_number = np.loadtxt('timesteps.list',unpack=True)
ts_zto5_num   = ts_number[2:15]
#halo      = filein[1] # Don't need this bc may change based on this result
print len(timesteps)
ts_zto5   = timesteps[0:13]
print ts_zto5
print ts_zto5_num

bhhalo = scipy.io.readsav('bhhalo.sav', verbose=True)
#print bhhalo
data = bhhalo['bhhalo']
data.dtype.fields


halo1_ts_array = []
halo1_x_array  = []
halo1_y_array  = []
halo1_z_array  = []

halo2_ts_array = []
halo2_x_array  = []
halo2_y_array  = []
halo2_z_array  = []

# BH282 is number 0 in bh.sav and BH 
BH_282 = 0
BH_283 = 3
bhs_of_interest = [BH_282,BH_283]

bh282_x_array = []
bh282_y_array = []
bh283_x_array = []
bh283_y_array = []
#quit()
# Gonna do this for the first 14 timesteps [0,13] (so to z~5, when BH283 disappears)
for i in range(0,len(ts_zto5)):
    halodist     = np.loadtxt(timesteps[i]+'.shrinkcenters',dtype='str',skiprows=1,unpack=True)
    halo1_ts = halodist[0][0]
    halo1_x  = halodist[1][0]
    halo1_y  = halodist[2][0]
    halo1_z  = halodist[3][0]

    halo1_ts_array.append(halo1_ts)
    halo1_x_array.append(halo1_x * dKpc)
    halo1_y_array.append(halo1_y * dKpc)
    halo1_z_array.append(halo1_z * dKpc)

    halo2_ts = halodist[0][1]
    halo2_x  = halodist[1][1]
    halo2_y  = halodist[2][1]
    halo2_z  = halodist[3][1]

    halo2_ts_array.append(halo2_ts)
    halo2_x_array.append(halo2_x * dKpc)
    halo2_y_array.append(halo2_y * dKpc)
    halo2_z_array.append(halo2_z * dKpc)

    #for j in range(0,len(bhs_of_interest)):
    #data['field'][bh number in created order][timestep]
    bhiord = data['bhiord'][BH_282][i]
    bhmass = data['mass'][BH_282][i]
    bhhalo = data['haloid'][BH_282][i]
    bh282_x   = data['x'][BH_282][i]
    bh282_y   = data['y'][BH_282][i]
        
    bh282_x_array.append(bh282_x * dKpc)
    bh282_y_array.append(bh282_y * dKpc)

    bhiord = data['bhiord'][BH_283][i]
    bhmass = data['mass'][BH_283][i]
    bhhalo = data['haloid'][BH_283][i]
    bh283_x   = data['x'][BH_283][i]
    bh283_y   = data['y'][BH_283][i]

    bh283_x_array.append(bh283_x * dKpc)
    bh283_y_array.append(bh283_y * dKpc)
    
    print ts_zto5[i]
    plt.plot(halo1_x_array,halo1_y_array,'o',color='Red',ms=7)
    plt.plot(halo2_x_array,halo2_y_array,'o',color='Salmon',ms=7)
    plt.plot(bh282_x_array,bh282_y_array,'o',color='Blue',ms=7)
    if i != 0 :
        plt.plot(bh283_x_array[1:],bh283_y_array[1:],'o',color='Green',ms=7)
    plt.xlim(-0.01,0.03)
    plt.ylim(-0.02,0.02)

    plt.text(0.015,0.01,'Timestep = '+str(ts_zto5_num[i]))
    plt.text(0.015,0.008,'Main Halo',color='Red')
    plt.text(0.015,0.006,'Halo 2',color='Salmon')
    plt.text(0.015,0.004,'BH282',color='Blue')
    plt.text(0.015,0.002,'BH283',color='Green')
    plt.savefig('halo_position_'+str(i)+'.ps')
    plt.show()


