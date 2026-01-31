import uvicorn
import os
import sys

if __name__ == "__main__":
    # Force the current folder into Python's path
    sys.path.append(os.getcwd())
    
    # Run Uvicorn directly from Python
    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=True)
