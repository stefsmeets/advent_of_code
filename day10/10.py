filename = 'data.txt'

with open(filename) as f:
    lines = f.readlines()

corrupted_score_table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

incomplete_score_table = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

mapping = {
    '(': ')',
    '{': '}',
    '<': '>',
    '[': ']',
}

corrupted_score = 0
incomplete_scores = []

for chunk in lines:
    chunk = chunk.strip()
    
    is_corrupted = False
    heap = []

    for char in chunk:
        # print(''.join(heap), repr(char))
        
        if char in mapping:
            heap.append(char)
        
        elif not heap:
            print('heap empty')
            break
        
        else:
            lastchar = heap.pop()
            expected = mapping[lastchar]
            if expected != char:
                print(f'corrupted, got {char} expected {expected}')
                corrupted_score += corrupted_score_table[char]
                is_corrupted = True
                break
            else:
                assert expected == char

    if not is_corrupted:
        score = 0
        for char in reversed(heap):
            score *= 5
            closing = mapping[char]
            score += incomplete_score_table[closing]
        
        incomplete_scores.append(score)
        # print(heap, score)

print(f'{corrupted_score=}')

middle = len(incomplete_scores) // 2
middle_incomplete_score = sorted(incomplete_scores)[middle]

print(f'{middle_incomplete_score=}')
