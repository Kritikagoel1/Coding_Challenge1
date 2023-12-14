import datetime
from Util.dbconnection import Connect
mdb = Connect()
mdb.dbconnect()


# Get user input for pet table
name = input("Enter pet name: ")
age = int(input("Enter pet age: "))
breed = input("Enter pet breed: ")


create_pet_str = '''
INSERT INTO pet (name, age, breed) VALUES (%s, %s, %s)
'''
data = [(name, age, breed)]
mdb.perform_database_operation(create_pet_str,data)
print('Inserted Successfully:')

# Get user input for dog table
dog_breed = input("Enter dog breed: ")


create_dog_str = '''
INSERT INTO dog (dog_breed) VALUES (%s)
'''
mdb.perform_database_operation(create_dog_str, (dog_breed))

print("Dog record created successfully")

# Get user input for cat table
cat_color = input("Enter cat color: ")


create_cat_str = '''
INSERT INTO cat (cat_color) VALUES (%s)
'''
mdb.perform_database_operation(create_cat_str, (cat_color,))

print("Cat record created successfully")

# Get user input for pet_shelter table
shelter_name = input("Enter shelter name: ")


create_shelter_str = '''
INSERT INTO pet_shelter (shelter_name) VALUES (%s)
'''
mdb.perform_database_operation(create_shelter_str, (shelter_name,))

print("Pet Shelter record created successfully")

# Get user input for donation table
donor_name = input("Enter donor name: ")
amount = float(input("Enter donation amount: "))


create_donation_str = '''
INSERT INTO donation (donor_name, amount) VALUES (%s, %s)
'''
data = (donor_name, amount)
mdb.perform_database_operation(create_donation_str, data)

print("Donation record created successfully")

# Get user input for cash_donation table
donor_name = input("Enter cash donor name: ")
donation_amount = float(input("Enter cash donation amount: "))


create_cash_donation_str = '''
INSERT INTO cash_donation (donor_name, amount) VALUES (%s, %s)
'''
data = (donor_name, amount)
mdb.perform_database_operation(create_cash_donation_str, data)

print("Cash Donation record created successfully")

# Get user input for item_donation table
item_donor_name = input("Enter item donor name: ")
item_donation_amount = float(input("Enter item donation amount: "))
item_type = input("Enter item type: ")


create_item_donation_str = '''
INSERT INTO item_donation (donor_name, amount, item_type) VALUES (%s, %s, %s)
'''
data = [(donor_name, amount, item_type)]
mdb.perform_database_operation(create_item_donation_str, data)

print("Item Donation record created successfully")

# Get user input for adoption_event table
event_date_str = input("Enter event date (YYYY-MM-DD HH:MM:SS): ")
event_date = datetime.datetime.strptime(event_date_str, "%Y-%m-%d %H:%M:%S")


create_adoption_str = '''
INSERT INTO adoption_event (event_date) VALUES (%s)
'''
mdb.perform_database_operation(create_adoption_str, (event_date,))

print("Adoption Event record created successfully")

# Get user input for participation table
event_id = int(input("Enter event ID: "))
participant_name = input("Enter participant name: ")
participant_contact = input("Enter participant contact: ")


create_participation_str = '''
INSERT INTO participation (event_id, participant_name, participant_contact) VALUES (%s, %s, %s)
'''
data = [(event_id, participant_name, participant_contact)]
mdb.perform_database_operation(create_participation_str, data)

print("Participation record created successfully")

