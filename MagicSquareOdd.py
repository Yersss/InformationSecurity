def generateOdd(n): 

    mS = []
    for i in range(n):
      s = []
      for j in range(n):
        s.append(0)
      mS.append(s)

    i = 0
    j = int(n / 2)
    place = 1
    while place <= (n*n):
        if i == -1 and j == n: 
            j = n - 2
            i = 0
        else: 
            if j == n: 
                j = 0
                  
            if i < 0: 
                i = n - 1
                  
        if mS[int(i)][int(j)]: 
            j = j - 2
            i = i + 1
            continue
        else: 
            mS[int(i)][int(j)] = place 
            place = place + 1
                  
        j = j + 1
        i = i - 1 
    return mS
  
def encrypt(o, t, k):
  for i in range(len(k)):
    if int(k[i]) <= len(t):
      o += t[int(k[i]) - 1]
    else:
      o += '*'
  if(len(t) <= len(k)):
    return o
  return encrypt(o, t[len(k):], k)

def decrypt(o, t, k):
  for i in range(1, min(len(t), len(k)) + 1):
    o += t[k.index(str(i))]
  if(len(t) <= len(k)):
    new_output = o.split('*')
    return new_output[0]
  return decrypt(o, t[len(k):], k)

text = input()
n = int(input())
key = generateOdd(n)   
new_key = []
for i in range(0, n): 
        for j in range(0, n): 
            new_key.append(str(key[i][j]))
output = str()
#print(new_key)
new_text = encrypt(output, text, new_key)
print(new_text)
output = str()
print(decrypt(output, new_text, new_key))

