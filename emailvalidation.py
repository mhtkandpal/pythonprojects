email=input("enter your email :")
k,j,d=0,0,0
#g@mail.com
if len(email)>=6:  # should not be less than 6
    if email[0].isalpha():  #should be alphabet
        if "@" in (email) and (email.count("@")==1): #
            if (email[-4]==".")^(email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("wrong email")
            else:
                print("wrong email 4")
        else:
            print("wrong email 3")
    else:
        print("wrong email 2")
else:
    print("wrong Email 1")