

class Time_played:
    def __init__(self, id, unit, start, end):
        self.id = id
        self.unit = unit
        self.start = start
        self.end = end

    def __str__(self):
        return f"""Zeitstaffel
id: {self.id}
Einheit: {self.unit}
Start: {self.start}
Ende: {self.end}"""

    def get_id(self):
        return self.id

    def get_unit(self):
        return self.unit

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end
