try:
    with open("sample.txt","r") as fh:
        res=fh.readline()
        res1=fh.readline()
except FileNotFoundError:
    print("The file sample.txt was not found")   
else:
    print(f'Line1:{res}')
    print(f'Line2:{res1}')         
