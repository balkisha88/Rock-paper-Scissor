import random
import time

def menu(option): #menu function to tell which option is selcted
	if option==1:
		return "Stone"
	elif option==2:
		return "Paper"
	elif option==3:
		return "Scissor"
		
def rules(player,comp): #rules function to decide who wins
    if (player==1 and comp==2) or (player==2  and comp==1):
        print("***** Paper wins*******\n")
        result=2
        return result
    elif (player==2 and comp==3) or (comp==2 and player==3):
        print("******Scissor wins*****\n")
        result=3
        return result
    elif (player==1 and comp==3) or (comp==1 and player==3):
        print("******Stone Wins******\n")
        result=1
        return result
    
    

def main():
    
	print("****Stone Paper Scissor****")
	round=int(input("Enter number of rounds\n"));
	print("Select from these options: \n 1:Stone \n 2:Paper \n 3:Scissor \n ")
	player_score=0
	comp_score=0
	i=1
	while i<=round:
		player=int(input("Enter your choice: "))
		while player >3 or player < 0:
		    player=int(input("\nPlease enter valid choice\n"))
		player_choice=menu(player)
		print("\nYou have selected {}".format(player_choice))
		print("\nIts Computer's turn now:\n ")
		comp=random.randint(1,3)
		while comp==player: #To check if computer randomly selected the same option as user
		    comp=random.randint(1,3)
		comp_choice=menu(comp)
		time.sleep(2)
		print("I have selected {}\n".format(comp_choice))
		time.sleep(2)
		result=rules(player,comp)
		if result==player:
		    player_score+=1
		else:
		    comp_score+=1
		
		print("At the end of round {} \nYour Scores are {} \nComputer's Score are {}  " .format(i,player_score,comp_score))
		i=i+1
	
	time.sleep(2)
	if player_score>comp_score:
	    print("\n**User wins**")
	elif comp_score>player_score:
	    print("\n**Computer Wins**")
	else:
	    print("\n**Its a draw**")
    
	
if __name__=='__main__':
    
	main()
	play=input("want to play more Type Y for Yes and N for NO\n");
	while play=='Y':
	    main()
	    play=input("want to play more Type Y for Yes and N for NO\n");
	print ("\nThanks for Playing")  
	
	
