import random
print ("\033[1;36;40m                                                                       Welkom  bij galgje!                                                                                    ")
print ("Uitleg: Er verschijnen straks streepjes op uw beeld. Vervolgens krijgt u de mogelijkheid een letter te kiezen, waarvan u denkt dat de letter in het woord zit. Bij een goed gekozen letter komt hij op de juiste plek in het woord te staan. Bij een foutgekozen letter komt hij ergens anders op het scherm te staan en is er 1 van je 10 beurten voorbij. Zodra je alle letters, binnen je 10 beurten, hebt geraden, heb je gewonnen. Heb je niet het woord binnen 10 beurten geraden, heb je verloren.                                \033[1;36;40m \n")

def get_guess():
  
  # streepjes geven lengte van woord aan 
  # 10 beurten
  dashes = "-"* len(secret_word)
  guesses_left = 10 
  
  # dit gaat in een loop als de volgende dingen waar zijn
  # 1. het aantal beurten geraden of over is groter dan -1
  # 2. de dash string is niet het woord
  while guesses_left > -1 and not dashes == secret_word:
    
    # toon het aantal beurten dat je nog over hebt 
    print ("Het woord:")
    print(dashes)
    print("Beurten over:")
    print (str(guesses_left))
    
    # input vragen van speler
    guess = input("Gok een letter:")
    
    # dit komt in beeld, als er een verkeerde input is gegeven 
    if len(guess) != 1 or guess.isdigit():
      print ("Per beurt mag je één letter gokken en geen cijfers invoeren.")
      
    # als de letter in het woord zit dan update je de dashes 
    # corresponding dash with the correct index the guess belongs to in the 
    # secret word
    elif guess in secret_word:
      print ("Deze letter zit in het woord!")
      dashes = update_dashes(secret_word, dashes, guess)
      
    # Als de letter niet in het woord zit, krijg je dat te zien en gaat er een beurt af
    else:
      print ("Deze letter zit niet in het woord! ")
      guesses_left -= 1
    
  if guesses_left < 0:
    print ("Je hebt verloren, het woord was: " + str(secret_word))
  
  # Als de dash string hetzelfde is als het woord aan het einde dan wint de speler
  else:
    print ("Gefeliciteerd, je hebt gewonnen. Het woord was: " + str(secret_word))
    
# de function updates de string van dashes door het vervangen van de dashes
# met de letters die hetzelfde zijn als het woord als de speler ze correct gokken
def update_dashes(secret, cur_dash, rec_guess):
  result = ""
  
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess     # voegd beurt aan string toe als het goed gegokt is
      
    else:
      # voeg de dash toe aan index i als het niet hetzelfde is als de gok
      result = result + cur_dash[i]
      
  return result
    
words = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

secret_word = random.choice(words)
get_guess()
