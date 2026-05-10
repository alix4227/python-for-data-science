from load_csv import load

df = load("life_expectancy_years.csv")
fr = df[df['country'] == 'France']
print(fr)
