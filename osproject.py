from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
import tkinter as tk
from tkinter import filedialog
import platform
import psutil

#brightness
import screen_brightness_control as pct

#audio
from ctypes import cast,POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities , IAudioEndpointVolume

#weather
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

#clock
from time import strftime

#calendar
from tkcalendar import *

#open google
import pyautogui

import subprocess
import webbrowser as wb
import random
from PIL import Image,ImageTk

#for internet speed
import speedtest

#idle
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import os


root=Tk()
root.title('MAC OS')
root.geometry("850x500+300+170")
root.resizable(False,False)
root.configure(bg='#292e2e') 

#icon
image_icon=PhotoImage(file="E:\\New folder\Desktop\\vscode\\python\\osprojectimg\\2.png")
root.iconphoto(False,image_icon)

Body=Frame(root,width=900,height=600,bg='#d6d6d6')
Body.pack(pady=20,padx=20)

#---------------------------------------------------------------

LHS=Frame(Body,width=310,height=435,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
LHS.place(x=10,y=10)

#logo
photo=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\macbook-16121 (1).png")
myimage=Label(LHS,image=photo,background="#f4f5f5")
myimage.place(x=2,y=20)

my_system= platform.uname()

l1=Label(LHS, text='CODINGWITHHARSH',bg="#f4f5f5",font=("Acumin Variable Concept",15,"bold"),justify="center")
l1.place(x=20,y=200)

l2=Label(LHS, text=f"Version:{my_system.version}",bg="#f4f5f5",font=("Acumin Variable Concept",9,"bold"),justify="center")
l2.place(x=20,y=225)

l3=Label(LHS, text=f"System:{my_system.system}",bg="#f4f5f5",font=("Acumin Variable Concept",15,"bold"),justify="center")
l3.place(x=20,y=250)

l4=Label(LHS, text=f"Machine:{my_system.machine}",bg="#f4f5f5",font=("Acumin Variable Concept",15,"bold"),justify="center")
l4.place(x=20,y=285)

l5=Label(LHS, text=f"Total RAM installed:{round(psutil.virtual_memory().total/1000000000,2)} GB",bg="#f4f5f5",font=("Acumin Variable Concept",13,"bold"),justify="center")
l5.place(x=18,y=317)

l6=Label(LHS, text=f"Processor:AMD RYZEN 5600G",bg="#f4f5f5",font=("Acumin Variable Concept",13,"bold"),justify="center")
l6.place(x=20,y=340)

#_______________________________________________


RHS=Frame(Body,width=470,height=230,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
RHS.place(x=330,y=10)

system=Label(RHS,text='System',font=("Acumin Variable Concept",15),bg='#f4f5f5')
system.place(x=10,y=10)

#battery

def convertTime(seconds):
    minutes,seconds=divmod(seconds,60)
    hours,minutes=divmod(minutes,60)
    return "%d:%02d:%02d"% (hours,minutes,seconds)

def none():
    global battery_png
    global battery_label
    battery=psutil.sensors_battery()
    percent=battery.percent
    time=convertTime(battery.secsleft)

    # print(percent)
    # print(time)

    lbl.config(text=f"{percent}%")
    lbl_plug.config(text=f"Plug in:{str(battery.power_plugged)}")
    lbl_time.config(text=f"{time} remaining")
    
    battery_label=Label(RHS,background='#f4f5f5')
    battery_label.place(x=15,y=50)

    lbl.after(1000,none)

    if battery.power_plugged==True:
        battery_png=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\charging.png")  #charging png
        battery_label.config(image=battery_png)   
    else:
        battery_png=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\battery.png")     #full charge
        battery_label.config(image=battery_png)   


lbl=Label(RHS,font=("Acumin Variable Concept",40,"bold"),bg='#f4f5f5')
lbl.place(x=200,y=40)

lbl_plug=Label(RHS,font=("Acumin Variable Concept",40,"bold"),bg='#f4f5f5')
lbl_plug.place(x=20,y=100)

lbl_time=Label(RHS,font=("Acumin Variable Concept",40,"bold"),bg='#f4f5f5')
lbl_time.place(x=200,y=100)

#none()



#####################################
#speaker

lbl_speaker=Label(RHS,text="Speaker:",font=('arial',10,'bold'),bg='#f4f5f5')
lbl_speaker.place(x=10,y=150)
volume_value=tk.DoubleVar()

def get_current_volume_value():
    return '{: .2f}'.format(volume_value.get())

def volume_changed(event):
    device =AudioUtilities.GetSpeakers()
    interface = device.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
    volume= cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(-float(get_current_volume_value()),None)


style=  ttk.Style()
style.configure("TScale", background='#f4f5f5')
volume=ttk.Scale(RHS,from_=60,to=0,orient='horizontal',
                 command=volume_changed,variable=volume_value)
volume.place(x=90,y=150)
volume.set(20)

##############################Brightness##############

lbl_brightness=Label(RHS,text='Brightness',font=('arial',10,'bold'),bg='#f4f5f5')
lbl_brightness.place(x=10,y=190)

current_value=tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def brightness_changed(event):
    pct.set_brightness(get_current_value())

brightness= ttk.Scale(RHS,from_=0,to=100,orient='horizontal',
                      command=brightness_changed,variable=current_value)
brightness.place(x=90,y=190)   


#####################################

def weather():
    app1=Toplevel()
    app1.geometry("1217x747+300+200")
    app1.title('Weather')
    app1.configure(bg='#f4f5f5')
    app1.resizable(False,False)

    image_icon=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\App1.png")
    app1.iconphoto(False,image_icon)

    def getWeather():
        try:
            city=textfield.get()

            geolocator= Nominatim(user_agent="geopiExercises")
            location= geolocator.geocode(city)
            obj = TimezoneFinder ()
            result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
     
            home=pytz.timezone(result)
            local_time=datetime.now(home)
            current_time=local_time.strftime("%I:%M %p")
            clock.config(text=current_time)
            name.config(text="CURRENT WEATHER")

     #weather
            api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=3bf4122d2d5dc1b7af198f3747e3d929"

            json_data =requests.get(api).json()
            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp = int(json_data['main']['temp']-273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind= json_data['wind']['speed']

            t.config(text=(temp,"ᵒ"))
            c.config(text=(condition,"FEELS","LIKE",temp,"ᵒ"))

            w.config(text=wind)
            h.config(text=humidity)
            d.config(text=description)
            p.config(text=pressure)

        except Exception as e:
            messagebox.showerror("Weather App","Invalid Entry!!")

    


    
    images = Image.open("E:\\New folder\\Desktop\\vscode\\python\\png\\cloudy (1).png")
    images = ImageTk.PhotoImage(images)

# Create a label to display the image
    image_label = tk.Label(app1, image=images)
    image_label.place(x=130,y=430)

#for search box
    image = Image.open("E:\\New folder\\Desktop\\vscode\\python\\png\\search.png.gif")
    image = ImageTk.PhotoImage(image)

# Create a label to display the image
    image_label = tk.Label(app1, image=image)
    image_label.pack()

    textfield=tk.Entry(app1,justify="center",width=17,font=("poppins",25,"bold"),bg="white",border=0)
    textfield.place(x=380,y=160)
    textfield.focus()


    cimage = Image.open("E:\\New folder\\Desktop\\vscode\\python\\png\\icons8-weather-app-100.png")
    cimage = ImageTk.PhotoImage(cimage)

#Create a label to display the image
    cimage_label = tk.Label(app1, image=cimage)
    cimage_label.place(x=20,y=130)


    b1=tk.Button(app1,text="",bg="white",fg="sky blue",font="Arial 18",border=0,command=getWeather)
    b1.place(x=927,y=250)

#logo
    logo_image=Image.open("E:\\New folder\\Desktop\\vscode\\python\\png\\icons8-weather-500 (2).png")

    logo_image=ImageTk.PhotoImage(logo_image)
    logo=tk.Label(app1,image=logo_image)
    logo.place(x=970,y=8)


#bottom box
    Frame_image=Image.open("E:\\New folder\\Desktop\\vscode\\python\\png\\ii.png")
    Frame_image=ImageTk.PhotoImage(Frame_image)
    frameimage=Label(app1,image=Frame_image)
    frameimage.place(x=410,y=330)


#time
    name=Label(app1,font=("arial",15,"bold"))
    name.place(x=200,y=260)
    clock=Label(app1,font=("Helveitica",20))
    clock.place(x=200,y=290)

#LABEL

    label1=Label(app1,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="sienna4")
    label1.place(x=550,y=600)

    label2=Label(app1,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="sienna4")
    label2.place(x=650,y=600)

    label3=Label(app1,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="sienna4")
    label3.place(x=800,y=600)

    label4=Label(app1,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="sienna4")
    label4.place(x=999,y=600)

    t=Label(app1,font=("arial",70,"bold"),fg="red")
    t.place(x=370,y=300)
    c=Label(app1,font=("arial",15,'bold'))
    c.place(x=370,y=400)

    w=Label(app1,text="...",font=("arial",20,"bold"),bg="sienna4",fg="white")
    w.place(x=560,y=640)

    h=Label(app1,text="...",font=("arial",20,"bold"),bg="sienna4",fg="white")
    h.place(x=680,y=640)

    d=Label(app1,text="...",font=("arial",20,"bold"),bg="sienna4",fg="white")
    d.place(x=810,y=640)

    p=Label(app1,text="...",font=("arial",20,"bold"),bg="sienna4",fg="white")
    p.place(x=1040,y=640)

    app1.mainloop()

def clock():
    app2=Toplevel()
    app2.geometry("850x110+300+10")
    app2.title('Clock')
    app2.configure(bg='#292e2e')
    app2.resizable(False,False)

    image_icon=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\App2.png")
    app2.iconphoto(False,image_icon)

    def clock():
        text=strftime('%H:%M:%S %p')
        lbl.config(text=text)
        lbl.after(1000,clock)

    lbl=Label(app2,font=('digital-7',50,'bold'),width=20,bg='#f4f5f5',fg='#292e2e')
    lbl.pack(anchor='center',pady=20)
    clock()


    app2.mainloop()
    

def calendar():
    app3=Toplevel()
    app3.geometry("300x300+-10+10")
    app3.title('Calendar')
    app3.configure(bg="#292e2e")
    app3.resizable(False,False)

    image_icon=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\clnd.png")
    app3.iconphoto(False,image_icon)

    mycal=Calendar(app3,setmode='day',date_pattern='d/m/yy')
    mycal.pack(padx=15,pady=35)

    app3.mainloop()
    

def idle():
    app4=Toplevel()
    app4.title("Python Idle")
    app4.geometry("1280x720+150+80")
    app4.configure(bg="#323846")
    app4.resizable(False,False)

    file_path= ''

    def set_file_path(path):
        global file_path
        file_path=path

    def open_file():
        path = askopenfilename(filetypes=[('Python Files','*.py')])
        with open(path, 'r') as file:
            code= file.read()
            code_input.delete('1.0',END)
            code_input.insert('1.0',code)
            set_file_path(path)

    def save():
        if file_path=='':
            path= asksaveasfilename(filetypes=[('Python Files','*.py')])
        else:
            path=file_path

        with open(path, 'w') as file:
            code= code_input.get('1.0',END)
            file.write(code)
            set_file_path(path)        

    def run():
        if file_path =='':
            messagebox.showerror("Python Idle","Save Your code")
            return
        command = f'python {file_path}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True) 
        output , error =process.communicate()
        code_output.insert('1.0', output)
        code_output.insert('1.0', error)   

    #icon
    image_icon=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\pyidle.png")
    app4.iconphoto(False,image_icon)

    #input

    code_input = Text(app4,font="cosolas 18")
    code_input.place(x=180,y=0,width=680,height=720)

    #output

    code_output = Text(app4,font="consolos 15",bg='#323846',fg='hotpink')
    code_output.place(x=860,y=0,width=430,height=720)

    #buttons

    Open=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\open.png")
    Save=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\save.png")
    Run=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\run.png")

    Button(app4,image=Open,bg="#323846",bd=0,command=open_file).place(x=30,y=30)
    Button(app4,image=Save,bg="#323846",bd=0,command=save).place(x=30,y=145)
    Button(app4,image=Run,bg="#323846",bd=0,command=run).place(x=30,y=260)

    
    app4.mainloop()


    

def google():
    wb.register('chrome',None)
    wb.open('https://www.google.com/')

def file():
    subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')    

################mode#####
button_mode=True

def mode():
    global button_mode
    if button_mode:
        LHS.config(bg="#292e2e")
        myimage.config(bg='#292e2e')
        l1.config(bg="#292e2e",fg="#d6d6d6")
        l2.config(bg="#292e2e",fg="#d6d6d6")
        l3.config(bg="#292e2e",fg="#d6d6d6")
        l4.config(bg="#292e2e",fg="#d6d6d6")
        l5.config(bg="#292e2e",fg="#d6d6d6")
        l6.config(bg="#292e2e",fg="#d6d6d6")

        RHB.config(bg="#292e2e")
        app1.config(bg="#292e2e")
        app2.config(bg="#292e2e")
        app3.config(bg="#292e2e")
        app4.config(bg="#292e2e")
        app5.config(bg="#292e2e")
        app6.config(bg="#292e2e")
        app7.config(bg="#292e2e")
        app8.config(bg="#292e2e")
        app9.config(bg="#292e2e")
        app10.config(bg="#292e2e")
        apps.config(bg="#292e2e",fg="#d6d6d6")


        button_mode=False
    else:
        LHS.config(bg="#f4f5f5")
        myimage.config(bg="#f4f5f5")
        l1.config(bg="#f4f5f5",fg="#292e2e")
        l2.config(bg="#f4f5f5",fg="#292e2e")
        l3.config(bg="#f4f5f5",fg="#292e2e")
        l4.config(bg="#f4f5f5",fg="#292e2e")
        l5.config(bg="#f4f5f5",fg="#292e2e")
        l6.config(bg="#f4f5f5",fg="#292e2e")

        RHB.config(bg="#f4f5f5")
        app1.config(bg="#f4f5f5")
        app2.config(bg="#f4f5f5")
        app3.config(bg="#f4f5f5")
        app4.config(bg="#f4f5f5")
        app5.config(bg="#f4f5f5")
        app6.config(bg="#f4f5f5")
        app7.config(bg="#f4f5f5")
        app8.config(bg="#f4f5f5")
        app9.config(bg="#f4f5f5")
        app10.config(bg="#f4f5f5")
        apps.config(bg="#f4f5f5",fg="#292e2e")


        button_mode=True    


def screenshot():
    root.iconify()

    myScreenshot=pyautogui.screenshot()
    file_path=filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)


def game():
    app10=Toplevel()
    app10.geometry("300x500+1170+170")
    app10.title("Ludo")
    app10.configure(bg='#dee2e5')
    app10.resizable(False,False)

    image_icon=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\App5.png") 
    app10.iconphoto(False,image_icon)

    ludo_image=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\ludo back.png")
    Label(app10,image=ludo_image).pack()

    label=Label(app10,text='',font=("times",150))
    
    def roll():
        dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685','\u2686']
        label.configure(text=f'{random.choice(dice)}{random.choice(dice)}',fg='#29232e')
        label.pack()

    btn_image=PhotoImage(file="E:\\New folder\Desktop\\vscode\\python\\osprojectimg\\ludo button.png")
    btn=Button(app10,image=btn_image,bg="#dee2e5",command=roll)
    btn.pack(padx=10,pady=10)

    app10.mainloop()  


def speed():
    app9=Toplevel()
    app9.title("Internet Speed Test")
    app9.geometry("360x600")
    app9.resizable(False,False)
    app9.configure(bg="#1a212d")

    def Fast():
        
        test=speedtest.Speedtest()

        Uploading=round(test.upload()/(1024*1024),2)
        upload.config(text=Uploading)

        downloading=round(test.download()/(1024*1024),2)
        download.config(text=downloading)
        Download.config(text=downloading)

        servernames= []
        test.get_servers(servernames)
        ping.config(text=test.results.ping)

    image_icon=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\speed.png")
    app9.iconphoto(False,image_icon)

    #images

    Top=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\top.png")
    Label(app9,image=Top,bg="#1a212d").pack()

    Main=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\main.png")
    Label(app9,image=Main,bg="#1a212d").pack(pady=(40,0))

    button=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\button.png")
    b1=Button(app9,image=button,bg="#1a212d",bd=0,command=Fast)
    b1.pack(pady=10)

    #Label

    Label(app9,text="PING",font="arial 10 bold",bg="#384056",fg='white').place(x=50,y=0)
    Label(app9,text="DOWNLOAD",font="arial 10 bold",bg="#384056",fg='white').place(x=140,y=0)
    Label(app9,text="UPLOAD",font="arial 10 bold",bg="#384056",fg='white').place(x=260,y=0)

    Label(app9,text="MS",font="arial 8 bold",bg="#384056",fg='white').place(x=60,y=80)
    Label(app9,text="MBPS",font="arial 8 bold",bg="#384056",fg='white').place(x=165,y=80)
    Label(app9,text="MBPS",font="arial 8 bold",bg="#384056",fg='white').place(x=275,y=80)

    Label(app9,text="Download",font="arial 15 bold",bg='#384056',fg='white').place(x=140,y=280)
    Label(app9,text="MBPS",font="arial 15 bold",bg='#384056',fg='white').place(x=155,y=380)

    ping=Label(app9,text="00",font="arial 13 bold",bg='#384056',fg='white')
    ping.place(x=70,y=60,anchor="center")

    download=Label(app9,text="00",font="arial 13 bold",bg='#384056',fg='white')
    download.place(x=180,y=60,anchor="center")

    upload=Label(app9,text="00",font="arial 13 bold",bg='#384056',fg='white')
    upload.place(x=290,y=60,anchor="center")

    Download=Label(app9,text="00",font="arial 40 bold",bg='#384056',fg="sky blue")
    Download.place(x=185,y=350,anchor="center")

    app9.mainloop()

#####################################

RHB=Frame(Body,width=470,height=190,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
RHB.place(x=330,y=255)


apps=Label(RHB,text='Apps',font=('Acumin Variable Concept',15),bg='#f4f5f5')
apps.place(x=10,y=10)

app1_image=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\App1.png")
app1=Button(RHB,image=app1_image,bd=0,command=weather)
app1.place(x=35,y=50)

app2_image=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\App2.png")
app2=Button(RHB,image=app2_image,bd=0,command=clock)
app2.place(x=120,y=50)

app3_image=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\clnd.png")
app3=Button(RHB,image=app3_image,bd=0,command=calendar)
app3.place(x=210,y=50)


app4_image=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\pyidle.png")
app4=Button(RHB,image=app4_image,bd=0,command=idle)
app4.place(x=300,y=50)

app5_image=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\App8.png")
app5=Button(RHB,image=app5_image,bd=0,command=google)
app5.place(x=375,y=50)

app6_image=PhotoImage(file="E:\\New folder\\Desktop\\vscode\python\\osprojectimg\\App7.png")
app6=Button(RHB,image=app6_image,bd=0,command=file)
app6.place(x=35,y=120)

app7_image=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\App4.png")
app7=Button(RHB,image=app7_image,bd=0,command=mode)
app7.place(x=120,y=120)

app8_image=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\App6.png")
app8=Button(RHB,image=app8_image,bd=0,command=screenshot)
app8.place(x=210,y=120)

app9_image=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\speed.png")
app9=Button(RHB,image=app9_image,bd=0,command=speed)
app9.place(x=300,y=120)
# "E:\New folder\Desktop\vscode\python\osprojectimg\speed.png"
# "E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\internet.png"

app10_image=PhotoImage(file="E:\\New folder\\Desktop\\vscode\\python\\osprojectimg\\App5.png")
app10=Button(RHB,image=app10_image,bd=0,command=game)
app10.place(x=375,y=120)

root.mainloop()