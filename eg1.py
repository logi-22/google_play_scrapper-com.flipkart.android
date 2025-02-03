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


