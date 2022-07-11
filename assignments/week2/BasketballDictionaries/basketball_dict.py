#Update the constructor to accept a dictionary
# with a single player's information instead of 
# individual arguments for the attributes.

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}

team_list = [
    {
        'name': 'Shaquille Oneil',
        'position': 'Point Guard',
        'age': '37',
    },
    { 
        'name': 'Kobe Bryant',
        'position': 'Forward',
        'age': '30',
    }
]     
class Player:
    new_players = []
    def __init__(self, players):
        self.players = players
    
    # method to print the object clearly
    def __repr__(self) -> str:
        return f"Player dictionary: {self.players}"
    
    #4 Bonus Add a get_team(cls, team_list) @class method
    
    @classmethod
    def get_team(cls, team_list):
        cls.team_list = team_list
        for team in cls.team_list:
            cls.new_players.append(team)

# #2 instantiating Player instances
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

player_kevin.get_team(team_list)

# 3
# diving deeper into the list to access the dictionaries
# using a for loop for the dictionaries and appending to a new list
new_team = []
for i in range(0, len(players)):
    for player in players:
        new_team.append(player)
  

            