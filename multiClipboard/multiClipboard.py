import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def saveItems(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def loadItems(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = loadItems(SAVED_DATA)
    
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        saveItems(SAVED_DATA, data)
    elif command == "list":
        print("list")
    elif command == "load":
        print("load")
    else:
        print("Unknown command")
else:
    print("Please input exactly 2 commands")