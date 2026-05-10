from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as ticker

from load_csv import load
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

def str_to_int(val):
    if isinstance(val, str):
        if val.endswith('k'):
            return int(float(val[:-1]) * 1_000)
        else:
            return int(float(val))
    else:
        return int(val) 
   
def thousands_formatter(x, pos):
    """Convertit les valeurs en milliers avec le suffixe k"""
    return f'{int(x / 1_000)}k'
def main():
    df = load("life_expectancy_years.csv")
    life_expectancy = df['1900']
    life =[x for x in life_expectancy]

    df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    Gdp = df['1900']
    Gdp1 = [str_to_int(x) for x in Gdp]
       
    plt.figure()
    plt.scatter(Gdp1, life)
    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life expectancy')
    ax = plt.gca()
    ax.xaxis.set_major_formatter(FuncFormatter(thousands_formatter))
    plt.xscale('log')
    # Give scale values and name to x axis
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.savefig('graphique.png')
    # plt.show()


if __name__ == "__main__":
    main()

