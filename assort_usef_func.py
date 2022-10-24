##  DATE:    12/02/2021
##  AUTHOR:  GIOVANNI MOTTOLA
#   per ripulire tutto all'avvio di uno script
def pulizia():
    try:
        from IPython import get_ipython
        #   pulizia variabili
        get_ipython().magic('reset -f')
        #   pulizia finestra comandi
        get_ipython().magic('clear')
        #   chiudo finestre vecchie
        plt.close( 'all' )
    except:
        pass