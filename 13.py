import xmlrpclib
pchal = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
print(pchal.phone('Bert'))