from pathlib import Path

FILENAME = "U5.txt"
contents = Path(FILENAME)
data = contents.read_text()

#  --- Separate the data into lines
lines = data.split('\n')

#  --- Convert into text again
body = "\n".join(lines[1:])

#  --- Print the body
print(f"Body of the {FILENAME} file: ")
print(body)
