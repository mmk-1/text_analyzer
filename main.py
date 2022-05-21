from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from analyzer import TextAnalyzer
from urllib.parse import urlparse, parse_qs

PORT = 8080

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        content = json.loads(self.rfile.read(length))
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        if(content['text'] == ''):
            output_data = "Cannot analyze an empty text!"
            output_json = json.dumps(output_data)
            self.wfile.write(output_json.encode('utf-8'))
        ta = TextAnalyzer(content['text'])

        parsed_url = urlparse(self.path)
        filters = set()
        # Check if there is queries in the url
        if(parsed_url.query != ''):
            queries = parse_qs(parsed_url.query)['analysis'][0].split(',')
            for q in queries:
                filters.add(q)
        # Check if filters are in the POST req
        if('analysis' in content):
            for q in content['analysis']:
                filters.add(q)

        output_data = {
                    "wordCount": ta.getNumberOfWords(),
                    "letters": ta.getNumberOfLetters(),
                    "longest": ta.getLongestWord(),
                    "avgLength": ta.getAvgWordLength(),
                    "duration": ta.getReadingDuration(),
                    "medianWordLength": ta.getMedianLength(),
                    "medianWord": ta.getMedianOfSorted(),
                    "language": ta.getLanguage()
        }
        if(filters != set()):
            output_data = {f: output_data[f] for f in filters}
        
        output_json = json.dumps(output_data)
        self.wfile.write(output_json.encode('utf-8'))

server = HTTPServer(('', PORT), MyHandler)
print(f'Server is running on port {PORT}')
server.serve_forever()
server.server_close()