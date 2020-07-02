import getpass
import sys
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

with telnetlib.Telnet(HOST) as tn:
    tn.read_until("login: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("ls\n")
    tn.write("exit\n")

    print(tn.read_all())