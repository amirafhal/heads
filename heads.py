import random 
print("""Welcome to the Coin Guessing Game!
Choose a method to toss the coin:
1. Using random.random()
2. Using random.randint()""")
choice = int(input("Enter your choice (1 or 2): "))
if choice == 1:
  G = input("Enter your Guess (Heads or Tails): ")
  computer = random.random()
  if computer >= 0.5 :
    if G.lower() == "heads":
      print("Congratulations! You won!")
      print("The computer's coin toss result was: Heads")
    else:
       print("Sorry, you lost!")
       print("The computer's coin toss result was: Heads")
  else:
    if G.upper() == "TAILS":
       print("Congratulations! You won!")
       print("The computer's coin toss result was: Tails")
    else:
       print("Sorry, you lost!")
       print("The computer's coin toss result was: Tails")
elif choice == 2:
  Guess = input("Enter your Guess (Heads or Tails): ")
  c = random.randint(0,1)
  if c == 0 :
    if Guess.lower() == "heads":
       print("Congratulations! You won!")
       print("The computer's coin toss result was: Heads")
    else:
      print("Sorry, you lost!")
      print("The computer's coin toss result was: Heads")
  else:
    if Guess.lower() == "tails":
       print("Congratulations! You won!")
       print("The computer's coin toss result was: Tails")
    else:
      print("Sorry, you lost!")
      print("The computer's coin toss result was: Tails")
else:
  print("Invalid choice. Please select either 1 or 2.")
  print("Enter your choice (1 or 2): ")
