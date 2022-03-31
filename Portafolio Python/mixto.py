class Metodosa1:
    from ast import pattern
    from mimetypes import init


    def OrdenarNumeros():
     print("Ingresar 3 Valores")
     Numero=[]
     Numero.append(input("Numero 1: \n"))
     Numero.append(input("Numero 2: \n"))
     Numero.append(input("Numero 3: \n"))
     Numero.sort()
     print("La Lista se ha ordenado felicidades")
     print("Numero Menor: "+Numero[0]+"\n Numero Mediano: "+Numero[1]+"\n Numero Mayor: "+Numero[2])


     
    def Diamante():
        side = 7
        height =list(range(side))+ list(reversed(range(side-1)))
        pattern = '{: <{space}}{:+<{val}}'
        for x in height:
            a =side -x -1
            b=x*2+1
            print(pattern.format('', '',space=a,val=b))
    
        
    def DescargarVideo():
        from pytube import YouTube
        link =(input("Ingresa el link: \n"))
        yt=YouTube(link)
        yt.streams.filter(only_audio=True)
        stream = yt.streams.get_by_itag(251)
        stream.download()
        return("Descargardo")


    print ("--------------------Selecciona alguno de estos programas---------------------")
    print("°1 Determinar el numero Mayor , Mediano y Menor de valores Capturados")
    print("°2 figura de diamante +")
    print("°3 Descargar un video de Youtube ") 
    Seleccion=(input("\n"))

    if Seleccion=="1":
     OrdenarNumeros()
    elif Seleccion=="2": 
     Diamante()
    elif Seleccion=="3":
      DescargarVideo()
        

