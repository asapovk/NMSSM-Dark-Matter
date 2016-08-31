import subprocess
import os
path = '/home/inar/MC/MG5_aMC_v2_4_0/bin/DMjune7/Cards'
path2 = '/home/inar/Dropbox/CURRENT/NMSSM/scripts'


# subprocess.call("rm param_card.dat", shell=True)
# wr_data = open('param_card.dat', 'w+')

def rewrite_param_card(MV, MX):
	'''Modify param_card_default: put tags scanMV and scanMX'''
	subprocess.call('rm '+path+'/param_card.dat', shell=True)
	wr_data = open(path+'/param_card.dat', 'w+')
	def_data = open(path+'/param_card_default.dat', 'r')
	for line in def_data:
			if 'scanMV' in line:
				new_line = line.split()
				new_line[1] = "{:.6e}".format(MV)
				new_str='   '
				for w in new_line:
					new_str+=w+' '
				new_str+='\n'	
				wr_data.write(new_str)
			elif 'scanMX' in line:
				new_line = line.split()
				new_line[1] = "{:.6e}".format(MX)
				new_str='   '
				for w in new_line:
					new_str+=w+' '
				new_str+='\n'	
				wr_data.write(new_str)
			else: wr_data.write(line)
	wr_data.close()
	def_data.close()

par_data = open(path2+'/params.dat', 'r')

os.remove('/home/inar/Dropbox/CURRENT/NMSSM/scripts/param_card.dat')

par_data.close()