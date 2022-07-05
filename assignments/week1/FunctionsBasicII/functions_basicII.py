# list countdown from input

def countdown(num):
    my_list = []
    for num in range(0, num):
        my_list.append(num)
        num += 1
    return my_list

print(countdown(10))

# Print and return
def print_and_return(list):
    print(list[0])
    return list[1]

returnedList = [1,2] 
print(print_and_return(returnedList))  

# first plus length
def first_plus_length(list):
    x = list[0]
    y = len(list)
    sum = x + y
    return(sum)

print(first_plus_length([1,3,5]))

# values greater than second
def values_greater_than_second(input_list):
    my_list = []
    for i in range(0, len(input_list)):
        if input_list[i] > input_list[1]:
            my_list.append(input_list[i])
            print(len(my_list))
            return my_list
    if len(my_list) == 2:
        return False

print(values_greater_than_second([1,2]))

#this length, that value
def length_and_value(size, value):
    list_size = []
    for i in range(0, size):
        list_size.append(value)

length_and_value(5, 10)
