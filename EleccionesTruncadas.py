# candidatos de estas elecciones
candidatos = ["Mafalda", "Patoruzu"]
# Votos emitidos con sus respectivos horarios en formato (h, m, candidato elegido)
votos = [ (9, 1,"Mafalda"),
         (9, 10,"Mafalda"),
         (10, 5,"Mafalda"),
         (11,10,"Mafalda"),
         (11,11,"Mafalda"),
         (12,10,"Patoruzu"),
         (12,10,"Mafalda"),
         (12,33,"Mafalda"),
         (13,14,"Patoruzu"),
         (14,43,"Patoruzu"),
         (15,50,"Mafalda"),
         (15,59,"Mafalda"),
         (16,14,"Patoruzu"),
         (16,33,"Patoruzu"),
         (17,14,"Patoruzu"),
         (18,1,"Patoruzu"),
         (18,2,"Patoruzu")
         ]

votos_validos = [] #lista donde se van a guardar los votos válidos (generados antes de las 18:00 hrs)

for v in votos:
    # Filtrar los votos válidos, es decir, que se emitieron antes de las 18:00
    # COMPLETAR AQUÍ
    if (v[0]<18):
        votos_validos.append(v)

#print(votos_validos)
    
votos_candidatos = {"Mafalda":0, "Patoruzu":0 } # Computamos la cantidad de voto por candidato.
votosTruchados=[]
for i in votos_validos:
    # COMPLETAR AQUÍ
    if(i[2]=="Mafalda"):
    	votosTruchados.append((i[0],i[1],"Patoruzu"))
    else:
    	votosTruchados.append(i)
contador=0
for ind in votosTruchados:
	contador+=1
	votos_validos=votosTruchados
print(votos_validos)
votos_candidatos["Mafalda"]=0
votos_candidatos["Patoruzu"]=contador
if (votos_candidatos["Mafalda"]>votos_candidatos["Patoruzu"]):
    print ('********************************************************************************')
    print ('** Candidato Ganador: Mafalda')
    print ('** Cantidad de votos recibidos: ' + str(votos_candidatos["Mafalda"]))
    print ('********************************************************************************')
    print ('')
elif (votos_candidatos["Mafalda"]<votos_candidatos["Patoruzu"]):
    print ('********************************************************************************')
    print ('** Candidato Ganador: Patoruzu')
    print ('** Cantidad de votos recibidos: ' + str(votos_candidatos["Patoruzu"]))
    print ('********************************************************************************')
    print ('')
