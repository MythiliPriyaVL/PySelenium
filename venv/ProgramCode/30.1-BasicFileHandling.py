def main():
    f = open("textfile.txt", "w+")

    for i in range(10):
        f.write("this is line " + str(i) +"\r\n")

    f = open("textfile.txt", "a+")
    f.write("this is line " + str(10) +"\r\n")

    f.close()

    f = open("textfile.txt", "r")
    #Open file and read complete contents
    if f.mode == 'r':
        contents = f.read()
        print(contents)

    #Open file and read lines one by one
    if f.mode == 'r':
        fl = f.readlines()
        for x in fl:
            print(x)

if __name__ =="__main__":
    main();