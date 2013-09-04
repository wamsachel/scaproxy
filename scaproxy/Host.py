
class Host:
	def __init__(self, ip_addr, h_name):
		self.ip_address = ip_addr
		self.hostname = h_name
	def get_address(self):
		return self.ip_address
	def get_hostname(self):
		return self.hostname
	#TODO Add set_addresses, set_hostname etc
	
