import random
import string
import socket
import struct
import sqlite3


class SqlLite3Connection:
    def __init__(self, database_path):
        self.database_path = database_path

    def __get_connection(self):
        return sqlite3.connect(database=self.database_path)

    def __get_cursor(self):
        return self.__connection.cursor()

    def execute_query(self, query, params=None):
        curr = self.__get_cursor()
        curr.execute(query, params)
        print(curr.lastrowid, " --> Row Inserted into Table")

    def __enter__(self):
        self.__connection = self.__get_connection()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__connection.commit()
        self.__connection.close()


no_of_records = int(input("Enter no of records"))

with SqlLite3Connection("../db.sqlite3") as conn:
    router_type = ["AG1", "CSS"]
    for i in range(no_of_records):
        # Generate unique Ip Address
        ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        # Generate unique Mac Address
        mac_address = "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255),
                                 random.randint(0, 255),
                                 random.randint(0, 255))
        # Generate unique Sapid
        sapid = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=10))
        # Generate unique Hostname
        hostname = ''.join(random.choices(string.ascii_uppercase +
                                       string.digits, k=10))
        # choose between AG1 & CSS
        router = random.choices(router_type)
        conn.execute_query(
            "INSERT INTO router_router (router_type, sap_id, host_name, loopback, is_active, mac_address) VALUES (?, ?, ?, ?, ?, ?)",
            (router[0], sapid, hostname, ip, True, mac_address)
        )