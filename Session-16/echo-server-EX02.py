import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        request = self.requestline.split(' ')
        raw_arg = request[1]
        clean_arg = raw_arg.split('?')
        argument = clean_arg[0]

        if argument == '/':
            contents = Path('form-EX02.html').read_text()

        elif argument == '/echo':
            argument1 = clean_arg[1]
            # -- Given the fact that in my url it appeared: http://localhost:8080/echo?msg=vita&%27chk=on
            # -- I had to add the %27
            arguments = argument1.split('&%27')
            value = arguments[0].split('=')[1]
            contents = Path('form-EX01.html').read_text()

            if len(arguments) > 1:
                chk, chk_value = arguments[1].split("=")
                print(chk, chk_value)
                if chk == "chk":
                    value = value.upper()

            print_value = f"<p>{value}</p>"
            contents += print_value

        else:
            contents = Path('Error.html').read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new one
    # -- client, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
