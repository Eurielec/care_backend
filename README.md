# C.A.R.E project backend

Backend application for EKG storage. Allows the frontend to access stored EKGs
and the hardware to save recorded EKGs.

## Installation

```bash
pip install -r requirements.txt
```

## Running the application

From the root path of this repo run:

```bash
uvicorn --app-dir src/care_backend main:app --reload
```
