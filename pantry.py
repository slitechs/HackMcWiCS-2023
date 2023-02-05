# What's in my pantry?

# Import modules
from backend import object_detection as od, text_detection as td
from collections import Counter

import foodlist

# Print out the words
# print(tdresult)



result = []
tdresult = []
foods = {}

# Object detection and text recognition in images, for pantry items
def get_items(filename):
    # Detect objects from an image
    output = od.query('./uploads/'+filename)

    for item in output:
        print(item)
        if item['label'] != "dining table" and item['label'] != "bottle": # Prevents labling non-foods
            result.append(item['label'])
    

    # Detect text from an image
    tdresult = td.detect_text('./uploads/'+filename)

    # Add text-processed foods to list  

    for food in foodlist.common_foods:
        for word in tdresult:
            if word.lower() == food or (food in word.lower() and len(word.lower()) > len(food)):
                result.append(food)
            

    # Group results
    items = Counter(result).most_common()

    # Organize objects by item and amount
    for x in items:
        foods.update({x[0]:x[1]})


    return foods
