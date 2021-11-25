listx = ["satu", "dua", 3, 4, 5.6]
#akses list
print (listx[3] )
print (listx[1:3])
print (listx[4] )
#merubah elemen list
listx[3] = "tiga"
print(listx)
listx[3:5] = [7, "empat"]
print(listx)
#menambah elemen list
listy=(listx[2:4] + ["lima"] + [12,34,56])
print(listy)
listgabung=(listx + listy)
print(listgabung)