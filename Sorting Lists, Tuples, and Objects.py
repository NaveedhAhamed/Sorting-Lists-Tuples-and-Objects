li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li)
print(s_li)
print(li)
#even if this came with negative vales it will sort ly

#to go descending
s_li = sorted(li,reverse=True)
print(s_li)
print(li)


#another ex
tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print(s_tup)



#this will sort only keys
di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('Dict:', s_di)



#if we are considering the absolute value despite negativity
li=[-6,-5,-4,1,4,3]
s_li = sorted(li,key=abs)
print(s_li)



#sometimes we need custom functions in case if keys got mixed up

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

def e_sort(emp):
    return emp.age, emp.salary

s_emp = sorted(employees, key=e_sort)

print(s_emp)

from operator import attrgetter
s_emp = sorted(employees, key=attrgetter('age'))
print(s_emp)
