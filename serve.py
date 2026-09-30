import http.server
import socketserver
import os
import webbrowser

PORT = 8080
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.glb': 'model/gltf-binary',
    '.gltf': 'model/gltf+json',
})

print(f"Starting 3D Lamp Web Viewer on http://localhost:{PORT} ...")
webbrowser.open(f"http://localhost:{PORT}/index.html")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
