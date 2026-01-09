import firebase_admin
from firebase_admin import credentials, auth
import os, json

if not firebase_admin._apps:
    if "FIREBASE_SERVICE_ACCOUNT" in os.environ:
        cred_dict = json.loads(os.environ["FIREBASE_SERVICE_ACCOUNT"])
        cred = credentials.Certificate(cred_dict)
    else:
        cred = credentials.Certificate("serviceAccountKey.json")

    firebase_admin.initialize_app(cred)

__all__ = ["auth"]
