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
    #create a copy for tracking pool
    tracking_pool = []
    # use list insted of dictionary
    for key, value in LETTER_POOL.items():
        tracking_pool.append([key, value])
    
    letters = [] # this will be returned
    
    while len(letters) < HAND_SIZE:
        random_index = randint(0, len(tracking_pool) - 1) # 8
        picked_pair = tracking_pool[random_index] # ['I', 9 ]
        # print(picked_pair)
        LETTER = picked_pair[0]
        COUNT = picked_pair[1]
        
        # if picked_pair's count > 0, add the letter to letters list. 
        if COUNT > 0:
            # if value > 0, append the key and value - 1
            letters.append(LETTER)
            COUNT -= 1
            [LETTER, COUNT] # update the value 
            #if value == 0, do nothing
    
    # print("letters:", letters)
    return letters
    
# draw_letters()

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

    scores = []

    for word in words:
        scores.append((word, score_word(word)))
    
    print("scores: ", scores)

    best_pair = scores[0] # set 1st pair is the best_pair

    # loop scores-list, compare score and best_pair[1]. 
    for word, score in scores: # unpack to (word, score) 
        if score > best_pair[1]: # when score is higher than (, score) 
            best_pair = (word, score)

        elif score == best_pair[1]: # score is tied
            # if word len is 10 & best_pair's len is not 10, take the word
            if len(word) == 10 and len(best_pair[0]) != 10:
                best_pair = (word, score)
            # if word len is fewer than best_pair & best_pair's len is not 10, take the word
            elif len(word) < len(best_pair[0]) and len(best_pair[0]) != 10:
                best_pair = (word, score)
            # If the there are multiple words that are the same score and the same length, pick the first one in the supplied list -> keep the earlier one = do nothing

    # print(best_pair)
    return best_pair

# words = ["AAAAAAAAAA", "BBBBBB"]
# get_highest_word_score(words)

