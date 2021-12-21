from functools import cache
from collections import Counter
from itertools import product

filename = 'data.txt'

with open(filename) as f:
    player1, player2 = f.readlines()

pos1 = int(player1.strip()[-1])
pos2 = int(player2.strip()[-1])


def deterministic_die(sides=100):
    value = 0
    while True:
        yield value % 100 + 1 
        value += 1


die = deterministic_die()

scores = [0, 0]
positions = [pos1, pos2]
player = 0
rolls_per_turn = 3
N_ROLLS = 0

while max(scores) < 1000:
    N_ROLLS += rolls_per_turn
    roll = sum(next(die) for _ in range(rolls_per_turn))
    positions[player] = (positions[player] + roll - 1) % 10 + 1
    scores[player] += positions[player]
    player = int(not player)

loser = min(scores)

print(f'part 1: {loser*N_ROLLS=}')


quantum_rolls = Counter(sum(c) for c in product((1,2,3), repeat=3))

@cache
def quantum_turn(position_1, position_2, score_1=0, score_2=0):
    if score_2 >= 21:
        return (0, 1)

    win_counter = [0, 0]

    for roll, n in quantum_rolls.items():
        new_position = (position_1 + roll - 1) % 10 + 1
        wins_2, wins_1 = quantum_turn(position_2, new_position, score_2, score_1 + new_position)
        
        win_counter[0] += wins_1*n
        win_counter[1] += wins_2*n
    
    return win_counter


wins = quantum_turn(pos1, pos2)

print(f'part 2: {max(wins)=}')
