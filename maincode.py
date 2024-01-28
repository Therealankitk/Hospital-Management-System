from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk,Image
import mysql.connector
webdb=mysql.connector.connect(host="localhost",user="root",password="ankit2005",database="hospital")
cursor=webdb.cursor()

def secn():
   global new
   new=Toplevel(win)
   new.title("AUTHORIZATION!")
   new.geometry("500x300")
   image2=Image.open("C:\Program Files\Sublime Text\LOGIN.png")
   image2=image2.resize((500,300))
   bg2=ImageTk.PhotoImage(image2)
   cv2=Canvas(new,width=500,height=300)
   cv2.grid()
   cv2.create_image(0,0,image=bg2,anchor="nw")
   cv2.create_text(200,50,text = "VERIFY THAT YOU ARE A DEVELOPER",font=("albania 15 bold"))
   '''aut=Label(new,text="Enter User Id",font=("calibri,10")).grid(row=2,column=0)
   cv.l2 = cv.create_window(90, 120, anchor="nw", window=aut)'''
   cv2.create_text(90,120,text = "Enter User Id",font=("albania 15"))
   auten=Entry(new,width=25)
   auten.focus_set()
   cv.en=cv2.create_window(170,110,anchor="nw",window=auten)
   cv2.create_text(90,170,text="Enter Password",font=("albania 15"))
   aupas=Entry(new,width=25)
   aupas.focus_set()
   cven2=cv2.create_window(170,160,anchor="nw",window=aupas)
   disp=cv2.create_text(240,270, text="",font=("courier 22 bold"))
   def passcheck():
      user=auten.get()
      passw=aupas.get()
      if user=="ankitk" and passw=="12345":
         cv2.itemconfig(disp,text="VERIFIED!!")
         thir()
         new.destroy()
      else:
         cv2.itemconfig(disp,text="!WRONG USER ID AND PASSWORD!",fill="red")
   bn=Button(new,text="LOGIN",command=passcheck)
   bnc=cv2.create_window(100,200,anchor="nw",window=bn)
   new.mainloop()

def thir():
   global new
   global thir
   def viwtab():
      tab=Toplevel(thir)
      tab.title("TABLES")
      tab.geometry("750x750")
      treehos=ttk.Treeview(tab)
      treehos['columns']=("HospitalID","Name","Bedcount","PhoneNumber")


      treehos.column("HospitalID",anchor=W,width=120)
      treehos.column("Name", anchor=CENTER, width=80)
      treehos.column("Bedcount", anchor=W, width=120)
      treehos.column("PhoneNumber", anchor=W, width=120)

      treehos.heading("HospitalID", text="HospitalID", anchor=W)
      treehos.heading("Name", text="Name", anchor=CENTER)
      treehos.heading("Bedcount", text="Bedcount", anchor=W)
      treehos.heading("PhoneNumber", text="PhoneNumber", anchor=W)



      cursor.execute("SELECT * FROM hospitals")
      data=cursor.fetchall()
      for x in data:
         treehos.insert(parent='',index='end',values=x)
      treehos.pack()

      treedoc = ttk.Treeview(tab)
      treedoc['columns'] = ("DoctorID", "Name", "HospitalID","Speciality","Salary","Experience")

      treedoc.column("DoctorID", anchor=W, width=120)
      treedoc.column("Name", anchor=CENTER, width=80)
      treedoc.column("HospitalID", anchor=W, width=120)
      treedoc.column("Speciality", anchor=W, width=120)
      treedoc.column("Salary", anchor=W, width=120)
      treedoc.column("Experience", anchor=W, width=120)

      treedoc.heading("DoctorID", text="DoctorID", anchor=W)
      treedoc.heading("Name", text="Name", anchor=CENTER)
      treedoc.heading("HospitalID", text="HospitalID", anchor=W)
      treedoc.heading("Speciality", text="Speciality", anchor=W)
      treedoc.heading("Salary", text="Salary", anchor=W)
      treedoc.heading("Experience", text="Experience", anchor=W)

      cursor.execute("SELECT * FROM doctors")
      data2 = cursor.fetchall()
      for y in data2:
         treedoc.insert(parent='', index='end', values=y)
      treedoc.pack()
      tab.mainloop()
   #def cretab():
   def deleteobjhos():
      cv3.delete(de1)
      cv3.delete(de2)
      cv3.delete(de3)
      cv3.delete(de4)
      cv3.delete(de5)
      cv3.delete(de6)
      cv3.delete(de7)
      doc.destroy()
      doc2.destroy()
      doc3.destroy()
      doc4.destroy()
      doc5.destroy()
      doc6.destroy()
      sav1.destroy()

   def deleteobjdoc():
      cv3.delete(he)
      cv3.delete(he1)
      cv3.delete(he2)
      cv3.delete(he3)
      cv3.delete(he4)
      hosi.destroy()
      hosi2.destroy()
      hosi3.destroy()
      hosi4.destroy()
      sav.destroy()

   def deletecontent():
      try:
         cv3.delete(delcd)
         deled2.destroy()
         deld.destroy()
      except:
         cv3.delete(delch)
         deleh1.destroy()
         delh.destroy()
      else:
         cv3.delete(delch)
         deleh1.destroy()
         delh.destroy()

      finally:
         del1.destroy()
         del2.destroy()
         del3.destroy()
         del4.destroy()

   def deletecons():
      try:
         cv3.delete(de1)
         cv3.delete(de2)
         cv3.delete(de3)
         cv3.delete(de4)
         cv3.delete(de5)
         cv3.delete(de6)
         cv3.delete(de7)
         doc.destroy()
         doc2.destroy()
         doc3.destroy()
         doc4.destroy()
         doc5.destroy()
         doc6.destroy()
         sav1.destroy()
      except:
         cv3.delete(he)
         cv3.delete(he1)
         cv3.delete(he2)
         cv3.delete(he3)
         cv3.delete(he4)
         hosi.destroy()
         hosi2.destroy()
         hosi3.destroy()
         hosi4.destroy()
         sav.destroy()

      else:
         cv3.delete(he)
         cv3.delete(he1)
         cv3.delete(he2)
         cv3.delete(he3)
         cv3.delete(he4)
         hosi.destroy()
         hosi2.destroy()
         hosi3.destroy()
         hosi4.destroy()
         sav.destroy()

      finally:
         ch1.destroy()
         ch2.destroy()
   def hosordoc():
      global ch1,ch2
      ch1 = Button(thir, text="EDIT HOSPITALS", command=lambda :[edithospital(),deleteobjhos()])
      ch2 = Button(thir, text="EDIT DOCTORS", command=lambda :[editdoctor(),deleteobjdoc()])
      ch1c = cv3.create_window(250, 350, anchor="nw", window=ch1)
      ch1c = cv3.create_window(250, 400, anchor="nw", window=ch2)


   def savbtn():
      a=[]
      b=[]
      x,y,z,v=hosi.get(),hosi2.get(),hosi3.get(),hosi4.get()
      a.append(x)
      a.append(y)
      a.append(z)
      a.append(v)
      b.append(tuple(a))
      sql = "INSERT INTO hospitals(hospitalid,hospitalname,waitcount,phonenumber)VALUES(%s,%s, %s,%s)"
      val = b
      cursor.executemany(sql, val)
      webdb.commit()

   def savbtn2():
      h=[]
      k=[]
      u,v,w,s,t,d=doc.get(),doc2.get(),doc3.get(),doc4.get(),doc5.get(),doc6.get()
      h.append(u)
      h.append(v)
      h.append(w)
      h.append(s)
      h.append(t)
      h.append(d)
      k.append(tuple(h))

      por = "INSERT INTO doctors(doctorid,doctorname,hospitalid,speciality,salary,experience)VALUES(%s,%s, %s,%s,%s,%s)"
      que = k
      cursor.executemany(por, que)
      webdb.commit()

   '''cursor.execute("DROP TABLE IF EXISTS doctors")
   cursor.execute("DROP TABLE IF EXISTS hospitals")
   cursor.execute("CREATE TABLE hospitals(hospitalid SMALLINT NOT NULL PRIMARY KEY,hospitalname varchar(255),bedcount int(20))")'''
   def edithospital():
      global hosi,hosi2,hosi3,hosi4,he4,he,he1,he2,he3,sav
      he=cv3.create_text(750,200,text="ENTER HOSPITAL DETAILS:-",fill="black",font=('comicsans',15,'bold'))
      he1=cv3.create_text(800, 250, text="enter hospital id", fill="purple")
      hosi = Entry(thir, width=15)
      hosi.focus_set()
      hosip = cv3.create_window(850, 250, anchor="nw", window=hosi)
      he2=cv3.create_text(800, 300, text="Enter Hospital Name", fill="purple")
      hosi2 = Entry(thir, width=15)
      hosi2.focus_set()
      hosip2 = cv3.create_window(850, 300, anchor="nw", window=hosi2)
      he3=cv3.create_text(800, 350, text="Enter Bed Count", fill="purple")
      hosi3 = Entry(thir, width=15)
      hosi3.focus_set()
      he4 = cv3.create_text(800, 400, text="Enter Phone Number", fill="purple")
      hosi4 = Entry(thir, width=15)
      hosi4.focus_set()
      hosip3 = cv3.create_window(850, 350, anchor="nw", window=hosi3)
      hosip4 = cv3.create_window(850, 400, anchor="nw", window=hosi4)
      sav=Button(thir,text="DONE",style="W.TButton",command=savbtn)
      savc=cv3.create_window(890,450,anchor="nw",window=sav)

   def editdoctor():
      global de1,de2,de3,de4,de5,de6,de7,doc,doc2,doc3,doc4,doc5,doc6,sav1
      de7=cv3.create_text(750,200,text="ENTER DOCTOR DETAILS:-",fill="black",font=("calibri",15,'bold'))
      de6=cv3.create_text(800, 250, text="Enter Doctor Id", fill="purple")
      doc = Entry(thir, width=15)
      doc.focus_set()
      docip = cv3.create_window(850, 250, anchor="nw", window=doc)
      de1=cv3.create_text(800, 300, text="Enter Doctor Name", fill="purple")
      doc2 = Entry(thir, width=15)
      doc2.focus_set()
      docip2 = cv3.create_window(850, 300, anchor="nw", window=doc2)
      de2=cv3.create_text(800, 350, text="Enter Hospital Id", fill="purple")
      doc3 = Entry(thir, width=15)
      doc3.focus_set()
      docip3 = cv3.create_window(850, 350, anchor="nw", window=doc3)
      de3=cv3.create_text(800, 400, text="Enter Speciality", fill="purple")
      doc4 = Entry(thir, width=15)
      doc4.focus_set()
      docip4 = cv3.create_window(850, 400, anchor="nw", window=doc4)
      de4=cv3.create_text(800, 450, text="Enter Fees", fill="purple")
      doc5 = Entry(thir, width=15)
      doc5.focus_set()
      docip5 = cv3.create_window(850, 450, anchor="nw", window=doc5)
      de5=cv3.create_text(800, 500, text="Enter Experience", fill="purple")
      doc6 = Entry(thir, width=15)
      doc6.focus_set()
      docip6 = cv3.create_window(850, 500, anchor="nw", window=doc6)
      sav1 = Button(thir, text="DONE",style="W.TButton", command=savbtn2)
      sav1c = cv3.create_window(890, 550, anchor="nw", window=sav1)
   def delhos():
      a=deleh1.get()
      quer1="DELETE FROM hospitals WHERE hospitalname=%s"
      cursor.execute(quer1, (a,))
      webdb.commit()
   def deldoc():
      b = deled2.get()
      quer2 = "DELETE FROM doctors WHERE doctorname=%s"
      cursor.execute(quer2, (b,))
      webdb.commit()
   def delhostable():
      cursor.execute("DROP TABLE hospitals")
      webdb.commit()
      cursor.execute("CREATE TABLE hospitals(hospitalid SMALLINT NOT NULL PRIMARY KEY,hospitalname varchar(255),bedcount int(20)),phonenumber varchar(10)")
   def deldoctable():
      cursor.execute("DROP TABLE doctors")
      webdb.commit()
      cursor.execute("CREATE TABLE doctors(doctorid int PRIMARY KEY,doctorname varchar(255),hospitalid SMALLINT NOT NULL, FOREIGN KEY(hospitalid) REFERENCES hospitals(hospitalid),speciality varchar(50),salary varchar(50),experience int(4))")


   def warn():
      global change, new2
      new2 = Toplevel(win)
      new2.title("sure?")
      new2.geometry("600x300")
      text = Label(new2, text="YOU SURE YOU WANT TO DELETE THE ENTIRE TABLE", font=("calibri 20")).grid(padx=5,
                                                                                                        pady=30)
      change = ttk.Button(new2, text='SURE',style='X.TButton', command=lambda:[delhostable(),new2.destroy()]).grid(row=3, column=0, pady=10, padx=30)
      ttk.Button(new2, text='CANCEL',style='W.TButton', command=new2.destroy).grid(row=4, column=0, pady=10, padx=30)
      new2.mainloop()

   def warn2():
      global change, new2
      new2 = Toplevel(win)
      new2.title("sure?")
      new2.geometry("600x300")
      text = Label(new2, text="YOU SURE YOU WANT TO DELETE THE ENTIRE TABLE", font=("calibri 20")).grid(padx=5,
                                                                                                        pady=30)
      change = ttk.Button(new2, text='SURE',style='X.TButton', command=lambda:[deldoctable(),new2.destroy()]).grid(row=3, column=0, pady=10, padx=30)
      ttk.Button(new2, text='CANCEL',style='W.TButton', command=new2.destroy).grid(row=4, column=0, pady=10, padx=30)
      new2.mainloop()

   def dele1():
      global delch,deleh1,delh
      try:
         cv3.delete(delcd)
         deled2.destroy()
         deld.destroy()
      finally:
         delch=cv3.create_text(850,200 ,text="ENTER NAME OF HOSPITAL YOU WANT TO DELETE",fill="red",font=('comicsans',15))
         deleh1 = Entry(thir, width=15)
         deleh1.focus_set()
         hosdel = cv3.create_window(850, 250, anchor="nw", window=deleh1)
         delh=Button(thir, text="DELETE", command=delhos)
         delhc = cv3.create_window(780, 400, anchor="nw", window=delh)
   def dele2():
      global delcd, deled2, deld
      try:
         cv3.delete(delch)
         deleh1.destroy()
         delh.destroy()

      finally:
         delcd = cv3.create_text(850, 200, text="ENTER NAME OF DOCTOR YOU WANT TO DELETE", fill="red",
                                 font=('comicsans', 15))
         deled2 = Entry(thir, width=15)
         deled2.focus_set()
         docdel = cv3.create_window(850, 250, anchor="nw", window=deled2)
         deld = Button(thir, text="DELETE", command=deldoc)
         deldc = cv3.create_window(780, 400, anchor="nw", window=deld)

   def editab():
      global del1,del2,del3,del4
      del1 = Button(thir, text="DELETE SPECIFIC ENTRY FROM HOSPITALS", command=dele1)
      del1c=cv3.create_window(250, 350, anchor="nw", window=del1)
      del2 = Button(thir, text="DELETE SPECIFIC ENTRY FROM DOCTORS", command=dele2)
      del2c = cv3.create_window(250, 400, anchor="nw", window=del2)
      del3 = Button(thir, text="DELETE HOSPITAL TABLE", command=warn)
      del3c = cv3.create_window(300, 450, anchor="nw", window=del3)
      del4 = Button(thir, text="DELETE DOCTOR TABLE", command=warn2)
      del4c = cv3.create_window(300, 500, anchor="nw", window=del4)




   thir=Toplevel(win)
   thir.title("WELCOME TO DEVELOPERS' SITE")
   thir.geometry("1080x900")
   img2= Image.open("C:\Program Files\Sublime Text\devel.png")
   img2=img2.resize((1080,900))
   bg3=ImageTk.PhotoImage(img2)
   cv3=Canvas(thir,width=1080,height=900)
   cv3.grid()
   cv3.create_image(0,0,image=bg3,anchor="nw")
   cv3.create_text(400,50 ,text="WELCOME TO THE DEVELOPER'S PORTAL",fill="yellow",font=('comicsans',25,'bold'))
   tempbut=Button(thir,text="EXIT",command=win.destroy)
   tempbutc=cv3.create_window(700,100,anchor="ne",window=tempbut)
   cv3.create_text(300, 130, text="What do you want to do?", fill="red", font=('comicsans', 18, 'bold'))
   bt1=Button(thir,text="VIEW EXISTING TABLES",command=viwtab)
   bn1c = cv3.create_window(200, 200, anchor="nw", window=bt1)
   bt2=Button(thir,text="ADD NEW INFORMATION",command=lambda:[hosordoc(),deletecontent()])
   bn2c = cv3.create_window(200, 250, anchor="nw", window=bt2)
   bt3=Button(thir,text="DELETE TABLES",command=lambda:[editab(),deletecons()])
   bn3c = cv3.create_window(200, 300, anchor="nw", window=bt3)


   thir.mainloop()

def thir2():
   global new
   thir2=Toplevel(win)
   thir2.title("WELCOME TO USER'S PORTAL")
   thir2.geometry("850x770")
   img2= Image.open("C:\Program Files\Sublime Text\image2.jpg")
   img2=img2.resize((850,770))
   bg3=ImageTk.PhotoImage(img2)
   cv4=Canvas(thir2,width=1080,height=900)
   cv4.grid()
   cv4.create_image(0,0,image=bg3,anchor="nw")
   sty.configure('TButton2',font=('calibri',10),borderwidth=400)
   sty.map('TButton2',foreground=[('active','!disabled','green')],background = [('active','red')])

   def delobjs1():
      try:
         cv4.delete(hosname3)
         cv4.delete(resname3)
         cv4.delete(hosname4)
         cv4.delete(resname4)
         cv4.delete(hosname5)
         cv4.delete(resname5)
         cv4.delete(hosname6)
         cv4.delete(resname6)
         cv4.delete(hosname7)
         cv4.delete(resname7)
      except:
         try:
            cv4.delete(docname)
            cv4.delete(resdoc)
         except:
            cv4.delete(docname2)
            cv4.delete(resdoc2)
      else:
         cv4.delete(docname2)
         cv4.delete(resdoc2)

      finally:
         try:
            cv4.delete(fetname2)
            name2.destroy()
            find2.destroy()
         except:
            try:
               cv4.delete(fetname3)
               name3.destroy()
               find3.destroy()
            except:
               cv4.delete(fetname4)
               name4.destroy()
               find4.destroy()
         else:
            cv4.delete(fetname4)
            name4.destroy()
            find4.destroy()

   def delobjs2():
      try:
         cv4.delete(hosname)
         cv4.delete(resname)
         cv4.delete(hosname1)
         cv4.delete(resname1)
         cv4.delete(hosname2)
         cv4.delete(resname2)
      except:
         try:
            cv4.delete(docname)
            cv4.delete(resdoc)
         except:
            cv4.delete(docname2)
            cv4.delete(resdoc2)
      finally:
         try:
            cv4.delete(fetname)
            name.destroy()
            find.destroy()
         except:
            try:
               cv4.delete(fetname3)
               name3.destroy()
               find3.destroy()
            except:
               cv4.delete(fetname4)
               name4.destroy()
               find4.destroy()
         else:
            cv4.delete(fetname4)
            name4.destroy()
            find4.destroy()

   def delobjs3():
      try:
         cv4.delete(hosname)
         cv4.delete(resname)
         cv4.delete(hosname1)
         cv4.delete(resname1)
         cv4.delete(hosname2)
         cv4.delete(resname2)
      except:
         try:
            cv4.delete(hosname3)
            cv4.delete(resname3)
            cv4.delete(hosname4)
            cv4.delete(resname4)
            cv4.delete(hosname5)
            cv4.delete(resname5)
            cv4.delete(hosname6)
            cv4.delete(resname6)
            cv4.delete(hosname7)
            cv4.delete(resname7)
         except:
            cv4.delete(docname2)
            cv4.delete(resdoc2)
      else:
         cv4.delete(hosname3)
         cv4.delete(resname3)
         cv4.delete(hosname4)
         cv4.delete(resname4)
         cv4.delete(hosname5)
         cv4.delete(resname5)
         cv4.delete(hosname6)
         cv4.delete(resname6)
         cv4.delete(hosname7)
         cv4.delete(resname7)


      finally:
         try:
            cv4.delete(fetname)
            name.destroy()
            find.destroy()
         except:
            try:
               cv4.delete(fetname2)
               name2.destroy()
               find2.destroy()
            except:
               cv4.delete(fetname4)
               name4.destroy()
               find4.destroy()
         else:
            cv4.delete(fetname2)
            name2.destroy()
            find2.destroy()



   def delobjs4():
      try:
         cv4.delete(hosname)
         cv4.delete(resname)
         cv4.delete(hosname1)
         cv4.delete(resname1)
         cv4.delete(hosname2)
         cv4.delete(resname2)
      except:
         try:
            cv4.delete(hosname3)
            cv4.delete(resname3)
            cv4.delete(hosname4)
            cv4.delete(resname4)
            cv4.delete(hosname5)
            cv4.delete(resname5)
            cv4.delete(hosname6)
            cv4.delete(resname6)
            cv4.delete(hosname7)
            cv4.delete(resname7)
         except:
            cv4.delete(docname)
            cv4.delete(resdoc)
      else:
         cv4.delete(docname)
         cv4.delete(resdoc)

      finally:
         try:
            cv4.delete(fetname)
            name.destroy()
            find.destroy()
         except:
            try:
               cv4.delete(fetname2)
               name2.destroy()
               find2.destroy()
            except:
               cv4.delete(fetname3)
               name3.destroy()
               find3.destroy()
         else:
            cv4.delete(fetname3)
            name3.destroy()
            find3.destroy()






   def res1():
      global hosname,resname,hosname1,resname1,hosname2,resname2
      namh=name.get()
      quenam="SELECT * FROM hospitals WHERE hospitalname=%s"
      cursor.execute(quenam,(namh,))
      hosdit=cursor.fetchall()
      for dete in hosdit:
         hosname=cv4.create_text(400,400,text="hospital id:-")
         resname=cv4.create_text(450,400,text=dete[0])
         hosname1 = cv4.create_text(400, 450, text="hospital name:-")
         resname1 = cv4.create_text(450, 450, text=dete[1])
         hosname2 = cv4.create_text(400, 500, text="bed count:-")
         resname2 = cv4.create_text(450, 500, text=dete[2])
   def res2():
      global hosname3, resname3, hosname4, resname4, hosname5, resname5,hosname6, resname6, hosname7, resname7
      namd = name2.get()
      quenam = "SELECT * FROM doctors WHERE doctorname=%s"
      cursor.execute(quenam, (namd,))
      docdit = cursor.fetchall()
      for dete in docdit:
         hosname3 = cv4.create_text(400, 400, text="doctor id:-",fill="green",font=('courier',13))
         resname3 = cv4.create_text(480, 400, text=dete[0],fill="green",font=('courier',13))
         hosname4 = cv4.create_text(400, 450, text="doctor name:-",fill="green",font=('courier',13))
         resname4 = cv4.create_text(500, 450, text=dete[1],fill="green",font=('courier',13))
         hosname5 = cv4.create_text(400, 500, text="speciality:-",fill="green",font=('courier',13))
         resname5 = cv4.create_text(500, 500, text=dete[3],fill="green",font=('courier',13))
         hosname6 = cv4.create_text(400, 550, text="salary:-",fill="green",font=('courier',13))
         resname6 = cv4.create_text(480, 550, text=dete[4],fill="green",font=('courier',13))
         hosname7 = cv4.create_text(400, 600, text="experience:-",fill="green",font=('courier',13))
         resname7 = cv4.create_text(500, 600, text=str(dete[5])+'years',fill="green",font=('courier',13))
   def res3():
      global docname,resdoc
      namspec=name3.get()
      lis=[]
      queapec="SELECT * FROM doctors WHERE speciality=%s"
      cursor.execute(queapec,(namspec,))
      specil=cursor.fetchall()
      for specs in specil:
         lis.append(specs[1])
      docname=cv4.create_text(400,400, text="Doctor name:-")
      resdoc=cv4.create_text(500,400,text=lis)

   def res4():
      global docname2,resdoc2
      namfac=name4.get()
      falis=[]
      quefac="select doctorname from doctors,hospitals where hospitalname=%s and hospitals.hospitalid=doctors.hospitalid;"
      cursor.execute(quefac,(namfac,))
      facil=cursor.fetchall()
      for facs in facil:
         falis.append(facs[0])
      docname2 = cv4.create_text(400, 400, text="Doctor present:-")
      resdoc2 = cv4.create_text(500, 400, text=falis)




   def findhos():
      global fetname,name,find
      fetname=cv4.create_text(250,200,text="ENTER HOSPITAL NAME:-",fill="blue",font=('comicsans',18))
      name = Entry(thir2, width=15)
      name.focus_set()
      docdel = cv4.create_window(450, 190, anchor="nw", window=name)
      find=Button(thir2, text="FIND",command=lambda:[res1()])
      cv4.create_window(650,190,window=find)

   def findoc():
      global fetname2, name2, find2
      fetname2 = cv4.create_text(250, 200, text="ENTER DOCTOR NAME:-", fill="blue", font=('comicsans', 18))
      name2 = Entry(thir2, width=15)
      name2.focus_set()
      docdel = cv4.create_window(450, 190, anchor="nw", window=name2)
      find2 = Button(thir2, text="FIND", command=lambda:[res2()])
      cv4.create_window(650, 190, window=find2)
   def findspec():
      global fetname3, name3, find3
      fetname3 = cv4.create_text(250, 200, text="ENTER SPECIALITY:-", fill="blue", font=('comicsans', 18))
      name3 = Entry(thir2, width=15)
      name3.focus_set()
      docdel = cv4.create_window(450, 190, anchor="nw", window=name3)
      find3 = Button(thir2, text="FIND", command=lambda:[res3()])
      cv4.create_window(650, 190, window=find3)
   def findfac():
      global fetname4,name4,find4
      fetname4 = cv4.create_text(250, 200, text="ENTER HOSPITAL:-", fill="blue", font=('comicsans', 18))
      name4 = Entry(thir2, width=15)
      name4.focus_set()
      docdel = cv4.create_window(450, 190, anchor="nw", window=name4)
      find4 = Button(thir2, text="FIND", command=lambda:[res4()])
      cv4.create_window(650, 190, window=find4)


   cv4.create_text(300,50 ,text="WELCOME TO THE USER'S PORTAL",fill="yellow",font=('comicsans',25,'bold'))
   r1=Button(thir2, text="SEARCH FOR HOSPITALS",style='Y.TButton',command=lambda:[findhos(),delobjs1()])
   cv4.create_window(120, 130, window=r1)
   r2=Button(thir2, text="SEARCH FOR DOCTORS",style='Y.TButton',command=lambda:[findoc(),delobjs2()])
   cv4.create_window(320, 130, window=r2)
   r3 = Button(thir2, text="SEARCH FOR SPECIALITY",style='Y.TButton',command=lambda:[findspec(),delobjs3()])
   cv4.create_window(523, 130, window=r3)
   r4 = Button(thir2, text="SEARCH FOR FACULTY",style='Y.TButton',command=lambda:[findfac(),delobjs4()])
   cv4.create_window(720, 130, window=r4)
   r5=Button(thir2, text="QUIT",command=win.destroy)
   cv4.create_window(260, 750, window=r5)
   thir2.mainloop()

win= Tk()
win.geometry("750x400")
win.title("Hospital Management")
image = Image.open("C:\Program Files\Sublime Text\image.jpg")
image = image.resize((750, 400))
bg=ImageTk.PhotoImage(image)
cv=Canvas(win,width=750,height=400)
cv.grid(column=0)
cv.create_image( 0, 0, image = bg, anchor = "nw")
cv.create_text( 250, 70, text = "HOSPITAL MANAGEMENT",fill="orange",font=('comic sans', 25))
sty=Style()
sty.configure('TButton',font = ('albania',18),borderwidth = '500')
sty.map('TButton',foreground=[('active','!disabled','blue')],background = [('active','red')])
sty.configure('W.TButton', font =
               ('calibri', 18),
                foreground = 'green')
sty.configure('X.TButton', font =
               ('calibri', 18),
                foreground = 'red')
sty.configure('Y.TButton', font =
               ('calibri', 15),
                foreground = 'violet')


#ttk.Button(win,text="I am an Administator",command=secn).grid(row=0,column=0,padx=10)
#ttk.Button(win,text="I am a Patient",command=next).grid(row=1,column=0,padx=10)

b1=Button(win,text="I am an Administrator",command=thir)#-->change to secn
b1_c=cv.create_window(90,200,anchor="nw",window=b1)
b2=Button(win,text="I am a Patient",command=thir2)
b2_c=cv.create_window(130,250,anchor="nw",window=b2)
win.mainloop()
