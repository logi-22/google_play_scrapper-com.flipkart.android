import pandas as pd #From pandas package manager
#from file_io import read_country_data #print_complete_dataframe#user defined module
file_path="D:\world_population.csv"
countries_df = pd.read_csv(file_path)

# country_india_df = countries_df.loc[1] #First Row of countries_df

# capital_of_india = country_india_df["Capital"]

# print(capital_of_india)

# country_india_df = countries_df.loc[1] #First Row of countries_df
# capital_of_india_1 = country_india_df["Capital"]
# print(f"capital_of_india_1: {capital_of_india_1}")

# capital_of_india_2 = countries_df.loc[1]["Capital"]
# print(f"capital_of_india_2: {capital_of_india_2}")

# capital_of_india_3 = countries_df.loc[1, "Capital"]
# print(f"capital_of_india_3: {capital_of_india_3}")

# Aggregation Functions
# print("\nTotal World Population:", countries_df["Population"].sum())
# print("\Mean World Population:", countries_df["Population"].mean()) #2 kind of averages: mean and median


countries_of_asia_df = countries_df[countries_df["Continent"] == "Asia"]
# print("\Asian Population:", countries_of_asia_df["Population"].sum())
# print("\Mean Asian Population:", countries_of_asia_df["Population"].mean()) #2 kind of averages: mean and median

# countries_df.loc[countries_df["Continent"] == "Asia"].mean()
countries_df.loc[countries_df["Continent"] == "Asia", "Population"].mean() 

#countries_df["Continent"] == "Asia" This is filter that select rows where Continent  == Asia
#using the above filter, and column name i get the population of all asian countries
## asian_countries_df = countries_df.loc[countries_df["Continent"] == "Asia"] 
## population_of_asian_countries = asian_countries_df["population"]
##Mean of asian countries population = population_of_asian_countries.mean()

## print("\nAverage Area:", countries_df["Area"].mean())

colunms_to_select = ["Country", "Population", "Area"]
asian_countries_df = countries_df.loc[countries_df["Continent"] == "Asia", colunms_to_select]
print(asian_countries_df)
# print(type(asian_countries_df))