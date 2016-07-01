import urllib

for num in range(167534,168000):
	elencoParcometri = { }
	link = 'http://giromilano.atm.it/tpportalbackend/geodata/pois/'+ str(num)
	print link
	f = urllib.urlopen(link)
	myfile = f.read()
	elencoParcometri['metro'] = myfile
	print elencoParcometri