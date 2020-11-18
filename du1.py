from turtle import forward, exitonclick, left, right, setpos, circle, penup, pendown, speed
import math

def Lv(r1,poled,rovn): #lambertovo zobrazeni valcove
    # x=r*arc(lambda) > x=r1*v*math.pi/180
    # y=r*sin(fi) > y=r1*math.sin(math.radians(u))
    for v in range(-180,181,poled):
        x=r1*v*math.pi/180
        penup()
        setpos(x,r1*math.sin(math.radians(-90))) #presune zelvu na polednik (x) a na jizni pol
        pendown()
        setpos(x,r1*math.sin(math.radians(90))) #úresune zelvu na polednik (x) a na severni pol, nakreslí se polednik x
    
    for u in range(-90,91,rovn):
        y=r1*math.sin(math.radians(u))
        penup()
        setpos(r1*(-180)*math.pi/180,y) #presune zelvu na rovnobezku (y) a na poledník -180
        pendown()
        setpos(r1*180*math.pi/180,y) #presune zelvu na rovnobezku y a na polednik 180, nakresli se rovnobezka y
    
    xy=body() #nahravani vice bodu nez jednoho dokud se nezada (0,0)
    while xy !=(0,0): 
        x1=xy[0]
        y1=xy[1]
        x_vyst=r1*0.3*x1*math.pi/180 #vypocet souradnic bodu v mm
        y_vyst=r1*0.3*math.sin(math.radians(y1))
        kartez(x_vyst,y_vyst)
        xy=body()
    exitonclick()
    pass

def Ma(r1,poled,rovn): #Marinovo zobrazeni valcove
    # x=r*arc(lambda) > x=r1*v*math.pi/180
    # y=r*arc(fi) > y=r1*u*math.pi/180
    for v in range(-180,181,poled):
        x=r1*v*math.pi/180
        penup()
        setpos(x,r1*(-90)*math.pi/180) #presune zelvu na polednik (x) a na jizni pol
        pendown()
        setpos(x,r1*(90)*math.pi/180) #úresune zelvu na polednik (x) a na severni pol, nakreslí se polednik x
    
    for u in range(-90,91,rovn):
        y=r1*u*math.pi/180
        penup()
        setpos(r1*(-180)*math.pi/180,y) #presune zelvu na rovnobezku (y) a na poledník -180
        pendown()
        setpos(r1*(180)*math.pi/180,y) #presune zelvu na rovnobezku y a na polednik 180, nakresli se rovnobezka y
    
    xy=body() #nahravani vice bodu nez jednoho dokud se nezada (0,0)
    while xy !=(0,0): 
        x1=xy[0]
        y1=xy[1]
        x_vyst=r1*0.3*x1*math.pi/180 #vypocet souradnic bodu v mm
        y_vyst=r1*0.3*y1*math.pi/180
        kartez(x_vyst,y_vyst)
        xy=body()
    exitonclick()
    pass

def Po(r1,poled,rovn): #Postelovo zobrazeni azimutalni, je v polarnich souradnicich (ro,epsilon)
    #ro=r*arc(delta), delta=90-fi > ro=r1*(90-u)*math.pi/180
    #eps=lambda > eps=v
    
    for u in range(-90,90,rovn):
        ro=r1*(90-u)*math.pi/180 
        penup()
        setpos(0,-ro) #posune zelvu na severni pol(zobrazeni je v normálni poloze)
        pendown()
        circle(ro)
    
    for v in range(-180,181,poled): #promenou v nepotrebujeme, jen chceme aby se cyklus opakoval podle poctu poledniku
        penup()
        setpos(0,0)
        pendown()
        forward(r1*math.pi) #r1*(90-(-90))*pi/180= r1*pi
        left(poled)
    
    xy=body() #nahravani vice bodu nez jednoho dokud se nezada (0,0)
    while xy !=(0,0): 
        x1=xy[0]
        y1=xy[1]
        ro_vyst=r1*0.3*(90-y1)*math.pi/180 #vypocet souradnic bodu, ro je v mm eps je ve stupnich
        eps_vyst=x1
        polar(ro_vyst,eps_vyst)
        xy=body()
    exitonclick()

def La(r1,poled,rovn): #Lambertovo zobrazeni azimutalni, je v polarnich souradnicich (ro,epsilon)
    #ro=2r*sin(delta/2), delta=90-fi > 2*r1*math.sin(math.radians((90-u)/2))
    #eps=lambda > eps=v

    for u in range(-90,90,rovn):
        ro=2*r1*math.sin(math.radians((90-u)/2)) 
        penup()
        setpos(0,-ro) #posune zelvu na severni pol(zobrazeni je v normálni poloze)
        pendown()
        circle(ro)
    
    for v in range(-180,181,poled): #promenou v nepotrebujeme, jen chceme aby se cyklus opakoval podle poctu poledniku
        penup()
        setpos(0,0)
        pendown()
        forward(2*r1) #2*r1*sin((90+90)/2)-2*r1*sin((90-90)/2) = 2*r1
        left(poled)
    
    xy=body() #nahravani vice bodu nez jednoho dokud se nezada (0,0)
    while xy !=(0,0): 
        x1=xy[0]
        y1=xy[1]
        ro_vyst=2*r1*0.3*math.sin(math.radians((90-y1)/2)) #vypocet souradnic bodu, ro je v mm eps je ve stupnich
        eps_vyst=x1
        polar(ro_vyst,eps_vyst)
        xy=body()
    exitonclick()
    pass

def Pt(r1,fi0,poled,rovn): #Ptolemaiovo zobrazeni kuzelove delkojevne podle rovnobezky fi0
    #eps= n*lambda > eps=n*v , n je velikost vysece
    #ro= r* [tg(delta0)-arc(delta-delta0)], delta=90-fi, delta0=90-fi0 > ro=r1*(math.tan(math.radians(90-fi0))+(90-u-(90-fi0))*math.pi/180)
    #n= cos(delta0) > n=math.cos(math.radians(90-fi0))
    
    n=math.cos(math.radians(90-fi0))
    for u in range(-90,91,rovn):
        ro=r1*(math.tan(math.radians(90-fi0))+(90-u-(90-fi0))*math.pi/180)
        penup()
        setpos(0,-ro)
        pendown()
        circle(ro,360*n/2) #nakresli jen polovinu vysece
        penup()
        setpos(0,-ro)
        right(360*n/2)
        pendown()
        circle(ro,-360*n/2) #nakresli druho polovinu vysece
        left(360*n/2)
    
    left(-90+180*n) #vypocet otoceni zelvy, aby se kreslilo vzdy od okraje vysece v zavislosti na fi0 zadane pri vsupu
    
    for v in range(-180,181,poled): #promenou v nepotrebujeme, jen chceme aby se cyklus opakoval podle poctu poledniku
        penup()
        setpos(0,0)
        forward(r1*(math.tan(math.radians(90-fi0))+(-(90-fi0))*math.pi/180)) #za u dosadime 90, aby se kreslilo od prvni rovnobezky, pol u tohoto zobrazeni neni v pocatku
        pendown()
        forward(r1*(math.tan(math.radians(90-fi0))+(90+90-(90-fi0))*math.pi/180)-r1*(math.tan(math.radians(90-fi0))+(-(90-fi0))*math.pi/180)) #vzdalenost mezi rovnobezkou -90 a 90
        right(poled*n)

    xy=body() #nahravani vice bodu nez jednoho dokud se nezada (0,0)
    
    while xy !=(0,0): 
        x1=xy[0]
        y1=xy[1]
        eps_vyst=n*x1
        ro_vyst=r1*0.3*(math.tan(math.radians(90-fi0))+(90-y1-(90-fi0))*math.pi/180)
        polar(ro_vyst,eps_vyst)
        xy=body()
    exitonclick()
    pass

def Sa(r1,poled,rovn): #sansonovo nepravé zobrazení
    #x=r*arc(lambda)*cos(fi) > x=r1*v*math.pi/180*math.cos(math.radians(u))
    #y=r*arc(fi) > y=r1*u*math.pi/180
    for v in range(-180,181,poled):
        penup()
        setpos(0,r1*-90*math.pi/180)
        pendown()
        for i in range(-90,91,10): #x je zavysla i na fi, zde se da urcit lomenost car
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
    
    xy=body() #nahravani vice bodu nez jednoho dokud se nezada (0,0)
    while xy !=(0,0): 
        x1=xy[0]
        y1=xy[1]
        x_vyst=r1*0.3*x1*math.pi/180*math.cos(math.radians(y1)) #vypocet souradnic bodu v pixelech
        y_vyst=r1*0.3*y1*math.pi/180
        kartez(x_vyst,y_vyst)
        xy=body()
    exitonclick()
    pass


def kartez(x_vyst,y_vyst):
    return( print('x={:.4} mm a y= {:.4} mm'.format(x_vyst,y_vyst))) #vypuse zadaný bod v pixelech

def polar(ro_vyst,eps_vyst):
    return( print('ro={:.4} mm a epsilon= {:.4} stupňů'.format(ro_vyst,eps_vyst))) #vypuse zadaný bod v pixelech a uhlech, jsou to polarni souradnice

def body():
    x1=float(input('Zadejte hodnotou souradnice x ve formatu deg:'))
    y1=float(input('Zadejte hodnotou souradnice y ve formatu deg:'))
    
    return x1, y1



zobrazeni=input('Vyberte zobrazení (Lv,Ma,Po,La,Pt,Sa):') #vstupni parametry
meritko=int(input('Zadejte X pro určení měřítka (1:X)'))
r=float(input('Zadejte polomer Země v km:'))
rovn=int(input('Zadejte po kolika stupnich se vykresli rovnobezeky:'))
poled=int(input('Zadejte po kolika stupnich se vykresli poledniky:'))

if r==0:
    r=6371.11
r1=r*10**6/meritko/0.3 #polomer z km na mm a ty pak na pixely
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
    while fi0 == 0:
        print('Kuželove zobrazeni neni definovano pro fi0=0')
        fi0=abs(float(input('Zadejte tečnou rovnoběžku fi0():')))
    Pt(r1,fi0,poled,rovn)
elif zobrazeni=='Sa':
    Sa(r1,poled,rovn)
else:
    print(f'zobrazení "{zobrazeni}" není definováno')




