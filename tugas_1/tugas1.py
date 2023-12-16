#habis dibagi 2, Fizz
#habis dibagi 3, Buzz
#habis dibagi 2 dan 3, FizzBuzz
#20
batas = int(input('masukkan angka batas:'))
for i in range(batas):
    hasil = ''
    Fizz = (i + 1) % 2 == 0
    Buzz = (i + 1) % 3 == 0
    
    if Fizz:
        hasil += 'Fizz'

    if Buzz:
        hasil += 'Buzz'
    
    print('{} -> {}'.format(i + 1, hasil))