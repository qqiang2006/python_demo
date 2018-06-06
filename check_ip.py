#coding=utf8
import re
def check_IP(IP):
    num=0
    if not re.search('[a-zA-Z]', IP):
        for i in IP.split('.'):
            if int(i)>=0 and int(i)<256:
                num+=1
                if num==4:
                    print 'this ip is ok'
                continue
            else:
                print "this ip is illegal"
                break
    else:
        print "this ip is illegal"

if __name__=='__main__':
    IP_address = raw_input("please input the IP address:")
    check_IP(IP_address)
    #check_IP('1.1.1.1')
