#%% PROPERTIES
##  DATE:    20/04/2022
##  AUTHOR:  Giovanni Mottola

#%% CLEAN WORKSPACE
from assort_usef_func import cleanup
cleanup()

#%% IMPORTS
# -*- coding: utf-8 -*-
from pynomo.nomographer import *
from numpy import *
from pyx import text, color
T0=text.size.Large;
T1=text.size.large;
Tt='\Large';
col=color.cmyk.Black;

#   FUNCTION FOR CONVERTING FROM SHORE DEGREES TO YOUNG MODULUS (APPROX.)
def young(Shore):
    return (0.0981*(56+7.62336*Shore))/(0.137505*(254-2.54*Shore))

#%% MAIN BLOCK 1 (LEFTMOST NOMOGRAM)
#   rubber hardness S [°Sh]
S_params={
        'u_min':20,
        'u_max':80,
        'function':lambda S:sqrt(young(S)),
        'title':Tt+r'$S\,[^\circ\rm{Sh}]$',
        'tick_levels':4,
        'tick_text_levels':2,
        'tick_side':'right',
        'scale_type':'linear smart',
        'title_x_shift':0.9,
        'title_y_shift':0.5,
        'text_size_0':T0,
        'text_size_1':T1,
        'tag':'ES',
        'align_func':young,
        }

#   Young's modulus E [MPa]
E_params={
        'u_min':0.5,
        'u_max':9.5,
        'function':lambda E:sqrt(E),
        'title':Tt+r'$E$ [MPa]',
        'tick_levels':4,
        'tick_text_levels':2,
        'tick_side':'left',
        'scale_type':'linear smart',
        'title_x_shift':-1,
        'title_y_shift':0.35,
        'text_size_0':T0,
        'text_size_1':T1,
        'tag':'ES',
        }
 
block_params_S={
        'block_type':'type_8',
        'f_params':S_params,
        'isopleth_values':[[70]],
        }

block_params_E={
        'block_type':'type_8',
        'f_params':E_params,
        'isopleth_values':[['x']],
        }

#%% MAIN BLOCK 2 (LEFT-SIDE NOMOGRAM)
#   cross-section diameter d [mm]
d_params={
        'u_min':0,
        'u_max':270,
        'function':lambda d:sqrt(pi)*d,
        'title':Tt+r'$d$ [mm]',
        'tick_levels':4,
        'tick_text_levels':1,
        'tick_side':'left',
        'extra_angle':45.0,
        'scale_type':'linear smart',
        'title_x_shift':-21.5,
        'text_size_0':T0,
        'text_size_1':T1,
        }

#   spring height h [mm]
h_params={
        'u_min':12,
        'u_max':100,
        'function':lambda h:2*sqrt(h),
        'title':Tt+r'$h$ [mm]',
        'tick_levels':4,
        'tick_text_levels':2,
        'scale_type':'linear smart',
        'title_x_shift':0.9,
        'title_y_shift':-0.3,
        'text_size_0':T0,
        'text_size_1':T1,
        }

#   spring stiffness k [N/mm]
k_paramsSX={
        'u_min':0.0,
        'u_max':5500.0,
        'function':lambda k:sqrt(k),
        'title':Tt+r'$k \left[{\rm{N} \over \rm{mm}}\right]$',
        'title_x_shift':0.5,
        'title_y_shift':-21.5,
        'tick_levels':4,
        'tick_text_levels':2,
        'text_format':r"$%3.0f$",
        'scale_type':'linear smart',
        'text_size_0':T0,
        'text_size_1':T1,
        'tag':'k',
        }

block_params_k={
        'block_type':'type_4',
        'f1_params':E_params,
        'f2_params':k_paramsSX,
        'f3_params':h_params,
        'f4_params':d_params,
        'isopleth_values':[['x','x',45,150]],
        }

#%% MAIN BLOCK 2 (RIGHT-SIDE NOMOGRAM)
#   suspended mass [kg]
m_params={
        'u_min':0.,
        'u_max':10.0,
        'function':lambda m:2*sqrt(m),
        'title':Tt+r'$m$ [kg]',
        'title_x_shift':-0.8,
        'title_y_shift':0.5,
        'tick_levels':4,
        'tick_text_levels':2,
        'scale_type':'linear smart',
        'text_horizontal_align_center':True,
        'text_size_0':T0,
        'text_size_1':T1,
        'tick_side':'left',
        }

#   critical damping factor [N/m/s]
c_params={
        'u_min':0,
        'u_max':470,
        'function':lambda c:c,
        'title':Tt+r'$c_{cr} \left[{\rm{Ns} \over \rm{m}}\right]$',
        'title_x_shift':-0.,
        'title_y_shift':0.5,
        'tick_levels':4,
        'tick_text_levels':2,
        'scale_type':'linear smart',
        'text_horizontal_align_center':True,
        'extra_angle':45.0,
        'text_size_0':T0,
        'text_size_1':T1,
        }

#   spring stiffness k [N/mm]
k_paramsDX={
        'u_min':10.0,
        'u_max':5000.0,
        'function':lambda k:sqrt(k),
        'tick_levels':0,
        'tick_text_levels':0,
        'tag':'k',
        }

block_params_c={
        'block_type':'type_2',
        'f1_params':c_params,
        'f2_params':m_params,
        'f3_params':k_paramsDX,
        'mirror_x':True,
        'isopleth_values':[['x',5,'x']],
        }

#%% GLOBAL SETTINGS
main_params={
        'filename':'Figure10.pdf',
        'paper_width':42.0,
        'paper_height':23,
        'block_params':[block_params_E,block_params_S,block_params_k,block_params_c],
        'transformations':[('scale paper',)],
        'title_str':Tt+r'$c_{cr} = 2 \sqrt{k m}$',
        'title_x':33,
        'title_y':22.5,
        'extra_texts':[{
                'x':9.0,
                'y':18.0,
                'text':Tt+r'$k={{\pi d^2 E}\over{4h}}={F \over x}$',
                'width':5,
                'pyx_extra_defs':[T1]
                },{
                'x':-2.25,
                'y':3.5,
                'text':Tt+r'$E={{0.0981(56+7.62336^\circ\rm{Sh})}\over{0.137505(254-2.54^\circ\rm{Sh})}}$',
                'width':7,
                'pyx_extra_defs':[T1]
                }],
        'isopleth_params':[{
                'color':'Red',
                'linewidth':'THIN',
                'linestyle':'solid',
                'transparency':0.2
                },{
                'color':'Red',
                'linewidth':'THIN',
                'linestyle':'solid',
                'transparency':0.2
                },{
                'color':'Red',
                'linewidth':'THIN',
                'linestyle':'solid',
                'transparency':0.2
                }]
        }

Nomographer(main_params)
print('\a')