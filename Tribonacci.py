import py7zr

def tribonacci(n) :
    trib = []

    if (n < 1) :
        return
  
    first = 0
    second = 0
    third = 1
 
    trib.append(str(first))
    if (n > 1) :
      trib.append(str(second))
    if (n > 2) :
      trib.append(str(second))

    for i in range(3, n) :
        curr = first + second + third
        first = second
        second = third
        third = curr
 
        trib.append(str(curr))

    return ','.join(trib)
     

trib = tribonacci(10000)

num = "10"
fh = open(f"Tribonacci_{num}k.txt","w")
fh.write(trib)
fh.close()

with py7zr.SevenZipFile(f'Tribonacci_{num}k.7z', 'w') as archive:
    archive.write(f'Tribonacci_{num}k.txt')
