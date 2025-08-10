import pyrebase



firebaseConfig = {
    "apiKey": "AIzaSyAu8c7xkKU5gUX7RMHAamqE9TdwjZq8XSA",
    "authDomain": "studentmangementsystem-d4168.firebaseapp.com",
    "projectId": "studentmangementsystem-d4168",
    "storageBucket": "studentmangementsystem-d4168.appspot.com",
    "messagingSenderId": "165780601657",
    "appId": "1:165780601657:web:712111187baeefa1b0c6e8",
    "measurementId": "G-9N58SQLD4V",
    "databaseURL": ""  # Only if using Firebase Realtime DB
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
storage = firebase.storage()
