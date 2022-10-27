#%% PROPERTIES
##  DATE:    04/02/2022
##  AUTHOR:  GIOVANNI MOTTOLA

#%% CLEAN WORKSPACE
from assort_usef_func import cleanup
cleanup()

#%% IMPORTS
# -*- coding: utf-8 -*-
from pynomo.nomographer import *
from scipy.constants import g
from numpy import sqrt

#   FUNCTION FOR COMPUTING THE OPTIMAL SPRING STIFFNESS, GIVEN THE RADIUS
def calc_K(r):
    return (r*(5*r**6+36*r**4+64*r**2-512))/(4+r**2)

#   FUNCTION FOR COMPUTING THE RADIUS, GIVEN THE OPTIMAL SPRING LENGTH
def calc_r(s):
    radq=sqrt(3834+351*s-1584*s**2+448*s**3)
    radc=(2403-504*s+34.3*radq)**(1./3.)
    return 0.436*sqrt(-15+156/radc-(116.5*s)/radc+radc*3**(1./3.))

#%% MAIN BLOCK 1 (LEFT-SIDE NOMOGRAM)
#   normalized distance c from the center of mass to the axis of rotation [-]
c1_params={
        'u_min':2.0,
        'u_max':20.0,
        'function':lambda c1:-c1*128*g,
        'title':r'$c$',
        'tick_levels':3,
        'tick_text_levels':1,
        'tick_side':'left',
        }
        
#   normalized optimal spring stiffness K_opt [m/s^2]
Kb_params={
        'u_min':50.0,
        'u_max':4000.0,
        'function':lambda Kb:Kb,
        'title':r'$K_b$',
        'tick_levels':3,
        'tick_text_levels':1,
        'tick_side':'left',
        }

#   normalized radius r of the crank [-]
r_params={
        'u_min':0.05,
        'u_max':0.35,
        'function':lambda r:calc_K(r),
        'title':r'$r$',
        'tick_levels':3,
        'tick_text_levels':1,
        'tag':'rs',
        'title_x_shift':0.5,
        }
 
block_1_params={
        'block_type':'type_2',
        'height':9.0,
        'width':12.0,
        'f1_params':c1_params,
        'f2_params':Kb_params,
        'f3_params':r_params,
        }

#%% MAIN BLOCK 2 (RIGHT-SIDE NOMOGRAM)
#   normalized optimal spring free length s_0,opt [m/s^2]
s_params={
        'u_min':1.9406,
        'u_max':1.9988,
        'function':lambda s:calc_r(s),
        'title':r'$s_0$',
        'tick_levels':3,
        'tick_text_levels':1,
        'tag':'rs',
        'tick_side':'left',
        'align_func':calc_r,
        'title_x_shift':-0.5,
        }

block_params_s={
        'block_type':'type_8',
        'f_params':s_params,
        }

#%% GLOBAL SETTINGS
main_params={
        'filename':'Figure12.pdf',
        'paper_height':9.0,
        'paper_width':12.0,
        'block_params':[block_1_params,block_params_s],
        'transformations':[('rotate',0.01),('scale paper',)],
        'title_str':r'Optimal balance',
        }

Nomographer(main_params)
print('\a')