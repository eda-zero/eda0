from chips import *
from gateLib import *

a = "_"; b= "_"; c="_"; d="_"; e="_"; f="_"; g="_"; h="_"

gateLib1 = {
"NOT"    :[2, Not(a)],
"NAND"   :[3, Nand(a,b)],
"NAND3"  :[4, Nand(Not(Nand(a,b)),c)],
"NAND4"  :[5, Nand(Not(Nand(Not(Nand(a,b)),c)),d),
              Nand(Not(Nand(a,b)),Not(Nand(c,d)))],
"AOI21"  :[4, Not(Nand(Nand(a,b),Not(c)))],
"AOI22"  :[5, Not(Nand(Nand(a,b),Nand(c,d)))]
}

if __name__ == '__main__':
    glib = GateLib(gateLib1)
    glib.dump()
    print('NAND=', glib.findByName('NAND'))
    print('NAND4=', glib.findByName('NAND4'))
    print('not(_)=', glib.findByExp('not(_)'))
    print('nand(not(nand(not(nand(_,_)),_)),_)=', glib.findByExp('nand(not(nand(not(nand(_,_)),_)),_)'))
    print('exp:xxx=', glib.findByExp('exp:xxx'))
    print('name:xxx=', glib.findByName('name:xxx'))

