from matrix_instant import *
import LED_display_instant as LMD
import threading
from random import *

def LED_init():
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return
arrayBlk = [ [ 1 ] ]
ghost = [ [ 3 ] ]
ghost2 = [ [ 3 ] ]
ghost3 = [ [ 3 ] ]
ghost4 = [ [ 3 ] ]


def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()-4):
        for x in range(4, m.get_dx()-4):
            if array[y][x] == 0:
                LMD.set_pixel(y, 19-x, 0)
            elif array[y][x] == 2:
                LMD.set_pixel(y, 19-x, 4)
            elif array[y][x] == 1: 
                LMD.set_pixel(y, 19-x, 3)
            elif array[y][x] == 3:
                LMD.set_pixel(y, 19-x, 1)
            else:
                continue
        print()


###
### initialize variables
###     



### integer variables: must always be integer!
iScreenDy = 32
iScreenDx = 16
iScreenDw = 4
top = 16
left = iScreenDw + iScreenDx//2 - 1

top_G = 24
left_G = iScreenDw + iScreenDx//2 - 8

top_G2 = 8
left_G2 = iScreenDw + iScreenDx//2 - 8

top_G3 = 24
left_G3 = iScreenDw + iScreenDx//2 + 6

top_G4 = 8
left_G4 = iScreenDw + iScreenDx//2 + 6




arrayScreen = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 0, 2, 2, 0, 2, 0, 2, 2, 2, 0, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 2, 2, 2, 0, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 2, 0, 2, 0, 2, 0, 2, 2, 2, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2 ],
    [ 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]]


iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
currBlk = Matrix(arrayBlk)
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)

currGho = Matrix(ghost)
tempGho = iScreen.clip(top_G, left_G, top_G+currGho.get_dy(), left_G+currGho.get_dx())
tempGho = tempGho + currGho
oScreen.paste(tempGho, top_G, left_G)

currGho2 = Matrix(ghost2)
tempGho2 = iScreen.clip(top_G2, left_G2, top_G2+currGho2.get_dy(), left_G2+currGho2.get_dx())
tempGho2 = tempGho2 + currGho2
oScreen.paste(tempGho2, top_G2, left_G2)

currGho3 = Matrix(ghost3)
tempGho3 = iScreen.clip(top_G3, left_G3, top_G3+currGho3.get_dy(), left_G3+currGho3.get_dx())
tempGho3 = tempGho3 + currGho3
oScreen.paste(tempGho3, top_G3, left_G3)

currGho4 = Matrix(ghost4)
tempGho4 = iScreen.clip(top_G4, left_G4, top_G4+currGho4.get_dy(), left_G4+currGho4.get_dx())
tempGho4 = tempGho4 + currGho4
oScreen.paste(tempGho4, top_G4, left_G4)
oScreen.paste(tempGho, top_G, left_G)

LED_init()
draw_matrix(oScreen); print()

    
    
tempGho = iScreen.clip(top_G, left_G, top_G+currGho.get_dy(), left_G+currGho.get_dx())
tempGho = tempGho + currGho

tempGho2 = iScreen.clip(top_G2, left_G2, top_G2+currGho2.get_dy(), left_G2+currGho.get_dx())
tempGho2 = tempGho2 + currGho2

tempGho3 = iScreen.clip(top_G3, left_G3, top_G3+currGho3.get_dy(), left_G3+currGho3.get_dx())
tempGho3 = tempGho3 + currGho3

tempGho4 = iScreen.clip(top_G4, left_G4, top_G4+currGho4.get_dy(), left_G4+currGho4.get_dx())
tempGho4 = tempGho4 + currGho4

score =0

while True:
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a': # move left
        left -= 1
        
    elif key == 'd': # move right
        left += 1
    elif key == 's': # move down
        top += 1
    elif key == 'w': # move up
        top -= 1
    elif key == ' ': # drop the block
        print('Not implemented')
        continue
    else:
        print('Wrong key!!!')
        continue
      
    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    
    if tempBlk.anyGreaterThan(2):
        if key == 'a': # undo: move right
            left += 1
        elif key == 'd': # undo: move left
            left -= 1
        elif key == 's': # undo: move up
            top -= 1
#             newBlockNeeded = True
        elif key == 'w': # undo: move down
            top += 1
        elif key == ' ': # undo: move up
            print('Not implemented')
        
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
    
    if (top == top_G) & (left == left_G):
        print('GG')
        print("score: ",score)
        break
    elif (top == top_G2) & (left == left_G2):
        print('GG')
        print("score: ",score)
        break
    elif (top == top_G3) & (left == left_G3):
        print('GG')
        print("score: ",score)
        break
    elif (top == top_G4) & (left == left_G4):
        print('GG')
        print("score: ",score)
        break
    
    tap = 0
    if tap == 0:
        tap += 1
    if tap == 1:
        i = randint(1,4)
        o = randint(1,4)
        p = randint(1,4)
        q = randint(1,4)
        if i == 1:
            left_G -= 1
        elif i == 2:
            left_G += 1
        elif i == 3:
            top_G += 1
        elif i == 4:
            top_G -= 1
        tempGho = iScreen.clip(top_G, left_G, top_G+currGho.get_dy(), left_G+currGho.get_dx())
        tempGho = tempGho + currGho
        if tempGho.anyGreaterThan(3):
            if i == 1:
                left_G += 1
            if i == 2:
                left_G -= 1
            if i == 3:
                top_G -= 1
            if i == 4:
                top_G += 1
        tempGho = iScreen.clip(top_G, left_G, top_G+currGho.get_dy(), left_G+currGho.get_dx())
        tempGho = tempGho + currGho
        
        if o == 1:
            left_G2 -= 1
        elif o == 2:
            left_G2 += 1
        elif o == 3:
            top_G2 += 1
        elif o == 4:
            top_G2 -= 1
        tempGho2 = iScreen.clip(top_G2, left_G2, top_G2+currGho2.get_dy(), left_G2+currGho2.get_dx())
        tempGho2 = tempGho2 + currGho2
        
        if tempGho2.anyGreaterThan(3):
            if o == 1:
                left_G2 += 1
            if o == 2:
                left_G2 -= 1
            if o == 3:
                top_G2 -= 1
            if o == 4:
                top_G2 += 1
        tempGho2 = iScreen.clip(top_G2, left_G2, top_G2+currGho2.get_dy(), left_G2+currGho2.get_dx())
        tempGho2 = tempGho2 + currGho2

        if p == 1:
            left_G3 -= 1
        elif p == 2:
            left_G3 += 1
        elif p == 3:
            top_G3 += 1
        elif p == 4:
            top_G3 -= 1
        tempGho3 = iScreen.clip(top_G3, left_G3, top_G3+currGho3.get_dy(), left_G3+currGho3.get_dx())
        tempGho3 = tempGho3 + currGho3
        if tempGho3.anyGreaterThan(3):
            if p == 1:
                left_G3 += 1
            if p == 2:
                left_G3 -= 1
            if p == 3:
                top_G3 -= 1
            if p == 4:
                top_G3 += 1
        tempGho3 = iScreen.clip(top_G3, left_G3, top_G3+currGho3.get_dy(), left_G3+currGho3.get_dx())
        tempGho3 = tempGho3 + currGho3
        
        if q == 1:
            left_G4 -= 1
        elif q == 2:
            left_G4 += 1
        elif q == 3:
            top_G4 += 1
        elif q == 4:
            top_G4 -= 1
        tempGho4 = iScreen.clip(top_G4, left_G4, top_G4+currGho4.get_dy(), left_G4+currGho4.get_dx())
        tempGho4 = tempGho4 + currGho4
        if tempGho4.anyGreaterThan(3):
            if q == 1:
                left_G4 += 1
            if q == 2:
                left_G4 -= 1
            if q == 3:
                top_G4 -= 1
            if q == 4:
                top_G4 += 1
        tempGho4 = iScreen.clip(top_G4, left_G4, top_G4+currGho4.get_dy(), left_G4+currGho4.get_dx())
        tempGho4 = tempGho4 + currGho4
        
        tap = 0


    score += 1
    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    oScreen.paste(tempGho, top_G, left_G)
    oScreen.paste(tempGho2, top_G2, left_G2)
    oScreen.paste(tempGho3, top_G3, left_G3)
    oScreen.paste(tempGho4, top_G4, left_G4)
    draw_matrix(oScreen); print()
    