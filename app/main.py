class Distance:
    def __init__(self, km: float):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if type(other) == float or type(other) == int:
            self.km = self.km + other
            return self
        elif type(other) == Distance:
            self.km = self.km + other.km
            return self

    def __iadd__(self, other):
        if type(other) == float or type(other) == int:
            self.km += other
            return self
        elif type(other) == Distance:
            self.km += other.km
            return self
        if not other:
            return self

    def __mul__(self, other):
        result = self.km * other
        return Distance(km=result)

    def __truediv__(self, other):
        result = round(self.km / other, 2)
        return Distance(
            km=result
        )

    def __lt__(self, other):
        if type(other) == float or type(other) == int:
            return self.km < other
        if type(other) == Distance:
            result = self.km < other.km
            return result

    def __gt__(self, other):
        trig = False
        if type(other) == float or type(other) == int:
            trig = self.km > other
        if isinstance(other, Distance):
            trig = self.km > other.km
        return trig

    def __eq__(self, other):
        trig = self.km == other
        return trig

    def __le__(self, other):
        result = True
        if type(other) == float or type(other) == int:
            temp = Distance(km=other)
            result = self.km <= temp.km
        if type(other) == Distance:
            result = self.km <= other.km

        return result

    def __ge__(self, other):
        trig = False
        if type(other) == float or type(other) == int:
            trig = self.km >= other
        if isinstance(other, Distance):
            trig = self.km >= other.km
        return trig
