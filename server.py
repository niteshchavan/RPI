################################
##Generated with a lot of love##
##    with   EasyPython       ##
##Web site: easycoding.tn     ##
################################
import subprocess

from http.server import BaseHTTPRequestHandler, HTTPServer

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
    if Request == 'poweroff':
      output = subprocess.run(["poweroff"], shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.decode('utf-8')
    if Request == 'reboot':
      output = subprocess.run(["reboot"], shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.decode('utf-8')
    if Request == 'startkodi':
      output = subprocess.Popen(["export DISPLAY=:1.0 && kodi"], shell=True)
    if Request == 'stopkodi':
      output = subprocess.Popen(["killall kodi"], shell=True)
    if Request == 'bton':
      output = subprocess.Popen(["bash /nitesh/Bluetooth/BTon"], shell=True)
    if Request == 'btoff':
      output = subprocess.Popen([" bash /nitesh/Bluetooth/BToff"], shell=True)
    if Request == 'startyt':
      output = subprocess.Popen(["bash /nitesh/youtube"], shell=True)
    if Request == 'stopyt':
      output = subprocess.run(["killall chromium-browser"], shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.decode('utf-8')
    if Request == 'volumeup':
      output = subprocess.run(["amixer -q sset HDMI 10%+"], shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.decode('utf-8')
    if Request == 'volumedown':
      output = subprocess.run(["amixer -q sset HDMI 10%-"], shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.decode('utf-8')
    return


server_address_httpd = ('192.168.0.100',8090)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('Strting Server')
httpd.serve_forever()
