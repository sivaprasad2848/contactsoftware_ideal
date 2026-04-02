contact=[]
y=0
while y==0:
    print("Menu")
    print("1->For insert new contact")
    print("2->For Display contact")
    opt=int(input("Enter Your Option"))
    if(opt==1):
        name=input("Enter Name")
        email=input("Enter Email")
        mobile=input("Enter Mobile")
        contact.append((name,email,mobile))
    if(opt==2):
        print(contact)
    y=int(input("Do you want to continue?Press 0 for yes"))

