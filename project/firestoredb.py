import firebase_admin
from google.cloud import firestore
from firebase_admin import credentials, firestore, auth

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# adding collection
# db.collection('users').add({'name':'Britney', 'email':'bcalulot09@gmail.com'})

# getting docs in a coll
# docs = db.collection('users').get()
# for doc in docs:
#     print(doc.id)
#     print(doc.to_dict())
