#question 1
print("<------solution 1-------->")
a=3
try:
    if(a<4):
        a=a/(a-3)
      
except ZeroDivisionError:
    print('cannot divide by zero')
print(a)


#question 2
print("<------solution 2-------->")
l=[1,2,3]
try:
     print(l[3])
except IndexError:
     print("index error")



#question 3
'''
print("<------solution 3-------->")
An exception
Name Error: Hi there
'''

#question 4

'''
print("<------solution 4-------->")
-5.0
a/b result in 0
'''

#question 5
print("<------solution 5-------->")
#import error

try:
    import aa
except ImportError as msg:
    print(msg)

#value error
    
try:
     a=int(input("value: "))
     print(a)
except ValueError:
     print("Enter desired input")


#index error
     
l=[1,2,3]
try:
  print(l[3])
except IndexError:
  print("index error")
  
