from __future__ import print_function
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative

def back_drone():
    print("Returning to Launch")
    vehicle.mode = VehicleMode("RTL")
    # Close vehicle object before exiting script
    print("Close vehicle object")
    vehicle.close()

def call_drone():
    arm_and_takeoff(10)
    print("Set default/target airspeed to 1")
    vehicle.airspeed = 1
    print("Going towards first point for 3 seconds ...")
    #position is xiatian,
    point1 = LocationGlobalRelative(-35.361354, 149.165218, 15)
    vehicle.simple_goto(point1)
    # this is adjust the altitude, and arrive the target postition 
    point2 = LocationGlobalRelative(vehicle.location.global_relative_frame.lat, vehicle.location.global_relative_frame.lon,TARGet_ALTI )
    vehicle.simple_goto(point2)

    # adjust the altitude is sati
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
    	if vehicle.location.global_relative_frame.alt <= TARGET_ALTI * 1.05:
            print("Reached target altitude")
            break
        time.sleep(1)

def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto
    #  (otherwise the command after Vehicle.simple_takeoff will execute
    #   immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)



connection_string = "127.0.0.1:14551"
vehicle = connect(connection_string, wait_ready=True)
TARGET_ALTI = 2

if __name__ == '__main__':
    call_drone()
    back_drone()
