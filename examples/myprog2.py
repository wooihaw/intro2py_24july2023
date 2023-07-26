import mypackage.module1 as m1
import mypackage.module2 as m2
m1.greet('Alibaba')
m2.depart('Alibaba')

from mypackage import module1 as m
m.greet("John")

from mypackage.module1 import greet
greet('Peter')
