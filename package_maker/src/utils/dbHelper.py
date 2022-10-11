import os.path
import sqlite3

from package_maker.src.resource import message_box

class ConnectDB(object):

    def __init__(self, db_file=None):
        self.db_file = db_file

    def check_db(self):
        if not os.path.exists(self.db_file):
            os.makedirs(os.path.dirname(self.db_file))

    def __enter__(self):
        self.check_db()
        self.conn = sqlite3.connect(self.db_file)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()


if __name__ == '__main__':
    with ConnectDB(r"C:\mnt\mpcparis\A5\io\To_Client\packages\.package\asterix.db") as tt:
        tt.execute("SELECT client_version FROM roto WHERE shot = '080_bb_0375'")


    tr = tt.fetchone()
    print(tr, type(tr[0]))

