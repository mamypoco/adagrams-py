from random import randint
# from adagrams.asset import LETTER_POOL

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

HAND_SIZE = 10 # define constant to tacke magic number

def draw_letters():
    # create a copy for tracking pool
    tracking_pool = []
    # use list instead of dict
    for letter, count in LETTER_POOL.items():
        # create flat list using letter only for probability ["A", "A", "A", "B", "B"]
        tracking_pool += [letter] * count 
        # tracking_pool.append([key, value]) this would create inside list

    print("tracking_pool:", tracking_pool)
    
    letters = [] # this will be returned
    
    while len(letters) < HAND_SIZE:
        random_index = randint(0, len(tracking_pool) - 1) # 8
        # once you append letter by index, remove it from pool
        letters.append(tracking_pool[random_index])
        tracking_pool.pop(random_index)
    
    print("letters:", letters)
    return letters
    
draw_letters()

def uses_available_letters(word, letter_bank):
    updated_letter_bank = letter_bank.copy()

    for letter in word: # loop through "zebra"
        letter = letter.upper()
        #loop through updated_letter_bank
        for bank_letter in updated_letter_bank: 
            # if letter in word matches bank_letter
            if letter == bank_letter:
                # remove the letter from updated_letter_bank
                updated_letter_bank.remove(letter)
                break
            else:
                return False
            
    # once the word is all available from the updated_letter_bank, 
    return True
    
# uses_available_letters("zebra", ["Z", "E", "B", "R", "A", "I", "O", "E", "C", "K"])

def score_word(word):

    word = word.upper()

    SCORE_CHART = {
        "A": 1, 
        "E": 1,
        "I": 1,
        "O": 1,
        "U": 1,
        "L": 1,
        "N": 1,
        "R": 1,
        "S": 1,
        "T": 1,
        "D": 2,
        "G": 2,
        "B": 3,
        "C": 3,
        "M": 3,
        "P": 3,
        "F": 4,
        "H": 4,
        "V": 4,
        "W": 4,
        "Y": 4,
        "K": 5,
        "J": 8,
        "X": 8,
        "Q": 10,
        "Z": 10
    }
        
    # get a letter score (fast) via key
    def get_letter_score(letter_to_score):
        #return the value/score
        return SCORE_CHART[letter_to_score] 

    # sum the score
    score = 0
    for letter in word:
        score += get_letter_score(letter)
    # print("before length: ", score) 

    BONUS_MIN_LENGTH = 7
    # BONUS_MAX_LENGH = 10 # this won't need
    BONUS_POINTS = 8

    if len(word) >= BONUS_MIN_LENGTH:
        score += BONUS_POINTS
    return score


def get_highest_word_score(words):
    # get the score for the word and compare in the same for-loop
    best_word = words[0] # set 1st word is the best_word
    best_score = score_word(best_word) # set the 1st score is the best_score

    for word in words[1:]:
        score = score_word(word) # in the loop, get score for each word

        if score > best_score: # when score is higher than best_score
            best_word, best_score = word, score

        elif score == best_score: # score is tied
            
            if len(word) == 10 and len(best_word) != 10:
                best_word = word
            
            elif len(word) < len(best_word) and len(best_word) != 10:
                best_word = word

    return best_word, best_score

# words = ["AAAAAAAAAA", "BBBBBB"]
# get_highest_word_score(words)

