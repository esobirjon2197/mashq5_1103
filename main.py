
# 4-m
class Misol:
    x = "klass ma'lumoti"


    def __init__(self):
        self.y = "obyekt ma'lumoti"


    def instance_m(self):
        return f"instance: {self.y} va {self.x}"


    @classmethod
    def class_m(cls):
        return f"class: {cls.x}"


    @staticmethod
    def static_m():
        return "static: hech narsaga bog'liq emas"

    
m = Misol()
print(m.instance_m())
print(Misol.class_m())
print(Misol.static_m())




