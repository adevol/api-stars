'''
This module provides an API for calculating the Eddington ratio of stars.
It includes endpoints for both single star calculations and batch processing from a CSV file.
'''
import pandas as pd
import io
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import Optional, List

from app.star_utils.eddington import calculate_eddington_ratio

app = FastAPI()

class StarInput(BaseModel):
    luminosity: float
    mass: float
    temperature: Optional[float] = None
    metallicity: Optional[float] = None

@app.post("/eddington_ratio")
def compute_eddington_ratio_single_star(data: StarInput):
    ratio = calculate_eddington_ratio(data.luminosity, data.mass)
    return {"eddington_ratio": ratio}

@app.post("/eddington_ratio_batch")
async def compute_eddington_ratio_from_csv(
        file: UploadFile = 
        File(..., description="Upload a CSV file with at least the 'luminosity' and 'mass' columns")
        ):
    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

    if 'luminosity' not in df.columns or 'mass' not in df.columns:
        return {"error": "CSV must contain 'luminosity' and 'mass' columns."}

    df['eddington_ratio'] = df.apply(
        lambda row: calculate_eddington_ratio(row['luminosity'], row['mass']), axis=1
    )
    return df.to_dict(orient="records")
