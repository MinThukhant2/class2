


from distutils.command.install_egg_info import safe_name


class Emplyoee:
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Emplyoee.empCount += 1
    def displayEmplyoee(self):
        print("Name : " , self.name,"Salary : ", self.salary)

emp1 = Emplyoee("Min Min ", 30000000)
emp2 = Emplyoee("Min Thu ", 30000000)
emp3 = Emplyoee("Min Thu ", 30000000)
emp4 = Emplyoee("Min Thu ", 30000000)
emp45 = Emplyoee("Min Thu ", 30000000)

emp1.displayEmplyoee()
emp2.displayEmplyoee()
emp3.displayEmplyoee()
emp4.displayEmplyoee()
emp45.displayEmplyoee()
print("Total Emplyoee %d" % Emplyoee.empCount)
