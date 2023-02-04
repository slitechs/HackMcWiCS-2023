# Import modules
import object_detection as od
import text_detection as td

# Detect text from an image and print it out
td.detect_text('groceries.jpg')

# Detect objects from an image
output = od.query("groceries.jpg")

# Print out the name of the object
for item in output:
    print(item['label'])