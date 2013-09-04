import Host

class Proxy:
	def __init__(self, proxy_type=ProxyType.Transparent, client_list=[], server_list=[], proxy_addr='localhost', proxy_port=8080):
		assert type(proxy_type) is ProxyType, "Provided proxy_type is not a ProxyType!" 
		assert type(client_list) is list, "Provided client_list is not a list type!"
		assert type(server_list) is list, "Provided server_list is not a list type!"
		#TODO assert the types of proxy_addr and proxy_port
		self.proxy_type = proxy_type
		self.client_list = client_list
		self.server_list = server_list
		self.proxy_addr = proxy_addr
		self.proxy_port = proxy_port

		self.create_ip_table_rule()
	def create_ip_table_rule()
			

	#TODO create set_client_list etc. 
	
	
class ProxyType:
	Transparent, Interactive = range(2)
