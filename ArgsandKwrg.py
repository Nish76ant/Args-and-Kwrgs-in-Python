#Args and Kwrgs

# def function1_name_print(a,b,c,d,e):
#     print(a,b,c,d)


def funargs(normal,*args,**Kwargs):
    # print(type(args))
    # print(args[0])
    print(normal)
    for item in args:
        print(item)
    print('\nNow i would like to introduce some of our heroes') 
    for key,value in Kwargs.items():
        print(f'{key} is a {value}') 

#function1_name_print('Harry','Rohan','Skillf','Hammad','Shivam')

har = ['Harry','Rohan','Skillf','Hammad','Shivam','The Programmer']
normal = 'I am a normal arguement and the students are'
kw = {'Rohan':'Monitor','Harry':'Fitness Instructor','Programmer':'Cordinator','Shivam':'Cooker'}
funargs(normal, *har, **kw)


