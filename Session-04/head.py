from pathlib import Path

FILENAME = "RNU6_269P.txt"
file = Path(FILENAME)
data = file.read_text()

#  --- Separate the data into lines
lines = data.split('\n')
print(f"First line of the {FILENAME} file:")
print(lines[1])
