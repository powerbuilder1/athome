import subprocess
from decouple import config
import time

# dic of mac_address and associated name
devices = {}

try:
    file = open('devices', 'r')
    for line in file.readlines():
        # array of [mac_address, name]
        line_arr = line.split("-")
        mac_address = line_arr[0]
        name = line_arr[1][:len(line_arr[1])-1]
        # add mac_address and name to dic
        devices[mac_address] = name
except FileNotFoundError:
    print("Could not open file!")
finally:
    file.close()

MAC_ADDRESS = config("MAC_ADDRESS")

while True:
    for entry in devices.items():
        command = f"sudo arp-scan -l | grep {entry[0]}"
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdout, stderr) = proc.communicate()

        res = str(stdout, "utf8")

        print(res)

        if len(res) > 0:
            print(f"{entry[1]}, is da!")
        else:
            print(f"{entry[1]}, is ni da!")

    time.sleep(10)