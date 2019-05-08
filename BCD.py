import os,time,subprocess,fileinput


ip = input('Enter ip server: ')
print('Example Engter Netmask: 8 16 24')
netmask = input('Enter Netmask: ')

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

eno_ = eno()
print(bool(eno_))

eth_ = eth()
print(bool(eth_))

em_ = em()
print(bool(em_))

if bool(eth_) == True:
    print('have eth0')

elif bool(eno_) == True:
    print('have eno1')
    with fileinput.FileInput('ifcfg-eth0', inplace=True, backup='.bak') as  f:
        for line in f:
            #print(line.replace('BOOTPROTO="none"', 'BOOTPROTO=static'))
            print(line.replace('ONBOOT="no"', 'ONBOOT=yes'))
        f.close()
    with open('ifcfg-eth0','a+') as f1:
        f1.write('\nIPADDR='+ip)
        f1.write('\nFREFIX='+netmask)
        f1.write('\nGATEWAY='+gw)
        f1.write('\nDNS1=8.8.8.8')
        f1.close()

elif bool(em_ )== True:
    print('have em1')
else:
    print("dont't have interface")