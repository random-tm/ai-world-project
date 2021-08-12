from io.input.file.loader.json import load_json_file

def get_db(self):
    db_config = load_json_file("./config/db.json")
    # TODO Implement DB based on type
    # Current considerations are MySQL\MariaDB, Cassandra, and Redis
