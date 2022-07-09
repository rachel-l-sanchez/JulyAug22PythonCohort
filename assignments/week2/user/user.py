# Attributes on function call: first_name, last_name, email, age
# default attributes is_rewards_member - default value of False
# default gold_card_points = 0

# methods display_info(self) - Have this method print all of the users'
# details on separate lines.
#enroll(self) - Have this method change the user's member status
# to True and set their gold card points to 200.
#spend_points(self, amount) - have this method decrease the user's
# points by the amount specified.

#Add logic in the enroll method to check if they are a member already, 
# and if they are, print "User already a member." and return False, otherwise return True.
#Add logic in the spend points method to be sure they have
#enough points to spend that amount and handle appropriately.

class User:
    def __init__(self,first_name,last_name, email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member= False
        self.gold_card_points = 0

    # method to output the attributes from the constructor init
    def display_info(self):
        print(f"{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}")

    # conditional statement to check first they are a rewards member
    # if true they won't be enrolled and it will return false
    
    # if false they will be enrolled and 
    def enroll(self):
            if self.is_rewards_member != True:
                self.is_rewards_member = True
                self.gold_card_points = self.gold_card_points + 200
                return True
            elif self.is_rewards_member ==True:
                print("User already a member.")
                return False
                   
    # amount is the amount of gold card points to spend
    # set a conditional so that the amount to spend does not exceed the number of points available      
    def spend_points(self,amount):
    
        points = self.gold_card_points
        if amount <= points:
            points = points - amount
            print(f"You now have {points} points left")
        elif amount> points:
            print(f'You only have {points} points to spend')
            return False
       

# assigning instance variables to constructor
john = User('john', 'smith', 'john.smith@gmail.com', 27)
john.is_rewards_member = True
john.gold_card_points = 50
michael = User('Mike', 'Sanchez','mikesanchez@gmail.com', 53)
michael.is_rewards_member = False
#assigning attribute values to sarah
sarah = User('Sarah', 'Merritt','sarahmerritt@gmail.com', 30)
sarah.is_rewards_member = True
sarah.gold_card_points = 200     
# printing attributes
john.display_info()
michael.display_info()
sarah.display_info()
# enrolling all and re-enrolling John
john.enroll()
michael.enroll()
sarah.enroll()
# spent_points method
p_spent = john.spend_points(50)
points_spend = michael.spend_points(80)
points_left = sarah.spend_points(40)
