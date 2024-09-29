def shifter(message,shift):
    output=''
    for i in range(len(message)):
        char=message[i]
        letter = ord(char)
        if letter > 64 and letter <91 or letter>96 and letter<123:    #A-Z and a-z
            letter+=shift
            if letter >=91 and letter <=96:
                letter+=6
            elif letter>=123:
                letter+=-58
            output += chr(letter)
        
        
        else:

            output += chr(letter)
    return output

with open('cipher_text.txt','r') as key:               #this is where we read the key file
    message=key.read()

with open ('possible_plaintext.txt','w') as output:    #this is where we create/write to our output file
    
    for i in range(0, 26):                             #this is for every letter of the alphabet
        text=shifter(message,i)
        output.write(text)
        output.write('\n')
