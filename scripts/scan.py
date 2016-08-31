import subprocess

path = '/home/inar/MC/MG5_aMC_v2_4_0/bin/DMjune7/Cards'
path2 = '/home/inar/Dropbox/CURRENT/NMSSM/scripts'
path_mg5 = '/home/inar/MC/MG5_aMC_v2_4_0/bin/'

def rewrite_param_card(MV, MX):
	'''before running, Modify param_card_default:
	 put tags scanMV and scanMX'''
	wr_data = open(path+'/param_card.dat', 'w+')
	def_data = open(path+'/param_card_default.dat', 'r')
	for line in def_data:
			if 'scanMV' in line:
				new_line = line.split()
				new_line[1] = "{:.6e}".format(MV)
				new_str= '   ' + ' '.join(new_line)+'\n'	
				wr_data.write(new_str)
			elif 'scanMX' in line:
				new_line = line.split()
				new_line[1] = "{:.6e}".format(MX)
				new_str= '   ' + ' '.join(new_line)+'\n'
				wr_data.write(new_str)
			else: wr_data.write(line)
	wr_data.close()
	def_data.close()

par_data = open(path2+'/params.dat', 'r')

for line_dat in par_data:
	list_dat = line_dat.split()
	MX = float(list_dat[1])
	MV = float(list_dat[0])

	rewrite_param_card(MV,MX)
	subprocess.call(path_mg5+'mg5_aMC', 'autorun', shell=True)

par_data.close()