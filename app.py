# Import modules
import object_detection as od
import text_detection as td

# Detect text from an image and print it out
result = td.detect_text('receipt.jpg')

# Print out the words
print(result)

# Detect objects from an image
output = od.query("groceries.jpg")

# Print out the name of the object
# for item in output:
    # print(item['label'])