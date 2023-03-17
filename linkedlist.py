import os
os.system ('cls')

#Node
class Node():
    def __init__(self,data):
        self._data = data
        self._next = None

#Linked list 
class LL:
    def __init__(self):
        self._head =None
        
    #Untuk menambahkan data
    def add1(self,data):
        a=Node(data)
        if self._head == None:
            self._head = a
        else:
            a._next = self._head
            self._head = a
               
    #Untuk menampilkan data
    def cetak(self):
        a=self._head
        while a != None:
            print(a._data)
            a=a._next

#Deklarasi bahwa myLL adalah linkedlist
myLL = LL()

while True:
    os.system ('cls')
    #Menu user
    print ("[1] Input nomor registrasi")
    print ("[2] Lihat nomor registrasi Saya")
    
    tindakan = input("Ketik angka dari tindakan yang Anda pilih : ")
    if tindakan =='1':
        tambah = input("Masukkan nomor registrasi Anda : ")
        myLL.add1(tambah)

    elif tindakan == '2':
        print ("Nomor yang telah terdaftar:")
        myLL.cetak()


    lanjut = input("Ketik 0 jika ingin mengakhiri program: ")
    if lanjut == '0':
        print("OKE MAKASIH YA")
        break