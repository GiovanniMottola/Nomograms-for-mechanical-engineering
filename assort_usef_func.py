##  DATE:    12/02/2021
##  AUTHOR:  GIOVANNI MOTTOLA
#   for cleaning up when starting a script
def cleanup():
    try:
        from IPython import get_ipython
        #   cleanup variables
        get_ipython().magic('reset -f')
        #   cleanup command window
        get_ipython().magic('clear')
        #   close old windows
        plt.close( 'all' )
    except:
        pass