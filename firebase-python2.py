from firebase import firebase
firebase=firebase.FirebaseApplication("https://pythondbtest-5bbc3.firebaseio.com/",None)
result=firebase.get("pythondbtest-5bbc3/Customer",'')
print(result)