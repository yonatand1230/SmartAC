from fastapi import FastAPI
from fastapi.responses import JSONResponse
from database.database import Database
from timer.timer import Timer

app = FastAPI()

# Handle Server HTTP Functions


"""
Handle GET /gettimers
Parameters:     None
Returns:        list[Timer]
"""
@app.get("/get_timers")
def handle_get_timers():
    return JSONResponse(Database.get_timers(raw=True))


"""
Handle POST /addtimer
Parameters:     
"""
@app.post('/add_timer')
def handler_add_timer(time: str, action: str, temp: int):
    timer = Timer({'time': time, 'action': action, 'temp': temp}, override_id=Database.generate_timer_id())
    Database.add_timer(timer)