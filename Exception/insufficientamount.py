class Insufficient_amount(Exception):
    def __init__(self, message="Insufficient amount."):
        self.message = message
        super().__init__(self.message)


class CashDonation(Donation):
    def __init__(self, donor_name, amount, donation_date):
        super().__init__(donor_name, amount)
        self.DonationDate = donation_date

    def record_donation(self):
        try:
            if self.Amount<200.0:
                raise Insufficient_amount

            print(f"Cash donation of ${self.Amount} recorded on {self.DonationDate} by {self.DonorName}")
        except Insufficient_amount():
            raise Insufficient_amount()


try:

    donor_name=input("enter name")
    amount = float(input("enter amount"))
    donation_date=input("enter num")

    cash_donation=CashDonation(donor_name,amount,donation_date)
    cash_donation.record_donation()
except ValueError:
    print("Error: Please enter a valid number for the donation amount")