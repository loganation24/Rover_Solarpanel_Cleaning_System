#===============================
# Mars Rover Dust Sensing System
#===============================
#Logan Brown
#6/03/2026

#Variables
rover_s = "Stationary "
rover_o = "Operating "
rover_c = "Panels dirty, initating cleaning process. "                                              #status signals the panel wipers to begin the cleaning process
rover_m = "Rover is currently moving. "
rover_status = rover_o                                                                              #setting the default status to operating is the intial status of the rover beginning its mission objective
battery_reserves = 100
dust_storm = (input("Dust storm status: (Active/Clear)"))                                           #This information is acquired through a sensor. 

while True:
    if dust_storm == "Clear":
        solar_panels = int(input("Dust accumulation percentage (1-100): "))
        if solar_panels <= 10:
            rover_status = rover_o
            print(f"Rover status: {rover_o}")
        elif 10 < solar_panels <= 100:
            rover_status = rover_c
            print(f"Rover status: {rover_c}")
        else:
            rover_status = rover_s
            print(f"Rover status: {rover_s}")
        break
    elif dust_storm == "Active":
        print("Dust storm active!")
        print(f"Rover status: {rover_s}")
        print("Sleep mode is active, battery reserves engaged. Sending most recent coordinates!")
        lattitude = 18.38  # North
        longitude = 77.53  # East
        print(lattitude, "N", longitude, "E")  # ← also changed W to E
        while True:
            print("Coordinates saved, awaiting clearance for cleaning procedure.")
            panel_sensor = input("Dust storm status: (Active/Clear)? ")
            if panel_sensor == "Clear":
                print("Dust storm has passed! Rebooting main battery system.")
                print("Initializing cleaning procedure.")
                solar_panels = int(input("Dust accumulation percentage (1-100): "))
                rover_status = rover_c
                break
            else:
                continue
        break
    else:
        print("Invalid input, please try again.")


if rover_status == rover_c:
    while solar_panels > 0:
        solar_panels -= 1
        print(f"Executing cleaning procedure, dust accumulation: {solar_panels}%  ")
    print("Solar panels are clear of all dust!") 
    print("Resuming all operations and restoring battery reserves to full charge. ")

#===========================
#Sand trap manuvering system 
#===========================
#rover must detect that it is stuck, so we are going to ask the user to input rotational velocity [m/s] and time [s] to calculate for displacement
#if the displacement is zero, then the rover knows its stuck and will intiate the manuvering system 

#-------------------------
#Formula for Displacement:
#-------------------------
#find wheel circumference then mutiply by amount of wheel rotations
from math import pi
def displacement_calc(rotational_velocity , time):
    wheel_diam = 0.50 #meters
    circumference = wheel_diam * pi
    rotations = (rotational_velocity / 60) * time 
    displacement = rotations * circumference
    return displacement 

rover_moving_check = input("Is rover currently moving? (Yes/No)") #Calculated through accelerometer inside rover
while True:
    if rover_moving_check == "Yes":
        #----------------------------------------------------------------------------
        velocity = float(input("Enter rotational velocity (rotations per minute): "))
        time = float(input("Enter time in seconds: "))
        displacement = displacement_calc(velocity, time)
        print(f"Expected displacement: {displacement:.2f} meters")
        #----------------------------------------------------------------------------

        print("Rover is moving normally continuing all operations.")
        print(f"Rover's actual displacement: {displacement:.2f} meters. ")
        break
    elif rover_moving_check == "No":
        #----------------------------------------------------------------------------
        velocity = float(input("Enter rotational velocity (rotations per minute): "))
        time = float(input("Enter time in seconds: "))
        displacement = displacement_calc(velocity, time)
        print(f"Expected displacement: {displacement:.2f} meters")
        #----------------------------------------------------------------------------
        
        print("Rover is stuck! Extending wheel paddles... ")
        break
    else: 
        print("Invalid input, please try again")
