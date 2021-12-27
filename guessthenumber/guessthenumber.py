from random import randrange
import logging

# this is used to manage the runner loop state
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S')
logging.info("Logging Number Guess...")

PLAY = True

def exit_game():
    """
    Sets Runner state to false
    """

    global PLAY
    PLAY = False

def display_stats(gave_up, num_tries, answer):
    """
    Displays end of game messages

    Parameters:
    gave_up (Boolean): indicates if user gave up
    num_tries (int): Number of tries
    answer (int): the correct answer

    Returns:
    Boolean: if game should end
    """

    msg = f'You gave up! The answer was {answer}' if gave_up else f'You won!'

    print(msg)
    print(f'Number of tries: {num_tries}')

    return True

def play_game():
    """Game Logic function
    """

    logging.info('Starting new game')
    random_num = 1 + randrange(0, 99)
    found = False
    last_guess = None
    num_tries = 0

    while not found:
        if last_guess:
            print(f'Last Guess: {last_guess}')

        if num_tries > 0:
            print(f'Number of tries: {num_tries}')
        try:
            logging.info('Requesting new guess')
            guess = int(input(('What is your guess (1 - 100) (-1 to give up): ')))
        except ValueError:
            print("Invalid option!")
            logging.error('User entered invalid guess')
            continue

        if guess < 0:
            logging.info('User gave up')
            found = display_stats(True, num_tries, random_num)
            return

        num_tries += 1
        if guess == random_num:
            logging.info('User successfully guessed number')
            found = display_stats(False, num_tries, random_num)
            return

        if guess < random_num:
            print('Wrong number! (hint: The answer is greater than your choice)')
            logging.info('User guessed lower')
        else:
            print('Wrong number! (hint: The answer is less than your choice)')
            logging.info('User guessed lower')

    return

OPTIONS = {
    "1": play_game,
    "2": exit_game
}

while PLAY:
    print('[1]: Play')
    print('[2]: Exit')

    CHOICE = input("What would you like to do: ")

    if CHOICE in OPTIONS:
        OPTIONS[CHOICE]()
        logging.info('User chose valid option')
    else:
        print("Invalid option!")
        logging.error('Invalid menu option')
