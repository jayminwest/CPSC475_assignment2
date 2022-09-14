import sys

def open_infile():
    print("Here")
    while(True):
        filename = input("Enter file name: ")
        # Trying to open file:
        try:
            filename = open(filename, 'r')
            break
        except:
            print("File doesn't exist! Try again")
    return filename

def read_file(infile):
    mode = input("Read as string or line (S/L)? : ")
    if (mode == 'S'):
        string = infile.read()
    elif(mode == 'L'):
        text = ""
        for curr_line in infile:
            text += curr_line.rstrip('/n')
    else: 
        print("Invalid Entry")
        sys.exit()
    infile.close()

def main():
    open_infile()



if __name__ == "__main__":
    main()