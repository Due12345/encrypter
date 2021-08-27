import sys


def menu():
    print("************MAIN MENU**************")
    
    print()

    choice = input("""
                      1.Encryption
                      2.Decryption
                      3.Exit

                      Please enter your choice: """)

    if choice == "1" :
        Encription()
    elif choice == "2":
        Decription()
    elif choice == "3":
        sys.exit
    
    else:
        print("You must only select either 1,2 or 3")
        print("Please try again")
        menu()
def Decription():
    elines=read("ciphertext.txt")
    dkey=round(average((read("Enc_key.txt"))[1]))
    
    my_file = open("Decrypted.txt","w+")
    
    my_file.write('{}\n{}\n{}\n'.format(remove(elines[1],dkey)+"\n",remove(elines[2],dkey)+"\n",remove(elines[3],dkey)))
                  
def remove(ciphertext,key):
    result = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]

        if (char.isupper()):
            result += chr((ord(char) - key-65) % 26 + 65)
        if (char.islower()):
            result += chr((ord(char) - key - 97) % 26 + 97)
        else:
            result += chr(ord(char) - key )
    return result
def Encription():
    lines=read("Student_info.txt")
    my_file = open("plaintext.txt","w+")
    my_file.write(lines[1]+lines[2]+lines[3])
    key=list(str(keycreator(lines)))
    averag=round(average(key))
    sdob=lines[1]
    sid=lines[2]
    sname=lines[3]
    esdob=move(sdob,averag)
    esid=move(sid,averag)
    esname=move(sname,averag)
    my_file = open("ciphertext.txt","w+")
    my_file.write(esdob+esid+esname)
    
def move(plaintext,key):
    result = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char=="\n":
            continue
        
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
        if (char.islower()):
            result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result += chr(ord(char) + key )
    return result
def average(key):
        f=len(key)
        z=0
        while f:
            f=f-1
            z=z+int(key[f])
            
        average=z/len(key)
        return average
    
def keycreator(lines):
    sdob=lines[1]
    sid=lines[2]
    sname=lines[3]
    reversedid=sid[::-1]
    Sum=int(reversedid)+int(sdob)
    if not((Sum% len(sname))%2):
        key= int(reversedid) +len(sname)
    else:
        key= len(sname) + int(sdob)
    my_file = open("Enc_key.txt","w+")
    my_file.write(str(key))
    return key


def read(adres):
    k={}
    file=open(adres,"r")
    k[1]=file.readline()
    k[2]=file.readline()
    k[3]=file.readline()
    return k
    
menu()