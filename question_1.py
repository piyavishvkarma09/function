def eligible_for_vote(age):
    if age>=18:
        return(age,"you are eligible for voting")
    else:
       return(age,"you are not eligible for voting")
user=int(input("enter the number"))
age=eligible_for_vote(user)
print(age)