class BikeRental():
    def __init__(self):
        self.bikes = 5
        self.hourly_rate = 5
        self.daily_rate = 20
        self.weekly_rate = 60
        self.unlock = 5
        self.revenue = 0

    def rent_bikes(self):
        self.user_action = input("###---WELCOME TO PS BIKE RENTALS---###\nPlease select if you like to rent the bikes or return the bikes:\nTo rent the bikes type 'Rent'\nTo return the bikes type 'Return'\n").lower()
        if self.user_action == "rent":
            self.user_input_bikes = int(input(f"###---RENT---###\nPlease select number of bikes you would like to rent\nAvailable number of bikes: {self.bikes}\nPlease enter: "))
            if self.user_input_bikes <= self.bikes:
                self.user_input_use = input("Please select what type of use suites you?\nHourly: $5\nDaily: $20\nWeekly:$60\n").lower()
            else:
                print("We do not have sufficient number of bikes. Please check the number of available bikes and try again. Thank you!")
        elif self.user_action == "return":
            self.user_return_bikes = int(input("###---RETURN---###\nPlease type the number of bikes you want to return: "))
            self.bikes += self.user_return_bikes

    def usage(self):
        if self.user_input_use == "hourly":
            user_input_hours = int(input("Please specify the number of hours: "))
            self.hourly_bill = user_input_hours * self.hourly_rate * self.user_input_bikes
            return print(f"Total billable amount for {self.user_input_bikes} bikes for {user_input_hours} hours is ${self.hourly_bill}")
        elif self.user_input_use == "daily":
            user_input_days = int(input("Please specify the number of days: "))
            self.daily_bill =  user_input_days * self.daily_rate * self.user_input_bikes
            return print(f"Total billable amount for {self.user_input_bikes} bikes for {user_input_days} days is ${self.daily_bill}")
        elif self.user_input_use == "weekly":
            user_input_weeks = int(input("Please specify the number of weeks: "))
            self.weekly_bill = user_input_weeks * self.weekly_rate * self.user_input_bikes
            return print(f"Total billable amount for {self.user_input_bikes} bikes for {user_input_weeks} weeks is ${self.weekly_bill}")

    def payment(self):
        print("###---PAYMENT---###")
        user_money_10 = int(input("Please insert $10 notes: "))
        user_money_5 = int(input("Please insert $5 notes: "))
        user_money_1 = int(input("Please insert $1 notes: "))

        user_payment = user_money_10 * 10 + user_money_5 * 5 + user_money_1 * 1

        if self.user_input_use == "hourly":
            if user_payment > self.hourly_bill:
                difference = user_payment - self.hourly_bill
                self.unlock -= self.user_input_bikes
                self.bikes -= self.user_input_bikes
                self.revenue = self.revenue + user_payment - difference
                return print(f"Here is your change ${difference}. Payment done successfully! Bikes are unlocked")
            elif user_payment == self.hourly_bill:
                self.unlock -= self.user_input_bikes
                self.bikes -= self.user_input_bikes
                self.revenue = self.revenue + user_payment
                return print("Payment done successfully! Bikes are unlocked")
            elif user_payment < self.hourly_bill:
                return print(f"Payment Unsucessful! Please try again")
            
        if self.user_input_use == "daily":
            if user_payment > self.daily_bill:
                difference = user_payment - self.daily_bill
                self.unlock -= self.user_input_bikes
                self.bikes -= self.user_input_bikes
                self.revenue = self.revenue + user_payment - difference
                return print(f"Here is your change ${difference}. Payment done successfully! Bikes are unlocked")
            elif user_payment == self.daily_bill:
                self.unlock -= self.user_input_bikes
                self.bikes -= self.user_input_bikes
                self.revenue = self.revenue + user_payment
                return print("Payment done successfully! Bikes are unlocked")
            elif user_payment < self.daily_bill:
                return print(f"Payment Unsucessful! Please try again")
            
        if self.user_input_use == "weekly":
            if user_payment > self.weekly_bill:
                difference = user_payment - self.weekly_bill
                self.unlock -= self.user_input_bikes
                self.bikes -= self.user_input_bikes
                self.revenue = self.revenue + user_payment - difference
                return print(f"Here is your change ${difference}. Payment done successfully! Bikes are unlocked")
            elif user_payment == self.weekly_bill:
                self.unlock -= self.user_input_bikes
                self.bikes -= self.user_input_bikes
                self.revenue = self.revenue + user_payment
                return print("Payment done successfully! Bikes are unlocked")
            elif user_payment < self.weekly_bill:
                return print(f"Payment Unsucessful! Please try again")
            
    def report(self):
        if self.user_action == "report":
            return print(f"Total revenue generated: ${self.revenue}\nTotal Bikes Available: {self.bikes}")
