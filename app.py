print("importing data")
import os
import sys
path = os.path.dirname(os.path.abspath(__file__))
saved_path = path + "\saved.csv"
print("SUCCESSFUL")

print("Creating Functions")
def create_id(id_in):
    print("Generating information")
    id_in = id_in.lower()
    try:
        level = id_in[0]
        sec = id_in[1]
        num = id_in[2:]
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
    file = open(saved_path, "a")
    file.write(full_id + ", " + newID[0] + ", " + newID[1] + ", " + newID[2] + ", " + content + "\n")
    file.close()
def search(findID):
    file.open(saved_path, "r")
    if findID in file.read():
        print("Cabnet found")
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
    elif command[0] == "find":
        try:
            findID = command[1]
            search(findID)
        except:
            print("error: unknown issue with command.")
    else:
        print("error: Command not found.")

def generate():
    try:
        file = open(saved_path, "w")
        file.write("full_id, level, section, number, contents\n\n")
        file.close()
    except:
        print("error creating files, status: unknown.")
print("SUCCESSFUL")

print("Checking for external file data")
if os.path.exists(saved_path):
    print("SUCCESSFUL")
else:
    print("error finding data, generating new data")
    generate()
    print("SUCCESSFUL")

print("STARTING SHELL")
print("type ? for help")
run = True
while run == True:
    command=input("User: ")
    if command == "?":
        print("""
__BASIC__
?|Displays this help message.
info|Displays information about this app.|info
close|closes cabnetic|close
__CABNET__
create|creates new container.|new <id> content
find|finds container based on id.|find <id>
del|deletes container based on id.|del <id>
reset|deletes all containers.|reset
__ADVANCED__
set|changes settings.
show_saved|opens data file.
source|Opens source file.
        """)
    elif command == "close":
        run = False
    elif command == "reset":
        try:
            generate()
        except:
            print("error: Unknown error resetting file.")
        print("Reset properly")
    elif command == "about":
        print("""
This is an inventory management system, created in a terminal.  Yeah, its a "light" UI, I know.  I will probably use the basics of this code in the future to create a website/app/mobile app.  But that, for now, is not what this project is about.  As this is in the terminal, I tried to make it as easy to use as possible to use.  Now, for the part your probably waiting for, this allows you to add, edit, and find information about bins, cabinets, or anything else that would be personal inventory.  This would be super useful for moving, or insurance/purposes(I may add a setting for value of the "crate").  This started out as a project to manage stuff in cabinets, cause, you know, you can't generally see in them, so it's hard to id them.  It comes with a standard id system with a default of 2 parameters(this number can be changes, cool, I know), that I started out using as level, and section, then a sequential number as an id, which can be changed to letters, I know, again, so cool.  Anyway, this is dragging on and I should be writing more code for this, so enjoy.
        """)
    else:
        handler(command)
