import json
from timer.timer import Timer

DATABASE_PATH = 'database.json'

class Database:
    """
    Read Database
    Parameters:     None
    Returns:        DB as dict
    """
    def read_db() -> dict:
        return json.load(open(DATABASE_PATH))

    """
    Write to Database
    Parameters:     dict - Data to write
    Returns:        None
    """
    def set_db(data: dict) -> None:
        open('database.previous.json','w').write(json.dumps(Database.read_db(), indent=2))
        open(DATABASE_PATH,'w').write(json.dumps(data, indent=2))

    """
    Get Timers From Database
    Parameters:     None
    Returns:        list[Timers]
    """
    def get_timers(raw=False) -> list[Timer]:
        timers = []
        for t in Database.read_db().get('timers'):
            if raw: timers.append(t)
            else: timers.append(Timer(t))
        return timers

    """
    Update Timers
    Parameters:     New timers list
    Returns:        None
    """
    def set_timers(timers: list[Timer]) -> None:
        timers_json = []
        for t in timers:
            timers_json.append(t.__dict__())
        
        db = Database.read_db()
        db['timers'] = timers_json
        Database.set_db(db)


    """
    Add Timer to Database
    Parameters:     `Timer` object
    Returns:        None
    """
    def add_timer(timer: Timer) -> None:
        Database.set_timers(Database.get_timers() + [timer])
    
    """
    Generate ID based on db
    Parameters:     None
    Returns:        int
    """
    def generate_timer_id() -> int:
        biggest = 0
        for t in Database.get_timers():
            if t.id:
                if t.id > biggest: 
                    biggest = t.id
        return biggest+1