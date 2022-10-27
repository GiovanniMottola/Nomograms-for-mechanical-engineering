#%% PROPERTIES
##  DATE:    04/12/2021
##  AUTHOR:  GIOVANNI MOTTOLA

#%% CLEAN WORKSPACE
from assort_usef_func import cleanup
cleanup()

#%% IMPORTS
# -*- coding: utf-8 -*-
from pynomo.nomographer import *
from pyx import text
T0=text.size.huge;
T1=text.size.LARGE;

#%% MAIN BLOCK
#   stiffness k_1 of spring 1 [N/m]
k1_params={
        'u_min':5000.0,
        'u_max':50000.0,
        'function':lambda k1:k1,
        'title':r'\huge $k_1 \left[{\rm{N} \over \rm{m}}\right]$',
        'title_x_shift':-1,
        'title_y_shift':0.5,
        'tick_levels':4,
        'tick_text_levels':1,
        'text_format':r"$%3.0f$",
        'text_size_0': T0,
        }

#   stiffness k_2 of spring 2 [N/m]
k2_params={
        'u_min':5000.0,
        'u_max':50000.0,
        'function':lambda k2:k2,
        'title':r'\huge $k_2 \left[{\rm{N} \over \rm{m}}\right]$',
        'title_x_shift':-1,
        'title_y_shift':0.5,
        'tick_levels':4,
        'tick_text_levels':1,
        'text_format':r"$%3.0f$",
        'text_size_0': T0,
        }

#   stiffness k_eq of equivalent spring [N/m]
ke_params={
        'u_min':5000.0,
        'u_max':50000.0,
        'function':lambda ke:ke,
        'title':r'\huge $k_{eq} \left[{\rm{N} \over \rm{m}}\right]$',
        'title_x_shift':-1,
        'title_y_shift':0.5,
        'tick_levels':4,
        'tick_text_levels':1,
        'text_format':r"$%3.0f$",
        'text_size_0': T0,
        }

block_keq_params={
        'block_type':'type_7',
        'height':17.25,
        'width':30.0,
        'f1_params':k1_params,
        'f2_params':k2_params,
        'f3_params':ke_params,
        'angle_u':60.0,
        'angle_v':60.0,
        'isopleth_values':[[45000,30000,'x']],
        }

#%% GLOBAL SETTINGS
main_params={
        'filename':'Figure6.pdf',
        'paper_height':17.25,
        'paper_width':30.0,
        'block_params':[block_keq_params],
        'transformations':[('rotate',0.01),('scale paper',)],
        'title_y':17,
        'title_str':r'\huge ${1 \over k_{eq}} = {1 \over k_1}+{1 \over k_2}$',
        }

Nomographer(main_params)
print('\a')