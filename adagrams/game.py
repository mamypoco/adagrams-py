from random import randint
from adagrams.asset import LETTER_POOL


def draw_letters():
    #create a copy of pool for tracking
    tracking_pool = []
    for key, value in LETTER_POOL.items():
        tracking_pool.append({key: value})
    
    letters = [] #create like ["A", "K", "S", "O", "R", "E", "T", "A", "I", "N"]
    
    counter = 1
    while counter <= 10:
        
        random_index = randint(0, len(tracking_pool) -1) # 3
        dict_item = tracking_pool[random_index] # {'A': 9 }
        
        # in {'B': 2}, if value > 0, append the key and -1 the value
        for key, value in dict_item.items(): 
            if value > 0:
                letters.append(key)
                value -= 1
                tracking_pool[random_index][key] = value #update the value in the tracking_pool
        
        counter += 1
    
    # print("tracking_pool", tracking_pool)
    print("letters:", letters)
    return letters
    
# draw_letters()

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
    # print(matched)
    # print(matched == word)
    return matched == word
    
# uses_available_letters("zebra", ["Z", "E", "B", "R", "A", "I", "O", "E", "C", "K"])

def score_word(word):
    # word could be lower case
    word = word.upper()
    
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
    # print(SCORE_CHART)
        
    # get a letter score (fast) via key
    def get_letter_score(letter_to_score):
        #return the value/score
        return SCORE_CHART[letter_to_score] 

    # sum the score
    score = 0
    for letter in word:
        score += get_letter_score(letter)
    # print("before length: ", score) 

    if len(word) in range(7, 11):
        score += 8
    # print("after length: ", score)
    return score


# word = "zebra"
# score_word(word)


def get_highest_word_score(words):
    # create () inside [("flower", 20), ("earth", 18), ("wonderful", 45)]
    # create {} inside [{"flower", 20}, {"earth", 18}, {"wonderful", 45}]
    scores = []

    for word in words:
        scores.append((word, score_word(word)))
    # for dict option
    # for word in words:
    #     scores.append({word: score_word(word)})
    
    print("scores: ", scores)

    best_pair = scores[0] # set 1st pair( , ) is the best_pair

    # tried to use dict pair {word: score} here, but could not find better way to access key without using separate for-loop

    # loop scores-list, compare score and best_pair[1]. Can't use max so use comparison
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

