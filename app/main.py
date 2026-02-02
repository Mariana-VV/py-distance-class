class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance | None:
        if type(other) == float or type(other) == int:
            self.km = self.km + other
            return self
        elif type(other) == Distance:
            self.km = self.km + other.km
            return self

    def __iadd__(self, other: Distance | int | float) -> Distance | None:
        if type(other) == float or type(other) == int:
            self.km += other
            return self
        elif type(other) == Distance:
            self.km += other.km
            return self
        if not other:
            return self

    def __mul__(self, other: Distance | int | float) -> Distance | None:
        result = self.km * other
        return Distance(km=result)

    def __truediv__(self, other: Distance | int | float) -> Distance | None:
        result = round(self.km / other, 2)
        return Distance(
            km=result
        )

    def __lt__(self, other: Distance | int | float) -> bool:
        if type(other) == float or type(other) == int:
            return self.km < other
        if type(other) == Distance:
            result = self.km < other.km
            return result

    def __gt__(self, other: Distance | int | float) -> bool:
        trig = False
        if type(other) == float or type(other) == int:
            trig = self.km > other
        if type(other) == Distance:
            trig = self.km > other.km
        return trig

    def __eq__(self, other: Distance | int | float) -> bool:
        trig = self.km == other
        return trig

    def __le__(self, other: Distance | int | float) -> bool:
        result = True
        if type(other) == float or type(other) == int:
            temp = Distance(km=other)
            result = self.km <= temp.km
        if type(other) == Distance:
            result = self.km <= other.km

        return result

    def __ge__(self, other: Distance | int | float) -> bool:
        trig = False
        if type(other) == float or type(other) == int:
            trig = self.km >= other
        if type(other) == Distance:
            trig = self.km >= other.km
        return trig
