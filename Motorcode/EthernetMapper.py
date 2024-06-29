import nmap

def mapDevices():
    nm =nmap.PortScanner()
    ipRange = '192.168.1.0/24'

    nm.scan(hosts=ipRange,arguments='-sn')

    devices=[]

    for host in nm.all_hosts():
        if 'mac' in nm[host]['adresses']:
            mac_address = nm[host]['addresses']['mac']
            devices.append({
                            'ip':host,
                            'mac_address':mac_address
                            })
    
    return devices

print(mapDevices())