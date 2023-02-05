# What's in my pantry?

# Import modules
from backend import object_detection as od, text_detection as td
from collections import Counter

# Detect text from an image
tdresult = td.detect_text('uploads/'+'receipt.jpg')

# Print out the words
# print(tdresult)


# Detect objects from an image
output = od.query('uploads/groceries.jpg')

odresult = []
foods = {}

# for item in output:
    # odresult.append(item['label'])

# Print out the name of the object
# print(odresult)

def get_items(file_name):
    # Detect objects from an image
    output = od.query("uploads/"+file_name)

    for item in output:
        odresult.append(item['label'])

    items = Counter(odresult).most_common()

    # Organize objects by item and amount
    for x in items:
        foods.update({x[0]:x[1]})

    return foods


print(foods)
