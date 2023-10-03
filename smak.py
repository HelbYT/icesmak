zminna1 = ""
zminna2 = ""
zminna3 = ""


class Ice:
    
    def printall():
        global zminna1
        global zminna2
        global zminna3
        print("Your smaks: " + zminna1 + ", " + zminna2 + ", " + zminna3 + ".")

class Smak1(Ice):
    def __init__(self, smak1):
        self.smak1 = smak1
        global zminna1
        zminna1 = smak1 

class Smak2(Ice):
    def __init__(self, smak2):
        self.smak2 = smak2
        global zminna2
        zminna2 = smak2
    
class Smak3(Ice):
    def __init__(self, smak3):
        self.smak3 = smak3
        global zminna3
        zminna3 = smak3

smak1 = Smak1("Strawberry")
smak2 = Smak2("Banana")
smak3 = Smak3("Chocolate")
Ice.printall()