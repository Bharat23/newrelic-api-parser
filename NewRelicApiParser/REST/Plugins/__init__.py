from NewRelicApiParser.Base import BaseNewRelic


class Plugins(BaseNewRelic):
    def __init__(self, API_KEY):
        super().__init__(API_KEY)

    def get_list(self, options: dict = {}) -> dict:
        """
        fetch the plugins for new relic
        """
        url = self.BASE_URI + "/plugins.json"
        return super().get_data(url, options=options)

    def show(self, id: int) -> dict:
        """
        fetch single plugin based on id provided
        """
        url = self.BASE_URI + "/plugins/{0}.json".format(id)
        return super().get_data(url)
