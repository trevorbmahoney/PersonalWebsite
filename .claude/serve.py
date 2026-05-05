import http.server, socketserver, functools, os
ROOT = "/Users/trevormahoney/Documents/Personal Website/trevors-website"
os.chdir(ROOT)
Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
with socketserver.TCPServer(("127.0.0.1", 5173), Handler) as httpd:
    httpd.serve_forever()
