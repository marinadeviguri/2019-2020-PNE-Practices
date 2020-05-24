import http.server
import socketserver
import termcolor
import json
import http.client
from Seq import Seq


PORT = 8080
HOSTNAME = "rest.ensembl.org"

class TestHandler(http.server.BaseHTTPRequestHandler):


#Created this function in order to know what are the parameters requested:
    def endpoints(self, url):
        dictionary = dict()
        if '?'in url:
            url_split1 = url.split('?')[1]
            url_split2 = url_split1.split(" ")[0]
            endpoints_list = url_split2.split("&")
            for endpoint in endpoints_list:
                try:
                    key = endpoint.split("=")[0]
                    value = endpoint.split("=")[1]
                    dictionary[key] = value
                except IndexError:
                    pass
        return dictionary

    #Main function of the program
    def do_GET(self):
        codigo_respuesta = 200
        res_json = False

        termcolor.cprint(self.requestline, 'green')

        if self.path == "/":
            with open("index.html", "r") as f:
                contents = f.read()

        elif self.path[0:12] == "/listSpecies":
            parameters = self.endpoints(self.path)
            if 'limit' in parameters:
                try:
                    limit = int(parameters['limit'])
                except:
                    limit = 0
            else:
                limit = 0

            #Make the request to the API and obtain the list of the species:
            conn = http.client.HTTPConnection(HOSTNAME)
            conn.request("GET", "/info/species?content-type=application/json")
            r1 = conn.getresponse()
            text_json = r1.read().decode("utf-8")
            conn.close()
            list = json.loads(text_json)
            list = list['species']
            if limit == 0:
                limit = len(list)
            else:
                limit = limit
            if 'json' in parameters:
                res_json = True
                contents = []
                count = 0
                for i in list:
                    specie_name = i['display_name']
                    contents.append(specie_name)
                    count = count + 1
                    if count == limit:
                        break
                contents = json.dumps(contents)
            else:
                contents = """
                <html>
                <body>
                <ol>
                <h3 align=center><p style="color:#fe70f4";><u>SPECIES LIST</u></p>"""
                count = 0
                for i in list:
                    contents = contents+"<li>"+i['display_name']+"</li<br>"
                    count = count + 1
                    if count == limit:
                        break
                contents = contents+"""</ol> 
                </body>
                </html>
                """

        elif self.path[0:10] == "/karyotype":
            parameters = self.endpoints(self.path)
            if parameters == {}:
                codigo_respuesta = 400

                #If the endpoint requested isn´t correct, an error file is opened:
                with open("unavailable.html", "r") as f:
                    contents = f.read()

            elif 'specie' not in parameters or parameters['specie'] == '':
                codigo_respuesta = 400
                #If the parameter is empty:
                with open("unavailable.html", "r") as f:
                    contents = f.read()
            else:
                specie = parameters['specie']
                conn = http.client.HTTPConnection(HOSTNAME)
                conn.request("GET", "/info/assembly/"+specie+"?content-type=application/json")
                r1 = conn.getresponse()
                text_json = r1.read().decode("utf-8")
                conn.close()
                response = json.loads(text_json)

                #If there appears an error in the console, an error file is displayed:
                if 'error' in response:
                    codigo_respuesta = 400
                    with open("error.html", "r") as f:
                        contents = f.read()
                else:
                    karyotype_list = response['karyotype']
                    if karyotype_list == []:
                        codigo_respuesta = 400
                        with open("error.html", "r") as f:
                            contents = f.read()

                    #If the JSON checkbox is selected:
                    elif 'json' in parameters:
                        res_json = True
                        contents = json.dumps(karyotype_list)

                    #If the JSON checkbox is not selected:
                    else:
                        contents = """
                                   <html>
                                   <body>
                                   <ul>
                                   <h3 align=center><p style="color:#f8fe70";><u>SPECIE KARYOTYPE</u></p>"""
                        for i in karyotype_list:
                            contents = contents + "<li>" + i + "</li<br>"
                        contents = contents + """</ul> 
                                   </body>
                                   </html>
                                   """

        elif self.path[0:17] == "/chromosomeLength":
            parameters = self.endpoints(self.path)
            if parameters == {}:
                codigo_respuesta = 400
                with open("unavailable.html", "r") as f:
                    contents = f.read()

            #If the parameter requested is not correct, an error file is displayed
            elif 'chromo' not in parameters or 'specie' not in parameters or parameters['chromo'] == '' or parameters['specie'] == '':
                codigo_respuesta = 400
                with open("unavailable.html", "r") as f:
                    contents = f.read()

            else:
                chromo = parameters['chromo']
                specie = parameters['specie']
                conn = http.client.HTTPConnection(HOSTNAME)
                conn.request("GET", "/info/assembly/"+specie+"?content-type=application/json")
                r1 = conn.getresponse()
                text_json = r1.read().decode("utf-8")  # En string format
                conn.close()
                response = json.loads(text_json)
                if 'error' in response:
                    codigo_respuesta = 400
                    with open("error.html", "r") as f:
                        contents = f.read()
                else:
                    list = response['top_level_region']
                    length = "This chromosome does not exist for the specie selected"
                    for i in list:
                        if i['name'] == chromo:
                            length = i['length']
                    if 'json' in parameters:
                        res_json = True
                        contents = json.dumps(length)
                    else:
                        contents = """
                                              <html>
                                              <body>
                                              <ul>
                                              <h3 align=center><p style="color:#adfe70";><u>CHROMOSME LENGTH</u></p>"""
                        contents = contents + "<li>" + "The length of the chromosome  " + chromo + ",  specie  " + specie +",  is: " + str(length) + "</li>"
                        contents = contents + """</ul> 
                                              </body>
                                              </html>
                                          """

        elif self.path[0:8] == "/geneSeq":
            parameters = self.endpoints(self.path)
            if parameters == {}:
                codigo_respuesta = 400
                with open("unavailable.html", "r") as f:
                    contents = f.read()

            elif 'gene' not in parameters or parameters['gene'] == '':
                codigo_respuesta = 400
                with open("unavailable.html", "r") as f:
                    contents = f.read()

            else:
                gene = parameters['gene']
                conn = http.client.HTTPConnection(HOSTNAME)
                conn.request("GET", "/homology/symbol/human/" + gene + "?content-type=application/json")
                r1 = conn.getresponse()
                text_json = r1.read().decode("utf-8")  # En string format
                conn.close()
                response = json.loads(text_json)
                if 'error' in response:
                    codigo_respuesta = 400
                    with open("error.html", "r") as f:
                        contents = f.read()
                else:
                    id = response['data'][0]['id']
                    conn.request("GET", "/sequence/id/" + id + "?content-type=application/json")
                    r1 = conn.getresponse()
                    text_json = r1.read().decode("utf-8")  # String format
                    conn.close()
                    dictionary = json.loads(text_json)
                    human_sequence = dictionary['seq']
                    if 'json' in parameters:
                        res_json = True
                        contents = json.dumps(human_sequence)
                    else:
                        contents = """
                                              <html>
                                              <body>
                                              <ul>
                                              <h3 align=center><p style="color:#fed570";><u>SEQUENCE OF A HUMAN GENE</u></p>"""
                        contents = contents + "<li>" + human_sequence + "</li<br>"
                        contents = contents + """</ul> 
                                              </body>
                                              </html>
                                              """

        elif self.path[0:9] == "/geneInfo":
            parameters = self.endpoints(self.path)
            if parameters == {}:
                codigo_respuesta = 400
                with open("unavailable.html", "r") as f:
                    contents = f.read()

            elif 'gene' not in parameters or parameters['gene'] == '':
                codigo_respuesta = 400
                with open("unavailable.html", "r") as f:
                    contents = f.read()

            else:
                gene = parameters['gene']
                conn = http.client.HTTPConnection(HOSTNAME)
                conn.request("GET", "/homology/symbol/human/" + gene + "?content-type=application/json")
                r1 = conn.getresponse()
                text_json = r1.read().decode("utf-8")  # En string format
                conn.close()
                response = json.loads(text_json)
                if 'error' in response:
                    codigo_respuesta = 400
                    with open("error.html", "r") as f:
                        contents = f.read()
                else:
                    id = response['data'][0]['id']
                    conn.request("GET", "/overlap/id/" + id + "?feature=gene;content-type=application/json")
                    r1 = conn.getresponse()
                    text_json = r1.read().decode("utf-8")  # En string format
                    conn.close()
                    dictionary = json.loads(text_json)
                    start = dictionary[0]['start']
                    end = dictionary[0]['end']
                    length = end-start
                    id = dictionary[0]['id']
                    chromosome = dictionary[0]['assembly_name']
                    if 'json' in parameters:
                        res_json = True
                        names = ["Start", "End", "Length", "Id", "Chromosome"]
                        info = [start, end, length, id, chromosome]
                        contents = dict(zip(names, info))
                        contents = json.dumps(contents)
                    else:
                        contents = """
                                              <html>
                                              <body>
                                              <ul>
                                              <h3 align=center><p style="color:#70c2fe";><u>INFORMATION ABOUT A HUMAN GENE</u></p>"""
                        contents = contents + " The end is: " + str(end) + "<br> The start is: "+str(start)+"<br> The lenght is: "+str(length)+"<br> The ID is: "+str(id)+ "<br>The chromosome is: "+str(chromosome)+"<br>"""
                        contents = contents + """</ul> 
                                              </body>
                                              </html>
                                              """
        elif self.path[0:9] == "/geneCalc":
            parameters = self.endpoints(self.path)
            if parameters == {}:
                codigo_respuesta = 400
                with open("unavailable.html", "r") as f:
                    contents = f.read()

            elif 'gene' not in parameters or parameters['gene'] == '':
                codigo_respuesta = 400
                with open("unavailable.html", "r") as f:
                    contents = f.read()

            else:
                gene = parameters['gene']
                conn = http.client.HTTPConnection(HOSTNAME)
                conn.request("GET", "/homology/symbol/human/" + gene + "?content-type=application/json")
                r1 = conn.getresponse()
                text_json = r1.read().decode("utf-8")  # En string format
                conn.close()
                response = json.loads(text_json)
                if 'error' in response:
                    codigo_respuesta = 400
                    with open("error.html", "r") as f:
                        contents = f.read()
                else:
                    id = response['data'][0]['id']
                    conn.request("GET", "/sequence/id/" + id + "?content-type=application/json")
                    r1 = conn.getresponse()
                    text_json = r1.read().decode("utf-8")
                    conn.close()
                    dictionary = json.loads(text_json)
                    human_seq = dictionary['seq']
                    s1 = Seq(human_seq)
                    total_len = len(human_seq)
                    percA = s1.perc('A')
                    percT = s1.perc('T')
                    percG = s1.perc('G')
                    percC = s1.perc('C')
                    if 'json' in parameters:
                        res_json = True
                        names_list = ["Total length", "Percentage A", "Percentage T", "Percentage G", "Percentage C"]
                        calculations_list = [total_len, percA, percT, percG, percC]
                        contents = json.dumps(dict(zip(names_list, calculations_list)))
                    else:
                        contents = """
                                              <html>
                                              <body>
                                              <ul>
                                              <h3 align=center><p style="color:#d970fe";><u>CALCULATIONS ON A HUMAN GENE</u></p>"""
                        contents = contents + " The total length is: " + str(total_len) + "<br> The percentage of the base Adenine is: "+str(percA)+"<br> The percentage of the base Thymine is: "+str(percT)+"<br> The percentage of the base Guanine is: "+str(percG) + "<br>The percentage of the base Cytosine is: "+str(percC)+"<br>"""
                        contents = contents + """</ul> 
                                              </body>
                                              </html>
                                              """

        elif self.path[0:9] == "/geneList":
            parameters = self.endpoints(self.path)
            if parameters == {}:
                codigo_respuesta = 400
                with open("unavailable.html", "r") as f:
                    contents = f.read()

            elif 'chromo' not in parameters or 'start' not in parameters or 'end' not in parameters:
                codigo_respuesta = 400
                with open("unavailable.html", "r") as f:
                    contents = f.read()

            elif parameters['chromo'] == '' or parameters['start'] == '' or parameters['end'] == '':
                codigo_respuesta = 400
                with open("unavailable.html", "r") as f:
                    contents = f.read()
            else:
                chromo = parameters['chromo']
                start = parameters['start']
                end = parameters['end']
                conn = http.client.HTTPConnection(HOSTNAME)
                conn.request("GET", "/overlap/region/human/" +str(chromo)+ ":"+str(start)+"-"+str(end)+"?content-type=application/json;feature=gene;feature=transcript;feature=cds;feature=exon")
                r1 = conn.getresponse()
                text_json = r1.read().decode("utf-8")  # En string format
                conn.close()
                response = json.loads(text_json)
                if 'error' in response:
                    codigo_respuesta = 400
                    with open("error.html", "r") as f:
                        contents = f.read()
                elif 'json' in parameters:
                    res_json = True
                    lista = []
                    for i in response:
                        if i['feature_type'] == 'gene':
                            diccionario = dict()
                            diccionario['external_name'] = i['external_name']
                            diccionario['start'] = i['start']
                            diccionario['end'] = i['end']
                            lista.append(diccionario)
                    contents = json.dumps(lista)
                else:
                    contents = """
                                                      <html>
                                                      <body>
                                                      <ol>
                                                      <h3 align=center><p style="color:#70feb9";><u>GENES LOCA
                                                      TED ON A CHROMOSOME FROM START TO END POSITIONS</u></p>"""
                    for element in response:
                        if element['feature_type'] == 'gene':
                            contents = contents+"<li>"+"GENE "+(str(element['external_name']) + ";   START:" + " " + str(element['start'])+ "   END:"+" " + str(element['end']))+"</li><br>"
                    contents = contents + """</ol> 
                                                                  </body>
                                                                  </html>
                                                                  """
        else:
            codigo_respuesta = 400
            with open("error.html", "r") as f:
                contents = f.read()

        #To generate the response message:
        self.send_response(codigo_respuesta)
        if res_json:
            #To define the content-type header:
            self.send_header('Content-Type', 'application/json')
        else:
            self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        #Now the header is finished:
        self.end_headers()
        #Send the response message
        self.wfile.write(str.encode(contents))
        return


# ------------------------

# - MAIN program

# ------------------------

# -- Set the new handler
Handler = TestHandler
socketserver.TCPServer.allow_reuse_address = True

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new one
    # -- client, the handler is called

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")
