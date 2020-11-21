## Dokumenrace k programu
Program má za úkol umět nakreslit alespoň jedno z každé kategorie zobrazení a vypočítat kde se v něm nachází hledané body.

### Funkce programu
Program se zeptá na vstupní zobrazení, k dispozici jsou Lambertovo válcové (`Lv`) , Marinovo válcové (`Ma`), Lambertovo azimutální (`La`), Postelovo azimutální (`Po`),
Ptolemáiovo kuželové (`Pt`) a Sansonovo nepravé (`Sa`), na měřítko a na to, po kolika stupnich se mají
vykreslovat poledníky a rovnoběžky. Když dané zobrazení není podporováno, program skončí.
U zobrazení `Pt` se program ještě navrch zeptá na tečnou rovnoběžku, která je potřeba k výpočtu a určuje velikost výseče mapy.
Dále se program zeptá na poloměr Země, když je 0, tak se počítá se zadaným (6371,11 km).

Program obsahuje funkce pro 6 zobrazení. 2 válcová, 2 azimutální, 1 kuželové a jedno nepravé. 
Funkce zobrazení využívají pro rovnoběžky i pro poledníky podobné forcykly. Vstupní argumenty jsou `r1`, což je poloměr země zahrnující
měřítko a přepočet na pixely, ve kterých želví funkce operují, `poled` a `rovn`, což jsou proměnné, které nesou informace o kroku pro focykly a tím
zajišťují po kolika stupních se budou vykreslovat. U Kuželového zobrazení je navíc ještě vstupní proměnná `fi0`, která udává dotekovou rovnoběžku.

Válcová zobrazení mají jen 2 forcykly. Jeden k poledníkům a druhý k rovnoběžkám, kde se pomocí funkce setpos přesouvá želva na začátek kreslené linie a pomocí druhé setpos na konec kreslené linie. Tím se vytvoří síť. Pro druhé válcové zobrazení je jen vyměněn vzorec.

Azimutální zobrazení mají opět 2 forcykly. Rovnoběžky jsou zde kružnice a forcyklus zajišťuje jejich vykreslení ve správné poloze. Ve středu je severní pól
a na okraji pól jižní. Poledníky se zde vykreslují jako rovné čáry ze středu ven. Pro jejich kreselní se želva vždy jen otočí o daný úhle a posune se o maximální vzdálenost.
Nakonec se vrátí zpět do středu.

Kuželové zobrazení narozdíl od ostatních má vstupní parametr navíc, ze kterého se vypočte `n`. To nám dává velikost kruhové výseče. Rovnoběžky se zde kreslí po polovinách,
kvůli kruhovým výsečím, aby byly ve středu. Poledníky se zde vykreslují podobně jako u azimutálních zobrazení, jen úhel je opět zmenšen o `n`.

Poslední zobrazení je nepravé. To pro výpočet poledníků používá 2 proměnné, jak zeměpisnou šířku, tak i délku. Proto zde musí být dvojnásovný forcyklus. Vnořený cyklus má nastavený pevný krok,
který zajišťuje hladkost linie (kolika body bude lomená čára procházet). Rovnoběžky se zde vytvoří zase pomocí funkce setpos.

Na konci každá funkce pro zobrazení odkáže na jinou funkci body(), která se zeptá uživatele na počítané body. Tato funkce se pak dokola spouští, dokud nejsou
body (0,0), poté se program ukončí. Spouští se zde ještě funkce kartez() a polar(), které mají za úkol jen vracet hodnotu vypočtených bodů v daném formátu.
