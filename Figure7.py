#%% PROPERTIES
##  DATE:    27/07/2022
##  AUTHOR:  GIOVANNI MOTTOLA

#%% CLEAN WORKSPACE
from assort_usef_func import cleanup
cleanup()

#%% IMPORTS
# -*- coding: utf-8 -*-
from pynomo.nomographer import *
from pyx import text

#%% MAIN BLOCK
#   contact force P [N]
P_params={
        'u_min':1.0,
        'u_max':1200.0,
        'function':lambda P:P,
        'title':r'$P$ [N]',
        'tick_levels':3,
        'tick_text_levels':1,
        'tick_side':'left',
        'text_format':r"$%3.0f$",
        }

#   maximum contact stress sigma_c [MPa]
s_params={
        'u_min':300.0,
        'u_max':1050.0,
        'function':lambda s:(s/0.616)**3,
        'title':r'$\sigma_c$ [MPa]',
        'tick_levels':3,
        'tick_text_levels':1,
        'tick_side':'right',
        'title_x_shift':1,
        'text_format':r"$%3.0f$",
        }

#   harmonic mean K_D of sphere diameters [mm]
K_params={
        'u_min':5.0,
        'u_max':100.0,
        'function':lambda K:K**2,
        'title':r'$K_D$ [mm]',
        'tick_levels':3,
        'tick_text_levels':1,
        'tick_side':'right',
        'title_opposite_tick':False,
        }
                
#   Young's modulus E [MPa]
E_params={
        'u_min':45000.0,
        'u_max':206000.0,
        'function':lambda E:E**2,
        'title':r'$E$ [MPa]',
        'tick_levels':3,
        'tick_text_levels':1,
        'tick_side':'left',
        'title_x_shift':-9.5,
        'title_opposite_tick':False,
        'text_format':r"$%3.0f$",
        }
 
block_1_params={
        'block_type':'type_4',
        'f1_params':P_params,
        'f2_params':s_params,
        'f3_params':K_params,
        'f4_params':E_params,
        'isopleth_values':[[1100,1000,'x',120000]],
        }
                             
#%% GLOBAL SETTINGS
main_params={
        'filename':'Figure7.pdf',
        'paper_height':10.0,
        'paper_width':10.0,
        'block_params':[block_1_params],
        'transformations':[('rotate',0.01),('scale paper',)],
        'title_str':r'$\sigma_c=0.616^3\sqrt{{PE^2}\over{K_D^2}}$',
        'title_x':4.0,
        'title_y':8.0,
        }

Nomographer(main_params)
print('\a')