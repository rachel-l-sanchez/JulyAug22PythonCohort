# Basic
for i in range(0,151):
    print(i)

# Multiples of five
for i in range(5,1005, 5):
    print(i)

# Counting, the Dojo Way
for i in range(1, 101):
    if i % 10:
        print("Coding Dojo")
    elif i % 5:
        print("Coding")
    else: 
        print(i)

# Whoa. That Sucker's Huge
for i in range(1, 500000):
    sum = 0
    if i % 2 == 1:
        sum += i
    print(sum)

# Countdown by Fours
for i in range(2022,0, -4):
    if i % 2 == 0:
        print(i)

# Flexible Counter
lowNum = 2
highNum = 25
mult = 3
for i in range(lowNum, highNum, mult):
    print(i)


