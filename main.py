from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import pandas as pd

app = FastAPI()

# Read outlet data from the CSV file
df = pd.read_csv("/workspace/outlets_with_coordinates.csv")

# Pydantic model for response
class OutletResponse(BaseModel):
    outlet_name: str
    latitude: float
    longitude: float

# Endpoint to get all outlets
@app.get("/outlets", response_model=List[OutletResponse])
async def get_all_outlets():
    outlets = []
    for _, row in df.iterrows():
        outlet = OutletResponse(
            outlet_name=row['outlet_name'],
            latitude=row['Latitude'],
            longitude=row['Longitude']
        )
        outlets.append(outlet)
    return outlets

# Endpoint to get a specific outlet by name
@app.get("/outlets/{outlet_name}", response_model=OutletResponse)
async def get_outlet(outlet_name: str):
    outlet_row = df[df['outlet_name'] == outlet_name]
    if outlet_row.empty:
        raise HTTPException(status_code=404, detail="Outlet not found")
    
    row = outlet_row.iloc[0]
    outlet = OutletResponse(
        outlet_name=row['outlet_name'],
        latitude=row['Latitude'],
        longitude=row['Longitude']
    )
    return outlet
