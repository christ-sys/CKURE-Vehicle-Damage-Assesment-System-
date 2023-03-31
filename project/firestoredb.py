import firebase_admin
from google.cloud import firestore
from firebase_admin import credentials, firestore, auth

cred = credentials.Certificate("project/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
