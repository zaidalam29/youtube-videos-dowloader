from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from yt_dlp import YoutubeDL
import json
import os

# Ensure the downloads directory exists
if not os.path.exists('downloads'):
    os.makedirs('downloads')

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the HTML page
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        # Handle the download request
        if self.path == '/download':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = parse_qs(post_data.decode('utf-8'))

            url = data.get('url', [''])[0]
            if not url:
                self.send_error(400, "No URL provided")
                return

            try:
                # Set download options
                ydl_opts = {
                    'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save in the downloads folder
                }
                with YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(url, download=True)
                    title = info_dict.get('title', 'video')
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response = {
                        'status': 'success',
                        'title': title,
                        'message': 'Download complete!'
                    }
                    self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                self.send_error(500, str(e))
        else:
            self.send_error(404, "Not Found")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()