options = ["Yes","YES","Y","y"]

print("!!!!Welcome to Auto Compose!!!!\n")

print("Please Enter how many applications you want to configure\n")

number_of_apps = int(input())

final_string = "version: \"3.9\" \n" + "services: "

apps_counter = 1

def updateFinalString(update_string=None,type_of_field=None):
	return "\t\t{0}: {1}\n".format(type_of_field,update_string)

while number_of_apps > 0:
	print("Enter the name of the service {} \n".format(apps_counter))
	service_name = input()
	final_string += "\n\t {}:\n".format(service_name)
	print("Enter the name of the image")
	image_name = input()
	final_string += updateFinalString(image_name,"image")
	print("Do you want to add build location")
	add_build = input()
	if add_build in options:
		print("Enter build location (\".\" for current directory)")
		build = input()
		final_string += updateFinalString(build,"build")
	print("Do you want to add any command?")
	add_command = input()
	if add_command in options:
		print("Please enter the command")
		command = input()
		final_string+= updateFinalString(command,"command")
	print("Do you want to add an entrypoint")
	add_entrypoint = input()
	if add_entrypoint in options:
		print("Add entrypoint command")
		entrypoint = input()
		final_string += updateFinalString(entrypoint,"entrypoint")
	number_of_apps -= 1
	apps_counter += 1

with open("docker-compose.yaml","w") as f:
	f.write(final_string)

print("Done")


