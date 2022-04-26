from typing import List

class Engine:
    def init(self, power, volume, weight):
        self.power = power
        self.volume = volume
        self.weight = weight

class Wheel:
    def init(self, weight, mfr, radius):
        self.weight = weight
        self.mfr = mfr
        self.radius = radius

class Steering:
    def init(self, shape, mfr, weight, q):
        self.shape = shape
        self.mfr = mfr
        self.weight = weight
        self.q = q
        self.steering_wheel_orientation = steering_wheel_orientation
        steering_wheel_orientation = 'Right' if mfr in ['Japan', 'England'] else 'Left'

class Car:
    def __init__(self, eng:Engine, whs:List[Wheel], st:Steering):
        w_all = sum([item.weight for item in [eng, st].extend(whs)])
        self.hp = eng.power / w_all
        self.engine = eng
        self.wheels = whs
        self.steering_wheel = st
        q_whs = sum([w.q for w in whs]) / len(whs) #качество колес
        self.q = (eng.q + q_whs + st.q) / 3