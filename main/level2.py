### python L2

# PKG.MOD - FUNCTION
from urllib.request import urlopen

# MODULE: string / gzip-zlib / datetime
import string

request = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")

a = request.read()
print(a.splitlines())
