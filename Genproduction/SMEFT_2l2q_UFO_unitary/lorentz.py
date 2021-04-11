# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.0.0 for Linux x86 (64-bit) (April 7, 2019)
# Date: Thu 24 Oct 2019 15:52:55


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


SSS1 = Lorentz(name = 'SSS1',
               spins = [ 1, 1, 1 ],
               structure = '1')

FFS1 = Lorentz(name = 'FFS1',
               spins = [ 2, 2, 1 ],
               structure = 'Identity(2,1)')

FFV1 = Lorentz(name = 'FFV1',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1)')

FFV2 = Lorentz(name = 'FFV2',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV3 = Lorentz(name = 'FFV3',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjP(-1,1)')

FFV4 = Lorentz(name = 'FFV4',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)')

VVS1 = Lorentz(name = 'VVS1',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

VVV1 = Lorentz(name = 'VVV1',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

SSSS1 = Lorentz(name = 'SSSS1',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

FFFF1 = Lorentz(name = 'FFFF1',
                spins = [ 2, 2, 2, 2 ],
                structure = 'ProjM(2,1)*ProjM(4,3)')

FFFF2 = Lorentz(name = 'FFFF2',
                spins = [ 2, 2, 2, 2 ],
                structure = 'Gamma(-1,2,-2)*Gamma(-1,4,-3)*ProjM(-3,3)*ProjM(-2,1)')

FFFF3 = Lorentz(name = 'FFFF3',
                spins = [ 2, 2, 2, 2 ],
                structure = 'Gamma(-2,-4,-3)*Gamma(-2,2,-6)*Gamma(-1,-6,-5)*Gamma(-1,4,-4)*ProjM(-5,1)*ProjM(-3,3)')

FFFF4 = Lorentz(name = 'FFFF4',
                spins = [ 2, 2, 2, 2 ],
                structure = 'Gamma(-2,-4,-3)*Gamma(-2,4,-6)*Gamma(-1,-6,-5)*Gamma(-1,2,-4)*ProjM(-5,3)*ProjM(-3,1)')

FFFF5 = Lorentz(name = 'FFFF5',
                spins = [ 2, 2, 2, 2 ],
                structure = 'Gamma(-2,-6,-5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Gamma(-1,4,-6)*ProjM(-5,3)*ProjM(-3,1)')

FFFF6 = Lorentz(name = 'FFFF6',
                spins = [ 2, 2, 2, 2 ],
                structure = 'ProjM(4,3)*ProjP(2,1)')

FFFF7 = Lorentz(name = 'FFFF7',
                spins = [ 2, 2, 2, 2 ],
                structure = 'ProjM(2,1)*ProjP(4,3)')

FFFF8 = Lorentz(name = 'FFFF8',
                spins = [ 2, 2, 2, 2 ],
                structure = 'ProjP(2,1)*ProjP(4,3)')

FFFF9 = Lorentz(name = 'FFFF9',
                spins = [ 2, 2, 2, 2 ],
                structure = 'Gamma(-1,2,-3)*Gamma(-1,4,-2)*ProjM(-2,3)*ProjP(-3,1)')

FFFF10 = Lorentz(name = 'FFFF10',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'Gamma(-1,2,-2)*Gamma(-1,4,-3)*ProjM(-2,1)*ProjP(-3,3)')

FFFF11 = Lorentz(name = 'FFFF11',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'Gamma(-1,2,-2)*Gamma(-1,4,-3)*ProjP(-3,3)*ProjP(-2,1)')

FFFF12 = Lorentz(name = 'FFFF12',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'Gamma(-2,-4,-3)*Gamma(-2,2,-6)*Gamma(-1,-6,-5)*Gamma(-1,4,-4)*ProjP(-5,1)*ProjP(-3,3)')

FFFF13 = Lorentz(name = 'FFFF13',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'Gamma(-2,-4,-3)*Gamma(-2,4,-6)*Gamma(-1,-6,-5)*Gamma(-1,2,-4)*ProjP(-5,3)*ProjP(-3,1)')

FFFF14 = Lorentz(name = 'FFFF14',
                 spins = [ 2, 2, 2, 2 ],
                 structure = 'Gamma(-2,-6,-5)*Gamma(-2,-4,-3)*Gamma(-1,2,-4)*Gamma(-1,4,-6)*ProjP(-5,3)*ProjP(-3,1)')

VVSS1 = Lorentz(name = 'VVSS1',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVVV1 = Lorentz(name = 'VVVV1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV2 = Lorentz(name = 'VVVV2',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV3 = Lorentz(name = 'VVVV3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV4 = Lorentz(name = 'VVVV4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVV5 = Lorentz(name = 'VVVV5',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

