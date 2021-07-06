import os                                                                                                             

folder = input("Please input the folder path: ")

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name) + " file size: " + str(os.stat(os.path.join(root, name)).st_size))
            
    return r

finalList = list_files(folder)

fileName = input("Please input the file you want to create: ")

with open( fileName , 'w') as f:
    for item in finalList:
        f.write("%s\n" % item)

