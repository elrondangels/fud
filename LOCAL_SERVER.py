import http.server
import socketserver
import webbrowser

#############
PORT = 9033 # if needed, change port number
#############

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        super().end_headers()

Handler = MyHTTPRequestHandler

GAME_URL = "http://localhost:" + str(PORT) + "/GhostChains.html"
webbrowser.open(GAME_URL, new= 1)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
