# coding: utf-8

import re
import requests
from pprint import pprint


#关闭证书验证
from requests.packages.urllib3.exceptions import InsecureRequestWarning, InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)



url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955'
text = requests.get(url, verify=False)
stations = re.findall(r'([A-Z]+)\|([a-z]+)', text.text)
stations = dict(stations)
stations = dict(zip(stations.values(), stations.keys()))
pprint(stations, indent=4)