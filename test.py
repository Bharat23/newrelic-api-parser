from NewRelicApiParser import Config
from NewRelicApiParser.REST.Users import Users

from NewRelicApiParser.Insights import Insights

from NewRelicApiParser.Graph import GraphQlApi

# Config.API_KEY = 'a5dddf11c60833e89fd73b39e59438456aea2b0e0477d99'

# query_key = 'NRIQ-Jx8rU3vspwnvwL2Kj6lP3EDq5dwah6C8'

# print(Insights(query_key=query_key).query(1690570, nrql='SELECT * from PageView'))

print(GraphQlApi(graphql_key='346M14LO9OV42318NQR3U6LPCX0TTR68').query('{\
                actor {\
                entitySearch(query: "type in (\'DASHBOARD\') and accountId = 1690570") {\
                  results {\
                    entities {\
                      ... on DashboardEntityOutline {\
                        guid\
                        name\
                      }\
                    }\
                    nextCursor\
                  }\
                }\
                }\
                }'))

# print(Users().show(id = None))
