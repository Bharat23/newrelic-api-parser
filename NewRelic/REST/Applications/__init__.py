from NewRelic.Base import BaseNewRelic
from NewRelic.CustomExceptions import ArgumentException

class Applications(BaseNewRelic):

    def get_list(self, options = {}):
        """
        fetch the apm applications for new relic
        """
        url = self.BASE_URI + '/applications.json'
        return super().get_data(url, options=options)

    def show(self, app_id):
        """
        fetch single application data
        """
        url = self.BASE_URI + '/applcations/{0}.json'.format(app_id)
        return super().get_data(url)

    def dele(self, app_id):
        """
        fetch single application data
        """
        url = self.BASE_URI + '/applcations/{0}.json'.format(app_id)
        return super().delete(url, app_id)