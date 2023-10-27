meme_dict = {
    'CRINGE': 'Pena Ajena',
    'LOL': 'Una respuesta común a algo gracioso',
    'ROLF': 'Una respuesta a una broma',
    'SHEESH': 'Ligera Desaprobación',
    'CREEPY': 'Aterrador, Siniestro',
    'AGGRO': 'Ponerse agresivo/enojado'
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])

else:
    # ¿Qué hacer si no se encuentra la palabra?
    print('Tu palabra no está, lo siento')