import random

money = 100

#Write your game of chance functions here
def heads_or_tail_game(bet, guess): 
  global money
  print ("Make sure you pick higher than zero.")
  if bet > money:
    print ("Sorry dont have enough money. Please try again.\n!")
  else:
    number = random.randint(1,2)
    if number == 1:
      result = "Heads"
    else:
      result = "Tails"
    print ("You flipped a " + result)

    if guess.lower() == result.lower():
      money += bet
      print ("Wheyy no money lost!" + str(bet) + " !")
      print ("Your current total of money is £" + str (money))
    else:
      money = money - bet
      print ("You have lost £" + str(-bet))
      print ("Your current total of money is £" + str (money))
    
def cho_han (bet, guess):
  global money
  print ("You are playing 'Cho Han'")
  if bet > money:
    print ("You cannot bet more than you already have!")
  else:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    value_sum = dice1 + dice2
    print ("You rolled a total of " + str   (value_sum))
    if value_sum % 2 == 0:
      result = "Even"
    else:
      result = "Odd"
    if guess.lower() == result.lower():
      money += bet
      print ("Wheyy you won £" + str(bet) + " !")
      print ("Your current total of money is £" + str (money))
    else:
      money = money - bet
      print ("Ahh never mind you lost this time £" + str(-bet))
      print ("Your current total of money is £" + str (money))

def card_wars (bet):
  global money
  print ("You are now playing 'Card Wars'")
  if bet > money:
    print ("You cannot bet more than you already have!")
  else:
    cards = [1,2,3,4,5,6,7,8,9,10,11,12,13] * 4
    cards.sort()
    player = random.choice(cards)
    print ("You draw a " + str(player))
    cards.remove (player)
    opponent = random.choice(cards)
    print ( "Your opponent drew a " + str (opponent))
    if player > opponent:
      money += bet
      print ("Wheyy you on £" + str(bet) + " !")
      print ("You current total is £" + str (money))
    if player < opponent:
      money = money - bet
      print ("Ohh no you have lost £" + str(-bet))
      print ("Your current total is £" + str (money))
    if player == opponent: 
      print ("It is a tie! You neither win nor lose.")
      print ("Your current total is £" + str (money))
    
def roulette (bet, guess):
  global money
  print ("You are now playing 'Roulette'")
  if bet > money:
    print ("You cannot bet more than you already have!")
  else:
    roulette_numbers = [00] + list(range(38))
    roll = random.choice (roulette_numbers)
    if roll == 0:
      result ='neither'
    elif roll % 2 == 0:
      result = "Even"
    else:
      result = "Odd"
    print ("You landed at " + str(roll))
    if isinstance (guess, int) and guess == roll:
      money += bet*10
      print ("You won £" + str(bet*10) + " !")
      print ("You current total is £" + str (money))
    elif isinstance (guess, int) and guess != roll:
      money -= bet*3
      print ("Uhh ooh you lost £" + str(bet*3) + " !")
      print ("You current total is £" + str (money))
    if isinstance (guess, str) and guess.lower() == result.lower():
      money += bet
      print ("Wheyy you won £" + str(bet) + " !")
      print ("You current total of money is £" + str (money))
    elif isinstance (guess, str) and guess.lower() != result.lower():
      money -= bet
      print ("Uhh ooh you lost £" + str(bet) + " !")
      print ("Your grand total of money is £" + str (money))

      
          
    
  





#Call your game of chance functions here
heads_or_tail_game (20, "taIls")
print ()
cho_han (30, "OdD")
print ()
card_wars(50)
print ()
roulette (20, "EVen")