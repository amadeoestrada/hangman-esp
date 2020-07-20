"""
    This module contains all the functions used by hangman-esp(nish)
"""
__author__ = "Amadeo Estrada"
__date__ = "19 / Jul / 2020"

import random


def get_word(difficulty):
    """ This function fetches a word stored in one of the three dictionaries.
        Any of the three dictionaries is randomly picked. Then a word from is randomly
        chosen from the picked dictionary. If the chosen word doesn't match the
        difficulty level, another word is randomly picked.
        """
    if difficulty == 1:
        letras = 4  # 'letas' is characters in spanish. 4 is easy
    elif difficulty == 2:
        letras = 6  # 6 characters is medium difficulty
    else:
        letras = 8  # 8 characters is challenging
    workingfolder = 'dictionaries/'
    dic = ['NombresFemeninos.txt', 'NombresMasculinos.txt', 'NombresMasculinosFemeninos.txt']
    file = (workingfolder + random.choice(dic))
    L = []
    for line in open(str(file)):
        if line[0].isalpha():
            L.append(line.rstrip())
    word = random.choice(L)
    word = remove_nonalpha(word)
    while len(word) > letras:
        word = random.choice(L)
        word = remove_nonalpha(word)
    return word


def play(word):
    """ This function allows the player to play.
        Firstly, the accents are removed from the word to be guessed. Otherwise
        it would be extremely difficult to guess.
        Supports full word guesses. Does not support partial word guesses
        Warns the player about letters he already input.
        Shows the user how many tries he has left in the game.
    """
    tries = int(0)
    hyph = ''
    word2 = accent_substitution(word)
    for c in word:
        hyph += '_'
    guesses = []
    while True:
        display_hangman(tries)
        if tries > 5:
            print('\n¡AHORCADO! La palabra correcta era \'', word, '\'\n')
            break
        print('Adivina la palabra: ' + hyph + '\n')
        tried_char = input('Oportunidades ' + str(6 - tries) + ': ')
        tried_char2 = tried_char.lower()
        if tried_char in guesses:
            print('\n¡Ya probaste la letra \'', tried_char, '\'\n')
            continue
        else:
            guesses.append(tried_char)
        if len(tried_char.rstrip()) < 1:
            print('\nIntroduce una letra\n')
            continue
        elif len(tried_char.rstrip()) == 1:
            if tried_char2 in word2:
                index_list = []
                j = 0
                for c in word2:
                    if c == tried_char2:
                        index_list.append(j)
                    j += 1
                for k in index_list:
                    hyph = hyph[0:k] + word[k] + hyph[k+1:]
                if hyph == word2:
                    print('\n¡FELICIDADES! Adivinaste la palabra \'', word, '\'\n')
                    break
                print('\nEncontraste una letra.\n')
                continue
            else:
                print('\n\'', tried_char, '\' no está en la palabra. Intenta otra vez.\n')
                tries += 1
                continue
        else:
            if tried_char2 == word2:
                print('\n¡FELICIDADES! Adivinaste la palabra\n')
                break
            else:
                print('\n\'', tried_char, '\' no es en la palabra correcta. Intenta otra vez.\n')
                tries += 1
                continue

def display_hangman(tries):
    """ This function displays the hangman according to the number of tries.
    """
    hangman = ["""
    ┌───────┐
    │       │
    │      
    │     
    │     
    │      
    │     
    |     
    │          
    ┴------------""",
    """
    ┌───────┐
    │       │
    │       O
    │     
    │     
    │     
    │     
    |     
    │          
    ┴------------""",
    """
    ┌───────┐
    │       │
    │       O
    │      /|\\
    │     
    │     
    │     
    |     
    │          
    ┴------------""",
    """
    ┌───────┐
    │       │
    │       O
    │      /|\\
    │     / │ \\
    │     
    │    
    |     
    │          
    ┴------------""",
    """
    ┌───────┐
    │       │
    │       O
    │      /|\\
    │     / │ \\
    │      / \\
    │    
    |    
    │          
    ┴------------""",
    """
    ┌───────┐
    │       │
    │       O
    │      /|\\
    │     / │ \\
    │      / \\
    │     |   |
    |    
    │          
    ┴------------""",
    """
    ┌───────┐
    │       │
    │       O
    │      /|\\
    │     / │ \\
    │      / \\
    │     |   |
    |     ┘   └
    │          
    ┴------------"""]
    print(hangman[tries])


def remove_nonalpha(word):
    """ This function removes the '/' and suffix characters from the chosen word.
    """
    if '/' in word:
        i = word.find('/')
        word = word[0:i]
    return word


def config():
    """ This function asks the player's name and the difficulty setting for the
        game.
        The difficulty level is only allowed to be within 1,2, and 3. The logic
        won't allow the player to set an input other than those numbers.
        """
    player = input('¿Cuál es tu nombre? \n\t\t\tR.: ')
    print('\n\n')
    print(player, 'elige la dificultad: \n\t\t\t\tFácil\t...\t1\n',
          '\t\t\t\tMedia\t...\t2\n\t\t\t\tDifícil\t...\t3\n')
    difficulty = 0
    while difficulty == 0:
        difficulty = input('\t\t\t\tR.: ')
        try:
            int(difficulty)
        except:
            print('\nERROR EN LA ENTRADA DE DATOS\n')
            print('\n', player, 'elige la dificultad: \n\t\t\t\tFácil\t...\t1\n',
                  '\t\t\t\tMedia\t...\t2\n\t\t\t\tDifícil\t...\t3\n')
            difficulty = 0
        else:
            if difficulty not in ['1', '2', '3']:
                print('\nSELECCIÓN NO VÁLIDA\n')
                print('\n', player, 'elige la dificultad: \n\t\t\t\tFácil\t...\t1\n',
                      '\t\t\t\tMedia\t...\t2\n\t\t\t\tDifícil\t...\t3\n')
                difficulty = 0
    print('\n\n')
    print(player, 'la dificultad que elegiste es: ', difficulty, '. Juguemos.')
    return player, int(difficulty)


def gameover(player):
    """ This function allows the player to continue playing or quit the game
    """
    while True:
        ans = input('¿Deseas seguir jugando? (Si o No)\nR.: ').upper()
        if ans == 'SI':
            print('\n')
            return 1
        elif ans == 'NO':
            print('\n')
            return 0
        else:
            print('\nNo entendí. ')
            continue


def accent_substitution(word):
    """ Spanish is a complex language with multiple accents. This functions simplifies
        the language, otherwise, this hangman game would be EXTREMELY difficult
    """
    word2 = ''
    for c in word:
        if 'á' == c:    word2 += 'a'
        elif 'é' == c:  word2 += 'e'
        elif 'í' == c:  word2 += 'i'
        elif 'ó' == c:  word2 += 'o'
        elif 'ú' == c:  word2 += 'u'
        elif 'ü' == c:  word2 += 'u'
        else: word2 += c
    return word2