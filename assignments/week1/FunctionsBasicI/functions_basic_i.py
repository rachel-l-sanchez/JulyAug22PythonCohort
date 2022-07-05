#1 will return 5 when called
def number_of_food_groups():
    return 5
print(number_of_food_groups())


#2 would return 5 when called but there is an undefined function in the print statement
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


#3 will only return the first return statement of 5
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())


#4 will return 5 and print 10
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())


#5 will print 5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)


#6 will print 3 + 5 = 8
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))


#7 will return "25" as a string
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))


#8 will print 100 then return 10. Second return statement is ignored since the function has already terminated
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9 will return 7 and ignore all other code blocks for the first print, return 14 when invoked, will return 7 + 14 
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10 will return 8 and ignore second return statement
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))


#11 print 500, print 500, print 300, print 500
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


#12 print 500, print 500, print 300 and return 300, print 500
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


#13 print 500, print 500, print 300 and return 300 and print 300 with the final print statement
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14 will have an error since function called inside foo has yet to be defined
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15 error 
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)