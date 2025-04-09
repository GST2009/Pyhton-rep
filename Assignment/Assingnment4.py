# TASK 1
try:
    with open("sample.txt") as file:
        file1 = open("sample.txt", 'r')
        read = file1.readline()
        read2 = file1.readline()
        print("Reading the contents of the file: ")
        print("line 1:", read)
        print("line 2:", read2)
except FileNotFoundError:
    print("Error: 'sample.txt' not found.")

# TASK 2
file1=open("output.txt", 'r+')
Write=input('Enter text to write to the file: ')
file1.write(Write)
file1.close()
print('Data successfully written to output.txt')
file1=open("output.txt", 'a')
Write2=input('Enter additional text to append: ')
file1.write(Write2)
print("final content of output.txt:")
file1=open("output.txt", 'r')
Read=file1.read()
[print(Read)]
file1.close()