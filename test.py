from NewRelic import Config
from NewRelic.REST.Users import Users

from NewRelic.Insights import Insights

Config.API_KEY = 'a5dddf11c60833e89fd73b39e59438456aea2b0e0477d99'

query_key = 'NRIQ-Jx8rU3vspwnvwL2Kj6lP3EDq5dwah6C8'

print(Insights(query_key=query_key).query(1690570, nrql='SELECT * from PageView'))

# print(Users().show(id = None))
