from pathlib import Path

def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

def createFile():
    try:
        readFileAndFolder()
        name = input('Please tell your file name :- ')
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data=input("What you want to write in this file :- ")
                fs.write(data)

            print("File Created Successfully!")
        else:
            print("This File already exists!")
    except Exception as err:
        print(f"An error occured as {err}")

print('Type 1 for creating a file')
print('Type 2 for reading a file')
print('Type 3 for updating a file')
print('Type 4 for deleting a file')

check = int(input('Please tell your response :- '))

if check == 1:
    createFile()