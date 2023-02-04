# What's in my pantry?

# Import modules
from backend import object_detection as od, text_detection as td
from collections import Counter

# Detect text from an image
tdresult = td.detect_text('uploads/receipt1.jpg')

# Print out the words
# print(tdresult)

# Detect objects from an image
output = od.query("uploads/groceries.jpg")

odresult = []

for item in output:
    odresult.append(item['label'])

# Print out the name of the object
print(odresult)

def get_items():
    # Detect objects from an image
    output = od.query("uploads/groceries.jpg")

    odresult = []

    for item in output:
        odresult.append(item['label'])

    # Print out the name of the object
    return odresult

items = Counter(odresult).most_common()

# print(items)

foods = {}

# Organize objects by item and amount
for x in items:
    foods.update({x[0]:x[1]})

print(foods)

# Get foods