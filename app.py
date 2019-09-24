class Alert:

    def __init__(self, alert_attributes):
        for attr_name, attr_value in alert_attributes.items():
            setattr(self, attr_name, attr_value)

class AlertsList:

    LIST = []

    def __init__(self, alert):
        self.LIST.append(alert)

    def add_alert(self, alert):
        self.LIST.append(alert)

    def display_alerts(self):
        print(self.LIST)
        return self.LIST

def main():
    alert_attributes = {
        "id": "1234",
        "category": "dark web",
        "score": 78,
        "date": "2017/11/03 15:00:56 UTC",
        "status": "new",
        "client": "Johnny",
        "summary": "This is a summary of the alert's content"
    }

    alert = Alert(alert_attributes)
    alerts = AlertsList(alert)
    alerts.add_alert(alert)
    alerts.display_alerts()

main()
