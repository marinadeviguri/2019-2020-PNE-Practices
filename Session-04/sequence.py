from pathlib import Path

FILENAME = "ADA.txt"
file = Path(FILENAME)
data = file.read_text()
lines = data.split("\n")
body = "".join(lines[1:])


print(f"The total number of bases of the file {FILENAME} is: ")
print(len(body))
