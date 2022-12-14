# -*- coding: utf-8 -*-
"""ProjectPython_Cashier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R4GIVZ2f6PFZazk6NytCMJd9VBjHu3M9
"""

#Class
class Transaction:
#create dict  
  def __init__(self):  
    self.ItemList = dict()
#add item
  def add_item(self,item):
    self.ItemList[item[0]]=item
    #untuk mengetahui jumalh item 
  #update item
  def UpdateName(self,namaItem,UpdateNamaItem):
    tempItem = self.ItemList.get(namaItem)
    #mencari namaItem yang ada pada itemlist
    if tempItem: #tidakMemilikiNilaiNull
      self.ItemList[UpdateNamaItem]=[UpdateNamaItem,tempItem[1], tempItem[2]]
      self.ItemList.pop(namaItem)

  def UpdateQty(self,namaItem,UpdateQTY):
    tempItem = self.ItemList.get(namaItem)
    if tempItem:
       self.ItemList[namaItem]=[namaItem,UpdateQTY,tempItem[2]]

  def UpdatePrice(self,namaItem,UpdatePRC):
    tempItem = self.ItemList.get(namaItem)
    if tempItem:
       self.ItemList[namaItem]=[namaItem,tempItem[1],UpdatePRC]
  def Delete(self,namaItem):
    tempItem = self.ItemList.get(namaItem)
    if tempItem:
      self.ItemList.pop(namaItem)

  def Reset(self):
    self.ItemList.clear()
  
  def OrderCheck(self):
    for tempKeyNama in self.ItemList:
      #mengambil key karena nama = key line atas
      if '' in self.ItemList[tempKeyNama]:
        print("Pesanan Salah")
      else:
        print("Pesanan Benar")

  def PrintTransac(self):
    #mendapatkan key/index
    # print(self.ItemList)
    for itemlist in self.ItemList:
      print("Nama: ",self.ItemList[itemlist][0])
      print("Jumlah: ",self.ItemList[itemlist][1])
      print("Price: ",self.ItemList[itemlist][2])
      print("Total Harga: ",self.ItemList[itemlist][2]*self.ItemList[itemlist][1])
      print("==========================================================================")
  
  def FinalTransaction(self):
    TotalHargaFinal=0
    for itemlist in self.ItemList:
       TotalHargaFinal += self.ItemList[itemlist][2]*self.ItemList[itemlist][1]
    if TotalHargaFinal>500000:
      disc=TotalHargaFinal*0.1
      TotalHargaFinal-=disc
    elif TotalHargaFinal>300000:
      disc=TotalHargaFinal*0.08
      TotalHargaFinal-=disc
    elif TotalHargaFinal>200000:
      disc= TotalHargaFinal*0.05
      TotalHargaFinal-=disc
    print('Total Belanja yang perlu anda bayar adalah: Rp. ',TotalHargaFinal)

tempKey=0
Tranc = Transaction()
while tempKey !=10:
  print("================")
  print("1. Add Item")
  print("2. Update Item Name")
  print("3. Update Item Qty")
  print("4. Update Item Price")
  print("5. Delete Item")
  print("6. Clear Transaction")
  print("7. Print Transaction")
  print("8. Final")
  print("9. OrderCheck")
  print("10. Exit")
  print("=================")
  tempKey=input("Pilih menu yang Anda inginkan: ")
  if (tempKey=='1'):
    print("ADD ITEM")
    Nama=input("Item Name: ")
    Quantity=input("Item Quantity: ")
    Price=input("Item Price: ")
    Tranc.add_item([Nama,int(Quantity),int(Price)])
  elif (tempKey=='2'):
    print("UPDATE NAMA ITEM")
    TempName=input("Input Nama Item: ")
    TempNamaPengganti=input("Input Update Nama Terbaru: ")
    Tranc.UpdateName(TempName,TempNamaPengganti)
  elif (tempKey=='3'):
    print("UPDATE ITEM QTY")
    TempName=input("Input Nama Item: ")
    TempQTY=input("Input update QTY")
    Tranc.UpdateQty(TempName,int(TempQTY))
  elif (tempKey=='4'):
    print("Update Item price")
    TempName=input("Input Nama Item: ")
    TempPrice=input("Input New Price Item: ")
    Tranc.UpdatePrice(TempName,int(TempPrice))
  elif (tempKey=='5'):
    print("DELETE")
    TempName=input("Input Nama Item: ")
    Tranc.Delete(TempName)
  elif (tempKey=='6'):
    Tranc.Reset()
  elif (tempKey=='7'):
    Tranc.PrintTransac()
  elif (tempKey=='8'):
    Tranc.FinalTransaction()
  elif (tempKey=='9'):
    Tranc.OrderCheck()