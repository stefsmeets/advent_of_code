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
    
    heap = []

    for char in chunk:
        
        if char in mapping:
            heap.append(char)
        
        elif mapping[heap.pop()] != char:
            corrupted_score += corrupted_score_table[char]
            break

    else:
        score = 0
        for opening in reversed(heap):
            score *= 5
            closing = mapping[opening]
            score += incomplete_score_table[closing]
        
        incomplete_scores.append(score)

print(f'part 1: {corrupted_score=}')

middle = len(incomplete_scores) // 2
middle_incomplete_score = sorted(incomplete_scores)[middle]

print(f'part 2: {middle_incomplete_score=}')
