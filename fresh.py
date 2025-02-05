from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

file_path = "D:/pandas/world_population (1).csv"
countries_df = pd.read_csv(file_path)

@app.get("/")
def home():
    return {"message": "Welcome to the World Population API"}

@app.get("/continent/{continent_name}")
def get_continent_population(continent_name: str):
    continent_group = countries_df[countries_df["Continent"] == continent_name]
    continent_group = continent_group.dropna(subset=["Population", "Area"])
    
    if continent_group.empty:
        raise HTTPException(status_code=404, detail=f"No data found for continent: {continent_name}")
    
    # Ensure Population and Area are numeric, coercing errors to NaN
    continent_group["Population"] = pd.to_numeric(continent_group["Population"])
    continent_group["Area"] = pd.to_numeric(continent_group["Area"])
    
    # Drop rows with invalid numeric values
    continent_group = continent_group.dropna(subset=["Population", "Area"])
    
    # Calculate total population and total area
    total_population = int(continent_group["Population"].sum())
    total_area = int(continent_group["Area"].sum())
    
    # Calculate population density
    continent_density = total_population / total_area
    
    # Find max and min population countries
    max_row = continent_group.loc[continent_group["Population"].idxmax()]
    min_row = continent_group.loc[continent_group["Population"].idxmin()]
    avg_population = int(continent_group["Population"].mean())
    
    return {
        "continent": continent_name,
        "total_population": total_population,
        "total_area": total_area,
        "continent_population_density": round(continent_density, 2),
        "max_population": {
            "country": max_row["Country"],
            "population": int(max_row["Population"])
        },
        "min_population": {
            "country": min_row["Country"],
            "population": int(min_row["Population"])
        },
        "avg_population": avg_population
    }
