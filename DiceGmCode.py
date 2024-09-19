#random module needed for six-sided dice
import random
#asks for player's name
user_name = input("Hi there! Please enter your name to start the game! ")
number_of_rounds = int(input("How many rounds of the game would you like to play? "))
number_of_turns = int(input("How many turns would you like each round to be? "))

#Variable that keep updating the score for each turn before appending it
#into the score lists at end of each round
user_points = 0
computer_points = 0

#Lists that store the user and computer points for each round of the game
user_score = []
computer_score = []

#function responsible for rolling the dice and updating the score varibles for each turn this function also displays both the players' rolls and scores for each turn
def rolls_and_score_numbers ():
  global user_points
  global computer_points

  user_roll = input ("\nYour turn to roll, " + user_name + "! Enter 'roll' to get a dice number! ")
  while (user_roll.lower() != "roll" ):
    user_roll = input ("\nYour turn to roll, " + user_name + "! Enter 'roll' to get a dice number! ")
  if (user_roll == "roll"):
    #the user's six-sided dice
    user_dice = random.randint(1,6)
    user_points = user_points + user_dice 
    #the computer's six-sided dice
    computer_dice = random.randint(1,6)
    computer_points = computer_points + computer_dice
    print (user_name + " rolled: " + str(user_dice))
    print("Now it is the computer's turn")
    print ("Computer rolled: " + str(computer_dice))
    print("\n" + user_name + "'s current score: " + str(user_points))
    print("Computer's current score: " + str(computer_points))

#function responsible for appending the players' points received at the end of every round
def append_scores ():
  global user_score
  global computer_score
  user_score.append(user_points)
  computer_score.append(computer_points)

#this dictionary is used to keep track of the number of wins for each player which helps determine the final winnner, who has the highest wins 
User_name = user_name
Computer = "Computer"
number_of_wins = {
  User_name: 0,
  Computer: 0
}

#function responsible for compared the players' scores for each round, declaring the round's winners, and updating the number_of_wins dictionary, which then help decide the ultimate winner based on the highest number of wins
def compare_scores_and_play_again (number_of_wins, number_of_rounds, user_score, computer_score):
  #index of eveery element or score stored in the score lists
  element = 0
  #repeats for every round
  for y in range (number_of_rounds):
    #if user scored more than computer
    if (user_score[element] > computer_score[element]):
      print("\n" + user_name + " won round " + str(element + 1) + " !")
      #updates the number of wins by 1 in the dictionary
      number_of_wins[User_name] = number_of_wins[User_name] + 1
    #if user scored less than computer
    elif (user_score[element] < computer_score[element]):
      print("\nComputer won round " + str(element + 1) + "!")
      number_of_wins[Computer] = number_of_wins[Computer] + 1
    #if user scored less same as the computer
    else:
      print ("\nRound " + str(element + 1) + " was a tie!")
    element = element + 1 

  #if user has more wins than the computer
  if (number_of_wins[User_name] > number_of_wins[Computer]):
    print("Thus, " + user_name + " is the ultimate winner!!")
  #if user has the same wins than the computer
  elif (number_of_wins[User_name] == number_of_wins[Computer]):
    print("Thus, it is an ultimate tie!!")
  #if user has less wins than the computer
  else:
    print("Thus, the computer is the ultimate winner!!")

#function responsible for repeating the game if the user wants to play it again. Or ending the game if the user does not want to continue
def new_game (play_again):
    if (play_again == "YES"):
      #scores are set to 0 for new game
      user_score = []
      computer_score = []

      number_of_rounds = int(input("How many rounds of the game would you like to play? "))
      number_of_turns = int(input("How many turns would you like each round to be? "))
      #calls the function that runs the whole game once again
      dice_game(number_of_rounds, number_of_turns)
    else:
      print("Thank you for playing the DiceGame, " + user_name + "! I hope you had a good time!")

#this function gathers all the functions created needed to run the game in the right order
def dice_game(rounds, turns_per_round):
  for each_round in range (rounds):
    #starting rounf 1 and transition to other rounds
    print("\nTime for round " + str(each_round + 1) + "!")
    for each_turn in range (turns_per_round):
      rolls_and_score_numbers()
    append_scores()
    global user_points
    global computer_points
    #intializing score variable once again for the next possible game
    user_points = 0
    computer_points = 0  
  compare_scores_and_play_again(number_of_wins, number_of_rounds, user_score, computer_score)
  play_again = input("\nWould like to play the game again? Enter 'YES' to play and 'NO' to stop. ")
  #runs th game again if user says "YES"
  new_game(play_again)

#holistic function, which starts and runs the whole game
dice_game(number_of_rounds, number_of_turns)
