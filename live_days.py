from datetime import datetime


now = datetime.today()
birthday = datetime(1990, 5, 30)

live_days = now - birthday

print(live_days)
