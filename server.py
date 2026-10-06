from http.server import HTTPServer, BaseHTTPRequestHandler

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Simple Web Server</title>
        </head>

        <body>
            <h1>Simple Web Server</h1>

            <h2>Student Details</h2>
            <p><b>Name:</b> STEFFI</p>
            <p><b>Register Number:</b> 26017879</p>

            <h2>TCP/IP Protocol Suite</h2>

            <h3>Application Layer</h3>
            <ul>
                <li>HTTP</li>
                <li>HTTPS</li>
                <li>FTP</li>
                <li>SMTP</li>
                <li>DNS</li>
                <li>SSH</li>
                <li>Telnet</li>
            </ul>

            <h3>Transport Layer</h3>
            <ul>
                <li>TCP</li>
                <li>UDP</li>
            </ul>

            <h3>Internet Layer</h3>
            <ul>
                <li>IP</li>
                <li>ICMP</li>
                <li>ARP</li>
            </ul>

            <h3>Network Access Layer</h3>
            <ul>
                <li>Ethernet</li>
                <li>Wi-Fi</li>
            </ul>

        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())


server = HTTPServer(("127.0.0.1", 8000), MyServer)

print("Server started at http://127.0.0.1:8000")

server.serve_forever()