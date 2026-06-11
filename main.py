#===============================
# Mars Rover Dust Sensing System
#===============================
#Logan Brown
#6/03/2026

#Variables
rover_s = "Stationary "
rover_o = "Operating "
rover_c = "Panels dirty, initating cleaning process. "                                              #status signals the panel wipers to begin the cleaning process
rover_status = rover_o                                                                              #setting the default status to operating is the intial status of the rover beginning its mission objective
battery_reserves = 100
dust_storm = (input("Dust storm status: (Active/Clear)"))                                           #This information is acquired through a sensor. 

if dust_storm == "Clear":
    solar_panels = int(input("Dust accumulation percentage (1-100) :"))                             #This information is acquired through a sensor. 
    if solar_panels <= 10:
        rover_status = rover_o
        print(f"Rover status: {rover_o} ")
    elif 10 < solar_panels <= 100:
        rover_status = rover_c
        print(f"Rover status: {rover_c} ")
    else:
        rover_status = rover_s
        print(f"Rover status: {rover_s} ")
elif dust_storm == "Active":

    print("Dust storm active!") 
    print(f"Rover status: {rover_s}") 
    print("Sleep mode is active, battery reserves engaged. Sending most recent coordinates! ")       #Coordinates are sent to mission control to track the rover's status manually in the storm. 

    lattitude = (18.38) #North
    longitude = (77.53) #East 
    print(lattitude,"N" , longitude,"W")

    while True:
        print("Coordinates saved, awaiting clearance for cleaning procedure. ")

        a = "Active"
        c = "Clear"

        panel_sensor = (input("Dust storm status: (Active/Clear)? "))
        if panel_sensor == c: 
            print("Dust storm has passed! Rebooting main battery system. ") 
            print("Initializing cleaning procedure. ")
            solar_panels = int(input("Dust accumulation percentage (1-100) :"))
            rover_status = rover_c
            break
        else:
            continue
else:
    print("Invalid input, please try again. ")


if rover_status == rover_c:
    while solar_panels > 0:
        solar_panels -= 1
        print(f"Executing cleaning procedure, dust accumulation: {solar_panels}%  ")
    print("Solar panels are clear of all dust!") 
    print("Resuming all operations and restoring battery reserves to full charge. ")

#===========================
#Sand trap manuvering system 
#===========================
