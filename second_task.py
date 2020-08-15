import re
from collections import Counter



def data_preparation(filepath):
    with open(filepath) as file:
        ip_list = []
        line = file.readline()
        while line:
            ip = re.search(r"\d+.\d+.\d+", line)
            ip_list.append(ip.group(0))
            line = file.readline()      
    return ip_list

def five_common_ip(list_of_ip):
    return Counter(list_of_ip).most_common(5)
    


if __name__ == "__main__":
    filepath = 'hits.txt'
    list_of_ip = data_preparation(filepath)
    list = five_common_ip(list_of_ip)
    for ip in list:
        print(ip)
    