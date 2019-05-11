#!/usr/bin/python3.6

import os,time,subprocess,fileinput

ip_dc2 = input('Enter ip dc2 : ')
print('Example Engter Netmask: 8 16 24')
netmask = input('Enter Netmask : ')

print('Example domain : domain.local')
domain = input('Enter domain : ')

############ tach chuoi

a = domain.split('.')[0]

ip_dc1 = input('Enter ip dc1 : ')

host_pdc = input('Enter hostname PDC: ')

host_n = subprocess.check_output('cat /etc/hostname',shell=True,universal_newlines=True)

with open('/etc/hosts','a+') as f:

   f.write('\n'+ ip_dc2 +' '+host_n+'.'+ domain +' '+host_n)
   f.write('\n' + ip_dc1 + ' ' + host_pdc+'.' + domain + ' '+host_pdc)
   f.close()

gw = os.popen("ip route |grep default | awk '{print $3}'").read()

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
        f1.write('\nIPADDR=' + ip_dc2)
        f1.write('\nFREFIX=' + netmask)
        f1.write('\nGATEWAY=' + gw)
        f1.write('\nDNS1=' + ip_dc2)
        f1.write('\nDNS2=8.8.8.8')
        f1.close()

elif bool(eno_) == True:

    with fileinput.FileInput('/etc/sysconfig/network-scripts/ifcfg-eno1', inplace=True, backup='.bak') as  f:
        for line in f:
            print(line.replace('BOOTPROTO="dhcp"','BOOTPROTO=static'),end='')
            #print(line.replace('ONBOOT="no"', 'ONBOOT=yes'))
        f.close()
    with open('/etc/sysconfig/network-scripts/ifcfg-eno1','a+') as f1:
        f1.write('\nIPADDR='+ip_dc2)
        f1.write('\nFREFIX='+netmask)
        f1.write('\nGATEWAY='+gw)
        f1.write('\nDNS1='+ ip_dc2)
        f1.write('\nDNS2=8.8.8.8')
        f1.close()

elif bool(em_ )== True:

    with fileinput.FileInput('/etc/sysconfig/network-scripts/ifcfg-em1', inplace=True, backup='.bak') as  f:
        for line in f:
            print(line.replace('BOOTPROTO="dhcp"','BOOTPROTO=static'),end='')
            #print(line.replace('ONBOOT="no"', 'ONBOOT=yes'))
        f.close()
    with open('/etc/sysconfig/network-scripts/ifcfg-em1', 'a+') as f1:
        f1.write('\nIPADDR=' + ip_dc2)
        f1.write('\nFREFIX=' + netmask)
        f1.write('\nGATEWAY=' + gw)
        f1.write('\nDNS1=' + ip_dc2)
        f1.write('\nDNS2=8.8.8.8')
        f1.close()

elif bool(ens_ )== True:

    with fileinput.FileInput('/etc/sysconfig/network-scripts/ifcfg-ens33', inplace=True, backup='.bak') as  f:
        for line in f:
            print(line.replace('BOOTPROTO="dhcp"','BOOTPROTO=static'),end='')
            #print(line.replace('ONBOOT="no"', 'ONBOOT=yes'))
        f.close()
    with open('/etc/sysconfig/network-scripts/ifcfg-ens33', 'a+') as f1:
        f1.write('\nIPADDR=' + ip_dc2)
        f1.write('\nFREFIX=' + netmask)
        f1.write('\nGATEWAY=' + gw)
        f1.write('\nDNS1=' + ip_dc2)
        f1.write('\nDNS2=8.8.8.8')
        f1.close()

else:
    print("dont't have interface")

########### restart network

os.system('systemctl restart network')

print('\nprepare install.......\n')

time.sleep(7)


#os.system('yum  –y  install epel-release && yum –y update')

#### install packet basic

os.system('yum groups -y install "Development Tools" ')
os.system('yum -y install iniparser libldb libtalloc libtdb libtevent python-devel gnutls-devel libacl-devel openldap-devel pam-devel readline-devel krb5-devel cups-devel')


###### dowload samba4

os.system('wget https://download.samba.org/pub/samba/stable/samba-4.6.0.tar.gz')

#### extract

os.system('tar -zxvf samba-4.6.0.tar.gz')

### buil

print('\n Begin compile')

time.sleep(3)

os.system('''cd samba-4.6.0 && ./configure \
--prefix=/usr \
--localstatedir=/var \
--with-configdir=/etc/samba \
--libdir=/usr/lib64 \
--with-modulesdir=/usr/lib64/samba \
--with-pammodulesdir=/lib64/security \
--with-lockdir=/var/lib/samba \
--with-logfilebase=/var/log/samba \
--with-piddir=/run/samba \
--with-privatedir=/etc/samba \
--enable-cups \
--with-acl-support \
--with-ads \
--with-automount \
--enable-fhs \
--with-pam \
--with-quotas \
--with-shared-modules=idmap_rid,idmap_ad,idmap_hash,idmap_adex \
--with-syslog \
--with-utmp \
--with-dnsupdate  ''')

############ make and install

os.system('cd samba-4.6.0 && make ')

os.system('cd samba-4.6.0 && make install ')


with open('/etc/resolv.conf','w') as f2:
    f2.write('# Generated by NetworkManager')
    f2.write('\nsearch '+ domain )
    f2.write('\nnameserver ' + ip_dc1)
    f2.close()



########### transfer file hosts

print('copy file')

time.sleep(3)

os.system('scp /etc/hosts root@'+host_pdc+'.'+domain+':/etc/')


## remove file created when install samba

os.system('rm -rf /etc/krb5.conf')
os.system('rm -rf /etc/samba/smb.conf')

##domain = input('Enter domain name : ')

## copy file krb5.conf to etc

os.system('cd domain/ && cp krb5.conf /etc/')

with open('/etc/krb5.conf','a+') as f3:

    f3.write('\n    default_realm = '+domain.upper())
    f3.close()

##### get the kerberos key from PDC

os.system('kinit administrator@'+domain.upper())
os.system('klist')


###add the server to the existing domain


os.system('samba-tool domain join '+domain+'  DC -U"'+a+'\/administrator" --dns-backend=SAMBA_INTERNAL')

### create samba service
os.system('cp domain/samba.service /etc/systemd/system/samba.service')

####################################################################

print('switch PDC press Enter')

time.sleep(60)

input('Enter to continue.....')

#################################################################

os.system('systemctl enable samba &&  systemctl start samba')

##################################################################

os.system('scp /etc/krb5.conf root@'+host_pdc+'.'+domain+':/etc/ ')

###################################################################

print('switch PDC press Enter')

time.sleep(30)

input('Enter to continue.....')

###################################################################

os.system('samba-tool drs showrepl')

###################################################################

print('switch PDC press Enter')

time.sleep(30)

input('Enter to continue.....')

###################################################################

print('install and config done!!!! reboot after 5s')
time.sleep(5)

os.system('reboot now')

