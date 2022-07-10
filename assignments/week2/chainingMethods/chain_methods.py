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
        return self
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
        elif amount > points:
            print(f'You only have {points} points to spend')
        return self

# assigning instance variables to constructor
john = User('John', 'Smith', 'john.smith@gmail.com', 27)
michael =User('Mike', 'Sanchez', 'mikesanchez@gmail.com', 53)
michael.is_rewards_member = True
michael.gold_card_points = 50
#assigning attribute values to sarah
sarah = User('Sarah', 'Merritt','snmerritt@gmail.com', 30)
sarah.is_rewards_member = True
sarah.gold_card_points = 190
# calling methods
john.enroll()
john.spend_points(80).display_info()
michael.enroll()
michael.spend_points(50).display_info()
sarah.enroll()
sarah.spend_points(60).display_info()


