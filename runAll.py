def main():
    import os
    path = 'C:\UsefulScripts\\'


    #read in blacklisted files
    blacklist = []
    for e in open(path+'blacklist.txt', 'r').readlines():
        blacklist.append(e.strip())

    for f in os.listdir(path):
        if f not in blacklist and f[-4:] == '.bat':
            os.system(path + f)


if __name__ == "__main__":
    main()