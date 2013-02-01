import urllib2
import time
import smtplib

#Let's check every 5 seconds? 
for i in range(0, 60):
	print 'checking url'
	u = urllib2.urlopen('http://www.walmart.com/ip/VIZIO-60-Class-LED-1080p-120Hz-SMART-HDTV-1.94-ultra-slim-E601i-A3/21311919#rr')
	if u.read().find('Out of stock') == -1:
		print "It's not in stock anymore? yahoo, lets send an email"
		s = smtplib.SMTP('smtp.gmail.com', 587)
		tls = s.starttls()
		print tls
		if "".join(map(str,tls)).find('Ready to start TLS') > -1:
			print "Ready to start connection"
			login = s.login('singh0833@gmail.com', 'F84B1D81DBFCA')
			print login
			if "".join(map(str,login )).find('Accepted') > -1:
				headers = ["from: singh0833@gmail.com", "subject: vizio might be in stock now", "to: singh0833@gmail.com", "mime-version: 1.0", "content-type: text/html"]
				headers = "\r\n".join(headers)
				s.sendmail("singh0833@gmail.com", "singh0833@gmail.com", headers + "\r\n\r\n" + "http://www.walmart.com/ip/VIZIO-60-Class-LED-1080p-120Hz-SMART-HDTV-1.94-ultra-slim-E601i-A3/21311919#rr")
	else:
		print 'still out of stock..'
	time.sleep(600)
