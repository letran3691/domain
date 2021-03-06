#!/usr/bin/python3.6

import os,time,subprocess,fileinput,sys

with fileinput.FileInput('/etc/selinux/config', inplace=True,backup='.bak') as  f1:

    for line in f1:
       print(line.replace('SELINUX=enforcing','SELINUX=disabled'),end='')
    f1.close()

ip = input('\nEnter ip Primary DC: ')
print('Example Enter Netmask: 8 16 24')
netmask = input('Enter Netmask: ')

host_n = subprocess.check_output('cat /etc/hostname',shell=True,universal_newlines=True)

host =host_n.rstrip('\n')


print('\nExample domain : domain.local')
domain = input('Enter domain name : ')

with open('/etc/hosts','a+') as f:

   f.write('\n'+ ip +' '+ host+'.'+ domain +' '+host)
   f.close()


gw = os.popen("ip route |grep default | awk '{print $3}'").read()

################################## config network interface

###################################################################################################

if  os.path.exists('/sys/class/net/')== True:

    err = subprocess.check_output('ls /sys/class/net/',shell=True,universal_newlines=True)

    print(str(err))

    b = err.split()
    c = (b[0])

    with fileinput.FileInput('/etc/sysconfig/network-scripts/ifcfg-'+str(c), inplace=True) as  f:
        for line in f:
            print(line.replace('BOOTPROTO="dhcp"','BOOTPROTO=static'),end='')
        f.close()

    with open('/etc/sysconfig/network-scripts/ifcfg-'+str(c), 'a+') as f1:
        f1.write('\nIPADDR=' + ip)
        f1.write('\nFREFIX=' + netmask)
        f1.write('\nGATEWAY=' + gw)
        f1.write('\nDNS1=127.0.0.1')
        f1.write('\nDNS2=8.8.8.8')
        f1.close()

else:
    print("ERROR!!! Dont't have interface\n")

    #err = subprocess.check_output('ls /sys/class/net/',shell=True,universal_newlines=True)
    err = os.listdir('/sys/class/net/')

    print(str(err))

    exit(0)

#### restart network

print('Restart network')

os.system('systemctl restart network')

time.sleep(4)

##### install epel-release

os.system('yum -y install epel-release && yum update -y')

print('update done!!!!')

#### install packets need for samba4

print('\nInstall packets need for samba4')

time.sleep(3)

os.system('yum -y install perl gcc libacl-devel libblkid-devel gnutls-devel readline-devel python-devel gdb pkgconfig krb5-workstation zlib-devel setroubleshoot-server libaio-devel setroubleshoot-plugins policycoreutils-python libsemanage-python setools-libs-python setools-libs popt-devel libpcap-devel sqlite-devel libidn-devel libxml2-devel libacl-devel libsepol-devel libattr-devel keyutils-libs-devel cyrus-sasl-devel cups-devel bind-utils libxslt docbook-style-xsl openldap-devel pam-devel bzip2 wget install tdb-tools')

#### dowload samba4

os.system('wget https://download.samba.org/pub/samba/stable/samba-4.6.0.tar.gz')

### extract

os.system('tar -zxvf samba-4.6.0.tar.gz')

### buil

print('\n Begin compile')
time.sleep(3)
os.system('cd /root/samba-4.6.0 && ./configure --enable-debug --enable-selftest --with-ads --with-systemd --with-winbind')


##### install

print('\nBegin install')

time.sleep(3)

os.system('cd /root/samba-4.6.0 && make && make install')


print('\nCompile and install done!!!!')

time.sleep(3)


##### Edit file  /etc/krb5.conf

with fileinput.FileInput('/etc/krb5.conf', inplace=True,backup='.bak') as  f2:

    for line in f2:
       print(line.replace('includedir /etc/krb5.conf.d/','#includedir /etc/krb5.conf.d/'),end='')
    f2.close()

#### domain provision

print('\nPassword Administrator > 7 characters and complex'.upper())

time.sleep(3)

os.system('/usr/local/samba/bin/samba-tool domain provision --use-rfc2307 --interactive')

os.system('cp domain/samba.service /etc/systemd/system/samba.service')

os.system('cp /usr/local/samba/bin/samba-tool /usr/sbin/')

##########################################
a = domain.split('.')[0]
for line in fileinput.FileInput('/usr/local/samba/etc/smb.conf',inplace=1):
    if "workgroup = "+a.upper() in line:
        line=line.replace(line,line+"\tallow dns updates = nonsecure and secure\n")
    print (line,end='')

#########################################


print('\nRestart and enable samba service\n')

os.system('systemctl enable samba && systemctl start samba')


print('\n1:Switch Backup DC to install')

time.sleep(20)

input('Enter to continue.....')

##########################################################


### backup file idmap.ldb
os.system('tdbbackup -s .bak /usr/local/samba/private/idmap.ldb')

######################################################################################################################

### copy file imap.ldb.bak to Backup DC

print('\nCopy dmap.ldb.bak to Backup DC')

time.sleep(3)

host_bdc = input('\nEnter hostname Backup DC: ')


os.system('scp -r /usr/local/samba/private/idmap.ldb.bak root@'+host_bdc+'.'+domain+':/usr/local/samba/private/idmap.ldb ')

############################################################################
# remove file krb5.conf

os.system('rm -f /etc/krb5.conf')

print('\n3: Switch Backup DC press Enter ')

time.sleep(20)

input('\nEnter to continue.....')

#############################################################################

# with open('/etc/resolv.conf','a+') as f3:
#     f3.write('search '+ domain )
#     f3.write('nameserver '+ ip)
#     f3.close()
#
# os.system('cd domain && cp krb5.conf /etc/ ')
#
# with fileinput.FileInput('/etc/krb5.conf', inplace=True, backup='.bak') as f4:
#     for line in f4:
#
#         print(line.replace('default_realm = domain.local', 'default_realm = '+ domain.upper()))
#
#     f4.close()

# #### Checking the Kerberos ticket

os.system('kinit administrator@'+domain.upper())
os.system('klist')

###################################################################################

print('\n5: Switch Backup DC press Enter')

time.sleep(20)

input('Enter to continue.....')

################################################################################

print('Backup DC showrepl done')

os.system('/usr/local/samba/bin/samba-tool drs showrepl')

print('\n7: Switch Backup DC press Enter')

time.sleep(3)

print('Install and config done!!!! reboot after 5s')

time.sleep(5)

os.system('reboot now')
