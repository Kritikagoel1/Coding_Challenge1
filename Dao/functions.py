from Util.dbconnection import Connect
mdb=Connect()
mdb.dbconnect()

def display_pet():
    name = input("Enter pet name: ")
    age = int(input("Enter pet age: "))
    breed = input("Enter pet breed: ")
    try:

        create_pet_str = '''
        INSERT INTO pet (name, age, breed) VALUES (%s, %s, %s)
        '''
        data = [(name, age, breed)]
        mdb.perform_database_operation(create_pet_str, data)

        print('Inserted Successfully:')
    except:
        print("failed to insert data")

    def select():
        try:
           select_str = 'select * from pet'
           data=mdb.perform_database_operation(select_str)
           #data = mdb.fetchall()
           for p in data:
               print(p)

        except:
            print("couldn't select")
    select()

display_pet()

def donation_record():
    donor_name = input("enter donor name")
    amount = float(input("enter amount donated"))
    try:
       create_insert = '''insert into cash_donation(donor_name,amount) values(%s,%s)'''
       data = (donor_name, amount)

       mdb.perform_database_operation(create_insert, data)

       print('Inserted Successfully:')
    except:
        print("failed to insert data")


donation_record()

def adoption_event_manage():
    def display_upcoming_events():
        try:

            select_upcoming_events = 'SELECT * FROM adoption_event WHERE event_date > CURRENT_TIMESTAMP;'
            data=mdb.perform_database_operation(select_upcoming_events)


            for p in data:
                print(p)

            if not data:
                print("No upcoming adoption events.")
            else:
                print("Upcoming Adoption Events:")
                for event in data:
                    print(event)
        except:
            print(f"Error retrieving upcoming events:")

    def register_for_event():
        event_id = int(input("Enter the event ID you want to register for: "))
        participant_name = input("Enter your name: ")
        participant_contact = input("Enter your contact information: ")
        try:
            create_insert = '''INSERT INTO Participation (event_id, participant_name, participant_contact) VALUES (%s, '%s', '%s')'''
            data = (event_id, participant_name, participant_contact)

            mdb.perform_database_operation(create_insert % data)

            print('Registration Successful.')
        except:
            print("Registration not done")

    display_upcoming_events()
    register_for_event()
adoption_event_manage()