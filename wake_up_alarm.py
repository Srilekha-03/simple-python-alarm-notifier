import pygame
import win10toast
from win10toast import ToastNotifier
import time
import datetime

pygame.mixer.init()

toaster = ToastNotifier()

datetimeString = input("enter date and time in this format dd/mm/yyyy hh:mm:ss")
today = datetime.datetime.today()
target = datetime.datetime.strptime(datetimeString, "%d/%m/%Y %H:%M:%S")
totalTime = target - today
seconds = totalTime.total_seconds()


print("\nALARM CLOCK SET SUCCESSFULLY\n")
time.sleep(seconds)
toaster.show_toast("Alarm clock","Wake Up",duration=10, threaded=True)
pygame.mixer.music.load(r"C:\Users\srile\Downloads\sound.mp3")
#pygame.mixer.music.load("path/to/sound.mp3")

pygame.mixer.music.play()
