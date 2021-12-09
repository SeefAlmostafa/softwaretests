import random


class Robot:
        robotName = None
        health_level = 0


        def __init__(self, name):
               self.robotName = name
               self.health_level = random.randrange(0,101)

        



        def say_hi(name):
                print("Hallo " + name)

        def introduce(self):
                print("Hallo, mein Name ist " + self.robotName)

        def calculate(self, zahl1, op, zahl2):
                if(self.is_healthy):
                        if(op == '+'):
                                return zahl1 + zahl2
                        elif(op == '-'):
                                return zahl1 - zahl2
                        elif(op == '*'):
                                return zahl1 * zahl2
                        elif(op == '/'):
                                if(zahl2 == 0):
                                        return ("Durch 0 darf nicht geteilt werden!!!")
                                else:
                                        return zahl1 / zahl2
                        elif(op == '%'):
                                return zahl1 % zahl2
                        else:
                                return ("Operation nicht bekannt!!!")
                else:
                        return ("Roboter ist defekt!!!")



        def is_healthy(self):
                if(self.health_level < 50):
                        return False
                else:
                        return True




r1 = Robot("Mark")

print(r1.is_healthy())
Robot.say_hi("Julian")

print(r1.calculate(3,'/',0))