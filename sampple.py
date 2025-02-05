# from fastapi import FastAPI, HTTPException, Query
# import pandas as pd

# app = FastAPI()

# # Path to the uploaded CSV file
# file_path = "D:/pandas/world_pop.csv"

# # Read the CSV file into a DataFrame

# df = pd.read_csv(file_path)


# @app.get("/")
# def home():
#     return {"message": "Welcome to homepage."}

# @app.get("/{continent}")
# def get_countries(continent:str,):
#     countries_population=df.groupby("Continent")["Population"].agg(
#     max_population="max",
#     min_population="min"
# ).reset_index()
#     response={}
#     result=countries_population[continent]
#     response["max"]=f"{result["max_population"]}"
#     return response
    
    
from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# Path to the uploaded CSV file
file_path ="D:/pandas/world_population (1).csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

@app.get("/")
def home():
    return {"message": "Welcome to the homepage."}

@app.get("/{continent}")
def get_countries(continent: str):
    # Group by Continent and calculate max and min populations
    countries_population = df.groupby("Continent").agg(
        max_population=("Population", "max"),
        min_population=("Population", "min")
    ).reset_index()
    
    # Filter for the requested continent
    result = countries_population[countries_population["Continent"] == continent]
    
    if result.empty:
        raise HTTPException(status_code=404, detail="Continent not found")

    # Prepare response
    response = {
        "max_population": result.iloc[0]["max_population"],
        "min_population": result.iloc[0]["min_population"]
    }
    return response






