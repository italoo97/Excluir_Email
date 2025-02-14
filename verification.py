import pickle

with open('token.pickle', 'rb') as token:
    creds = pickle.load(token)
    print(creds.scopes)