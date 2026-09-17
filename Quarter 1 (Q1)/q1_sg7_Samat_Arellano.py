class Glassware:
    def __init__(self, kindofglassware):
        self.kindofglassware = kindofglassware
        print(f"{kindofglassware} exists.")


class Beaker(Glassware):
    def __init__(self,kindofglassware,size):
        self.size = size
        super().__init__(kindofglassware)
        print (f"There is a {self.size} beaker.")

    def __del__(self):
        print("Beaker is reduced to atoms.")


class Tray:
    def __init__(self):
        print("Tray is created.")
        self.beaker = [
            Beaker("Beaker","50mL"),
            Beaker("Beaker","100mL"),
            Beaker("Beaker","150mL"),
            Beaker("Beaker","200mL"),
            Beaker("Beaker","250mL"),
        ]

        
    def count(self):
        
        for x in self.beaker:
            print (f"I have a beaker at {id(x)}")
            print ("                                                      ")
    def __del__(self):
        del self.beaker

Lab = Tray()
Lab.count()
del Lab

