from subprocess import Popen, PIPE
proc = Popen(
    "./CheckMATE testparam.dat",
    shell=True,
    stdout=PIPE, stderr=PIPE
)

(res,err) = proc.communicate()  

print res

if 'Allowed' in res:
	print '!!!!'

# import subprocess
# p = subprocess.Popen(['./CheckMATE', 'testparam.dat','y','o'], stdout=subprocess.PIPE, 
# stderr=subprocess.PIPE)
# out, err = p.communicate()
# print out, err