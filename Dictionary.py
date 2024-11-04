#keys values
Aot ={
    'Tone':'Action',
    'Episodes':104,
    'Main':'Eren'
}
Frieren={
    'Tone':'Fantasy',
    'Episodes':23,
    'Main':'Fern'
}
#add
Aot['Second']='Mikasa'
Aot.update({'Third':'Armin'})
#copy
Copy_Frieren = Frieren.copy()
for a,b in Frieren.items():
    print(a,'=',b)
#remove
Aot.pop('Tone')
#show
for i,j in Aot.items():
    print(i,'=',j)

    