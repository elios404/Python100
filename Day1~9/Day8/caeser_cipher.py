#알파벳은 대문자는 아스키코드 65 부터 90까지 소문자는 아스키코드 97부터 122까지이다.
#문자 -> 아스키코드 숫자 : ord() || 아스키코드 숫자 -> 문자 : chr()

from image import logo

print(logo)
program_on = True

while program_on:
    which_type = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    while which_type != 'encode' and which_type != "decode":
        which_type = input("Wrong input! Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    message = input("Type your message: ")
    shift = int(input("Type the shift number: "))

    if which_type == 'encode':
        encrypted_message = ''
        for l in message:
            l_num = ord(l)
            if l_num >= 65 and l_num <= 90: #Upper letter
                l_num += shift
                if l_num > 90 :
                    cal = (l_num-90)%25
                    l_num = 64+cal
                encrypted_message += chr(l_num)
            elif l_num >= 97 and l_num <= 122: #loewr letter
                l_num += shift
                if l_num > 122:
                    cal = (l_num-122)%25
                    l_num = 96+cal
                encrypted_message += chr(l_num)
            else: #not alphabet
                encrypted_message += chr(l_num)
        print(encrypted_message)

    elif which_type == 'decode':
        decrypted_message = ''
        for l in message:
            l_num = ord(l)
            if l_num >= 65 and l_num <= 90: #Upper letter
                l_num -= shift
                if l_num < 65 :
                    cal = (65-l_num)%25
                    l_num = 91-cal
                decrypted_message += chr(l_num)
            elif l_num >= 97 and l_num <= 122: #loewr letter
                l_num -= shift
                if l_num < 97:
                    cal = (97-l_num)%25
                    l_num = 123-cal
                decrypted_message += chr(l_num)
            else: #not alphabet
                decrypted_message += chr(l_num)
        print(decrypted_message)

    end_loop = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    while end_loop != "yes" and end_loop != "no":
        print("Wrong input!")
        end_loop = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if end_loop == 'yes':
        program_on = True
    elif end_loop == 'no':
        program_on = False
        print("Good Bye!")
