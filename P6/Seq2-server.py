import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

Sequences = [
    "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]

bases = ["A", "C", "G", "T"]
FOLDER = "../Session-04/"
EXT = '.txt'


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')
        request = self.requestline.split(' ')
        raw_arg = request[1]
        clean_arg = raw_arg.split('?')
        argument = clean_arg[0]

        if argument == '/':
            contents = Path('form-4.html').read_text()

        elif argument == '/ping':
            contents = f"""
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                          <title> PING </title >
                        </head >
                        <body>
                        <h2> PING OK!</h2>
                        <p> The SEQ2 server is running </p>
                        <a href="/">Main page</a>
                        </body>
                        </html> """

        elif argument == '/get':
            argument1 = clean_arg[1].split('&')
            name, value = argument1[0].split('=')
            value = int(value)
            sequence = Sequences[value]
            contents = f"""
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                          <title> GET </title >
                        </head >
                        <body>
                        <h2> Sequence number {value}</h2>
                        <p> {sequence} </p>
                        <a href="/">Main page</a>
                        </body>
                        </html> """

        elif argument == '/gene':
            argument1 = clean_arg[1].split('&')
            name, gene = argument1[0].split('=')
            sequence = Seq()
            sequence.read_fasta(FOLDER + gene + EXT)
            gene_str = str(sequence)
            contents = f"""
                       <!DOCTYPE html>
                       <html lang = "en">
                       <head>
                       <meta charset = "utf-8" >
                         <title> GENE </title >
                       </head >
                       <body>
                       <h2> Gene: {gene}</h2>
                       <textarea readonly rows="20" cols="80"> {gene_str} </textarea>
                       <br>
                       <br>
                       <a href="/">Main page</a>
                       </body>
                       </html>"""

        elif argument == '/operation':
            argument1 = clean_arg[1].split('&')
            name, sequence = argument1[0].split("=")
            name, operation = argument1[1].split("=")
            seq = Seq(sequence)
            if operation == 'comp':
                result = seq.complement()
            elif operation == 'rev':
                result = seq.reverse()
            else:
                length = seq.len()
                num_bases = []
                perc_bases = []
                for element in bases:
                    counter_bases = seq.count_base(element)
                    percentage = round((seq.count_base(element) * 100 / seq.len()), 2)
                    num_bases.append(counter_bases)
                    perc_bases.append(percentage)

                result = f"""
                        <p>Total length: {length}</p>
                        <p>A: {num_bases[0]} ({perc_bases[0]}%)</p>
                        <p>C: {num_bases[1]} ({perc_bases[1]}%)</p>
                        <p>G: {num_bases[2]} ({perc_bases[2]}%)</p>
                        <p>T: {num_bases[3]} ({perc_bases[3]}%)</p>"""

            contents = f"""
                    <!DOCTYPE html>
                    <html lang = "en">
                    <head>
                    <meta charset = "utf-8" >
                      <title> OPERATION </title >
                    </head >
                    <body>
                    <h2>Sequence</h2>
                    <p>{seq}</p>
                     <h2>Operation</h2>
                    <p>{operation}</p>
                     <h2>Result</h2>
                    <p>{result}</p>
                    <br>
                    <br>
                    <a href="/">Main page</a>
                    </body>
                    </html>"""

        else:
            contents = Path('Error.html').read_text()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))

        return


Handler = TestHandler

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Server stopped by the user")
        httpd.server_close()
