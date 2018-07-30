import subprocess
import socket
import requests
import json
import smtplib
from email.mime.text import MIMEText
from uuid import getnode as get_mac
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#Get location by using API and load into a dictionary and traverse and concat it into a string
s = ""
# s is the result string of both ip address and location
def getJson(d):
    global s
    s += '\n'
    s += 'Latitude: ' + str(d['latitude']) + '\n'
    s += 'Longitude: ' + str(d['longitude']) + '\n'
    s += 'State: ' + str(d['state_prov']) + '\n'
    s += 'City: ' + str(d['city']) + '\n'
    s += 'District: ' + str(d['district']) + '\n'
    s += 'Zipcode: ' + str(d['zipcode']) + '\n'
    s += 'Internet Service Provider: ' + str(d['isp']) + '\n'
    s += 'Organization: ' + str(d['organization']) + '\n'
    s += 'Time zone: ' + str(d['time_zone']['name']) + '\n'
    s += 'Current time: ' + str(d['time_zone']['current_time']) + '\n'


arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src')+1]
s += ipaddr + '\n\nThe location of this device is:'

#api request and json
ip = requests.get('https://api.ipify.org').text
send_url = 'https://api.ipgeolocation.io/ipgeo?apiKey=26bfbd75bad0467ca96927704e4eb3ad'
jResult = requests.get(send_url)
result = json.loads(jResult.text)
getJson(result) 
s = s.decode('ascii','ignore')
#The part where the email will be send
#Change to your own account information
to = 
gmail_user = 
gmail_password = 
mac = str(hex(get_mac()))
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()
# Very Linux Specific
my_ip = 'The IP address of this device is: %s' %  s
msg = MIMEText(my_ip)
msg['Subject'] = 'Information For D.R.O.N.E with MAC ' + mac + ' on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()

