def PrintOutput(input_string):
    print ('OUTPUT', input_string)
user_string=input('Enter a string:')
print(f'>>>PrintOutput({user_string})')
PrintOutput(user_string)

def LoadFile (filename):
    f=open(filename, 'r+')
    contents=f.read()
    contents=contents.split("\n")
    return contents
user_file=input("Enter the file:")
LoadFile(user_file)
