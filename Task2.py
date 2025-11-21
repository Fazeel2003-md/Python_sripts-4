text=input("Enter text to write in file : ")
with open('output.txt','w') as fh:
    fh.write(text)
print("Data successfully written in output.txt") 
addition=input("Enter additional text to append : ")
with open('output.txt','a') as fh:
    fh.write(addition)   
print("Data successfully appended") 
with open('output.txt','r') as fh:
    fh.read()
