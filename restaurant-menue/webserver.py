from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_resonse(200)
                self.send_header('Content-type', 'text/html')
                self.end_header()

                output = ""
                output += "<html><body>Hello!</body></html>"
                self.wfile.write(output)
                print(output)
                return
        except:
            self.send_error(404, "File not Found %s" % self.path)


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print("Web server running on port %s") % port
        server.serve_forever()

    except KeyboardInterrupt:
        print("^C entered, stopping web server...")
        server.socket.close()


if __name__ == '__main__':
    main()
