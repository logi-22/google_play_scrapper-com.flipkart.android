import pandas as pd

file_path="D:\world_population.csv"

countries_df=pd.read_csv(file_path)
#filter=countries_df["Country"]=="china"
china_df=countries_df[countries_df["Country"]=="China"]
print(china_df)

china_df1=countries_df.loc[0,"Capital"]
print(china_df1)


india_df=countries_df.tail(1)["Capital"]
print(india_df)

#unique continents
unique_continents=countries_df["Continent"].unique()
print(f"Unique Continent:\n",unique_continents)

#GroupBy
continent_status=countries_df.groupby("Continent")["Population"].agg(
Total_countries="count",
Total_population="sum",
Average_population="mean",
Total_Area="sum"
)
print(continent_status.to_string(index=False))

#population density
continent_status["Population_density"]=continent_status["Total_population"]/continent_status["Total_Area"]
print(continent_status)


#countries with maximum and minimum population
countries_population=countries_df.groupby("Continent")["Population"].agg(
    max_population="max",
    min_population="min"
).reset_index()
total_index=(countries_population.to_string(index=False))
print(total_index)




