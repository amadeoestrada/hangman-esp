"""
    Hangman-spa(nish):
    Version 1:
    This is a hangman game with spanish.
    This hangman uses words fetched from dictionaries at https://github.com/sbosio/rla-es
"""
__author__ = "Amadeo Estrada"
__date__ = "19 / Jul / 2020"

import game_func

def main():
    cont = 1
    player, difficulty = game_func.config()
    while cont:
        word = game_func.get_word(difficulty)
        game_func.play(word)
        cont = game_func.gameover(player)

main()