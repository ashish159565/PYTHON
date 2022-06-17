from itertools import tee
from tkinter import *
from tkinter.ttk import *
import mysql.connector
import webbrowser
mydb = mysql.connector.connect(host="localhost",user="root",password="Z/NL3ivh#7KA",database="java")
mycursor = mydb.cursor()

main = Tk()
width = main.winfo_screenwidth()
height = main.winfo_screenheight()
main.geometry("%dx%d" % (width,height))
main.state('zoomed')
main.title("J.A.V.A. Pilot")
#main.configure(bg='#ffffff')
icon = PhotoImage(file='Icon.png')
main.iconphoto(False,icon)


t_var = StringVar()

def callback(url):
       webbrowser.open_new_tab(url)
       
def research():
    
    main.destroy()
    b = Tk()
    def back1():
        b.destroy()
        import main
            
    b.geometry("%dx%d" % (width,height))
    b.state('zoomed')
    b.title("Results")
    icon = PhotoImage(file='Icon.png')
    b.iconphoto(False,icon)

    Label(b,text="Trending Research Papers",font=("Rockwell",30)).pack(anchor=CENTER)
    
    R_List = [("Research Paper 1"),("Research Paper 2"),("Research Paper 3")]
    for index,item in enumerate(R_List):
        Label(b,text=f'{item}',font=("Rockwell",15)).pack(pady=index+10,anchor=CENTER)

    Button(b,text="Back",command=back1).pack()
    b.mainloop()

def projects():
    
    main.destroy()
    c = Tk()
    def back2():
        c.destroy()
        import main
            
    c.geometry("%dx%d" % (width,height))
    c.state('zoomed')
    c.title("Results")
    icon = PhotoImage(file='Icon.png')
    c.iconphoto(False,icon)

    Label(c,text="New Projects",font=("Rockwell",30)).pack(anchor=CENTER)
    
    R_List = [("Project Report 1"),("Project Report 2"),("Project Report 3")]
    for index,item in enumerate(R_List):
        Label(c,text=f'{item}',font=("Rockwell",15)).pack(pady=index+10,anchor=CENTER)

    Button(c,text="Back",command=back2).pack()
    c.mainloop()

def b_level():
    data = t_var.get()
    if(data == "python"):
        main.destroy()
        b = Tk()
        def back1():
            b.destroy()
            import main

        b.geometry("%dx%d" % (width,height))
        b.state('zoomed')
        b.title("Results")
        icon = PhotoImage(file='Icon.png')
        b.iconphoto(False,icon)

        Label(b,text="Python For Beginners Level",font=("Rockwell",40)).pack()
        mycursor.execute("select * from data2 where id = 1")
        R_List = mycursor.fetchall()
        for index,item in enumerate(R_List):
            a = list(item)
            a[1] = "https://www.youtube.com/watch?v="+a[1]
            Label(b,text=f'VIDEO LINK : {a[1]}\nCHANNEL TITLE : {a[2]}\nVIDEO TITLE : {a[3]}\n',font=("Rockwell",15)).pack(pady=index+10)
            
        Button(b,text="Back",command=back1).pack()
        b.mainloop()
        
    elif(data == "java"):
        main.destroy()
        b = Tk()
        def back1():
            b.destroy()
            import main

        b.geometry("%dx%d" % (width,height))
        b.state('zoomed')
        b.title("Results")
        icon = PhotoImage(file='Icon.png')
        b.iconphoto(False,icon)

        Label(b,text="Java For Beginners Level",font=("Rockwell",40)).pack()
        
        mycursor.execute("select * from data2 where id = 4")
        R_List = mycursor.fetchall()
        
        for index,item in enumerate(R_List):
            a = list(item)
            a[1] = "https://www.youtube.com/watch?v="+a[1]
            Label(b,text=f'VIDEO LINK : {a[1]}\nCHANNEL TITLE : {a[2]}\nVIDEO TITLE : {a[3]}\n',font=("Rockwell",15)).pack(pady=index+10)
            
        Button(b,text="Back",command=back1).pack()
        b.mainloop()
        
    else:
        main.destroy()
        b = Tk()
        def back1():
            b.destroy()
            import main

        b.geometry("%dx%d" % (width,height))
        b.state('zoomed')
        b.title("Results")
        icon = PhotoImage(file='Icon.png')
        b.iconphoto(False,icon)

        Label(b,text="Resources Related To The Search "+"'"+data+"' For Beginners Level",font=("Rockwell",40)).pack()
        
        R_List = [("Resource 1"),("Resource 2"),("Resource 3")]
        for index,item in enumerate(R_List):
            Label(b,text=f'{item}',font=("Rockwell",15)).pack(pady=index+10)
            
        Button(b,text="Back",command=back1).pack()
        b.mainloop()

def i_level():
    data = t_var.get()
    if(data == "python"):
        main.destroy()
        b = Tk()
        def back1():
            b.destroy()
            import main

        b.geometry("%dx%d" % (width,height))
        b.state('zoomed')
        b.title("Results")
        icon = PhotoImage(file='Icon.png')
        b.iconphoto(False,icon)

        Label(b,text="Python For Intermediate Level",font=("Rockwell",40)).pack()
        
        mycursor.execute("select * from data2 where id = 2")
        R_List = mycursor.fetchall()
        
        for index,item in enumerate(R_List):
            a = list(item)
            a[1] = "https://www.youtube.com/watch?v="+a[1]
            Label(b,text=f'VIDEO LINK : {a[1]}\nCHANNEL TITLE : {a[2]}\nVIDEO TITLE : {a[3]}\n',font=("Rockwell",15)).pack(pady=index+10)
            
        Button(b,text="Back",command=back1).pack()
        b.mainloop()
        
    else:
        main.destroy()
        b = Tk()
        def back1():
            b.destroy()
            import main

        b.geometry("%dx%d" % (width,height))
        b.state('zoomed')
        b.title("Results")
        icon = PhotoImage(file='Icon.png')
        b.iconphoto(False,icon)

        Label(b,text="Resources Related To The Search "+"'"+data+"' For Intermediate Level",font=("Rockwell",40)).pack()
        R_List = [("Resource 1"),("Resource 2"),("Resource 3")]

        for index,item in enumerate(R_List):
            Label(b,text=f'{item}',font=("Rockwell",15)).pack(pady=index+10)
        Button(b,text="Back",command=back1).pack()
        b.mainloop()
        
def p_level():
    data = t_var.get()
    if(data=="java"):
        main.destroy()
        b = Tk()
        def back1():
            b.destroy()
            import main
                
        b.geometry("%dx%d" % (width,height))
        b.state('zoomed')
        b.title("Results")
        icon = PhotoImage(file='Icon.png')
        b.iconphoto(False,icon)

        Label(b,text="Java For Profressional Level",font=("Rockwell",40)).pack()
        
        mycursor.execute("select * from data2 where id = 5")
        R_List = mycursor.fetchall()
        
        for index,item in enumerate(R_List):
            a = list(item)
            a[1] = "https://www.youtube.com/watch?v="+a[1]
            Label(b,text=f'VIDEO LINK : {a[1]}\nCHANNEL TITLE : {a[2]}\nVIDEO TITLE : {a[3]}\n',font=("Rockwell",15)).pack(pady=index+10)
            
        Button(b,text="Back",command=back1).pack()
        b.mainloop()
        
    elif(data=="python"):
        main.destroy()
        b = Tk()
        def back1():
            b.destroy()
            import main
                
        b.geometry("%dx%d" % (width,height))
        b.state('zoomed')
        b.title("Results")
        icon = PhotoImage(file='Icon.png')
        b.iconphoto(False,icon)

        Label(b,text="Python For Profressional Level",font=("Rockwell",40)).pack()
        
        mycursor.execute("select * from data2 where id = 3")
        R_List = mycursor.fetchall()
        
        for index,item in enumerate(R_List):
            a = list(item)
            a[1] = "https://www.youtube.com/watch?v="+a[1]
            Label(b,text=f'VIDEO LINK : {a[1]}\nCHANNEL TITLE : {a[2]}\nVIDEO TITLE : {a[3]}\n',font=("Rockwell",15)).pack(pady=index+10)
        
        Button(b,text="Back",command=back1).pack()
        b.mainloop()
        
    else:
        main.destroy()
        b = Tk()
        def back1():
            b.destroy()
            import main
                
        b.geometry("%dx%d" % (width,height))
        b.state('zoomed')
        b.title("Results")
        icon = PhotoImage(file='Icon.png')
        b.iconphoto(False,icon)

        Label(b,text="Java For Profressional Level",font=("Rockwell",40)).pack()
        
        R_List = [("Resource 1"),("Resource 2"),("Resource 3")]
        for index,item in enumerate(R_List):
            Label(b,text=f'{item}',font=("Rockwell",15)).pack(pady=index+10)
            
        Button(b,text="Back",command=back1).pack()
        b.mainloop()

canvas = Canvas(main, width = 220, height = 220)
canvas.place(relx = 0.5,rely=0.15,anchor=CENTER)
img = PhotoImage(file="Logo1.png")
canvas.create_image(20,20, anchor=NW, image=img)
t1 = Label(main,text="J.A.V.A. Pilot",font=("Rockwell",80)).place(relx = 0.5,rely=0.35,anchor=CENTER)
lbl1=Label(main,text = "Enter Keyword To Search",font = ("Rockwell",20)).place(relx=0.5,rely=0.44,anchor=CENTER)
ebox=Entry(main, width=50,textvariable=t_var).place(anchor=CENTER,relx=0.5,rely=0.5)

v=StringVar(main,"1")

Label(main,text="Select Level of Learning",font = ("Rockwell",15)).place(anchor=CENTER,relx=0.5,rely=0.55)
data = t_var.get()
data.lower()
    
level_1 = Radiobutton(main, text = "Beginner Level",value = "1",variable=v,command=b_level).place(anchor=CENTER,relx=0.2,rely=0.6)
level_2 = Radiobutton(main, text = "Intermediate Level",value = "2",variable=v,command=i_level).place(anchor=CENTER,relx=0.5,rely=0.6)
level_3 = Radiobutton(main, text = "Profressional Level",value = "3",variable=v,command=p_level).place(anchor=CENTER,relx=0.8,rely=0.6)

Button(main,text="Trending Research Papers",command=research).place(anchor=CENTER,relx=0.5,rely=0.7)

Button(main,text="Recent Updated Projects",command=projects).place(anchor=CENTER,relx=0.5,rely=0.8)

Label(main,text="Contact Us",font = ("Rockwell",15)).place(anchor=CENTER,relx=0.5,rely=0.9)
Button(main,text="Help").place(relx=0.05,rely=0.95)
Button(main,text="Instagram").place(relx=0.25,rely=0.95)
Button(main,text="LinkedIn").place(relx=0.45,rely=0.95)
Button(main,text="Twitter").place(relx=0.65,rely=0.95)
Button(main,text="Email").place(relx=0.85,rely=0.95)

main.mainloop()