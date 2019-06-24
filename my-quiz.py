import time

skor = 0

nama = str(input("Masukkan Nama Anda ! : "))
print("Selamat Datang " + nama + " Di MyQuiz")

def tambahSkor():
	global skor
	skor += 1

def minusSkor():
	global skor
	skor -= 1

def tampilSkor():
	global skor
	print("Skor Anda : ",skor)


def q1():
	global skor
	print("\nIbu kota Negara Indonesia adalah ... ")
	time.sleep(0.5)
	print("a) Surabaya")
	print("b) Malang")
	print("c) Jakarta")
	print("d) Jogjakarya\n")

	answer = str(input("Manakah Jawaban yang paling benar : "))

	if answer == "c":
		tambahSkor()
	else:
		minusSkor()

	q2()

def q2():
	global skor
	print("\nProses memasukkan dan memasang software disebut ... ")
	time.sleep(0.5)
	print("a) Reading")
	print("b) Creating")
	print("c) Installing")
	print("d) Planning\n")

	answer = str(input("Manakah Jawaban yang paling benar : "))

	if answer == "c":
		tambahSkor()
	else:
		minusSkor()

	q3()

def q3():
	global skor
	print("\nAsal Usul Internet Beawal dari tahun 1970 yang pada waktu itu bernama ...")
	time.sleep(0.5)
	print("a) Blissnet")
	print("b) Interner")
	print("c) Sandernet")
	print("d) Arpanet\n")

	answer = str(input("Manakah Jawaban yang paling benar : "))

	if answer == "d":
		tambahSkor()
	else:
		minusSkor()

q1()
tampilSkor()