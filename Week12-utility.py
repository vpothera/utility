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

def UpdateString (orig_string, replace_string, index):
    orig_string=list(orig_string)
    orig_string[index]=replace_string
    orig_string=''.join(orig_string)
    print('OUTPUT', orig_string)
user_string=str(input('Enter string:'))
user_string2=str(input('Enter string:'))
user_index=int(input('Enter index:'))
print(f'>>>UpdateString({user_string}, {user_string2}, {user_index})')
UpdateString(user_string, user_string2, user_index)

def FindWordCount(orig_list, orig_string):
    num_total=0
    contents=LoadFile(orig_list)
    for i in range(len(contents)):
        num_line=0
        num_line=contents[i].count(orig_string)
        num_total=num_total+num_line
    print ('OUTPUT', num_total)
user_list=input('Enter file for list:')
user_string=input('Enter string:')
FindWordCount(user_list, user_string)
