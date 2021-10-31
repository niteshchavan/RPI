################################
##Generated with a lot of love##
##    with   EasyPython       ##
##Web site: easycoding.tn     ##
################################
import subprocess
import re

from http.server import BaseHTTPRequestHandler, HTTPServer

audio_folder = '/mnt/INTERNAL/%\(title\)s.%\(ext\)s'
Request = None

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global Request
    messagetosend = bytes('Hi',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    Request = self.requestline
    Request = Request[5 : int(len(Request)-9)]
    print(Request)
    if Request == Request:
      url = (re.search("(?P<url>https?://[^\s]+)", Request).group("url"))
      process = subprocess.run([f"youtube-dl -o /mnt/INTERNAL/%\(title\)s.%\(ext\)s -f 140 {url}"], shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if Request == 'poweroff':
      output = subprocess.run(["poweroff"], shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.decode('utf-8')
    if Request == 'reboot':
      output = subprocess.run(["reboot"], shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.decode('utf-8')
    if Request == 'volumeup':
      output = subprocess.run(["amixer -q sset bluealsa 10%+"], shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.decode('utf-8')
    if Request == 'volumedown':
      output = subprocess.run(["amixer -q sset bluealsa 10%-"], shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.decode('utf-8')
    return


server_address_httpd = ('192.168.0.200',8090)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('Strting Server')
httpd.serve_forever()
