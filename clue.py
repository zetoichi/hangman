import random

def give_clue(word):
  hint_i_1 = random.randrange(len(word))
  hint_i_2 = random.randrange(len(word))
  
  # functionality for replacing all instances of a hint
  def replace_all(hint_i):
    for i in range(len(word)):
      if word[i] == word[hint_i]:
        clue_list[i] = word[hint_i]
    return clue_list
  
  # avoids dupicate hints
  while hint_i_2 == hint_i_1:
    hint_i_2 = random.randrange(len(word))
  
  # gives one or two clues depending on word length
  clue_list = ['*' for i in range(len(word))]
  clue_list = replace_all(hint_i_1)
  if len(word) > 8:
    clue_list = replace_all(hint_i_2)
      
  return ''.join(clue_list)
