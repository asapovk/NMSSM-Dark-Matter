import subprocess

try:
	a=1/0
except Exception, e:
	print e
# a=1/0

print 'All done!'