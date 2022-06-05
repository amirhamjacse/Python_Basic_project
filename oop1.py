class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
         

hasan = Employee('hasan', 'johan', 23999)
rohan = Employee('rohan', 'dana', 43000)

print(hasan.fname, rohan.fname)