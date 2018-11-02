import sys
import logging
import json

from pyzabbix import ZabbixAPI
from utils.modify_config import read_config

logtype = logging.WARN
stream = logging.StreamHandler(sys.stdout)
stream.setLevel(logtype)
log = logging.getLogger('pyzabbix')
log.addHandler(stream)
log.setLevel(logtype)

ZabbixServer = read_config('zabbix','ZabbixServer')
User = read_config('zabbix','User')
Password = read_config('zabbix','Password')


def ZAPI():
	ZabbixServerUrl = ZabbixServer
	zapi = ZabbixAPI(ZabbixServerUrl)
	zapi.login(User, Password)
	return zapi


if __name__ == '__main__':
	# import pdb; pdb.set_trace()
	zbx = ZAPI()
	host = zbx.host.get(hostids='10257')[0]
	#host = json.dumps(host)
	print(host)
	name = host['name']
	print(type(name))
	print(name)
