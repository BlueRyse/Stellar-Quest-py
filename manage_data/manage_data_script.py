import manage_data

source_secret = "your secret seed"
data_name = input("Insert the data name: ")
data_value = input("Insert the data value: ")
manage_data_op = manage_data.manage_data(source_secret,data_name,data_value)

print("Setted: " + data_name + " " + data_value + " for " + manage_data_op.source.public_key)
