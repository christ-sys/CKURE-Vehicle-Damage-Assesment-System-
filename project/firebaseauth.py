import pyrebase
from getpass import getpass


firebaseConfig = {
  "apiKey": "AIzaSyAYkWpFXiGKcoTfdrQPULd1Gvsr2pMXstM",
  "authDomain": "ckure-db.firebaseapp.com",
  "databaseURL": "https://ckure-db-default-rtdb.firebaseio.com",
  "projectId": "ckure-db",
  "storageBucket": "ckure-db.appspot.com",
  "messagingSenderId": "379512987829",
  "appId": "1:379512987829:web:02d01cfa08a1186bea5efc",
  "measurementId": "G-M4RNLKWGW7",
  "serviceAccount": "./serviceAccountKey.json"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
# email = input("Enter Email:")
# password = getpass("Enter Password")


# user = auth.create_user_with_email_and_password(email, password)
# login = auth.sign_in_with_email_and_password(email, password)
# auth.send_email_verification(login['idToken'])
# print("Login Success!")
# print("Registration Success")