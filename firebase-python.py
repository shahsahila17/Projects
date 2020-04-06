from firebase import firebase
firebase=firebase.FirebaseApplication("https://pythondbtest-5bbc3.firebaseio.com/",None)
data={
"Name":"Sahil",
"Age":19      
}

result=firebase.post("pythondbtest-5bbc3/Customer",data)
print(result)
