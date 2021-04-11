import gzip


fw = gzip.open('test.txt.gz', 'wb')
fw.write(b"Testing gzip")
fw.close()
fr = gzip.open('test.txt.gz', 'rb')
print(fr.read().decode("utf-8"))
fr.close()