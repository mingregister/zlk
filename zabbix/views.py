from django.shortcuts import render
from django.shortcuts import reverse

from django.http import HttpResponse
from django.views.generic import View

from .utils import zapi

# Create your views here.

def index(request):
	context = dict()
	return render(request,'zabbix/index.html',context)


class Q_host(View):
	
	def get(self, request):
		host = dict()
		cururl = reverse('zabbix:zabbixindex')
		host['cururl']=cururl
		return render(request,'zabbix/result.html', host)

	def post(self, request):
		hostid = request.POST['id']
		try:
			zbx = zapi.ZAPI()
			hosts = zbx.host.get(hostids=hostid)
			host = hosts[0]
			cururl = reverse('zabbix:zabbixindex')
			host['cururl']=cururl
		except Exception as e :
			return HttpResponse('query zabbix {} failed'.format(e.args))

		return render(request,'zabbix/result.html', host)

class Q_history(View):

	def get(self, request):
		pass

	def post(self, request):
		pass
