import random

print("""

  _                                             
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       



""")
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
 

chosen_word = random.choice(word_list)


display = []
wordlength = len(chosen_word)


wrongwords =[]
for _ in range(wordlength):
    display += "_"
print("".join(display))

lives = wordlength + 5
print(f"You have {lives} lives")

end = False
while not end:
  
  guess = input("Guess a letter: \n").lower()
  
  for position in range(wordlength):
      letter = chosen_word[position]
      if letter == guess:
          display[position] = letter


  if guess not in chosen_word:
    lives -=1
    wrongwords.append(guess)
    editedlist = "".join(wrongwords)
    print(f"WRONGLETTERS: {editedlist.upper()}\n")
    
    print(f"You have {lives} lives left\n")
  print("".join(display))

  if lives == 0:
    end = True
    print("YOU LOST ALL YOUR LIVES HAVE GONE")
  if "_" not in display:
    print("You have won the word was "+(chosen_word).upper())
    end = True
    