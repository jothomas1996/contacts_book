import json_file

# delete all contacts in list
def delete_all():
	confirm = input("Are you sure you want to delete all contacts from contact book [yes / no]: ").lower()
	if confirm == "yes":
		deleted_data = json_file.read('deleted_data.json')
		data = json_file.read('data.json')

		for contact in data:
			deleted_data.append(contact)

		# write to file
		json_file.write('data.json', [])
		json_file.write('deleted_data.json', deleted_data)

		print("All contacts are deleted")
		return 1
	else:
		return 0

# delete single contact in list
def delete_contact(contact_index):
	temp_data = json_file.read('data.json')

	# retrive name
	name = temp_data[contact_index]["name"]["name_preffix"] + " " + temp_data[contact_index]["name"]["first_name"] + " " + temp_data[contact_index]["name"]["middle_name"] + " " + temp_data[contact_index]["name"]["last_name"] + " " + temp_data[contact_index]["name"]["name_suffix"]

	confirm = input("Are you sure you want to delete " + name + " from contact book [yes / no]: ").lower()

	if confirm == "yes":
		# delete contact
		temp_deleted_data = temp_data.pop(contact_index)

		# write back to main file
		json_file.write('data.json', temp_data)

		# write to delete database
		temp_data = json_file.read('deleted_data.json')
		temp_data.append(temp_deleted_data)
		json_file.write('deleted_data.json', temp_data)

		print(name, "has been deleted from contact book")
		return 1
	else:
		return 0
