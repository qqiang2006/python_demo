#coding=utf8
import re
check_IP=raw_input("please input the IP address:")
num=0
if not re.search('[a-zA-Z]', check_IP):
    for i in check_IP.split('.'):
        if int(i)>=0 and int(i)<256:
            num+=1
            if num==4:
                print 'this ip is ok'
            continue
        else:
            print "this %s is ilegal"
            break
else:
    print "this %s is ilegal"
