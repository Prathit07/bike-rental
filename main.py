from bikeRental import BikeRental

machine_on = True
bike_rental = BikeRental()
while machine_on == True:
    bike_rental.rent_bikes()
    if bike_rental.user_action == "rent":
        if bike_rental.bikes >= bike_rental.user_input_bikes:
            bike_rental.usage()
            bike_rental.payment()
        else:
            pass
    elif bike_rental.user_action == "return":
        pass
    elif bike_rental.user_action == "report":
        bike_rental.report()