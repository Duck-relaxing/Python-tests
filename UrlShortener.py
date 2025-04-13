import pyshorteners
import pyshorteners.shorteners
import pyshorteners.shorteners.shortcm

url = input("Escribe la URL que quieres acortar: ")

short_url = pyshorteners.Shortener().tinyurl.short(url)

print(short_url)