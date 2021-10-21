#Ek function define karo jo ki input me 2 strings lega aur dono strings me se 
# jiski length jyaada hogi use print karega aur agar dono strings ki length equal 
# hui to dono ko line by line print karega . Hint :- use len() builtin function.
def strings_fun(str1,str2):
    if len(str1)>len(str2):
        print(str1,len(str1))
    elif len(str2)>len(str1):
        print(str2,len(str2))
    else:
        print(str1,"and",str2,"are equal")
strings_fun("piyasha","piya")