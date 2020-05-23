import http.client
import json
import termcolor
from Seq1 import Seq

GENES = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362', }


all_bases = ["A", "C", "G", "T"]
# This will be used to obtain the most frequent base
counter = 0
freq_base = ""

# Ask for a gene
gene_input = input("Write the gene name: ")

# We need to add the Id of our gene
Server = "rest.ensembl.org"
Endpoint = "/sequence/id/"
Id = GENES[gene_input]
Parameters = "?content-type=application/json"
URL = Server + Endpoint + Id + Parameters


print()
print(f"Server: {Server}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(Server)
# -- Send the request message, using the GET method.
try:
    conn.request("GET", Endpoint + Id + Parameters)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
response = json.loads(data1)

# Information of the gene
Description = response["desc"]


termcolor.cprint(f"Gene:", "green", end=" ")
print(gene_input)
termcolor.cprint(f"Description:", "green", end=" ")
print(Description)


# Introduce the sequence
seq = Seq(response["seq"])
s_length = seq.len()
counter_A = seq.count_base(all_bases[0])
counter_C = seq.count_base(all_bases[1])
counter_G = seq.count_base(all_bases[2])
counter_T = seq.count_base(all_bases[3])
per_A = "{:.1f}".format(100 * counter_A / s_length)
per_C = "{:.1f}".format(100 * counter_C / s_length)
per_G = "{:.1f}".format(100 * counter_G / s_length)
per_T = "{:.1f}".format(100 * counter_T / s_length)

# Print the length
termcolor.cprint(f"Total length:", "green", end=" ")
print(s_length)

termcolor.cprint(f"A", "blue", end=" ")
print(f"{counter_A} {per_A}%")
termcolor.cprint(f"C", "blue", end=" ")
print(f"{counter_C} {per_C}%")
termcolor.cprint(f"G", "blue", end=" ")
print(f"{counter_G} {per_G}%")
termcolor.cprint(f"T", "blue", end=" ")
print(f"{counter_T} {per_T}%")

# For printing the most frequent base
dictionary = seq.seq_count()
list_values = list(dictionary.values())
max_base = max(list_values)
ci = dictionary.items()

termcolor.cprint("Most frequent Base", 'green', end="")
print(f": {all_bases[list_values.index(max_base)]}")
