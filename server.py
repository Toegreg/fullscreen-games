import http.server
import socketserver
import subprocess

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Assuming the command to run is fixed
        command = "python script.py"
        
        # Execute the command
        response = subprocess.run(command, capture_output=True, text=True, shell=True)
        output = response.stdout

        # Send back the output of the script
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(output.encode())

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()
