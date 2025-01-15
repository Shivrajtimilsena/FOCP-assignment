file_name = input("Enter the name of the file you want to back up: ")

try:
    with open(file_name, 'r') as original_file:
        file_contents = original_file.read()

    backup_file_name = file_name.split('.')[0] + "_backup." + file_name.split('.')[1]

    with open(backup_file_name, 'w') as backup_file:
        backup_file.write(file_contents)

    print(f"Backup of {file_name} created as {backup_file_name}")

except FileNotFoundError:
    print(f"The file {file_name} does not exist.") #error handling if file doesnot exist
except Exception as e:
    print(f"Error occurred while creating the backup: {e}")