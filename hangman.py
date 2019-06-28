import random
print ("\033[1;36;40m                                                                       Welkom  bij galgje!                                                                                    ")
print ("Uitleg: Er verschijnen straks streepjes op uw beeld. Vervolgens krijgt u de mogelijkheid een letter te kiezen, waarvan u denkt dat de letter in het woord zit. Bij een goed gekozen letter komt hij op de juiste plek in het woord te staan. Bij een foutgekozen letter komt hij ergens anders op het scherm te staan en is er 1 van je 10 beurten voorbij. Zodra je alle letters, binnen je 10 beurten, hebt geraden, heb je gewonnen. Heb je niet het woord binnen 10 beurten geraden, heb je verloren.                                \033[1;36;40m \n")

def get_guess():
  foute_letters = []
  dashes = "-"* len(secret_word)
  guesses_left = 10 
  

  while guesses_left > -1 and not dashes == secret_word:
    
    print ("Het woord:")
    print(dashes)
    print("Beurten over:")
    print (str(guesses_left))
  
    guess = input("Gok een letter:")
    
    if len(guess) != 1 or guess.isdigit():
      print ("Per beurt mag je één letter gokken en geen cijfers invoeren.")
      
 
    elif guess in secret_word:
      print ("Deze letter zit in het woord!")
      dashes = update_dashes(secret_word, dashes, guess)
    
    else:
      print ("Deze letter zit niet in het woord! ")
      foute_letters.append(guess)
      print (foute_letters)
      guesses_left -= 1
 
  if guesses_left < 0:
    print ("Je hebt verloren, het woord was: " + str(secret_word))
  
  else:
    print ("Gefeliciteerd, je hebt gewonnen. Het woord was: " + str(secret_word))

def update_dashes(secret, cur_dash, rec_guess):
  result = ""
  
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess     
      
    else:

      result = result + cur_dash[i]
      
  return result
    
words = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

secret_word = random.choice(words)
get_guess()
