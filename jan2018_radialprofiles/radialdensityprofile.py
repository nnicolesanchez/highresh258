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

p_clumpy = pynbody.analysis.profile.Profile(h1.g[h1_clumpy_mask])
p_cold   = pynbody.analysis.profile.Profile(h1.g[h1_cold_mask])
p_shock  = pynbody.analysis.profile.Profile(h1.g[h1_shock_mask])


plt.plot(p_shock['rbins'],p_shock['density']/np.max(p_shock['density']), color='Red',label='Clumpy, Max Density ='+str("%.4g" % np.max(p_shock['density'])))
plt.plot(p_cold['rbins'],p_cold['density']/np.max(p_cold['density']), color='Blue',label='Cold, Max Density ='+str("%.4g" % np.max(p_cold['density'])))
plt.plot(p_clumpy['rbins'],p_clumpy['density']/np.max(p_clumpy['density']), color='Green',label='Shocked, Max Density ='+str("%.4g" % np.max(p_clumpy['density'])))
plt.ylabel('Normalized Radial Density Profile of Gas in Main Halo')
plt.xlabel('R [kpc]')
plt.legend()
plt.savefig('radialdensityprofile.pdf')
plt.show()
