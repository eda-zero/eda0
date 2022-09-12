import schemdraw
import schemdraw.elements as elm
from schemdraw import logic
from schemdraw.parsing import logicparse

with schemdraw.Drawing() as d:
    d.config(unit=0.5)
    d += (S := logic.Xor().label('S', 'right'))
    d += logic.Line().left(d.unit*2).at(S.in1).idot().label('A', 'left')
    d += (B := logic.Line().left().at(S.in2).dot())
    d += logic.Line().left().label('B', 'left')
    d += logic.Line().down(d.unit*3).at(S.in1)
    d += (C := logic.And().right().anchor('in1').label('C', 'right'))
    d += logic.Wire('|-').at(B.end).to(C.in2)
    
# d += logicparse('not ((w and x) or (y and z))', outlabel='$\overline{Q}$')

d.draw()
d.save('logic1.svg')
