# 📡 Eddington Ratio API

This API provides tools for calculating the **Eddington ratio** of stars based on their physical properties. It is intended as a small demo for the astronomy department of KU Leuven.

The **Eddington ratio** is defined as:

    Γ = L / L_Edd

where:

- `L` is the star’s luminosity in erg/s  
- `L_Edd` is the Eddington luminosity — the theoretical maximum luminosity a star can achieve before radiation pressure blows away its outer layers

---

## 🚀 Endpoints

### `POST /eddington_ratio`

Calculate the Eddington ratio for a **single star**.

**Request JSON:**

```json
{
  "luminosity": 1,
  "mass": 1,
  "temperature": 7000,
  "metallicity": 1
}
```

* Only luminosity and mass are required.
* temperature and metallicity are accepted for future extensions.
* The units are in **solar units**.

**Response:**
```json
{
  "eddington_ratio": 0.42
}
```

### `POST /eddington_ratio_batch`
Upload a CSV file to compute Eddington ratios for multiple stars.

File Requirements:

* CSV with at least luminosity and mass columns

* Optional columns: temperature, metallicity

**Example Response:**
```json
[
  {"luminosity": 1e38, "mass": 10, "eddington_ratio": 0.42},
  {"luminosity": 2e38, "mass": 20, "eddington_ratio": 0.32}
]
```

## 🛠️ Dev Info
Framework: FastAPI

Language: Python 3.10+

A working environment is provided in the file requirements.txt.
To use this environment, please create a new environment and run:

```bash
pip install -r requirements.txt
```



Run locally with:
```bash
python main.py
```
* Open your browser to: http://127.0.0.1:8000/docs for interactive API documentation.

## ✅ Running Unit Tests

To run the unit tests:

```bash
python -m unittest discover -s tests
```

Or use the preconfigured Run Unit Tests debug option from the included launch.json