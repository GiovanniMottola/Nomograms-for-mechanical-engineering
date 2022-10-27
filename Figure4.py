#%% PROPERTIES
##  DATE:    29/11/2021
##  AUTHOR:  GIOVANNI MOTTOLA

#%% CLEAN WORKSPACE
from assort_usef_func import cleanup
cleanup()

#%% IMPORTS
# -*- coding: utf-8 -*-
from pynomo.nomographer import *
from numpy import log, pi, sqrt
from pyx import text
T0=text.size.huge;
T1=text.size.LARGE;

#%% MAIN BLOCK
#   number of oscillations n [-]
n_params={
        'u_min':1.0,
        'u_max':10.0,
        'function':lambda n:log(n),
        'title':r'\huge $n$',
        'title_x_shift':-1,
        'title_y_shift':0.5,
        'tick_levels':1,
        'tick_text_levels':1,
        'text_horizontal_align_center':True,
        'text_size_0': T0,
        }

#   logarithmic decrement delta_n [-]
d_params={
        'u_min':0.4409,
        'u_max':47.2,
        'function':lambda d:log(2*pi)-log(d),
        'title':r'$\huge \delta_n $',
        'title_x_shift':-1,
        'title_y_shift':0.5,
        'tick_levels':4,
        'tick_text_levels':2,
        'text_horizontal_align_center':True,
        'text_size_0': T0,
        'text_size_1': T1,
        }

#   damping coefficient zeta [-]
z_params={
        'u_min':0.07,
        'u_max':0.6,
        'function':lambda z:log(z/sqrt(1-z**2)),
        'title':r'\huge $\zeta$',
        'title_x_shift':-1,
        'title_y_shift':0.5,
        'tick_levels':4,
        'tick_text_levels':2,
        'text_horizontal_align_center':True,
        'text_size_0': T0,
        'text_size_1': T1,
        }

block_z_params={
        'block_type':'type_1',
        'width':10.0,
        'height':10.0,
        'f1_params':n_params,
        'f2_params':d_params,
        'f3_params':z_params,
        'isopleth_values':[[3,'x',0.4]],
        }

#%% GLOBAL SETTINGS
main_params={
        'filename':'Figure4.pdf',
        'paper_height':10.0,
        'paper_width':30.0,
        'block_params':[block_z_params],
        'transformations':[('rotate',90),('scale paper',)],
        'title_y':11,
        'title_str':r'\huge $\delta_n = {{2 \pi n \zeta}\over{\sqrt{1-\zeta^2}}} $',
        }

Nomographer(main_params)
print('\a')