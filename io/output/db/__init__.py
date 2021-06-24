from json import loadjsonfile

def get_db(self):
    db_config = loadjsonfile("./config/db.json")
    #TODO Implement DB based on type
    #Current considerations are MySQL\MariaDB, Cassandra, and Redis