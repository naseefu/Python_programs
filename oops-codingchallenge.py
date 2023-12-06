class hospital:
    def __init__(self,admin,doc,sister,dep):
        self.admin = admin
        self.doc = doc
        self.sister = sister
        self.dep = dep
    def getinfo(self):
        self.admin = input("enter the admin name: ")
        self.doc = input("enter the doc name: ")
        self.sister = input("enter the sister name: ")
        self.dep = input("enter the department name:")
class department(hospital):
    def display(self):
        print("admin name is : ",self.admin)
        print("doctor name is : ",self.doc)
        print("sister name is : ",self.sister)
        print("department name is : ",self.dep)
class patientward:
    def __init__(self,name,age,num,dis):
        self.name = name
        self.age = age
        self.num = num
        self.dis = dis
    def info(self):
        self.name = input("enter name of patient:")
        self.age = int(input("enter the age: "))
        self.num = int(input("enter the phone number: "))
        self.dis = input("enter the disease: ")
    def disp(self):
        print("Name of patient: ",self.name)
        print("age of patient: ",self.age)
        print("phone number of patient : ",self.num)
        print("Disease of patient : ",self.dis)
a = department("","","","")
a.getinfo()
a.display()
b = patientward("","","","")
b.info()
b.disp()