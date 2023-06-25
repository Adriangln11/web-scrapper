import re 
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

regex = r'/problems/[\w-]*'

url = 'https://leetcode.com/problemset/all/?sorting=W3sic29ydE9yZGVyIjoiQVNDRU5ESU5HIiwib3JkZXJCeSI6IkFDX1JBVEUifV0%3D'
res = requests.get(url)
html = res.text

problems = re.findall(regex, str(html))
content = []
counter = 1
for i in problems:
    url = f'https://leetcode.com{i}'
    problem = i.replace('/problems/', '')
    problem = problem.replace('-', ' ')
    problem = problem.replace(problem[0], problem[0].upper(), 1)
    content.append(f'{counter}. -{problem} -- {url}')
    counter += 1

contenido = ', '.join(content)

contenido = contenido.replace(', ', '<br>')

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            
            response = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href="https://bootswatch.com/5/darkly/bootstrap.min.css">
                    <title>Miniproyectos | Web Scrapping</title>
                </head>
                <body>
                    

                    <main class="container text-center">
                        <h1>Problemas LeetCode</h1>
                        <div class="m-5">{contenido}</div>
                        <span class="">Web Scrapped - <a href="https://leetcode.com/problemset/all/">LeetCode</a></span>
                    </main>
                </body>
                </html>
            """
                
            

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(response, 'utf-8'))

def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Server listening on port: ', port)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
