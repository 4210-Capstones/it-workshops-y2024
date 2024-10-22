import pinching_at_location_example
from pinching_at_location_example import MyListener as Listener
import leap, time

new_listener = Listener()
connection = leap.Connection()
connection.add_listener(new_listener)

with connection.open():
    while True:
        print(new_listener.is_pinching())
        print(new_listener.get_palm_position())
        time.sleep(0.3)