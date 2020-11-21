from turtle import forward, exitonclick, left, right, setpos, circle, penup, pendown, speed
import math

def Lv(r1,poled,rovn): #lambertovo zobrazení válcové
    # x=r*arc(lambda) > x=r1*v*math.pi/180
    # y=r*sin(fi) > y=r1*math.sin(math.radians(u))
    for v in range(-180,181,poled):
        x=r1*v*math.pi/180
        penup()
        setpos(x,r1*math.sin(math.radians(-90))) #přesune želvu na poledník (x) a na jižní pól
        pendown()
        setpos(x,r1*math.sin(math.radians(90))) #přesune želvu na poledník (x) a na severní pól, nakreslí se poledník x
    
    for u in range(-90,91,rovn):
        y=r1*math.sin(math.radians(u))
        penup()
        setpos(r1*(-180)*math.pi/180,y) #přesune želvu na rovnoběžku (y) a na poledník -180
        pendown()
        setpos(r1*180*math.pi/180,y) #přesune želvu na rovnoběžku y a na poledník 180, nakresli se rovnoběžka y
    
    xy=body() #nahrávání více bodů než jednoho dokud se nezadá (0,0)
    while xy !=(0,0): 
        x1=xy[0]
        y1=xy[1]
        x_vyst=r1*0.3*x1*math.pi/180 #výpočet souřadnic bodu v mm
        y_vyst=r1*0.3*math.sin(math.radians(y1))
        kartez(x_vyst,y_vyst)
        xy=body()

def Ma(r1,poled,rovn): #Marinovo zobrazení válcové
    # x=r*arc(lambda) > x=r1*v*math.pi/180
    # y=r*arc(fi) > y=r1*u*math.pi/180
    for v in range(-180,181,poled):
        x=r1*v*math.pi/180
        penup()
        setpos(x,r1*(-90)*math.pi/180) #přesune želvu na poledník (x) a na jižní pól
        pendown()
        setpos(x,r1*(90)*math.pi/180) #přesune želvu na poledník (x) a na severní pól, nakreslí se poledník x
    
    for u in range(-90,91,rovn):
        y=r1*u*math.pi/180
        penup()
        setpos(r1*(-180)*math.pi/180,y)  #přesune želvu na rovnoběžku (y) a na poledník -180
        pendown()
        setpos(r1*(180)*math.pi/180,y) #přesune želvu na rovnoběžku y a na poledník 180, nakresli se rovnoběžka y
    
    xy=body() #nahrávání více bodů než jednoho dokud se nezadá (0,0)
    while xy !=(0,0): 
        x1=xy[0]
        y1=xy[1]
        x_vyst=r1*0.3*x1*math.pi/180
        y_vyst=r1*0.3*y1*math.pi/180
        kartez(x_vyst,y_vyst)
        xy=body()

def Po(r1,poled,rovn): #Postelovo zobrazení azimutaální, je v polárních souřadnicích (ro,epsilon)
    #ro=r*arc(delta), delta=90-fi > ro=r1*(90-u)*math.pi/180
    #eps=lambda > eps=v
    
    for u in range(-90,90,rovn):
        ro=r1*(90-u)*math.pi/180 
        penup()
        setpos(0,-ro) #posune želvu na severní pól(zobrazení je v normální poloze)
        pendown()
        circle(ro)
    
    for _ in range(-180,181,poled):
        setpos(0,0)
        pendown()
        forward(r1*math.pi) #r1*(90-(-90))*pi/180= r1*pi
        left(poled)
    
    xy=body() #nahrávání více bodů než jednoho dokud se nezadá (0,0)
    while xy !=(0,0): 
        x1=xy[0]
        y1=xy[1]
        ro_vyst=r1*0.3*(90-y1)*math.pi/180 #výpočet souřadnic bodů, ro je v mm eps je ve stupních
        eps_vyst=x1
        polar(ro_vyst,eps_vyst)

def La(r1,poled,rovn): #Lambertovo zobrazení azimutalní, je v polarních souřadnicích (ro,epsilon)
    #ro=2r*sin(delta/2), delta=90-fi > 2*r1*math.sin(math.radians((90-u)/2))
    #eps=lambda > eps=v

    for u in range(-90,90,rovn):
        ro=2*r1*math.sin(math.radians((90-u)/2)) 
        penup()
        setpos(0,-ro) #posune želvu na severní pól(zobrazení je v normální poloze)
        pendown()
        circle(ro)
    
    for _ in range(-180,181,poled):
        penup()
        setpos(0,0)
        pendown()
        forward(2*r1) #2*r1*sin((90+90)/2)-2*r1*sin((90-90)/2) = 2*r1
        left(poled)
    
    xy=body() #nahrávání více bodů než jednoho dokud se nezadá (0,0)
    while xy !=(0,0): 
        x1=xy[0]
        y1=xy[1]
        ro_vyst=2*r1*0.3*math.sin(math.radians((90-y1)/2))
        eps_vyst=x1
        polar(ro_vyst,eps_vyst)
        xy=body()

def Pt(r1,fi0,poled,rovn): #Ptolemaiovo zobrazení kuželové délkojevné podle rovnoběžky fi0
    #eps= n*lambda > eps=n*v , n je velikost výseče
    #ro= r* [tg(delta0)-arc(delta-delta0)], delta=90-fi, delta0=90-fi0 > ro=r1*(math.tan(math.radians(90-fi0))+(90-u-(90-fi0))*math.pi/180)
    #n= cos(delta0) > n=math.cos(math.radians(90-fi0))
    
    n=math.cos(math.radians(90-fi0))
    for u in range(-90,91,rovn):
        ro=r1*(math.tan(math.radians(90-fi0))+(90-u-(90-fi0))*math.pi/180)
        penup()
        setpos(0,-ro)
        pendown()
        circle(ro,360*n/2) #nakreslí jen polovinu výseče
        penup()
        setpos(0,-ro)
        right(360*n/2)
        pendown()
        circle(ro,-360*n/2) #nakreslí druho polovinu výseče
        left(360*n/2)
    
    left(-90+180*n) #výpočet otočení želvy, aby se kreslilo vždy od okraje výseče v zavislosti na fi0 zadaného při vsupu
    
    for _ in range(-180,181,poled):
        penup()
        setpos(0,0)
        forward(r1*(math.tan(math.radians(90-fi0))+(-(90-fi0))*math.pi/180)) #za u dosadíme 90, aby se kreslilo od první rovnoběžky, pól u tohoto zobrazení není v počátku
        pendown()
        forward(r1*(math.tan(math.radians(90-fi0))+(90+90-(90-fi0))*math.pi/180)-r1*(math.tan(math.radians(90-fi0))+(-(90-fi0))*math.pi/180)) #vzdálenost mezi rovnoběžkou -90 a 90
        right(poled*n)

    xy=body()
    
    while xy !=(0,0): 
        x1=xy[0]
        y1=xy[1]
        eps_vyst=n*x1
        ro_vyst=r1*0.3*(math.tan(math.radians(90-fi0))+(90-y1-(90-fi0))*math.pi/180)
        polar(ro_vyst,eps_vyst)
        xy=body()

def Sa(r1,poled,rovn): #Sansonovo nepravé zobrazení
    #x=r*arc(lambda)*cos(fi) > x=r1*v*math.pi/180*math.cos(math.radians(u))
    #y=r*arc(fi) > y=r1*u*math.pi/180
    for v in range(-180,181,poled):
        penup()
        setpos(0,r1*-90*math.pi/180)
        pendown()
        for i in range(-90,91,10): #x je závislá i na fi
            x=r1*v*math.pi/180*math.cos(math.radians(i))
            y=r1*i*math.pi/180
            setpos(x,y)

    for u in range(-90,91,rovn):
        x=r1*-180*math.pi/180*math.cos(math.radians(u))
        y=r1*u*math.pi/180
        penup()
        setpos(x,y)
        pendown()
        x=r1*180*math.pi/180*math.cos(math.radians(u))
        setpos(x,y)
    
    xy=body() 
    while xy !=(0,0): 
        x1=xy[0]
        y1=xy[1]
        x_vyst=r1*0.3*x1*math.pi/180*math.cos(math.radians(y1)) #výpočet souřadnic bodu v pixelech
        y_vyst=r1*0.3*y1*math.pi/180
        kartez(x_vyst,y_vyst)
        xy=body()

def kartez(x_vyst,y_vyst):
    return( print('x={:.4} mm a y= {:.4} mm'.format(x_vyst,y_vyst))) #vypíše zadaný bod v pixelech

def polar(ro_vyst,eps_vyst):
    return( print('ro={:.4} mm a epsilon= {:.4} stupňů'.format(ro_vyst,eps_vyst))) #vypíše zadaný bod v pixelech a úhlech, jsou to polární souřadnice

def body():
    x1=float(input('Zadejte hodnotou souradnice x ve formatu deg:'))
    y1=float(input('Zadejte hodnotou souradnice y ve formatu deg:'))
    if x1 <-180 or\
        x1 >180 or\
        y1 <-90 or\
        y1 >90:
        print('Bod se nachází mimo zeměpisnou síť')
        exit()
    return x1, y1



zobrazeni=input('Vyberte zobrazení (Lv,Ma,Po,La,Pt,Sa):') #vstupní parametry
meritko=int(input('Zadejte X pro určení měřítka (1:X)'))
r=float(input('Zadejte polomer Země v km:'))
rovn=int(input('Zadejte po kolika stupnich se vykresli rovnobezeky:'))
poled=int(input('Zadejte po kolika stupnich se vykresli poledniky:'))

#kontrola vstupů

if rovn <= 0 or \
    rovn > 90:
    print(f'Nelze rovnoběžky vykreslit po {rovn} stupních')
    exit()
if poled <= 0 or \
    poled > 360:
    print(f'Nelze poledníky vykreslit po {poled} stupních')
    exit()
if r < 0:
    print('Měřítko musí být nezáporné')
    exit()
if r==0:
    r=6371.11
if meritko <=0:
    print('Měřítko musí být kladné číslo')
    exit()

r1=r*10**6/meritko/0.3 #poloměr z km na mm a ty pak na pixely
speed(0)
 
if zobrazeni == 'Lv': #konrtola a vstup zobrazení
    Lv(r1,poled,rovn)
elif zobrazeni=='Ma':
    Ma(r1,poled,rovn)
elif zobrazeni=='Po':
    Po(r1,poled,rovn)
elif zobrazeni=='La':
    La(r1,poled,rovn)
elif zobrazeni=='Pt':
    fi0=abs(float(input('Zadejte tečnou rovnoběžku fi0():')))
    while fi0 == 0 or fi0>90:
        print(f'Kuželove zobrazeni neni definovano pro {fi0}')
        fi0=abs(float(input('Zadejte tečnou rovnoběžku fi0():')))
    Pt(r1,fi0,poled,rovn)
elif zobrazeni=='Sa':
    Sa(r1,poled,rovn)
else:
    print(f'zobrazení "{zobrazeni}" není definováno')
exitonclick()


