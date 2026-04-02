contact=[]
y=0
while y==0:
    print("Menu")
    print("1->For insert new contact")
    print("2->For Display contact")
    print("3->For Delete Contact")
    print("4->For Update")
    opt=int(input("Enter Your Option"))
    if(opt==1):
        name=input("Enter Name")
        email=input("Enter Email")
        mobile=input("Enter Mobile")
        contact.append((name,email,mobile))
    if(opt==2):
        print(contact)
    if(opt==3):
        i=int(input("Enter the index you want to remove"))
        contact.pop(i)
    if(opt==4):
        i=int(input("Enter the index you want to update"))
        name=input("Enter Name")
        email=input("Enter Email")
        mobile=input("Enter Mobile")
        contact[i]=(name,email,mobile)
    y=int(input("Do you want to continue?Press 0 for yes"))

