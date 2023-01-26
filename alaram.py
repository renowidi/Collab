import datetime
from playsound import playsound

alarmHour = int(input("Masukkan Jam : "))
alarmMin = int(input("Masukkan Menit : "))
alarmAm = input("AM / PM : ")

if alarmAm == "pm":
  alarmHour += 12

  while True:
    if alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute:
      print("Playing..")
      playsound("/petir.mp3")
    break
