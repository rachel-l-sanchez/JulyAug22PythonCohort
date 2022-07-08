# 1 Change the value 10 in x to 15. Once you're done,
# x should now be [ [5,2,3], [15,8,9] ].
#Change the last_name of the first student from 'Jordan' to 'Bryant'
#In the sports_directory, change 'Messi' to 'Andres'
#Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20}]

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30 

# 2 Create a function iterateDictionary(some_list) that,
# given a list of dictionaries, the function loops
# through each dictionary in the list and prints each key
# and the associated value.
def iterateDictionary(some_list):
    for i in some_list:
        for key,value in i.items():
            N = 2
            output = dict(list(i.items())[0:N])
            print(str(output))
            
sports_players = [
         {'Basketball':  'Kobe Bryant', 'Golf' : 'Tiger Woods'},
         {'Soccer' : 'Messi', 'Swimming' : 'Michael Phelps'},
         {'Baseball' : 'Felix Hernandez', 'Football' : 'Jerry Rice'}
]  
     
print(iterateDictionary(sports_players))

#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

# 3 Create a function iterateDictionary2(key_name, some_list)
# that, given a list of dictionaries and a key name,
# the function prints the value stored in that key for each dictionary.
# For example, iterateDictionary2('first_name', students)

def iterateDictionary2(key_name,list):
    for i in list:
        for key_name, val in i.items():
            try:
                items = i.keys()
                keys = iter(items)
                key1 = next(keys)
                res = (f"{key1} - {val}")
                key2= next(keys)
                res2= (f"{key2} - {val}")
                print(str(f"{res}, {res2}"))
            except: 
                return None
    
students = [   {'first_name': 'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
         ]

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

