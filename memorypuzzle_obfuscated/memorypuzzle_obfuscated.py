import random, pygame, sys
from pygame.locals import *
def hhh():
    global a, b
    pygame.init()
    a = pygame.time.Clock()
    b = pygame.display.set_mode((640, 480))
    j = 0
    k = 0
    pygame.display.set_caption('Memory Game')
    i = c()
    hh = d(False)
    h = None
    b.fill((60, 60, 100))
    g(i)
    while True:
        e = False
        b.fill((60, 60, 100))
        f(i, hh)
        for eee in pygame.event.get():
            if eee.type == QUIT or (eee.type == KEYUP and eee.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif eee.type == MOUSEMOTION:
                j, k = eee.pos
            elif eee.type == MOUSEBUTTONUP:
                j, k = eee.pos
                e = True
        bb, ee = m(j, k)
        if bb != None and ee != None:
            if not hh[bb][ee]:
                n(bb, ee)
            if not hh[bb][ee] and e:
                o(i, [(bb, ee)])
                hh[bb][ee] = True
                if h == None:
                    h = (bb, ee)
                else:
                    q, fff = s(i, h[0], h[1])
                    r, ggg = s(i, bb, ee)
                    if q != r or fff != ggg:
                        pygame.time.wait(1000)
                        p(i, [(h[0], h[1]), (bb, ee)])
                        hh[h[0]][h[1]] = False
                        hh[bb][ee] = False
                    elif ii(hh):
                        jj(i)
                        pygame.time.wait(2000)
                        i = c()
                        hh = d(False)
                        f(i, hh)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        g(i)
                    h = None
        pygame.display.update()
        a.tick(30)
def d(ccc):
    hh = []
    for i in range(10):
        hh.append([ccc] * 7)
    return hh
def c():
    rr = []
    for tt in ((255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 128, 0), (255, 0, 255), (0, 255, 255)):
        for ss in ('a', 'b', 'c', 'd', 'e'):
            rr.append( (ss, tt) )
    random.shuffle(rr)
    rr = rr[:35] * 2
    random.shuffle(rr)
    bbb = []
    for x in range(10):
        v = []
        for y in range(7):
            v.append(rr[0])
            del rr[0]
        bbb.append(v)
    return bbb
def t(vv, uu):
    ww = []
    for i in range(0, len(uu), vv):
        ww.append(uu[i:i + vv])
    return ww
def aa(bb, ee):
    return (bb * 50 + 70, ee * 50 + 65)
def m(x, y):
    for bb in range(10):
        for ee in range(7):
            oo, ddd = aa(bb, ee)
            aaa = pygame.Rect(oo, ddd, 40, 40)
            if aaa.collidepoint(x, y):
                return (bb, ee)
    return (None, None)
def w(ss, tt, bb, ee):
    oo, ddd = aa(bb, ee)
    if ss == 'a':
        pygame.draw.circle(b, tt, (oo + 20, ddd + 20), 15)
        pygame.draw.circle(b, (60, 60, 100), (oo + 20, ddd + 20), 5)
    elif ss == 'b':
        pygame.draw.rect(b, tt, (oo + 10, ddd + 10, 20, 20))
    elif ss == 'c':
        pygame.draw.polygon(b, tt, ((oo + 20, ddd), (oo + 40 - 1, ddd + 20), (oo + 20, ddd + 40 - 1), (oo, ddd + 20)))
    elif ss == 'd':
        for i in range(0, 40, 4):
            pygame.draw.line(b, tt, (oo, ddd + i), (oo + i, ddd))
            pygame.draw.line(b, tt, (oo + i, ddd + 39), (oo + 39, ddd + i))
    elif ss == 'e':
        pygame.draw.ellipse(b, tt, (oo, ddd + 10, 40, 20))
def s(bbb, bb, ee):
    return bbb[bb][ee][0], bbb[bb][ee][1]
def dd(bbb, boxes, gg):
    for box in boxes:
        oo, ddd = aa(box[0], box[1])
        pygame.draw.rect(b, (60, 60, 100), (oo, ddd, 40, 40))
        ss, tt = s(bbb, box[0], box[1])
        w(ss, tt, box[0], box[1])
        if gg > 0:
            pygame.draw.rect(b, (255, 255, 255), (oo, ddd, gg, 40))
    pygame.display.update()
    a.tick(30)
def o(bbb, cc):
    for gg in range(40, (-8) - 1, -8):
        dd(bbb, cc, gg)
def p(bbb, ff):
    for gg in range(0, 48, 8):
        dd(bbb, ff, gg)
def f(bbb, pp):
    for bb in range(10):
        for ee in range(7):
            oo, ddd = aa(bb, ee)
            if not pp[bb][ee]:
                pygame.draw.rect(b, (255, 255, 255), (oo, ddd, 40, 40))
            else:
                ss, tt = s(bbb, bb, ee)
                w(ss, tt, bb, ee)
def n(bb, ee):
    oo, ddd = aa(bb, ee)
    pygame.draw.rect(b, (0, 0, 255), (oo - 5, ddd - 5, 50, 50), 4)
def g(bbb):
    mm = d(False)
    boxes = []
    for x in range(10):
        for y in range(7):
            boxes.append( (x, y) )
    random.shuffle(boxes)
    kk = t(8, boxes)
    f(bbb, mm)
    for nn in kk:
        o(bbb, nn)
        p(bbb, nn)
def jj(bbb):
    mm = d(True)
    tt1 = (100, 100, 100)
    tt2 = (60, 60, 100)
    for i in range(13):
        tt1, tt2 = tt2, tt1
        b.fill(tt1)
        f(bbb, mm)
        pygame.display.update()
        pygame.time.wait(300)
def ii(hh):
    for i in hh:
        if False in i:
            return False
    return True
if __name__ == '__main__':
    hhh()