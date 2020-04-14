# We need to receive the basic info of user
#(first_name,last_name,age,email)
# and save them as keys into a dict call user.
#After recive the data, shw the info in the console

user = {}
user["first_name"] = input("hey bro, cual es tu nombre?:")
user["last_name"] = input("como dices que se apellidan tus gfes?: ")
user["age"] = input("ya alcanzar el timbre?: ")
user["email"] =input("pasame tu correo para enviarte unas fotos: ")

for key, value in user.items():
    print(f"{key.capitalize()}: {value}")