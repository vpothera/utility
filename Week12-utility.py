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

def Union(list_one, list_two):
    union_list=[]
    list_one=list_one.split(" ")
    list_two=list_two.split(" ")
    for i in list_one:
        if i not in list_two:
            union_list.append(i)
    for i in list_two:
        if i not in list_one:
            union_list.append(i)
    for i in union_list:
        if i==' ':
            union_list.remove(i)
    print ('OUTPUT', union_list)
user_list_one=input('Enter the first list:')
user_list_two=input('Enter the second list:')
Union(user_list_one, user_list_two)

def Intersection (list_one, list_two):
    out_list=[]
    list_one=list_one.split(" ")
    list_two=list_two.split(" ")
    for i in list_one:
        if i in list_two:
            out_list.append(i)
    print ('OUTPUT', out_list)
user_list1=input('Enter the first list:')
user_list2=input('Enter the second list:')
Intersection (user_list1, user_list2)
