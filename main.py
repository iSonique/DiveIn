from online import onlinenet

apikey = '2b5b1f962f2fcc1dc094c0b7c0b444dd7bac8381'
#apikey = 'f76be1f975fc03e08f1e43ac37dabdbe8d52f435'
onlineapi = onlinenet()

#print onlineapi.ddos(apikey)

print onlineapi.ddos_info("183414", apikey)
