import os,time,subprocess,fileinput
#os.system('systemctl stop firewalld')
#os.system('systemctl disable firewalld')

with fileinput.FileInput('config', inplace=True,backup='.bak') as  f1:

    for line in f1:
       print(line.replace('SELINUX=enforcing','SELINUX=disabled'),end='')
    f1.close()

os.system("echo 'dc1' > hostname")

#ip = input('enter ip PDC: ')
#print('Example hostname : dc1.domain.local dc1')
#host = input('Enter hostname: ')

#with open('hosts','a+') as f:

#    f.write('\n'+ ip +' '+ host)
#    f.close()

# install epel-release

# os.system('yum install epel-release –y && yum update')
#
# # install packets need for samba4
#
# os.system('yum install perl gcc libacl-devel libblkid-devel gnutls-devel readline-devel python-devel gdb pkgconfig krb5-workstation zlib-devel setroubleshoot-server libaio-devel setroubleshoot-plugins policycoreutils-python libsemanage-python setools-libs-python setools-libs popt-devel libpcap-devel sqlite-devel libidn-devel libxml2-devel libacl-devel libsepol-devel libattr-devel keyutils-libs-devel cyrus-sasl-devel cups-devel bind-utils libxslt docbook-style-xsl openldap-devel pam-devel bzip2 vim wget -y')
#
# # dowload samba4
#
# os.system('wget https://download.samba.org/pub/samba/stable/samba-4.6.0.tar.gz')
#
# # extract
#
# os.system('tar -zxvf samba-4.6.0.tar.gz && cd samba-4.6.0')
#
# #buil
#
# os.system('./configure --enable-debug --enable-selftest --with-ads --with-systemd --with-winbind')
#
# # install
#
# os.system('make && make install')
#
# # Edit file  /etc/krb5.conf

with fileinput.FileInput('config', inplace=True,backup='.bak') as  f2:

    for line in f2:
       print(line.replace('includedir /etc/krb5.conf.d/','#includedir /etc/krb5.conf.d/'),end='')
    f2.close()

# domain provision

os.system('/usr/local/samba/bin/samba-tool domain provision --use-rfc2307 --interactive')

os.system('cp samba.service /etc/systemd/system/samba.service')

os.system('systemctl enable samba && systemctl start samba')

print('install and config done!!!! reboot after 5s')
time.sleep(5)
