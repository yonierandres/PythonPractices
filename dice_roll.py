import random as r

def run():

    def roll_dice():   
                roll = r.randint(1,6)
                return roll

    n_roll = int(input("how many times do you want to roll? :"))
    n_dices = int(input("how many dices wanna use? 1 or 2? "))
    player1_name = str(input("type your name player 1: "))
    player2_name = str(input("type your name player 2: "))
    

    if n_roll > 0:

        if n_dices == 1:
            for i in range(1,n_roll+1):
                roll1 = roll_dice()
            
                print("in the roll",i,"the result is",roll1)


        elif n_dices == 2:
            for i in range(1,n_roll+1):
                roll2 = roll_dice()
                roll3 = roll_dice()
                    
                print("in the roll",i, "the dice one result is",roll2,"and the dice two result is",roll3)
                
                if roll2 == roll3:
                        print("Good Luck", player1_name, "!!! you got a pair")

    else:
        print("why you don't want to play? are you afraid",player1_name, "?")
        print("you'll got lucky today", player1_name)

if __name__ == "__main__":
    run()

