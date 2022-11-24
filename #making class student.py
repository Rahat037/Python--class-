#making class student
'''class student:
    reg_no = None
    name = None

s1=student()
s1.reg_no='1213457'
s1.name='Mohit Kumar'
print(s1.name,s1.reg_no)'''


#######
'''class student:
    reg_no=None
    Name=None
    def details(self):
        name=input("Name: ")
        reg_no=input("reg_no:")
        return name + " " +reg_no

s1=student()
print(s1.details())
s2=student()
print(s2.details())'''


'''class student:
    def get_details(self):
        self.name=input('Name: ')
        self.reg_no=input("reg_no: ")
    def print_details(self):
        return self.name+ " "+self.reg_no
s1=student()
s1.get_details()
print(s1.print_details())'''


'''class student:
    def get_details (self,n,r):
        self.name=n
        self.reg_no=r
    def print_details(self):
        return self.name+" "+self.reg_no

s1=student()
s1.get_details('rahat','12220202')
s2=student()
s2.get_details('rat','1222077202')
print(s1.print_details())
print(s2.print_details())'''

#write a prg to declare a prg which contains 2 method to get details 


'''class employee:
    def get_details(self,n,e,s):
        self.name=n
        self.emp_id=e
        self.sal=s
    def print_details(self):
        print(self.name,self.emp_id,self.sal)
e1=employee()
e1.get_details('abc','emp101','8000')
e2=employee()
e2.get_details('abcd','efmp101','08000')
e1.print_details()
e2.print_details()'''

'''class student:
    def __init__ (self,n,r):
        self.name=n
        self.reg_no=r
    def print_details(self):
        return self.name+" "+self.reg_no

s1=student('rahat','161611')
print(s1.print_details())
s2=student('rahatk','1dd61611')
print(s2.print_details())'''

class car:
    def __init__ (self,m,c):
        self.modelnumber=m
        self.color=c
    def print_details(self):
        return self.modelnumber+" "+self.color

s1=car('Lamborgini','161611')
print(s1.print_details())
s2=car('Ferreari','1dd61611')
print(s2.print_details())

























