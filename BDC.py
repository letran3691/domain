#!/usr/bin/python3.6

import os,time,subprocess,fileinput

os.system('systemctl stop firewalld')
os.system('systemctl disable firewalld')

ip_dc2 = input('Enter ip dc2 : ')
print('Example Engter Netmask: 8 16 24')
netmask = input('Enter Netmask: ')

print('Example domain : domain.local')
host = input('Enter domain : ')

ip_dc1 = input('Enter ip dc1 :')

with open('/etc/hosts','a+') as f:

   f.write('\n'+ ip_dc2 +' '+ 'dc2.'+ host +' dc2')
   f.write('\n' + ip_dc1 + ' ' + 'dc1.' + host + ' dc1')
   f.close()

gw = os.popen("ip route |grep default | awk '{print $3}'").read()
print(gw)

################################## config network interface

def eno():
    a = os.path.exists('/sys/class/net/eno1')

    return a
def eth():
    a = os.path.exists('/sys/class/net/eth0')
    return a

def em():
    a = os.path.exists('/sys/class/net/em1')
    return a
def ens():
    a = os.path.exists('/sys/class/net/ens33')
    return a

eno_ = eno()
#print(bool(eno_))

eth_ = eth()
#print(bool(eth_))

em_ = em()
#print(bool(em_))

ens_ = ens()
#print(bool(ens_))

if bool(eth_) == True:

    with fileinput.FileInput('/etc/sysconfig/network-scripts/ifcfg-eth0', inplace=True, backup='.bak') as  f:
        for line in f:
            print(line.replace('BOOTPROTO="dhcp"','BOOTPROTO=static'),end='')
            #print(line.replace('ONBOOT="no"', 'ONBOOT=yes'))
        f.close()
    with open('/etc/sysconfig/network-scripts/ifcfg-eth0', 'a+') as f1:
        f1.write('\nIPADDR=' + ip)
        f1.write('\nFREFIX=' + netmask)
        f1.write('\nGATEWAY=' + gw)
        f1.write('\nDNS1=' + ip)
        f1.write('\nDNS2=8.8.8.8')
        f1.close()

elif bool(eno_) == True:

    with fileinput.FileInput('/etc/sysconfig/network-scripts/ifcfg-eno1', inplace=True, backup='.bak') as  f:
        for line in f:
            print(line.replace('BOOTPROTO="dhcp"','BOOTPROTO=static'),end='')
            #print(line.replace('ONBOOT="no"', 'ONBOOT=yes'))
        f.close()
    with open('/etc/sysconfig/network-scripts/ifcfg-eno1','a+') as f1:
        f1.write('\nIPADDR='+ip)
        f1.write('\nFREFIX='+netmask)
        f1.write('\nGATEWAY='+gw)
        f1.write('\nDNS1='+ ip)
        f1.write('\nDNS2=8.8.8.8')
        f1.close()

elif bool(em_ )== True:

    with fileinput.FileInput('/etc/sysconfig/network-scripts/ifcfg-em1', inplace=True, backup='.bak') as  f:
        for line in f:
            print(line.replace('BOOTPROTO="dhcp"','BOOTPROTO=static'),end='')
            #print(line.replace('ONBOOT="no"', 'ONBOOT=yes'))
        f.close()
    with open('/etc/sysconfig/network-scripts/ifcfg-em1', 'a+') as f1:
        f1.write('\nIPADDR=' + ip)
        f1.write('\nFREFIX=' + netmask)
        f1.write('\nGATEWAY=' + gw)
        f1.write('\nDNS1=' + ip)
        f1.write('\nDNS2=8.8.8.8')
        f1.close()

elif bool(ens_ )== True:

    with fileinput.FileInput('/etc/sysconfig/network-scripts/ifcfg-ens33', inplace=True, backup='.bak') as  f:
        for line in f:
            print(line.replace('BOOTPROTO="dhcp"','BOOTPROTO=static'),end='')
            #print(line.replace('ONBOOT="no"', 'ONBOOT=yes'))
        f.close()
    with open('/etc/sysconfig/network-scripts/ifcfg-ens33', 'a+') as f1:
        f1.write('\nIPADDR=' + ip)
        f1.write('\nFREFIX=' + netmask)
        f1.write('\nGATEWAY=' + gw)
        f1.write('\nDNS1=' + ip)
        f1.write('\nDNS2=8.8.8.8')
        f1.close()

else:
    print("dont't have interface")

########### restart network

os.system('systemctl restart network')

#os.system('yum  –y  install epel-release && yum –y update')

#### install packet basic

os.system('yum -y install wget authconfig krb5-workstation')

##### install repo samba4

#os.system('cd  /etc/yum.repos.d/')

os.system(' cd  /etc/yum.repos.d/ && wget http://wing-net.ddo.jp/wing/7/EL7.wing.repo')
os.system("sed -i 's@enabled=0@enabled=1@g' /etc/yum.repos.d/EL7.wing.repo")
os.system('yum clean all')

## install samba4

os.system('yum install -y samba45 samba45-winbind-clients samba45-winbind samba45-client samba45-dc samba45-pidl samba45-python samba45-winbind-krb5-locator perl-Parse-Yapp perl-Test-Base python2-crypto samba45-common-tools')


with open('/etc/resolv.conf','a+') as f2:
    f2.write('nameserver ' + ip_dc1)
    f2.close()



############ transfer file hosts

os.system('scp /etc/hosts root@dc1.'+domain+':/etc/')


## remove file created when install samba

os.system('rm -rf /etc/krb5.conf')
os.system('rm -rf /etc/samba/smb.conf')

domain = input('Enter domain name : ')

## copy file krb5.conf to etc

with fileinput.FileInput('krb5.conf', inplace=True,backup='.bak') as f3:
    for line in 3:
        print(line.replace('default_realm = domain.local','default_realm = '+domain.upper()))
        f3.close()


os.system('cp krb5.conf /etc/')

###### get the kerberos key from DC1

os.system('kinit administrator@'+domain.upper())
os.system('klist')


###add the server to the existing domain

os.system('samba-tool domain join sunil.cc  DC -U"SUNIL\/administrator" --dns-backend=SAMBA_INTERNAL')

### create samba service
os.system('cp samba.service /etc/systemd/system/samba.service')

####################################################################

print('switch DC1 press Enter')

time.sleep(60)

input('Enter to continue.....')

#################################################################

os.system('systemctl enable samba &&  systemctl start samba')

##################################################################

print('switch DC1 press Enter')

time.sleep(30)

input('Enter to continue.....')

###################################################################

os.system('samba-tool drs showrepl')

###################################################################

print('switch DC1 press Enter')

time.sleep(30)

input('Enter to continue.....')

###################################################################

print('install and config done!!!! reboot after 5s')
time.sleep(5)

os.system('reboot now')

