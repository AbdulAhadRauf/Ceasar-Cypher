import string
l=list(string.ascii_lowercase)

def Encrypt(w,s):
  code=''
  for i in w:
    newpos=(l.index(i)+s)%26
    code+= l[newpos]
  print(f"the Encrypted code is {code}")

def Decrypt(w,s):
  code=''
  for i in w:
    pos = l.index(i) - s
    pos =pos%26
    code+=l[pos]
  print(f"The decrypted code is {code}")

go='Y'
while go=="Y":
  word = input("Enter The Word ").lower()
  shift = int(input("Enter the shift "))
  Typeofenc = input("Encode or Decode ").lower()
  if Typeofenc=="encode":
    Encrypt(w=word, s=shift)
  elif Typeofenc=="decode":
    Decrypt(w=word, s=shift)
  else:
    print("Please enter encrypt or decrypt ")
  go = input('Do you want to go again? Y/N ').upper()