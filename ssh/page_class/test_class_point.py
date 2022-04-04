"""
class CoordValue:
    def __set_name__(self, owner, name):
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        return instance.__dict__[self.__name]=value

   

class Point:
    __count = 0
    __instance = 0

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance , cls):
            cls.__instance = super(Point, cls).__new__(cls)

    def __init__(self, x = 0, y = 0):
        Point.__count +=1
        self.coordX = x
        self.coordY = y
    
    def getCount(self):
        return Point.__count

   


pt = Point(3, 4)

class Circle:
    def __init__(self, coorX, coorY, radius):
        self.coorX = coorX
        self.coorY = coorY
        self.radius = radius



class Point:
    def __init__(self, x = 0 , y = 0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"    

class Styles:
    def __init__(self):
        super().__init__()

class Pos(Styles):
    def __init__(self):
        super().__init__()


class Line(Pos, Styles):
    def __init__(self, sp:Point, ep:Point, color = "red", width = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = 1
        super().__init__()

    def draw(self):
        print(f"{self._sp}, {self._ep}, {self._color}, {self._width}")


l = Line(Point(1,2), Point(3,4), "blue", 3)
l.draw()
print(Line.__mro__)

class Clock:
    __day = 84000
   
    def __init__(self, secs:int):
        if not isinstance(secs, int):
            raise ValueError("Time must be an integer")
        self.__secs = secs %self.__day

    def getFormatTime(self):
        s = self.__secs % 60
        m = (self.__secs // 60) % 60
        h = (self.__secs // 60) % 24

        return f"{Clock.__getForm(h)}:{Clock.__getForm(m)}:{Clock.__getForm(s)}"

    @staticmethod
    def __getForm(x):
        return str(x) if x > 9 else "0" + str(x)

    def getSeconds(self):
        return self.__secs

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("First operand must be object in Clock")
        
        return Clock(self.__secs + other.getSeconds())

    def __iadd__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("First operand must be object in Clock")
       
        self.__secs += other.getSeconds()
        return self
    def __eq__(self, other):
        return self.__secs == other.getSeconds()
            
    def __nq__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Item should be string")

        if item == "hour":
            return (self.__secs // 60) % 24
        elif item == "minute":
            return (self.__secs // 60) % 60
        elif item == "sec":
            return self.__secs % 60
        else:
            return "Item is not found"

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Key should be string")
        
        if not isinstance(value, int):
            raise ValueError("Value should be integer")

        s = self.__secs % 60
        m = (self.__secs // 60) % 60
        h = (self.__secs // 60) % 24

        if key == "hour":
            self.__secs = s + 60 * m + value * 3600
        elif key == "minute":
            self.__secs = s + 60 * value + h * 3600
        elif key == "sec":
            self.__secs = value + 60 * m + h * 3600 




c1 = Clock(100777)
c2 = Clock(100)
c3 = c1 + c2


print(c1.getFormatTime())
if c1 == c2:
    print("Time equals")
else:
    print("Time is not equals")


if c1 != c3:
    print("Time is not equals")
else:
    ptint("chok")

c1["hour"] = 10 
print(c1["hour"], c1["minute"], c1["sec"])


class CoordError(Exception):
    pass

class Image:
    def __init__(self, width, hight, background = "_"):
        self.__background = background
        self.__width = width
        self.__hight = hight
        self.__pixels = {}
        self.__colors = {self.__background}
        
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width
  
    @property
    def hight(self):
        return self.__hight

    @hight.setter
    def hight(self, hight):
        self.__hight = hight

    def __checkColor(self, coord):

        if not isinstance(coord, tuple) or len(coord) != 2:
            raise CoordError(" Coordinates should be two-dimensional ")
        if not (0 <= coord[0] < self.__width) or not (0 <= coord[1] < self.__hight):
            raise CoordError(" Coordinates should be two-dimensional bbbbbbbbbbbbb")        

    def __setitem__(self, coord, color):
        self.__checkColor(coord)

        if color == self.__background:
            self.__pixels.pop(color, None)
        else:
            self.__pixels[coord] = color
            self.__colors.add(color)
 
    def __getitem__(self, coord):
        self.__checkColor(coord)
        return self.__pixels.get(coord, self.__background)

class MyIter:
    def __init__(self, limit):
        self.__num = 0
        self.__limit = limit
  
    def __iter__(self):
        return self

    def __next__(self):
        if self.__num >= self.__limit:
            raise StopIteration
        self.__num += 1
        return self.__num



img = Image(4, 4)
img[1, 1] = "*"
img[2, 1] = "*"
img[3, 1] = "*"

for y in range(img.hight):
    for x in range(img.width):
        print(img[x, y], sep = " " , end = " ")
    print()


it = MyIter(10)
for i in it:
    print (i)



class DeferentVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp
        return False

v1 = [1, 2, 3]
v2 = [2, 3, 4]

with DeferentVector(v1) as dv:
    for i in range(len(dv)):
        dv[i] += v2[i]
print(v1)



class ThreadData:
    __comman_case = {
           'name' : 'thread_1',
           'data' : {}, 
           'id' :  1
}

    def __init__(self):
        self.__dict__ = ThreadData.__comman_case



th1 = ThreadData()

print(th1.__dict__)

"""
class Car:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__} : {self.name}"

    def __repr__(self):
        return f"{self.name}"
    def __len__(self):
        return len(self.name)


cat = Car("Mulan")

print(len(cat))







    






