#%% PROPERTIES
##  DATE:    10/02/2021
##  AUTHOR:  GIOVANNI MOTTOLA

#%% CLEAN WORKSPACE
from assort_usef_func import cleanup
cleanup()

#%% IMPORTS
# -*- coding: utf-8 -*-
from pynomo.nomographer import *
from numpy import *

#%% MAIN BLOCK 1 (LEFTMOST NOMOGRAM)
#   number of pistons Z [-]
Z_params={
        'u_min':1.0,
        'u_max':15.0,
        'function':lambda Z:Z,
        'title':r'$Z$',
        'tick_levels':1,
        'tick_text_levels':1,
        'tick_side':'left',
        'scale_type':'linear smart'
        }

#   piston diameter d [mm]
d_params={
        'u_min':10,
        'u_max':30.0,
        'function':lambda d:1.0/d**2,
        'title':r'$d$ [mm]',
        'tick_levels':4,
        'tick_text_levels':1,
        'tick_side':'left',
        'scale_type':'linear smart',
        'title_y_shift':0.75
        }
 
#   total piston cross section area A [mm^2], first intermediate result
r_params={
        'u_min':70,
        'u_max':11000,
        'function':lambda r:r*4/pi,
        'title':r'',
        'tick_levels':0,
        'tick_text_levels':0,
        'tag':'r'
        }
 
block_params_1={
        'block_type':'type_2',
        'width':30.0,
        'height':20.0,
        'f1_params':Z_params,
        'f2_params':d_params,
        'f3_params':r_params
        }

#%% MAIN BLOCK 2 (CENTER NOMOGRAM)
#   total piston cross section area A [mm^2], first intermediate result
r_params_2={
        'u_min':70,
        'u_max':11000,
        'function':lambda r:r,
        'title':r'',
        'tick_levels':0,
        'tick_text_levels':0,
        'tag':'r'
        }

#   diameter D of circle across piston axes [mm]
D_params={
        'u_min':20,
        'u_max':150,
        'function':lambda D:1.0/D,
        'title':r'$D$ [mm]',
        'tick_levels':4,
        'tick_text_levels':2,
        'title_y_shift':1,
        'scale_type':'linear smart'
        }

#   displacement V0 at alpha=45° [mm^3], second intermediate result
q_params={
        'u_min':1400,
        'u_max':1650000,
        'function':lambda u:u,
        'title':r'',
        'tick_levels':0,
        'tick_text_levels':0,
        'tag':'q'
        }
 
block_params_2={
        'block_type':'type_2',
        'width':30.0,
        'height':20.0,
        'f1_params':r_params_2,
        'f2_params':D_params,
        'f3_params':q_params,
        'mirror_x':True
        }
              
#%% MAIN BLOCK 3 (RIGHTMOST NOMOGRAM)
#   displacement V0 at alpha=45° [mm^3], second intermediate result
q_params_2={
        'u_min':1400,
        'u_max':1650000,
        'function':lambda u:u,
        'title':r'',
        'tick_levels':0,
        'tick_text_levels':0,
        'tag':'q'
        }

#   swashplate inclination angle alpha [°]
alpha_params={
        'u_min':0.05,
        'u_max':25,
        'function':lambda a:1.0/tan(radians(a)),
        'title':r'$\alpha\,[^\circ]$',
        'tick_levels':4,
        'tick_text_levels':2,
        'tick_side':'left',
        'scale_type':'linear smart',
        'title_x_shift':-1
        }

#   total pump displacement V per rotation [cm^3]
V_params={
        'u_min':0.0,
        'u_max':800,
        'function':lambda V:V*1000,
        'title':r'$V\,[\rm{cm}^3]$',
        'tick_levels':4,
        'tick_text_levels':2,
        'title_x_shift':1,
        'text_format':r"$%3.0f$"
        }

block_params_3={
        'block_type':'type_2',
        'width':30.0,
        'height':20.0,
        'f1_params':q_params_2,
        'f2_params':alpha_params,
        'f3_params':V_params,
        'mirror_x':False
        }
 
#%% GLOBAL SETTINGS
main_params={
        'filename':'Figure8.pdf',
        'paper_width':35.0,
        'paper_height':25.0,
        'block_params':[block_params_1,block_params_2,block_params_3],
        'transformations':[('rotate',0.01),('scale paper',)],
        'title_str':r'$V=Z {\pi d^2 \over 4} D \rm{tan}\,\alpha$'
        }
        
Nomographer(main_params)
print('\a')