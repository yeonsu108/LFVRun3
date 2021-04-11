# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.0.0 for Linux x86 (64-bit) (April 7, 2019)
# Date: Thu 24 Oct 2019 15:52:53


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_22})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_2391})

V_3 = Vertex(name = 'V_3',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_2})

V_4 = Vertex(name = 'V_4',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
             couplings = {(1,1):C.GC_3,(0,0):C.GC_3,(2,2):C.GC_3})

V_5 = Vertex(name = 'V_5',
             particles = [ P.d__tilde__, P.d, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_2398})

V_6 = Vertex(name = 'V_6',
             particles = [ P.s__tilde__, P.s, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_2399})

V_7 = Vertex(name = 'V_7',
             particles = [ P.b__tilde__, P.b, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_2396})

V_8 = Vertex(name = 'V_8',
             particles = [ P.e__plus__, P.e__minus__, P.H ],
             color = [ '1' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_2393})

V_9 = Vertex(name = 'V_9',
             particles = [ P.mu__plus__, P.mu__minus__, P.H ],
             color = [ '1' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_2394})

V_10 = Vertex(name = 'V_10',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_2395})

V_11 = Vertex(name = 'V_11',
              particles = [ P.u__tilde__, P.u, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_2401})

V_12 = Vertex(name = 'V_12',
              particles = [ P.c__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_2397})

V_13 = Vertex(name = 'V_13',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_2400})

V_14 = Vertex(name = 'V_14',
              particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2300,(0,9):C.GC_1572,(0,7):C.GC_1571,(0,8):C.GC_1571,(0,0):C.GC_1247,(0,11):C.GC_1490,(0,1):C.GC_356,(0,2):C.GC_113,(0,5):C.GC_1734,(0,3):C.GC_1733,(0,4):C.GC_1733,(0,10):C.GC_1409})

V_15 = Vertex(name = 'V_15',
              particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2301,(0,9):C.GC_1574,(0,7):C.GC_1573,(0,8):C.GC_1573,(0,0):C.GC_1248,(0,11):C.GC_1491,(0,1):C.GC_357,(0,2):C.GC_114,(0,5):C.GC_1736,(0,3):C.GC_1735,(0,4):C.GC_1735,(0,10):C.GC_1410})

V_16 = Vertex(name = 'V_16',
              particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,8):C.GC_1575,(0,6):C.GC_2302,(0,9):C.GC_1576,(0,7):C.GC_1575,(0,0):C.GC_1249,(0,3):C.GC_1737,(0,4):C.GC_1737,(0,11):C.GC_1492,(0,1):C.GC_358,(0,2):C.GC_115,(0,5):C.GC_1738,(0,10):C.GC_1411})

V_17 = Vertex(name = 'V_17',
              particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2303,(0,9):C.GC_1578,(0,7):C.GC_1577,(0,8):C.GC_1577,(0,0):C.GC_1250,(0,11):C.GC_1493,(0,1):C.GC_359,(0,2):C.GC_116,(0,5):C.GC_1740,(0,3):C.GC_1739,(0,4):C.GC_1739,(0,10):C.GC_1412})

V_18 = Vertex(name = 'V_18',
              particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2304,(0,9):C.GC_1580,(0,7):C.GC_1579,(0,8):C.GC_1579,(0,0):C.GC_1251,(0,11):C.GC_1494,(0,1):C.GC_360,(0,2):C.GC_117,(0,5):C.GC_1742,(0,3):C.GC_1741,(0,4):C.GC_1741,(0,10):C.GC_1413})

V_19 = Vertex(name = 'V_19',
              particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2305,(0,9):C.GC_1582,(0,7):C.GC_1581,(0,8):C.GC_1581,(0,0):C.GC_1252,(0,11):C.GC_1495,(0,1):C.GC_361,(0,2):C.GC_118,(0,5):C.GC_1744,(0,3):C.GC_1743,(0,4):C.GC_1743,(0,10):C.GC_1414})

V_20 = Vertex(name = 'V_20',
              particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2306,(0,9):C.GC_1584,(0,7):C.GC_1583,(0,8):C.GC_1583,(0,0):C.GC_1253,(0,11):C.GC_1496,(0,1):C.GC_362,(0,2):C.GC_119,(0,5):C.GC_1746,(0,3):C.GC_1745,(0,4):C.GC_1745,(0,10):C.GC_1415})

V_21 = Vertex(name = 'V_21',
              particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2307,(0,9):C.GC_1586,(0,7):C.GC_1585,(0,8):C.GC_1585,(0,0):C.GC_1254,(0,11):C.GC_1497,(0,1):C.GC_363,(0,2):C.GC_120,(0,5):C.GC_1748,(0,3):C.GC_1747,(0,4):C.GC_1747,(0,10):C.GC_1416})

V_22 = Vertex(name = 'V_22',
              particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2308,(0,9):C.GC_1588,(0,7):C.GC_1587,(0,8):C.GC_1587,(0,0):C.GC_1255,(0,11):C.GC_1498,(0,1):C.GC_364,(0,2):C.GC_121,(0,5):C.GC_1750,(0,3):C.GC_1749,(0,4):C.GC_1749,(0,10):C.GC_1417})

V_23 = Vertex(name = 'V_23',
              particles = [ P.mu__plus__, P.e__minus__, P.u__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2309,(0,9):C.GC_1590,(0,7):C.GC_1589,(0,8):C.GC_1589,(0,0):C.GC_1256,(0,11):C.GC_1499,(0,1):C.GC_365,(0,2):C.GC_122,(0,5):C.GC_1752,(0,3):C.GC_1751,(0,4):C.GC_1751,(0,10):C.GC_1418})

V_24 = Vertex(name = 'V_24',
              particles = [ P.mu__plus__, P.e__minus__, P.c__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2310,(0,9):C.GC_1592,(0,7):C.GC_1591,(0,8):C.GC_1591,(0,0):C.GC_1257,(0,11):C.GC_1500,(0,1):C.GC_366,(0,2):C.GC_123,(0,5):C.GC_1754,(0,3):C.GC_1753,(0,4):C.GC_1753,(0,10):C.GC_1419})

V_25 = Vertex(name = 'V_25',
              particles = [ P.mu__plus__, P.e__minus__, P.t__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2311,(0,9):C.GC_1594,(0,7):C.GC_1593,(0,8):C.GC_1593,(0,0):C.GC_1258,(0,11):C.GC_1501,(0,1):C.GC_367,(0,2):C.GC_124,(0,5):C.GC_1756,(0,3):C.GC_1755,(0,4):C.GC_1755,(0,10):C.GC_1420})

V_26 = Vertex(name = 'V_26',
              particles = [ P.mu__plus__, P.e__minus__, P.u__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2312,(0,9):C.GC_1596,(0,7):C.GC_1595,(0,8):C.GC_1595,(0,0):C.GC_1259,(0,11):C.GC_1502,(0,1):C.GC_368,(0,2):C.GC_125,(0,5):C.GC_1758,(0,3):C.GC_1757,(0,4):C.GC_1757,(0,10):C.GC_1421})

V_27 = Vertex(name = 'V_27',
              particles = [ P.mu__plus__, P.e__minus__, P.c__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2313,(0,9):C.GC_1598,(0,7):C.GC_1597,(0,8):C.GC_1597,(0,0):C.GC_1260,(0,11):C.GC_1503,(0,1):C.GC_369,(0,2):C.GC_126,(0,5):C.GC_1760,(0,3):C.GC_1759,(0,4):C.GC_1759,(0,10):C.GC_1422})

V_28 = Vertex(name = 'V_28',
              particles = [ P.mu__plus__, P.e__minus__, P.t__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2314,(0,9):C.GC_1600,(0,7):C.GC_1599,(0,8):C.GC_1599,(0,0):C.GC_1261,(0,11):C.GC_1504,(0,1):C.GC_370,(0,2):C.GC_127,(0,5):C.GC_1762,(0,3):C.GC_1761,(0,4):C.GC_1761,(0,10):C.GC_1423})

V_29 = Vertex(name = 'V_29',
              particles = [ P.mu__plus__, P.e__minus__, P.u__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2315,(0,9):C.GC_1602,(0,7):C.GC_1601,(0,8):C.GC_1601,(0,0):C.GC_1262,(0,11):C.GC_1505,(0,1):C.GC_371,(0,2):C.GC_128,(0,5):C.GC_1764,(0,3):C.GC_1763,(0,4):C.GC_1763,(0,10):C.GC_1424})

V_30 = Vertex(name = 'V_30',
              particles = [ P.mu__plus__, P.e__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2316,(0,9):C.GC_1604,(0,7):C.GC_1603,(0,8):C.GC_1603,(0,0):C.GC_1263,(0,11):C.GC_1506,(0,1):C.GC_372,(0,2):C.GC_129,(0,5):C.GC_1766,(0,3):C.GC_1765,(0,4):C.GC_1765,(0,10):C.GC_1425})

V_31 = Vertex(name = 'V_31',
              particles = [ P.mu__plus__, P.e__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2317,(0,9):C.GC_1606,(0,7):C.GC_1605,(0,8):C.GC_1605,(0,0):C.GC_1264,(0,11):C.GC_1507,(0,1):C.GC_373,(0,2):C.GC_130,(0,5):C.GC_1768,(0,3):C.GC_1767,(0,4):C.GC_1767,(0,10):C.GC_1426})

V_32 = Vertex(name = 'V_32',
              particles = [ P.ta__plus__, P.e__minus__, P.u__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2318,(0,9):C.GC_1608,(0,7):C.GC_1607,(0,8):C.GC_1607,(0,0):C.GC_1265,(0,11):C.GC_1508,(0,1):C.GC_374,(0,2):C.GC_131,(0,5):C.GC_1770,(0,3):C.GC_1769,(0,4):C.GC_1769,(0,10):C.GC_1427})

V_33 = Vertex(name = 'V_33',
              particles = [ P.ta__plus__, P.e__minus__, P.c__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2319,(0,9):C.GC_1610,(0,7):C.GC_1609,(0,8):C.GC_1609,(0,0):C.GC_1266,(0,11):C.GC_1509,(0,1):C.GC_375,(0,2):C.GC_132,(0,5):C.GC_1772,(0,3):C.GC_1771,(0,4):C.GC_1771,(0,10):C.GC_1428})

V_34 = Vertex(name = 'V_34',
              particles = [ P.ta__plus__, P.e__minus__, P.t__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2320,(0,9):C.GC_1612,(0,7):C.GC_1611,(0,8):C.GC_1611,(0,0):C.GC_1267,(0,11):C.GC_1510,(0,1):C.GC_376,(0,2):C.GC_133,(0,5):C.GC_1774,(0,3):C.GC_1773,(0,4):C.GC_1773,(0,10):C.GC_1429})

V_35 = Vertex(name = 'V_35',
              particles = [ P.ta__plus__, P.e__minus__, P.u__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2321,(0,9):C.GC_1614,(0,7):C.GC_1613,(0,8):C.GC_1613,(0,0):C.GC_1268,(0,11):C.GC_1511,(0,1):C.GC_377,(0,2):C.GC_134,(0,5):C.GC_1776,(0,3):C.GC_1775,(0,4):C.GC_1775,(0,10):C.GC_1430})

V_36 = Vertex(name = 'V_36',
              particles = [ P.ta__plus__, P.e__minus__, P.c__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2322,(0,9):C.GC_1616,(0,7):C.GC_1615,(0,8):C.GC_1615,(0,0):C.GC_1269,(0,11):C.GC_1512,(0,1):C.GC_378,(0,2):C.GC_135,(0,5):C.GC_1778,(0,3):C.GC_1777,(0,4):C.GC_1777,(0,10):C.GC_1431})

V_37 = Vertex(name = 'V_37',
              particles = [ P.ta__plus__, P.e__minus__, P.t__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2323,(0,9):C.GC_1618,(0,7):C.GC_1617,(0,8):C.GC_1617,(0,0):C.GC_1270,(0,11):C.GC_1513,(0,1):C.GC_379,(0,2):C.GC_136,(0,5):C.GC_1780,(0,3):C.GC_1779,(0,4):C.GC_1779,(0,10):C.GC_1432})

V_38 = Vertex(name = 'V_38',
              particles = [ P.ta__plus__, P.e__minus__, P.u__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2324,(0,9):C.GC_1620,(0,7):C.GC_1619,(0,8):C.GC_1619,(0,0):C.GC_1271,(0,11):C.GC_1514,(0,1):C.GC_380,(0,2):C.GC_137,(0,5):C.GC_1782,(0,3):C.GC_1781,(0,4):C.GC_1781,(0,10):C.GC_1433})

V_39 = Vertex(name = 'V_39',
              particles = [ P.ta__plus__, P.e__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2325,(0,9):C.GC_1622,(0,7):C.GC_1621,(0,8):C.GC_1621,(0,0):C.GC_1272,(0,11):C.GC_1515,(0,1):C.GC_381,(0,2):C.GC_138,(0,5):C.GC_1784,(0,3):C.GC_1783,(0,4):C.GC_1783,(0,10):C.GC_1434})

V_40 = Vertex(name = 'V_40',
              particles = [ P.ta__plus__, P.e__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2326,(0,9):C.GC_1624,(0,7):C.GC_1623,(0,8):C.GC_1623,(0,0):C.GC_1273,(0,11):C.GC_1516,(0,1):C.GC_382,(0,2):C.GC_139,(0,5):C.GC_1786,(0,3):C.GC_1785,(0,4):C.GC_1785,(0,10):C.GC_1435})

V_41 = Vertex(name = 'V_41',
              particles = [ P.e__plus__, P.mu__minus__, P.u__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2327,(0,9):C.GC_1626,(0,7):C.GC_1625,(0,8):C.GC_1625,(0,0):C.GC_1274,(0,11):C.GC_1517,(0,1):C.GC_383,(0,2):C.GC_140,(0,5):C.GC_1788,(0,3):C.GC_1787,(0,4):C.GC_1787,(0,10):C.GC_1436})

V_42 = Vertex(name = 'V_42',
              particles = [ P.e__plus__, P.mu__minus__, P.c__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2328,(0,9):C.GC_1628,(0,7):C.GC_1627,(0,8):C.GC_1627,(0,0):C.GC_1275,(0,11):C.GC_1518,(0,1):C.GC_384,(0,2):C.GC_141,(0,5):C.GC_1790,(0,3):C.GC_1789,(0,4):C.GC_1789,(0,10):C.GC_1437})

V_43 = Vertex(name = 'V_43',
              particles = [ P.e__plus__, P.mu__minus__, P.t__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,9):C.GC_1630,(0,7):C.GC_1629,(0,8):C.GC_1629,(0,6):C.GC_2329,(0,0):C.GC_1276,(0,11):C.GC_1519,(0,1):C.GC_385,(0,2):C.GC_142,(0,5):C.GC_1792,(0,3):C.GC_1791,(0,4):C.GC_1791,(0,10):C.GC_1438})

V_44 = Vertex(name = 'V_44',
              particles = [ P.e__plus__, P.mu__minus__, P.u__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2330,(0,9):C.GC_1632,(0,7):C.GC_1631,(0,8):C.GC_1631,(0,0):C.GC_1277,(0,11):C.GC_1520,(0,1):C.GC_386,(0,2):C.GC_143,(0,5):C.GC_1794,(0,3):C.GC_1793,(0,4):C.GC_1793,(0,10):C.GC_1439})

V_45 = Vertex(name = 'V_45',
              particles = [ P.e__plus__, P.mu__minus__, P.c__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2331,(0,9):C.GC_1634,(0,7):C.GC_1633,(0,8):C.GC_1633,(0,0):C.GC_1278,(0,11):C.GC_1521,(0,1):C.GC_387,(0,2):C.GC_144,(0,5):C.GC_1796,(0,3):C.GC_1795,(0,4):C.GC_1795,(0,10):C.GC_1440})

V_46 = Vertex(name = 'V_46',
              particles = [ P.e__plus__, P.mu__minus__, P.t__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2332,(0,9):C.GC_1636,(0,7):C.GC_1635,(0,8):C.GC_1635,(0,0):C.GC_1279,(0,11):C.GC_1522,(0,1):C.GC_388,(0,2):C.GC_145,(0,5):C.GC_1798,(0,3):C.GC_1797,(0,4):C.GC_1797,(0,10):C.GC_1441})

V_47 = Vertex(name = 'V_47',
              particles = [ P.e__plus__, P.mu__minus__, P.u__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2333,(0,9):C.GC_1638,(0,7):C.GC_1637,(0,8):C.GC_1637,(0,0):C.GC_1280,(0,11):C.GC_1523,(0,1):C.GC_389,(0,2):C.GC_146,(0,5):C.GC_1800,(0,3):C.GC_1799,(0,4):C.GC_1799,(0,10):C.GC_1442})

V_48 = Vertex(name = 'V_48',
              particles = [ P.e__plus__, P.mu__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2334,(0,9):C.GC_1640,(0,7):C.GC_1639,(0,8):C.GC_1639,(0,0):C.GC_1281,(0,11):C.GC_1524,(0,1):C.GC_390,(0,2):C.GC_147,(0,5):C.GC_1802,(0,3):C.GC_1801,(0,4):C.GC_1801,(0,10):C.GC_1443})

V_49 = Vertex(name = 'V_49',
              particles = [ P.e__plus__, P.mu__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2335,(0,9):C.GC_1642,(0,7):C.GC_1641,(0,8):C.GC_1641,(0,0):C.GC_1282,(0,11):C.GC_1525,(0,1):C.GC_391,(0,2):C.GC_148,(0,5):C.GC_1804,(0,3):C.GC_1803,(0,4):C.GC_1803,(0,10):C.GC_1444})

V_50 = Vertex(name = 'V_50',
              particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2336,(0,9):C.GC_1644,(0,7):C.GC_1643,(0,8):C.GC_1643,(0,0):C.GC_1283,(0,11):C.GC_1526,(0,1):C.GC_392,(0,2):C.GC_149,(0,5):C.GC_1806,(0,3):C.GC_1805,(0,4):C.GC_1805,(0,10):C.GC_1445})

V_51 = Vertex(name = 'V_51',
              particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2337,(0,9):C.GC_1646,(0,7):C.GC_1645,(0,8):C.GC_1645,(0,0):C.GC_1284,(0,11):C.GC_1527,(0,1):C.GC_393,(0,2):C.GC_150,(0,5):C.GC_1808,(0,3):C.GC_1807,(0,4):C.GC_1807,(0,10):C.GC_1446})

V_52 = Vertex(name = 'V_52',
              particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2338,(0,9):C.GC_1648,(0,7):C.GC_1647,(0,8):C.GC_1647,(0,0):C.GC_1285,(0,11):C.GC_1528,(0,1):C.GC_394,(0,2):C.GC_151,(0,5):C.GC_1810,(0,3):C.GC_1809,(0,4):C.GC_1809,(0,10):C.GC_1447})

V_53 = Vertex(name = 'V_53',
              particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2339,(0,9):C.GC_1650,(0,7):C.GC_1649,(0,8):C.GC_1649,(0,0):C.GC_1286,(0,11):C.GC_1529,(0,1):C.GC_395,(0,2):C.GC_152,(0,5):C.GC_1812,(0,3):C.GC_1811,(0,4):C.GC_1811,(0,10):C.GC_1448})

V_54 = Vertex(name = 'V_54',
              particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2340,(0,9):C.GC_1652,(0,7):C.GC_1651,(0,8):C.GC_1651,(0,0):C.GC_1287,(0,11):C.GC_1530,(0,1):C.GC_396,(0,2):C.GC_153,(0,5):C.GC_1814,(0,3):C.GC_1813,(0,4):C.GC_1813,(0,10):C.GC_1449})

V_55 = Vertex(name = 'V_55',
              particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2341,(0,9):C.GC_1654,(0,7):C.GC_1653,(0,8):C.GC_1653,(0,0):C.GC_1288,(0,11):C.GC_1531,(0,1):C.GC_397,(0,2):C.GC_154,(0,5):C.GC_1816,(0,3):C.GC_1815,(0,4):C.GC_1815,(0,10):C.GC_1450})

V_56 = Vertex(name = 'V_56',
              particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2342,(0,9):C.GC_1656,(0,7):C.GC_1655,(0,8):C.GC_1655,(0,0):C.GC_1289,(0,11):C.GC_1532,(0,1):C.GC_398,(0,2):C.GC_155,(0,5):C.GC_1818,(0,3):C.GC_1817,(0,4):C.GC_1817,(0,10):C.GC_1451})

V_57 = Vertex(name = 'V_57',
              particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2343,(0,9):C.GC_1658,(0,7):C.GC_1657,(0,8):C.GC_1657,(0,0):C.GC_1290,(0,11):C.GC_1533,(0,1):C.GC_399,(0,2):C.GC_156,(0,5):C.GC_1820,(0,3):C.GC_1819,(0,4):C.GC_1819,(0,10):C.GC_1452})

V_58 = Vertex(name = 'V_58',
              particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2344,(0,9):C.GC_1660,(0,7):C.GC_1659,(0,8):C.GC_1659,(0,0):C.GC_1291,(0,11):C.GC_1534,(0,1):C.GC_400,(0,2):C.GC_157,(0,5):C.GC_1822,(0,3):C.GC_1821,(0,4):C.GC_1821,(0,10):C.GC_1453})

V_59 = Vertex(name = 'V_59',
              particles = [ P.ta__plus__, P.mu__minus__, P.u__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2345,(0,9):C.GC_1662,(0,7):C.GC_1661,(0,8):C.GC_1661,(0,0):C.GC_1292,(0,11):C.GC_1535,(0,1):C.GC_401,(0,2):C.GC_158,(0,5):C.GC_1824,(0,3):C.GC_1823,(0,4):C.GC_1823,(0,10):C.GC_1454})

V_60 = Vertex(name = 'V_60',
              particles = [ P.ta__plus__, P.mu__minus__, P.c__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2346,(0,9):C.GC_1664,(0,7):C.GC_1663,(0,8):C.GC_1663,(0,0):C.GC_1293,(0,11):C.GC_1536,(0,1):C.GC_402,(0,2):C.GC_159,(0,5):C.GC_1826,(0,3):C.GC_1825,(0,4):C.GC_1825,(0,10):C.GC_1455})

V_61 = Vertex(name = 'V_61',
              particles = [ P.ta__plus__, P.mu__minus__, P.t__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,8):C.GC_1665,(0,6):C.GC_2347,(0,9):C.GC_1666,(0,7):C.GC_1665,(0,0):C.GC_1294,(0,3):C.GC_1827,(0,4):C.GC_1827,(0,11):C.GC_1537,(0,1):C.GC_403,(0,2):C.GC_160,(0,5):C.GC_1828,(0,10):C.GC_1456})

V_62 = Vertex(name = 'V_62',
              particles = [ P.ta__plus__, P.mu__minus__, P.u__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2348,(0,9):C.GC_1668,(0,7):C.GC_1667,(0,8):C.GC_1667,(0,0):C.GC_1295,(0,11):C.GC_1538,(0,1):C.GC_404,(0,2):C.GC_161,(0,5):C.GC_1830,(0,3):C.GC_1829,(0,4):C.GC_1829,(0,10):C.GC_1457})

V_63 = Vertex(name = 'V_63',
              particles = [ P.ta__plus__, P.mu__minus__, P.c__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2349,(0,9):C.GC_1670,(0,7):C.GC_1669,(0,8):C.GC_1669,(0,0):C.GC_1296,(0,11):C.GC_1539,(0,1):C.GC_405,(0,2):C.GC_162,(0,5):C.GC_1832,(0,3):C.GC_1831,(0,4):C.GC_1831,(0,10):C.GC_1458})

V_64 = Vertex(name = 'V_64',
              particles = [ P.ta__plus__, P.mu__minus__, P.t__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2350,(0,9):C.GC_1672,(0,7):C.GC_1671,(0,8):C.GC_1671,(0,0):C.GC_1297,(0,11):C.GC_1540,(0,1):C.GC_406,(0,2):C.GC_163,(0,5):C.GC_1834,(0,3):C.GC_1833,(0,4):C.GC_1833,(0,10):C.GC_1459})

V_65 = Vertex(name = 'V_65',
              particles = [ P.ta__plus__, P.mu__minus__, P.u__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2351,(0,9):C.GC_1674,(0,7):C.GC_1673,(0,8):C.GC_1673,(0,0):C.GC_1298,(0,11):C.GC_1541,(0,1):C.GC_407,(0,2):C.GC_164,(0,5):C.GC_1836,(0,3):C.GC_1835,(0,4):C.GC_1835,(0,10):C.GC_1460})

V_66 = Vertex(name = 'V_66',
              particles = [ P.ta__plus__, P.mu__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2352,(0,9):C.GC_1676,(0,7):C.GC_1675,(0,8):C.GC_1675,(0,0):C.GC_1299,(0,11):C.GC_1542,(0,1):C.GC_408,(0,2):C.GC_165,(0,5):C.GC_1838,(0,3):C.GC_1837,(0,4):C.GC_1837,(0,10):C.GC_1461})

V_67 = Vertex(name = 'V_67',
              particles = [ P.ta__plus__, P.mu__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2353,(0,9):C.GC_1678,(0,7):C.GC_1677,(0,8):C.GC_1677,(0,0):C.GC_1300,(0,11):C.GC_1543,(0,1):C.GC_409,(0,2):C.GC_166,(0,5):C.GC_1840,(0,3):C.GC_1839,(0,4):C.GC_1839,(0,10):C.GC_1462})

V_68 = Vertex(name = 'V_68',
              particles = [ P.e__plus__, P.ta__minus__, P.u__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2354,(0,9):C.GC_1680,(0,7):C.GC_1679,(0,8):C.GC_1679,(0,0):C.GC_1301,(0,11):C.GC_1544,(0,1):C.GC_410,(0,2):C.GC_167,(0,5):C.GC_1842,(0,3):C.GC_1841,(0,4):C.GC_1841,(0,10):C.GC_1463})

V_69 = Vertex(name = 'V_69',
              particles = [ P.e__plus__, P.ta__minus__, P.c__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2355,(0,9):C.GC_1682,(0,7):C.GC_1681,(0,8):C.GC_1681,(0,0):C.GC_1302,(0,11):C.GC_1545,(0,1):C.GC_411,(0,2):C.GC_168,(0,5):C.GC_1844,(0,3):C.GC_1843,(0,4):C.GC_1843,(0,10):C.GC_1464})

V_70 = Vertex(name = 'V_70',
              particles = [ P.e__plus__, P.ta__minus__, P.t__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2356,(0,9):C.GC_1684,(0,7):C.GC_1683,(0,8):C.GC_1683,(0,0):C.GC_1303,(0,11):C.GC_1546,(0,1):C.GC_412,(0,2):C.GC_169,(0,5):C.GC_1846,(0,3):C.GC_1845,(0,4):C.GC_1845,(0,10):C.GC_1465})

V_71 = Vertex(name = 'V_71',
              particles = [ P.e__plus__, P.ta__minus__, P.u__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2357,(0,9):C.GC_1686,(0,7):C.GC_1685,(0,8):C.GC_1685,(0,0):C.GC_1304,(0,11):C.GC_1547,(0,1):C.GC_413,(0,2):C.GC_170,(0,5):C.GC_1848,(0,3):C.GC_1847,(0,4):C.GC_1847,(0,10):C.GC_1466})

V_72 = Vertex(name = 'V_72',
              particles = [ P.e__plus__, P.ta__minus__, P.c__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2358,(0,9):C.GC_1688,(0,7):C.GC_1687,(0,8):C.GC_1687,(0,0):C.GC_1305,(0,11):C.GC_1548,(0,1):C.GC_414,(0,2):C.GC_171,(0,5):C.GC_1850,(0,3):C.GC_1849,(0,4):C.GC_1849,(0,10):C.GC_1467})

V_73 = Vertex(name = 'V_73',
              particles = [ P.e__plus__, P.ta__minus__, P.t__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2359,(0,9):C.GC_1690,(0,7):C.GC_1689,(0,8):C.GC_1689,(0,0):C.GC_1306,(0,11):C.GC_1549,(0,1):C.GC_415,(0,2):C.GC_172,(0,5):C.GC_1852,(0,3):C.GC_1851,(0,4):C.GC_1851,(0,10):C.GC_1468})

V_74 = Vertex(name = 'V_74',
              particles = [ P.e__plus__, P.ta__minus__, P.u__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2360,(0,9):C.GC_1692,(0,7):C.GC_1691,(0,8):C.GC_1691,(0,0):C.GC_1307,(0,11):C.GC_1550,(0,1):C.GC_416,(0,2):C.GC_173,(0,5):C.GC_1854,(0,3):C.GC_1853,(0,4):C.GC_1853,(0,10):C.GC_1469})

V_75 = Vertex(name = 'V_75',
              particles = [ P.e__plus__, P.ta__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2361,(0,9):C.GC_1694,(0,7):C.GC_1693,(0,8):C.GC_1693,(0,0):C.GC_1308,(0,11):C.GC_1551,(0,1):C.GC_417,(0,2):C.GC_174,(0,5):C.GC_1856,(0,3):C.GC_1855,(0,4):C.GC_1855,(0,10):C.GC_1470})

V_76 = Vertex(name = 'V_76',
              particles = [ P.e__plus__, P.ta__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2362,(0,9):C.GC_1696,(0,7):C.GC_1695,(0,8):C.GC_1695,(0,0):C.GC_1309,(0,11):C.GC_1552,(0,1):C.GC_418,(0,2):C.GC_175,(0,5):C.GC_1858,(0,3):C.GC_1857,(0,4):C.GC_1857,(0,10):C.GC_1471})

V_77 = Vertex(name = 'V_77',
              particles = [ P.mu__plus__, P.ta__minus__, P.u__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2363,(0,9):C.GC_1698,(0,7):C.GC_1697,(0,8):C.GC_1697,(0,0):C.GC_1310,(0,11):C.GC_1553,(0,1):C.GC_419,(0,2):C.GC_176,(0,5):C.GC_1860,(0,3):C.GC_1859,(0,4):C.GC_1859,(0,10):C.GC_1472})

V_78 = Vertex(name = 'V_78',
              particles = [ P.mu__plus__, P.ta__minus__, P.c__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2364,(0,9):C.GC_1700,(0,7):C.GC_1699,(0,8):C.GC_1699,(0,0):C.GC_1311,(0,11):C.GC_1554,(0,1):C.GC_420,(0,2):C.GC_177,(0,5):C.GC_1862,(0,3):C.GC_1861,(0,4):C.GC_1861,(0,10):C.GC_1473})

V_79 = Vertex(name = 'V_79',
              particles = [ P.mu__plus__, P.ta__minus__, P.t__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2365,(0,9):C.GC_1702,(0,7):C.GC_1701,(0,8):C.GC_1701,(0,0):C.GC_1312,(0,11):C.GC_1555,(0,1):C.GC_421,(0,2):C.GC_178,(0,5):C.GC_1864,(0,3):C.GC_1863,(0,4):C.GC_1863,(0,10):C.GC_1474})

V_80 = Vertex(name = 'V_80',
              particles = [ P.mu__plus__, P.ta__minus__, P.u__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2366,(0,9):C.GC_1704,(0,7):C.GC_1703,(0,8):C.GC_1703,(0,0):C.GC_1313,(0,11):C.GC_1556,(0,1):C.GC_422,(0,2):C.GC_179,(0,5):C.GC_1866,(0,3):C.GC_1865,(0,4):C.GC_1865,(0,10):C.GC_1475})

V_81 = Vertex(name = 'V_81',
              particles = [ P.mu__plus__, P.ta__minus__, P.c__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2367,(0,9):C.GC_1706,(0,7):C.GC_1705,(0,8):C.GC_1705,(0,0):C.GC_1314,(0,11):C.GC_1557,(0,1):C.GC_423,(0,2):C.GC_180,(0,5):C.GC_1868,(0,3):C.GC_1867,(0,4):C.GC_1867,(0,10):C.GC_1476})

V_82 = Vertex(name = 'V_82',
              particles = [ P.mu__plus__, P.ta__minus__, P.t__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2368,(0,9):C.GC_1708,(0,7):C.GC_1707,(0,8):C.GC_1707,(0,0):C.GC_1315,(0,11):C.GC_1558,(0,1):C.GC_424,(0,2):C.GC_181,(0,5):C.GC_1870,(0,3):C.GC_1869,(0,4):C.GC_1869,(0,10):C.GC_1477})

V_83 = Vertex(name = 'V_83',
              particles = [ P.mu__plus__, P.ta__minus__, P.u__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2369,(0,9):C.GC_1710,(0,7):C.GC_1709,(0,8):C.GC_1709,(0,0):C.GC_1316,(0,11):C.GC_1559,(0,1):C.GC_425,(0,2):C.GC_182,(0,5):C.GC_1872,(0,3):C.GC_1871,(0,4):C.GC_1871,(0,10):C.GC_1478})

V_84 = Vertex(name = 'V_84',
              particles = [ P.mu__plus__, P.ta__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2370,(0,9):C.GC_1712,(0,7):C.GC_1711,(0,8):C.GC_1711,(0,0):C.GC_1317,(0,11):C.GC_1560,(0,1):C.GC_426,(0,2):C.GC_183,(0,5):C.GC_1874,(0,3):C.GC_1873,(0,4):C.GC_1873,(0,10):C.GC_1479})

V_85 = Vertex(name = 'V_85',
              particles = [ P.mu__plus__, P.ta__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2371,(0,9):C.GC_1714,(0,7):C.GC_1713,(0,8):C.GC_1713,(0,0):C.GC_1318,(0,11):C.GC_1561,(0,1):C.GC_427,(0,2):C.GC_184,(0,5):C.GC_1876,(0,3):C.GC_1875,(0,4):C.GC_1875,(0,10):C.GC_1480})

V_86 = Vertex(name = 'V_86',
              particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2372,(0,9):C.GC_1716,(0,7):C.GC_1715,(0,8):C.GC_1715,(0,0):C.GC_1319,(0,11):C.GC_1562,(0,1):C.GC_428,(0,2):C.GC_185,(0,5):C.GC_1878,(0,3):C.GC_1877,(0,4):C.GC_1877,(0,10):C.GC_1481})

V_87 = Vertex(name = 'V_87',
              particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2373,(0,9):C.GC_1718,(0,7):C.GC_1717,(0,8):C.GC_1717,(0,0):C.GC_1320,(0,11):C.GC_1563,(0,1):C.GC_429,(0,2):C.GC_186,(0,5):C.GC_1880,(0,3):C.GC_1879,(0,4):C.GC_1879,(0,10):C.GC_1482})

V_88 = Vertex(name = 'V_88',
              particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,9):C.GC_1720,(0,7):C.GC_1719,(0,8):C.GC_1719,(0,6):C.GC_2374,(0,0):C.GC_1321,(0,11):C.GC_1564,(0,1):C.GC_430,(0,2):C.GC_187,(0,5):C.GC_1882,(0,3):C.GC_1881,(0,4):C.GC_1881,(0,10):C.GC_1483})

V_89 = Vertex(name = 'V_89',
              particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2375,(0,9):C.GC_1722,(0,7):C.GC_1721,(0,8):C.GC_1721,(0,0):C.GC_1322,(0,11):C.GC_1565,(0,1):C.GC_431,(0,2):C.GC_188,(0,5):C.GC_1884,(0,3):C.GC_1883,(0,4):C.GC_1883,(0,10):C.GC_1484})

V_90 = Vertex(name = 'V_90',
              particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2376,(0,9):C.GC_1724,(0,7):C.GC_1723,(0,8):C.GC_1723,(0,0):C.GC_1323,(0,11):C.GC_1566,(0,1):C.GC_432,(0,2):C.GC_189,(0,5):C.GC_1886,(0,3):C.GC_1885,(0,4):C.GC_1885,(0,10):C.GC_1485})

V_91 = Vertex(name = 'V_91',
              particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2377,(0,9):C.GC_1726,(0,7):C.GC_1725,(0,8):C.GC_1725,(0,0):C.GC_1324,(0,11):C.GC_1567,(0,1):C.GC_433,(0,2):C.GC_190,(0,5):C.GC_1888,(0,3):C.GC_1887,(0,4):C.GC_1887,(0,10):C.GC_1486})

V_92 = Vertex(name = 'V_92',
              particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2378,(0,9):C.GC_1728,(0,7):C.GC_1727,(0,8):C.GC_1727,(0,0):C.GC_1325,(0,11):C.GC_1568,(0,1):C.GC_434,(0,2):C.GC_191,(0,5):C.GC_1890,(0,3):C.GC_1889,(0,4):C.GC_1889,(0,10):C.GC_1487})

V_93 = Vertex(name = 'V_93',
              particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2379,(0,9):C.GC_1730,(0,7):C.GC_1729,(0,8):C.GC_1729,(0,0):C.GC_1326,(0,11):C.GC_1569,(0,1):C.GC_435,(0,2):C.GC_192,(0,5):C.GC_1892,(0,3):C.GC_1891,(0,4):C.GC_1891,(0,10):C.GC_1488})

V_94 = Vertex(name = 'V_94',
              particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF8, L.FFFF9 ],
              couplings = {(0,6):C.GC_2380,(0,9):C.GC_1732,(0,7):C.GC_1731,(0,8):C.GC_1731,(0,0):C.GC_1327,(0,11):C.GC_1570,(0,1):C.GC_436,(0,2):C.GC_193,(0,5):C.GC_1894,(0,3):C.GC_1893,(0,4):C.GC_1893,(0,10):C.GC_1489})

V_95 = Vertex(name = 'V_95',
              particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
              couplings = {(0,2):C.GC_2057,(0,5):C.GC_437,(0,0):C.GC_194,(0,1):C.GC_32,(0,3):C.GC_275,(0,4):C.GC_2402})

V_96 = Vertex(name = 'V_96',
              particles = [ P.mu__plus__, P.e__minus__, P.d__tilde__, P.d ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
              couplings = {(0,2):C.GC_2066,(0,5):C.GC_438,(0,0):C.GC_203,(0,1):C.GC_41,(0,3):C.GC_284,(0,4):C.GC_2429})

V_97 = Vertex(name = 'V_97',
              particles = [ P.ta__plus__, P.e__minus__, P.d__tilde__, P.d ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
              couplings = {(0,2):C.GC_2075,(0,5):C.GC_439,(0,0):C.GC_212,(0,1):C.GC_50,(0,3):C.GC_293,(0,4):C.GC_2456})

V_98 = Vertex(name = 'V_98',
              particles = [ P.e__plus__, P.mu__minus__, P.d__tilde__, P.d ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
              couplings = {(0,2):C.GC_2084,(0,5):C.GC_440,(0,0):C.GC_221,(0,1):C.GC_59,(0,3):C.GC_302,(0,4):C.GC_2411})

V_99 = Vertex(name = 'V_99',
              particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
              couplings = {(0,2):C.GC_2093,(0,5):C.GC_441,(0,0):C.GC_230,(0,1):C.GC_68,(0,3):C.GC_311,(0,4):C.GC_2438})

V_100 = Vertex(name = 'V_100',
               particles = [ P.ta__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2102,(0,5):C.GC_442,(0,0):C.GC_239,(0,1):C.GC_77,(0,3):C.GC_320,(0,4):C.GC_2465})

V_101 = Vertex(name = 'V_101',
               particles = [ P.e__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2111,(0,5):C.GC_443,(0,0):C.GC_248,(0,1):C.GC_86,(0,3):C.GC_329,(0,4):C.GC_2420})

V_102 = Vertex(name = 'V_102',
               particles = [ P.mu__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2120,(0,5):C.GC_444,(0,0):C.GC_257,(0,1):C.GC_95,(0,3):C.GC_338,(0,4):C.GC_2447})

V_103 = Vertex(name = 'V_103',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2129,(0,5):C.GC_445,(0,0):C.GC_266,(0,1):C.GC_104,(0,3):C.GC_347,(0,4):C.GC_2474})

V_104 = Vertex(name = 'V_104',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2058,(0,5):C.GC_446,(0,0):C.GC_195,(0,1):C.GC_33,(0,3):C.GC_276,(0,4):C.GC_2405})

V_105 = Vertex(name = 'V_105',
               particles = [ P.mu__plus__, P.e__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2067,(0,5):C.GC_447,(0,0):C.GC_204,(0,1):C.GC_42,(0,3):C.GC_285,(0,4):C.GC_2432})

V_106 = Vertex(name = 'V_106',
               particles = [ P.ta__plus__, P.e__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2076,(0,5):C.GC_448,(0,0):C.GC_213,(0,1):C.GC_51,(0,3):C.GC_294,(0,4):C.GC_2459})

V_107 = Vertex(name = 'V_107',
               particles = [ P.e__plus__, P.mu__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2085,(0,5):C.GC_449,(0,0):C.GC_222,(0,1):C.GC_60,(0,3):C.GC_303,(0,4):C.GC_2414})

V_108 = Vertex(name = 'V_108',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2094,(0,5):C.GC_450,(0,0):C.GC_231,(0,1):C.GC_69,(0,3):C.GC_312,(0,4):C.GC_2441})

V_109 = Vertex(name = 'V_109',
               particles = [ P.ta__plus__, P.mu__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2103,(0,5):C.GC_451,(0,0):C.GC_240,(0,1):C.GC_78,(0,3):C.GC_321,(0,4):C.GC_2468})

V_110 = Vertex(name = 'V_110',
               particles = [ P.e__plus__, P.ta__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2112,(0,5):C.GC_452,(0,0):C.GC_249,(0,1):C.GC_87,(0,3):C.GC_330,(0,4):C.GC_2423})

V_111 = Vertex(name = 'V_111',
               particles = [ P.mu__plus__, P.ta__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2121,(0,5):C.GC_453,(0,0):C.GC_258,(0,1):C.GC_96,(0,3):C.GC_339,(0,4):C.GC_2450})

V_112 = Vertex(name = 'V_112',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2130,(0,5):C.GC_454,(0,0):C.GC_267,(0,1):C.GC_105,(0,3):C.GC_348,(0,4):C.GC_2477})

V_113 = Vertex(name = 'V_113',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2059,(0,5):C.GC_455,(0,0):C.GC_196,(0,1):C.GC_34,(0,3):C.GC_277,(0,4):C.GC_2408})

V_114 = Vertex(name = 'V_114',
               particles = [ P.mu__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2068,(0,5):C.GC_456,(0,0):C.GC_205,(0,1):C.GC_43,(0,3):C.GC_286,(0,4):C.GC_2435})

V_115 = Vertex(name = 'V_115',
               particles = [ P.ta__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2077,(0,5):C.GC_457,(0,0):C.GC_214,(0,1):C.GC_52,(0,3):C.GC_295,(0,4):C.GC_2462})

V_116 = Vertex(name = 'V_116',
               particles = [ P.e__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2086,(0,5):C.GC_458,(0,0):C.GC_223,(0,1):C.GC_61,(0,3):C.GC_304,(0,4):C.GC_2417})

V_117 = Vertex(name = 'V_117',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2095,(0,5):C.GC_459,(0,0):C.GC_232,(0,1):C.GC_70,(0,3):C.GC_313,(0,4):C.GC_2444})

V_118 = Vertex(name = 'V_118',
               particles = [ P.ta__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2104,(0,5):C.GC_460,(0,0):C.GC_241,(0,1):C.GC_79,(0,3):C.GC_322,(0,4):C.GC_2471})

V_119 = Vertex(name = 'V_119',
               particles = [ P.e__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2113,(0,5):C.GC_461,(0,0):C.GC_250,(0,1):C.GC_88,(0,3):C.GC_331,(0,4):C.GC_2426})

V_120 = Vertex(name = 'V_120',
               particles = [ P.mu__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2122,(0,5):C.GC_462,(0,0):C.GC_259,(0,1):C.GC_97,(0,3):C.GC_340,(0,4):C.GC_2453})

V_121 = Vertex(name = 'V_121',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2131,(0,5):C.GC_463,(0,0):C.GC_268,(0,1):C.GC_106,(0,3):C.GC_349,(0,4):C.GC_2480})

V_122 = Vertex(name = 'V_122',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2060,(0,5):C.GC_464,(0,0):C.GC_197,(0,1):C.GC_35,(0,3):C.GC_278,(0,4):C.GC_2403})

V_123 = Vertex(name = 'V_123',
               particles = [ P.mu__plus__, P.e__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2069,(0,5):C.GC_465,(0,0):C.GC_206,(0,1):C.GC_44,(0,3):C.GC_287,(0,4):C.GC_2430})

V_124 = Vertex(name = 'V_124',
               particles = [ P.ta__plus__, P.e__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2078,(0,5):C.GC_466,(0,0):C.GC_215,(0,1):C.GC_53,(0,3):C.GC_296,(0,4):C.GC_2457})

V_125 = Vertex(name = 'V_125',
               particles = [ P.e__plus__, P.mu__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2087,(0,5):C.GC_467,(0,0):C.GC_224,(0,1):C.GC_62,(0,3):C.GC_305,(0,4):C.GC_2412})

V_126 = Vertex(name = 'V_126',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2096,(0,5):C.GC_468,(0,0):C.GC_233,(0,1):C.GC_71,(0,3):C.GC_314,(0,4):C.GC_2439})

V_127 = Vertex(name = 'V_127',
               particles = [ P.ta__plus__, P.mu__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2105,(0,5):C.GC_469,(0,0):C.GC_242,(0,1):C.GC_80,(0,3):C.GC_323,(0,4):C.GC_2466})

V_128 = Vertex(name = 'V_128',
               particles = [ P.e__plus__, P.ta__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2114,(0,5):C.GC_470,(0,0):C.GC_251,(0,1):C.GC_89,(0,3):C.GC_332,(0,4):C.GC_2421})

V_129 = Vertex(name = 'V_129',
               particles = [ P.mu__plus__, P.ta__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2123,(0,5):C.GC_471,(0,0):C.GC_260,(0,1):C.GC_98,(0,3):C.GC_341,(0,4):C.GC_2448})

V_130 = Vertex(name = 'V_130',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2132,(0,5):C.GC_472,(0,0):C.GC_269,(0,1):C.GC_107,(0,3):C.GC_350,(0,4):C.GC_2475})

V_131 = Vertex(name = 'V_131',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2061,(0,5):C.GC_473,(0,0):C.GC_198,(0,1):C.GC_36,(0,3):C.GC_279,(0,4):C.GC_2406})

V_132 = Vertex(name = 'V_132',
               particles = [ P.mu__plus__, P.e__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2070,(0,5):C.GC_474,(0,0):C.GC_207,(0,1):C.GC_45,(0,3):C.GC_288,(0,4):C.GC_2433})

V_133 = Vertex(name = 'V_133',
               particles = [ P.ta__plus__, P.e__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2079,(0,5):C.GC_475,(0,0):C.GC_216,(0,1):C.GC_54,(0,3):C.GC_297,(0,4):C.GC_2460})

V_134 = Vertex(name = 'V_134',
               particles = [ P.e__plus__, P.mu__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2088,(0,5):C.GC_476,(0,0):C.GC_225,(0,1):C.GC_63,(0,3):C.GC_306,(0,4):C.GC_2415})

V_135 = Vertex(name = 'V_135',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2097,(0,5):C.GC_477,(0,0):C.GC_234,(0,1):C.GC_72,(0,3):C.GC_315,(0,4):C.GC_2442})

V_136 = Vertex(name = 'V_136',
               particles = [ P.ta__plus__, P.mu__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2106,(0,5):C.GC_478,(0,0):C.GC_243,(0,1):C.GC_81,(0,3):C.GC_324,(0,4):C.GC_2469})

V_137 = Vertex(name = 'V_137',
               particles = [ P.e__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2115,(0,5):C.GC_479,(0,0):C.GC_252,(0,1):C.GC_90,(0,3):C.GC_333,(0,4):C.GC_2424})

V_138 = Vertex(name = 'V_138',
               particles = [ P.mu__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2124,(0,5):C.GC_480,(0,0):C.GC_261,(0,1):C.GC_99,(0,3):C.GC_342,(0,4):C.GC_2451})

V_139 = Vertex(name = 'V_139',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2133,(0,5):C.GC_481,(0,0):C.GC_270,(0,1):C.GC_108,(0,3):C.GC_351,(0,4):C.GC_2478})

V_140 = Vertex(name = 'V_140',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2062,(0,5):C.GC_482,(0,0):C.GC_199,(0,1):C.GC_37,(0,3):C.GC_280,(0,4):C.GC_2409})

V_141 = Vertex(name = 'V_141',
               particles = [ P.mu__plus__, P.e__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2071,(0,5):C.GC_483,(0,0):C.GC_208,(0,1):C.GC_46,(0,3):C.GC_289,(0,4):C.GC_2436})

V_142 = Vertex(name = 'V_142',
               particles = [ P.ta__plus__, P.e__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2080,(0,5):C.GC_484,(0,0):C.GC_217,(0,1):C.GC_55,(0,3):C.GC_298,(0,4):C.GC_2463})

V_143 = Vertex(name = 'V_143',
               particles = [ P.e__plus__, P.mu__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2089,(0,5):C.GC_485,(0,0):C.GC_226,(0,1):C.GC_64,(0,3):C.GC_307,(0,4):C.GC_2418})

V_144 = Vertex(name = 'V_144',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2098,(0,5):C.GC_486,(0,0):C.GC_235,(0,1):C.GC_73,(0,3):C.GC_316,(0,4):C.GC_2445})

V_145 = Vertex(name = 'V_145',
               particles = [ P.ta__plus__, P.mu__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2107,(0,5):C.GC_487,(0,0):C.GC_244,(0,1):C.GC_82,(0,3):C.GC_325,(0,4):C.GC_2472})

V_146 = Vertex(name = 'V_146',
               particles = [ P.e__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2116,(0,5):C.GC_488,(0,0):C.GC_253,(0,1):C.GC_91,(0,3):C.GC_334,(0,4):C.GC_2427})

V_147 = Vertex(name = 'V_147',
               particles = [ P.mu__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2125,(0,5):C.GC_489,(0,0):C.GC_262,(0,1):C.GC_100,(0,3):C.GC_343,(0,4):C.GC_2454})

V_148 = Vertex(name = 'V_148',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2134,(0,5):C.GC_490,(0,0):C.GC_271,(0,1):C.GC_109,(0,3):C.GC_352,(0,4):C.GC_2481})

V_149 = Vertex(name = 'V_149',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2063,(0,5):C.GC_491,(0,0):C.GC_200,(0,1):C.GC_38,(0,3):C.GC_281,(0,4):C.GC_2404})

V_150 = Vertex(name = 'V_150',
               particles = [ P.mu__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2072,(0,5):C.GC_492,(0,0):C.GC_209,(0,1):C.GC_47,(0,3):C.GC_290,(0,4):C.GC_2431})

V_151 = Vertex(name = 'V_151',
               particles = [ P.ta__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2081,(0,5):C.GC_493,(0,0):C.GC_218,(0,1):C.GC_56,(0,3):C.GC_299,(0,4):C.GC_2458})

V_152 = Vertex(name = 'V_152',
               particles = [ P.e__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2090,(0,5):C.GC_494,(0,0):C.GC_227,(0,1):C.GC_65,(0,3):C.GC_308,(0,4):C.GC_2413})

V_153 = Vertex(name = 'V_153',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2099,(0,5):C.GC_495,(0,0):C.GC_236,(0,1):C.GC_74,(0,3):C.GC_317,(0,4):C.GC_2440})

V_154 = Vertex(name = 'V_154',
               particles = [ P.ta__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2108,(0,5):C.GC_496,(0,0):C.GC_245,(0,1):C.GC_83,(0,3):C.GC_326,(0,4):C.GC_2467})

V_155 = Vertex(name = 'V_155',
               particles = [ P.e__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2117,(0,5):C.GC_497,(0,0):C.GC_254,(0,1):C.GC_92,(0,3):C.GC_335,(0,4):C.GC_2422})

V_156 = Vertex(name = 'V_156',
               particles = [ P.mu__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2126,(0,5):C.GC_498,(0,0):C.GC_263,(0,1):C.GC_101,(0,3):C.GC_344,(0,4):C.GC_2449})

V_157 = Vertex(name = 'V_157',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2135,(0,5):C.GC_499,(0,0):C.GC_272,(0,1):C.GC_110,(0,3):C.GC_353,(0,4):C.GC_2476})

V_158 = Vertex(name = 'V_158',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2064,(0,5):C.GC_500,(0,0):C.GC_201,(0,1):C.GC_39,(0,3):C.GC_282,(0,4):C.GC_2407})

V_159 = Vertex(name = 'V_159',
               particles = [ P.mu__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2073,(0,5):C.GC_501,(0,0):C.GC_210,(0,1):C.GC_48,(0,3):C.GC_291,(0,4):C.GC_2434})

V_160 = Vertex(name = 'V_160',
               particles = [ P.ta__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2082,(0,5):C.GC_502,(0,0):C.GC_219,(0,1):C.GC_57,(0,3):C.GC_300,(0,4):C.GC_2461})

V_161 = Vertex(name = 'V_161',
               particles = [ P.e__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2091,(0,5):C.GC_503,(0,0):C.GC_228,(0,1):C.GC_66,(0,3):C.GC_309,(0,4):C.GC_2416})

V_162 = Vertex(name = 'V_162',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2100,(0,5):C.GC_504,(0,0):C.GC_237,(0,1):C.GC_75,(0,3):C.GC_318,(0,4):C.GC_2443})

V_163 = Vertex(name = 'V_163',
               particles = [ P.ta__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2109,(0,5):C.GC_505,(0,0):C.GC_246,(0,1):C.GC_84,(0,3):C.GC_327,(0,4):C.GC_2470})

V_164 = Vertex(name = 'V_164',
               particles = [ P.e__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2118,(0,5):C.GC_506,(0,0):C.GC_255,(0,1):C.GC_93,(0,3):C.GC_336,(0,4):C.GC_2425})

V_165 = Vertex(name = 'V_165',
               particles = [ P.mu__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2127,(0,5):C.GC_507,(0,0):C.GC_264,(0,1):C.GC_102,(0,3):C.GC_345,(0,4):C.GC_2452})

V_166 = Vertex(name = 'V_166',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2136,(0,5):C.GC_508,(0,0):C.GC_273,(0,1):C.GC_111,(0,3):C.GC_354,(0,4):C.GC_2479})

V_167 = Vertex(name = 'V_167',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2065,(0,5):C.GC_509,(0,0):C.GC_202,(0,1):C.GC_40,(0,3):C.GC_283,(0,4):C.GC_2410})

V_168 = Vertex(name = 'V_168',
               particles = [ P.mu__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2074,(0,5):C.GC_510,(0,0):C.GC_211,(0,1):C.GC_49,(0,3):C.GC_292,(0,4):C.GC_2437})

V_169 = Vertex(name = 'V_169',
               particles = [ P.ta__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2083,(0,5):C.GC_511,(0,0):C.GC_220,(0,1):C.GC_58,(0,3):C.GC_301,(0,4):C.GC_2464})

V_170 = Vertex(name = 'V_170',
               particles = [ P.e__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2092,(0,5):C.GC_512,(0,0):C.GC_229,(0,1):C.GC_67,(0,3):C.GC_310,(0,4):C.GC_2419})

V_171 = Vertex(name = 'V_171',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2101,(0,5):C.GC_513,(0,0):C.GC_238,(0,1):C.GC_76,(0,3):C.GC_319,(0,4):C.GC_2446})

V_172 = Vertex(name = 'V_172',
               particles = [ P.ta__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2110,(0,5):C.GC_514,(0,0):C.GC_247,(0,1):C.GC_85,(0,3):C.GC_328,(0,4):C.GC_2473})

V_173 = Vertex(name = 'V_173',
               particles = [ P.e__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2119,(0,5):C.GC_515,(0,0):C.GC_256,(0,1):C.GC_94,(0,3):C.GC_337,(0,4):C.GC_2428})

V_174 = Vertex(name = 'V_174',
               particles = [ P.mu__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2128,(0,5):C.GC_516,(0,0):C.GC_265,(0,1):C.GC_103,(0,3):C.GC_346,(0,4):C.GC_2455})

V_175 = Vertex(name = 'V_175',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_2137,(0,5):C.GC_517,(0,0):C.GC_274,(0,1):C.GC_112,(0,3):C.GC_355,(0,4):C.GC_2482})

V_176 = Vertex(name = 'V_176',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_518,(0,2):C.GC_600,(0,0):C.GC_599,(0,1):C.GC_599,(0,4):C.GC_1895,(0,5):C.GC_1976})

V_177 = Vertex(name = 'V_177',
               particles = [ P.c__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_519,(0,2):C.GC_602,(0,0):C.GC_601,(0,1):C.GC_601,(0,4):C.GC_1896,(0,5):C.GC_1977})

V_178 = Vertex(name = 'V_178',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_520,(0,2):C.GC_604,(0,0):C.GC_603,(0,1):C.GC_603,(0,4):C.GC_1897,(0,5):C.GC_1978})

V_179 = Vertex(name = 'V_179',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_521,(0,2):C.GC_606,(0,0):C.GC_605,(0,1):C.GC_605,(0,4):C.GC_1898,(0,5):C.GC_1979})

V_180 = Vertex(name = 'V_180',
               particles = [ P.c__tilde__, P.d, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_522,(0,2):C.GC_608,(0,0):C.GC_607,(0,1):C.GC_607,(0,4):C.GC_1899,(0,5):C.GC_1980})

V_181 = Vertex(name = 'V_181',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_523,(0,1):C.GC_609,(0,2):C.GC_610,(0,0):C.GC_609,(0,4):C.GC_1900,(0,5):C.GC_1981})

V_182 = Vertex(name = 'V_182',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_524,(0,2):C.GC_612,(0,0):C.GC_611,(0,1):C.GC_611,(0,4):C.GC_1901,(0,5):C.GC_1982})

V_183 = Vertex(name = 'V_183',
               particles = [ P.c__tilde__, P.d, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_525,(0,2):C.GC_614,(0,0):C.GC_613,(0,1):C.GC_613,(0,4):C.GC_1902,(0,5):C.GC_1983})

V_184 = Vertex(name = 'V_184',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_526,(0,2):C.GC_616,(0,0):C.GC_615,(0,1):C.GC_615,(0,4):C.GC_1903,(0,5):C.GC_1984})

V_185 = Vertex(name = 'V_185',
               particles = [ P.u__tilde__, P.d, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_527,(0,2):C.GC_618,(0,0):C.GC_617,(0,1):C.GC_617,(0,4):C.GC_1904,(0,5):C.GC_1985})

V_186 = Vertex(name = 'V_186',
               particles = [ P.c__tilde__, P.d, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_528,(0,2):C.GC_620,(0,0):C.GC_619,(0,1):C.GC_619,(0,4):C.GC_1905,(0,5):C.GC_1986})

V_187 = Vertex(name = 'V_187',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_529,(0,2):C.GC_622,(0,0):C.GC_621,(0,1):C.GC_621,(0,4):C.GC_1906,(0,5):C.GC_1987})

V_188 = Vertex(name = 'V_188',
               particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_530,(0,2):C.GC_624,(0,0):C.GC_623,(0,1):C.GC_623,(0,4):C.GC_1907,(0,5):C.GC_1988})

V_189 = Vertex(name = 'V_189',
               particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_531,(0,2):C.GC_626,(0,0):C.GC_625,(0,1):C.GC_625,(0,4):C.GC_1908,(0,5):C.GC_1989})

V_190 = Vertex(name = 'V_190',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_532,(0,2):C.GC_628,(0,0):C.GC_627,(0,1):C.GC_627,(0,4):C.GC_1909,(0,5):C.GC_1990})

V_191 = Vertex(name = 'V_191',
               particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_533,(0,2):C.GC_630,(0,0):C.GC_629,(0,1):C.GC_629,(0,4):C.GC_1910,(0,5):C.GC_1991})

V_192 = Vertex(name = 'V_192',
               particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_534,(0,2):C.GC_632,(0,0):C.GC_631,(0,1):C.GC_631,(0,4):C.GC_1911,(0,5):C.GC_1992})

V_193 = Vertex(name = 'V_193',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_535,(0,2):C.GC_634,(0,0):C.GC_633,(0,1):C.GC_633,(0,4):C.GC_1912,(0,5):C.GC_1993})

V_194 = Vertex(name = 'V_194',
               particles = [ P.u__tilde__, P.d, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_536,(0,2):C.GC_636,(0,0):C.GC_635,(0,1):C.GC_635,(0,4):C.GC_1913,(0,5):C.GC_1994})

V_195 = Vertex(name = 'V_195',
               particles = [ P.c__tilde__, P.d, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_537,(0,2):C.GC_638,(0,0):C.GC_637,(0,1):C.GC_637,(0,4):C.GC_1914,(0,5):C.GC_1995})

V_196 = Vertex(name = 'V_196',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_538,(0,2):C.GC_640,(0,0):C.GC_639,(0,1):C.GC_639,(0,4):C.GC_1915,(0,5):C.GC_1996})

V_197 = Vertex(name = 'V_197',
               particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_539,(0,2):C.GC_642,(0,0):C.GC_641,(0,1):C.GC_641,(0,4):C.GC_1916,(0,5):C.GC_1997})

V_198 = Vertex(name = 'V_198',
               particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_540,(0,2):C.GC_644,(0,0):C.GC_643,(0,1):C.GC_643,(0,4):C.GC_1917,(0,5):C.GC_1998})

V_199 = Vertex(name = 'V_199',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_541,(0,2):C.GC_646,(0,0):C.GC_645,(0,1):C.GC_645,(0,4):C.GC_1918,(0,5):C.GC_1999})

V_200 = Vertex(name = 'V_200',
               particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_542,(0,2):C.GC_648,(0,0):C.GC_647,(0,1):C.GC_647,(0,4):C.GC_1919,(0,5):C.GC_2000})

V_201 = Vertex(name = 'V_201',
               particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_543,(0,2):C.GC_650,(0,0):C.GC_649,(0,1):C.GC_649,(0,4):C.GC_1920,(0,5):C.GC_2001})

V_202 = Vertex(name = 'V_202',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_544,(0,2):C.GC_652,(0,0):C.GC_651,(0,1):C.GC_651,(0,4):C.GC_1921,(0,5):C.GC_2002})

V_203 = Vertex(name = 'V_203',
               particles = [ P.u__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_545,(0,2):C.GC_654,(0,0):C.GC_653,(0,1):C.GC_653,(0,4):C.GC_1922,(0,5):C.GC_2003})

V_204 = Vertex(name = 'V_204',
               particles = [ P.c__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_546,(0,2):C.GC_656,(0,0):C.GC_655,(0,1):C.GC_655,(0,4):C.GC_1923,(0,5):C.GC_2004})

V_205 = Vertex(name = 'V_205',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_547,(0,2):C.GC_658,(0,0):C.GC_657,(0,1):C.GC_657,(0,4):C.GC_1924,(0,5):C.GC_2005})

V_206 = Vertex(name = 'V_206',
               particles = [ P.u__tilde__, P.s, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_548,(0,2):C.GC_660,(0,0):C.GC_659,(0,1):C.GC_659,(0,4):C.GC_1925,(0,5):C.GC_2006})

V_207 = Vertex(name = 'V_207',
               particles = [ P.c__tilde__, P.s, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_549,(0,2):C.GC_662,(0,0):C.GC_661,(0,1):C.GC_661,(0,4):C.GC_1926,(0,5):C.GC_2007})

V_208 = Vertex(name = 'V_208',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_550,(0,2):C.GC_664,(0,0):C.GC_663,(0,1):C.GC_663,(0,4):C.GC_1927,(0,5):C.GC_2008})

V_209 = Vertex(name = 'V_209',
               particles = [ P.u__tilde__, P.s, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_551,(0,2):C.GC_666,(0,0):C.GC_665,(0,1):C.GC_665,(0,4):C.GC_1928,(0,5):C.GC_2009})

V_210 = Vertex(name = 'V_210',
               particles = [ P.c__tilde__, P.s, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_552,(0,2):C.GC_668,(0,0):C.GC_667,(0,1):C.GC_667,(0,4):C.GC_1929,(0,5):C.GC_2010})

V_211 = Vertex(name = 'V_211',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_553,(0,2):C.GC_670,(0,0):C.GC_669,(0,1):C.GC_669,(0,4):C.GC_1930,(0,5):C.GC_2011})

V_212 = Vertex(name = 'V_212',
               particles = [ P.u__tilde__, P.s, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_554,(0,2):C.GC_672,(0,0):C.GC_671,(0,1):C.GC_671,(0,4):C.GC_1931,(0,5):C.GC_2012})

V_213 = Vertex(name = 'V_213',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_555,(0,2):C.GC_674,(0,0):C.GC_673,(0,1):C.GC_673,(0,4):C.GC_1932,(0,5):C.GC_2013})

V_214 = Vertex(name = 'V_214',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_556,(0,2):C.GC_676,(0,0):C.GC_675,(0,1):C.GC_675,(0,4):C.GC_1933,(0,5):C.GC_2014})

V_215 = Vertex(name = 'V_215',
               particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_557,(0,2):C.GC_678,(0,0):C.GC_677,(0,1):C.GC_677,(0,4):C.GC_1934,(0,5):C.GC_2015})

V_216 = Vertex(name = 'V_216',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_558,(0,2):C.GC_680,(0,0):C.GC_679,(0,1):C.GC_679,(0,4):C.GC_1935,(0,5):C.GC_2016})

V_217 = Vertex(name = 'V_217',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_559,(0,2):C.GC_682,(0,0):C.GC_681,(0,1):C.GC_681,(0,4):C.GC_1936,(0,5):C.GC_2017})

V_218 = Vertex(name = 'V_218',
               particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_560,(0,2):C.GC_684,(0,0):C.GC_683,(0,1):C.GC_683,(0,4):C.GC_1937,(0,5):C.GC_2018})

V_219 = Vertex(name = 'V_219',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_561,(0,2):C.GC_686,(0,0):C.GC_685,(0,1):C.GC_685,(0,4):C.GC_1938,(0,5):C.GC_2019})

V_220 = Vertex(name = 'V_220',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_562,(0,2):C.GC_688,(0,0):C.GC_687,(0,1):C.GC_687,(0,4):C.GC_1939,(0,5):C.GC_2020})

V_221 = Vertex(name = 'V_221',
               particles = [ P.u__tilde__, P.s, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_563,(0,2):C.GC_690,(0,0):C.GC_689,(0,1):C.GC_689,(0,4):C.GC_1940,(0,5):C.GC_2021})

V_222 = Vertex(name = 'V_222',
               particles = [ P.c__tilde__, P.s, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_564,(0,2):C.GC_692,(0,0):C.GC_691,(0,1):C.GC_691,(0,4):C.GC_1941,(0,5):C.GC_2022})

V_223 = Vertex(name = 'V_223',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_565,(0,2):C.GC_694,(0,0):C.GC_693,(0,1):C.GC_693,(0,4):C.GC_1942,(0,5):C.GC_2023})

V_224 = Vertex(name = 'V_224',
               particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_566,(0,2):C.GC_696,(0,0):C.GC_695,(0,1):C.GC_695,(0,4):C.GC_1943,(0,5):C.GC_2024})

V_225 = Vertex(name = 'V_225',
               particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_567,(0,2):C.GC_698,(0,0):C.GC_697,(0,1):C.GC_697,(0,4):C.GC_1944,(0,5):C.GC_2025})

V_226 = Vertex(name = 'V_226',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_568,(0,2):C.GC_700,(0,0):C.GC_699,(0,1):C.GC_699,(0,4):C.GC_1945,(0,5):C.GC_2026})

V_227 = Vertex(name = 'V_227',
               particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_569,(0,2):C.GC_702,(0,0):C.GC_701,(0,1):C.GC_701,(0,4):C.GC_1946,(0,5):C.GC_2027})

V_228 = Vertex(name = 'V_228',
               particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_570,(0,2):C.GC_704,(0,0):C.GC_703,(0,1):C.GC_703,(0,4):C.GC_1947,(0,5):C.GC_2028})

V_229 = Vertex(name = 'V_229',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_571,(0,2):C.GC_706,(0,0):C.GC_705,(0,1):C.GC_705,(0,4):C.GC_1948,(0,5):C.GC_2029})

V_230 = Vertex(name = 'V_230',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_572,(0,2):C.GC_708,(0,0):C.GC_707,(0,1):C.GC_707,(0,4):C.GC_1949,(0,5):C.GC_2030})

V_231 = Vertex(name = 'V_231',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_573,(0,2):C.GC_710,(0,0):C.GC_709,(0,1):C.GC_709,(0,4):C.GC_1950,(0,5):C.GC_2031})

V_232 = Vertex(name = 'V_232',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_574,(0,2):C.GC_712,(0,0):C.GC_711,(0,1):C.GC_711,(0,4):C.GC_1951,(0,5):C.GC_2032})

V_233 = Vertex(name = 'V_233',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_575,(0,2):C.GC_714,(0,0):C.GC_713,(0,1):C.GC_713,(0,4):C.GC_1952,(0,5):C.GC_2033})

V_234 = Vertex(name = 'V_234',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_576,(0,2):C.GC_716,(0,0):C.GC_715,(0,1):C.GC_715,(0,4):C.GC_1953,(0,5):C.GC_2034})

V_235 = Vertex(name = 'V_235',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_577,(0,2):C.GC_718,(0,0):C.GC_717,(0,1):C.GC_717,(0,4):C.GC_1954,(0,5):C.GC_2035})

V_236 = Vertex(name = 'V_236',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_578,(0,2):C.GC_720,(0,0):C.GC_719,(0,1):C.GC_719,(0,4):C.GC_1955,(0,5):C.GC_2036})

V_237 = Vertex(name = 'V_237',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_579,(0,2):C.GC_722,(0,0):C.GC_721,(0,1):C.GC_721,(0,4):C.GC_1956,(0,5):C.GC_2037})

V_238 = Vertex(name = 'V_238',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_580,(0,2):C.GC_724,(0,0):C.GC_723,(0,1):C.GC_723,(0,4):C.GC_1957,(0,5):C.GC_2038})

V_239 = Vertex(name = 'V_239',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_581,(0,0):C.GC_725,(0,1):C.GC_725,(0,2):C.GC_726,(0,4):C.GC_1958,(0,5):C.GC_2039})

V_240 = Vertex(name = 'V_240',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_582,(0,2):C.GC_728,(0,0):C.GC_727,(0,1):C.GC_727,(0,4):C.GC_1959,(0,5):C.GC_2040})

V_241 = Vertex(name = 'V_241',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_583,(0,2):C.GC_730,(0,0):C.GC_729,(0,1):C.GC_729,(0,4):C.GC_1960,(0,5):C.GC_2041})

V_242 = Vertex(name = 'V_242',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_584,(0,2):C.GC_732,(0,0):C.GC_731,(0,1):C.GC_731,(0,4):C.GC_1961,(0,5):C.GC_2042})

V_243 = Vertex(name = 'V_243',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_585,(0,2):C.GC_734,(0,0):C.GC_733,(0,1):C.GC_733,(0,4):C.GC_1962,(0,5):C.GC_2043})

V_244 = Vertex(name = 'V_244',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_586,(0,2):C.GC_736,(0,0):C.GC_735,(0,1):C.GC_735,(0,4):C.GC_1963,(0,5):C.GC_2044})

V_245 = Vertex(name = 'V_245',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_587,(0,2):C.GC_738,(0,0):C.GC_737,(0,1):C.GC_737,(0,4):C.GC_1964,(0,5):C.GC_2045})

V_246 = Vertex(name = 'V_246',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_588,(0,2):C.GC_740,(0,0):C.GC_739,(0,1):C.GC_739,(0,4):C.GC_1965,(0,5):C.GC_2046})

V_247 = Vertex(name = 'V_247',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_589,(0,2):C.GC_742,(0,0):C.GC_741,(0,1):C.GC_741,(0,4):C.GC_1966,(0,5):C.GC_2047})

V_248 = Vertex(name = 'V_248',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_590,(0,2):C.GC_744,(0,0):C.GC_743,(0,1):C.GC_743,(0,4):C.GC_1967,(0,5):C.GC_2048})

V_249 = Vertex(name = 'V_249',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_591,(0,2):C.GC_746,(0,0):C.GC_745,(0,1):C.GC_745,(0,4):C.GC_1968,(0,5):C.GC_2049})

V_250 = Vertex(name = 'V_250',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_592,(0,2):C.GC_748,(0,0):C.GC_747,(0,1):C.GC_747,(0,4):C.GC_1969,(0,5):C.GC_2050})

V_251 = Vertex(name = 'V_251',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_593,(0,2):C.GC_750,(0,0):C.GC_749,(0,1):C.GC_749,(0,4):C.GC_1970,(0,5):C.GC_2051})

V_252 = Vertex(name = 'V_252',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_594,(0,2):C.GC_752,(0,0):C.GC_751,(0,1):C.GC_751,(0,4):C.GC_1971,(0,5):C.GC_2052})

V_253 = Vertex(name = 'V_253',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_595,(0,2):C.GC_754,(0,0):C.GC_753,(0,1):C.GC_753,(0,4):C.GC_1972,(0,5):C.GC_2053})

V_254 = Vertex(name = 'V_254',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_596,(0,2):C.GC_756,(0,0):C.GC_755,(0,1):C.GC_755,(0,4):C.GC_1973,(0,5):C.GC_2054})

V_255 = Vertex(name = 'V_255',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_597,(0,2):C.GC_758,(0,0):C.GC_757,(0,1):C.GC_757,(0,4):C.GC_1974,(0,5):C.GC_2055})

V_256 = Vertex(name = 'V_256',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF7, L.FFFF8 ],
               couplings = {(0,3):C.GC_598,(0,2):C.GC_760,(0,0):C.GC_759,(0,1):C.GC_759,(0,4):C.GC_1975,(0,5):C.GC_2056})

V_257 = Vertex(name = 'V_257',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_923,(0,4):C.GC_1005,(0,2):C.GC_1004,(0,3):C.GC_1004,(0,0):C.GC_761,(0,5):C.GC_842})

V_258 = Vertex(name = 'V_258',
               particles = [ P.vm__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_924,(0,4):C.GC_1007,(0,2):C.GC_1006,(0,3):C.GC_1006,(0,0):C.GC_762,(0,5):C.GC_843})

V_259 = Vertex(name = 'V_259',
               particles = [ P.vt__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_925,(0,4):C.GC_1009,(0,2):C.GC_1008,(0,3):C.GC_1008,(0,0):C.GC_763,(0,5):C.GC_844})

V_260 = Vertex(name = 'V_260',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_926,(0,4):C.GC_1011,(0,2):C.GC_1010,(0,3):C.GC_1010,(0,0):C.GC_764,(0,5):C.GC_845})

V_261 = Vertex(name = 'V_261',
               particles = [ P.vm__tilde__, P.e__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_927,(0,4):C.GC_1013,(0,2):C.GC_1012,(0,3):C.GC_1012,(0,0):C.GC_765,(0,5):C.GC_846})

V_262 = Vertex(name = 'V_262',
               particles = [ P.vt__tilde__, P.e__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_928,(0,4):C.GC_1015,(0,2):C.GC_1014,(0,3):C.GC_1014,(0,0):C.GC_766,(0,5):C.GC_847})

V_263 = Vertex(name = 'V_263',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_929,(0,4):C.GC_1017,(0,2):C.GC_1016,(0,3):C.GC_1016,(0,0):C.GC_767,(0,5):C.GC_848})

V_264 = Vertex(name = 'V_264',
               particles = [ P.vm__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_930,(0,4):C.GC_1019,(0,2):C.GC_1018,(0,3):C.GC_1018,(0,0):C.GC_768,(0,5):C.GC_849})

V_265 = Vertex(name = 'V_265',
               particles = [ P.vt__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_931,(0,4):C.GC_1021,(0,2):C.GC_1020,(0,3):C.GC_1020,(0,0):C.GC_769,(0,5):C.GC_850})

V_266 = Vertex(name = 'V_266',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_932,(0,4):C.GC_1023,(0,2):C.GC_1022,(0,3):C.GC_1022,(0,0):C.GC_770,(0,5):C.GC_851})

V_267 = Vertex(name = 'V_267',
               particles = [ P.vm__tilde__, P.e__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_933,(0,4):C.GC_1025,(0,2):C.GC_1024,(0,3):C.GC_1024,(0,0):C.GC_771,(0,5):C.GC_852})

V_268 = Vertex(name = 'V_268',
               particles = [ P.vt__tilde__, P.e__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_934,(0,4):C.GC_1027,(0,2):C.GC_1026,(0,3):C.GC_1026,(0,0):C.GC_772,(0,5):C.GC_853})

V_269 = Vertex(name = 'V_269',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_935,(0,4):C.GC_1029,(0,2):C.GC_1028,(0,3):C.GC_1028,(0,0):C.GC_773,(0,5):C.GC_854})

V_270 = Vertex(name = 'V_270',
               particles = [ P.vm__tilde__, P.e__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_936,(0,4):C.GC_1031,(0,2):C.GC_1030,(0,3):C.GC_1030,(0,0):C.GC_774,(0,5):C.GC_855})

V_271 = Vertex(name = 'V_271',
               particles = [ P.vt__tilde__, P.e__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_937,(0,4):C.GC_1033,(0,2):C.GC_1032,(0,3):C.GC_1032,(0,0):C.GC_775,(0,5):C.GC_856})

V_272 = Vertex(name = 'V_272',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_938,(0,4):C.GC_1035,(0,2):C.GC_1034,(0,3):C.GC_1034,(0,0):C.GC_776,(0,5):C.GC_857})

V_273 = Vertex(name = 'V_273',
               particles = [ P.vm__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_939,(0,4):C.GC_1037,(0,2):C.GC_1036,(0,3):C.GC_1036,(0,0):C.GC_777,(0,5):C.GC_858})

V_274 = Vertex(name = 'V_274',
               particles = [ P.vt__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_940,(0,4):C.GC_1039,(0,2):C.GC_1038,(0,3):C.GC_1038,(0,0):C.GC_778,(0,5):C.GC_859})

V_275 = Vertex(name = 'V_275',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_941,(0,4):C.GC_1041,(0,2):C.GC_1040,(0,3):C.GC_1040,(0,0):C.GC_779,(0,5):C.GC_860})

V_276 = Vertex(name = 'V_276',
               particles = [ P.vm__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_942,(0,4):C.GC_1043,(0,2):C.GC_1042,(0,3):C.GC_1042,(0,0):C.GC_780,(0,5):C.GC_861})

V_277 = Vertex(name = 'V_277',
               particles = [ P.vt__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_943,(0,4):C.GC_1045,(0,2):C.GC_1044,(0,3):C.GC_1044,(0,0):C.GC_781,(0,5):C.GC_862})

V_278 = Vertex(name = 'V_278',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_944,(0,4):C.GC_1047,(0,2):C.GC_1046,(0,3):C.GC_1046,(0,0):C.GC_782,(0,5):C.GC_863})

V_279 = Vertex(name = 'V_279',
               particles = [ P.vm__tilde__, P.e__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_945,(0,4):C.GC_1049,(0,2):C.GC_1048,(0,3):C.GC_1048,(0,0):C.GC_783,(0,5):C.GC_864})

V_280 = Vertex(name = 'V_280',
               particles = [ P.vt__tilde__, P.e__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_946,(0,4):C.GC_1051,(0,2):C.GC_1050,(0,3):C.GC_1050,(0,0):C.GC_784,(0,5):C.GC_865})

V_281 = Vertex(name = 'V_281',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_947,(0,4):C.GC_1053,(0,2):C.GC_1052,(0,3):C.GC_1052,(0,0):C.GC_785,(0,5):C.GC_866})

V_282 = Vertex(name = 'V_282',
               particles = [ P.vm__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_948,(0,4):C.GC_1055,(0,2):C.GC_1054,(0,3):C.GC_1054,(0,0):C.GC_786,(0,5):C.GC_867})

V_283 = Vertex(name = 'V_283',
               particles = [ P.vt__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_949,(0,4):C.GC_1057,(0,2):C.GC_1056,(0,3):C.GC_1056,(0,0):C.GC_787,(0,5):C.GC_868})

V_284 = Vertex(name = 'V_284',
               particles = [ P.ve__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_950,(0,4):C.GC_1059,(0,2):C.GC_1058,(0,3):C.GC_1058,(0,0):C.GC_788,(0,5):C.GC_869})

V_285 = Vertex(name = 'V_285',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_951,(0,4):C.GC_1061,(0,2):C.GC_1060,(0,3):C.GC_1060,(0,0):C.GC_789,(0,5):C.GC_870})

V_286 = Vertex(name = 'V_286',
               particles = [ P.vt__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_952,(0,4):C.GC_1063,(0,2):C.GC_1062,(0,3):C.GC_1062,(0,0):C.GC_790,(0,5):C.GC_871})

V_287 = Vertex(name = 'V_287',
               particles = [ P.ve__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_953,(0,4):C.GC_1065,(0,2):C.GC_1064,(0,3):C.GC_1064,(0,0):C.GC_791,(0,5):C.GC_872})

V_288 = Vertex(name = 'V_288',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_954,(0,4):C.GC_1067,(0,2):C.GC_1066,(0,3):C.GC_1066,(0,0):C.GC_792,(0,5):C.GC_873})

V_289 = Vertex(name = 'V_289',
               particles = [ P.vt__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_955,(0,4):C.GC_1069,(0,2):C.GC_1068,(0,3):C.GC_1068,(0,0):C.GC_793,(0,5):C.GC_874})

V_290 = Vertex(name = 'V_290',
               particles = [ P.ve__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_956,(0,4):C.GC_1071,(0,2):C.GC_1070,(0,3):C.GC_1070,(0,0):C.GC_794,(0,5):C.GC_875})

V_291 = Vertex(name = 'V_291',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_957,(0,4):C.GC_1073,(0,2):C.GC_1072,(0,3):C.GC_1072,(0,0):C.GC_795,(0,5):C.GC_876})

V_292 = Vertex(name = 'V_292',
               particles = [ P.vt__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_958,(0,4):C.GC_1075,(0,2):C.GC_1074,(0,3):C.GC_1074,(0,0):C.GC_796,(0,5):C.GC_877})

V_293 = Vertex(name = 'V_293',
               particles = [ P.ve__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_959,(0,4):C.GC_1077,(0,2):C.GC_1076,(0,3):C.GC_1076,(0,0):C.GC_797,(0,5):C.GC_878})

V_294 = Vertex(name = 'V_294',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_960,(0,4):C.GC_1079,(0,2):C.GC_1078,(0,3):C.GC_1078,(0,0):C.GC_798,(0,5):C.GC_879})

V_295 = Vertex(name = 'V_295',
               particles = [ P.vt__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_961,(0,4):C.GC_1081,(0,2):C.GC_1080,(0,3):C.GC_1080,(0,0):C.GC_799,(0,5):C.GC_880})

V_296 = Vertex(name = 'V_296',
               particles = [ P.ve__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_962,(0,4):C.GC_1083,(0,2):C.GC_1082,(0,3):C.GC_1082,(0,0):C.GC_800,(0,5):C.GC_881})

V_297 = Vertex(name = 'V_297',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,2):C.GC_1084,(0,3):C.GC_1084,(0,1):C.GC_963,(0,4):C.GC_1085,(0,0):C.GC_801,(0,5):C.GC_882})

V_298 = Vertex(name = 'V_298',
               particles = [ P.vt__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_964,(0,4):C.GC_1087,(0,2):C.GC_1086,(0,3):C.GC_1086,(0,0):C.GC_802,(0,5):C.GC_883})

V_299 = Vertex(name = 'V_299',
               particles = [ P.ve__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_965,(0,4):C.GC_1089,(0,2):C.GC_1088,(0,3):C.GC_1088,(0,0):C.GC_803,(0,5):C.GC_884})

V_300 = Vertex(name = 'V_300',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_966,(0,4):C.GC_1091,(0,2):C.GC_1090,(0,3):C.GC_1090,(0,0):C.GC_804,(0,5):C.GC_885})

V_301 = Vertex(name = 'V_301',
               particles = [ P.vt__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_967,(0,4):C.GC_1093,(0,2):C.GC_1092,(0,3):C.GC_1092,(0,0):C.GC_805,(0,5):C.GC_886})

V_302 = Vertex(name = 'V_302',
               particles = [ P.ve__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_968,(0,4):C.GC_1095,(0,2):C.GC_1094,(0,3):C.GC_1094,(0,0):C.GC_806,(0,5):C.GC_887})

V_303 = Vertex(name = 'V_303',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_969,(0,4):C.GC_1097,(0,2):C.GC_1096,(0,3):C.GC_1096,(0,0):C.GC_807,(0,5):C.GC_888})

V_304 = Vertex(name = 'V_304',
               particles = [ P.vt__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_970,(0,4):C.GC_1099,(0,2):C.GC_1098,(0,3):C.GC_1098,(0,0):C.GC_808,(0,5):C.GC_889})

V_305 = Vertex(name = 'V_305',
               particles = [ P.ve__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_971,(0,4):C.GC_1101,(0,2):C.GC_1100,(0,3):C.GC_1100,(0,0):C.GC_809,(0,5):C.GC_890})

V_306 = Vertex(name = 'V_306',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_972,(0,4):C.GC_1103,(0,2):C.GC_1102,(0,3):C.GC_1102,(0,0):C.GC_810,(0,5):C.GC_891})

V_307 = Vertex(name = 'V_307',
               particles = [ P.vt__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_973,(0,4):C.GC_1105,(0,2):C.GC_1104,(0,3):C.GC_1104,(0,0):C.GC_811,(0,5):C.GC_892})

V_308 = Vertex(name = 'V_308',
               particles = [ P.ve__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_974,(0,4):C.GC_1107,(0,2):C.GC_1106,(0,3):C.GC_1106,(0,0):C.GC_812,(0,5):C.GC_893})

V_309 = Vertex(name = 'V_309',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_975,(0,4):C.GC_1109,(0,2):C.GC_1108,(0,3):C.GC_1108,(0,0):C.GC_813,(0,5):C.GC_894})

V_310 = Vertex(name = 'V_310',
               particles = [ P.vt__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_976,(0,4):C.GC_1111,(0,2):C.GC_1110,(0,3):C.GC_1110,(0,0):C.GC_814,(0,5):C.GC_895})

V_311 = Vertex(name = 'V_311',
               particles = [ P.ve__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_977,(0,4):C.GC_1113,(0,2):C.GC_1112,(0,3):C.GC_1112,(0,0):C.GC_815,(0,5):C.GC_896})

V_312 = Vertex(name = 'V_312',
               particles = [ P.vm__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_978,(0,4):C.GC_1115,(0,2):C.GC_1114,(0,3):C.GC_1114,(0,0):C.GC_816,(0,5):C.GC_897})

V_313 = Vertex(name = 'V_313',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_979,(0,4):C.GC_1117,(0,2):C.GC_1116,(0,3):C.GC_1116,(0,0):C.GC_817,(0,5):C.GC_898})

V_314 = Vertex(name = 'V_314',
               particles = [ P.ve__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_980,(0,4):C.GC_1119,(0,2):C.GC_1118,(0,3):C.GC_1118,(0,0):C.GC_818,(0,5):C.GC_899})

V_315 = Vertex(name = 'V_315',
               particles = [ P.vm__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_981,(0,4):C.GC_1121,(0,2):C.GC_1120,(0,3):C.GC_1120,(0,0):C.GC_819,(0,5):C.GC_900})

V_316 = Vertex(name = 'V_316',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_982,(0,4):C.GC_1123,(0,2):C.GC_1122,(0,3):C.GC_1122,(0,0):C.GC_820,(0,5):C.GC_901})

V_317 = Vertex(name = 'V_317',
               particles = [ P.ve__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_983,(0,4):C.GC_1125,(0,2):C.GC_1124,(0,3):C.GC_1124,(0,0):C.GC_821,(0,5):C.GC_902})

V_318 = Vertex(name = 'V_318',
               particles = [ P.vm__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_984,(0,4):C.GC_1127,(0,2):C.GC_1126,(0,3):C.GC_1126,(0,0):C.GC_822,(0,5):C.GC_903})

V_319 = Vertex(name = 'V_319',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_985,(0,4):C.GC_1129,(0,2):C.GC_1128,(0,3):C.GC_1128,(0,0):C.GC_823,(0,5):C.GC_904})

V_320 = Vertex(name = 'V_320',
               particles = [ P.ve__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_986,(0,4):C.GC_1131,(0,2):C.GC_1130,(0,3):C.GC_1130,(0,0):C.GC_824,(0,5):C.GC_905})

V_321 = Vertex(name = 'V_321',
               particles = [ P.vm__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_987,(0,4):C.GC_1133,(0,2):C.GC_1132,(0,3):C.GC_1132,(0,0):C.GC_825,(0,5):C.GC_906})

V_322 = Vertex(name = 'V_322',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_988,(0,4):C.GC_1135,(0,2):C.GC_1134,(0,3):C.GC_1134,(0,0):C.GC_826,(0,5):C.GC_907})

V_323 = Vertex(name = 'V_323',
               particles = [ P.ve__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_989,(0,4):C.GC_1137,(0,2):C.GC_1136,(0,3):C.GC_1136,(0,0):C.GC_827,(0,5):C.GC_908})

V_324 = Vertex(name = 'V_324',
               particles = [ P.vm__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_990,(0,4):C.GC_1139,(0,2):C.GC_1138,(0,3):C.GC_1138,(0,0):C.GC_828,(0,5):C.GC_909})

V_325 = Vertex(name = 'V_325',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_991,(0,4):C.GC_1141,(0,2):C.GC_1140,(0,3):C.GC_1140,(0,0):C.GC_829,(0,5):C.GC_910})

V_326 = Vertex(name = 'V_326',
               particles = [ P.ve__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_992,(0,4):C.GC_1143,(0,2):C.GC_1142,(0,3):C.GC_1142,(0,0):C.GC_830,(0,5):C.GC_911})

V_327 = Vertex(name = 'V_327',
               particles = [ P.vm__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_993,(0,4):C.GC_1145,(0,2):C.GC_1144,(0,3):C.GC_1144,(0,0):C.GC_831,(0,5):C.GC_912})

V_328 = Vertex(name = 'V_328',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_994,(0,4):C.GC_1147,(0,2):C.GC_1146,(0,3):C.GC_1146,(0,0):C.GC_832,(0,5):C.GC_913})

V_329 = Vertex(name = 'V_329',
               particles = [ P.ve__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_995,(0,4):C.GC_1149,(0,2):C.GC_1148,(0,3):C.GC_1148,(0,0):C.GC_833,(0,5):C.GC_914})

V_330 = Vertex(name = 'V_330',
               particles = [ P.vm__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_996,(0,4):C.GC_1151,(0,2):C.GC_1150,(0,3):C.GC_1150,(0,0):C.GC_834,(0,5):C.GC_915})

V_331 = Vertex(name = 'V_331',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_997,(0,4):C.GC_1153,(0,2):C.GC_1152,(0,3):C.GC_1152,(0,0):C.GC_835,(0,5):C.GC_916})

V_332 = Vertex(name = 'V_332',
               particles = [ P.ve__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_998,(0,4):C.GC_1155,(0,2):C.GC_1154,(0,3):C.GC_1154,(0,0):C.GC_836,(0,5):C.GC_917})

V_333 = Vertex(name = 'V_333',
               particles = [ P.vm__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_999,(0,4):C.GC_1157,(0,2):C.GC_1156,(0,3):C.GC_1156,(0,0):C.GC_837,(0,5):C.GC_918})

V_334 = Vertex(name = 'V_334',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_1000,(0,4):C.GC_1159,(0,2):C.GC_1158,(0,3):C.GC_1158,(0,0):C.GC_838,(0,5):C.GC_919})

V_335 = Vertex(name = 'V_335',
               particles = [ P.ve__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_1001,(0,4):C.GC_1161,(0,2):C.GC_1160,(0,3):C.GC_1160,(0,0):C.GC_839,(0,5):C.GC_920})

V_336 = Vertex(name = 'V_336',
               particles = [ P.vm__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_1002,(0,4):C.GC_1163,(0,2):C.GC_1162,(0,3):C.GC_1162,(0,0):C.GC_840,(0,5):C.GC_921})

V_337 = Vertex(name = 'V_337',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_1003,(0,4):C.GC_1165,(0,2):C.GC_1164,(0,3):C.GC_1164,(0,0):C.GC_841,(0,5):C.GC_922})

V_338 = Vertex(name = 'V_338',
               particles = [ P.A, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_15})

V_339 = Vertex(name = 'V_339',
               particles = [ P.A, P.A, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_7})

V_340 = Vertex(name = 'V_340',
               particles = [ P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_18})

V_341 = Vertex(name = 'V_341',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_5})

V_342 = Vertex(name = 'V_342',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_4})

V_343 = Vertex(name = 'V_343',
               particles = [ P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_2390})

V_344 = Vertex(name = 'V_344',
               particles = [ P.A, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_8})

V_345 = Vertex(name = 'V_345',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_9})

V_346 = Vertex(name = 'V_346',
               particles = [ P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_6})

V_347 = Vertex(name = 'V_347',
               particles = [ P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_2392})

V_348 = Vertex(name = 'V_348',
               particles = [ P.e__plus__, P.e__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_16})

V_349 = Vertex(name = 'V_349',
               particles = [ P.mu__plus__, P.mu__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_16})

V_350 = Vertex(name = 'V_350',
               particles = [ P.ta__plus__, P.ta__minus__, P.A ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_16})

V_351 = Vertex(name = 'V_351',
               particles = [ P.u__tilde__, P.u, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_14})

V_352 = Vertex(name = 'V_352',
               particles = [ P.c__tilde__, P.c, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_14})

V_353 = Vertex(name = 'V_353',
               particles = [ P.t__tilde__, P.t, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_14})

V_354 = Vertex(name = 'V_354',
               particles = [ P.d__tilde__, P.d, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_13})

V_355 = Vertex(name = 'V_355',
               particles = [ P.s__tilde__, P.s, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_13})

V_356 = Vertex(name = 'V_356',
               particles = [ P.b__tilde__, P.b, P.A ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_13})

V_357 = Vertex(name = 'V_357',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_358 = Vertex(name = 'V_358',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_359 = Vertex(name = 'V_359',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_360 = Vertex(name = 'V_360',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_361 = Vertex(name = 'V_361',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_362 = Vertex(name = 'V_362',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_363 = Vertex(name = 'V_363',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_23})

V_364 = Vertex(name = 'V_364',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_24})

V_365 = Vertex(name = 'V_365',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_25})

V_366 = Vertex(name = 'V_366',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_26})

V_367 = Vertex(name = 'V_367',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_27})

V_368 = Vertex(name = 'V_368',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_28})

V_369 = Vertex(name = 'V_369',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_29})

V_370 = Vertex(name = 'V_370',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_30})

V_371 = Vertex(name = 'V_371',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_31})

V_372 = Vertex(name = 'V_372',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2483})

V_373 = Vertex(name = 'V_373',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2486})

V_374 = Vertex(name = 'V_374',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2489})

V_375 = Vertex(name = 'V_375',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2484})

V_376 = Vertex(name = 'V_376',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2487})

V_377 = Vertex(name = 'V_377',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2490})

V_378 = Vertex(name = 'V_378',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2485})

V_379 = Vertex(name = 'V_379',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2488})

V_380 = Vertex(name = 'V_380',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2491})

V_381 = Vertex(name = 'V_381',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2492})

V_382 = Vertex(name = 'V_382',
               particles = [ P.mu__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2495})

V_383 = Vertex(name = 'V_383',
               particles = [ P.ta__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2498})

V_384 = Vertex(name = 'V_384',
               particles = [ P.e__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2493})

V_385 = Vertex(name = 'V_385',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2496})

V_386 = Vertex(name = 'V_386',
               particles = [ P.ta__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2499})

V_387 = Vertex(name = 'V_387',
               particles = [ P.e__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2494})

V_388 = Vertex(name = 'V_388',
               particles = [ P.mu__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2497})

V_389 = Vertex(name = 'V_389',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2500})

V_390 = Vertex(name = 'V_390',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2381})

V_391 = Vertex(name = 'V_391',
               particles = [ P.vm__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2382})

V_392 = Vertex(name = 'V_392',
               particles = [ P.vt__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2383})

V_393 = Vertex(name = 'V_393',
               particles = [ P.ve__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2384})

V_394 = Vertex(name = 'V_394',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2385})

V_395 = Vertex(name = 'V_395',
               particles = [ P.vt__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2386})

V_396 = Vertex(name = 'V_396',
               particles = [ P.ve__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2387})

V_397 = Vertex(name = 'V_397',
               particles = [ P.vm__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2388})

V_398 = Vertex(name = 'V_398',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2389})

V_399 = Vertex(name = 'V_399',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_20,(0,1):C.GC_12})

V_400 = Vertex(name = 'V_400',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_20,(0,1):C.GC_12})

V_401 = Vertex(name = 'V_401',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_20,(0,1):C.GC_12})

V_402 = Vertex(name = 'V_402',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_21,(0,1):C.GC_10})

V_403 = Vertex(name = 'V_403',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_21,(0,1):C.GC_10})

V_404 = Vertex(name = 'V_404',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_21,(0,1):C.GC_10})

V_405 = Vertex(name = 'V_405',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_19})

V_406 = Vertex(name = 'V_406',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_19})

V_407 = Vertex(name = 'V_407',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_19})

V_408 = Vertex(name = 'V_408',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,1):C.GC_11,(0,0):C.GC_17})

V_409 = Vertex(name = 'V_409',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,1):C.GC_11,(0,0):C.GC_17})

V_410 = Vertex(name = 'V_410',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,1):C.GC_11,(0,0):C.GC_17})

V_411 = Vertex(name = 'V_411',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2138,(0,1):C.GC_1166})

V_412 = Vertex(name = 'V_412',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2139,(0,1):C.GC_1167})

V_413 = Vertex(name = 'V_413',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2140,(0,1):C.GC_1168})

V_414 = Vertex(name = 'V_414',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2141,(0,1):C.GC_1169})

V_415 = Vertex(name = 'V_415',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2142,(0,1):C.GC_1170})

V_416 = Vertex(name = 'V_416',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2143,(0,1):C.GC_1171})

V_417 = Vertex(name = 'V_417',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2144,(0,1):C.GC_1172})

V_418 = Vertex(name = 'V_418',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2145,(0,1):C.GC_1173})

V_419 = Vertex(name = 'V_419',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2146,(0,1):C.GC_1174})

V_420 = Vertex(name = 'V_420',
               particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2147,(0,1):C.GC_1175})

V_421 = Vertex(name = 'V_421',
               particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2148,(0,1):C.GC_1176})

V_422 = Vertex(name = 'V_422',
               particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2149,(0,1):C.GC_1177})

V_423 = Vertex(name = 'V_423',
               particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2150,(0,1):C.GC_1178})

V_424 = Vertex(name = 'V_424',
               particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2151,(0,1):C.GC_1179})

V_425 = Vertex(name = 'V_425',
               particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2152,(0,1):C.GC_1180})

V_426 = Vertex(name = 'V_426',
               particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2153,(0,1):C.GC_1181})

V_427 = Vertex(name = 'V_427',
               particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2154,(0,1):C.GC_1182})

V_428 = Vertex(name = 'V_428',
               particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2155,(0,1):C.GC_1183})

V_429 = Vertex(name = 'V_429',
               particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2156,(0,1):C.GC_1184})

V_430 = Vertex(name = 'V_430',
               particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2157,(0,1):C.GC_1185})

V_431 = Vertex(name = 'V_431',
               particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2158,(0,1):C.GC_1186})

V_432 = Vertex(name = 'V_432',
               particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2159,(0,1):C.GC_1187})

V_433 = Vertex(name = 'V_433',
               particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2160,(0,1):C.GC_1188})

V_434 = Vertex(name = 'V_434',
               particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2161,(0,1):C.GC_1189})

V_435 = Vertex(name = 'V_435',
               particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2162,(0,1):C.GC_1190})

V_436 = Vertex(name = 'V_436',
               particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2163,(0,1):C.GC_1191})

V_437 = Vertex(name = 'V_437',
               particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2164,(0,1):C.GC_1192})

V_438 = Vertex(name = 'V_438',
               particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2165,(0,1):C.GC_1193})

V_439 = Vertex(name = 'V_439',
               particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2166,(0,1):C.GC_1194})

V_440 = Vertex(name = 'V_440',
               particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2167,(0,1):C.GC_1195})

V_441 = Vertex(name = 'V_441',
               particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2168,(0,1):C.GC_1196})

V_442 = Vertex(name = 'V_442',
               particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2169,(0,1):C.GC_1197})

V_443 = Vertex(name = 'V_443',
               particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2170,(0,1):C.GC_1198})

V_444 = Vertex(name = 'V_444',
               particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2171,(0,1):C.GC_1199})

V_445 = Vertex(name = 'V_445',
               particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2172,(0,1):C.GC_1200})

V_446 = Vertex(name = 'V_446',
               particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2173,(0,1):C.GC_1201})

V_447 = Vertex(name = 'V_447',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2174,(0,1):C.GC_1202})

V_448 = Vertex(name = 'V_448',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2175,(0,1):C.GC_1203})

V_449 = Vertex(name = 'V_449',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2176,(0,1):C.GC_1204})

V_450 = Vertex(name = 'V_450',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2177,(0,1):C.GC_1205})

V_451 = Vertex(name = 'V_451',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2178,(0,1):C.GC_1206})

V_452 = Vertex(name = 'V_452',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2179,(0,1):C.GC_1207})

V_453 = Vertex(name = 'V_453',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2180,(0,1):C.GC_1208})

V_454 = Vertex(name = 'V_454',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2181,(0,1):C.GC_1209})

V_455 = Vertex(name = 'V_455',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2182,(0,1):C.GC_1210})

V_456 = Vertex(name = 'V_456',
               particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2183,(0,1):C.GC_1211})

V_457 = Vertex(name = 'V_457',
               particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2184,(0,1):C.GC_1212})

V_458 = Vertex(name = 'V_458',
               particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2185,(0,1):C.GC_1213})

V_459 = Vertex(name = 'V_459',
               particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2186,(0,1):C.GC_1214})

V_460 = Vertex(name = 'V_460',
               particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2187,(0,1):C.GC_1215})

V_461 = Vertex(name = 'V_461',
               particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2188,(0,1):C.GC_1216})

V_462 = Vertex(name = 'V_462',
               particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2189,(0,1):C.GC_1217})

V_463 = Vertex(name = 'V_463',
               particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2190,(0,1):C.GC_1218})

V_464 = Vertex(name = 'V_464',
               particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2191,(0,1):C.GC_1219})

V_465 = Vertex(name = 'V_465',
               particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2192,(0,1):C.GC_1220})

V_466 = Vertex(name = 'V_466',
               particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2193,(0,1):C.GC_1221})

V_467 = Vertex(name = 'V_467',
               particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2194,(0,1):C.GC_1222})

V_468 = Vertex(name = 'V_468',
               particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2195,(0,1):C.GC_1223})

V_469 = Vertex(name = 'V_469',
               particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2196,(0,1):C.GC_1224})

V_470 = Vertex(name = 'V_470',
               particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2197,(0,1):C.GC_1225})

V_471 = Vertex(name = 'V_471',
               particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2198,(0,1):C.GC_1226})

V_472 = Vertex(name = 'V_472',
               particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2199,(0,1):C.GC_1227})

V_473 = Vertex(name = 'V_473',
               particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2200,(0,1):C.GC_1228})

V_474 = Vertex(name = 'V_474',
               particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2201,(0,1):C.GC_1229})

V_475 = Vertex(name = 'V_475',
               particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2202,(0,1):C.GC_1230})

V_476 = Vertex(name = 'V_476',
               particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2203,(0,1):C.GC_1231})

V_477 = Vertex(name = 'V_477',
               particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2204,(0,1):C.GC_1232})

V_478 = Vertex(name = 'V_478',
               particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2205,(0,1):C.GC_1233})

V_479 = Vertex(name = 'V_479',
               particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2206,(0,1):C.GC_1234})

V_480 = Vertex(name = 'V_480',
               particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2207,(0,1):C.GC_1235})

V_481 = Vertex(name = 'V_481',
               particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2208,(0,1):C.GC_1236})

V_482 = Vertex(name = 'V_482',
               particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2209,(0,1):C.GC_1237})

V_483 = Vertex(name = 'V_483',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2210,(0,1):C.GC_1238})

V_484 = Vertex(name = 'V_484',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2211,(0,1):C.GC_1239})

V_485 = Vertex(name = 'V_485',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2212,(0,1):C.GC_1240})

V_486 = Vertex(name = 'V_486',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2213,(0,1):C.GC_1241})

V_487 = Vertex(name = 'V_487',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2214,(0,1):C.GC_1242})

V_488 = Vertex(name = 'V_488',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2215,(0,1):C.GC_1243})

V_489 = Vertex(name = 'V_489',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2216,(0,1):C.GC_1244})

V_490 = Vertex(name = 'V_490',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2217,(0,1):C.GC_1245})

V_491 = Vertex(name = 'V_491',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2218,(0,1):C.GC_1246})

V_492 = Vertex(name = 'V_492',
               particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2219,(0,1):C.GC_1328})

V_493 = Vertex(name = 'V_493',
               particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2220,(0,1):C.GC_1329})

V_494 = Vertex(name = 'V_494',
               particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2221,(0,1):C.GC_1330})

V_495 = Vertex(name = 'V_495',
               particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2222,(0,1):C.GC_1331})

V_496 = Vertex(name = 'V_496',
               particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2223,(0,1):C.GC_1332})

V_497 = Vertex(name = 'V_497',
               particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2224,(0,1):C.GC_1333})

V_498 = Vertex(name = 'V_498',
               particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2225,(0,1):C.GC_1334})

V_499 = Vertex(name = 'V_499',
               particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2226,(0,1):C.GC_1335})

V_500 = Vertex(name = 'V_500',
               particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2227,(0,1):C.GC_1336})

V_501 = Vertex(name = 'V_501',
               particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2228,(0,1):C.GC_1337})

V_502 = Vertex(name = 'V_502',
               particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2229,(0,1):C.GC_1338})

V_503 = Vertex(name = 'V_503',
               particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2230,(0,1):C.GC_1339})

V_504 = Vertex(name = 'V_504',
               particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2231,(0,1):C.GC_1340})

V_505 = Vertex(name = 'V_505',
               particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2232,(0,1):C.GC_1341})

V_506 = Vertex(name = 'V_506',
               particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2233,(0,1):C.GC_1342})

V_507 = Vertex(name = 'V_507',
               particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2234,(0,1):C.GC_1343})

V_508 = Vertex(name = 'V_508',
               particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2235,(0,1):C.GC_1344})

V_509 = Vertex(name = 'V_509',
               particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2236,(0,1):C.GC_1345})

V_510 = Vertex(name = 'V_510',
               particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2237,(0,1):C.GC_1346})

V_511 = Vertex(name = 'V_511',
               particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2238,(0,1):C.GC_1347})

V_512 = Vertex(name = 'V_512',
               particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2239,(0,1):C.GC_1348})

V_513 = Vertex(name = 'V_513',
               particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2240,(0,1):C.GC_1349})

V_514 = Vertex(name = 'V_514',
               particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2241,(0,1):C.GC_1350})

V_515 = Vertex(name = 'V_515',
               particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2242,(0,1):C.GC_1351})

V_516 = Vertex(name = 'V_516',
               particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2243,(0,1):C.GC_1352})

V_517 = Vertex(name = 'V_517',
               particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2244,(0,1):C.GC_1353})

V_518 = Vertex(name = 'V_518',
               particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2245,(0,1):C.GC_1354})

V_519 = Vertex(name = 'V_519',
               particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2246,(0,1):C.GC_1355})

V_520 = Vertex(name = 'V_520',
               particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2247,(0,1):C.GC_1356})

V_521 = Vertex(name = 'V_521',
               particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2248,(0,1):C.GC_1357})

V_522 = Vertex(name = 'V_522',
               particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2249,(0,1):C.GC_1358})

V_523 = Vertex(name = 'V_523',
               particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2250,(0,1):C.GC_1359})

V_524 = Vertex(name = 'V_524',
               particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2251,(0,1):C.GC_1360})

V_525 = Vertex(name = 'V_525',
               particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2252,(0,1):C.GC_1361})

V_526 = Vertex(name = 'V_526',
               particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2253,(0,1):C.GC_1362})

V_527 = Vertex(name = 'V_527',
               particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2254,(0,1):C.GC_1363})

V_528 = Vertex(name = 'V_528',
               particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2255,(0,1):C.GC_1364})

V_529 = Vertex(name = 'V_529',
               particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2256,(0,1):C.GC_1365})

V_530 = Vertex(name = 'V_530',
               particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2257,(0,1):C.GC_1366})

V_531 = Vertex(name = 'V_531',
               particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2258,(0,1):C.GC_1367})

V_532 = Vertex(name = 'V_532',
               particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2259,(0,1):C.GC_1368})

V_533 = Vertex(name = 'V_533',
               particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2260,(0,1):C.GC_1369})

V_534 = Vertex(name = 'V_534',
               particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2261,(0,1):C.GC_1370})

V_535 = Vertex(name = 'V_535',
               particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2262,(0,1):C.GC_1371})

V_536 = Vertex(name = 'V_536',
               particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2263,(0,1):C.GC_1372})

V_537 = Vertex(name = 'V_537',
               particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2264,(0,1):C.GC_1373})

V_538 = Vertex(name = 'V_538',
               particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2265,(0,1):C.GC_1374})

V_539 = Vertex(name = 'V_539',
               particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2266,(0,1):C.GC_1375})

V_540 = Vertex(name = 'V_540',
               particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2267,(0,1):C.GC_1376})

V_541 = Vertex(name = 'V_541',
               particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2268,(0,1):C.GC_1377})

V_542 = Vertex(name = 'V_542',
               particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2269,(0,1):C.GC_1378})

V_543 = Vertex(name = 'V_543',
               particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2270,(0,1):C.GC_1379})

V_544 = Vertex(name = 'V_544',
               particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2271,(0,1):C.GC_1380})

V_545 = Vertex(name = 'V_545',
               particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2272,(0,1):C.GC_1381})

V_546 = Vertex(name = 'V_546',
               particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2273,(0,1):C.GC_1382})

V_547 = Vertex(name = 'V_547',
               particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2274,(0,1):C.GC_1383})

V_548 = Vertex(name = 'V_548',
               particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2275,(0,1):C.GC_1384})

V_549 = Vertex(name = 'V_549',
               particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2276,(0,1):C.GC_1385})

V_550 = Vertex(name = 'V_550',
               particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2277,(0,1):C.GC_1386})

V_551 = Vertex(name = 'V_551',
               particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2278,(0,1):C.GC_1387})

V_552 = Vertex(name = 'V_552',
               particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2279,(0,1):C.GC_1388})

V_553 = Vertex(name = 'V_553',
               particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2280,(0,1):C.GC_1389})

V_554 = Vertex(name = 'V_554',
               particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2281,(0,1):C.GC_1390})

V_555 = Vertex(name = 'V_555',
               particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2282,(0,1):C.GC_1391})

V_556 = Vertex(name = 'V_556',
               particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2283,(0,1):C.GC_1392})

V_557 = Vertex(name = 'V_557',
               particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2284,(0,1):C.GC_1393})

V_558 = Vertex(name = 'V_558',
               particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2285,(0,1):C.GC_1394})

V_559 = Vertex(name = 'V_559',
               particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2286,(0,1):C.GC_1395})

V_560 = Vertex(name = 'V_560',
               particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2287,(0,1):C.GC_1396})

V_561 = Vertex(name = 'V_561',
               particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2288,(0,1):C.GC_1397})

V_562 = Vertex(name = 'V_562',
               particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2289,(0,1):C.GC_1398})

V_563 = Vertex(name = 'V_563',
               particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2290,(0,1):C.GC_1399})

V_564 = Vertex(name = 'V_564',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2291,(0,1):C.GC_1400})

V_565 = Vertex(name = 'V_565',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2292,(0,1):C.GC_1401})

V_566 = Vertex(name = 'V_566',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2293,(0,1):C.GC_1402})

V_567 = Vertex(name = 'V_567',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2294,(0,1):C.GC_1403})

V_568 = Vertex(name = 'V_568',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2295,(0,1):C.GC_1404})

V_569 = Vertex(name = 'V_569',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2296,(0,1):C.GC_1405})

V_570 = Vertex(name = 'V_570',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2297,(0,1):C.GC_1406})

V_571 = Vertex(name = 'V_571',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2298,(0,1):C.GC_1407})

V_572 = Vertex(name = 'V_572',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF9 ],
               couplings = {(0,0):C.GC_2299,(0,1):C.GC_1408})

