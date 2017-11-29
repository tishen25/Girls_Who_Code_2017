"""
   Tiffany Shen
   11/27/17
   Girls Who Code Application
   Assignment: Rock_Paper_Scissors.py

   This program will introduce the game, continually prompt the user to play games of rock, paper, scissors,
   and print the winner to the console.
   
"""

# This function prints out an introduction of what the program does
def intro():
   print "Welcome to a game of rock, paper, scissors!"
   print "There will be two players: player 1 and player 2."
   print "Input either rock, paper, or scissors into the console"
   print "for each player!"

# This function takes the player number as a parameter and prompts the user
# to type in rock, paper, or scissors, reprompts if an invalid response
# is given, and returns the valid input
def prompt(player):
   print "%s enter a move (rock/paper/scissors): " %(player)
   input = raw_input().lower()
   while ((input != "rock") and (input != "paper") and (input != "scissors")):
      print "%s try again (rock/paper/scissors): " %(player)
      input = raw_input().lower()
   return input

# This function takes in two players as parameters and rrints which
# player wins or if it is a tie
def play(p1, p2):
   if (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
      print "Player 1 wins!"
   elif (p2 == "rock" and p1 == "scissors") or (p2 == "scissors" and p1 == "paper") or (p2 == "paper" and p1 == "rock"):
      print "Player 2 wins!"
   else:
      print "It's a tie!"   

   
intro()
play_again = "y"
while (play_again == "y"):
   print ""
   p1 = prompt("Player 1")
   p2 = prompt("Player 2")
   play(p1, p2)
   print "Would you like to play again? [y/n] "
   play_again = raw_input().lower()
   