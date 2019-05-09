#!/usr/bin/python3.6

import os,time,subprocess,fileinput


ip = input('Enter ip server: ')
print('Example Engter Netmask: 8 16 24')
netmask = input('Enter Netmask: ')

print('Example host : dc1.domain.local dc1')
host = input('Enter host: ')

gw = os.popen("ip route |grep default | awk '{print $3}'").read()
print(gw)

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
    a = os.system('find / -name ifcfg-eth0')
    with fileinput.FileInput(a, inplace=True, backup='.bak') as  f:
        for line in f:
            # print(line.replace('BOOTPROTO="none"', 'BOOTPROTO=static'))
            print(line.replace('ONBOOT="no"', 'ONBOOT=yes'))
        f.close()
    with open(a, 'a+') as f1:
        f1.write('\nIPADDR=' + ip)
        f1.write('\nFREFIX=' + netmask)
        f1.write('\nGATEWAY=' + gw)
        f1.write('\nDNS1=' + ip)
        f1.write('\nDNS2=8.8.8.8')
        f1.close()

elif bool(eno_) == True:

    a = os.system('find / -name ifcfg-eno1')
    with fileinput.FileInput(a, inplace=True, backup='.bak') as  f:
        for line in f:
            #print(line.replace('BOOTPROTO="none"', 'BOOTPROTO=static'))
            print(line.replace('ONBOOT="no"', 'ONBOOT=yes'))
        f.close()
    with open(a,'a+') as f1:
        f1.write('\nIPADDR='+ip)
        f1.write('\nFREFIX='+netmask)
        f1.write('\nGATEWAY='+gw)
        f1.write('\nDNS1='+ ip)
        f1.write('\nDNS2=8.8.8.8')
        f1.close()

elif bool(em_ )== True:

    a = os.system('find / -name ifcfg-em1')
    with fileinput.FileInput(a, inplace=True, backup='.bak') as  f:
        for line in f:
            # print(line.replace('BOOTPROTO="none"', 'BOOTPROTO=static'))
            print(line.replace('ONBOOT="no"', 'ONBOOT=yes'))
        f.close()
    with open(a, 'a+') as f1:
        f1.write('\nIPADDR=' + ip)
        f1.write('\nFREFIX=' + netmask)
        f1.write('\nGATEWAY=' + gw)
        f1.write('\nDNS1=' + ip)
        f1.write('\nDNS2=8.8.8.8')
        f1.close()

elif bool(ens__ )== True:

    a = os.system('find / -name ifcfg-ens33')

    with fileinput.FileInput( a, inplace=True, backup='.bak') as  f:
        for line in f:
            # print(line.replace('BOOTPROTO="none"', 'BOOTPROTO=static'))
            print(line.replace('ONBOOT="no"', 'ONBOOT=yes'))
        f.close()
    with open(a, 'a+') as f1:
        f1.write('\nIPADDR=' + ip)
        f1.write('\nFREFIX=' + netmask)
        f1.write('\nGATEWAY=' + gw)
        f1.write('\nDNS1=' + ip)
        f1.write('\nDNS2=8.8.8.8')
        f1.close()

else:
    print("dont't have interface")


with open('hosts','a+') as f:

   f.write('\n'+ ip +' '+ host)
   f.close()

os.system('yum  –y  install epel-release && yum –y update')

## install packet basic

os.system('yum install vim wget authconfig krb5-workstation -y')

## install repo samba4

os.system('cd  /etc/yum.repos.d/')

os.system('wget http://wing-net.ddo.jp/wing/7/EL7.wing.repo')
os.system("sed -i 's@enabled=0@enabled=1@g' /etc/yum.repos.d/EL7.wing.repo")
os.system('yum clean all')

## install samba4

os.system('yum install -y samba45 samba45-winbind-clients samba45-winbind samba45-client samba45-dc samba45-pidl samba45-python samba45-winbind-krb5-locator perl-Parse-Yapp perl-Test-Base python2-crypto samba45-common-tools')


with open('resolv.conf','w+') as f2:
    f2.write('nameserver ' + ip)
    f2.close()

## remove file created when install samba

os.system('rm -rf /etc/krb5.conf')
os.system('rm -rf /etc/samba/smb.conf')

domain = input('Enter domain name : ')
## copy file krb5.conf to etc
os.system('cp krb5.conf /etc/')

## get the kerberos key from DC1
os.system('kinit administrator@'+domain.upper())
os.system('klist')


###add the server to the existing domain

os.system('samba-tool domain join sunil.cc  DC -U"SUNIL\administrator" --dns-backend=SAMBA_INTERNAL')
### create samba service
os.system('cp samba.service /etc/systemd/system/samba.service')


os.system('systemctl enable samba &&  systemctl start samba')
os.system('samba-tool drs showrepl')

# print('install and config done!!!! reboot after 5s')
# time.sleep(5)

