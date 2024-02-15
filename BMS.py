import tkinter as tk
from tkinter import messagebox
from time import gmtime, strftime


def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0

def check_acc_nmb(num):
	try:
		fpin=open(num+".txt",'r')
	except FileNotFoundError:
		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
		return 0
	fpin.close()
	return 

def home_return(master):
	master.destroy()
	Main_Menu()

def write(master,name,oc,pin):
	
	if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0)or name==""):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	f1=open("Accnt_Record.txt",'r')
	accnt_no=int(f1.readline())
	accnt_no+=1
	f1.close()

	f1=open("Accnt_Record.txt",'w')
	f1.write(str(accnt_no))
	f1.close()

	fdet=open(str(accnt_no)+".txt","w")
	fdet.write(pin+"\n")
	fdet.write(oc+"\n")
	fdet.write(str(accnt_no)+"\n")
	fdet.write(name+"\n")
	fdet.close()

	frec=open(str(accnt_no)+"-rec.txt",'w')
	frec.write("Date                             Credit      Debit     Balance\n")
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+oc+"              "+oc+"\n")
	frec.close()
	
	messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
	master.destroy()
	return


def disp_bal(accnt):
	fdet=open(accnt+".txt",'r')
	fdet.readline()
	bal=fdet.readline()
	fdet.close()
	messagebox.showinfo("Balance",bal)


def disp_tr_hist(accnt):
	disp_wn=tk.Tk()
	disp_wn.geometry("900x600")
	disp_wn.title("Transaction History")
	disp_wn.configure(bg="SteelBlue1")
	fr1=tk.Frame(disp_wn,bg="blue")
	l_title=tk.Message(disp_wn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))
	l_title.pack(side="top")
	fr1=tk.Frame(disp_wn)
	fr1.pack(side="top")
	l1=tk.Message(disp_wn,text="Your Transaction History:",font=("Times",16),padx=100,pady=20,width=1000,bg="blue4",fg="SteelBlue1",relief="raised")
	l1.pack(side="top")
	fr2=tk.Frame(disp_wn)
	fr2.pack(side="top")
	frec=open(accnt+"-rec.txt",'r')
	for line in frec:
		l=tk.Message(disp_wn,anchor="w",text=line,relief="raised",width=2000)
		l.pack(side="top")
	b=tk.Button(disp_wn,text="Quit",relief="raised",command=disp_wn.destroy)
	b.pack(side="top")
	frec.close()

def logged_in_menu(accnt,name):
	rootwn=tk.Tk()
	rootwn.geometry("1600x500")
	rootwn.title("Welcome - "+name)
	rootwn.configure(background='SteelBlue1')
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	l_title=tk.Message(rootwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))
	l_title.pack(side="top")
	label=tk.Label(text="Logged in as: "+name,relief="raised",bg="blue3",font=("Times",16),fg="white",anchor="center",justify="center")
	label.pack(side="top")
	img2=tk.PhotoImage(file="credit.gif")
	img3=tk.PhotoImage(file="debit.gif")
	img4=tk.PhotoImage(file="balance1.gif")
	img5=tk.PhotoImage(file="transaction.gif")
	img6=tk.PhotoImage(file="logout.gif")

	myimg2=img2.subsample(2,2)
	myimg3=img3.subsample(2,2)
	myimg4=img4.subsample(2,2)
	myimg5=img5.subsample(2,2)
	myimg6=img6.subsample(2,2)

	b2=tk.Button(image=myimg2)
	b3=tk.Button(image=myimg3)
	b4=tk.Button(image=myimg4)
	b5=tk.Button(image=myimg5,command=lambda: disp_tr_hist(accnt))
	b6=tk.Button(image=myimg6,relief="raised",command=lambda: logout(rootwn))

	b2.image=myimg2
	b3.image=myimg3
	b4.image=myimg4
	b5.image=myimg5
	b6.image=myimg6

	
	b2.place(x=100,y=150)
	b3.place(x=100,y=220)
	b4.place(x=900,y=150)
	b5.place(x=900,y=220)
	b6.place(x=500,y=400)

	
def logout(master):
	
	messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
	master.destroy()
	Main_Menu()

def check_log_in(master,name,acc_num,pin):
	if(check_acc_nmb(acc_num)==0):
		master.destroy()
		Main_Menu()
		return

	if( (is_number(name))  or (is_number(pin)==0) ):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		Main_Menu()
	else:
		master.destroy()
		logged_in_menu(acc_num,name)


def log_in(master):
	master.destroy()
	loginwn=tk.Tk()
	loginwn.geometry("600x300")
	loginwn.title("Log in")
	loginwn.configure(bg="SteelBlue1")
	fr1=tk.Frame(loginwn,bg="blue")
	l_title=tk.Message(loginwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(loginwn,text="Enter Name:",font=("Times",16),relief="raised")
	l1.pack(side="top")
	e1=tk.Entry(loginwn)
	e1.pack(side="top")
	l2=tk.Label(loginwn,text="Enter account number:",font=("Times",16),relief="raised")
	l2.pack(side="top")
	e2=tk.Entry(loginwn)
	e2.pack(side="top")
	l3=tk.Label(loginwn,text="Enter your PIN:",font=("Times",16),relief="raised")
	l3.pack(side="top")
	e3=tk.Entry(loginwn,show="*")
	e3.pack(side="top")
	b=tk.Button(loginwn,text="Submit",command=lambda: check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	b.pack(side="top")
	b1=tk.Button(text="HOME",font=("Times",16),relief="raised",bg="blue4",fg="white",command=lambda: home_return(loginwn))
	b1.pack(side="top")
	loginwn.bind("<Return>",lambda x:check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	

def Create():
	
	crwn=tk.Tk()
	crwn.geometry("600x300")
	crwn.title("Create Account")
	crwn.configure(bg="SteelBlue1")
	fr1=tk.Frame(crwn,bg="blue")
	l_title=tk.Message(crwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(crwn,text="Enter Name:",font=("Times",16),relief="raised")
	l1.pack(side="top")
	e1=tk.Entry(crwn)
	e1.pack(side="top")
	l2=tk.Label(crwn,text="Enter opening credit:",font=("Times",16),relief="raised")
	l2.pack(side="top")
	e2=tk.Entry(crwn)
	e2.pack(side="top")
	l3=tk.Label(crwn,text="Enter desired PIN:",font=("Times",16),relief="raised")
	l3.pack(side="top")
	e3=tk.Entry(crwn,show="*")
	e3.pack(side="top")
	b=tk.Button(crwn,text="Submit",font=("Times",16),command=lambda: write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	b.pack(side="top")
	crwn.bind("<Return>",font=("Times",16),command=lambda x:write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	return


def Main_Menu():
	rootwn=tk.Tk()
	rootwn.geometry("1600x500")
	rootwn.title("Bank Management System")
	rootwn.configure(background='SteelBlue1')
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	l_title=tk.Message(text="BANK MANAGEMENT SYSTEM ",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Verdana","40","bold"))
	l_title.pack(side="top")
	imgc1=tk.PhotoImage(file="new.gif")
	imglo=tk.PhotoImage(file="login.gif")
	img6=tk.PhotoImage(file="quit.gif")
	
	imgc=imgc1.subsample(2,2)
	imglog=imglo.subsample(2,2)
	myimg6=img6.subsample(2,2)

	b1=tk.Button(image=imgc,command=Create)
	b2=tk.Button(image=imglog,command=lambda: log_in(rootwn))
	b6=tk.Button(image=myimg6,command=rootwn.destroy)

	b1.image=imgc
	b2.image=imglog
	b6.image=myimg6
	
	b1.place(x=800,y=300)
	b2.place(x=800,y=200)	
	b6.place(x=920,y=400)

	rootwn.mainloop()

Main_Menu()