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

def ScoreFinder(name_list, score_list, name):
    name_list=name_list.lower()
    name=name.lower()
    name_list=name_list.split(" ")
    score_list=score_list.split(" ")
    if name in name_list:
        index=name_list.index(name)
        print(score_list[index])
    else:
        print ('OUTPUT player not found')
user_names=input('Enter names:')
user_scores=input('Enter scores:')
user_name=input('Enter name to search:')
ScoreFinder(user_names, user_scores, user_name)
