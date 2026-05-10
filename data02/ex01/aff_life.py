from load_csv import load
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
def main():
    df = load("life_expectancy_years.csv")
    fr = df[df['country'] == 'France'].squeeze()
    year = np.array(fr.drop('country').keys(), dtype=int)
    life_expectancy = np.array(fr.drop('country').values)
    plt.figure()
    plt.plot(year, life_expectancy)
    plt.title('France Life expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.savefig('graphique.png')
    # plt.show()


if __name__ == "__main__":
    main()

