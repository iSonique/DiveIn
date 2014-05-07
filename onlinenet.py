import slumber, requests


class onlinenet:
	def start(self, apikey):
		api_session = requests.session()
		api_session.headers['Authorization'] = 'Bearer ' + apikey
		api = slumber.API('https://api.online.net/api/v1', session=api_session)
		return api

	def user_info(self, apikey):
		api = self.start(apikey)
		user_info = api.user.info.get()
		return user_info

	def abuse(self, apikey):
		api = self.start(apikey)
		abuses = api.abuse.get()
		return abuses

	def abuse_info(self, apikey, abuseid):
		api = self.start(apikey)
		abuse_info = api.abuse.info.get({ 'alert_id': abuseid })
		return abuse_info

	def abuse_reply(self, apikey, abuseid, answer, solution):
		api = self.start(apikey)
		abuse_reply = api.abuse.reply.post({ 'alert_id': abuseid, 'answer': answer, 'solution': solution})
		return abuse_reply

	def ddos(self, apikey):
		api = self.start(apikey)
		ddos_list = api.ddos.list.get()
		return ddos_list

	def ddos_info(self, apikey, ddosid):
		api = self.start(apikey)
		ddos_info = api.ddos.info.get({ 'alert_id': ddosid })
		return ddos_info

	def d2dos(self, apikey):
		api = self.start(apikey)
		ddos_list1 = api.ddos1.get()
		return ddos_list1
