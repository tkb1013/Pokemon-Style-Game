import random

# common moves between players    
class Player:
    def getMove(self):
        pass
    
    def attack(self, move, oppScore):
        if move == 1:
            oppScore -= random.randint(18,25)
        elif move == 2:
            oppScore -= random.randint(10,35)
        return oppScore
    
    def heal(self, myScore):
        if myScore > (100-18):
            return myScore + (100 - myScore)
        else:
            return myScore + random.randint(18,25)
        
        
# The user player's options
class User(Player):
    
    def name(self):
        return "User"
    
    def getMove(self):
        print("Select your move:")
        print("1. Moderate Attack")
        print("2. High or Low Attack")
        print("3. Heal")
        move = int(input())
        
        #will prompt the user to enter the correct command for move
        while(move != 1 and move != 2 and move != 3):
            print("Select your move:")
            print("1. Moderate Attack")
            print("2. High or Low Attack")
            print("3. Heal")
            move = int(input())

        return move
        
# The computer player's options        
class Computer(Player):
    
    def name(self):
        return "Computer"
    
    
    #computer player's move set is selected at random
    def getMove(self, myScore):
        move = random.randint(1,3)
        
        #if computer score is below 35, then it will have an increased chance of healing itself
        if(myScore<=35):
            move = random.choice([1,2,3,3])
        else:
            move = random.choice([1,1,2,2,3])
        return move
        
        
    print(random.randint(1,3))
    
def play(p1, p2):    
    p1Score = 100
    p2Score = 100
    
    '''
    p1 = Player()
    p2 = Player()
    '''
    
    print("Player 1's health:", p1Score)
    print("Player 2's health:", p2Score)
    
    #game continues until one player reaches 0 points
    while p1Score > 0 and p2Score > 0:
        
        #Player 1's turn
        print("It's Player 1's turn")
        
        if(p1.name() == "User"):
            p1Move = p1.getMove()
        elif(p1.name() == "Computer"):
            p1Move = p1.getMove(p1Score)
            
            
        if(p1Move == 3):
            print('Player 1 heals.')
            p1Score = p1.heal(p1Score)
            print('Current score:')
            print('Player 1 score:', max(0, p1Score))
            print('Player 2 score:', max(0, p2Score))
        elif(p1Move == 1 or p1Move == 2):
            if(p1Move == 1):
                print('Player 1 uses Moderate Attack on Player 2.')
            elif(p1Move == 2):
                print('Player 1 uses High or Low Attack on Player 2.')
            p2Score = p1.attack(p1Move, p2Score)
            print('Current score:')
            print('Player 1 score:', max(0, p1Score))
            print('Player 2 score:', max(0, p2Score))
            
        if(p2Score <= 0):
            break
        
        
        #Player 2's turn
        
        print("It's Player 2's turn")    
        if(p2.name() == "User"):
            p2Move = p2.getMove()
        elif(p2.name() == "Computer"):
            p2Move = p2.getMove(p2Score)
            
            
        if(p2Move == 3):
            print('Player 2 heals.')
            p2Score = p2.heal(p2Score)
            print('Current score:')
            print('Player 1 score:', max(0, p1Score))
            print('Player 2 score:', max(0, p2Score))
        elif(p1Move == 1 or p1Move == 2):
            if(p2Move == 1):
                print('Player 2 uses Moderate Attack on Player 1.')
            elif(p2Move == 2):
                print('Player 2 uses High or Low Attack on Player 1.')
            p1Score = p2.attack(p2Move, p1Score)
            print('Current score:')
            print('Player 1 score:', max(0, p1Score))
            print('Player 2 score:', max(0, p2Score))
            
            
        if(p1Score <= 0):
            break
            
        
    if p2Score <= 0:
        print("Player 2 faints. Player 1 wins!")
    elif p1Score <= 0:
        print("Player 1 faints. Player 2 wins!")
        


#randomly selects who goes first
r = random.randint(1,2) 
user = User()
comp = Computer()

if(r == 1):
    p1 = user
    p2 = comp
    print("You are Player 1.")
else:
    p1 = comp
    p2 = user
    print("You are Player 2.")
    

play(p1, p2)
        
    
