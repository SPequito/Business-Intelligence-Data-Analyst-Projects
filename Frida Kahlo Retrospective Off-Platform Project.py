paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']

dates = [1939, 1933, 1946, 1940]

paintings = list(zip(paintings, dates))

print(paintings)
print()
#i can use paintings.apppend(("name", data ))
new_paintings = [["The Broken Column",1944],['The Wounded Deer',1946],['Me and My Doll',1937]]

paintings = paintings + new_paintings

print(paintings)
print()

paintings_len = len(paintings)
print(paintings_len)
print()

#for i in range(paintings_len):
 #audio_tour_number = paintings[i] 
 #print(audio_tour_number)
 #master_list = list(zip(audio_tour_number,audio_tour_number))
 #print(master_list)

audio_tour_number = list(range(1,8))
print(audio_tour_number) 
master_list = list(zip(audio_tour_number,paintings))
print(master_list)