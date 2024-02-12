from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/{date}")
def get_data(date: str):
    url = f'http://comptoirmecanique.ddns.net:8000/api/admin/admin/{date}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return {"error": f"Error fetching data: {e}"}
