teori = int(input("Masukan nilai ujian teori : "))
praktek = int(input("Masukan nilai ujian praktek : "))
if teori >= 70 & praktek >= 70:
    print("Selamat, anda lulus!")
if teori < 70 & praktek >= 70:
    print("Anda harus mengulang ujian teori.")
if teori >= 70 & praktek < 70:
    print("Anda harus mengulang ujian praktek.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")