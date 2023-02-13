class Date:
    def __init__(self,y, m, d):
        self.y = y
        self.m = m
        self.d = d
        
        def show(self):
            print(self.y, "/", self.m, "/", self.d)
            
        def GetMounthName(self):
            if self.m == 1:
                print("farvardin")
            elif self.m == 2:
                print("ordibehesht")
            elif self.m == 3:
                print("khordad")
            elif self.m == 4:
                print("tir")
            elif self.m == 5:
                print("mordad")
            elif self.m == 6:
                print("shahrivar")
            elif self.m == 7:
                print("mehr")
            elif self.m == 8:
                print("aban")
            elif self.m == 9:
                print("azar")
            elif self.m == 10:
                print("dey")
            elif self.m == 11:
                print("bahman")
            elif self.m == 12:
                print("esfand")
                
        def IsValidDate(self):
            if not 1 <= self.d <= 30:
                print("False")
            if not 1 <= self.m <= 12:
                print("False")
            if not 0 < self.y <= 9999:
                print("False")
            else:
                print("True")
                
date1 = Date(1379, 7, 3)

date1.show()

date1.GetMounthName()

date1.IsValidDate()