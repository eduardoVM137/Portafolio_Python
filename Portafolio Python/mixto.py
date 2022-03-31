class Metodosa1:
    from ast import pattern
    from mimetypes import init


    def Prueba(self):
     print("uwuwuuw") 
     
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
        link ="https://www.youtube.com/watch?v=5qm8PH4xAss"
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
     print(Prueba())
    elif Seleccion=="2": 
        print(Diamante())
    elif Seleccion=="3":
        print(DescargarVideo(2))
        

