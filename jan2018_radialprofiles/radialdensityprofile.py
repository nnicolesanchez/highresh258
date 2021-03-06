# This script makes radial profiles for the gas in h258 at z=0
# split into the differnt types of gas: clumpy, shocked, cold


# Vanderbilt Univ.  -- VPAC40:  /astro1/nicole/lowresh258/angmom.p
# N. Nicole Sanchez -- January 15, 2018
import matplotlib.pyplot as plt
import pyfits  as pyf
import numpy   as np
import pynbody

densunit = 147.8344
lunit    = 50000.     #Kpc

h1_iords_all      = pyf.getdata('../grp1.allgas.iord.fits')    # all gas IDs ending in MH
h1_iords_clumpy   = pyf.getdata('../../newgastracingfiles/newnew/clumpy.accr.iord.fits')    # all clumpy gas IDs
h1_iords_smooth   = pyf.getdata('../../newgastracingfiles/newnew/smooth.accr.iord.fits')
h1_iords_shock    = pyf.getdata('../../newgastracingfiles/newnew/shocked.iord.fits')
h1_iords_cold  = pyf.getdata('../../newgastracingfiles/newnew/unshock.iord.fits')           # aka "unshocked" 
#h1_iords_early    = pyf.getdata('../../newgastracingfiles/newnew/early.iord.fits')         # all early gas IDs (in MH)
#h1_accrz          = pyf.getdata('../../newgastracingfiles/newnew/grp1.accrz.fits')

sim = pynbody.load('../h258.cosmo50cmb.3072gst10bwepsK1BHC52.004096/h258.cosmo50cmb.3072gst10bwepsK1BHC52.004096')
sim.physical_units()
h = sim.halos()
h1 = h[1]
pynbody.analysis.angmom.faceon(h1)
print(h1_iords_clumpy[0:100])

h1_clumpy_mask = np.in1d(h1.g['iord'],h1_iords_clumpy) 
h1_cold_mask   = np.in1d(h1.g['iord'],h1_iords_cold)
h1_shock_mask  = np.in1d(h1.g['iord'],h1_iords_shock)

p_clumpy = pynbody.analysis.profile.Profile(h1.g[h1_clumpy_mask],min=0.3,type='log',nbins=50)
p_cold   = pynbody.analysis.profile.Profile(h1.g[h1_cold_mask],min=0.3,type='log',nbins=50)
p_shock  = pynbody.analysis.profile.Profile(h1.g[h1_shock_mask],min=0.3,type='log',nbins=50)

print(p_clumpy['rbins'][0:10],p_clumpy['rbins'].units)

total = p_clumpy['density']+p_cold['density']+p_shock['density']
print('Total array should be an array',total)
# Normalized
plt.plot(np.log10(p_clumpy['rbins']),p_clumpy['density']/total,color='Green',label='Clumpy')
plt.plot(np.log10(p_cold['rbins']),p_cold['density']/total, color='Blue',label='Cold')
plt.plot(np.log10(p_shock['rbins']),p_shock['density']/total, color='Red',label='Shocked')

plt.ylabel('Radial Density Profile')
plt.xlabel('log(R) [kpc]')
plt.legend()
plt.savefig('radialdensityprofile.pdf')
plt.show()


# Ratios 
#plt.plot(np.log10(p_clumpy['rbins']),p_clumpy['mass']/np.sum(h1.g['mass']), color='Green',label='Clumpy')
#plt.plot(np.log10(p_cold['rbins']),p_cold['mass']/np.sum(h1.g['mass']), color='Blue',label='Cold')
#plt.plot(np.log10(p_shock['rbins']),p_shock['mass']/np.sum(h1.g['mass']), color='Red',label='Shocked')

#plt.ylabel('Mass Fraction Profile of Gas in Main Halo')
#plt.xlabel('log(R) [kpc]')
#plt.legend()
#plt.savefig('massfractionprofile.pdf')
#plt.show()
