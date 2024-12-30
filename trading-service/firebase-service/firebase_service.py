import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("firebase_service_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def save_account(account_data):
    """Save account details to Firebase Firestore."""
    db.collection('accounts').document(account_data['id']).set(account_data)

def get_account(account_id):
    """Fetch account details from Firebase Firestore."""
    return db.collection('accounts').document(account_id).get().to_dict()

def save_transaction(transaction_data):
    """Save a transaction to Firebase Firestore."""
    db.collection('transactions').add(transaction_data)