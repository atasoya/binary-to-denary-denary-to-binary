def binary(denary) :
  total = ""
  if denary == 1 :
    total += "1"
    return total
  if denary % 2 == 0 :
    total += "0"
  else :
    total += "1"
  while denary // 2 != 1 :
    denary = denary // 2
    if denary % 2 == 0 :
      total += "0"
    else :
      total += "1"
  total += "1"
  return total[::-1]
def denary(binary) :
  total = 0
  binaryweight = len(binary) - 1
  for i in range(len(binary)) :
    if binary[i] == "0" :
      binaryweight -= 1
    else : 
      total = total + 2**(binaryweight)
      binaryweight -= 1
  return(total)
def home() :
  q1 = input("For changing denary to binary input '1' \n For changing binary to denary input '2':    ")
  if q1 == "1" :
    while True :
      userdenary = int(input("Input the denary :   "))
      print(binary(userdenary))
  else :
    while True :
      userbinary = input("Input the binary :   ")
      print(denary(userbinary))
home()

