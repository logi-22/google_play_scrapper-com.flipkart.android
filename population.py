from fastapi import FastAPI
from typing import Dict
import pandas as pd

# Load the dataset
data = pd.read_csv("D:/pandas/world_pop.csv")

# Initialize FastAPI app
app = FastAPI()

@app.get("/stats")
def get_population_stats():
    # Group by continent and calculate statistics
    grouped = data.groupby("Continent")
    stats = grouped["Population"].agg(["max", "min", "mean"]).reset_index()

    # Convert to dictionary for JSON response
    result = {
        row["Continent"]: {
            "max": int(row["max"]),
            "min": int(row["min"]),
            "average": round(row["mean"], 2)
        }
        for _, row in stats.iterrows()
    }

    return result
