print("importing data")
import os
import sys
print("SUCCESSFUL")

print("Creating Functions")
def create_id(id_in):
    print("Generating information")
    id_in = id_in.lower()
    try:
        level = id_in[0]
        sec = id_in[1]
        num = id_in[2]
        if level == "a" or level == "b":
            pass
        else:
            print("error: Issue with slice 1 (level)")
        if sec == "a" or sec == "b" or sec == "c":
            pass
        else:
            print("error: Issue with slice 2 (section)")
        return [level, sec, num]
    except:
        print("error: ID is not properly formated.")
def new(newID, content):
    newID = create_id(newID)
    full_id = ''.join(newID)
    print("Adding cabnet")
    file = open("D:\creation\code\pytho\cabnetic\saved.csv", "a")
    file.write(full_id + ", " + newID[0] + ", " + newID[1] + ", " + newID[2] + ", " + content)
    file.close()
def handler(command):
    if "new" in command:
        command = command.split(" ")
        if command[0] == "new":
            try:
                print("checking command")
                newID = command[1]
                newContent = command[2]
                new(newID, newContent)
            except:
                print("error: unknown issue with command.")
        else:
            print("error: Unknown format issue with command.")
    else:
        print("error: Command not found.")

def generate():
    try:
        file = open("D:\creation\code\pytho\cabnetic\saved.csv", "w")
        file.write("full_id, level, section, number, contents\n\n")
        file.close()
    except:
        print("error creating files, status: unknown.")
print("SUCCESSFUL")

print("Checking for external file data")
if os.path.exists("D:\creation\code\pytho\cabnetic\saved.csv"):
    print("SUCCESSFUL")
else:
    print("error finding data, generating new data")
    generate()
    errors += 1
    print("SUCCESSFUL")

print("STARTING SHELL")
print("type ? for help")
run = True
while run == True:
    command=input("User: ")
    if command == "?":
        print("""
?|Displays this help message.
create|creates new container.|new <id> content
find|finds container based on id.|find <id>
del|deletes container based on id.|del <id>
reset|deletes all containers.|reset
close|closes cabnetic|close
        """)
    elif command == "close":
        run = False
    else:
        handler(command)
