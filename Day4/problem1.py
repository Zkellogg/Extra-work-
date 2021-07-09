name1 = input("What is your first name? : ")
name2 = input("What is your last name? : ")
# address = input("Where do you live? : ")
# address2 = input("Where else do you live? : ")

full_address = {"street": "street1", "state": "state1"}
full_address2 = {"street": "street2", "state": "state2"}

full_names = {"firstname": name1, "lastname": name2}

name_and_addresses = [full_names, full_address, full_address2]


# print(full_names["firstname"] , full_names["lastname"])

print(name_and_addresses)
# test
