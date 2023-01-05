from rav_kav import RavKav
from datetime import datetime

if __name__ == "__main__":
    r = RavKav("292198319", "Daniel Raz")
    print(r.get_balance)
    r.top_up(5)
    print(r.get_balance)
    r.top_up(30)
    print(r.get_balance)
    r.ride(5, datetime.now().date())
    print()
    r.display_num_rides_by_dates_log()
    print()
    r.display_num_rides_by_type_log()

    print()
    print(r)
    print()
    print([r])
