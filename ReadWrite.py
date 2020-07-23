"""This program aims to demonstrate the usability of I/O console in python
   1. Create the file using write()
   2. Read the file at once
   3. Append few lines
   4. Read line by line"""

from sys import stdout
def main():
    print('Enter the Filename to read/write : ',end='')
    file=input()
    while True:
        print('1. Create a file\n2. Read entire file at once\n3. Append into file\n4. Read file line-wise')
        print('\nPress any other key to exit\n')
        print('Enter your choice (1/2/3/4/) :',end='')
        ch=input()
        if ch=='1':
            createfile(file)
        elif ch=='2':
            readall(file)
        elif ch=='3':
            appendfile(file)
        elif ch=='4':
            readbyline(file)
        else:
            print('Exit Console prompted')
            break
        print('\n\n!! Back to loop !!\n\n\n\n')

def createfile(file):
    fw=open(file,mode='wt',encoding='utf-8')
    while True :
        print('Enter line you wish to write : ',end='')
        fw.write(input())
        fw.write('\n')
        print('Press "Y" to continue or any other key to finish writing : ',end='')
        nt=input()
        if nt=='Y' or nt=='y':
            continue
        else:
            fw.close()
            break

def readall(file):
    frall=open(file,mode='rt',encoding='utf-8')
    f_list=frall.read()
    print(f_list)
    frall.close()

def appendfile(file):
    fa=open(file,mode='at',encoding='utf-8')
    while True :
        print('Enter line you wish to append : ',end='')
        fa.write(input())
        fa.write('\n')
        print('Press "Y" to continue or any other key to finish writing : ',end='')
        nt=input()
        if nt=='Y' or nt=='y':
            continue
        else:
            fa.close()
            break

def readbyline(file):
    frline=open(file,mode='rt',encoding='utf-8')
    print('\nReading file line by line using file iteration :\n')
    for line in frline:
        stdout.write(line)
    frline.close()

if __name__=='__main__':
    main()