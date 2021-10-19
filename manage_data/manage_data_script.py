import manage_data
from stellar_sdk import Keypair

source_secret = "SCWUTKBTSPKETXBAIFOIK6ZY33AJILNDGJTIN7J5QK7JCZBUFDPFCQKS"
data_name = input("Insert the data name: ")
data_value = input("Insert the data value: ")
manage_data_op = manage_data.manage_data(source_secret,data_name,data_value)

print("Set: " + data_name + " " + data_value + " for " + manage_data_op.source.public_key)
