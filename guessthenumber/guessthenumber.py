from random import randrange

# this is used to manage the runner loop state
PLAY = True

# set the runner state to false
def exit_game():
  global PLAY
  play = False;

# function that displays end of game message
def display_stats(gave_up, num_tries, answer):
  msg = f'You gave up! The answer was {answer}' if gave_up else f'You won!'

  print(msg)
  print(f'Number of tries: {num_tries}')
  
  return True

def play_game():
  random_num = 1 + randrange(0, 99)
  found = False
  last_guess = None
  num_tries = 0

  while not found:
    if last_guess:
      print(f'Last Guess: {last_guess}')
    
    if num_tries > 0:
      print(f'Number of tries: {num_tries}')

    guess = int(input(('What is your guess (1 - 100) (-1 to give up): ')))

    if guess < 0:
      found = display_stats(true, num_tries, random_num)
      return

    num_tries += 1
    if guess == random_num:
      found = display_stats(true, num_tries, random_num)
      return

    if guess < random_num:
      print('Wrong number! (hint: The answer is greater than your choice)')
    else:
      print('Wrong number! (hint: The answer is less than your choice)')

  return

OPTIONS = {
  "1": play_game,
  "2": exit_game
}

while PLAY:
  print('[1]: Play')
  print('[2]: Exit')

  choice = input("What would you like to do: ")

  if choice in OPTIONS:
    options[choice]()
  else:
    print("Invalid option!")
