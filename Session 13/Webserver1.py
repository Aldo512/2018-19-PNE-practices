import http.server
import socketserver

# Define the Server's port
PORT = 8000

# -- Use the http.server Handler
Handler = http.server.SimpleHTTPRequestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    httpd.serve_forever()