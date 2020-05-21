HANGMAN_ASCII_ART =r"""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
"""

MAX_TRIES = 6

HANGMAN_PHOTOS = {0: '''x-------x''',\
1: '''\
x-------x
|
|
|
|
|

''', \
2: '''\
x-------x
|       |
|       0
|
|
|

''', \
3: '''\
x-------x
|       |
|       0
|       |
|
|

''', \
4: '''\
x-------x
|       |
|       0
|      /|\\
|
|

''', \
5: '''\
x-------x
|       |
|       0
|      /|\\
|      /
|

''', \
6: '''\
x-------x
|       |
|       0
|      /|\\
|      / \\
|

'''}
    
def welcome_screen():
    '''Prints the welcoming screen
    :return: None
    :rtype: None '''
    
    print(HANGMAN_ASCII_ART)
    print(MAX_TRIES)
    
def choose_word(file_path, index):
    '''Returns the word in the given index in the file in the given file path
    :param file_path: the given file path
    :param index: the given index to choose the word
    :type file_path: str
    :type index: int
    :return: the word in the given index in the file in the given file path
    :rtype: str '''
    
    chosen_word = ""
    
    with open(file_path, 'r') as file:
        words_file = file.read()
        all_words = words_file.split(' ')
        choose_word = all_words[(index - 1) % len(all_words)]

    return choose_word

def check_win(secret_word, old_letters_guessed):
    '''Checks if all the letter that composed the given word are in the given list
    :param secret_word: the word that the user needs to guess
    :param old_letters_guessed: the list of all the letter that already been guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True if all the letter that composed the given word are in the given list
    False otherwise
    :rtype: bool'''
    
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    
    return True        

def show_hidden_word(secret_word, old_letters_guessed):
    '''Creates string that shows which letters have been exposed
    and where there are letter that need to be revealed.
    :param secret_word: the word that the user needs to guess
    :param old_letters_guessed: the list of all the letter that already been guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: string that shows which letters have been exposed
    and where there are letter that need to be revealed
    :rtype: str'''
    
    my_str = ""
    
    for char in secret_word:
        if char in old_letters_guessed:
            my_str += char + ' '
        else:
            my_str += '_ '
    
    return my_str

def check_valid_input(letter_guessed, old_letters_guessed):
    '''Validates the user input. 
    :param letter_guessed: user choice
    :param old_letters_guessed: all the previous choices of the user
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: returns true only if the input 
    is one character and it's an english character and the letter is a new letter
    :rtype: bool'''
    
    if (not letter_guessed.isalpha()) or (len(letter_guessed) > 1):
        return False
        
    return letter_guessed not in old_letters_guessed

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    '''Update the guessed list or printing appropriate messege. 
    :param letter_guessed: user choice
    :param old_letters_guessed: all the previous choices of the user
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: returns true only if the input 
    is one character and it's an english character and the letter is a new letter
    :rtype: bool'''
    
    if check_valid_input(letter_guessed, old_letters_guessed):
        return True
    else:
        print('X')
        if old_letters_guessed != []:
            print('-> '.join(sorted(list(dict.fromkeys((old_letters_guessed))))))
        return False

def check_state(letter_guessed, secret_word, old_letters_guessed):
    '''Check if the given parameters are valid.
    :param letter_guessed: the user guess
    :param secret_word: the secret word
    :param old_letters_guessed: all the letters guessed so far
    :type letter_guessed: str
    :type secret_word: str
    :type old_letters_guessed: list
    :return: returns True if the given letter is not in the word and it is a english letter and if it is one letter
    False otherwise
    :rtype: bool'''

    return (letter_guessed not in secret_word) and (letter_guessed.isalpha()) and (len(letter_guessed) == 1) \
        and (letter_guessed not in old_letters_guessed) 

def main():
    welcome_screen()
    file_path = input('Enter file path: ') # for example: C:\files\words.txt
    index = int(input('Enter index: '))
    secret_word = choose_word(file_path, index)
    num_of_tries = 0
    letter_guessed = 'A'
    old_letters_guessed = []
    state = 0 # 0 - mistake, 1 - correct, 2 - invalid
    
    print("Let's start!\n")
    while num_of_tries < MAX_TRIES and not check_win(secret_word, old_letters_guessed):
        if state == 0:
            print(HANGMAN_PHOTOS[num_of_tries])
            print(show_hidden_word(secret_word, old_letters_guessed))
        
        letter_guessed = input('Guess a letter: ').lower()

        if try_update_letter_guessed(letter_guessed, old_letters_guessed) == True and (letter_guessed in secret_word):
            old_letters_guessed.append(letter_guessed)
            print(show_hidden_word(secret_word,old_letters_guessed))
            state = 1
        
        elif check_state(letter_guessed, secret_word, old_letters_guessed):
            state = 0
            old_letters_guessed.append(letter_guessed)
            print(':(\n')
            num_of_tries += 1

        else:
            state = 2
    
    if state == 1:
        print('WIN')
    else:
        print(HANGMAN_PHOTOS[num_of_tries])
        print(show_hidden_word(secret_word, old_letters_guessed))   
        print('LOSE')
        
    input("\nenter 'ENTER' to exit: ")

if __name__ == "__main__":
    main()
