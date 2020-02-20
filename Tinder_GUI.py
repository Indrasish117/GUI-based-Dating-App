import mysql.connector
from tkinter import *
from PIL import ImageTk,Image

path='C:\\Users\\User\\Desktop\\download.jpg'

class Login:

    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost', user='root', password='', database='tinder3')
        self.mycursor = self.conn.cursor()

        self.root_home= Tk()
        self.root_home.title('Fuel!!')
        self.root_home.minsize(800, 600)
        self.root_home.maxsize(1366, 768)

        self.greet_label = Label(self.root_home, text='Welcome to Fuel!!\n')
        self.greet_label.config(font=("Impact",44))
        self.greet_label.pack()

        '''img = ImageTk.PhotoImage(Image.open(path))'''
        img = ImageTk.PhotoImage(Image.open(r'C:\Users\User\Desktop\download.jpg'))
        panel = Label(self.root_home, image=img)
        panel.pack(side="bottom", fill="both", expand="yes")

        self.greet_label = Label(self.root_home, text='Where you will find the perfect match!\n\n')
        self.greet_label.config(font=("Times New Roman", 26))
        self.greet_label.pack()

        self.login_button = Button(self.root_home,text='Click here to login!',width='15',command=lambda :self.login())
        self.login_button.pack()
        self.login_button = Button(self.root_home, text='Click here to register!',width='15',command=lambda: self.register())
        self.login_button.pack()
        self.exit_button = Button(self.root_home, text='Exit', width='15', command=lambda :self.root_home.destroy())
        self.exit_button.pack()

        self.root_home.mainloop()

    def login(self):
        self.root = Tk()
        self.root.title('Login page')
        self.root.minsize(800, 600)
        self.root.maxsize(1366, 768)

        self.email_label = Label(self.root, text='\n\nEnter email address:')
        self.email_label.pack()

        self.email_input = Entry(self.root)
        self.email_input.pack()

        self.password_label = Label(self.root, text='Enter Password:')
        self.password_label.pack()

        self.password_input = Entry(self.root)
        self.password_input.pack()

        self.button = Button(self.root, text='Login', command=lambda: self.user_menu())
        self.button.pack()

        self.reg_msg = Label(self.root, text="\n\n\n\nNot a member?Then please register!")
        self.reg_msg.pack()

        self.reg_button = Button(self.root, text='Register', command=lambda: self.register())
        self.reg_button.pack()

        self.result = Label(self.root, text='', fg='red')
        self.result.pack()
        self.root.mainloop()

    def user_menu(self):
        email=self.email_input.get()
        password=self.password_input.get()

        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` 
        LIKE '{}' AND `password` LIKE '{}'""".format(email,password))

        self.user_list=self.mycursor.fetchall()

        if len(self.user_list)>0:
            self.root.destroy()
            self.root_user=Tk()
            self.root_user.title('User Menu:')
            self.root_user.maxsize(1280,360)
            self.root_user.minsize(1280,360)

            string='Welcome '+self.user_list[0][1]+'!'
            self.welcome=Label(self.root_user,text=string,bg='Red')
            self.welcome.config(font=('Ariel',22))
            self.welcome.pack()

            self.choice=Label(self.root_user,text='\nChoose from the available menu:')
            self.choice.config(font=('Times New Roman',18))
            self.choice.pack()

            self.space = Label(self.root_user, text='\n\n')
            self.space.pack()

            self.choice1=Button(self.root_user,text='View all users',width='40',command=lambda :self.view_users())
            self.choice1.pack()

            self.choice2 = Button(self.root_user, text='View proposals',width='40',command=lambda :self.view_proposals())
            self.choice2.pack()

            self.choice3 = Button(self.root_user, text='View requests',width='40',command=lambda :self.view_requests())
            self.choice3.pack()

            self.choice4 = Button(self.root_user, text='View matches',width='40',command=lambda :self.view_matches())
            self.choice4.pack()

            self.choice6 = Button(self.root_user, text='Log out', width='40', command=lambda :self.log_out())
            self.choice6.pack()

            self.root_user.mainloop()
        else:
            self.result.configure(text='Incorrect credentials')

    def view_proposals(self):
        self.mycursor.execute("""SELECT * FROM `proposals` p
        JOIN `users` u ON u.`user_id`=p.`juliet_id`
        WHERE p.`romeo_id` LIKE '{}'""".format(self.user_list[0][0]))

        proposed_user_list = self.mycursor.fetchall()

        self.root_view_proposals = Tk()
        self.root_view_proposals.title("The users you have proposed are:")

        self.M_name = Label(self.root_view_proposals, text='Name', width='36').grid(row=0, column=0)
        self.M_gender = Label(self.root_view_proposals, text='Gender', width='12').grid(row=0, column=1)
        self.M_age = Label(self.root_view_proposals, text='Age', width='8').grid(row=0, column=2)
        self.M_city = Label(self.root_view_proposals, text='City', width='20').grid(row=0, column=3)

        c = 1

        for i in proposed_user_list:
            self.L_name = Label(self.root_view_proposals, text=i[4], width='36', bg='white').grid(row=c, column=0)
            self.L_gender = Label(self.root_view_proposals, text=i[7], width='12', bg='white').grid(row=c, column=1)
            self.L_age = Label(self.root_view_proposals, text=i[8], width='8', bg='white').grid(row=c, column=2)
            self.L_city = Label(self.root_view_proposals, text=i[9], width='20', bg='white').grid(row=c, column=3)
            c = c + 1

    def view_requests(self):
        self.mycursor.execute("""SELECT * FROM `proposals` p
        JOIN `users` u ON u.`user_id`=p.`romeo_id`
        WHERE p.`juliet_id` LIKE '{}'""".format(self.user_list[0][0]))

        requests_user_list = self.mycursor.fetchall()

        self.root_view_requests = Tk()
        self.root_view_requests.title("The users who have proposed you are:")

        self.M_name = Label(self.root_view_requests, text='Name', width='36').grid(row=0, column=0)
        self.M_gender = Label(self.root_view_requests, text='Gender', width='12').grid(row=0, column=1)
        self.M_age = Label(self.root_view_requests, text='Age', width='8').grid(row=0, column=2)
        self.M_city = Label(self.root_view_requests, text='City', width='20').grid(row=0, column=3)

        c = 1

        for i in requests_user_list:
            self.L_name = Label(self.root_view_requests, text=i[4], width='36', bg='white').grid(row=c, column=0)
            self.L_gender = Label(self.root_view_requests, text=i[7], width='12', bg='white').grid(row=c, column=1)
            self.L_age = Label(self.root_view_requests, text=i[8], width='8', bg='white').grid(row=c, column=2)
            self.L_city = Label(self.root_view_requests, text=i[9], width='20', bg='white').grid(row=c, column=3)
            c = c + 1

    def view_matches(self):
        self.mycursor.execute("""SELECT * FROM `proposals` p
                        JOIN `users` u ON u.`user_id`=p.`juliet_id`
                        WHERE p.`romeo_id` LIKE '{}'""".format(self.user_list[0][0]))

        proposed_user_list = self.mycursor.fetchall()

        self.mycursor.execute("""SELECT * FROM `proposals` p
                        JOIN `users` u ON u.`user_id`=p.`romeo_id`
                        WHERE p.`juliet_id` LIKE '{}'""".format(self.user_list[0][0]))

        requests_user_list = self.mycursor.fetchall()

        self.root_view_matches = Tk()
        self.root_view_matches.title("These are the matches we have found for you:")

        self.M_name = Label(self.root_view_matches, text='Name', width='36').grid(row=0, column=0)
        self.M_gender = Label(self.root_view_matches, text='Gender', width='12').grid(row=0, column=1)
        self.M_age = Label(self.root_view_matches, text='Age', width='8').grid(row=0, column=2)
        self.M_city = Label(self.root_view_matches, text='City', width='20').grid(row=0, column=3)

        c = 1

        for i in proposed_user_list:
            for j in requests_user_list:
                if i[2]==j[1]:
                    self.L_name = Label(self.root_view_matches, text=i[4], width='36', bg='white').grid(row=c, column=0)
                    self.L_gender = Label(self.root_view_matches, text=i[7], width='12', bg='white').grid(row=c, column=1)
                    self.L_age = Label(self.root_view_matches, text=i[8], width='8', bg='white').grid(row=c, column=2)
                    self.L_city = Label(self.root_view_matches, text=i[9], width='20', bg='white').grid(row=c, column=3)
                    c = c + 1


    def register(self):
        self.root1=Tk()
        self.root1.title('Registration')
        self.root1.minsize(300,600)
        self.root1.maxsize(300,600)

        self.d_msg=Label(self.root1,text='Please enter your details!!')
        self.d_msg.pack()

        self.d_name = Label(self.root1, text='Name:')
        self.d_name.pack()
        self.name = Entry(self.root1)
        self.name.pack()

        self.d_email = Label(self.root1, text='Email:')
        self.d_email.pack()
        self.email = Entry(self.root1)
        self.email.pack()

        self.d_password = Label(self.root1, text='Password:')
        self.d_password.pack()
        self.password = Entry(self.root1)
        self.password.pack()

        self.d_gender = Label(self.root1, text='Gender:')
        self.d_gender.pack()
        self.gender = Entry(self.root1)
        self.gender.pack()

        self.d_age = Label(self.root1, text='Age:')
        self.d_age.pack()
        self.age = Entry(self.root1)
        self.age.pack()

        self.d_city = Label(self.root1, text='City:')
        self.d_city.pack()
        self.city = Entry(self.root1)
        self.city.pack()

        self.reg_success=Label(self.root1,text='')
        self.reg_success.pack()

        self.reg_button=Button(self.root1,text='Register!',command=lambda :self.entry())
        self.reg_button.pack()

        self.root1.mainloop()

    def entry(self):
        Xname=self.name.get()
        Xemail=self.email.get()
        Xpassword=self.password.get()
        Xgender=self.gender.get()
        Xage=self.age.get()
        Xcity=self.city.get()

        self.mycursor.execute("""SELECT * FROM `users` 
        WHERE `email` LIKE '{}'""".format(Xemail))

        user_list = self.mycursor.fetchall()

        if len(user_list)>0:
            self.root_err=Tk()
            self.root_err.title('Error!')
            self.root_err.maxsize(300,180)
            self.root_err.minsize(300,180)

            self.error_msg=Label(self.root_err,text='An account with this name already exists!!')
            self.error_msg.pack()

            self.retry=Button(self.root_err,text='Retry',command=lambda :self.re_enter())
            self.retry.pack()

            self.home_button=Button(self.root_err,text='Go to Main page',command=lambda :self.go_home())
            self.home_button.pack()
        else:
            self.mycursor.execute("""INSERT INTO `users` 
            (`user_id`,`name`,`email`,`password`,`gender`,`age`,`city`) VALUES 
            (NULL,'{}','{}','{}','{}','{}','{}')""".format(Xname, Xemail, Xpassword, Xgender, Xage, Xcity))

            self.conn.commit()
            self.reg_success.configure(text='REGISTRATION SUCCESSFUL!!', fg='green')

    def go_home(self):
        self.root_err.destroy()
        self.root1.destroy()

    def log_out(self):
        self.root_user.destroy()
        self.user_list.clear()
        self.login()

    def re_enter(self):
        self.root_err.destroy()
        self.root1.destroy()
        self.register()

    def view_users(self):
        self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` NOT LIKE 
                '{}'""".format(self.user_list[0][0]))

        all_users_list = self.mycursor.fetchall()

        self.root_view_all=Tk()
        self.root_view_all.title("All users")


        self.M_user_id = Label(self.root_view_all, text='User ID', width='8').grid(row=0, column=0)
        self.M_name = Label(self.root_view_all, text='Name', width='36').grid(row=0, column=1)
        self.M_gender = Label(self.root_view_all, text='Gender', width='12').grid(row=0, column=2)
        self.M_age = Label(self.root_view_all, text='Age', width='8').grid(row=0, column=3)
        self.M_city = Label(self.root_view_all, text='City', width='20').grid(row=0, column=4)

        c=1

        for i in all_users_list:

            self.L_user_id = Label(self.root_view_all, text=i[0], width='8', bg='white').grid(row=c, column=0)
            self.L_name = Label(self.root_view_all, text=i[1], width='36', bg='white').grid(row=c, column=1)
            self.L_gender = Label(self.root_view_all, text=i[4], width='12', bg='white').grid(row=c, column=2)
            self.L_age = Label(self.root_view_all, text=i[5], width='8', bg='white').grid(row=c, column=3)
            self.L_city = Label(self.root_view_all, text=i[6], width='20', bg='white').grid(row=c, column=4)

            c=c+1

        self.B_propose = Button(self.root_view_all, text='Propose', width='8', bg='Yellow', command=lambda :self.get_id()).grid(row=c, column=2)
        self.B_return = Button(self.root_view_all, text='Return', width='8', bg='Red', command=lambda :self.root_view_all.destroy()).grid(row=c, column=3)

        self.root_view_all.mainloop()

    def get_id(self):
        self.root_get_id = Tk()
        self.root_get_id.title('Propose')
        self.root_get_id.maxsize(300,150)

        self.L_get_id = Label(self.root_get_id, text='Enter the User-ID of the user you want to propose:')
        self.L_get_id.pack()

        self.juliet_input = Entry(self.root_get_id)
        self.juliet_input.pack()

        self.propose_button = Button(self.root_get_id, text='Propose', command=lambda :self.call_propose())
        self.propose_button.pack()

        self.return_button = Button(self.root_get_id, text='Return', command=lambda :self.root_get_id.destroy())
        self.return_button.pack()

        self.root_get_id.mainloop()

    def call_propose(self):
        juliet_id=self.juliet_input.get()
        self.propose(self.user_list[0][0], juliet_id)

    def propose(self,romeo_id,juliet_id):
        self.mycursor.execute("""SELECT * FROM  `proposals`
        WHERE `romeo_id` LIKE '{}' AND `juliet_id` LIKE '{}'""".format(romeo_id, juliet_id))

        propose_check_list = self.mycursor.fetchall()

        if len(propose_check_list)!=0:
            self.root_err_2=Tk()
            self.root_err_2.title('Error!!')

            self.error_label = Label(self.root_err_2, text='You have already proposed this user!!\nDon\'t be this desperate!')
            self.error_label.pack()
            self.root_err_2.mainloop()
        else:
            self.mycursor.execute("""INSERT INTO `proposals` 
            (`proposal_id`,`romeo_id`,`juliet_id`) VALUES
            (NULL,'{}','{}')""".format(romeo_id, juliet_id))
            self.conn.commit()

            self.root_wish=Tk()
            self.root_wish.title('Proposal successful!')

            self.wish = Label(self.root_wish, text='Proposal sent successfully!!\nFingers crossed!!')
            self.wish.pack()

            self.root_wish.mainloop()

obj1=Login()