import kivy
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.camera import Camera
from kivy.uix.image import Image
from kivymd.uix.datatables import MDDataTable
import firebaseauth
import firestoredb
import hashlib
import time
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

# from kivymd.uix.pickers import MDDatePicker
Window.size = (350, 580)
# .kv files
Builder.load_file("login.kv")
Builder.load_file("signup.kv")
Builder.load_file("home.kv")
Builder.load_file("result.kv")
Builder.load_file("report.kv")
Builder.load_file("driverdetails.kv")

class Login(Screen):
    def verify_user(self):
        email = self.ids.email.text
        password = self.ids.password.text
        try:
            user = firebaseauth.auth.sign_in_with_email_and_password(email, password)
            self.manager.current='home'
        except:
            self.manager.current='result'
class SignUp(Screen):
    def reg_user(self):
        email = self.ids.email.text
        password = self.ids.password.text
        pass_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        name = self.ids.name.text
        contact = self.ids.contact.text
        address = self.ids.address.text
        dob = self.ids.dob.text
        age = self.ids.age.text
        gender = self.ids.gender.text
        username = self.ids.username.text
        try:
            user = firebaseauth.auth.create_user_with_email_and_password(email, password)
            user_uid = user['localId']
            data={
                "email": email,
                "name": name,
                "phone": contact,
                "address": address,
                "dob": dob,
                "age": age,
                "gender": gender,
                "username": username,
                "password": pass_hash,
            }
            user_ref = firestoredb.db.collection('users').document(user_uid).set(data)
            self.manager.current = 'login'
            print('Registration Success!')
        except Exception as e:
            print(f"Error: {e}")

class capture(Screen):
    def Camera(self):
        self.cam = self.ids['camera']
        myImg = Image()
        timeStr = time.strftime("%Y%m%d_%H%M%S")
        self.cam.export_to_png("assets/IMG {}.png".format(timeStr))
        myImg.source = "assets/IMG {}.png".format(timeStr)
        screen_manager.transition.direction='left'
        self.manager.current = 'result'

        #TO UPDATE IMAGE SOURCE
        Ckure = MDApp.get_running_app()
        Ckure.myImage.source = myImg.source 
        Ckure.prev.append("home")
    

class Result(Screen):
    def back(self, button):
        screen_manager.transition.direction='right'
        screen_manager.current = "home"

class Report(Screen):
    def report(self):
        # screen_manager.transition.direction='right'
        screen_manager.current = "report"

    def back(self, button):
        screen_manager.transition.direction='right'
        screen_manager.current = "result"

        # pass

class driverDetails(Screen):
    def details(self):
        screen_manager.current="driverdetails"
    
    def back(self, button):
        screen_manager.transition.direction='right'
        screen_manager.current = "report"
        
        

class Ckure(MDApp):
    myImage = Image()
    myImage.source = "assets/ckure.png"
    prev = []

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("splashscreen.kv"))
        screen_manager.add_widget(Login(name='login'))
        screen_manager.add_widget(SignUp(name='signup'))
        screen_manager.add_widget(capture(name='home'))
        screen_manager.add_widget(Result(name='result'))
        screen_manager.add_widget(Report(name='report'))
        screen_manager.add_widget(driverDetails(name='driverdetails'))
        
        return screen_manager
    
    def on_start(self):
        Clock.schedule_once(self.login, 5)
    def login(self, *args):
        screen_manager.current = "login"
    
    
Ckure().run()