LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

# SCORE_CHART = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}

# SCORE_TO_LETTERS = {
#     1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
#     2: ["D", "G"],
#     3: ["B", "C", "M", "P"],
#     4: ["F", "H", "V","W", "Y"],
#     5: ["K"],
#     8: ["J", "X"],
#     10: ["Q", "Z"],
# }

# def get_letter_map(score_to_letters):
#     map = dict()

#     for score, letters in score_to_letters.items():
#         for letter in letters:
#             map[letter] = score

#     return map

# SCORE_CHART = get_letter_map(SCORE_TO_LETTERS)

# def get_letter_score_fast(letter_to_score):
#     return SCORE_CHART[letter_to_score]


# def get_letter_score_slow(letter_to_score):
#     for score, letters in SCORE_TO_LETTERS.items():
#         for letter in letters:
#             if letter == letter_to_score:
#                 return score
#     return 0




# def make_original_format(score_chart):
#     map = dict()
#     for letter, score in score_chart.items():
#         map.get(score, []).append(letter)

#     return map