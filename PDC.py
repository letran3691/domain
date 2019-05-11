#!/usr/bin/python3.6

import os,time,subprocess,fileinput,sys

# with fileinput.FileInput('/etc/selinux/config', inplace=True,backup='.bak') as  f1:
#
#     for line in f1:
#        print(line.replace('SELINUX=enforcing','SELINUX=disabled'),end='')
#     f1.close()
#
# ip = input('\nenter ip PDC: ')
# print('Example Enter Netmask: 8 16 24')
# netmask = input('Enter Netmask: ')
#
# host_n = subprocess.check_output('cat /etc/hostname',shell=True,universal_newlines=True)
#
#
# print('\nExample domain : domain.local')
# domain = input('Enter domain name : ')
#
# with open('/etc/hosts','a+') as f:
#
#    f.write('\n'+ ip +' '+ host_n+'.'+ domain +' '+host_n)
#    f.close()
#
# gw = os.popen("ip route |grep default | awk '{print $3}'").read()
#
# ################################## config network interface
#
# def eno():
#     a = os.path.exists('/sys/class/net/eno1')
#
#     return a
# def eth():
#     a = os.path.exists('/sys/class/net/eth0')
#     return a
#
# def em():
#     a = os.path.exists('/sys/class/net/em1')
#     return a
# def ens():
#     a = os.path.exists('/sys/class/net/ens33')
#     return a
#
# eno_ = eno()
# #print(bool(eno_))
#
# eth_ = eth()
# #print(bool(eth_))
#
# em_ = em()
# #print(bool(em_))
#
# ens_ = ens()
# #print(bool(ens_))
#
# if bool(eth_) == True:
#
#     with fileinput.FileInput('/etc/sysconfig/network-scripts/ifcfg-eth0', inplace=True, backup='.bak') as  f:
#         for line in f:
#             print(line.replace('BOOTPROTO="dhcp"','BOOTPROTO=static'),end='')
#             #print(line.replace('ONBOOT="no"', 'ONBOOT=yes'))
#         f.close()
#     with open('/etc/sysconfig/network-scripts/ifcfg-eth0', 'a+') as f1:
#         f1.write('\nIPADDR=' + ip)
#         f1.write('\nFREFIX=' + netmask)
#         f1.write('\nGATEWAY=' + gw)
#         f1.write('\nDNS1=' + ip)
#         f1.write('\nDNS2=8.8.8.8')
#         f1.close()
#
# elif bool(eno_) == True:
#
#     with fileinput.FileInput('/etc/sysconfig/network-scripts/ifcfg-eno1', inplace=True, backup='.bak') as  f:
#         for line in f:
#             print(line.replace('BOOTPROTO="dhcp"','BOOTPROTO=static'),end='')
#             #print(line.replace('ONBOOT="no"', 'ONBOOT=yes'))
#         f.close()
#     with open('/etc/sysconfig/network-scripts/ifcfg-eno1','a+') as f1:
#         f1.write('\nIPADDR='+ip)
#         f1.write('\nFREFIX='+netmask)
#         f1.write('\nGATEWAY='+gw)
#         f1.write('\nDNS1='+ ip)
#         f1.write('\nDNS2=8.8.8.8')
#         f1.close()
#
# elif bool(em_ )== True:
#
#     with fileinput.FileInput('/etc/sysconfig/network-scripts/ifcfg-em1', inplace=True, backup='.bak') as  f:
#         for line in f:
#             print(line.replace('BOOTPROTO="dhcp"','BOOTPROTO=static'),end='')
#             #print(line.replace('ONBOOT="no"', 'ONBOOT=yes'))
#         f.close()
#     with open('/etc/sysconfig/network-scripts/ifcfg-em1', 'a+') as f1:
#         f1.write('\nIPADDR=' + ip)
#         f1.write('\nFREFIX=' + netmask)
#         f1.write('\nGATEWAY=' + gw)
#         f1.write('\nDNS1=' + ip)
#         f1.write('\nDNS2=8.8.8.8')
#         f1.close()
#
# elif bool(ens_ )== True:
#
#     with fileinput.FileInput('/etc/sysconfig/network-scripts/ifcfg-ens33', inplace=True, backup='.bak') as  f:
#         for line in f:
#             print(line.replace('BOOTPROTO="dhcp"','BOOTPROTO=static'),end='')
#             #print(line.replace('ONBOOT="no"', 'ONBOOT=yes'))
#         f.close()
#     with open('/etc/sysconfig/network-scripts/ifcfg-ens33', 'a+') as f1:
#         f1.write('\nIPADDR=' + ip)
#         f1.write('\nFREFIX=' + netmask)
#         f1.write('\nGATEWAY=' + gw)
#         f1.write('\nDNS1=' + ip)
#         f1.write('\nDNS2=8.8.8.8')
#         f1.close()
#
# else:
#     print("dont't have interface")
#
# #### restart network
#
# print('restart network')
#
# os.system('systemctl restart network')
#
# time.sleep(4)
#
# ##### install epel-release
#
# #os.system('yum -y install epel-release && yum update -y')
#
# #### install packets need for samba4
#
# print('\ninstall packets need for samba4')
#
# time.sleep(3)
#
# os.system('yum -y install perl gcc libacl-devel libblkid-devel gnutls-devel readline-devel python-devel gdb pkgconfig krb5-workstation zlib-devel setroubleshoot-server libaio-devel setroubleshoot-plugins policycoreutils-python libsemanage-python setools-libs-python setools-libs popt-devel libpcap-devel sqlite-devel libidn-devel libxml2-devel libacl-devel libsepol-devel libattr-devel keyutils-libs-devel cyrus-sasl-devel cups-devel bind-utils libxslt docbook-style-xsl openldap-devel pam-devel bzip2 wget')
#
# #### dowload samba4
#
# os.system('wget https://download.samba.org/pub/samba/stable/samba-4.6.0.tar.gz')
#
# ### extract
#
# os.system('tar -zxvf samba-4.6.0.tar.gz')
#
# ### buil
#
# print('\n Begin compile')
# time.sleep(3)
# os.system('cd /root/samba-4.6.0 && ./configure --enable-debug --enable-selftest --with-ads --with-systemd --with-winbind')
#
#
# ##### install
#
# print('\nBegin install')
#
# time.sleep(3)
#
# os.system('cd /root/samba-4.6.0 && make && make install')
#
#
# print('\ncompile and install done!!!!')
#
# time.sleep(3)
#
#
# ##### Edit file  /etc/krb5.conf
#
# with fileinput.FileInput('/etc/krb5.conf', inplace=True,backup='.bak') as  f2:
#
#     for line in f2:
#        print(line.replace('includedir /etc/krb5.conf.d/','#includedir /etc/krb5.conf.d/'),end='')
#     f2.close()
#
# #### domain provision
#
# print('\nPassword Administrator > 7 characters'.upper())
#
# time.sleep(5)
#
#
# os.system('/usr/local/samba/bin/samba-tool domain provision --use-rfc2307 --interactive')
#
# os.system('cp domain/samba.service /etc/systemd/system/samba.service')
#
# os.system('cp /usr/local/samba/bin/samba-tool /usr/sbin/')
#
# os.system('systemctl enable samba && systemctl start samba')
#
#
# print('\n1:switch BDC to install')
#
# time.sleep(50)
#
# input('Enter to continue.....')
#
# ##########################################################
#
# print(' install tdb-tools')
#
# time.sleep(3)
#
# os.system('yum -y install tdb-tools')

### backup file idmap.ldb
os.system('tdbbackup -s .bak /usr/local/samba/private/idmap.ldb')

exit(0)
######################################################################################################################

### copy file imap.ldb.bak to BDC

# print('\nCopy dmap.ldb.bak to BDC')
#
# time.sleep(3)
#
# host_bdc = input('\nEnter hostname BDC: ')
#
#
# os.system('scp -r /usr/local/samba/private/idmap.ldb.bak root@'+host_bdc+'.'+domain+':/var/lib/samba/private/idmap.ldb ')
#
# ############################################################################
# ## remove file krb5.conf
#
# os.system('rm -f /etc/krb5.conf')
#
# print('\n3: switch BDC press Enter ')
#
# time.sleep(30)
#
# input('\nEnter to continue.....')
#
# #############################################################################
#
# with open('/etc/resolv.conf','a+') as f3:
#     f3.write('search '+ domain )
#     f3.write('nameserver '+ ip)
#     f3.close()
#
# # os.system('cd domain && cp krb5.conf /etc/ ')
# #
# # with fileinput.FileInput('/etc/krb5.conf', inplace=True, backup='.bak') as f4:
# #     for line in f4:
# #
# #         print(line.replace('default_realm = domain.local', 'default_realm = '+ domain.upper()))
# #
# #     f4.close()
# # #
# # #### Checking the Kerberos ticket
#
# os.system('kinit administrator@'+domain.upper())
# os.system('klist')
#
# ###################################################################################
#
# print('\n5: switch BDC press Enter')
#
# time.sleep(30)
#
# input('Enter to continue.....')
#
# ################################################################################
#
# print('BDC showrepl done')
#
# os.system('/usr/local/samba/bin/samba-tool drs showrepl')
#
# print('install and config done!!!! reboot after 5s')
#
# time.sleep(5)
#
# os.system('reboot now')
