from datetime import datetime
from .action import Action

class Timer:
    def __init__(self, data: dict, override_id=None):
        self.id = override_id if override_id else data.get('id')
        self.time = datetime.strptime(data.get('time'), '%Y-%m-%d %H:%M:%S')
        self.action = Action.ON if data.get('action')=='ON' else Action.OFF if data.get('action')=='OFF' else None
        self.temp = data.get('temp')

    def __dict__(self):
        return {
            'id': self.id,
            'time': str(self.time),
            'action': self.action.name,
            'temp': self.temp
        }