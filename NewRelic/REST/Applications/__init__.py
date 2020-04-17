from NewRelic.Base import BaseNewRelic
from NewRelic.CustomExceptions import ArgumentException

class Applications(BaseNewRelic):

    def get_list(self, options = {}):
        """
        fetch the apm applications for new relic
        """
        url = self.BASE_URI + '/applications.json'
        return super().get_data(url, options=options)