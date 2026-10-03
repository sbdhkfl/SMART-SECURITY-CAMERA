"""Browser launcher for the local security-camera dashboard."""
import webbrowser
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent/"orange-pi"))
from app.main import app
import uvicorn
if __name__=="__main__":
    url="http://127.0.0.1:8080"
    webbrowser.open(url)
    uvicorn.run(app,host="127.0.0.1",port=8080)
