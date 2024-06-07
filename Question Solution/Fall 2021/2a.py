class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        total_minutes = total_minutes % 60
        return Time(total_hours, total_minutes)

    def __str__(self):
        return f"{self.hours} hr {self.minutes} min"

    def display_minutes(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"Total minutes: {total_minutes}")

t1 = Time(2, 50)
t2 = Time(1, 20)
t3 = t1.add(t2)
print(t3)
t3.display_minutes()
