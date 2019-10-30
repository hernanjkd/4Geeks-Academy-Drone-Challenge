
from pyparrot.Minidrone import Mambo
import os

# you will need to change this to the address of YOUR mambo

# make my mambo object
# remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect

mamboAddr = os.environ.get('DRONE_ADDRESS')

mambo = Mambo(mamboAddr, use_wifi=False)

print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

if (success):
    # get the state information
    print("sleeping")
    mambo.smart_sleep(2)
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)

    print("taking off!")
    mambo.safe_takeoff(5)

    print("Flying direct: going forward (positive pitch)")
    mambo.fly_direct(roll=50, pitch=50, yaw=0, vertical_movement=0, duration=0.5)
    mambo.fly_direct(roll=-50, pitch=-50, yaw=0, vertical_movement=0, duration=0.5)
    mambo.fly_direct(roll=50, pitch=50, yaw=0, vertical_movement=0, duration=0.5)
    mambo.fly_direct(roll=-50, pitch=-50, yaw=0, vertical_movement=0, duration=0.5)
    mambo.fly_direct(roll=50, pitch=50, yaw=0, vertical_movement=0, duration=0.5)
    mambo.fly_direct(roll=-50, pitch=-50, yaw=0, vertical_movement=0, duration=0.5)


    print("Showing turning (in place) using turn_degrees")
    mambo.turn_degrees(90)
    mambo.smart_sleep(2)
    mambo.turn_degrees(-90)
    mambo.smart_sleep(2)

    print("Flying direct: yaw")
    mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=0.4)
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=0.4)
    mambo.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=0.4)
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-50, duration=0.4)

    mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=0.4)
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=0.4)
    mambo.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=0.4)
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-50, duration=0.4)

    mambo.fly_direct(roll=0, pitch=0, yaw=90, vertical_movement=0, duration=0.4)

    mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=0.4)
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=0.4)
    mambo.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=0.4)
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-50, duration=0.4)

    mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=0.4)
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=0.4)
    mambo.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=0.4)
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-50, duration=0.4)

    mambo.fly_direct(roll=0, pitch=0, yaw=90, vertical_movement=0, duration=0.4)

    mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=0.4)
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=0.4)
    mambo.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=0.4)
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-50, duration=0.4)

    mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=0.4)
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=0.4)
    mambo.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=0.4)
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-50, duration=0.4)

    mambo.fly_direct(roll=0, pitch=0, yaw=90, vertical_movement=0, duration=0.4)

    print("Flying direct: going backwards (negative pitch)")
    mambo.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=-50, duration=0.4)
    mambo.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=50, duration=0.4)
    mambo.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=-50, duration=0.4)
    mambo.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=50, duration=0.4)
    mambo.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=-50, duration=0.4)
    mambo.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=50, duration=0.4)

    print("Boogie Woogie")
    mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=0.5)
    mambo.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=0.5)
    mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=0.5)
    mambo.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=0.5)
    mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=0.5)
    mambo.fly_direct(roll=-50, pitch=0, yaw=0, vertical_movement=0, duration=0.5)

    print("Flying direct: going up")
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=1)

    print("Flying direct: going around in a circle (yes you can mix roll, pitch, yaw in one command!)")
    mambo.fly_direct(roll=25, pitch=0, yaw=50, vertical_movement=0, duration=3)

    print("landing")
    mambo.safe_land(5)
    mambo.smart_sleep(5)

    print("disconnect")
    mambo.disconnect()
