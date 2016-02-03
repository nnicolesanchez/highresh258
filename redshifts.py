#Usage:
#rtipsy(filename, VERBOSE=False)        
#Input parameters:                                                            
#filename  filename string
#VERBOSE  print messages (optional)
#Return values:
#(header,g,d,s)
#header    tipsy header struct
#g,d,s     gas, dark and star structures
#Please read rtipsy.py for the structure definitions
#Example:
#h,g,d,s = rtipsy('/home/wadsley/usr5/mihos/mihos.std')
#print, h['ndark']
#plt.plot(d['x'], d['y'], 'k,')"""


execfile('./pytipsy.py')
ts_directs  = np.loadtxt('./timestep_directories.list',dtype=str,unpack=True)
ts_numbers  = np.loadtxt('./timesteps.list',unpack=True)

#redshifts   = ['Redshift'] 
redshifts   = []
number      = []
for i in range(0,len(ts_numbers)):
    #ts_directs = str(ts_directs[i])
    #print ts_directs[i]
    ts_n = float(ts_numbers[i])
    h,g,d,s    = rtipsy(ts_directs[i],VERBOSE=False)
    a = h['time']
    z = (1./a) - 1.
    z = float(z)
    number.append(ts_n)
    redshifts.append(z)
    round(redshifts[i], 5)
    print(number[i],redshifts[i])

#ts_numbers_label = ['Timestep']
#ts_numbers_label.append(ts_numbers)
#redshifts = np.array(redshifts)
np.savetxt('./ts_redshifts.dat', np.transpose([ts_numbers,redshifts]))
#np.savetxt('./redshifts.dat',redshifts)
