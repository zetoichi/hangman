import random
import time
import string

with open('sowpods.txt') as f:
  words = list(f)

print("\n### Welcome to a new game of HANGMAN! ###")
print("\nYour friend is in serious trouble and he needs you to save him! \nAre you ready to start playing...?\n")

start_playing = input("\nPress Y for yes or N for no\n")
start_playing = start_playing.upper()

while start_playing == 'Y':
  word = random.choice(words).strip()
  word_length = len(word) 

  print(word) 

  print("\nIn the hidden word lies the secret for saving your friend\'s life.")
  print("\nEvery wrong guess of a letter, your little friend is closer to his death!")
  print("\nYou can only guess wrong 8 times, if don't want to \'leave him hanging\'") 

  chances_left = 8
  attempts_num = 0  

  time.sleep(0.6)
  print("\nThe hidden word is {} letters long.".format(word_length))  

  # creates a series of asterisks that will be switched by the letters the user guessed
  word_guess = ''
  for i in range(word_length):
    word_guess += '*' 

  while word_guess != word:
    # makes a list out of the asterisk series, in order for them to be switchable
    word_guess_list = [word_guess[i] for i in range(word_length)]

    # defines message depending on number of attempts and chances left
    time.sleep(0.6)
    if chances_left == 8:
      if attempts_num == 0:
        letter_guess = input("\nTry your first guess...\n")
        attempts_num += 1
      elif attempts_num > 0:
        print("\nYour progress so far: " + word_guess) # keeps the users progress visible
        letter_guess = input("\nTry once again...\n")  
        attempts_num += 1
    elif chances_left == 7:
      print("\nYour progress so far: " + word_guess)
      letter_guess = input("\nThere goes your first wrong attempt. Don\'t worry, you still have {} left! Try once again...\n".format(chances_left))
      attempts_num += 1
    elif chances_left < 7 and chances_left > 1:
      print("\nYour progress so far: " + word_guess)
      letter_guess = input("\nTry once again...\n")
      attempts_num += 1
    elif chances_left == 1:
      print("\nYour progress so far: " + word_guess)
      letter_guess = input("\nThis is your last chance to save your friend, he\'s entering the tunnel!!\n")
      attempts_num += 1
    else:
      print("\nYou have lost after {} attempts. Your friend is dead, and it's all on you.".format(attempts_num))
      print("\nThe word you were looking for was {}".format(word))
      print("\nDo you want to give it another go..?")
      start_playing = input("\nPress Y for yes or N for no\n")
      start_playing = start_playing.upper()
      if start_playing == 'N':
        print("\nBetter luck next time!! Bye!") 
        break

    # checks if user entered one letter only. If they did, checks if guess is correct.
    # if correct, switches asterisk for guessed letter
    # if incorrect, tells the user how many chances he has left
    time.sleep(0.6)
    letter_guess = letter_guess.upper() 
    if len(letter_guess) == 1:
      if letter_guess in word_guess:
        letter_guess = input("\nYou already tried that letter. Once is enough! Try again...\n")
      if letter_guess not in word:
        chances_left -= 1
        print("\nSorry!! The letter you chose is not contained in the hidden word")
        print("\nYou have {} chances left.".format(chances_left))
      if letter_guess in word:
        print("\nGreat!! The letter {} is in the hidden word.".format(letter_guess))
        print("\nYou are one step closer to saving your buddy!\n")
        for i in range(len(word_guess_list)):
          if word[i] == letter_guess:
            word_guess_list[i] = letter_guess
        word_guess = ''.join(word_guess_list) # joins the list back to be shown to user
    else:
      print("\nThat's cheating! You can only guess one letter at a time.")
      letter_guess = input("\nWe\'ll let that one slide, tho. Try again...")
    if letter_guess not in string.ascii_letters:
      print("\nSymbols are never part of words!")
      letter_guess = input("\nYou\'ll never save your friend if you don\'t take this seriously. Try again...")
  
  if word_guess == word:
    print("\nYou won!! Your buddy may be a bit sore in the neck, but he is now safe and sound, thanks to you!!")
    print("\nYor skills can save many mor lives!! Do you want to play another game?")
    start_playing = input("\nPress Y for yes or N for no\n")
    start_playing = start_playing.upper()
    if start_playing == 'N':
      print("That's it then, maybe they can manage without you... See you next time!")

