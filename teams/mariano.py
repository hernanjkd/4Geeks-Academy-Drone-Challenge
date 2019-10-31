"""
4Geeks Hackathon
"""
import os
from pyparrot.Minidrone import Mambo

# CHANGE THIS?
mamboAddr = os.environ.get('DRONE_ADDRESS', "D0:3A:F7:D9:E6:20")

# Is it gonna be WIFI? ask.
mambo = Mambo(mamboAddr, use_wifi=False)

print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

if not success:
	exit(1)


print("sleeping")
mambo.smart_sleep(1)
mambo.ask_for_state_update()
mambo.smart_sleep(1)

print("taking off!")
mambo.safe_takeoff(5)
mambo.smart_sleep(1)


print("dancing")
mambo.turn_degrees(90)
mambo.smart_sleep(1)
mambo.turn_degrees(-90)
mambo.smart_sleep(1)

print("I wish I was dancing the meneaito")

mambo.fly_direct(roll=0, pitch=1, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=1, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=3, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=-5, yaw=0, vertical_movement=0, duration=1)
mambo.turn_degrees(90)
mambo.fly_direct(roll=0, pitch=5, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=-1, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=-1, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=-3, yaw=0, vertical_movement=0, duration=1)
mambo.turn_degrees(-180)
mambo.fly_direct(roll=0, pitch=2, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=2, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=-2, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=-3, yaw=0, vertical_movement=0, duration=1)
mambo.turn_degrees(90)

mambo.smart_sleep(1)

print("Look at me ma")

mambo.fly_direct(roll=15, pitch=0, yaw=20, vertical_movement=0, duration=1)
mambo.fly_direct(roll=-15, pitch=0, yaw=-20, vertical_movement=0, duration=1)

mambo.smart_sleep(1)

mambo.flip(direction="back")
mambo.smart_sleep(2)
mambo.flip(direction="front")
mambo.smart_sleep(2)

mambo.fly_direct(roll=0, pitch=1, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=1, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=3, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=-5, yaw=0, vertical_movement=0, duration=1)
mambo.turn_degrees(90)
mambo.fly_direct(roll=0, pitch=5, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=-1, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=-1, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=-3, yaw=0, vertical_movement=0, duration=1)
mambo.turn_degrees(-180)
mambo.fly_direct(roll=0, pitch=2, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=2, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=-2, yaw=0, vertical_movement=0, duration=1)
mambo.fly_direct(roll=0, pitch=-3, yaw=0, vertical_movement=0, duration=1)
mambo.turn_degrees(90)

mambo.flip(direction="right")
mambo.smart_sleep(2)
mambo.flip(direction="left")
mambo.smart_sleep(2)

mambo.turn_degrees(90)
mambo.smart_sleep(1)
mambo.turn_degrees(-90)
mambo.smart_sleep(1)
mambo.turn_degrees(-90)
mambo.smart_sleep(1)
mambo.turn_degrees(90)

mambo.safe_land(5)
mambo.smart_sleep(5)

mambo.disconnect()

# End program
exit(0)
