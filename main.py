import logging, json, os.path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from api import app as api_app

logging.basicConfig(level=logging.DEBUG)

# Define DB Format
DB_EXAMPLE = {
    'min_temp': 16,
    'max_temp': 27,
    'timers' : []
}

# Write required files
REQUIRED_FILES = ['database.json', 'database.previous.json']
for f in REQUIRED_FILES:
    if not os.path.exists(f): open(f, 'w').write(json.dumps(DB_EXAMPLE))
    if open(f,'r').read().strip() == '': open(f, 'w').write(json.dumps(DB_EXAMPLE))
    if list(json.load(open(f, 'r'))) != list(DB_EXAMPLE): open(f, 'w').write(json.dumps(DB_EXAMPLE))

app = FastAPI()
app.mount("/api", api_app, name='api')
app.mount("/", StaticFiles(directory='static', html=True), name='static')

# Handle index.html
#@app.get("/")
#def handle_index():
#    return FileResponse('static/index.html')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)