#message = \
#"""Hey there! How have you been? I've been great! I just learned about this really cool type of cipher called a Caesar Cipher. Here's how it works: You take your message, something like "hello" and then you shift all of the letters by a certain offset. 

#For example, if I chose an offset of 3 and a message of "hello", I would encode my message by shifting each letter 3 places to the left with respect to the alphabet. So "h" becomes "e", "e" becomes "b", "l" becomes "i", and "o" becomes "l". Then I have my encoded message, "ebiil"! Now I can send you my message and the offset and you can decode it by shifting each letter 3 places to the right. The best thing is that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher! Isn't that so cool! Okay, now I'm going to send you a longer encoded message that you have to decode yourself!
    
#xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!
    
#This message has an offset of 10. Can you decode it?"""

#we decode de message using alphabet have 26 caracter we use a for and save te letter and compared with the alphabet and wend thwy are thew same we plus 10, if they dont find nothing we copy the same at this case all the space and caractere they are not letter 
alphabet = [chr(97 + i) for i in range(0,26)]

def decodeMsg(message, offSet):
  decode_msg = []
  for i in message:
    if i in alphabet:
      decode_msg.append(alphabet[(alphabet.index(i) + offSet) % 26])  
    else:
      decode_msg.append(i)
  print("".join(decode_msg))
  print()

decodeMsg("xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!", 10)

# send back the msg but this time we code the msg
def encodeMsg(message, offSet):
  encode_msg = []
  for i in message:
    if i in alphabet:
      encode_msg.append(alphabet[(alphabet.index(i) - offSet) % 26])  
    else:
      encode_msg.append(i)
  print("".join(encode_msg))
  print()

encodeMsg("I dont like you man. Please dont send me more message up. the next time i dont replay", 10)


decodeMsg("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 10)


decodeMsg("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14)


#Awesome work! While you were working to decode his last two messages, Vishal sent over another letter! He's really been bitten by the crypto-bug. Read it and see what interesting task he has lined up for you this time.

#Hello again friend! I knew you would love the Caesar Cipher, it's a cool, simple way to encrypt messages. Diwere unaware of the value of the shift? That's all changed witd you know that back in Caesar's time, it was considered a very secure way of communication and it took a lot of effort to crack if you h computers! Now we can brute force these kinds of ciphers very quickly, as I'm sure you can imagine.
            
#To test your cryptography skills, this next coded message is going to be harder than the last couple to crack. It's still going to be coded with a Caesar Cipher but this time I'm not going to tell you the value of the shift. You'll have to brute force it yourself.
            
#Here's the coded message:
            
   #     vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.
            
#Good luck!Decode Vishal's most recent message and see what it says!
print()

# we force and find the offset is 7 
for i in range(1,26):
  decodeMsg(" vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.", i)
  print()

decodeMsg("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.", 7)

def decodeMsgVigenere(message, keyword):
  keyMsg =""
  decodeMsg = ""
  keyword_index = 0

  for j in message:
    if keyword_index >= len(keyword):
      keyword_index = 0
    if j in alphabet:
      keyMsg += keyword[keyword_index]
      keyword_index += 1
    else:
      keyMsg += j
  
  for i in range(len(message)):
    if message[i] in alphabet:
      old_character_index = alphabet.index(message[i])
      offset_index = alphabet.index(keyMsg[i])
      new_character = alphabet[(old_character_index + offset_index) % 26]
      decodeMsg += new_character
    else:
      decodeMsg += message[i]
  return decodeMsg

print(decodeMsgVigenere("txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!", "friends"))
print()

def encodeMsgVigenere(message, keyword):
  keyMsg =""
  decodeMsg = ""
  keyword_index = 0

  for j in message:
    if keyword_index >= len(keyword):
      keyword_index = 0
    if j in alphabet:
      keyMsg += keyword[keyword_index]
      keyword_index += 1
    else:
      keyMsg += j
  
  for i in range(len(message)):
    if message[i] in alphabet:
      old_character_index = alphabet.index(message[i])
      offset_index = alphabet.index(keyMsg[i])
      new_character = alphabet[(old_character_index - offset_index) % 26]
      decodeMsg += new_character
    else:
      decodeMsg += message[i]
  return decodeMsg

print(encodeMsgVigenere("you were able to decode this? nice work! you are becoming quite the expert at crytography!", "friends"))
