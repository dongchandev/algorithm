keyboard_1=['`','1','2','3','4','5','6','7','8','9','0','-','=']
keyboard_2=['Q','W','E','R','T','Y','U','I','O','P','[',']','\\']
keyboard_3=['A','S','D','F','G','H','J','K','L',';','\'']
keyboard_4=['Z','X','C','V','B','N','M',',','.','/']
while 1:
    try:
        s=input()
        if s=='':
            break
        for i in s:
            if i==' ':
                print(' ',end='')
            if i in keyboard_1:
                print(keyboard_1[keyboard_1.index(i)-1],end='')
            elif i in keyboard_2:
                print(keyboard_2[keyboard_2.index(i)-1],end='')
            elif i in keyboard_3:
                print(keyboard_3[keyboard_3.index(i)-1],end='')
            elif i in keyboard_4:
                print(keyboard_4[keyboard_4.index(i)-1],end='')
        print()
    except:
        break