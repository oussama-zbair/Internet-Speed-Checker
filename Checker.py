import psutil
import speedtest
from tabulate import tabulate

class Net:
    def __init__(self):
        self.interfaces = self.get_interfaces()
        self.speed_parser = speedtest.Speedtest()
    
    def get_interfaces(self):
        parser = psutil.net_if_addrs()
        interfaces = []
        for interface_name, _ in parser.items():
            interfaces.append(interface_name)
        return interfaces
        
    def get_download_speed(self):
        return round(self.speed_parser.download() / 1_000_000, 2)
    
    def get_upload_speed(self):
        return round(self.speed_parser.upload() / 1_000_000, 2)
    
    def __repr__(self):
        data = {
            "Interfaces": self.interfaces,
            "Download": self.get_download_speed(),
            "Upload": self.get_upload_speed()
        }
        table = tabulate(data, headers="keys", tablefmt="pretty")
        return table

if __name__ == "__main__":
    net = Net()
    print(net)
