from Tkinter import *
root=Tk()

def Add_Record():
    f=open('ekta.txt','a')
    DATE=s2.get()
    WATCH_ID=s1.get()
    CUSTOMER_NAME=s3.get()
    PHONE_NUM=s4.get()
    STORE=s5.get()
    TIME_AT_IN=s6.get()
    TIME_AT_OUT=s7.get()
    ARTICLES=s8.get()
    f.writelines(WATCH_ID.ljust(20)+DATE.ljust(20)+CUSTOMER_NAME.ljust(20)+PHONE_NUM.ljust(20)+STORE.ljust(20)+TIME_AT_IN.ljust(20)+TIME_AT_OUT.ljust(20)+ARTICLES.ljust(20)+"\n")
    print("Record added to file!")
    f.close()
    
def get_first():
    f=open("ekta.txt",'r')
    k=f.readlines()[0]
    j=k.split()
    print(j)
    s1.set(j[0])
    s2.set(j[1]) 
    s3.set(j[2]) 
    s4.set(j[3]) 
    s5.set(j[4]) 
    s6.set(j[5])
    s7.set(j[6])
    s8.set(j[7])
    f.close()

def get_last():
    f=open("ekta.txt",'r')
    ctr= sum(1 for line in open("ekta.txt"))-1
    print(ctr)
    k=f.readlines()[ctr]
    j=k.split()
    print(j)
    s1.set(j[0])
    s2.set(j[1]) 
    s3.set(j[2]) 
    s4.set(j[3]) 
    s5.set(j[4]) 
    s6.set(j[5])
    s7.set(j[6])
    s8.set(j[7])
    f.close()
c=0

def get_next():
    global c
    f=open("ekta.txt",'r')
    ctr= sum(1 for line in open("ekta.txt"))-1
    print(ctr)
    k=f.readlines()[c]
    j=k.split()
    print(j)
    s1.set(j[0])
    s2.set(j[1]) 
    s3.set(j[2]) 
    s4.set(j[3]) 
    s5.set(j[4]) 
    s6.set(j[5])
    s7.set(j[6])
    s8.set(j[7])
    c=c+1
    if(c==ctr+1):
        c=0
    f.close()


c1=0
def get_previous():
    global c1
    f=open("ekta.txt",'r')
    ctr= sum(1 for line in open("ekta.txt"))-1
    print(ctr)
    k=f.readlines()[c1]
    j=k.split()
    print(j)
    s1.set(j[0])
    s2.set(j[1]) 
    s3.set(j[2]) 
    s4.set(j[3]) 
    s5.set(j[4]) 
    s6.set(j[5])
    s7.set(j[6])
    s8.set(j[7])
    c1=c1-1
    if(c1==-1):
        c1=ctr
    f.close()


    
def SEARCH():
    k=s1.get()
    f=open('ekta.txt','r')
    h=f.readlines() 
    for i in h: 
        j=i.split() 
        if(j[0]==k): 
            print("WATCH found")  
            print(j)
            s1.set(j[0])
            s2.set(j[1]) 
            s3.set(j[2]) 
            s4.set(j[3]) 
            s5.set(j[4]) 
            s6.set(j[5])
            s7.set(j[6])
            s8.set(j[7])

             
    f.close()        


def update():

    x1=s1.get()
    x2=s2.get()
    x3=s3.get()
    x4=s4.get()
    x5=s5.get()
    x6=s6.get()
    x7=s7.get()
    x8=s8.get()
    f=open("ekta.txt",'r')
    k=f.readlines()
    f.close()
    f=open("ekta.txt",'w')
    z=0
    for i in k:
        j=i.split()
        if(j[0]!=x1):
            f.writelines(j[0].ljust(20)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(20)+j[5].ljust(20)+j[6].ljust(20)+j[7].ljust(20)+"\n")
            
            
        else:
            f.writelines(x1.ljust(20)+x2.ljust(20)+x3.ljust(20)+x4.ljust(20)+x5.ljust(20)+x6.ljust(20)+x7.ljust(20)+x8.ljust(20)+"\n")
            z=1
            s9.set("Successfully updated")

    if(z==0):
        s9.set("Cannot be updated")
            
    
    
def clear():
     s1.set("")
     s2.set("") 
     s3.set("") 
     s4.set("") 
     s5.set("") 
     s6.set("")
     s7.set("")
     s8.set("")

        

def delrec(): 
    k=[s1.get(),s2.get(),s3.get(),s4.get(),s5.get(),s6.get(),s7.get(),s8.get()] 
    f=open("ekta.txt","r") 
    lines=f.readlines() 
    print(lines) 
    print(k) 
    f.close() 
    f=open("ekta.txt","w") 
    for i in lines: 
        m=i.split() 
        print(m) 
        if(m!=k): 
             f.writelines(m[0].ljust(20)+m[1].ljust(20)+m[2].ljust(20)+m[3].ljust(20)+m[4].ljust(20)+m[5].ljust(20)+m[6].ljust(20)+m[7].ljust(20)+"\n") 
    f.close() 

    





l1=Label(root,text="WATCHES PORTAL ",font=('Ariel',17),bg="black",fg="white")
l1.grid(row=0,column=1)
l3=Label(root,text="DATE OF PURCHASE",font=('Ariel',15,'bold'),fg="black")
l2=Label(root,text="WATCH ID ",font=('Ariel',15,'bold'),fg="black")
l4=Label(root,text="CUSTOMER NAME ",font=('Ariel',15,'bold'),fg="black")
l5=Label(root,text="PHONE NUMBER",font=('Ariel',15,'bold'),fg="black")
l6=Label(root,text="STORE",font=('Ariel',15,'bold'),fg="black")
l7=Label(root,text="TIME AT IN",font=('Ariel',15,'bold'),fg="black")
l8=Label(root,text="TIME AT OUT",font=('Ariel',15,'bold'),fg="black")
l9=Label(root,text="ARTICLES BOUGHT",font=('Ariel',15,'bold'),fg="black")




l2.grid(row=1,column=0)
l3.grid(row=2,column=0)
l4.grid(row=3,column=0)
l5.grid(row=4,column=0)
l6.grid(row=5,column=0)
l7.grid(row=6,column=0)
l8.grid(row=7,column=0)
l9.grid(row=8,column=0)

s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()
s7=StringVar()
s8=StringVar()
s9=StringVar()






e2=Entry(root,textvariable=s1)
e3=Entry(root,textvariable=s2)
e4=Entry(root,textvariable=s3)
e5=Entry(root,textvariable=s4)
e6=Entry(root,textvariable=s5)
e7=Entry(root,textvariable=s6)
e8=Entry(root,textvariable=s7)
e9=Entry(root,textvariable=s8)
e10=Entry(root,textvariable=s9)



e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
e5.grid(row=4,column=1)
e6.grid(row=5,column=1)
e7.grid(row=6,column=1)
e8.grid(row=7,column=1)
e9.grid(row=8,column=1)
e10.grid(row=10,column=3)

b11=Button(root,text="|<",width=15,bg="RED",font=('Ariel',15,'bold'),command=get_first).grid(row=13, column=0)
b12=Button(root,text="<",width=15,bg="RED",font=('Ariel',15,'bold'),command=get_previous).grid(row=13, column=1)
b13=Button(root,text=">",width=15,bg="RED",font=('Ariel',15,'bold'),command=get_next).grid(row=13, column=2)
b14=Button(root,text=">|",width=15,bg="RED",font=('Ariel',15,'bold'),command=get_last).grid(row=13, column=3)
b15=Button(root,text="clear",width=15,bg="green",font=('Ariel',15,'bold'),command=clear).grid(row=11, column=0)

b1=Button(root,text="ADD",width=15,bg="BLUE",font=('Ariel',15,'bold'),command=Add_Record).grid(row=2, column=3)
b2=Button(root,text="DELETE",width=15,bg="BLUE",font=('Ariel',15,'bold'),command=delrec).grid(row=3, column=3)
b3=Button(root,text="SEARCH",width=15,bg="BLUE",font=('Ariel',15,'bold'),command=SEARCH).grid(row=4, column=3)
b4=Button(root,text="UPDATE",width=15,bg="BLUE",font=('Ariel',15,'bold'),command=update).grid(row=5, column=3)

root.mainloop()


