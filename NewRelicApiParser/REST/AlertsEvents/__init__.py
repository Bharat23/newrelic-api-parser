from NewRelicApiParser.Base import BaseNewRelic


class AlertsEvents(BaseNewRelic):
    def __init__(self, API_KEY: str):
        super().__init__(API_KEY)

    def get_list(self, options: dict = {}) -> dict:
        """
        fetch the alert events for new relic
        """
        url = self.BASE_URI + "/alerts_events.json"
        return super().get_data(url, options=options)
