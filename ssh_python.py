#coding=utf8
import paramiko,yaml,os,time
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conf_yaml=yaml.load(open(os.getcwd()+'/'+'conf.yaml'))
#print conf_yaml
host=conf_yaml['server_ips']['value']
usrname=conf_yaml['login']['username']
passwd=conf_yaml['login']['passwd']
Port=conf_yaml['login']['port']
cmd=conf_yaml['exec_cmd']['cmd']
for i in host.split(','):
	try:
		ssh.connect(hostname=i,port=Port,username=usrname,password=passwd,timeout=2)
		print 'login' + ' '+ i + ' '+ 'success'

		for j in cmd.split(','):
			stdin,stdout,stderr=ssh.exec_command(j)
			result=stdout.read()
			print result
		ssh.close()
	except:
		print 'login' + ' ' + 'i' + ' ' + 'failed'
