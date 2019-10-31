
from pyparrot.Minidrone import Mambo
import os

# you will need to change this to the address of YOUR mambo
mamboAddr = os.environ.get('DRONE_ADDRESS')

# make my mambo object
# remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
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
    
    print("Flying direct: going up")
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=1)

    print("Showing turning (in place) using turn_degrees")
    mambo.turn_degrees(90)
    mambo.smart_sleep(2)

    print("flip left")
    print("flying state is %s" % mambo.sensors.flying_state)
    success = mambo.flip(direction="left")
    print("mambo flip result %s" % success)
    mambo.smart_sleep(4)

    # print("Flying direct: going up")
    # mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=0.5)

    mambo.turn_degrees(-90)
    mambo.smart_sleep(2)

    mambo.turn_degrees(-90)
    mambo.smart_sleep(2)
    
    print("Flying direct: going up")
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=1)    
    
    print("flip right")
    print("flying state is %s" % mambo.sensors.flying_state)
    success = mambo.flip(direction="right")
    print("mambo flip result %s" % success)
    mambo.smart_sleep(5)

    mambo.turn_degrees(90)
    mambo.smart_sleep(2)

    print("Flying direct: yaw")
    mambo.fly_direct(roll=0, pitch=0, yaw=30, vertical_movement=0, duration=1)
        
    mambo.turn_degrees(-180)
    mambo.smart_sleep(2)

    print("flip front")
    print("flying state is %s" % mambo.sensors.flying_state)
    success = mambo.flip(direction="front")
    print("mambo flip result %s" % success)
    mambo.smart_sleep(5)
                
    mambo.turn_degrees(180)
    mambo.smart_sleep(2)

    print("Flying direct: going backwards (negative pitch)")
    mambo.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=0.5)

                
    mambo.turn_degrees(180)
    mambo.smart_sleep(2)

    print("flip back")
    print("flying state is %s" % mambo.sensors.flying_state)
    success = mambo.flip(direction="back")
    print("mambo flip result %s" % success)
    mambo.smart_sleep(5)

    mambo.turn_degrees(360)
    mambo.smart_sleep(2)

    print("landing")
    print("flying state is %s" % mambo.sensors.flying_state)
    mambo.safe_land(5)
    mambo.smart_sleep(5)

print("disconnect")
mambo.disconnect()
