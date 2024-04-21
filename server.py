import http.server
import socketserver
import subprocess
import requests
import json

PORT = 8000
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1227314096404434964/UuerVrxbUe8YPSdhVbnsOw3a0BSSL6N3Cnflv4NNeMTahbZNsuuc5_0MWlax5dv1fRJJ"

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Define the message content
        message_content = "Bob"

        # Create the payload
        payload = {
            "content": message_content
        }

        # Convert the payload to JSON format
        json_payload = json.dumps(payload)

        # Send a POST request to the Discord webhook URL with the JSON payload
        response = requests.post(DISCORD_WEBHOOK_URL, data=json_payload, headers={'Content-Type': 'application/json'})

        # Check the response status
        if response.status_code == 204:
            print("Message sent successfully to Discord")
        else:
            print("Failed to send message to Discord. Status code:", response.status_code)

        # Send back the response to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Message sent to Discord")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()
