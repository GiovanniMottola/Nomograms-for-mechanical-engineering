#%% PROPERTIES
##  DATE:    19/04/2022
##  AUTHOR:  Giovanni Mottola

#%% CLEAN WORKSPACE
from assort_usef_func import cleanup
cleanup()

#%% IMPORTS
# -*- coding: utf-8 -*-
from pynomo.nomographer import *
from numpy import *
from pyx import text, color
T0=text.size.large;
T1=text.size.normal;
Tt='\large';
col=color.cmyk.Black;

#%% MAIN BLOCK 1 (LEFT-SIDE NOMOGRAM)
#   string tension T [kgf]
T_params={
        'u_min':5,
        'u_max':9.0,
        'function':lambda T:sqrt(9.80665*T),
        'title':Tt+r'$T$ [kgf]',
        'tick_levels':4,
        'tick_text_levels':2,
        'tick_side':'left',
        'scale_type':'linear smart',
        'text_size_0':T0,
        'text_size_1':T1,
        }

#   string linear density rho [kg/m]
rh_params={
        'u_min':6.*10**(-4),
        'u_max':4*10**(-3),
        'function':lambda rho:sqrt(rho),
        'title':Tt+r'$\rho\,[{\rm{kg} \over \rm{m}}]$',
        'tick_levels':4,
        'tick_text_levels':2,
        'tick_side':'left',
        'scale_type':'linear smart',
        'title_y_shift':0.5,
        'extra_params':[{
                },
                {
                'scale_type':'manual line',
                'manual_axis_data':{
                        6.73*10**(-4):Tt+r' Nylon',
                        3.31*10**(-3):Tt+r' Coated',
                        },
                'tick_side':'right',
                'text_color':col,
                }],
        'text_size_0':T0,
        'text_size_1':T1,
        }

#   square root of T/rho [m/s], first intermediate result
r_params={
        'u_min':120,
        'u_max':365,
        'function':lambda r:r,
        'title':r'',
        'tick_levels':0,
        'tick_text_levels':0,
        'tag':'r'
        }
 
block_params_1={
        'block_type':'type_2',
        'width':30.0,
        'height':20.0,
        'f1_params':T_params,
        'f2_params':rh_params,
        'f3_params':r_params,
        'isopleth_values':[[6.7,3.31*10**(-3),'x']]
        }

#%% MAIN BLOCK 2 (RIGHT-SIDE NOMOGRAM)
#   square root of T/rho [m/s], first intermediate result
r_params_2={
        'u_min':120,
        'u_max':365,
        'function':lambda r:r,
        'title':r'',
        'tick_levels':0,
        'tick_text_levels':0,
        'tag':'r'
        }

#   string length l [cm]
l_params={
        'u_min':30,
        'u_max':70,
        'function':lambda l:(2*l/100),
        'title':Tt+r'$l$ [cm]',
        'tick_levels':4,
        'tick_text_levels':2,
        'title_y_shift':0.5,
        'tick_side':'left',
        'scale_type':'linear smart',
        'text_size_0':T0,
        'text_size_1':T1,
        }

#   vibration frequency f [Hz]
f_params={
        'u_min':85.0,
        'u_max':650.0,
        'function':lambda f:f,
        'title':Tt+r'$f$ [Hz]',
        'title_x_shift':-0.5,
        'tick_levels':4,
        'tick_text_levels':2,
        'tick_side':'right',
        'scale_type':'linear smart',
        'extra_params':[{
                'scale_type':'manual line',
                'manual_axis_data':{
                        87.30706:Tt+r'$F_2$',
                        110.0000:Tt+r'$A_2$',
                        130.8128:Tt+r'$C_3$',
                        146.8324:Tt+r'$D_3$',
                        174.6141:Tt+r'$F_3$',
                        195.9977:Tt+r'$G_3$',
                        220.0000:Tt+r'$A_3$',
                        246.9417:Tt+r'$B_3$',
                        261.6256:Tt+r'$C_4$',
                        293.6648:Tt+r'$D_4$',
                        329.6276:Tt+r'$E_4$',
                        349.2282:Tt+r'$F_4$',
                        391.9954:Tt+r'$G_4$',
                        440.0000:Tt+r'$A_4$',
                        493.8833:Tt+r'$B_4$',
                        523.2511:Tt+r'$C_5$',
                        587.3295:Tt+r'$D_5$'},
                'tick_side':'left',
                'text_color':col,
                },
                {
                'scale_type':'manual line',
                'manual_axis_data':{
                        97.99886:Tt+r'$G_2$',
                        123.4708:Tt+r'$B_2$',
                        164.8138:Tt+r'$E_3$'
                },
                'tick_side':'left',
                'text_color':col,
                'grid_length_1':1,
                'text_distance_1':1.,
                }],
        'text_size_0':T0,
        'text_size_1':T1,
        }

block_params_2={
        'block_type':'type_2',
        'width':30.0,
        'height':20.0,
        'f1_params':r_params_2,
        'f2_params':l_params,
        'f3_params':f_params,
        'mirror_x':True,
        'isopleth_values':[['x',66,'x']]
        }

#%% GLOBAL SETTINGS
main_params={
        'filename':'Figure9.pdf',
        'paper_width':29.7,
        'paper_height':21.0,
        'block_params':[block_params_1,block_params_2],
        'transformations':[('rotate',0.01),('scale paper',)],
        'title_str':Tt+r'$f={1 \over 2 l} \sqrt{T \over \rho}$',
        'title_y':21.5,
        'isopleth_params':[{
                'color':'Red',
                'linewidth':'THIN',
                'linestyle':'solid',
                'transparency':0.2,
                },
                {
                'color':'Red',
                'linewidth':'THIN',
                'linestyle':'solid',
                'transparency':0.2,
                }]
        }
        
Nomographer(main_params)
print('\a')