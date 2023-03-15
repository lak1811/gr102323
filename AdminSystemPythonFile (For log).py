from tkinter import*
import os
import mysql.connector
import urllib
#importing a mysql connector and connecting it to our admin user
mydatabase=mysql.connector.connect(host='localhost',port=3306,user='Admin',passwd='ADMINPASSWORD',db='gr102023')

def window1():
    #window number one that is called locations
    window=Toplevel()
    window.title('Locations')
    window.configure(background="#fff7e6")
    
    
    def addlocations():
        #window 1[1]
        window1=Toplevel()
        window1.title('Add location')
        window1.configure(background="#fff7e6")
        #making a cursor to connect to the database
        def savedef():
            #making a cursor to connect to the database
            savecursor1=mydatabase.cursor()
            message.set("")
            message.set("Error something went wrong!")
            #put the query and recieve informations from getters to execute
            
            addquery=('INSERT INTO locations'
                        '(location,poststed,dato)'
                        'VALUES(%s,%s,%s)')
            adddata=(location.get(),postcode.get(),dato.get())
            savecursor1.execute(addquery,adddata)
            #committing the transaction
            mydatabase.commit()
            message.set("Insert completed!")

            savecursor1.close()
            
            
        #labels
        lbl_location=Label(window1,text='Submit location')
        lbl_location.grid(row=0,column=0,pady=5,sticky=W)
        

        lbl_date=Label(window1,text='Submit date of event')
        lbl_date.grid(row=1,column=0,pady=5,sticky=W)

        lbl_pc=Label(window1,text='Submit city')
        lbl_pc.grid(row=2,column=0,pady=5,sticky=W)

        #entries, stringvars
        location=StringVar()
        ent_location=Entry(window1,width=25,textvariable=location)
        ent_location.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        dato=StringVar()
        ent_dato=Entry(window1,width=15,textvariable=dato)
        ent_dato.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        postcode=StringVar()
        ent_pc=Entry(window1,width=25,textvariable=postcode)
        ent_pc.grid(row=2,column=1,sticky=W)

        btn_save=Button(window1,text='Submit',bg='green',command=savedef)
        btn_save.grid(row=3,column=2,padx=5,pady=25,sticky=E)
        message=StringVar()
        ent_message=Entry(window1, width = 30, state='readonly' ,textvariable=message)
        ent_message.grid(row=3, column = 1, padx = 5, pady = 5,sticky=E)
        

        #a way to press enter instead of clicking submit
        window1.bind('<Return>', savedef)
        btn_out=Button(window1,text='Back',bg='red',command=window1.destroy)
        btn_out.grid(row=3,column=3,padx=5,pady=25,sticky=E)
        



        
        

    def dellocations():
        #window 1[2]
        window11=Toplevel()
        window11.title('Delete location')
        window11.configure(background="#fff7e6")

        def deldef():
            #making a cursor
            delcursor=mydatabase.cursor()
            message.set("")
            message.set("Something went wrong!")
            #making a query with input from stringvars to execute

            delquery=('''DELETE FROM LOCATIONS
                            WHERE location=%s and dato=%s''')
            deldata=(location.get(),dato.get())
            
            delcursor.execute(delquery,deldata)
            
            
            mydatabase.commit()
            message.set("Delete completed")
            #commit
            delcursor.close()

        #labels

        lbl_location=Label(window11,text='Location')
        lbl_location.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        lbl_date=Label(window11,text='Date ')
        lbl_date.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        #stringvars

        location=StringVar()
        ent_location=Entry(window11,width=25,textvariable=location)
        ent_location.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        dato=StringVar()
        ent_dato=Entry(window11,width=15,textvariable=dato)
        ent_dato.grid(row=1,column=1,padx=5,pady=5,sticky=W)


        btn_save=Button(window11,text='Submit',bg='green',command=deldef)
        btn_save.grid(row=3,column=2,padx=5,pady=25,sticky=S)
        message=StringVar()
        ent_message=Entry(window11, width = 30, state='readonly' ,textvariable=message)
        ent_message.grid(row=3, column = 1, padx = 5, pady = 5,sticky=W)

        btn_out=Button(window11,text='Back',bg='red',command=window11.destroy)
        btn_out.grid(row=3,column=3,padx=5,pady=25,sticky=S)
        window11.bind('<Return>', deldef)

        


    def viewlocations():
        #window 1[3]
        window111=Toplevel()
        window111.configure(background="#fff7e6")
        window111.title('View locations')

        def windowevent(event):
            #curselection (currentselection). Must have a parameter called event so this can work
            chosen=lst_locations.get(lst_locations.curselection())
            cursord=mydatabase.cursor()
            
            #create data for the function. This data will go into input fields when the conditions are right
            cursord.execute('''SELECT location,poststed,date_format(dato,'%d-%m-%Y') as dato
                            FROM locations
                            order by dato DESC''')
            
            for row in cursord:
                #for all information in cursor, look for the information that the user clicked on and put in in the boxes
                
                if chosen[0]==(row[0]):
                    #using the rows to recieve info
                    location.set(row[0])
                    postcode.set(row[1])
                    dato.set(row[2])
            cursord.close()
            
                    
        #making data for the listbox
        cursorx=mydatabase.cursor()   
        cursorx.execute('''SELECT DISTINCT location
                                FROM locations
                                order by dato desc''')

        #making a list and adding everything in it, furthermore adding it into a listbox
        locations=[]
        for row in cursorx:
            locations+=[row]
        list_locations=StringVar()       
        lst_locations=Listbox(window111,width=25,height=10,listvariable=list_locations)
        lst_locations.grid(row=1,column=1,rowspan=2,pady=5,sticky=W)
        list_locations.set(tuple(locations))

        cursorx.close()


        #stringvars
        postcode=StringVar()
        ent_pc=Entry(window111,width=25,textvariable=postcode,state='readonly')
        ent_pc.grid(row=5,column=1,sticky=E)

        location=StringVar()
        ent_location=Entry(window111,width=25,textvariable=location,state='readonly')
        ent_location.grid(row=3,column=1,sticky=E)

        dato=StringVar()
        ent_dato=Entry(window111,width=20,textvariable=dato,state='readonly')
        ent_dato.grid(row=4,column=1,sticky=W)

        #labels

        lbl_loca=Label(window111,text='Location: ')
        lbl_loca.grid(row=3,column=0,sticky=W)

        lbl_dato=Label(window111,text='Date: ')
        lbl_dato.grid(row=4,column=0,sticky=W)

        lbl_location=Label(window111,text='Locations: ')
        lbl_location.grid(row=1,column=0,sticky=W)

        lbl_pc=Label(window111,text='City: ')
        lbl_pc.grid(row=5,column=0,sticky=W)

        #important as the event parameter

        lst_locations.bind('<<ListboxSelect>>',windowevent)
        


        
        btn_avslut2=Button(window111,text='Quit',bg='red',command=window111.destroy)
        btn_avslut2.grid(row=8,column=7,padx=5,pady=25,sticky=E)
            

    #All the buttons for the window
    
    btn_save=Button(window,bg='green',text='Register',command=addlocations)
    btn_save.grid(row=1,column=0,padx=5,pady=25,sticky=E)
    btn_del=Button(window,bg='red',text='Delete',command=dellocations)
    btn_del.grid(row=1,column=1,padx=5,pady=25,sticky=W)
    btn_view=Button(window,bg='Yellow',text='View',command=viewlocations)
    btn_view.grid(row=1,column=2,padx=5,pady=25,sticky=W)


    

    


def window2():
    window2=Toplevel()
    window2.title('News')
    window2.configure(background="#fff7e6")
    news=[]

    def windowevent(event):
        #curselection
        chosen=lst_news.get(lst_news.curselection())
        cursord=mydatabase.cursor()
        #delete all information on the text before inputing more text
        ent_text.delete('1.0',END)
        
        
        cursord.execute('''SELECT title,news,url,date_format(dato,'%d-%m-%Y') as dato
                        FROM news
                        order by title asc''')
        
        for row in cursord:
            #adding information in input fields. I have to use insert on ent_text since its a textbox.
            
            if chosen[0]==(row[0]):
                title.set(row[0])
                ent_text.insert(INSERT,(row[1]))
                url.set(row[2])
                dato.set(row[3])

        cursord.close()

    def save2():
        savecursor2=mydatabase.cursor()
        test=[]
        message.set('')
        message.set('Something went wrong!')
        name=ent_text.get("1.0",END)
        #get text into a variable from textbox
        delcursor=mydatabase.cursor()
        testcursor=mydatabase.cursor()
        testcursor.execute(''' select news from news ''')
        for row in testcursor:
            test+=[row]

        addquery=('INSERT INTO News'
                '(title,news,Url,dato)'
                'VALUES(%s,%s,%s,%s)')
        adddata=(title.get(),name,url.get(),dato.get())
        savecursor2.execute(addquery,adddata)
        #since its our plan to only have one news, then if you add a charity, then the oldest one will automatically be deleted
        if len(test)>6:
            delquery='''DELETE FROM NEWS
                        WHERE dato=(SELECT MIN(dato)) limit 1;'''
            delcursor.execute(delquery)



        mydatabase.commit()
        message.set('Insert completed!')

        savecursor2.close()
        delcursor.close()
        
        
                
    
    cursorx=mydatabase.cursor()   
    cursorx.execute('''SELECT DISTINCT title
                        FROM  news
                        order by dato desc''')
    
    

    #list, add everything to list and make a listbox
    news=[]
    for row in cursorx:
        news+=[row]
    list_news=StringVar()       
    lst_news=Listbox(window2,width=50,height=10,listvariable=list_news)
    lst_news.grid(row=1,column=2,rowspan=2,pady=5,sticky=W)
    list_news.set(tuple(news))
    cursorx.close()

    #description on how to use the page
    lbl_b=Label(window2,fg='red',bg='yellow',text='Fill in the spots "title", "url" of charity and a "description".''\n'
                'If you want to see info about current charities, click on them in the box')
    lbl_b.grid(row=0,column=2,padx=5,sticky=W)
    #Label
    lbl_current=Label(window2,text='Current'+'\n'+'Charities')
    lbl_current.grid(row=1,column=1,padx=5,pady=5,sticky=W)



    #stringvar, labels and textbox
    title=StringVar()
    ent_title=Entry(window2,width=70,textvariable=title)
    ent_title.grid(row=3,column=2,sticky=W)


    url=StringVar()
    ent_url=Entry(window2,width=70,textvariable=url)
    ent_url.grid(row=4,column=2,sticky=W)

    lbl_title=Label(window2,text='Title')
    lbl_title.grid(row=3,column=1,padx=5,pady=5,sticky=W)

    lbl_url=Label(window2,text='Url',)
    lbl_url.grid(row=4,column=1,padx=5,pady=5,sticky=W)

    lbl_dato=Label(window2,text='Date',)
    lbl_dato.grid(row=5,column=1,padx=5,pady=5,sticky=W)

    dato=StringVar()
    ent_dato=Entry(window2,width=40,textvariable=dato)
    ent_dato.grid(row=5,column=2,sticky=W)

    

    ent_text=Text(window2,width=50,height=10)
    ent_text.grid(row=7,column=2,padx=5,sticky=W)

    lbl_url=Label(window2,text='Descr')
    lbl_url.grid(row=7,column=1,padx=5,pady=5,sticky=W)
    
    
        
    
    

    message=StringVar()
    ent_message=Entry(window2, width = 55, state='readonly' ,textvariable=message)
    ent_message.grid(row=8, column = 2, padx = 10, pady = 15,sticky=W)




    lst_news.bind('<<ListboxSelect>>',windowevent)
    window2.bind('<Return>', save2)
    btn_lagre=Button(window2,text='Submit',bg='green',command=save2)
    btn_lagre.grid(row=8,column=6,padx=5,pady=5,sticky=W)

    
    btn_avslut2=Button(window2,text='Quit',bg='red',command=window2.destroy)
    btn_avslut2.grid(row=8,column=7,padx=5,pady=25,sticky=E)
    

    


def window3():
    window3=Toplevel()
    window3.title('Charities')
    window3.configure(background="#fff7e6")

    def windowevent(event):
        #curselection
        chosen=lst_charities.get(lst_charities.curselection())
        cursord=mydatabase.cursor()
        ent_text.delete('1.0',END)
        
        
        cursord.execute('''SELECT namee,descr,url
                        FROM charity
                        order by namee asc''')
        
        for row in cursord:
            #same as previous
            
            if chosen[0]==(row[0]):
                title.set(row[0])
                ent_text.insert(INSERT,(row[1]))
                url.set(row[2])
        cursord.close()

    def save2():
        #same as previous
        savecursor2=mydatabase.cursor()
        delcursor2=mydatabase.cursor()
        name=ent_text.get("1.0",END)
        message.set("")
        message.set("Error something went wrong!")
        #since its our plan to only have one news, then if you add a charity, then the oldest one will automatically be deleted

        delquery=(''' DELETE FROM charity''' )
        delcursor2.execute(delquery)

        addquery=('INSERT INTO Charity'
                        '(namee,Descr,Url)'
                        'VALUES(%s,%s,%s)')
        adddata=(title.get(),name,url.get())
        savecursor2.execute(addquery,adddata)
        mydatabase.commit()
        message.set("Insert completed!")
        

        savecursor2.close()
        delcursor2.close()
        
        
                
    
    cursorx=mydatabase.cursor()   
    cursorx.execute('''SELECT DISTINCT namee
                        FROM  charity
                        order by namee asc''')
    

    
    charities=[]
    for row in cursorx:
        #same as previous
        charities+=[row]
    list_charities=StringVar()       
    lst_charities=Listbox(window3,width=50,height=10,listvariable=list_charities)
    lst_charities.grid(row=1,column=2,rowspan=2,pady=5,sticky=W)
    list_charities.set(tuple(charities))
    cursorx.close()

    #instruction on how to use page
    lbl_b=Label(window3,fg='red',bg='yellow',text='Fill in the spots "title", "url" of charity and a "description".'
                '\n''If you want to see info about current charities, click on them in the box')
    lbl_b.grid(row=0,column=2,padx=5,sticky=W)

    lbl_current=Label(window3,text='Current'+'\n'+'Charities')
    lbl_current.grid(row=1,column=1,padx=5,pady=5,sticky=W)


    #stringvar, labels and textbox


    title=StringVar()
    ent_title=Entry(window3,width=40,textvariable=title)
    ent_title.grid(row=3,column=2,sticky=W)


    url=StringVar()
    ent_url=Entry(window3,width=40,textvariable=url)
    ent_url.grid(row=4,column=2,sticky=W)

    lbl_title=Label(window3,text='Title')
    lbl_title.grid(row=3,column=1,padx=5,pady=5,sticky=W)

    lbl_url=Label(window3,text='Url',)
    lbl_url.grid(row=4,column=1,padx=5,pady=5,sticky=W)

    ent_text=Text(window3,width=30,height=10)
    ent_text.grid(row=6,column=2,padx=5,sticky=W)

    lbl_descr=Label(window3,text='Descr')
    lbl_descr.grid(row=6,column=1,padx=5,pady=5,sticky=W)
    
        


    message=StringVar()
    ent_message=Entry(window3, width = 55, state='readonly' ,textvariable=message)
    ent_message.grid(row=9, column = 2, padx = 10, pady = 15,sticky=W)
    


    lst_charities.bind('<<ListboxSelect>>',windowevent)
    

    btn_add=Button(window3,text='Submit',bg='Green',command=save2)
    btn_add.grid(row=8,column=3,padx=5,pady=25,sticky=W)
    
    btn_avslut2=Button(window3,text='Quit',bg='red',command=window3.destroy)
    btn_avslut2.grid(row=8,column=4,padx=5,pady=25,sticky=W)

def window4():
    window4=Toplevel()
    window4.configure(background="#fff7e6")
    window4.title('Feedback')

    def windowevent(event):
        #curselection
        chosen=lst_contactus.get(lst_contactus.curselection())
        cursord=mydatabase.cursor()
        ent_text.delete('1.0',END)
        
        
        cursord.execute('''SELECT namee,email,concern,descr,date_format(dato,'%d-%m-%Y') as dato,ID
                        FROM Contactus
                        order by dato DESC''')
        
        for row in cursord:
            #set all areas to the right attribute
            
            if chosen[0]==(row[5]):
                name.set(row[0])
                email.set(row[1])
                concern.set(row[2])
                ent_text.insert(INSERT,(row[3]))
                dato.set(row[4])
                ID.set(row[5])
        cursord.close()
        
                
    
    cursorx=mydatabase.cursor()   
    cursorx.execute('''SELECT DISTINCT ID
                        FROM  contactus
                        order by ID asc''')

    #same as before
    contactus=[]
    for row in cursorx:
        contactus+=[row]
    list_contactus=StringVar()       
    lst_contactus=Listbox(window4,width=25,height=10,listvariable=list_contactus)
    lst_contactus.grid(row=2,column=1,rowspan=2,pady=5,sticky=W)
    list_contactus.set(tuple(contactus))
    cursorx.close()




    #stringvar
    name=StringVar()
    ent_name=Entry(window4,width=20,textvariable=name,state='readonly')
    ent_name.grid(row=0,column=3,sticky=E)


    email=StringVar()
    ent_email=Entry(window4,width=20,textvariable=email,state='readonly')
    ent_email.grid(row=1,column=3,sticky=E)

    concern=StringVar()
    ent_concern=Entry(window4,width=20,textvariable=concern,state='readonly')
    ent_concern.grid(row=2,column=3,sticky=E)


    dato=StringVar()
    ent_date=Entry(window4,width=20,textvariable=dato,state='readonly')
    ent_date.grid(row=3,column=3,sticky=E)

    ID=StringVar()
    ent_id=Entry(window4,width=20,textvariable=ID,state='readonly')
    ent_id.grid(row=4,column=3,sticky=E)

    ent_text=Text(window4,width=35,height=10)
    ent_text.grid(row=5,column=1,sticky=W)

    #labels

    lbl_ids=Label(window4,text='All IDs: ')
    lbl_ids.grid(row=1,column=1,sticky=W)

    lbl_des=Label(window4,fg='red',bg='yellow',text='Click on one of the IDs to display information ')
    lbl_des.grid(row=0,column=1,sticky=W)

    lbl_name=Label(window4,text='Name: ')
    lbl_name.grid(row=0,column=2,sticky=W,pady=15)

    lbl_email=Label(window4,text='Email: ')
    lbl_email.grid(row=1,column=2,sticky=W,pady=15)

    lbl_concern=Label(window4,text='Concern: ')
    lbl_concern.grid(row=2,column=2,sticky=W,pady=15)



    lbl_date=Label(window4,text='Date: ')
    lbl_date.grid(row=3,column=2,sticky=W,pady=15)

    lbl_id=Label(window4,text='ID: ')
    lbl_id.grid(row=4,column=2,sticky=W,pady=15)

    lbl_description=Label(window4,text='Description: ')
    lbl_description.grid(row=4,column=1,sticky=W)




    
    

    lst_contactus.bind('<<ListboxSelect>>',windowevent)
    


    
    btn_avslut2=Button(window4,text='Quit',bg='red',command=window4.destroy)
    btn_avslut2.grid(row=8,column=7,padx=5,pady=25,sticky=E)

    
def window5():
    def enter5(event):
        funksjon()
        
    def funksjon():
        #open up userfile and make a flag to make sure we can register user
        userfile=open('users.txt','r')
        flagg=True
        fname1=userfile.readline()
        #readline method used in prg1000 and prg1100
        while fname1!='':
            fname1=fname1.rstrip('\n')
            ename1=userfile.readline().rstrip('\n')
            username1=userfile.readline().rstrip('\n')
            password1=userfile.readline().rstrip('\n')
            #if usermane exist, then this should not work
            if username1==username.get():
                flagg=False
            fname1=userfile.readline()
            message.set('This user already exists')
        #close file
        userfile.close()
        #if any spaces are empty
        if fname.get()=='' or ename.get()=='' or username.get()=='' or password.get()=='':
            flagg=False
            message.set('One of the necessary fields is not filled')

        

        #if all conditions are met
        if flagg==True:
            userfilea=open('users.txt','a')
            userfilea.write(fname.get()+'\n')
            userfilea.write(ename.get()+'\n')
            userfilea.write(username.get()+'\n')
            userfilea.write(password.get()+'\n')
            message.set('Completed registration')



            

            
           
    #window details
    registerwindow=Toplevel()
    registerwindow.title('Register a new user!')
    registerwindow.configure(background="#fff7e6")

    #labels

    lbl_fname = Label(registerwindow, text = 'First name')
    lbl_fname.grid(row = 0, column = 0, padx = 10, pady = 15,sticky=W)

    lbl_ename = Label(registerwindow, text = 'Last name ')
    lbl_ename.grid(row = 1, column = 0, padx = 10, pady = 15,sticky=W)

    lbl_username = Label(registerwindow, text = 'Username ')
    lbl_username.grid(row = 2, column = 0, padx = 10, pady = 15,sticky=W)

    lbl_password = Label(registerwindow, text = 'Password: ')
    lbl_password.grid(row = 3, column = 0, padx = 10, pady = 15,sticky=W)

    #Stringvars


    fname = StringVar() 
    ent_fname = Entry(registerwindow, width = 20, textvariable = fname)
    ent_fname.grid(row = 0, column = 1, padx = 10, pady = 15,sticky=W)

    ename = StringVar()
    ent_ename = Entry(registerwindow, width = 20, textvariable = ename)
    ent_ename.grid(row=1, column = 1, padx = 10, pady = 15,sticky=W)

    username = StringVar() 
    ent_username = Entry(registerwindow, width = 20, textvariable = username)
    ent_username.grid(row = 2, column = 1, padx = 10, pady = 15,sticky=W)

    password = StringVar()
    ent_password = Entry(registerwindow,show='*', width = 20, textvariable = password)
    ent_password.grid(row=3, column = 1, padx = 10, pady = 15,sticky=W)



    btn_submit=Button(registerwindow,bg='green',text='Submit',command=funksjon)
    btn_submit.grid(row=4,column=3,padx=5,pady=25,sticky=E)

    btn_avslutt=Button(registerwindow,bg='red',text='Quit',command=registerwindow.destroy)
    btn_avslutt.grid(row=4,column=4,padx=5,pady=25,sticky=E)

    message=StringVar()
    ent_message=Entry(registerwindow, width = 55, state='readonly' ,textvariable=message)
    ent_message.grid(row=5, column = 1, padx = 10, pady = 15,sticky=W)

    

    registerwindow.bind('<Return>', enter5)








def window6():

    def enter6(event):
        funksjon()
        
    def funksjon():
        #open up userfile and make a flag to make sure we can delete user
        flagg=True
        flagg1=True

        #if any spaces are empty
        if username.get()=='' or password.get()=='':
            flagg=False
            message.set('One of the necessary fields is not filled')

        userfile=open('users.txt','r')
        fname1=userfile.readline()
        #readline method used in prg1000 and prg1100
        while fname1!='':
            fname1=fname1.rstrip('\n')
            ename1=userfile.readline().rstrip('\n')
            username1=userfile.readline().rstrip('\n')
            password1=userfile.readline().rstrip('\n')
            if username1==username.get():
                flagg1=False
            fname1=userfile.readline()
        #close file
        userfile.close()

        

        


        if flagg==True and flagg1==False:

            userfile=open('users.txt','r')
            temp_file=open('temp.txt','w')
            fname2=userfile.readline()
            while fname2!='':
                fname2=fname2.rstrip('\n')
                ename2=userfile.readline().rstrip('\n')
                username2=userfile.readline().rstrip('\n')
                password2=userfile.readline().rstrip('\n')
                if username2!=username.get():
                    temp_file.write(fname2+'\n')
                    temp_file.write(ename2+'\n')
                    temp_file.write(username2+'\n')
                    temp_file.write(password2+'\n')

                fname2=userfile.readline()
            temp_file.close()
            userfile.close()
                    
            
            message.set("Your file has been updated")
            os.remove('users.txt')
            os.rename('temp.txt','users.txt')

        else:
            message.set('ERROR!!')
        if flagg==False:
            message.set("Fill all the fields!")
        if flagg1==True:
            message.set('Could not find the user')
        
            

            
           
    #window details
    delwindow=Toplevel()
    delwindow.title('Delete user!')
    delwindow.configure(background="#fff7e6")

    #labels

    lbl_username = Label(delwindow, text = 'Username ')
    lbl_username.grid(row = 0, column = 0, padx = 10, pady = 15,sticky=W)

    lbl_password = Label(delwindow, text = 'Password: ')
    lbl_password.grid(row = 1, column = 0, padx = 10, pady = 15,sticky=W)

    #Stringvars

    username = StringVar() 
    ent_username = Entry(delwindow, width = 20, textvariable = username)
    ent_username.grid(row = 0, column = 1, padx = 10, pady = 15,sticky=W)

    password = StringVar()
    ent_password = Entry(delwindow,show='*', width = 20, textvariable = password)
    ent_password.grid(row=1, column = 1, padx = 10, pady = 15,sticky=W)



    btn_submit=Button(delwindow,bg='green',text='Submit',command=funksjon)
    btn_submit.grid(row=2,column=3,padx=5,pady=25,sticky=E)

    btn_avslutt=Button(delwindow,bg='red',text='Quit',command=delwindow.destroy)
    btn_avslutt.grid(row=2,column=4,padx=5,pady=25,sticky=E)

    message=StringVar()
    ent_message=Entry(delwindow, width = 55, state='readonly' ,textvariable=message)
    ent_message.grid(row=3, column = 1, padx = 10, pady = 15,sticky=W)

    

    delwindow.bind('<Return>', enter6)






def pageopen():
    os.system("start \"\" http://localhost/appen/main-LK.php")




def main():
    #mainwindow where you can choose which window you want to use
    mainwindow=Toplevel()
    mainwindow.title('Main window')
    mainwindow.configure(background="#fff7e6")
    #btn for all main windows
    btn_window1=Button(mainwindow,width=30, height=10,bg='#fff7e6',text='Locations',command=window1)
    btn_window1.grid(row=0,column=0,sticky=W)

    btn_window2=Button(mainwindow,width=30,height=10,bg='#fff7e6',text='News',command=window2)
    btn_window2.grid(row=0,column=1,sticky=E)

    btn_window3=Button(mainwindow,width=30,height=10,bg='#fff7e6',text='Charity',command=window3)
    btn_window3.grid(row=1,column=0,sticky=W)

    btn_window4=Button(mainwindow,width=30,height=10,bg='#fff7e6',text='Contact Us',command=window4)
    btn_window4.grid(row=1,column=1,sticky=E)

    btn_reg=Button(mainwindow,width=30,height=10,bg='#fff7e6',text='Register user',command=window5)
    btn_reg.grid(row=2,column=0,sticky=E)

    btn_del=Button(mainwindow,width=30,height=10,bg='#fff7e6',text='Delete user',command=window6)
    btn_del.grid(row=2,column=1,sticky=E)

    btn_visit=Button(mainwindow,width=30,height=10,bg='#fff7e6',text='Visit website',command=pageopen)
    btn_visit.grid(row=3,column=0,sticky=E)

    btn_quit=Button(mainwindow,width=30,height=10,bg='red',text='Quit',command=mainwindow.destroy)
    btn_quit.grid(row=3,column=1,sticky=E)



    
    
    
def loginauthentication():
    #login authentication, to make sure the password and username is correct
    loginfile=open('users.txt','r')
    flag=False
    #getters to get username and password, and therafter make sure they are correct
    getusername=username.get()
    getpassword=password.get()
    fname=loginfile.readline()
    while fname!='':
        fname=fname.rstrip('\n')
        ename=loginfile.readline().rstrip('\n')
        usernamee=loginfile.readline().rstrip('\n')
        passwordd=loginfile.readline().rstrip('\n')
        if usernamee==getusername and passwordd==getpassword:
            #if correct flag is true and main shall be started
            flag=True
            main()
            
        fname=loginfile.readline()
        
    #if not then this message will come up
    if flag==False:
        message.set('Wrong password, Try again')

    loginfile.close()
            
def enterroot(event):
    #a way to press enter and come to the menu from login
    loginauthentication()

def escape():
    #own def for close button
    root.destroy()
    mydatabase.close()

    
#root window TK()
root=Tk()
root.title('Login')
root.configure(background="#fff7e6")
#login page where you start when starting applications

#labels

lbl_brukernavn = Label(root, text = 'Username ')
lbl_brukernavn.grid(row = 0, column = 0, padx = 10, pady = 15,sticky=W)

lbl_password = Label(root, text = 'Password: ')
lbl_password.grid(row = 1, column = 0, padx = 10, pady = 15,sticky=W)

#username
username = StringVar() 
ent_username = Entry(root, width = 20, textvariable = username)
ent_username.grid(row = 0, column = 1, padx = 10, pady = 15,sticky=W)

password = StringVar()
ent_password = Entry(root,show='*', width = 20, textvariable = password)
ent_password.grid(row=1, column = 1, padx = 10, pady = 15,sticky=W)

btn_submit=Button(root,bg='green',text='Submit',command=loginauthentication)
btn_submit.grid(row=3,column=3,padx=5,pady=25,sticky=E)

btn_avslutt=Button(root,bg='red',text='Quit',command=escape)
btn_avslutt.grid(row=3,column=4,padx=5,pady=25,sticky=E)

message=StringVar()
ent_message=Entry(root, width = 35, state='readonly',textvariable=message)
ent_message.grid(row=5, column = 1, padx = 10, pady = 15,sticky=W)

root.bind('<Return>', enterroot)





root.mainloop()
