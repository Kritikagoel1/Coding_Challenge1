try:
    from Util.dbconnection import Connect
    mdb=Connect()
    mdb.dbconnect()
except:
    print("Database Connection Unsuccessful")

class MainModule():
    from Dao.functions import display_pet,donation_record,adoption_event_manage

    display_pet()
    donation_record()
    adoption_event_manage()
