from app.api_eddington import app

if __name__ == "__main__":
    # For local testing, run the FastAPI server with uvicorn
    # http://127.0.0.1:8000/docs#/ contains the API documentation
    # You can test the API using curl or Postman.
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)