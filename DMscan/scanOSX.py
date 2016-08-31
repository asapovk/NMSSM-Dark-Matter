import subprocess
import os


path_mg5 = '/Users/Inar/MG5/bin/'
path_cm = '/Users/Inar/CheckMATE-1.2.2Modified/bin/'
path_events = '/Users/Inar/DMtest/Events/run_01/'
path_cards = '/Users/Inar/DMtest/Cards/'
path = '/Users/Inar/'
path_dat = '/Users/Inar/DMscan/data/'

def rewrite_param_card(MV, MX):
	'''before running, Modify param_card_default:
	 put tags scanMV and scanMX'''
	wr_data = open(path_dat+'param_card.dat', 'w+')
	def_data = open(path_dat+'param_card_default.dat', 'r')
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

def rewrite_CheckMate_card(MV, MX):
	'''before running, Modify param_card_default:
	 put tags scanMV and scanMX'''
	wr_data = open(path_dat+'param_card.dat', 'w+')
	def_data = open(path_dat+'param_card_default.dat', 'r')
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

def rewrite_CheckMate_card(xsec):
	'''before running, Modify param_card_default:
	 put tags scanMV and scanMX'''
	wr_data = open(path_dat+'CheckMATErun.dat', 'w+')
	def_data = open(path_dat+'CheckMATErun_default.dat', 'r')
	for line in def_data:
			if 'XSect:' in line:
				new_line = line.split()
				new_line[1] = str(xsec)
				new_str= ' '.join(new_line)+'\n'	
				wr_data.write(new_str)
			else: wr_data.write(line)
	wr_data.close()
	def_data.close()
# XSect: 630 pb
def get_xsection():
	xsec = open(path+'cross_sectionDM.txt', 'r')
	for line in xsec:
		xsec_line = line.split()
		if 'tag_1' in xsec_line:
			xsection, xsec_err = xsec_line[2], xsec_line[3]
			return (xsection*10**12, xsec_err*10**12)
	xsec.close()

def write_scan_point(MV,MX,xsec,allowed):
	scan_dat = open(path_dat+'scan_points.dat', 'a')
	new_line = [str(MV),str(MX),str(xsec), str(allowed)]
	dat_str = '   '.join(new_line)+'\n'
	scan_dat.write(dat_str)
	scan_dat.close()

par_data = open(path_dat+'scan_params.dat', 'r')

for line_dat in par_data:
	list_dat = line_dat.split()
	MX = float(list_dat[1])
	MV = float(list_dat[0])

	rewrite_param_card(MV,MX)
	if os.path.exists(path+'DMtest'):
		print 'folder exists'
	mg_gen_str = path_mg5+'mg5_aMC '+ path+'auto_generate'
	subprocess.call(mg_gen_str, shell=True)
	cp_str_r = 'cp '+path_dat+'run_card.dat '+path_cards+'run_card.dat'
	cp_str_p = 'cp '+path_dat+'param_card.dat '+path_cards+'param_card.dat'
	subprocess.call(cp_str_r, shell=True)
	subprocess.call(cp_str_p, shell=True)
	mg_launch_str = path_mg5+'mg5_aMC '+ path+'auto_launch'
	subprocess.call(mg_launch_str, shell=True)
	xsection =  get_xsection()[0]
	rewrite_CheckMate_card(xsection)

	unzip_str ='gunzip '+path_events+'tag_1_pythia_events.hep.gz'
	subprocess.call(unzip_str, shell=True)

	chMrun_str = path_cm + 'CheckMATE '+path_dat+'CheckMATErun.dat'
	proc = subprocess.Popen(
	    chMrun_str,
	    shell=True,
	    stdout=subprocess.PIPE, stderr=subprocess.PIPE
	)
	(res,err) = proc.communicate()  

	print res

	if 'Allowed' in res:
		allowed =1
	else: allowed = 0
	write_scan_point(MV,MX,xsection,allowed)
	print(MV,MX,xsection,allowed) 


	print 'its ok, bro'
par_data.close()


# gunzip ~/MC/DMtest/Events/run_01/tag_1_pythia_events.hep.gz
# ~/MC/MG5_aMC_v2_4_0/bin/mg5_aMC ~/MC/autorun
# rm -r DMtest
