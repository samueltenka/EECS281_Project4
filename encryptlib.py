def encrypt(text, key):
   s = 0
   for i in xrange(len(text)):
      s += ord(text[i]) + ord(key[i % len(key)])
      s %= 256
      yield chr(s)
def decrypt(stext, key):
   s = 0
   for i in xrange(len(stext)):
      diff = ord(stext[i])-s
      yield chr((diff - ord(key[i % len(key)]))%256)
      s += diff
      
