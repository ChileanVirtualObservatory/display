import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import display.create_cube
import display.create_words
import display.script_spams

# Dictionary of molecules and its respective isotopes.
molist = {
            'CO' : ('COv=0','COv=1','13COv=0','C18O','C17O','13C17O','13C18O'),
            # Carbon Monoxide

            # 'NH2' : ('NH2'), # Amidogen

            'N2H' : ('N2H+v=0', 'N2D+', '15NNH+', 'N15NH+'), # Diazenylium

            'CN' : ('CNv=0', '13CN', 'C15N'), # Cyanide Radical

            'HCN' : ('HCNv=0', 'HCNv2=1', 'HCNv2=2','HCNv3=1', 'HC15Nv=0',
                     'H13CNv2=1', 'H13CNv=0', 'HCNv1=1', 'HCNv3=1', 'DCNv=0',
                     'DCNv2=1', 'HCNv2=4', 'HCNv2=1^1-v2=4^0'),
            # Hydrogen Cyanide

            # 'H2CN' : ('H2CN'), # Methylene amidogen

            'CS' : ('CSv=0', '13C34Sv=0', 'C36Sv=0', 'C34Sv=0', 'CSv=1-0',
                    '13CSv=0', 'C33Sv=0', 'CSv=1', 'C34Sv=1'),
            # Carbon Monosulfide

            'CCS' : ('CCS', 'C13CS', '13CCS', 'CC34S'), # Thioxoethenylidene

            'H2S' : ('H2S', 'H2S', 'H234S', 'D2S'), # Hydrogen sulfide

            'H2CS' : ('H2CS', 'H213CS', 'H2C34S'), # Thioformaldehyde

            'SO2' : ('SO2v=0', '33SO2', '34SO2v=0', 'SO2v2=1'),
            # Sulfur Dioxide

            'OSO' : ('OS18O', 'OS17O'),# Sulfur Dioxide

            'H2CO' : ('H2CO', 'H2C18O', 'H213CO'), # Formaldehyde

            'HCO' : ('HCO+v=0', 'HC18O+', 'HC17O+', 'H13CO+'), # Formylium

            # 'HC3N' : ('HC3Nv=0'), # Cyanoacetylene

            'HC5N' : ('HC5Nv=0', 'HC5Nv11=1', 'HCC13CCCN', 'HCCCC13CN',
                      'HCCC13CCN', 'H13CCCCCN', 'HC13CCCCN'), # Cyanobutadiyne

            'CH3OH' : ('CH3OHvt=0', '13CH3OHvt=0', 'CH318OH', 'CH3OHvt=1',
                       '13CH3OHvt=1') # Methanol
          }

# if __name__ == "__main__":


# Subset of molist to use in the simulation to generate spectral lines
#
#       @Test: Isotopes with theoretical lines on the Band 9 (602 - 720 Ghz),
#       in a sample of 4 Ghz with resolution 1 Mhz, Sample: [602 - 606]
#       HC15Nv=0
#       H13CNv2=1
#       H13CNv=0
#       H213CS
#       H2C34S
#       SO2v=0
#       33SO2
#       34SO2v=0
#       SO2v2=1
#       OS18O
#       OS17O
#       H2C18O
#       H213CO
#       13CH3OHvt=0
#       CH3OHvt=1
#       13CH3OHvt=1
#


# Function to create a fit containing an observed object (a Datacube
# ALMA-like) using ASYDO Project. Parameters:
#
#         - isolist     : list subset of the list of isotopes to generate a cube
#         - cube_name    : filename of the .fits generated by the simulation
#         - cube_params : parameters for the simulation of the cube


isolist = set(['HC15Nv=0', 'H13CNv2=1', 'H13CNv=0'])
cube_name = 'observed_cube'
#         Creation of a Data cube that needs the following parameters:
#
#         - freq    : spectral center (frequency)
#         - alpha   : right-ascension center
#         - delta   : declination center
#         - spe_res : spectral resolution
#         - spe_bw  : spectral bandwidth
#         - s_f     : the width of the spectral lines (fwhm)
cube_params = {
  'freq'     : 604000,
  'alpha'    : 0,
  'delta'    : 0,
  'spe_bw'   : 4000,
  'spe_res'  : 1,
  's_f'      : 85
              }
# display.create_cube.gen_cube(isolist, cube_params, cube_name)


# Function to create the words necessary to fit a sparse coding model
# to the observed spectra in the previous created cube. It uses:
#
#         - freq    : spectral center (frequency)
#         - spe_res : spectral resolution
#         - spe_bw  : spectral bandwidth
#         - s_f     : the width of the spectral lines (fwhm)
# Returns a DataFrame with a vector for each theoretical line for each isotope
# in molist
D = display.create_words.gen_words(molist, cube_params)











