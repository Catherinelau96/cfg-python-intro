import random
import requests
import time
import sys

# Delay Printing, to give it the old game.boy feel
# https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'base_experience': pokemon['base_experience'],
    }


if __name__ == '__main__':
    delay_print('Player 1\n')
    player1 = input('Enter Pokémon Trainer Name: \n')


def game():
    my_pokemon = random_pokemon()
    delay_print("Let the Pokémon Battle begin!\n")
    delay_print('This is your Pokémon card: {}\n'.format(my_pokemon['name']))
    print('  ID............... {}'.format(my_pokemon['id']))
    print('  HEIGHT........... {}'.format(my_pokemon['height']))
    print('  WEIGHT........... {}'.format(my_pokemon['weight']))
    print('  BASE EXPERIENCE.. {}\n'.format(my_pokemon['base_experience']))
    opponent_pokemon = random_pokemon()

    stat_choice = input('Which stat do you want to use? (id, height, weight, base_experience) ')
    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    if my_stat > opponent_stat:
        delay_print(f'Trainer {player1} Win!\n')
        result = 'Win'
    elif my_stat < opponent_stat:
        delay_print(f'Trainer {player1} Lose!\n')
        result = 'Lose'
    elif my_stat == opponent_stat:
        delay_print('Draw!\n')
        result = 'Draw'

    delay_print('This was your opponent\'s card: {}\n'.format(opponent_pokemon['name']))
    print('  ID............... {}'.format(opponent_pokemon['id']))
    print('  HEIGHT........... {}'.format(opponent_pokemon['height']))
    print('  WEIGHT........... {}'.format(opponent_pokemon['weight']))
    print('  BASE EXPERIENCE.. {}\n'.format(opponent_pokemon['base_experience']))

    return result

def announce_final_winner(player_score, computer_score):
    print('-----------------------')
    delay_print('The game is over!\n')
    if player_score > computer_score:
        delay_print(f'Congratulation trainer {player1}, you\'re a Pokémon Master!')
    elif computer_score > player_score:
        delay_print(f'Trainer {player1} have lost the battles! Better Luck next time!')
    elif player_score == computer_score:
        delay_print('Neither of you are winners!')
        rematch_choice = input('Do you want a final game to determine the winner? Yes/No ')
        if rematch_choice == 'Yes':
            result = game()
            if result == 'Win':
                delay_print(f'Congratulation trainer {player1}, you\'re a Pokémon Master!')
            elif result == 'Lose':
                delay_print(f'Sorry Trainer {player1}, you loose the game!')
            elif result == 'Draw':
                delay_print(f'Trainer {player1}, fate is merciless, no one wins the game!')


number_of_rounds = 3
my_score = 0
opponent_score = 0

for round in range(number_of_rounds):
    delay_print(f'Trainer {player1}, you\'re in round: {round + 1}\n')
    result = game()
    if result == 'Win':
        my_score += 1
    elif result == "Lose":
        opponent_score += 1

announce_final_winner(my_score, opponent_score)