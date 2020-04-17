from NewRelic import Config
from NewRelic.REST.Users import Users

Config.API_KEY = 'a5dddf11c60833e89fd73b39e59438456aea2b0e0477d99'

print(Users().show(id = None))
