class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return 3.14 * self.radius * self.radius

    def getCircumference(self):
        return 2 * 3.14 * self.radius


circle1 = Circle(3)

print(circle1.getArea())
print(circle1.getCircumference())



class Temprature:
    def __init__(self, temFahrenheit, temCelsius):
        self.temFahrenheit = temFahrenheit
        self.temCelsius = temCelsius

    def convertFahrenheit(self):
        return (self.temFahrenheit * 9/5) + 32

    def convertCelsius(self):
        return (self.temCelsius - 32) * 5/9 


temp = Temprature(10,12)

print(temp.convertFahrenheit())
print(temp.convertCelsius())



class Student:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def  display(self):
        return self.name, self.role

    def setAge(self, age):
        self.age = age
    
    def setMarks(self, marks):
        self.marks = marks

    def getAge(self):
        return self.age

    def getMarks(self):
        return self.marks

stu = Student("Aram", "student" )
stu.setAge(12)
stu.setMarks("Good")

print(stu.display())
print(stu.getAge())
print(stu.getMarks())


class Time:
    def __init__(self, hours, minute):
        self.hours = hours
        self.minute = minute
   
    def addTime(t1, t2):
        addminut = t1.minute + t2.minute
        if addminut >= 60:
            res = addminut / 60 
            addhours = t1.hours + t2.hours + res
            resul = addminut % 60
            return addhours, resul
        return t1.hours + t2.hours, t1.minute + t2.minute
    def displayTime(self):
        return self.hours

    def displayMinute(self):
        return self.hours * 60 + self.minute


time1 = Time(2, 50)
time2 = Time(1, 20)

print(Time.addTime(time1, time2))




    

























































