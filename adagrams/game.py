from random import randint

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
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass