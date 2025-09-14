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

#randint: randomly choose in range by index using parameter

def draw_letters():
    #create a copy of pool for tracking
    tracking_pool = []
    for key, value in LETTER_POOL.items():
        tracking_pool.append({key: value})
    
    letters = [] #create placeholder like ["A", "K", "S", "O", "R", "E", "T", "A", "I", "N"]
    
    counter = 1
    while counter <= 10:
        
        random_index = randint(0, len(tracking_pool) -1) # 3
        dict_item = tracking_pool[random_index] # {'A': 9 }
        
        #for dict_item {'B': 2}, if value > 0, append the key and -1 the value
        for key, value in dict_item.items(): 
            if value > 0:
                letters.append(key)
                value -= 1
                tracking_pool[random_index][key] = value #update the value in the tracking_pool
        
        counter += 1
    
    print("letters:", letters)
    print("tracking_pool", tracking_pool)
    return letters
    
draw_letters()

def uses_available_letters(word, letter_bank):
    updated_letter_bank = letter_bank.copy()
    
    matched = ""

    for letter in word: # "zebra"
        for bank_letter in updated_letter_bank: 
            # find out if every letter found
            if letter.upper() == bank_letter:
                #only take first match
                matched += letter
                updated_letter_bank.remove(letter.upper())
                break
    print(matched)
    print(matched == word)
    return matched == word
    
uses_available_letters("zebra", ["Z", "E", "B", "R", "A", "I", "O", "E", "C", "K"])

def score_word(word):
    # word could be lower case
    word = word.upper()
    print(word)
    # create a dict like { "A": 1, "E": 1 ...} to lookup
    # score chart - original format
    SCORE_TO_LETTERS = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V","W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"],
    }

    # create letter to score dict
    def get_letter_map(score_to_letters):
        map = {}

        for score, letters in score_to_letters.items():
            for letter in letters:
                map[letter] = score
        return map

    # save as a vaiable
    SCORE_CHART = get_letter_map(SCORE_TO_LETTERS)
    print(SCORE_CHART)
        
    # get a letter score (fast) via key
    def get_letter_score(letter_to_score):
        #return the value/score
        return SCORE_CHART[letter_to_score] 

    # sum the score
    score = 0
    for letter in word:
        score += get_letter_score(letter)
    print("before length: ", score) 

    if len(word) in range(7, 11):
        score += 8
    print("after length: ", score)
    return score


word = "star"
score_word(word)


def get_highest_word_score(word_list):
    pass
