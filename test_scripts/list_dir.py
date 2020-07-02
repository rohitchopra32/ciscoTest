import os

path = input("enter path")

for i in os.listdir(path):
    print(i)