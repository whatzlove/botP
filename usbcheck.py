def usbc(n):
	stop = 0
	j = 0
	file = open('ListUseUSB.txt')
	for word in file:
		name = word.split('	')
		LastArray =  len(name) - 1
	
	while j <= LastArray:
        if n == name[j]:
            print('Use USB and CD-ROM')
            print('j = ',j)
            j = LastArray
            stop = 1              
        else:
            j += 1
if stop == 0 :
    print('Block USB and CD-ROM')

