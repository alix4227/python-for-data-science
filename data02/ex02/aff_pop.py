from matplotlib.ticker import FuncFormatter

from load_csv import load
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

def str_to_int(val):
    if val.endswith('M'):
        return int(float(val[:-1]) * 1_000_000)
    elif val.endswith('k'):
        return int(float(val[:-1]) * 1_000)
   
def millions_formatter(x, pos):
    """Convertit les valeurs en millions avec le suffixe M"""
    return f'{int(x / 1_000_000)}M'
def main():
    df = load("population_total.csv")
    fr = df[df['country'] == 'France'].squeeze()
    year = np.array([int(x) for x in fr.drop('country').keys() if int(x) <= 2050])
    data_fr = fr.drop('country').values[:len(year)]
    population_fr = np.array([str_to_int(x) for x in data_fr])

    be = df[df['country'] == 'Belgium'].squeeze()
    data_be = be.drop('country').values[:len(year)]
    population_be = np.array([str_to_int(x) for x in data_be])
    plt.figure()
    plt.plot(year, population_fr, label='France')
    plt.plot(year, population_be, label='Belgium')
    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    plt.legend()
    plt.savefig('graphique.png')
    # plt.show()


if __name__ == "__main__":
    main()

