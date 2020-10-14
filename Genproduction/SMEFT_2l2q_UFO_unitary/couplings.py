# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.0.0 for Linux x86 (64-bit) (April 7, 2019)
# Date: Thu 24 Oct 2019 15:52:55


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(complex(0,1)*GS)',
                order = {'QCD':1})

GC_2 = Coupling(name = 'GC_2',
                value = 'GS',
                order = {'QCD':1})

GC_3 = Coupling(name = 'GC_3',
                value = 'complex(0,1)*GS**2',
                order = {'QCD':2})

GC_4 = Coupling(name = 'GC_4',
                value = '(complex(0,1)*GW**2)/2.',
                order = {'QED':2})

GC_5 = Coupling(name = 'GC_5',
                value = '-(complex(0,1)*GW**2)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '(complex(0,1)*G1**2)/2. + (complex(0,1)*GW**2)/2.',
                order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '(complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2)',
                order = {'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = '(-2*complex(0,1)*G1*GW**3)/(G1**2 + GW**2)',
                order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = '(complex(0,1)*GW**4)/(G1**2 + GW**2)',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-(complex(0,1)*G1**2)/(3.*cmath.sqrt(G1**2 + GW**2))',
                 order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-(complex(0,1)*G1**2)/(2.*cmath.sqrt(G1**2 + GW**2))',
                 order = {'QED':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '(2*complex(0,1)*G1**2)/(3.*cmath.sqrt(G1**2 + GW**2))',
                 order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '(complex(0,1)*G1*GW)/(3.*cmath.sqrt(G1**2 + GW**2))',
                 order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '(-2*complex(0,1)*G1*GW)/(3.*cmath.sqrt(G1**2 + GW**2))',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '-((complex(0,1)*G1*GW)/cmath.sqrt(G1**2 + GW**2))',
                 order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '(complex(0,1)*G1*GW)/cmath.sqrt(G1**2 + GW**2)',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '(complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '-((complex(0,1)*GW**2)/cmath.sqrt(G1**2 + GW**2))',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '-(complex(0,1)*cmath.sqrt(G1**2 + GW**2))/2.',
                 order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '(complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) - (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '(complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '-3*complex(0,1)*hlambda',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '-((complex(0,1)*GW*Kq1x1)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '-((complex(0,1)*GW*Kq1x2)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '-((complex(0,1)*GW*Kq1x3)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-((complex(0,1)*GW*Kq2x1)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '-((complex(0,1)*GW*Kq2x2)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '-((complex(0,1)*GW*Kq2x3)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '-((complex(0,1)*GW*Kq3x1)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '-((complex(0,1)*GW*Kq3x2)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '-((complex(0,1)*GW*Kq3x3)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = 'Ced1x1x1x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_33 = Coupling(name = 'GC_33',
                 value = 'Ced1x1x1x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_34 = Coupling(name = 'GC_34',
                 value = 'Ced1x1x1x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_35 = Coupling(name = 'GC_35',
                 value = 'Ced1x1x2x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_36 = Coupling(name = 'GC_36',
                 value = 'Ced1x1x2x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_37 = Coupling(name = 'GC_37',
                 value = 'Ced1x1x2x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_38 = Coupling(name = 'GC_38',
                 value = 'Ced1x1x3x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_39 = Coupling(name = 'GC_39',
                 value = 'Ced1x1x3x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_40 = Coupling(name = 'GC_40',
                 value = 'Ced1x1x3x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_41 = Coupling(name = 'GC_41',
                 value = 'Ced1x2x1x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_42 = Coupling(name = 'GC_42',
                 value = 'Ced1x2x1x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_43 = Coupling(name = 'GC_43',
                 value = 'Ced1x2x1x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_44 = Coupling(name = 'GC_44',
                 value = 'Ced1x2x2x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_45 = Coupling(name = 'GC_45',
                 value = 'Ced1x2x2x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_46 = Coupling(name = 'GC_46',
                 value = 'Ced1x2x2x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_47 = Coupling(name = 'GC_47',
                 value = 'Ced1x2x3x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_48 = Coupling(name = 'GC_48',
                 value = 'Ced1x2x3x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_49 = Coupling(name = 'GC_49',
                 value = 'Ced1x2x3x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_50 = Coupling(name = 'GC_50',
                 value = 'Ced1x3x1x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_51 = Coupling(name = 'GC_51',
                 value = 'Ced1x3x1x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_52 = Coupling(name = 'GC_52',
                 value = 'Ced1x3x1x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_53 = Coupling(name = 'GC_53',
                 value = 'Ced1x3x2x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_54 = Coupling(name = 'GC_54',
                 value = 'Ced1x3x2x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_55 = Coupling(name = 'GC_55',
                 value = 'Ced1x3x2x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_56 = Coupling(name = 'GC_56',
                 value = 'Ced1x3x3x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_57 = Coupling(name = 'GC_57',
                 value = 'Ced1x3x3x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_58 = Coupling(name = 'GC_58',
                 value = 'Ced1x3x3x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_59 = Coupling(name = 'GC_59',
                 value = 'Ced2x1x1x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_60 = Coupling(name = 'GC_60',
                 value = 'Ced2x1x1x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_61 = Coupling(name = 'GC_61',
                 value = 'Ced2x1x1x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_62 = Coupling(name = 'GC_62',
                 value = 'Ced2x1x2x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_63 = Coupling(name = 'GC_63',
                 value = 'Ced2x1x2x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_64 = Coupling(name = 'GC_64',
                 value = 'Ced2x1x2x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_65 = Coupling(name = 'GC_65',
                 value = 'Ced2x1x3x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_66 = Coupling(name = 'GC_66',
                 value = 'Ced2x1x3x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_67 = Coupling(name = 'GC_67',
                 value = 'Ced2x1x3x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_68 = Coupling(name = 'GC_68',
                 value = 'Ced2x2x1x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_69 = Coupling(name = 'GC_69',
                 value = 'Ced2x2x1x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_70 = Coupling(name = 'GC_70',
                 value = 'Ced2x2x1x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_71 = Coupling(name = 'GC_71',
                 value = 'Ced2x2x2x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_72 = Coupling(name = 'GC_72',
                 value = 'Ced2x2x2x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_73 = Coupling(name = 'GC_73',
                 value = 'Ced2x2x2x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_74 = Coupling(name = 'GC_74',
                 value = 'Ced2x2x3x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_75 = Coupling(name = 'GC_75',
                 value = 'Ced2x2x3x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_76 = Coupling(name = 'GC_76',
                 value = 'Ced2x2x3x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_77 = Coupling(name = 'GC_77',
                 value = 'Ced2x3x1x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_78 = Coupling(name = 'GC_78',
                 value = 'Ced2x3x1x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_79 = Coupling(name = 'GC_79',
                 value = 'Ced2x3x1x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_80 = Coupling(name = 'GC_80',
                 value = 'Ced2x3x2x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_81 = Coupling(name = 'GC_81',
                 value = 'Ced2x3x2x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_82 = Coupling(name = 'GC_82',
                 value = 'Ced2x3x2x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_83 = Coupling(name = 'GC_83',
                 value = 'Ced2x3x3x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_84 = Coupling(name = 'GC_84',
                 value = 'Ced2x3x3x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_85 = Coupling(name = 'GC_85',
                 value = 'Ced2x3x3x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_86 = Coupling(name = 'GC_86',
                 value = 'Ced3x1x1x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_87 = Coupling(name = 'GC_87',
                 value = 'Ced3x1x1x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_88 = Coupling(name = 'GC_88',
                 value = 'Ced3x1x1x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_89 = Coupling(name = 'GC_89',
                 value = 'Ced3x1x2x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_90 = Coupling(name = 'GC_90',
                 value = 'Ced3x1x2x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_91 = Coupling(name = 'GC_91',
                 value = 'Ced3x1x2x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_92 = Coupling(name = 'GC_92',
                 value = 'Ced3x1x3x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_93 = Coupling(name = 'GC_93',
                 value = 'Ced3x1x3x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_94 = Coupling(name = 'GC_94',
                 value = 'Ced3x1x3x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_95 = Coupling(name = 'GC_95',
                 value = 'Ced3x2x1x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_96 = Coupling(name = 'GC_96',
                 value = 'Ced3x2x1x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_97 = Coupling(name = 'GC_97',
                 value = 'Ced3x2x1x3*complex(0,1)*Lam',
                 order = {'NP':1})

GC_98 = Coupling(name = 'GC_98',
                 value = 'Ced3x2x2x1*complex(0,1)*Lam',
                 order = {'NP':1})

GC_99 = Coupling(name = 'GC_99',
                 value = 'Ced3x2x2x2*complex(0,1)*Lam',
                 order = {'NP':1})

GC_100 = Coupling(name = 'GC_100',
                  value = 'Ced3x2x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_101 = Coupling(name = 'GC_101',
                  value = 'Ced3x2x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_102 = Coupling(name = 'GC_102',
                  value = 'Ced3x2x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_103 = Coupling(name = 'GC_103',
                  value = 'Ced3x2x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_104 = Coupling(name = 'GC_104',
                  value = 'Ced3x3x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_105 = Coupling(name = 'GC_105',
                  value = 'Ced3x3x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_106 = Coupling(name = 'GC_106',
                  value = 'Ced3x3x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_107 = Coupling(name = 'GC_107',
                  value = 'Ced3x3x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_108 = Coupling(name = 'GC_108',
                  value = 'Ced3x3x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_109 = Coupling(name = 'GC_109',
                  value = 'Ced3x3x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_110 = Coupling(name = 'GC_110',
                  value = 'Ced3x3x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_111 = Coupling(name = 'GC_111',
                  value = 'Ced3x3x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_112 = Coupling(name = 'GC_112',
                  value = 'Ced3x3x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_113 = Coupling(name = 'GC_113',
                  value = 'Ceu1x1x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_114 = Coupling(name = 'GC_114',
                  value = 'Ceu1x1x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_115 = Coupling(name = 'GC_115',
                  value = 'Ceu1x1x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_116 = Coupling(name = 'GC_116',
                  value = 'Ceu1x1x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_117 = Coupling(name = 'GC_117',
                  value = 'Ceu1x1x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_118 = Coupling(name = 'GC_118',
                  value = 'Ceu1x1x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_119 = Coupling(name = 'GC_119',
                  value = 'Ceu1x1x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_120 = Coupling(name = 'GC_120',
                  value = 'Ceu1x1x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_121 = Coupling(name = 'GC_121',
                  value = 'Ceu1x1x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_122 = Coupling(name = 'GC_122',
                  value = 'Ceu1x2x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_123 = Coupling(name = 'GC_123',
                  value = 'Ceu1x2x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_124 = Coupling(name = 'GC_124',
                  value = 'Ceu1x2x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_125 = Coupling(name = 'GC_125',
                  value = 'Ceu1x2x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_126 = Coupling(name = 'GC_126',
                  value = 'Ceu1x2x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_127 = Coupling(name = 'GC_127',
                  value = 'Ceu1x2x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_128 = Coupling(name = 'GC_128',
                  value = 'Ceu1x2x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_129 = Coupling(name = 'GC_129',
                  value = 'Ceu1x2x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_130 = Coupling(name = 'GC_130',
                  value = 'Ceu1x2x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_131 = Coupling(name = 'GC_131',
                  value = 'Ceu1x3x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_132 = Coupling(name = 'GC_132',
                  value = 'Ceu1x3x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_133 = Coupling(name = 'GC_133',
                  value = 'Ceu1x3x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_134 = Coupling(name = 'GC_134',
                  value = 'Ceu1x3x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_135 = Coupling(name = 'GC_135',
                  value = 'Ceu1x3x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_136 = Coupling(name = 'GC_136',
                  value = 'Ceu1x3x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_137 = Coupling(name = 'GC_137',
                  value = 'Ceu1x3x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_138 = Coupling(name = 'GC_138',
                  value = 'Ceu1x3x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_139 = Coupling(name = 'GC_139',
                  value = 'Ceu1x3x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_140 = Coupling(name = 'GC_140',
                  value = 'Ceu2x1x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_141 = Coupling(name = 'GC_141',
                  value = 'Ceu2x1x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_142 = Coupling(name = 'GC_142',
                  value = 'Ceu2x1x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_143 = Coupling(name = 'GC_143',
                  value = 'Ceu2x1x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_144 = Coupling(name = 'GC_144',
                  value = 'Ceu2x1x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_145 = Coupling(name = 'GC_145',
                  value = 'Ceu2x1x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_146 = Coupling(name = 'GC_146',
                  value = 'Ceu2x1x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_147 = Coupling(name = 'GC_147',
                  value = 'Ceu2x1x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_148 = Coupling(name = 'GC_148',
                  value = 'Ceu2x1x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_149 = Coupling(name = 'GC_149',
                  value = 'Ceu2x2x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_150 = Coupling(name = 'GC_150',
                  value = 'Ceu2x2x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_151 = Coupling(name = 'GC_151',
                  value = 'Ceu2x2x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_152 = Coupling(name = 'GC_152',
                  value = 'Ceu2x2x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_153 = Coupling(name = 'GC_153',
                  value = 'Ceu2x2x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_154 = Coupling(name = 'GC_154',
                  value = 'Ceu2x2x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_155 = Coupling(name = 'GC_155',
                  value = 'Ceu2x2x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_156 = Coupling(name = 'GC_156',
                  value = 'Ceu2x2x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_157 = Coupling(name = 'GC_157',
                  value = 'Ceu2x2x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_158 = Coupling(name = 'GC_158',
                  value = 'Ceu2x3x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_159 = Coupling(name = 'GC_159',
                  value = 'Ceu2x3x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_160 = Coupling(name = 'GC_160',
                  value = 'Ceu2x3x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_161 = Coupling(name = 'GC_161',
                  value = 'Ceu2x3x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_162 = Coupling(name = 'GC_162',
                  value = 'Ceu2x3x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_163 = Coupling(name = 'GC_163',
                  value = 'Ceu2x3x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_164 = Coupling(name = 'GC_164',
                  value = 'Ceu2x3x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_165 = Coupling(name = 'GC_165',
                  value = 'Ceu2x3x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_166 = Coupling(name = 'GC_166',
                  value = 'Ceu2x3x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_167 = Coupling(name = 'GC_167',
                  value = 'Ceu3x1x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_168 = Coupling(name = 'GC_168',
                  value = 'Ceu3x1x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_169 = Coupling(name = 'GC_169',
                  value = 'Ceu3x1x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_170 = Coupling(name = 'GC_170',
                  value = 'Ceu3x1x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_171 = Coupling(name = 'GC_171',
                  value = 'Ceu3x1x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_172 = Coupling(name = 'GC_172',
                  value = 'Ceu3x1x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_173 = Coupling(name = 'GC_173',
                  value = 'Ceu3x1x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_174 = Coupling(name = 'GC_174',
                  value = 'Ceu3x1x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_175 = Coupling(name = 'GC_175',
                  value = 'Ceu3x1x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_176 = Coupling(name = 'GC_176',
                  value = 'Ceu3x2x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_177 = Coupling(name = 'GC_177',
                  value = 'Ceu3x2x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_178 = Coupling(name = 'GC_178',
                  value = 'Ceu3x2x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_179 = Coupling(name = 'GC_179',
                  value = 'Ceu3x2x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_180 = Coupling(name = 'GC_180',
                  value = 'Ceu3x2x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_181 = Coupling(name = 'GC_181',
                  value = 'Ceu3x2x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_182 = Coupling(name = 'GC_182',
                  value = 'Ceu3x2x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_183 = Coupling(name = 'GC_183',
                  value = 'Ceu3x2x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_184 = Coupling(name = 'GC_184',
                  value = 'Ceu3x2x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_185 = Coupling(name = 'GC_185',
                  value = 'Ceu3x3x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_186 = Coupling(name = 'GC_186',
                  value = 'Ceu3x3x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_187 = Coupling(name = 'GC_187',
                  value = 'Ceu3x3x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_188 = Coupling(name = 'GC_188',
                  value = 'Ceu3x3x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_189 = Coupling(name = 'GC_189',
                  value = 'Ceu3x3x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_190 = Coupling(name = 'GC_190',
                  value = 'Ceu3x3x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_191 = Coupling(name = 'GC_191',
                  value = 'Ceu3x3x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_192 = Coupling(name = 'GC_192',
                  value = 'Ceu3x3x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_193 = Coupling(name = 'GC_193',
                  value = 'Ceu3x3x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_194 = Coupling(name = 'GC_194',
                  value = 'Cld1x1x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_195 = Coupling(name = 'GC_195',
                  value = 'Cld1x1x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_196 = Coupling(name = 'GC_196',
                  value = 'Cld1x1x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_197 = Coupling(name = 'GC_197',
                  value = 'Cld1x1x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_198 = Coupling(name = 'GC_198',
                  value = 'Cld1x1x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_199 = Coupling(name = 'GC_199',
                  value = 'Cld1x1x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_200 = Coupling(name = 'GC_200',
                  value = 'Cld1x1x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_201 = Coupling(name = 'GC_201',
                  value = 'Cld1x1x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_202 = Coupling(name = 'GC_202',
                  value = 'Cld1x1x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_203 = Coupling(name = 'GC_203',
                  value = 'Cld1x2x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_204 = Coupling(name = 'GC_204',
                  value = 'Cld1x2x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_205 = Coupling(name = 'GC_205',
                  value = 'Cld1x2x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_206 = Coupling(name = 'GC_206',
                  value = 'Cld1x2x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_207 = Coupling(name = 'GC_207',
                  value = 'Cld1x2x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_208 = Coupling(name = 'GC_208',
                  value = 'Cld1x2x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_209 = Coupling(name = 'GC_209',
                  value = 'Cld1x2x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_210 = Coupling(name = 'GC_210',
                  value = 'Cld1x2x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_211 = Coupling(name = 'GC_211',
                  value = 'Cld1x2x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_212 = Coupling(name = 'GC_212',
                  value = 'Cld1x3x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_213 = Coupling(name = 'GC_213',
                  value = 'Cld1x3x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_214 = Coupling(name = 'GC_214',
                  value = 'Cld1x3x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_215 = Coupling(name = 'GC_215',
                  value = 'Cld1x3x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_216 = Coupling(name = 'GC_216',
                  value = 'Cld1x3x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_217 = Coupling(name = 'GC_217',
                  value = 'Cld1x3x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_218 = Coupling(name = 'GC_218',
                  value = 'Cld1x3x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_219 = Coupling(name = 'GC_219',
                  value = 'Cld1x3x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_220 = Coupling(name = 'GC_220',
                  value = 'Cld1x3x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_221 = Coupling(name = 'GC_221',
                  value = 'Cld2x1x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_222 = Coupling(name = 'GC_222',
                  value = 'Cld2x1x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_223 = Coupling(name = 'GC_223',
                  value = 'Cld2x1x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_224 = Coupling(name = 'GC_224',
                  value = 'Cld2x1x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_225 = Coupling(name = 'GC_225',
                  value = 'Cld2x1x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_226 = Coupling(name = 'GC_226',
                  value = 'Cld2x1x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_227 = Coupling(name = 'GC_227',
                  value = 'Cld2x1x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_228 = Coupling(name = 'GC_228',
                  value = 'Cld2x1x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_229 = Coupling(name = 'GC_229',
                  value = 'Cld2x1x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_230 = Coupling(name = 'GC_230',
                  value = 'Cld2x2x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_231 = Coupling(name = 'GC_231',
                  value = 'Cld2x2x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_232 = Coupling(name = 'GC_232',
                  value = 'Cld2x2x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_233 = Coupling(name = 'GC_233',
                  value = 'Cld2x2x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_234 = Coupling(name = 'GC_234',
                  value = 'Cld2x2x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_235 = Coupling(name = 'GC_235',
                  value = 'Cld2x2x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_236 = Coupling(name = 'GC_236',
                  value = 'Cld2x2x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_237 = Coupling(name = 'GC_237',
                  value = 'Cld2x2x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_238 = Coupling(name = 'GC_238',
                  value = 'Cld2x2x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_239 = Coupling(name = 'GC_239',
                  value = 'Cld2x3x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_240 = Coupling(name = 'GC_240',
                  value = 'Cld2x3x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_241 = Coupling(name = 'GC_241',
                  value = 'Cld2x3x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_242 = Coupling(name = 'GC_242',
                  value = 'Cld2x3x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_243 = Coupling(name = 'GC_243',
                  value = 'Cld2x3x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_244 = Coupling(name = 'GC_244',
                  value = 'Cld2x3x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_245 = Coupling(name = 'GC_245',
                  value = 'Cld2x3x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_246 = Coupling(name = 'GC_246',
                  value = 'Cld2x3x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_247 = Coupling(name = 'GC_247',
                  value = 'Cld2x3x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_248 = Coupling(name = 'GC_248',
                  value = 'Cld3x1x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_249 = Coupling(name = 'GC_249',
                  value = 'Cld3x1x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_250 = Coupling(name = 'GC_250',
                  value = 'Cld3x1x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_251 = Coupling(name = 'GC_251',
                  value = 'Cld3x1x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_252 = Coupling(name = 'GC_252',
                  value = 'Cld3x1x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_253 = Coupling(name = 'GC_253',
                  value = 'Cld3x1x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_254 = Coupling(name = 'GC_254',
                  value = 'Cld3x1x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_255 = Coupling(name = 'GC_255',
                  value = 'Cld3x1x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_256 = Coupling(name = 'GC_256',
                  value = 'Cld3x1x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_257 = Coupling(name = 'GC_257',
                  value = 'Cld3x2x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_258 = Coupling(name = 'GC_258',
                  value = 'Cld3x2x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_259 = Coupling(name = 'GC_259',
                  value = 'Cld3x2x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_260 = Coupling(name = 'GC_260',
                  value = 'Cld3x2x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_261 = Coupling(name = 'GC_261',
                  value = 'Cld3x2x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_262 = Coupling(name = 'GC_262',
                  value = 'Cld3x2x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_263 = Coupling(name = 'GC_263',
                  value = 'Cld3x2x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_264 = Coupling(name = 'GC_264',
                  value = 'Cld3x2x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_265 = Coupling(name = 'GC_265',
                  value = 'Cld3x2x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_266 = Coupling(name = 'GC_266',
                  value = 'Cld3x3x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_267 = Coupling(name = 'GC_267',
                  value = 'Cld3x3x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_268 = Coupling(name = 'GC_268',
                  value = 'Cld3x3x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_269 = Coupling(name = 'GC_269',
                  value = 'Cld3x3x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_270 = Coupling(name = 'GC_270',
                  value = 'Cld3x3x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_271 = Coupling(name = 'GC_271',
                  value = 'Cld3x3x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_272 = Coupling(name = 'GC_272',
                  value = 'Cld3x3x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_273 = Coupling(name = 'GC_273',
                  value = 'Cld3x3x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_274 = Coupling(name = 'GC_274',
                  value = 'Cld3x3x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_275 = Coupling(name = 'GC_275',
                  value = 'Cledq1x1x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_276 = Coupling(name = 'GC_276',
                  value = 'Cledq1x1x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_277 = Coupling(name = 'GC_277',
                  value = 'Cledq1x1x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_278 = Coupling(name = 'GC_278',
                  value = 'Cledq1x1x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_279 = Coupling(name = 'GC_279',
                  value = 'Cledq1x1x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_280 = Coupling(name = 'GC_280',
                  value = 'Cledq1x1x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_281 = Coupling(name = 'GC_281',
                  value = 'Cledq1x1x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_282 = Coupling(name = 'GC_282',
                  value = 'Cledq1x1x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_283 = Coupling(name = 'GC_283',
                  value = 'Cledq1x1x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_284 = Coupling(name = 'GC_284',
                  value = 'Cledq1x2x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_285 = Coupling(name = 'GC_285',
                  value = 'Cledq1x2x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_286 = Coupling(name = 'GC_286',
                  value = 'Cledq1x2x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_287 = Coupling(name = 'GC_287',
                  value = 'Cledq1x2x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_288 = Coupling(name = 'GC_288',
                  value = 'Cledq1x2x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_289 = Coupling(name = 'GC_289',
                  value = 'Cledq1x2x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_290 = Coupling(name = 'GC_290',
                  value = 'Cledq1x2x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_291 = Coupling(name = 'GC_291',
                  value = 'Cledq1x2x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_292 = Coupling(name = 'GC_292',
                  value = 'Cledq1x2x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_293 = Coupling(name = 'GC_293',
                  value = 'Cledq1x3x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_294 = Coupling(name = 'GC_294',
                  value = 'Cledq1x3x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_295 = Coupling(name = 'GC_295',
                  value = 'Cledq1x3x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_296 = Coupling(name = 'GC_296',
                  value = 'Cledq1x3x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_297 = Coupling(name = 'GC_297',
                  value = 'Cledq1x3x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_298 = Coupling(name = 'GC_298',
                  value = 'Cledq1x3x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_299 = Coupling(name = 'GC_299',
                  value = 'Cledq1x3x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_300 = Coupling(name = 'GC_300',
                  value = 'Cledq1x3x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_301 = Coupling(name = 'GC_301',
                  value = 'Cledq1x3x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_302 = Coupling(name = 'GC_302',
                  value = 'Cledq2x1x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_303 = Coupling(name = 'GC_303',
                  value = 'Cledq2x1x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_304 = Coupling(name = 'GC_304',
                  value = 'Cledq2x1x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_305 = Coupling(name = 'GC_305',
                  value = 'Cledq2x1x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_306 = Coupling(name = 'GC_306',
                  value = 'Cledq2x1x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_307 = Coupling(name = 'GC_307',
                  value = 'Cledq2x1x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_308 = Coupling(name = 'GC_308',
                  value = 'Cledq2x1x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_309 = Coupling(name = 'GC_309',
                  value = 'Cledq2x1x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_310 = Coupling(name = 'GC_310',
                  value = 'Cledq2x1x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_311 = Coupling(name = 'GC_311',
                  value = 'Cledq2x2x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_312 = Coupling(name = 'GC_312',
                  value = 'Cledq2x2x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_313 = Coupling(name = 'GC_313',
                  value = 'Cledq2x2x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_314 = Coupling(name = 'GC_314',
                  value = 'Cledq2x2x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_315 = Coupling(name = 'GC_315',
                  value = 'Cledq2x2x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_316 = Coupling(name = 'GC_316',
                  value = 'Cledq2x2x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_317 = Coupling(name = 'GC_317',
                  value = 'Cledq2x2x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_318 = Coupling(name = 'GC_318',
                  value = 'Cledq2x2x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_319 = Coupling(name = 'GC_319',
                  value = 'Cledq2x2x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_320 = Coupling(name = 'GC_320',
                  value = 'Cledq2x3x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_321 = Coupling(name = 'GC_321',
                  value = 'Cledq2x3x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_322 = Coupling(name = 'GC_322',
                  value = 'Cledq2x3x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_323 = Coupling(name = 'GC_323',
                  value = 'Cledq2x3x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_324 = Coupling(name = 'GC_324',
                  value = 'Cledq2x3x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_325 = Coupling(name = 'GC_325',
                  value = 'Cledq2x3x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_326 = Coupling(name = 'GC_326',
                  value = 'Cledq2x3x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_327 = Coupling(name = 'GC_327',
                  value = 'Cledq2x3x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_328 = Coupling(name = 'GC_328',
                  value = 'Cledq2x3x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_329 = Coupling(name = 'GC_329',
                  value = 'Cledq3x1x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_330 = Coupling(name = 'GC_330',
                  value = 'Cledq3x1x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_331 = Coupling(name = 'GC_331',
                  value = 'Cledq3x1x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_332 = Coupling(name = 'GC_332',
                  value = 'Cledq3x1x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_333 = Coupling(name = 'GC_333',
                  value = 'Cledq3x1x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_334 = Coupling(name = 'GC_334',
                  value = 'Cledq3x1x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_335 = Coupling(name = 'GC_335',
                  value = 'Cledq3x1x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_336 = Coupling(name = 'GC_336',
                  value = 'Cledq3x1x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_337 = Coupling(name = 'GC_337',
                  value = 'Cledq3x1x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_338 = Coupling(name = 'GC_338',
                  value = 'Cledq3x2x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_339 = Coupling(name = 'GC_339',
                  value = 'Cledq3x2x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_340 = Coupling(name = 'GC_340',
                  value = 'Cledq3x2x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_341 = Coupling(name = 'GC_341',
                  value = 'Cledq3x2x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_342 = Coupling(name = 'GC_342',
                  value = 'Cledq3x2x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_343 = Coupling(name = 'GC_343',
                  value = 'Cledq3x2x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_344 = Coupling(name = 'GC_344',
                  value = 'Cledq3x2x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_345 = Coupling(name = 'GC_345',
                  value = 'Cledq3x2x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_346 = Coupling(name = 'GC_346',
                  value = 'Cledq3x2x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_347 = Coupling(name = 'GC_347',
                  value = 'Cledq3x3x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_348 = Coupling(name = 'GC_348',
                  value = 'Cledq3x3x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_349 = Coupling(name = 'GC_349',
                  value = 'Cledq3x3x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_350 = Coupling(name = 'GC_350',
                  value = 'Cledq3x3x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_351 = Coupling(name = 'GC_351',
                  value = 'Cledq3x3x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_352 = Coupling(name = 'GC_352',
                  value = 'Cledq3x3x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_353 = Coupling(name = 'GC_353',
                  value = 'Cledq3x3x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_354 = Coupling(name = 'GC_354',
                  value = 'Cledq3x3x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_355 = Coupling(name = 'GC_355',
                  value = 'Cledq3x3x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_356 = Coupling(name = 'GC_356',
                  value = 'Clu1x1x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_357 = Coupling(name = 'GC_357',
                  value = 'Clu1x1x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_358 = Coupling(name = 'GC_358',
                  value = 'Clu1x1x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_359 = Coupling(name = 'GC_359',
                  value = 'Clu1x1x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_360 = Coupling(name = 'GC_360',
                  value = 'Clu1x1x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_361 = Coupling(name = 'GC_361',
                  value = 'Clu1x1x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_362 = Coupling(name = 'GC_362',
                  value = 'Clu1x1x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_363 = Coupling(name = 'GC_363',
                  value = 'Clu1x1x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_364 = Coupling(name = 'GC_364',
                  value = 'Clu1x1x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_365 = Coupling(name = 'GC_365',
                  value = 'Clu1x2x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_366 = Coupling(name = 'GC_366',
                  value = 'Clu1x2x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_367 = Coupling(name = 'GC_367',
                  value = 'Clu1x2x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_368 = Coupling(name = 'GC_368',
                  value = 'Clu1x2x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_369 = Coupling(name = 'GC_369',
                  value = 'Clu1x2x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_370 = Coupling(name = 'GC_370',
                  value = 'Clu1x2x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_371 = Coupling(name = 'GC_371',
                  value = 'Clu1x2x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_372 = Coupling(name = 'GC_372',
                  value = 'Clu1x2x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_373 = Coupling(name = 'GC_373',
                  value = 'Clu1x2x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_374 = Coupling(name = 'GC_374',
                  value = 'Clu1x3x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_375 = Coupling(name = 'GC_375',
                  value = 'Clu1x3x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_376 = Coupling(name = 'GC_376',
                  value = 'Clu1x3x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_377 = Coupling(name = 'GC_377',
                  value = 'Clu1x3x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_378 = Coupling(name = 'GC_378',
                  value = 'Clu1x3x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_379 = Coupling(name = 'GC_379',
                  value = 'Clu1x3x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_380 = Coupling(name = 'GC_380',
                  value = 'Clu1x3x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_381 = Coupling(name = 'GC_381',
                  value = 'Clu1x3x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_382 = Coupling(name = 'GC_382',
                  value = 'Clu1x3x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_383 = Coupling(name = 'GC_383',
                  value = 'Clu2x1x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_384 = Coupling(name = 'GC_384',
                  value = 'Clu2x1x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_385 = Coupling(name = 'GC_385',
                  value = 'Clu2x1x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_386 = Coupling(name = 'GC_386',
                  value = 'Clu2x1x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_387 = Coupling(name = 'GC_387',
                  value = 'Clu2x1x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_388 = Coupling(name = 'GC_388',
                  value = 'Clu2x1x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_389 = Coupling(name = 'GC_389',
                  value = 'Clu2x1x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_390 = Coupling(name = 'GC_390',
                  value = 'Clu2x1x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_391 = Coupling(name = 'GC_391',
                  value = 'Clu2x1x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_392 = Coupling(name = 'GC_392',
                  value = 'Clu2x2x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_393 = Coupling(name = 'GC_393',
                  value = 'Clu2x2x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_394 = Coupling(name = 'GC_394',
                  value = 'Clu2x2x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_395 = Coupling(name = 'GC_395',
                  value = 'Clu2x2x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_396 = Coupling(name = 'GC_396',
                  value = 'Clu2x2x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_397 = Coupling(name = 'GC_397',
                  value = 'Clu2x2x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_398 = Coupling(name = 'GC_398',
                  value = 'Clu2x2x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_399 = Coupling(name = 'GC_399',
                  value = 'Clu2x2x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_400 = Coupling(name = 'GC_400',
                  value = 'Clu2x2x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_401 = Coupling(name = 'GC_401',
                  value = 'Clu2x3x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_402 = Coupling(name = 'GC_402',
                  value = 'Clu2x3x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_403 = Coupling(name = 'GC_403',
                  value = 'Clu2x3x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_404 = Coupling(name = 'GC_404',
                  value = 'Clu2x3x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_405 = Coupling(name = 'GC_405',
                  value = 'Clu2x3x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_406 = Coupling(name = 'GC_406',
                  value = 'Clu2x3x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_407 = Coupling(name = 'GC_407',
                  value = 'Clu2x3x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_408 = Coupling(name = 'GC_408',
                  value = 'Clu2x3x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_409 = Coupling(name = 'GC_409',
                  value = 'Clu2x3x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_410 = Coupling(name = 'GC_410',
                  value = 'Clu3x1x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_411 = Coupling(name = 'GC_411',
                  value = 'Clu3x1x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_412 = Coupling(name = 'GC_412',
                  value = 'Clu3x1x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_413 = Coupling(name = 'GC_413',
                  value = 'Clu3x1x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_414 = Coupling(name = 'GC_414',
                  value = 'Clu3x1x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_415 = Coupling(name = 'GC_415',
                  value = 'Clu3x1x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_416 = Coupling(name = 'GC_416',
                  value = 'Clu3x1x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_417 = Coupling(name = 'GC_417',
                  value = 'Clu3x1x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_418 = Coupling(name = 'GC_418',
                  value = 'Clu3x1x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_419 = Coupling(name = 'GC_419',
                  value = 'Clu3x2x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_420 = Coupling(name = 'GC_420',
                  value = 'Clu3x2x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_421 = Coupling(name = 'GC_421',
                  value = 'Clu3x2x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_422 = Coupling(name = 'GC_422',
                  value = 'Clu3x2x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_423 = Coupling(name = 'GC_423',
                  value = 'Clu3x2x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_424 = Coupling(name = 'GC_424',
                  value = 'Clu3x2x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_425 = Coupling(name = 'GC_425',
                  value = 'Clu3x2x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_426 = Coupling(name = 'GC_426',
                  value = 'Clu3x2x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_427 = Coupling(name = 'GC_427',
                  value = 'Clu3x2x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_428 = Coupling(name = 'GC_428',
                  value = 'Clu3x3x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_429 = Coupling(name = 'GC_429',
                  value = 'Clu3x3x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_430 = Coupling(name = 'GC_430',
                  value = 'Clu3x3x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_431 = Coupling(name = 'GC_431',
                  value = 'Clu3x3x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_432 = Coupling(name = 'GC_432',
                  value = 'Clu3x3x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_433 = Coupling(name = 'GC_433',
                  value = 'Clu3x3x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_434 = Coupling(name = 'GC_434',
                  value = 'Clu3x3x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_435 = Coupling(name = 'GC_435',
                  value = 'Clu3x3x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_436 = Coupling(name = 'GC_436',
                  value = 'Clu3x3x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_437 = Coupling(name = 'GC_437',
                  value = 'Cqe1x1x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_438 = Coupling(name = 'GC_438',
                  value = 'Cqe1x1x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_439 = Coupling(name = 'GC_439',
                  value = 'Cqe1x1x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_440 = Coupling(name = 'GC_440',
                  value = 'Cqe1x1x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_441 = Coupling(name = 'GC_441',
                  value = 'Cqe1x1x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_442 = Coupling(name = 'GC_442',
                  value = 'Cqe1x1x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_443 = Coupling(name = 'GC_443',
                  value = 'Cqe1x1x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_444 = Coupling(name = 'GC_444',
                  value = 'Cqe1x1x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_445 = Coupling(name = 'GC_445',
                  value = 'Cqe1x1x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_446 = Coupling(name = 'GC_446',
                  value = 'Cqe1x2x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_447 = Coupling(name = 'GC_447',
                  value = 'Cqe1x2x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_448 = Coupling(name = 'GC_448',
                  value = 'Cqe1x2x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_449 = Coupling(name = 'GC_449',
                  value = 'Cqe1x2x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_450 = Coupling(name = 'GC_450',
                  value = 'Cqe1x2x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_451 = Coupling(name = 'GC_451',
                  value = 'Cqe1x2x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_452 = Coupling(name = 'GC_452',
                  value = 'Cqe1x2x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_453 = Coupling(name = 'GC_453',
                  value = 'Cqe1x2x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_454 = Coupling(name = 'GC_454',
                  value = 'Cqe1x2x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_455 = Coupling(name = 'GC_455',
                  value = 'Cqe1x3x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_456 = Coupling(name = 'GC_456',
                  value = 'Cqe1x3x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_457 = Coupling(name = 'GC_457',
                  value = 'Cqe1x3x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_458 = Coupling(name = 'GC_458',
                  value = 'Cqe1x3x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_459 = Coupling(name = 'GC_459',
                  value = 'Cqe1x3x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_460 = Coupling(name = 'GC_460',
                  value = 'Cqe1x3x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_461 = Coupling(name = 'GC_461',
                  value = 'Cqe1x3x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_462 = Coupling(name = 'GC_462',
                  value = 'Cqe1x3x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_463 = Coupling(name = 'GC_463',
                  value = 'Cqe1x3x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_464 = Coupling(name = 'GC_464',
                  value = 'Cqe2x1x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_465 = Coupling(name = 'GC_465',
                  value = 'Cqe2x1x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_466 = Coupling(name = 'GC_466',
                  value = 'Cqe2x1x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_467 = Coupling(name = 'GC_467',
                  value = 'Cqe2x1x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_468 = Coupling(name = 'GC_468',
                  value = 'Cqe2x1x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_469 = Coupling(name = 'GC_469',
                  value = 'Cqe2x1x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_470 = Coupling(name = 'GC_470',
                  value = 'Cqe2x1x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_471 = Coupling(name = 'GC_471',
                  value = 'Cqe2x1x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_472 = Coupling(name = 'GC_472',
                  value = 'Cqe2x1x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_473 = Coupling(name = 'GC_473',
                  value = 'Cqe2x2x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_474 = Coupling(name = 'GC_474',
                  value = 'Cqe2x2x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_475 = Coupling(name = 'GC_475',
                  value = 'Cqe2x2x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_476 = Coupling(name = 'GC_476',
                  value = 'Cqe2x2x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_477 = Coupling(name = 'GC_477',
                  value = 'Cqe2x2x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_478 = Coupling(name = 'GC_478',
                  value = 'Cqe2x2x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_479 = Coupling(name = 'GC_479',
                  value = 'Cqe2x2x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_480 = Coupling(name = 'GC_480',
                  value = 'Cqe2x2x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_481 = Coupling(name = 'GC_481',
                  value = 'Cqe2x2x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_482 = Coupling(name = 'GC_482',
                  value = 'Cqe2x3x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_483 = Coupling(name = 'GC_483',
                  value = 'Cqe2x3x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_484 = Coupling(name = 'GC_484',
                  value = 'Cqe2x3x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_485 = Coupling(name = 'GC_485',
                  value = 'Cqe2x3x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_486 = Coupling(name = 'GC_486',
                  value = 'Cqe2x3x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_487 = Coupling(name = 'GC_487',
                  value = 'Cqe2x3x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_488 = Coupling(name = 'GC_488',
                  value = 'Cqe2x3x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_489 = Coupling(name = 'GC_489',
                  value = 'Cqe2x3x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_490 = Coupling(name = 'GC_490',
                  value = 'Cqe2x3x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_491 = Coupling(name = 'GC_491',
                  value = 'Cqe3x1x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_492 = Coupling(name = 'GC_492',
                  value = 'Cqe3x1x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_493 = Coupling(name = 'GC_493',
                  value = 'Cqe3x1x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_494 = Coupling(name = 'GC_494',
                  value = 'Cqe3x1x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_495 = Coupling(name = 'GC_495',
                  value = 'Cqe3x1x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_496 = Coupling(name = 'GC_496',
                  value = 'Cqe3x1x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_497 = Coupling(name = 'GC_497',
                  value = 'Cqe3x1x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_498 = Coupling(name = 'GC_498',
                  value = 'Cqe3x1x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_499 = Coupling(name = 'GC_499',
                  value = 'Cqe3x1x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_500 = Coupling(name = 'GC_500',
                  value = 'Cqe3x2x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_501 = Coupling(name = 'GC_501',
                  value = 'Cqe3x2x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_502 = Coupling(name = 'GC_502',
                  value = 'Cqe3x2x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_503 = Coupling(name = 'GC_503',
                  value = 'Cqe3x2x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_504 = Coupling(name = 'GC_504',
                  value = 'Cqe3x2x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_505 = Coupling(name = 'GC_505',
                  value = 'Cqe3x2x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_506 = Coupling(name = 'GC_506',
                  value = 'Cqe3x2x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_507 = Coupling(name = 'GC_507',
                  value = 'Cqe3x2x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_508 = Coupling(name = 'GC_508',
                  value = 'Cqe3x2x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_509 = Coupling(name = 'GC_509',
                  value = 'Cqe3x3x1x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_510 = Coupling(name = 'GC_510',
                  value = 'Cqe3x3x1x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_511 = Coupling(name = 'GC_511',
                  value = 'Cqe3x3x1x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_512 = Coupling(name = 'GC_512',
                  value = 'Cqe3x3x2x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_513 = Coupling(name = 'GC_513',
                  value = 'Cqe3x3x2x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_514 = Coupling(name = 'GC_514',
                  value = 'Cqe3x3x2x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_515 = Coupling(name = 'GC_515',
                  value = 'Cqe3x3x3x1*complex(0,1)*Lam',
                  order = {'NP':1})

GC_516 = Coupling(name = 'GC_516',
                  value = 'Cqe3x3x3x2*complex(0,1)*Lam',
                  order = {'NP':1})

GC_517 = Coupling(name = 'GC_517',
                  value = 'Cqe3x3x3x3*complex(0,1)*Lam',
                  order = {'NP':1})

GC_518 = Coupling(name = 'GC_518',
                  value = '2*complex(0,1)*I10a1111*Lam',
                  order = {'NP':1})

GC_519 = Coupling(name = 'GC_519',
                  value = '2*complex(0,1)*I10a1112*Lam',
                  order = {'NP':1})

GC_520 = Coupling(name = 'GC_520',
                  value = '2*complex(0,1)*I10a1113*Lam',
                  order = {'NP':1})

GC_521 = Coupling(name = 'GC_521',
                  value = '2*complex(0,1)*I10a1121*Lam',
                  order = {'NP':1})

GC_522 = Coupling(name = 'GC_522',
                  value = '2*complex(0,1)*I10a1122*Lam',
                  order = {'NP':1})

GC_523 = Coupling(name = 'GC_523',
                  value = '2*complex(0,1)*I10a1123*Lam',
                  order = {'NP':1})

GC_524 = Coupling(name = 'GC_524',
                  value = '2*complex(0,1)*I10a1131*Lam',
                  order = {'NP':1})

GC_525 = Coupling(name = 'GC_525',
                  value = '2*complex(0,1)*I10a1132*Lam',
                  order = {'NP':1})

GC_526 = Coupling(name = 'GC_526',
                  value = '2*complex(0,1)*I10a1133*Lam',
                  order = {'NP':1})

GC_527 = Coupling(name = 'GC_527',
                  value = '2*complex(0,1)*I10a1211*Lam',
                  order = {'NP':1})

GC_528 = Coupling(name = 'GC_528',
                  value = '2*complex(0,1)*I10a1212*Lam',
                  order = {'NP':1})

GC_529 = Coupling(name = 'GC_529',
                  value = '2*complex(0,1)*I10a1213*Lam',
                  order = {'NP':1})

GC_530 = Coupling(name = 'GC_530',
                  value = '2*complex(0,1)*I10a1221*Lam',
                  order = {'NP':1})

GC_531 = Coupling(name = 'GC_531',
                  value = '2*complex(0,1)*I10a1222*Lam',
                  order = {'NP':1})

GC_532 = Coupling(name = 'GC_532',
                  value = '2*complex(0,1)*I10a1223*Lam',
                  order = {'NP':1})

GC_533 = Coupling(name = 'GC_533',
                  value = '2*complex(0,1)*I10a1231*Lam',
                  order = {'NP':1})

GC_534 = Coupling(name = 'GC_534',
                  value = '2*complex(0,1)*I10a1232*Lam',
                  order = {'NP':1})

GC_535 = Coupling(name = 'GC_535',
                  value = '2*complex(0,1)*I10a1233*Lam',
                  order = {'NP':1})

GC_536 = Coupling(name = 'GC_536',
                  value = '2*complex(0,1)*I10a1311*Lam',
                  order = {'NP':1})

GC_537 = Coupling(name = 'GC_537',
                  value = '2*complex(0,1)*I10a1312*Lam',
                  order = {'NP':1})

GC_538 = Coupling(name = 'GC_538',
                  value = '2*complex(0,1)*I10a1313*Lam',
                  order = {'NP':1})

GC_539 = Coupling(name = 'GC_539',
                  value = '2*complex(0,1)*I10a1321*Lam',
                  order = {'NP':1})

GC_540 = Coupling(name = 'GC_540',
                  value = '2*complex(0,1)*I10a1322*Lam',
                  order = {'NP':1})

GC_541 = Coupling(name = 'GC_541',
                  value = '2*complex(0,1)*I10a1323*Lam',
                  order = {'NP':1})

GC_542 = Coupling(name = 'GC_542',
                  value = '2*complex(0,1)*I10a1331*Lam',
                  order = {'NP':1})

GC_543 = Coupling(name = 'GC_543',
                  value = '2*complex(0,1)*I10a1332*Lam',
                  order = {'NP':1})

GC_544 = Coupling(name = 'GC_544',
                  value = '2*complex(0,1)*I10a1333*Lam',
                  order = {'NP':1})

GC_545 = Coupling(name = 'GC_545',
                  value = '2*complex(0,1)*I10a2111*Lam',
                  order = {'NP':1})

GC_546 = Coupling(name = 'GC_546',
                  value = '2*complex(0,1)*I10a2112*Lam',
                  order = {'NP':1})

GC_547 = Coupling(name = 'GC_547',
                  value = '2*complex(0,1)*I10a2113*Lam',
                  order = {'NP':1})

GC_548 = Coupling(name = 'GC_548',
                  value = '2*complex(0,1)*I10a2121*Lam',
                  order = {'NP':1})

GC_549 = Coupling(name = 'GC_549',
                  value = '2*complex(0,1)*I10a2122*Lam',
                  order = {'NP':1})

GC_550 = Coupling(name = 'GC_550',
                  value = '2*complex(0,1)*I10a2123*Lam',
                  order = {'NP':1})

GC_551 = Coupling(name = 'GC_551',
                  value = '2*complex(0,1)*I10a2131*Lam',
                  order = {'NP':1})

GC_552 = Coupling(name = 'GC_552',
                  value = '2*complex(0,1)*I10a2132*Lam',
                  order = {'NP':1})

GC_553 = Coupling(name = 'GC_553',
                  value = '2*complex(0,1)*I10a2133*Lam',
                  order = {'NP':1})

GC_554 = Coupling(name = 'GC_554',
                  value = '2*complex(0,1)*I10a2211*Lam',
                  order = {'NP':1})

GC_555 = Coupling(name = 'GC_555',
                  value = '2*complex(0,1)*I10a2212*Lam',
                  order = {'NP':1})

GC_556 = Coupling(name = 'GC_556',
                  value = '2*complex(0,1)*I10a2213*Lam',
                  order = {'NP':1})

GC_557 = Coupling(name = 'GC_557',
                  value = '2*complex(0,1)*I10a2221*Lam',
                  order = {'NP':1})

GC_558 = Coupling(name = 'GC_558',
                  value = '2*complex(0,1)*I10a2222*Lam',
                  order = {'NP':1})

GC_559 = Coupling(name = 'GC_559',
                  value = '2*complex(0,1)*I10a2223*Lam',
                  order = {'NP':1})

GC_560 = Coupling(name = 'GC_560',
                  value = '2*complex(0,1)*I10a2231*Lam',
                  order = {'NP':1})

GC_561 = Coupling(name = 'GC_561',
                  value = '2*complex(0,1)*I10a2232*Lam',
                  order = {'NP':1})

GC_562 = Coupling(name = 'GC_562',
                  value = '2*complex(0,1)*I10a2233*Lam',
                  order = {'NP':1})

GC_563 = Coupling(name = 'GC_563',
                  value = '2*complex(0,1)*I10a2311*Lam',
                  order = {'NP':1})

GC_564 = Coupling(name = 'GC_564',
                  value = '2*complex(0,1)*I10a2312*Lam',
                  order = {'NP':1})

GC_565 = Coupling(name = 'GC_565',
                  value = '2*complex(0,1)*I10a2313*Lam',
                  order = {'NP':1})

GC_566 = Coupling(name = 'GC_566',
                  value = '2*complex(0,1)*I10a2321*Lam',
                  order = {'NP':1})

GC_567 = Coupling(name = 'GC_567',
                  value = '2*complex(0,1)*I10a2322*Lam',
                  order = {'NP':1})

GC_568 = Coupling(name = 'GC_568',
                  value = '2*complex(0,1)*I10a2323*Lam',
                  order = {'NP':1})

GC_569 = Coupling(name = 'GC_569',
                  value = '2*complex(0,1)*I10a2331*Lam',
                  order = {'NP':1})

GC_570 = Coupling(name = 'GC_570',
                  value = '2*complex(0,1)*I10a2332*Lam',
                  order = {'NP':1})

GC_571 = Coupling(name = 'GC_571',
                  value = '2*complex(0,1)*I10a2333*Lam',
                  order = {'NP':1})

GC_572 = Coupling(name = 'GC_572',
                  value = '2*complex(0,1)*I10a3111*Lam',
                  order = {'NP':1})

GC_573 = Coupling(name = 'GC_573',
                  value = '2*complex(0,1)*I10a3112*Lam',
                  order = {'NP':1})

GC_574 = Coupling(name = 'GC_574',
                  value = '2*complex(0,1)*I10a3113*Lam',
                  order = {'NP':1})

GC_575 = Coupling(name = 'GC_575',
                  value = '2*complex(0,1)*I10a3121*Lam',
                  order = {'NP':1})

GC_576 = Coupling(name = 'GC_576',
                  value = '2*complex(0,1)*I10a3122*Lam',
                  order = {'NP':1})

GC_577 = Coupling(name = 'GC_577',
                  value = '2*complex(0,1)*I10a3123*Lam',
                  order = {'NP':1})

GC_578 = Coupling(name = 'GC_578',
                  value = '2*complex(0,1)*I10a3131*Lam',
                  order = {'NP':1})

GC_579 = Coupling(name = 'GC_579',
                  value = '2*complex(0,1)*I10a3132*Lam',
                  order = {'NP':1})

GC_580 = Coupling(name = 'GC_580',
                  value = '2*complex(0,1)*I10a3133*Lam',
                  order = {'NP':1})

GC_581 = Coupling(name = 'GC_581',
                  value = '2*complex(0,1)*I10a3211*Lam',
                  order = {'NP':1})

GC_582 = Coupling(name = 'GC_582',
                  value = '2*complex(0,1)*I10a3212*Lam',
                  order = {'NP':1})

GC_583 = Coupling(name = 'GC_583',
                  value = '2*complex(0,1)*I10a3213*Lam',
                  order = {'NP':1})

GC_584 = Coupling(name = 'GC_584',
                  value = '2*complex(0,1)*I10a3221*Lam',
                  order = {'NP':1})

GC_585 = Coupling(name = 'GC_585',
                  value = '2*complex(0,1)*I10a3222*Lam',
                  order = {'NP':1})

GC_586 = Coupling(name = 'GC_586',
                  value = '2*complex(0,1)*I10a3223*Lam',
                  order = {'NP':1})

GC_587 = Coupling(name = 'GC_587',
                  value = '2*complex(0,1)*I10a3231*Lam',
                  order = {'NP':1})

GC_588 = Coupling(name = 'GC_588',
                  value = '2*complex(0,1)*I10a3232*Lam',
                  order = {'NP':1})

GC_589 = Coupling(name = 'GC_589',
                  value = '2*complex(0,1)*I10a3233*Lam',
                  order = {'NP':1})

GC_590 = Coupling(name = 'GC_590',
                  value = '2*complex(0,1)*I10a3311*Lam',
                  order = {'NP':1})

GC_591 = Coupling(name = 'GC_591',
                  value = '2*complex(0,1)*I10a3312*Lam',
                  order = {'NP':1})

GC_592 = Coupling(name = 'GC_592',
                  value = '2*complex(0,1)*I10a3313*Lam',
                  order = {'NP':1})

GC_593 = Coupling(name = 'GC_593',
                  value = '2*complex(0,1)*I10a3321*Lam',
                  order = {'NP':1})

GC_594 = Coupling(name = 'GC_594',
                  value = '2*complex(0,1)*I10a3322*Lam',
                  order = {'NP':1})

GC_595 = Coupling(name = 'GC_595',
                  value = '2*complex(0,1)*I10a3323*Lam',
                  order = {'NP':1})

GC_596 = Coupling(name = 'GC_596',
                  value = '2*complex(0,1)*I10a3331*Lam',
                  order = {'NP':1})

GC_597 = Coupling(name = 'GC_597',
                  value = '2*complex(0,1)*I10a3332*Lam',
                  order = {'NP':1})

GC_598 = Coupling(name = 'GC_598',
                  value = '2*complex(0,1)*I10a3333*Lam',
                  order = {'NP':1})

GC_599 = Coupling(name = 'GC_599',
                  value = '(complex(0,1)*I11a1111*Lam)/4.',
                  order = {'NP':1})

GC_600 = Coupling(name = 'GC_600',
                  value = '-(complex(0,1)*I11a1111*Lam)/2.',
                  order = {'NP':1})

GC_601 = Coupling(name = 'GC_601',
                  value = '(complex(0,1)*I11a1112*Lam)/4.',
                  order = {'NP':1})

GC_602 = Coupling(name = 'GC_602',
                  value = '-(complex(0,1)*I11a1112*Lam)/2.',
                  order = {'NP':1})

GC_603 = Coupling(name = 'GC_603',
                  value = '(complex(0,1)*I11a1113*Lam)/4.',
                  order = {'NP':1})

GC_604 = Coupling(name = 'GC_604',
                  value = '-(complex(0,1)*I11a1113*Lam)/2.',
                  order = {'NP':1})

GC_605 = Coupling(name = 'GC_605',
                  value = '(complex(0,1)*I11a1121*Lam)/4.',
                  order = {'NP':1})

GC_606 = Coupling(name = 'GC_606',
                  value = '-(complex(0,1)*I11a1121*Lam)/2.',
                  order = {'NP':1})

GC_607 = Coupling(name = 'GC_607',
                  value = '(complex(0,1)*I11a1122*Lam)/4.',
                  order = {'NP':1})

GC_608 = Coupling(name = 'GC_608',
                  value = '-(complex(0,1)*I11a1122*Lam)/2.',
                  order = {'NP':1})

GC_609 = Coupling(name = 'GC_609',
                  value = '(complex(0,1)*I11a1123*Lam)/4.',
                  order = {'NP':1})

GC_610 = Coupling(name = 'GC_610',
                  value = '-(complex(0,1)*I11a1123*Lam)/2.',
                  order = {'NP':1})

GC_611 = Coupling(name = 'GC_611',
                  value = '(complex(0,1)*I11a1131*Lam)/4.',
                  order = {'NP':1})

GC_612 = Coupling(name = 'GC_612',
                  value = '-(complex(0,1)*I11a1131*Lam)/2.',
                  order = {'NP':1})

GC_613 = Coupling(name = 'GC_613',
                  value = '(complex(0,1)*I11a1132*Lam)/4.',
                  order = {'NP':1})

GC_614 = Coupling(name = 'GC_614',
                  value = '-(complex(0,1)*I11a1132*Lam)/2.',
                  order = {'NP':1})

GC_615 = Coupling(name = 'GC_615',
                  value = '(complex(0,1)*I11a1133*Lam)/4.',
                  order = {'NP':1})

GC_616 = Coupling(name = 'GC_616',
                  value = '-(complex(0,1)*I11a1133*Lam)/2.',
                  order = {'NP':1})

GC_617 = Coupling(name = 'GC_617',
                  value = '(complex(0,1)*I11a1211*Lam)/4.',
                  order = {'NP':1})

GC_618 = Coupling(name = 'GC_618',
                  value = '-(complex(0,1)*I11a1211*Lam)/2.',
                  order = {'NP':1})

GC_619 = Coupling(name = 'GC_619',
                  value = '(complex(0,1)*I11a1212*Lam)/4.',
                  order = {'NP':1})

GC_620 = Coupling(name = 'GC_620',
                  value = '-(complex(0,1)*I11a1212*Lam)/2.',
                  order = {'NP':1})

GC_621 = Coupling(name = 'GC_621',
                  value = '(complex(0,1)*I11a1213*Lam)/4.',
                  order = {'NP':1})

GC_622 = Coupling(name = 'GC_622',
                  value = '-(complex(0,1)*I11a1213*Lam)/2.',
                  order = {'NP':1})

GC_623 = Coupling(name = 'GC_623',
                  value = '(complex(0,1)*I11a1221*Lam)/4.',
                  order = {'NP':1})

GC_624 = Coupling(name = 'GC_624',
                  value = '-(complex(0,1)*I11a1221*Lam)/2.',
                  order = {'NP':1})

GC_625 = Coupling(name = 'GC_625',
                  value = '(complex(0,1)*I11a1222*Lam)/4.',
                  order = {'NP':1})

GC_626 = Coupling(name = 'GC_626',
                  value = '-(complex(0,1)*I11a1222*Lam)/2.',
                  order = {'NP':1})

GC_627 = Coupling(name = 'GC_627',
                  value = '(complex(0,1)*I11a1223*Lam)/4.',
                  order = {'NP':1})

GC_628 = Coupling(name = 'GC_628',
                  value = '-(complex(0,1)*I11a1223*Lam)/2.',
                  order = {'NP':1})

GC_629 = Coupling(name = 'GC_629',
                  value = '(complex(0,1)*I11a1231*Lam)/4.',
                  order = {'NP':1})

GC_630 = Coupling(name = 'GC_630',
                  value = '-(complex(0,1)*I11a1231*Lam)/2.',
                  order = {'NP':1})

GC_631 = Coupling(name = 'GC_631',
                  value = '(complex(0,1)*I11a1232*Lam)/4.',
                  order = {'NP':1})

GC_632 = Coupling(name = 'GC_632',
                  value = '-(complex(0,1)*I11a1232*Lam)/2.',
                  order = {'NP':1})

GC_633 = Coupling(name = 'GC_633',
                  value = '(complex(0,1)*I11a1233*Lam)/4.',
                  order = {'NP':1})

GC_634 = Coupling(name = 'GC_634',
                  value = '-(complex(0,1)*I11a1233*Lam)/2.',
                  order = {'NP':1})

GC_635 = Coupling(name = 'GC_635',
                  value = '(complex(0,1)*I11a1311*Lam)/4.',
                  order = {'NP':1})

GC_636 = Coupling(name = 'GC_636',
                  value = '-(complex(0,1)*I11a1311*Lam)/2.',
                  order = {'NP':1})

GC_637 = Coupling(name = 'GC_637',
                  value = '(complex(0,1)*I11a1312*Lam)/4.',
                  order = {'NP':1})

GC_638 = Coupling(name = 'GC_638',
                  value = '-(complex(0,1)*I11a1312*Lam)/2.',
                  order = {'NP':1})

GC_639 = Coupling(name = 'GC_639',
                  value = '(complex(0,1)*I11a1313*Lam)/4.',
                  order = {'NP':1})

GC_640 = Coupling(name = 'GC_640',
                  value = '-(complex(0,1)*I11a1313*Lam)/2.',
                  order = {'NP':1})

GC_641 = Coupling(name = 'GC_641',
                  value = '(complex(0,1)*I11a1321*Lam)/4.',
                  order = {'NP':1})

GC_642 = Coupling(name = 'GC_642',
                  value = '-(complex(0,1)*I11a1321*Lam)/2.',
                  order = {'NP':1})

GC_643 = Coupling(name = 'GC_643',
                  value = '(complex(0,1)*I11a1322*Lam)/4.',
                  order = {'NP':1})

GC_644 = Coupling(name = 'GC_644',
                  value = '-(complex(0,1)*I11a1322*Lam)/2.',
                  order = {'NP':1})

GC_645 = Coupling(name = 'GC_645',
                  value = '(complex(0,1)*I11a1323*Lam)/4.',
                  order = {'NP':1})

GC_646 = Coupling(name = 'GC_646',
                  value = '-(complex(0,1)*I11a1323*Lam)/2.',
                  order = {'NP':1})

GC_647 = Coupling(name = 'GC_647',
                  value = '(complex(0,1)*I11a1331*Lam)/4.',
                  order = {'NP':1})

GC_648 = Coupling(name = 'GC_648',
                  value = '-(complex(0,1)*I11a1331*Lam)/2.',
                  order = {'NP':1})

GC_649 = Coupling(name = 'GC_649',
                  value = '(complex(0,1)*I11a1332*Lam)/4.',
                  order = {'NP':1})

GC_650 = Coupling(name = 'GC_650',
                  value = '-(complex(0,1)*I11a1332*Lam)/2.',
                  order = {'NP':1})

GC_651 = Coupling(name = 'GC_651',
                  value = '(complex(0,1)*I11a1333*Lam)/4.',
                  order = {'NP':1})

GC_652 = Coupling(name = 'GC_652',
                  value = '-(complex(0,1)*I11a1333*Lam)/2.',
                  order = {'NP':1})

GC_653 = Coupling(name = 'GC_653',
                  value = '(complex(0,1)*I11a2111*Lam)/4.',
                  order = {'NP':1})

GC_654 = Coupling(name = 'GC_654',
                  value = '-(complex(0,1)*I11a2111*Lam)/2.',
                  order = {'NP':1})

GC_655 = Coupling(name = 'GC_655',
                  value = '(complex(0,1)*I11a2112*Lam)/4.',
                  order = {'NP':1})

GC_656 = Coupling(name = 'GC_656',
                  value = '-(complex(0,1)*I11a2112*Lam)/2.',
                  order = {'NP':1})

GC_657 = Coupling(name = 'GC_657',
                  value = '(complex(0,1)*I11a2113*Lam)/4.',
                  order = {'NP':1})

GC_658 = Coupling(name = 'GC_658',
                  value = '-(complex(0,1)*I11a2113*Lam)/2.',
                  order = {'NP':1})

GC_659 = Coupling(name = 'GC_659',
                  value = '(complex(0,1)*I11a2121*Lam)/4.',
                  order = {'NP':1})

GC_660 = Coupling(name = 'GC_660',
                  value = '-(complex(0,1)*I11a2121*Lam)/2.',
                  order = {'NP':1})

GC_661 = Coupling(name = 'GC_661',
                  value = '(complex(0,1)*I11a2122*Lam)/4.',
                  order = {'NP':1})

GC_662 = Coupling(name = 'GC_662',
                  value = '-(complex(0,1)*I11a2122*Lam)/2.',
                  order = {'NP':1})

GC_663 = Coupling(name = 'GC_663',
                  value = '(complex(0,1)*I11a2123*Lam)/4.',
                  order = {'NP':1})

GC_664 = Coupling(name = 'GC_664',
                  value = '-(complex(0,1)*I11a2123*Lam)/2.',
                  order = {'NP':1})

GC_665 = Coupling(name = 'GC_665',
                  value = '(complex(0,1)*I11a2131*Lam)/4.',
                  order = {'NP':1})

GC_666 = Coupling(name = 'GC_666',
                  value = '-(complex(0,1)*I11a2131*Lam)/2.',
                  order = {'NP':1})

GC_667 = Coupling(name = 'GC_667',
                  value = '(complex(0,1)*I11a2132*Lam)/4.',
                  order = {'NP':1})

GC_668 = Coupling(name = 'GC_668',
                  value = '-(complex(0,1)*I11a2132*Lam)/2.',
                  order = {'NP':1})

GC_669 = Coupling(name = 'GC_669',
                  value = '(complex(0,1)*I11a2133*Lam)/4.',
                  order = {'NP':1})

GC_670 = Coupling(name = 'GC_670',
                  value = '-(complex(0,1)*I11a2133*Lam)/2.',
                  order = {'NP':1})

GC_671 = Coupling(name = 'GC_671',
                  value = '(complex(0,1)*I11a2211*Lam)/4.',
                  order = {'NP':1})

GC_672 = Coupling(name = 'GC_672',
                  value = '-(complex(0,1)*I11a2211*Lam)/2.',
                  order = {'NP':1})

GC_673 = Coupling(name = 'GC_673',
                  value = '(complex(0,1)*I11a2212*Lam)/4.',
                  order = {'NP':1})

GC_674 = Coupling(name = 'GC_674',
                  value = '-(complex(0,1)*I11a2212*Lam)/2.',
                  order = {'NP':1})

GC_675 = Coupling(name = 'GC_675',
                  value = '(complex(0,1)*I11a2213*Lam)/4.',
                  order = {'NP':1})

GC_676 = Coupling(name = 'GC_676',
                  value = '-(complex(0,1)*I11a2213*Lam)/2.',
                  order = {'NP':1})

GC_677 = Coupling(name = 'GC_677',
                  value = '(complex(0,1)*I11a2221*Lam)/4.',
                  order = {'NP':1})

GC_678 = Coupling(name = 'GC_678',
                  value = '-(complex(0,1)*I11a2221*Lam)/2.',
                  order = {'NP':1})

GC_679 = Coupling(name = 'GC_679',
                  value = '(complex(0,1)*I11a2222*Lam)/4.',
                  order = {'NP':1})

GC_680 = Coupling(name = 'GC_680',
                  value = '-(complex(0,1)*I11a2222*Lam)/2.',
                  order = {'NP':1})

GC_681 = Coupling(name = 'GC_681',
                  value = '(complex(0,1)*I11a2223*Lam)/4.',
                  order = {'NP':1})

GC_682 = Coupling(name = 'GC_682',
                  value = '-(complex(0,1)*I11a2223*Lam)/2.',
                  order = {'NP':1})

GC_683 = Coupling(name = 'GC_683',
                  value = '(complex(0,1)*I11a2231*Lam)/4.',
                  order = {'NP':1})

GC_684 = Coupling(name = 'GC_684',
                  value = '-(complex(0,1)*I11a2231*Lam)/2.',
                  order = {'NP':1})

GC_685 = Coupling(name = 'GC_685',
                  value = '(complex(0,1)*I11a2232*Lam)/4.',
                  order = {'NP':1})

GC_686 = Coupling(name = 'GC_686',
                  value = '-(complex(0,1)*I11a2232*Lam)/2.',
                  order = {'NP':1})

GC_687 = Coupling(name = 'GC_687',
                  value = '(complex(0,1)*I11a2233*Lam)/4.',
                  order = {'NP':1})

GC_688 = Coupling(name = 'GC_688',
                  value = '-(complex(0,1)*I11a2233*Lam)/2.',
                  order = {'NP':1})

GC_689 = Coupling(name = 'GC_689',
                  value = '(complex(0,1)*I11a2311*Lam)/4.',
                  order = {'NP':1})

GC_690 = Coupling(name = 'GC_690',
                  value = '-(complex(0,1)*I11a2311*Lam)/2.',
                  order = {'NP':1})

GC_691 = Coupling(name = 'GC_691',
                  value = '(complex(0,1)*I11a2312*Lam)/4.',
                  order = {'NP':1})

GC_692 = Coupling(name = 'GC_692',
                  value = '-(complex(0,1)*I11a2312*Lam)/2.',
                  order = {'NP':1})

GC_693 = Coupling(name = 'GC_693',
                  value = '(complex(0,1)*I11a2313*Lam)/4.',
                  order = {'NP':1})

GC_694 = Coupling(name = 'GC_694',
                  value = '-(complex(0,1)*I11a2313*Lam)/2.',
                  order = {'NP':1})

GC_695 = Coupling(name = 'GC_695',
                  value = '(complex(0,1)*I11a2321*Lam)/4.',
                  order = {'NP':1})

GC_696 = Coupling(name = 'GC_696',
                  value = '-(complex(0,1)*I11a2321*Lam)/2.',
                  order = {'NP':1})

GC_697 = Coupling(name = 'GC_697',
                  value = '(complex(0,1)*I11a2322*Lam)/4.',
                  order = {'NP':1})

GC_698 = Coupling(name = 'GC_698',
                  value = '-(complex(0,1)*I11a2322*Lam)/2.',
                  order = {'NP':1})

GC_699 = Coupling(name = 'GC_699',
                  value = '(complex(0,1)*I11a2323*Lam)/4.',
                  order = {'NP':1})

GC_700 = Coupling(name = 'GC_700',
                  value = '-(complex(0,1)*I11a2323*Lam)/2.',
                  order = {'NP':1})

GC_701 = Coupling(name = 'GC_701',
                  value = '(complex(0,1)*I11a2331*Lam)/4.',
                  order = {'NP':1})

GC_702 = Coupling(name = 'GC_702',
                  value = '-(complex(0,1)*I11a2331*Lam)/2.',
                  order = {'NP':1})

GC_703 = Coupling(name = 'GC_703',
                  value = '(complex(0,1)*I11a2332*Lam)/4.',
                  order = {'NP':1})

GC_704 = Coupling(name = 'GC_704',
                  value = '-(complex(0,1)*I11a2332*Lam)/2.',
                  order = {'NP':1})

GC_705 = Coupling(name = 'GC_705',
                  value = '(complex(0,1)*I11a2333*Lam)/4.',
                  order = {'NP':1})

GC_706 = Coupling(name = 'GC_706',
                  value = '-(complex(0,1)*I11a2333*Lam)/2.',
                  order = {'NP':1})

GC_707 = Coupling(name = 'GC_707',
                  value = '(complex(0,1)*I11a3111*Lam)/4.',
                  order = {'NP':1})

GC_708 = Coupling(name = 'GC_708',
                  value = '-(complex(0,1)*I11a3111*Lam)/2.',
                  order = {'NP':1})

GC_709 = Coupling(name = 'GC_709',
                  value = '(complex(0,1)*I11a3112*Lam)/4.',
                  order = {'NP':1})

GC_710 = Coupling(name = 'GC_710',
                  value = '-(complex(0,1)*I11a3112*Lam)/2.',
                  order = {'NP':1})

GC_711 = Coupling(name = 'GC_711',
                  value = '(complex(0,1)*I11a3113*Lam)/4.',
                  order = {'NP':1})

GC_712 = Coupling(name = 'GC_712',
                  value = '-(complex(0,1)*I11a3113*Lam)/2.',
                  order = {'NP':1})

GC_713 = Coupling(name = 'GC_713',
                  value = '(complex(0,1)*I11a3121*Lam)/4.',
                  order = {'NP':1})

GC_714 = Coupling(name = 'GC_714',
                  value = '-(complex(0,1)*I11a3121*Lam)/2.',
                  order = {'NP':1})

GC_715 = Coupling(name = 'GC_715',
                  value = '(complex(0,1)*I11a3122*Lam)/4.',
                  order = {'NP':1})

GC_716 = Coupling(name = 'GC_716',
                  value = '-(complex(0,1)*I11a3122*Lam)/2.',
                  order = {'NP':1})

GC_717 = Coupling(name = 'GC_717',
                  value = '(complex(0,1)*I11a3123*Lam)/4.',
                  order = {'NP':1})

GC_718 = Coupling(name = 'GC_718',
                  value = '-(complex(0,1)*I11a3123*Lam)/2.',
                  order = {'NP':1})

GC_719 = Coupling(name = 'GC_719',
                  value = '(complex(0,1)*I11a3131*Lam)/4.',
                  order = {'NP':1})

GC_720 = Coupling(name = 'GC_720',
                  value = '-(complex(0,1)*I11a3131*Lam)/2.',
                  order = {'NP':1})

GC_721 = Coupling(name = 'GC_721',
                  value = '(complex(0,1)*I11a3132*Lam)/4.',
                  order = {'NP':1})

GC_722 = Coupling(name = 'GC_722',
                  value = '-(complex(0,1)*I11a3132*Lam)/2.',
                  order = {'NP':1})

GC_723 = Coupling(name = 'GC_723',
                  value = '(complex(0,1)*I11a3133*Lam)/4.',
                  order = {'NP':1})

GC_724 = Coupling(name = 'GC_724',
                  value = '-(complex(0,1)*I11a3133*Lam)/2.',
                  order = {'NP':1})

GC_725 = Coupling(name = 'GC_725',
                  value = '(complex(0,1)*I11a3211*Lam)/4.',
                  order = {'NP':1})

GC_726 = Coupling(name = 'GC_726',
                  value = '-(complex(0,1)*I11a3211*Lam)/2.',
                  order = {'NP':1})

GC_727 = Coupling(name = 'GC_727',
                  value = '(complex(0,1)*I11a3212*Lam)/4.',
                  order = {'NP':1})

GC_728 = Coupling(name = 'GC_728',
                  value = '-(complex(0,1)*I11a3212*Lam)/2.',
                  order = {'NP':1})

GC_729 = Coupling(name = 'GC_729',
                  value = '(complex(0,1)*I11a3213*Lam)/4.',
                  order = {'NP':1})

GC_730 = Coupling(name = 'GC_730',
                  value = '-(complex(0,1)*I11a3213*Lam)/2.',
                  order = {'NP':1})

GC_731 = Coupling(name = 'GC_731',
                  value = '(complex(0,1)*I11a3221*Lam)/4.',
                  order = {'NP':1})

GC_732 = Coupling(name = 'GC_732',
                  value = '-(complex(0,1)*I11a3221*Lam)/2.',
                  order = {'NP':1})

GC_733 = Coupling(name = 'GC_733',
                  value = '(complex(0,1)*I11a3222*Lam)/4.',
                  order = {'NP':1})

GC_734 = Coupling(name = 'GC_734',
                  value = '-(complex(0,1)*I11a3222*Lam)/2.',
                  order = {'NP':1})

GC_735 = Coupling(name = 'GC_735',
                  value = '(complex(0,1)*I11a3223*Lam)/4.',
                  order = {'NP':1})

GC_736 = Coupling(name = 'GC_736',
                  value = '-(complex(0,1)*I11a3223*Lam)/2.',
                  order = {'NP':1})

GC_737 = Coupling(name = 'GC_737',
                  value = '(complex(0,1)*I11a3231*Lam)/4.',
                  order = {'NP':1})

GC_738 = Coupling(name = 'GC_738',
                  value = '-(complex(0,1)*I11a3231*Lam)/2.',
                  order = {'NP':1})

GC_739 = Coupling(name = 'GC_739',
                  value = '(complex(0,1)*I11a3232*Lam)/4.',
                  order = {'NP':1})

GC_740 = Coupling(name = 'GC_740',
                  value = '-(complex(0,1)*I11a3232*Lam)/2.',
                  order = {'NP':1})

GC_741 = Coupling(name = 'GC_741',
                  value = '(complex(0,1)*I11a3233*Lam)/4.',
                  order = {'NP':1})

GC_742 = Coupling(name = 'GC_742',
                  value = '-(complex(0,1)*I11a3233*Lam)/2.',
                  order = {'NP':1})

GC_743 = Coupling(name = 'GC_743',
                  value = '(complex(0,1)*I11a3311*Lam)/4.',
                  order = {'NP':1})

GC_744 = Coupling(name = 'GC_744',
                  value = '-(complex(0,1)*I11a3311*Lam)/2.',
                  order = {'NP':1})

GC_745 = Coupling(name = 'GC_745',
                  value = '(complex(0,1)*I11a3312*Lam)/4.',
                  order = {'NP':1})

GC_746 = Coupling(name = 'GC_746',
                  value = '-(complex(0,1)*I11a3312*Lam)/2.',
                  order = {'NP':1})

GC_747 = Coupling(name = 'GC_747',
                  value = '(complex(0,1)*I11a3313*Lam)/4.',
                  order = {'NP':1})

GC_748 = Coupling(name = 'GC_748',
                  value = '-(complex(0,1)*I11a3313*Lam)/2.',
                  order = {'NP':1})

GC_749 = Coupling(name = 'GC_749',
                  value = '(complex(0,1)*I11a3321*Lam)/4.',
                  order = {'NP':1})

GC_750 = Coupling(name = 'GC_750',
                  value = '-(complex(0,1)*I11a3321*Lam)/2.',
                  order = {'NP':1})

GC_751 = Coupling(name = 'GC_751',
                  value = '(complex(0,1)*I11a3322*Lam)/4.',
                  order = {'NP':1})

GC_752 = Coupling(name = 'GC_752',
                  value = '-(complex(0,1)*I11a3322*Lam)/2.',
                  order = {'NP':1})

GC_753 = Coupling(name = 'GC_753',
                  value = '(complex(0,1)*I11a3323*Lam)/4.',
                  order = {'NP':1})

GC_754 = Coupling(name = 'GC_754',
                  value = '-(complex(0,1)*I11a3323*Lam)/2.',
                  order = {'NP':1})

GC_755 = Coupling(name = 'GC_755',
                  value = '(complex(0,1)*I11a3331*Lam)/4.',
                  order = {'NP':1})

GC_756 = Coupling(name = 'GC_756',
                  value = '-(complex(0,1)*I11a3331*Lam)/2.',
                  order = {'NP':1})

GC_757 = Coupling(name = 'GC_757',
                  value = '(complex(0,1)*I11a3332*Lam)/4.',
                  order = {'NP':1})

GC_758 = Coupling(name = 'GC_758',
                  value = '-(complex(0,1)*I11a3332*Lam)/2.',
                  order = {'NP':1})

GC_759 = Coupling(name = 'GC_759',
                  value = '(complex(0,1)*I11a3333*Lam)/4.',
                  order = {'NP':1})

GC_760 = Coupling(name = 'GC_760',
                  value = '-(complex(0,1)*I11a3333*Lam)/2.',
                  order = {'NP':1})

GC_761 = Coupling(name = 'GC_761',
                  value = 'complex(0,1)*I12a1111*Lam',
                  order = {'NP':1})

GC_762 = Coupling(name = 'GC_762',
                  value = 'complex(0,1)*I12a1112*Lam',
                  order = {'NP':1})

GC_763 = Coupling(name = 'GC_763',
                  value = 'complex(0,1)*I12a1113*Lam',
                  order = {'NP':1})

GC_764 = Coupling(name = 'GC_764',
                  value = 'complex(0,1)*I12a1121*Lam',
                  order = {'NP':1})

GC_765 = Coupling(name = 'GC_765',
                  value = 'complex(0,1)*I12a1122*Lam',
                  order = {'NP':1})

GC_766 = Coupling(name = 'GC_766',
                  value = 'complex(0,1)*I12a1123*Lam',
                  order = {'NP':1})

GC_767 = Coupling(name = 'GC_767',
                  value = 'complex(0,1)*I12a1131*Lam',
                  order = {'NP':1})

GC_768 = Coupling(name = 'GC_768',
                  value = 'complex(0,1)*I12a1132*Lam',
                  order = {'NP':1})

GC_769 = Coupling(name = 'GC_769',
                  value = 'complex(0,1)*I12a1133*Lam',
                  order = {'NP':1})

GC_770 = Coupling(name = 'GC_770',
                  value = 'complex(0,1)*I12a1211*Lam',
                  order = {'NP':1})

GC_771 = Coupling(name = 'GC_771',
                  value = 'complex(0,1)*I12a1212*Lam',
                  order = {'NP':1})

GC_772 = Coupling(name = 'GC_772',
                  value = 'complex(0,1)*I12a1213*Lam',
                  order = {'NP':1})

GC_773 = Coupling(name = 'GC_773',
                  value = 'complex(0,1)*I12a1221*Lam',
                  order = {'NP':1})

GC_774 = Coupling(name = 'GC_774',
                  value = 'complex(0,1)*I12a1222*Lam',
                  order = {'NP':1})

GC_775 = Coupling(name = 'GC_775',
                  value = 'complex(0,1)*I12a1223*Lam',
                  order = {'NP':1})

GC_776 = Coupling(name = 'GC_776',
                  value = 'complex(0,1)*I12a1231*Lam',
                  order = {'NP':1})

GC_777 = Coupling(name = 'GC_777',
                  value = 'complex(0,1)*I12a1232*Lam',
                  order = {'NP':1})

GC_778 = Coupling(name = 'GC_778',
                  value = 'complex(0,1)*I12a1233*Lam',
                  order = {'NP':1})

GC_779 = Coupling(name = 'GC_779',
                  value = 'complex(0,1)*I12a1311*Lam',
                  order = {'NP':1})

GC_780 = Coupling(name = 'GC_780',
                  value = 'complex(0,1)*I12a1312*Lam',
                  order = {'NP':1})

GC_781 = Coupling(name = 'GC_781',
                  value = 'complex(0,1)*I12a1313*Lam',
                  order = {'NP':1})

GC_782 = Coupling(name = 'GC_782',
                  value = 'complex(0,1)*I12a1321*Lam',
                  order = {'NP':1})

GC_783 = Coupling(name = 'GC_783',
                  value = 'complex(0,1)*I12a1322*Lam',
                  order = {'NP':1})

GC_784 = Coupling(name = 'GC_784',
                  value = 'complex(0,1)*I12a1323*Lam',
                  order = {'NP':1})

GC_785 = Coupling(name = 'GC_785',
                  value = 'complex(0,1)*I12a1331*Lam',
                  order = {'NP':1})

GC_786 = Coupling(name = 'GC_786',
                  value = 'complex(0,1)*I12a1332*Lam',
                  order = {'NP':1})

GC_787 = Coupling(name = 'GC_787',
                  value = 'complex(0,1)*I12a1333*Lam',
                  order = {'NP':1})

GC_788 = Coupling(name = 'GC_788',
                  value = 'complex(0,1)*I12a2111*Lam',
                  order = {'NP':1})

GC_789 = Coupling(name = 'GC_789',
                  value = 'complex(0,1)*I12a2112*Lam',
                  order = {'NP':1})

GC_790 = Coupling(name = 'GC_790',
                  value = 'complex(0,1)*I12a2113*Lam',
                  order = {'NP':1})

GC_791 = Coupling(name = 'GC_791',
                  value = 'complex(0,1)*I12a2121*Lam',
                  order = {'NP':1})

GC_792 = Coupling(name = 'GC_792',
                  value = 'complex(0,1)*I12a2122*Lam',
                  order = {'NP':1})

GC_793 = Coupling(name = 'GC_793',
                  value = 'complex(0,1)*I12a2123*Lam',
                  order = {'NP':1})

GC_794 = Coupling(name = 'GC_794',
                  value = 'complex(0,1)*I12a2131*Lam',
                  order = {'NP':1})

GC_795 = Coupling(name = 'GC_795',
                  value = 'complex(0,1)*I12a2132*Lam',
                  order = {'NP':1})

GC_796 = Coupling(name = 'GC_796',
                  value = 'complex(0,1)*I12a2133*Lam',
                  order = {'NP':1})

GC_797 = Coupling(name = 'GC_797',
                  value = 'complex(0,1)*I12a2211*Lam',
                  order = {'NP':1})

GC_798 = Coupling(name = 'GC_798',
                  value = 'complex(0,1)*I12a2212*Lam',
                  order = {'NP':1})

GC_799 = Coupling(name = 'GC_799',
                  value = 'complex(0,1)*I12a2213*Lam',
                  order = {'NP':1})

GC_800 = Coupling(name = 'GC_800',
                  value = 'complex(0,1)*I12a2221*Lam',
                  order = {'NP':1})

GC_801 = Coupling(name = 'GC_801',
                  value = 'complex(0,1)*I12a2222*Lam',
                  order = {'NP':1})

GC_802 = Coupling(name = 'GC_802',
                  value = 'complex(0,1)*I12a2223*Lam',
                  order = {'NP':1})

GC_803 = Coupling(name = 'GC_803',
                  value = 'complex(0,1)*I12a2231*Lam',
                  order = {'NP':1})

GC_804 = Coupling(name = 'GC_804',
                  value = 'complex(0,1)*I12a2232*Lam',
                  order = {'NP':1})

GC_805 = Coupling(name = 'GC_805',
                  value = 'complex(0,1)*I12a2233*Lam',
                  order = {'NP':1})

GC_806 = Coupling(name = 'GC_806',
                  value = 'complex(0,1)*I12a2311*Lam',
                  order = {'NP':1})

GC_807 = Coupling(name = 'GC_807',
                  value = 'complex(0,1)*I12a2312*Lam',
                  order = {'NP':1})

GC_808 = Coupling(name = 'GC_808',
                  value = 'complex(0,1)*I12a2313*Lam',
                  order = {'NP':1})

GC_809 = Coupling(name = 'GC_809',
                  value = 'complex(0,1)*I12a2321*Lam',
                  order = {'NP':1})

GC_810 = Coupling(name = 'GC_810',
                  value = 'complex(0,1)*I12a2322*Lam',
                  order = {'NP':1})

GC_811 = Coupling(name = 'GC_811',
                  value = 'complex(0,1)*I12a2323*Lam',
                  order = {'NP':1})

GC_812 = Coupling(name = 'GC_812',
                  value = 'complex(0,1)*I12a2331*Lam',
                  order = {'NP':1})

GC_813 = Coupling(name = 'GC_813',
                  value = 'complex(0,1)*I12a2332*Lam',
                  order = {'NP':1})

GC_814 = Coupling(name = 'GC_814',
                  value = 'complex(0,1)*I12a2333*Lam',
                  order = {'NP':1})

GC_815 = Coupling(name = 'GC_815',
                  value = 'complex(0,1)*I12a3111*Lam',
                  order = {'NP':1})

GC_816 = Coupling(name = 'GC_816',
                  value = 'complex(0,1)*I12a3112*Lam',
                  order = {'NP':1})

GC_817 = Coupling(name = 'GC_817',
                  value = 'complex(0,1)*I12a3113*Lam',
                  order = {'NP':1})

GC_818 = Coupling(name = 'GC_818',
                  value = 'complex(0,1)*I12a3121*Lam',
                  order = {'NP':1})

GC_819 = Coupling(name = 'GC_819',
                  value = 'complex(0,1)*I12a3122*Lam',
                  order = {'NP':1})

GC_820 = Coupling(name = 'GC_820',
                  value = 'complex(0,1)*I12a3123*Lam',
                  order = {'NP':1})

GC_821 = Coupling(name = 'GC_821',
                  value = 'complex(0,1)*I12a3131*Lam',
                  order = {'NP':1})

GC_822 = Coupling(name = 'GC_822',
                  value = 'complex(0,1)*I12a3132*Lam',
                  order = {'NP':1})

GC_823 = Coupling(name = 'GC_823',
                  value = 'complex(0,1)*I12a3133*Lam',
                  order = {'NP':1})

GC_824 = Coupling(name = 'GC_824',
                  value = 'complex(0,1)*I12a3211*Lam',
                  order = {'NP':1})

GC_825 = Coupling(name = 'GC_825',
                  value = 'complex(0,1)*I12a3212*Lam',
                  order = {'NP':1})

GC_826 = Coupling(name = 'GC_826',
                  value = 'complex(0,1)*I12a3213*Lam',
                  order = {'NP':1})

GC_827 = Coupling(name = 'GC_827',
                  value = 'complex(0,1)*I12a3221*Lam',
                  order = {'NP':1})

GC_828 = Coupling(name = 'GC_828',
                  value = 'complex(0,1)*I12a3222*Lam',
                  order = {'NP':1})

GC_829 = Coupling(name = 'GC_829',
                  value = 'complex(0,1)*I12a3223*Lam',
                  order = {'NP':1})

GC_830 = Coupling(name = 'GC_830',
                  value = 'complex(0,1)*I12a3231*Lam',
                  order = {'NP':1})

GC_831 = Coupling(name = 'GC_831',
                  value = 'complex(0,1)*I12a3232*Lam',
                  order = {'NP':1})

GC_832 = Coupling(name = 'GC_832',
                  value = 'complex(0,1)*I12a3233*Lam',
                  order = {'NP':1})

GC_833 = Coupling(name = 'GC_833',
                  value = 'complex(0,1)*I12a3311*Lam',
                  order = {'NP':1})

GC_834 = Coupling(name = 'GC_834',
                  value = 'complex(0,1)*I12a3312*Lam',
                  order = {'NP':1})

GC_835 = Coupling(name = 'GC_835',
                  value = 'complex(0,1)*I12a3313*Lam',
                  order = {'NP':1})

GC_836 = Coupling(name = 'GC_836',
                  value = 'complex(0,1)*I12a3321*Lam',
                  order = {'NP':1})

GC_837 = Coupling(name = 'GC_837',
                  value = 'complex(0,1)*I12a3322*Lam',
                  order = {'NP':1})

GC_838 = Coupling(name = 'GC_838',
                  value = 'complex(0,1)*I12a3323*Lam',
                  order = {'NP':1})

GC_839 = Coupling(name = 'GC_839',
                  value = 'complex(0,1)*I12a3331*Lam',
                  order = {'NP':1})

GC_840 = Coupling(name = 'GC_840',
                  value = 'complex(0,1)*I12a3332*Lam',
                  order = {'NP':1})

GC_841 = Coupling(name = 'GC_841',
                  value = 'complex(0,1)*I12a3333*Lam',
                  order = {'NP':1})

GC_842 = Coupling(name = 'GC_842',
                  value = 'complex(0,1)*I13a1111*Lam',
                  order = {'NP':1})

GC_843 = Coupling(name = 'GC_843',
                  value = 'complex(0,1)*I13a1112*Lam',
                  order = {'NP':1})

GC_844 = Coupling(name = 'GC_844',
                  value = 'complex(0,1)*I13a1113*Lam',
                  order = {'NP':1})

GC_845 = Coupling(name = 'GC_845',
                  value = 'complex(0,1)*I13a1121*Lam',
                  order = {'NP':1})

GC_846 = Coupling(name = 'GC_846',
                  value = 'complex(0,1)*I13a1122*Lam',
                  order = {'NP':1})

GC_847 = Coupling(name = 'GC_847',
                  value = 'complex(0,1)*I13a1123*Lam',
                  order = {'NP':1})

GC_848 = Coupling(name = 'GC_848',
                  value = 'complex(0,1)*I13a1131*Lam',
                  order = {'NP':1})

GC_849 = Coupling(name = 'GC_849',
                  value = 'complex(0,1)*I13a1132*Lam',
                  order = {'NP':1})

GC_850 = Coupling(name = 'GC_850',
                  value = 'complex(0,1)*I13a1133*Lam',
                  order = {'NP':1})

GC_851 = Coupling(name = 'GC_851',
                  value = 'complex(0,1)*I13a1211*Lam',
                  order = {'NP':1})

GC_852 = Coupling(name = 'GC_852',
                  value = 'complex(0,1)*I13a1212*Lam',
                  order = {'NP':1})

GC_853 = Coupling(name = 'GC_853',
                  value = 'complex(0,1)*I13a1213*Lam',
                  order = {'NP':1})

GC_854 = Coupling(name = 'GC_854',
                  value = 'complex(0,1)*I13a1221*Lam',
                  order = {'NP':1})

GC_855 = Coupling(name = 'GC_855',
                  value = 'complex(0,1)*I13a1222*Lam',
                  order = {'NP':1})

GC_856 = Coupling(name = 'GC_856',
                  value = 'complex(0,1)*I13a1223*Lam',
                  order = {'NP':1})

GC_857 = Coupling(name = 'GC_857',
                  value = 'complex(0,1)*I13a1231*Lam',
                  order = {'NP':1})

GC_858 = Coupling(name = 'GC_858',
                  value = 'complex(0,1)*I13a1232*Lam',
                  order = {'NP':1})

GC_859 = Coupling(name = 'GC_859',
                  value = 'complex(0,1)*I13a1233*Lam',
                  order = {'NP':1})

GC_860 = Coupling(name = 'GC_860',
                  value = 'complex(0,1)*I13a1311*Lam',
                  order = {'NP':1})

GC_861 = Coupling(name = 'GC_861',
                  value = 'complex(0,1)*I13a1312*Lam',
                  order = {'NP':1})

GC_862 = Coupling(name = 'GC_862',
                  value = 'complex(0,1)*I13a1313*Lam',
                  order = {'NP':1})

GC_863 = Coupling(name = 'GC_863',
                  value = 'complex(0,1)*I13a1321*Lam',
                  order = {'NP':1})

GC_864 = Coupling(name = 'GC_864',
                  value = 'complex(0,1)*I13a1322*Lam',
                  order = {'NP':1})

GC_865 = Coupling(name = 'GC_865',
                  value = 'complex(0,1)*I13a1323*Lam',
                  order = {'NP':1})

GC_866 = Coupling(name = 'GC_866',
                  value = 'complex(0,1)*I13a1331*Lam',
                  order = {'NP':1})

GC_867 = Coupling(name = 'GC_867',
                  value = 'complex(0,1)*I13a1332*Lam',
                  order = {'NP':1})

GC_868 = Coupling(name = 'GC_868',
                  value = 'complex(0,1)*I13a1333*Lam',
                  order = {'NP':1})

GC_869 = Coupling(name = 'GC_869',
                  value = 'complex(0,1)*I13a2111*Lam',
                  order = {'NP':1})

GC_870 = Coupling(name = 'GC_870',
                  value = 'complex(0,1)*I13a2112*Lam',
                  order = {'NP':1})

GC_871 = Coupling(name = 'GC_871',
                  value = 'complex(0,1)*I13a2113*Lam',
                  order = {'NP':1})

GC_872 = Coupling(name = 'GC_872',
                  value = 'complex(0,1)*I13a2121*Lam',
                  order = {'NP':1})

GC_873 = Coupling(name = 'GC_873',
                  value = 'complex(0,1)*I13a2122*Lam',
                  order = {'NP':1})

GC_874 = Coupling(name = 'GC_874',
                  value = 'complex(0,1)*I13a2123*Lam',
                  order = {'NP':1})

GC_875 = Coupling(name = 'GC_875',
                  value = 'complex(0,1)*I13a2131*Lam',
                  order = {'NP':1})

GC_876 = Coupling(name = 'GC_876',
                  value = 'complex(0,1)*I13a2132*Lam',
                  order = {'NP':1})

GC_877 = Coupling(name = 'GC_877',
                  value = 'complex(0,1)*I13a2133*Lam',
                  order = {'NP':1})

GC_878 = Coupling(name = 'GC_878',
                  value = 'complex(0,1)*I13a2211*Lam',
                  order = {'NP':1})

GC_879 = Coupling(name = 'GC_879',
                  value = 'complex(0,1)*I13a2212*Lam',
                  order = {'NP':1})

GC_880 = Coupling(name = 'GC_880',
                  value = 'complex(0,1)*I13a2213*Lam',
                  order = {'NP':1})

GC_881 = Coupling(name = 'GC_881',
                  value = 'complex(0,1)*I13a2221*Lam',
                  order = {'NP':1})

GC_882 = Coupling(name = 'GC_882',
                  value = 'complex(0,1)*I13a2222*Lam',
                  order = {'NP':1})

GC_883 = Coupling(name = 'GC_883',
                  value = 'complex(0,1)*I13a2223*Lam',
                  order = {'NP':1})

GC_884 = Coupling(name = 'GC_884',
                  value = 'complex(0,1)*I13a2231*Lam',
                  order = {'NP':1})

GC_885 = Coupling(name = 'GC_885',
                  value = 'complex(0,1)*I13a2232*Lam',
                  order = {'NP':1})

GC_886 = Coupling(name = 'GC_886',
                  value = 'complex(0,1)*I13a2233*Lam',
                  order = {'NP':1})

GC_887 = Coupling(name = 'GC_887',
                  value = 'complex(0,1)*I13a2311*Lam',
                  order = {'NP':1})

GC_888 = Coupling(name = 'GC_888',
                  value = 'complex(0,1)*I13a2312*Lam',
                  order = {'NP':1})

GC_889 = Coupling(name = 'GC_889',
                  value = 'complex(0,1)*I13a2313*Lam',
                  order = {'NP':1})

GC_890 = Coupling(name = 'GC_890',
                  value = 'complex(0,1)*I13a2321*Lam',
                  order = {'NP':1})

GC_891 = Coupling(name = 'GC_891',
                  value = 'complex(0,1)*I13a2322*Lam',
                  order = {'NP':1})

GC_892 = Coupling(name = 'GC_892',
                  value = 'complex(0,1)*I13a2323*Lam',
                  order = {'NP':1})

GC_893 = Coupling(name = 'GC_893',
                  value = 'complex(0,1)*I13a2331*Lam',
                  order = {'NP':1})

GC_894 = Coupling(name = 'GC_894',
                  value = 'complex(0,1)*I13a2332*Lam',
                  order = {'NP':1})

GC_895 = Coupling(name = 'GC_895',
                  value = 'complex(0,1)*I13a2333*Lam',
                  order = {'NP':1})

GC_896 = Coupling(name = 'GC_896',
                  value = 'complex(0,1)*I13a3111*Lam',
                  order = {'NP':1})

GC_897 = Coupling(name = 'GC_897',
                  value = 'complex(0,1)*I13a3112*Lam',
                  order = {'NP':1})

GC_898 = Coupling(name = 'GC_898',
                  value = 'complex(0,1)*I13a3113*Lam',
                  order = {'NP':1})

GC_899 = Coupling(name = 'GC_899',
                  value = 'complex(0,1)*I13a3121*Lam',
                  order = {'NP':1})

GC_900 = Coupling(name = 'GC_900',
                  value = 'complex(0,1)*I13a3122*Lam',
                  order = {'NP':1})

GC_901 = Coupling(name = 'GC_901',
                  value = 'complex(0,1)*I13a3123*Lam',
                  order = {'NP':1})

GC_902 = Coupling(name = 'GC_902',
                  value = 'complex(0,1)*I13a3131*Lam',
                  order = {'NP':1})

GC_903 = Coupling(name = 'GC_903',
                  value = 'complex(0,1)*I13a3132*Lam',
                  order = {'NP':1})

GC_904 = Coupling(name = 'GC_904',
                  value = 'complex(0,1)*I13a3133*Lam',
                  order = {'NP':1})

GC_905 = Coupling(name = 'GC_905',
                  value = 'complex(0,1)*I13a3211*Lam',
                  order = {'NP':1})

GC_906 = Coupling(name = 'GC_906',
                  value = 'complex(0,1)*I13a3212*Lam',
                  order = {'NP':1})

GC_907 = Coupling(name = 'GC_907',
                  value = 'complex(0,1)*I13a3213*Lam',
                  order = {'NP':1})

GC_908 = Coupling(name = 'GC_908',
                  value = 'complex(0,1)*I13a3221*Lam',
                  order = {'NP':1})

GC_909 = Coupling(name = 'GC_909',
                  value = 'complex(0,1)*I13a3222*Lam',
                  order = {'NP':1})

GC_910 = Coupling(name = 'GC_910',
                  value = 'complex(0,1)*I13a3223*Lam',
                  order = {'NP':1})

GC_911 = Coupling(name = 'GC_911',
                  value = 'complex(0,1)*I13a3231*Lam',
                  order = {'NP':1})

GC_912 = Coupling(name = 'GC_912',
                  value = 'complex(0,1)*I13a3232*Lam',
                  order = {'NP':1})

GC_913 = Coupling(name = 'GC_913',
                  value = 'complex(0,1)*I13a3233*Lam',
                  order = {'NP':1})

GC_914 = Coupling(name = 'GC_914',
                  value = 'complex(0,1)*I13a3311*Lam',
                  order = {'NP':1})

GC_915 = Coupling(name = 'GC_915',
                  value = 'complex(0,1)*I13a3312*Lam',
                  order = {'NP':1})

GC_916 = Coupling(name = 'GC_916',
                  value = 'complex(0,1)*I13a3313*Lam',
                  order = {'NP':1})

GC_917 = Coupling(name = 'GC_917',
                  value = 'complex(0,1)*I13a3321*Lam',
                  order = {'NP':1})

GC_918 = Coupling(name = 'GC_918',
                  value = 'complex(0,1)*I13a3322*Lam',
                  order = {'NP':1})

GC_919 = Coupling(name = 'GC_919',
                  value = 'complex(0,1)*I13a3323*Lam',
                  order = {'NP':1})

GC_920 = Coupling(name = 'GC_920',
                  value = 'complex(0,1)*I13a3331*Lam',
                  order = {'NP':1})

GC_921 = Coupling(name = 'GC_921',
                  value = 'complex(0,1)*I13a3332*Lam',
                  order = {'NP':1})

GC_922 = Coupling(name = 'GC_922',
                  value = 'complex(0,1)*I13a3333*Lam',
                  order = {'NP':1})

GC_923 = Coupling(name = 'GC_923',
                  value = '2*complex(0,1)*I14a1111*Lam',
                  order = {'NP':1})

GC_924 = Coupling(name = 'GC_924',
                  value = '2*complex(0,1)*I14a1112*Lam',
                  order = {'NP':1})

GC_925 = Coupling(name = 'GC_925',
                  value = '2*complex(0,1)*I14a1113*Lam',
                  order = {'NP':1})

GC_926 = Coupling(name = 'GC_926',
                  value = '2*complex(0,1)*I14a1121*Lam',
                  order = {'NP':1})

GC_927 = Coupling(name = 'GC_927',
                  value = '2*complex(0,1)*I14a1122*Lam',
                  order = {'NP':1})

GC_928 = Coupling(name = 'GC_928',
                  value = '2*complex(0,1)*I14a1123*Lam',
                  order = {'NP':1})

GC_929 = Coupling(name = 'GC_929',
                  value = '2*complex(0,1)*I14a1131*Lam',
                  order = {'NP':1})

GC_930 = Coupling(name = 'GC_930',
                  value = '2*complex(0,1)*I14a1132*Lam',
                  order = {'NP':1})

GC_931 = Coupling(name = 'GC_931',
                  value = '2*complex(0,1)*I14a1133*Lam',
                  order = {'NP':1})

GC_932 = Coupling(name = 'GC_932',
                  value = '2*complex(0,1)*I14a1211*Lam',
                  order = {'NP':1})

GC_933 = Coupling(name = 'GC_933',
                  value = '2*complex(0,1)*I14a1212*Lam',
                  order = {'NP':1})

GC_934 = Coupling(name = 'GC_934',
                  value = '2*complex(0,1)*I14a1213*Lam',
                  order = {'NP':1})

GC_935 = Coupling(name = 'GC_935',
                  value = '2*complex(0,1)*I14a1221*Lam',
                  order = {'NP':1})

GC_936 = Coupling(name = 'GC_936',
                  value = '2*complex(0,1)*I14a1222*Lam',
                  order = {'NP':1})

GC_937 = Coupling(name = 'GC_937',
                  value = '2*complex(0,1)*I14a1223*Lam',
                  order = {'NP':1})

GC_938 = Coupling(name = 'GC_938',
                  value = '2*complex(0,1)*I14a1231*Lam',
                  order = {'NP':1})

GC_939 = Coupling(name = 'GC_939',
                  value = '2*complex(0,1)*I14a1232*Lam',
                  order = {'NP':1})

GC_940 = Coupling(name = 'GC_940',
                  value = '2*complex(0,1)*I14a1233*Lam',
                  order = {'NP':1})

GC_941 = Coupling(name = 'GC_941',
                  value = '2*complex(0,1)*I14a1311*Lam',
                  order = {'NP':1})

GC_942 = Coupling(name = 'GC_942',
                  value = '2*complex(0,1)*I14a1312*Lam',
                  order = {'NP':1})

GC_943 = Coupling(name = 'GC_943',
                  value = '2*complex(0,1)*I14a1313*Lam',
                  order = {'NP':1})

GC_944 = Coupling(name = 'GC_944',
                  value = '2*complex(0,1)*I14a1321*Lam',
                  order = {'NP':1})

GC_945 = Coupling(name = 'GC_945',
                  value = '2*complex(0,1)*I14a1322*Lam',
                  order = {'NP':1})

GC_946 = Coupling(name = 'GC_946',
                  value = '2*complex(0,1)*I14a1323*Lam',
                  order = {'NP':1})

GC_947 = Coupling(name = 'GC_947',
                  value = '2*complex(0,1)*I14a1331*Lam',
                  order = {'NP':1})

GC_948 = Coupling(name = 'GC_948',
                  value = '2*complex(0,1)*I14a1332*Lam',
                  order = {'NP':1})

GC_949 = Coupling(name = 'GC_949',
                  value = '2*complex(0,1)*I14a1333*Lam',
                  order = {'NP':1})

GC_950 = Coupling(name = 'GC_950',
                  value = '2*complex(0,1)*I14a2111*Lam',
                  order = {'NP':1})

GC_951 = Coupling(name = 'GC_951',
                  value = '2*complex(0,1)*I14a2112*Lam',
                  order = {'NP':1})

GC_952 = Coupling(name = 'GC_952',
                  value = '2*complex(0,1)*I14a2113*Lam',
                  order = {'NP':1})

GC_953 = Coupling(name = 'GC_953',
                  value = '2*complex(0,1)*I14a2121*Lam',
                  order = {'NP':1})

GC_954 = Coupling(name = 'GC_954',
                  value = '2*complex(0,1)*I14a2122*Lam',
                  order = {'NP':1})

GC_955 = Coupling(name = 'GC_955',
                  value = '2*complex(0,1)*I14a2123*Lam',
                  order = {'NP':1})

GC_956 = Coupling(name = 'GC_956',
                  value = '2*complex(0,1)*I14a2131*Lam',
                  order = {'NP':1})

GC_957 = Coupling(name = 'GC_957',
                  value = '2*complex(0,1)*I14a2132*Lam',
                  order = {'NP':1})

GC_958 = Coupling(name = 'GC_958',
                  value = '2*complex(0,1)*I14a2133*Lam',
                  order = {'NP':1})

GC_959 = Coupling(name = 'GC_959',
                  value = '2*complex(0,1)*I14a2211*Lam',
                  order = {'NP':1})

GC_960 = Coupling(name = 'GC_960',
                  value = '2*complex(0,1)*I14a2212*Lam',
                  order = {'NP':1})

GC_961 = Coupling(name = 'GC_961',
                  value = '2*complex(0,1)*I14a2213*Lam',
                  order = {'NP':1})

GC_962 = Coupling(name = 'GC_962',
                  value = '2*complex(0,1)*I14a2221*Lam',
                  order = {'NP':1})

GC_963 = Coupling(name = 'GC_963',
                  value = '2*complex(0,1)*I14a2222*Lam',
                  order = {'NP':1})

GC_964 = Coupling(name = 'GC_964',
                  value = '2*complex(0,1)*I14a2223*Lam',
                  order = {'NP':1})

GC_965 = Coupling(name = 'GC_965',
                  value = '2*complex(0,1)*I14a2231*Lam',
                  order = {'NP':1})

GC_966 = Coupling(name = 'GC_966',
                  value = '2*complex(0,1)*I14a2232*Lam',
                  order = {'NP':1})

GC_967 = Coupling(name = 'GC_967',
                  value = '2*complex(0,1)*I14a2233*Lam',
                  order = {'NP':1})

GC_968 = Coupling(name = 'GC_968',
                  value = '2*complex(0,1)*I14a2311*Lam',
                  order = {'NP':1})

GC_969 = Coupling(name = 'GC_969',
                  value = '2*complex(0,1)*I14a2312*Lam',
                  order = {'NP':1})

GC_970 = Coupling(name = 'GC_970',
                  value = '2*complex(0,1)*I14a2313*Lam',
                  order = {'NP':1})

GC_971 = Coupling(name = 'GC_971',
                  value = '2*complex(0,1)*I14a2321*Lam',
                  order = {'NP':1})

GC_972 = Coupling(name = 'GC_972',
                  value = '2*complex(0,1)*I14a2322*Lam',
                  order = {'NP':1})

GC_973 = Coupling(name = 'GC_973',
                  value = '2*complex(0,1)*I14a2323*Lam',
                  order = {'NP':1})

GC_974 = Coupling(name = 'GC_974',
                  value = '2*complex(0,1)*I14a2331*Lam',
                  order = {'NP':1})

GC_975 = Coupling(name = 'GC_975',
                  value = '2*complex(0,1)*I14a2332*Lam',
                  order = {'NP':1})

GC_976 = Coupling(name = 'GC_976',
                  value = '2*complex(0,1)*I14a2333*Lam',
                  order = {'NP':1})

GC_977 = Coupling(name = 'GC_977',
                  value = '2*complex(0,1)*I14a3111*Lam',
                  order = {'NP':1})

GC_978 = Coupling(name = 'GC_978',
                  value = '2*complex(0,1)*I14a3112*Lam',
                  order = {'NP':1})

GC_979 = Coupling(name = 'GC_979',
                  value = '2*complex(0,1)*I14a3113*Lam',
                  order = {'NP':1})

GC_980 = Coupling(name = 'GC_980',
                  value = '2*complex(0,1)*I14a3121*Lam',
                  order = {'NP':1})

GC_981 = Coupling(name = 'GC_981',
                  value = '2*complex(0,1)*I14a3122*Lam',
                  order = {'NP':1})

GC_982 = Coupling(name = 'GC_982',
                  value = '2*complex(0,1)*I14a3123*Lam',
                  order = {'NP':1})

GC_983 = Coupling(name = 'GC_983',
                  value = '2*complex(0,1)*I14a3131*Lam',
                  order = {'NP':1})

GC_984 = Coupling(name = 'GC_984',
                  value = '2*complex(0,1)*I14a3132*Lam',
                  order = {'NP':1})

GC_985 = Coupling(name = 'GC_985',
                  value = '2*complex(0,1)*I14a3133*Lam',
                  order = {'NP':1})

GC_986 = Coupling(name = 'GC_986',
                  value = '2*complex(0,1)*I14a3211*Lam',
                  order = {'NP':1})

GC_987 = Coupling(name = 'GC_987',
                  value = '2*complex(0,1)*I14a3212*Lam',
                  order = {'NP':1})

GC_988 = Coupling(name = 'GC_988',
                  value = '2*complex(0,1)*I14a3213*Lam',
                  order = {'NP':1})

GC_989 = Coupling(name = 'GC_989',
                  value = '2*complex(0,1)*I14a3221*Lam',
                  order = {'NP':1})

GC_990 = Coupling(name = 'GC_990',
                  value = '2*complex(0,1)*I14a3222*Lam',
                  order = {'NP':1})

GC_991 = Coupling(name = 'GC_991',
                  value = '2*complex(0,1)*I14a3223*Lam',
                  order = {'NP':1})

GC_992 = Coupling(name = 'GC_992',
                  value = '2*complex(0,1)*I14a3231*Lam',
                  order = {'NP':1})

GC_993 = Coupling(name = 'GC_993',
                  value = '2*complex(0,1)*I14a3232*Lam',
                  order = {'NP':1})

GC_994 = Coupling(name = 'GC_994',
                  value = '2*complex(0,1)*I14a3233*Lam',
                  order = {'NP':1})

GC_995 = Coupling(name = 'GC_995',
                  value = '2*complex(0,1)*I14a3311*Lam',
                  order = {'NP':1})

GC_996 = Coupling(name = 'GC_996',
                  value = '2*complex(0,1)*I14a3312*Lam',
                  order = {'NP':1})

GC_997 = Coupling(name = 'GC_997',
                  value = '2*complex(0,1)*I14a3313*Lam',
                  order = {'NP':1})

GC_998 = Coupling(name = 'GC_998',
                  value = '2*complex(0,1)*I14a3321*Lam',
                  order = {'NP':1})

GC_999 = Coupling(name = 'GC_999',
                  value = '2*complex(0,1)*I14a3322*Lam',
                  order = {'NP':1})

GC_1000 = Coupling(name = 'GC_1000',
                   value = '2*complex(0,1)*I14a3323*Lam',
                   order = {'NP':1})

GC_1001 = Coupling(name = 'GC_1001',
                   value = '2*complex(0,1)*I14a3331*Lam',
                   order = {'NP':1})

GC_1002 = Coupling(name = 'GC_1002',
                   value = '2*complex(0,1)*I14a3332*Lam',
                   order = {'NP':1})

GC_1003 = Coupling(name = 'GC_1003',
                   value = '2*complex(0,1)*I14a3333*Lam',
                   order = {'NP':1})

GC_1004 = Coupling(name = 'GC_1004',
                   value = '(complex(0,1)*I15a1111*Lam)/4.',
                   order = {'NP':1})

GC_1005 = Coupling(name = 'GC_1005',
                   value = '-(complex(0,1)*I15a1111*Lam)/2.',
                   order = {'NP':1})

GC_1006 = Coupling(name = 'GC_1006',
                   value = '(complex(0,1)*I15a1112*Lam)/4.',
                   order = {'NP':1})

GC_1007 = Coupling(name = 'GC_1007',
                   value = '-(complex(0,1)*I15a1112*Lam)/2.',
                   order = {'NP':1})

GC_1008 = Coupling(name = 'GC_1008',
                   value = '(complex(0,1)*I15a1113*Lam)/4.',
                   order = {'NP':1})

GC_1009 = Coupling(name = 'GC_1009',
                   value = '-(complex(0,1)*I15a1113*Lam)/2.',
                   order = {'NP':1})

GC_1010 = Coupling(name = 'GC_1010',
                   value = '(complex(0,1)*I15a1121*Lam)/4.',
                   order = {'NP':1})

GC_1011 = Coupling(name = 'GC_1011',
                   value = '-(complex(0,1)*I15a1121*Lam)/2.',
                   order = {'NP':1})

GC_1012 = Coupling(name = 'GC_1012',
                   value = '(complex(0,1)*I15a1122*Lam)/4.',
                   order = {'NP':1})

GC_1013 = Coupling(name = 'GC_1013',
                   value = '-(complex(0,1)*I15a1122*Lam)/2.',
                   order = {'NP':1})

GC_1014 = Coupling(name = 'GC_1014',
                   value = '(complex(0,1)*I15a1123*Lam)/4.',
                   order = {'NP':1})

GC_1015 = Coupling(name = 'GC_1015',
                   value = '-(complex(0,1)*I15a1123*Lam)/2.',
                   order = {'NP':1})

GC_1016 = Coupling(name = 'GC_1016',
                   value = '(complex(0,1)*I15a1131*Lam)/4.',
                   order = {'NP':1})

GC_1017 = Coupling(name = 'GC_1017',
                   value = '-(complex(0,1)*I15a1131*Lam)/2.',
                   order = {'NP':1})

GC_1018 = Coupling(name = 'GC_1018',
                   value = '(complex(0,1)*I15a1132*Lam)/4.',
                   order = {'NP':1})

GC_1019 = Coupling(name = 'GC_1019',
                   value = '-(complex(0,1)*I15a1132*Lam)/2.',
                   order = {'NP':1})

GC_1020 = Coupling(name = 'GC_1020',
                   value = '(complex(0,1)*I15a1133*Lam)/4.',
                   order = {'NP':1})

GC_1021 = Coupling(name = 'GC_1021',
                   value = '-(complex(0,1)*I15a1133*Lam)/2.',
                   order = {'NP':1})

GC_1022 = Coupling(name = 'GC_1022',
                   value = '(complex(0,1)*I15a1211*Lam)/4.',
                   order = {'NP':1})

GC_1023 = Coupling(name = 'GC_1023',
                   value = '-(complex(0,1)*I15a1211*Lam)/2.',
                   order = {'NP':1})

GC_1024 = Coupling(name = 'GC_1024',
                   value = '(complex(0,1)*I15a1212*Lam)/4.',
                   order = {'NP':1})

GC_1025 = Coupling(name = 'GC_1025',
                   value = '-(complex(0,1)*I15a1212*Lam)/2.',
                   order = {'NP':1})

GC_1026 = Coupling(name = 'GC_1026',
                   value = '(complex(0,1)*I15a1213*Lam)/4.',
                   order = {'NP':1})

GC_1027 = Coupling(name = 'GC_1027',
                   value = '-(complex(0,1)*I15a1213*Lam)/2.',
                   order = {'NP':1})

GC_1028 = Coupling(name = 'GC_1028',
                   value = '(complex(0,1)*I15a1221*Lam)/4.',
                   order = {'NP':1})

GC_1029 = Coupling(name = 'GC_1029',
                   value = '-(complex(0,1)*I15a1221*Lam)/2.',
                   order = {'NP':1})

GC_1030 = Coupling(name = 'GC_1030',
                   value = '(complex(0,1)*I15a1222*Lam)/4.',
                   order = {'NP':1})

GC_1031 = Coupling(name = 'GC_1031',
                   value = '-(complex(0,1)*I15a1222*Lam)/2.',
                   order = {'NP':1})

GC_1032 = Coupling(name = 'GC_1032',
                   value = '(complex(0,1)*I15a1223*Lam)/4.',
                   order = {'NP':1})

GC_1033 = Coupling(name = 'GC_1033',
                   value = '-(complex(0,1)*I15a1223*Lam)/2.',
                   order = {'NP':1})

GC_1034 = Coupling(name = 'GC_1034',
                   value = '(complex(0,1)*I15a1231*Lam)/4.',
                   order = {'NP':1})

GC_1035 = Coupling(name = 'GC_1035',
                   value = '-(complex(0,1)*I15a1231*Lam)/2.',
                   order = {'NP':1})

GC_1036 = Coupling(name = 'GC_1036',
                   value = '(complex(0,1)*I15a1232*Lam)/4.',
                   order = {'NP':1})

GC_1037 = Coupling(name = 'GC_1037',
                   value = '-(complex(0,1)*I15a1232*Lam)/2.',
                   order = {'NP':1})

GC_1038 = Coupling(name = 'GC_1038',
                   value = '(complex(0,1)*I15a1233*Lam)/4.',
                   order = {'NP':1})

GC_1039 = Coupling(name = 'GC_1039',
                   value = '-(complex(0,1)*I15a1233*Lam)/2.',
                   order = {'NP':1})

GC_1040 = Coupling(name = 'GC_1040',
                   value = '(complex(0,1)*I15a1311*Lam)/4.',
                   order = {'NP':1})

GC_1041 = Coupling(name = 'GC_1041',
                   value = '-(complex(0,1)*I15a1311*Lam)/2.',
                   order = {'NP':1})

GC_1042 = Coupling(name = 'GC_1042',
                   value = '(complex(0,1)*I15a1312*Lam)/4.',
                   order = {'NP':1})

GC_1043 = Coupling(name = 'GC_1043',
                   value = '-(complex(0,1)*I15a1312*Lam)/2.',
                   order = {'NP':1})

GC_1044 = Coupling(name = 'GC_1044',
                   value = '(complex(0,1)*I15a1313*Lam)/4.',
                   order = {'NP':1})

GC_1045 = Coupling(name = 'GC_1045',
                   value = '-(complex(0,1)*I15a1313*Lam)/2.',
                   order = {'NP':1})

GC_1046 = Coupling(name = 'GC_1046',
                   value = '(complex(0,1)*I15a1321*Lam)/4.',
                   order = {'NP':1})

GC_1047 = Coupling(name = 'GC_1047',
                   value = '-(complex(0,1)*I15a1321*Lam)/2.',
                   order = {'NP':1})

GC_1048 = Coupling(name = 'GC_1048',
                   value = '(complex(0,1)*I15a1322*Lam)/4.',
                   order = {'NP':1})

GC_1049 = Coupling(name = 'GC_1049',
                   value = '-(complex(0,1)*I15a1322*Lam)/2.',
                   order = {'NP':1})

GC_1050 = Coupling(name = 'GC_1050',
                   value = '(complex(0,1)*I15a1323*Lam)/4.',
                   order = {'NP':1})

GC_1051 = Coupling(name = 'GC_1051',
                   value = '-(complex(0,1)*I15a1323*Lam)/2.',
                   order = {'NP':1})

GC_1052 = Coupling(name = 'GC_1052',
                   value = '(complex(0,1)*I15a1331*Lam)/4.',
                   order = {'NP':1})

GC_1053 = Coupling(name = 'GC_1053',
                   value = '-(complex(0,1)*I15a1331*Lam)/2.',
                   order = {'NP':1})

GC_1054 = Coupling(name = 'GC_1054',
                   value = '(complex(0,1)*I15a1332*Lam)/4.',
                   order = {'NP':1})

GC_1055 = Coupling(name = 'GC_1055',
                   value = '-(complex(0,1)*I15a1332*Lam)/2.',
                   order = {'NP':1})

GC_1056 = Coupling(name = 'GC_1056',
                   value = '(complex(0,1)*I15a1333*Lam)/4.',
                   order = {'NP':1})

GC_1057 = Coupling(name = 'GC_1057',
                   value = '-(complex(0,1)*I15a1333*Lam)/2.',
                   order = {'NP':1})

GC_1058 = Coupling(name = 'GC_1058',
                   value = '(complex(0,1)*I15a2111*Lam)/4.',
                   order = {'NP':1})

GC_1059 = Coupling(name = 'GC_1059',
                   value = '-(complex(0,1)*I15a2111*Lam)/2.',
                   order = {'NP':1})

GC_1060 = Coupling(name = 'GC_1060',
                   value = '(complex(0,1)*I15a2112*Lam)/4.',
                   order = {'NP':1})

GC_1061 = Coupling(name = 'GC_1061',
                   value = '-(complex(0,1)*I15a2112*Lam)/2.',
                   order = {'NP':1})

GC_1062 = Coupling(name = 'GC_1062',
                   value = '(complex(0,1)*I15a2113*Lam)/4.',
                   order = {'NP':1})

GC_1063 = Coupling(name = 'GC_1063',
                   value = '-(complex(0,1)*I15a2113*Lam)/2.',
                   order = {'NP':1})

GC_1064 = Coupling(name = 'GC_1064',
                   value = '(complex(0,1)*I15a2121*Lam)/4.',
                   order = {'NP':1})

GC_1065 = Coupling(name = 'GC_1065',
                   value = '-(complex(0,1)*I15a2121*Lam)/2.',
                   order = {'NP':1})

GC_1066 = Coupling(name = 'GC_1066',
                   value = '(complex(0,1)*I15a2122*Lam)/4.',
                   order = {'NP':1})

GC_1067 = Coupling(name = 'GC_1067',
                   value = '-(complex(0,1)*I15a2122*Lam)/2.',
                   order = {'NP':1})

GC_1068 = Coupling(name = 'GC_1068',
                   value = '(complex(0,1)*I15a2123*Lam)/4.',
                   order = {'NP':1})

GC_1069 = Coupling(name = 'GC_1069',
                   value = '-(complex(0,1)*I15a2123*Lam)/2.',
                   order = {'NP':1})

GC_1070 = Coupling(name = 'GC_1070',
                   value = '(complex(0,1)*I15a2131*Lam)/4.',
                   order = {'NP':1})

GC_1071 = Coupling(name = 'GC_1071',
                   value = '-(complex(0,1)*I15a2131*Lam)/2.',
                   order = {'NP':1})

GC_1072 = Coupling(name = 'GC_1072',
                   value = '(complex(0,1)*I15a2132*Lam)/4.',
                   order = {'NP':1})

GC_1073 = Coupling(name = 'GC_1073',
                   value = '-(complex(0,1)*I15a2132*Lam)/2.',
                   order = {'NP':1})

GC_1074 = Coupling(name = 'GC_1074',
                   value = '(complex(0,1)*I15a2133*Lam)/4.',
                   order = {'NP':1})

GC_1075 = Coupling(name = 'GC_1075',
                   value = '-(complex(0,1)*I15a2133*Lam)/2.',
                   order = {'NP':1})

GC_1076 = Coupling(name = 'GC_1076',
                   value = '(complex(0,1)*I15a2211*Lam)/4.',
                   order = {'NP':1})

GC_1077 = Coupling(name = 'GC_1077',
                   value = '-(complex(0,1)*I15a2211*Lam)/2.',
                   order = {'NP':1})

GC_1078 = Coupling(name = 'GC_1078',
                   value = '(complex(0,1)*I15a2212*Lam)/4.',
                   order = {'NP':1})

GC_1079 = Coupling(name = 'GC_1079',
                   value = '-(complex(0,1)*I15a2212*Lam)/2.',
                   order = {'NP':1})

GC_1080 = Coupling(name = 'GC_1080',
                   value = '(complex(0,1)*I15a2213*Lam)/4.',
                   order = {'NP':1})

GC_1081 = Coupling(name = 'GC_1081',
                   value = '-(complex(0,1)*I15a2213*Lam)/2.',
                   order = {'NP':1})

GC_1082 = Coupling(name = 'GC_1082',
                   value = '(complex(0,1)*I15a2221*Lam)/4.',
                   order = {'NP':1})

GC_1083 = Coupling(name = 'GC_1083',
                   value = '-(complex(0,1)*I15a2221*Lam)/2.',
                   order = {'NP':1})

GC_1084 = Coupling(name = 'GC_1084',
                   value = '(complex(0,1)*I15a2222*Lam)/4.',
                   order = {'NP':1})

GC_1085 = Coupling(name = 'GC_1085',
                   value = '-(complex(0,1)*I15a2222*Lam)/2.',
                   order = {'NP':1})

GC_1086 = Coupling(name = 'GC_1086',
                   value = '(complex(0,1)*I15a2223*Lam)/4.',
                   order = {'NP':1})

GC_1087 = Coupling(name = 'GC_1087',
                   value = '-(complex(0,1)*I15a2223*Lam)/2.',
                   order = {'NP':1})

GC_1088 = Coupling(name = 'GC_1088',
                   value = '(complex(0,1)*I15a2231*Lam)/4.',
                   order = {'NP':1})

GC_1089 = Coupling(name = 'GC_1089',
                   value = '-(complex(0,1)*I15a2231*Lam)/2.',
                   order = {'NP':1})

GC_1090 = Coupling(name = 'GC_1090',
                   value = '(complex(0,1)*I15a2232*Lam)/4.',
                   order = {'NP':1})

GC_1091 = Coupling(name = 'GC_1091',
                   value = '-(complex(0,1)*I15a2232*Lam)/2.',
                   order = {'NP':1})

GC_1092 = Coupling(name = 'GC_1092',
                   value = '(complex(0,1)*I15a2233*Lam)/4.',
                   order = {'NP':1})

GC_1093 = Coupling(name = 'GC_1093',
                   value = '-(complex(0,1)*I15a2233*Lam)/2.',
                   order = {'NP':1})

GC_1094 = Coupling(name = 'GC_1094',
                   value = '(complex(0,1)*I15a2311*Lam)/4.',
                   order = {'NP':1})

GC_1095 = Coupling(name = 'GC_1095',
                   value = '-(complex(0,1)*I15a2311*Lam)/2.',
                   order = {'NP':1})

GC_1096 = Coupling(name = 'GC_1096',
                   value = '(complex(0,1)*I15a2312*Lam)/4.',
                   order = {'NP':1})

GC_1097 = Coupling(name = 'GC_1097',
                   value = '-(complex(0,1)*I15a2312*Lam)/2.',
                   order = {'NP':1})

GC_1098 = Coupling(name = 'GC_1098',
                   value = '(complex(0,1)*I15a2313*Lam)/4.',
                   order = {'NP':1})

GC_1099 = Coupling(name = 'GC_1099',
                   value = '-(complex(0,1)*I15a2313*Lam)/2.',
                   order = {'NP':1})

GC_1100 = Coupling(name = 'GC_1100',
                   value = '(complex(0,1)*I15a2321*Lam)/4.',
                   order = {'NP':1})

GC_1101 = Coupling(name = 'GC_1101',
                   value = '-(complex(0,1)*I15a2321*Lam)/2.',
                   order = {'NP':1})

GC_1102 = Coupling(name = 'GC_1102',
                   value = '(complex(0,1)*I15a2322*Lam)/4.',
                   order = {'NP':1})

GC_1103 = Coupling(name = 'GC_1103',
                   value = '-(complex(0,1)*I15a2322*Lam)/2.',
                   order = {'NP':1})

GC_1104 = Coupling(name = 'GC_1104',
                   value = '(complex(0,1)*I15a2323*Lam)/4.',
                   order = {'NP':1})

GC_1105 = Coupling(name = 'GC_1105',
                   value = '-(complex(0,1)*I15a2323*Lam)/2.',
                   order = {'NP':1})

GC_1106 = Coupling(name = 'GC_1106',
                   value = '(complex(0,1)*I15a2331*Lam)/4.',
                   order = {'NP':1})

GC_1107 = Coupling(name = 'GC_1107',
                   value = '-(complex(0,1)*I15a2331*Lam)/2.',
                   order = {'NP':1})

GC_1108 = Coupling(name = 'GC_1108',
                   value = '(complex(0,1)*I15a2332*Lam)/4.',
                   order = {'NP':1})

GC_1109 = Coupling(name = 'GC_1109',
                   value = '-(complex(0,1)*I15a2332*Lam)/2.',
                   order = {'NP':1})

GC_1110 = Coupling(name = 'GC_1110',
                   value = '(complex(0,1)*I15a2333*Lam)/4.',
                   order = {'NP':1})

GC_1111 = Coupling(name = 'GC_1111',
                   value = '-(complex(0,1)*I15a2333*Lam)/2.',
                   order = {'NP':1})

GC_1112 = Coupling(name = 'GC_1112',
                   value = '(complex(0,1)*I15a3111*Lam)/4.',
                   order = {'NP':1})

GC_1113 = Coupling(name = 'GC_1113',
                   value = '-(complex(0,1)*I15a3111*Lam)/2.',
                   order = {'NP':1})

GC_1114 = Coupling(name = 'GC_1114',
                   value = '(complex(0,1)*I15a3112*Lam)/4.',
                   order = {'NP':1})

GC_1115 = Coupling(name = 'GC_1115',
                   value = '-(complex(0,1)*I15a3112*Lam)/2.',
                   order = {'NP':1})

GC_1116 = Coupling(name = 'GC_1116',
                   value = '(complex(0,1)*I15a3113*Lam)/4.',
                   order = {'NP':1})

GC_1117 = Coupling(name = 'GC_1117',
                   value = '-(complex(0,1)*I15a3113*Lam)/2.',
                   order = {'NP':1})

GC_1118 = Coupling(name = 'GC_1118',
                   value = '(complex(0,1)*I15a3121*Lam)/4.',
                   order = {'NP':1})

GC_1119 = Coupling(name = 'GC_1119',
                   value = '-(complex(0,1)*I15a3121*Lam)/2.',
                   order = {'NP':1})

GC_1120 = Coupling(name = 'GC_1120',
                   value = '(complex(0,1)*I15a3122*Lam)/4.',
                   order = {'NP':1})

GC_1121 = Coupling(name = 'GC_1121',
                   value = '-(complex(0,1)*I15a3122*Lam)/2.',
                   order = {'NP':1})

GC_1122 = Coupling(name = 'GC_1122',
                   value = '(complex(0,1)*I15a3123*Lam)/4.',
                   order = {'NP':1})

GC_1123 = Coupling(name = 'GC_1123',
                   value = '-(complex(0,1)*I15a3123*Lam)/2.',
                   order = {'NP':1})

GC_1124 = Coupling(name = 'GC_1124',
                   value = '(complex(0,1)*I15a3131*Lam)/4.',
                   order = {'NP':1})

GC_1125 = Coupling(name = 'GC_1125',
                   value = '-(complex(0,1)*I15a3131*Lam)/2.',
                   order = {'NP':1})

GC_1126 = Coupling(name = 'GC_1126',
                   value = '(complex(0,1)*I15a3132*Lam)/4.',
                   order = {'NP':1})

GC_1127 = Coupling(name = 'GC_1127',
                   value = '-(complex(0,1)*I15a3132*Lam)/2.',
                   order = {'NP':1})

GC_1128 = Coupling(name = 'GC_1128',
                   value = '(complex(0,1)*I15a3133*Lam)/4.',
                   order = {'NP':1})

GC_1129 = Coupling(name = 'GC_1129',
                   value = '-(complex(0,1)*I15a3133*Lam)/2.',
                   order = {'NP':1})

GC_1130 = Coupling(name = 'GC_1130',
                   value = '(complex(0,1)*I15a3211*Lam)/4.',
                   order = {'NP':1})

GC_1131 = Coupling(name = 'GC_1131',
                   value = '-(complex(0,1)*I15a3211*Lam)/2.',
                   order = {'NP':1})

GC_1132 = Coupling(name = 'GC_1132',
                   value = '(complex(0,1)*I15a3212*Lam)/4.',
                   order = {'NP':1})

GC_1133 = Coupling(name = 'GC_1133',
                   value = '-(complex(0,1)*I15a3212*Lam)/2.',
                   order = {'NP':1})

GC_1134 = Coupling(name = 'GC_1134',
                   value = '(complex(0,1)*I15a3213*Lam)/4.',
                   order = {'NP':1})

GC_1135 = Coupling(name = 'GC_1135',
                   value = '-(complex(0,1)*I15a3213*Lam)/2.',
                   order = {'NP':1})

GC_1136 = Coupling(name = 'GC_1136',
                   value = '(complex(0,1)*I15a3221*Lam)/4.',
                   order = {'NP':1})

GC_1137 = Coupling(name = 'GC_1137',
                   value = '-(complex(0,1)*I15a3221*Lam)/2.',
                   order = {'NP':1})

GC_1138 = Coupling(name = 'GC_1138',
                   value = '(complex(0,1)*I15a3222*Lam)/4.',
                   order = {'NP':1})

GC_1139 = Coupling(name = 'GC_1139',
                   value = '-(complex(0,1)*I15a3222*Lam)/2.',
                   order = {'NP':1})

GC_1140 = Coupling(name = 'GC_1140',
                   value = '(complex(0,1)*I15a3223*Lam)/4.',
                   order = {'NP':1})

GC_1141 = Coupling(name = 'GC_1141',
                   value = '-(complex(0,1)*I15a3223*Lam)/2.',
                   order = {'NP':1})

GC_1142 = Coupling(name = 'GC_1142',
                   value = '(complex(0,1)*I15a3231*Lam)/4.',
                   order = {'NP':1})

GC_1143 = Coupling(name = 'GC_1143',
                   value = '-(complex(0,1)*I15a3231*Lam)/2.',
                   order = {'NP':1})

GC_1144 = Coupling(name = 'GC_1144',
                   value = '(complex(0,1)*I15a3232*Lam)/4.',
                   order = {'NP':1})

GC_1145 = Coupling(name = 'GC_1145',
                   value = '-(complex(0,1)*I15a3232*Lam)/2.',
                   order = {'NP':1})

GC_1146 = Coupling(name = 'GC_1146',
                   value = '(complex(0,1)*I15a3233*Lam)/4.',
                   order = {'NP':1})

GC_1147 = Coupling(name = 'GC_1147',
                   value = '-(complex(0,1)*I15a3233*Lam)/2.',
                   order = {'NP':1})

GC_1148 = Coupling(name = 'GC_1148',
                   value = '(complex(0,1)*I15a3311*Lam)/4.',
                   order = {'NP':1})

GC_1149 = Coupling(name = 'GC_1149',
                   value = '-(complex(0,1)*I15a3311*Lam)/2.',
                   order = {'NP':1})

GC_1150 = Coupling(name = 'GC_1150',
                   value = '(complex(0,1)*I15a3312*Lam)/4.',
                   order = {'NP':1})

GC_1151 = Coupling(name = 'GC_1151',
                   value = '-(complex(0,1)*I15a3312*Lam)/2.',
                   order = {'NP':1})

GC_1152 = Coupling(name = 'GC_1152',
                   value = '(complex(0,1)*I15a3313*Lam)/4.',
                   order = {'NP':1})

GC_1153 = Coupling(name = 'GC_1153',
                   value = '-(complex(0,1)*I15a3313*Lam)/2.',
                   order = {'NP':1})

GC_1154 = Coupling(name = 'GC_1154',
                   value = '(complex(0,1)*I15a3321*Lam)/4.',
                   order = {'NP':1})

GC_1155 = Coupling(name = 'GC_1155',
                   value = '-(complex(0,1)*I15a3321*Lam)/2.',
                   order = {'NP':1})

GC_1156 = Coupling(name = 'GC_1156',
                   value = '(complex(0,1)*I15a3322*Lam)/4.',
                   order = {'NP':1})

GC_1157 = Coupling(name = 'GC_1157',
                   value = '-(complex(0,1)*I15a3322*Lam)/2.',
                   order = {'NP':1})

GC_1158 = Coupling(name = 'GC_1158',
                   value = '(complex(0,1)*I15a3323*Lam)/4.',
                   order = {'NP':1})

GC_1159 = Coupling(name = 'GC_1159',
                   value = '-(complex(0,1)*I15a3323*Lam)/2.',
                   order = {'NP':1})

GC_1160 = Coupling(name = 'GC_1160',
                   value = '(complex(0,1)*I15a3331*Lam)/4.',
                   order = {'NP':1})

GC_1161 = Coupling(name = 'GC_1161',
                   value = '-(complex(0,1)*I15a3331*Lam)/2.',
                   order = {'NP':1})

GC_1162 = Coupling(name = 'GC_1162',
                   value = '(complex(0,1)*I15a3332*Lam)/4.',
                   order = {'NP':1})

GC_1163 = Coupling(name = 'GC_1163',
                   value = '-(complex(0,1)*I15a3332*Lam)/2.',
                   order = {'NP':1})

GC_1164 = Coupling(name = 'GC_1164',
                   value = '(complex(0,1)*I15a3333*Lam)/4.',
                   order = {'NP':1})

GC_1165 = Coupling(name = 'GC_1165',
                   value = '-(complex(0,1)*I15a3333*Lam)/2.',
                   order = {'NP':1})

GC_1166 = Coupling(name = 'GC_1166',
                   value = 'complex(0,1)*I18a1111*Lam',
                   order = {'NP':1})

GC_1167 = Coupling(name = 'GC_1167',
                   value = 'complex(0,1)*I18a1112*Lam',
                   order = {'NP':1})

GC_1168 = Coupling(name = 'GC_1168',
                   value = 'complex(0,1)*I18a1113*Lam',
                   order = {'NP':1})

GC_1169 = Coupling(name = 'GC_1169',
                   value = 'complex(0,1)*I18a1121*Lam',
                   order = {'NP':1})

GC_1170 = Coupling(name = 'GC_1170',
                   value = 'complex(0,1)*I18a1122*Lam',
                   order = {'NP':1})

GC_1171 = Coupling(name = 'GC_1171',
                   value = 'complex(0,1)*I18a1123*Lam',
                   order = {'NP':1})

GC_1172 = Coupling(name = 'GC_1172',
                   value = 'complex(0,1)*I18a1131*Lam',
                   order = {'NP':1})

GC_1173 = Coupling(name = 'GC_1173',
                   value = 'complex(0,1)*I18a1132*Lam',
                   order = {'NP':1})

GC_1174 = Coupling(name = 'GC_1174',
                   value = 'complex(0,1)*I18a1133*Lam',
                   order = {'NP':1})

GC_1175 = Coupling(name = 'GC_1175',
                   value = 'complex(0,1)*I18a1211*Lam',
                   order = {'NP':1})

GC_1176 = Coupling(name = 'GC_1176',
                   value = 'complex(0,1)*I18a1212*Lam',
                   order = {'NP':1})

GC_1177 = Coupling(name = 'GC_1177',
                   value = 'complex(0,1)*I18a1213*Lam',
                   order = {'NP':1})

GC_1178 = Coupling(name = 'GC_1178',
                   value = 'complex(0,1)*I18a1221*Lam',
                   order = {'NP':1})

GC_1179 = Coupling(name = 'GC_1179',
                   value = 'complex(0,1)*I18a1222*Lam',
                   order = {'NP':1})

GC_1180 = Coupling(name = 'GC_1180',
                   value = 'complex(0,1)*I18a1223*Lam',
                   order = {'NP':1})

GC_1181 = Coupling(name = 'GC_1181',
                   value = 'complex(0,1)*I18a1231*Lam',
                   order = {'NP':1})

GC_1182 = Coupling(name = 'GC_1182',
                   value = 'complex(0,1)*I18a1232*Lam',
                   order = {'NP':1})

GC_1183 = Coupling(name = 'GC_1183',
                   value = 'complex(0,1)*I18a1233*Lam',
                   order = {'NP':1})

GC_1184 = Coupling(name = 'GC_1184',
                   value = 'complex(0,1)*I18a1311*Lam',
                   order = {'NP':1})

GC_1185 = Coupling(name = 'GC_1185',
                   value = 'complex(0,1)*I18a1312*Lam',
                   order = {'NP':1})

GC_1186 = Coupling(name = 'GC_1186',
                   value = 'complex(0,1)*I18a1313*Lam',
                   order = {'NP':1})

GC_1187 = Coupling(name = 'GC_1187',
                   value = 'complex(0,1)*I18a1321*Lam',
                   order = {'NP':1})

GC_1188 = Coupling(name = 'GC_1188',
                   value = 'complex(0,1)*I18a1322*Lam',
                   order = {'NP':1})

GC_1189 = Coupling(name = 'GC_1189',
                   value = 'complex(0,1)*I18a1323*Lam',
                   order = {'NP':1})

GC_1190 = Coupling(name = 'GC_1190',
                   value = 'complex(0,1)*I18a1331*Lam',
                   order = {'NP':1})

GC_1191 = Coupling(name = 'GC_1191',
                   value = 'complex(0,1)*I18a1332*Lam',
                   order = {'NP':1})

GC_1192 = Coupling(name = 'GC_1192',
                   value = 'complex(0,1)*I18a1333*Lam',
                   order = {'NP':1})

GC_1193 = Coupling(name = 'GC_1193',
                   value = 'complex(0,1)*I18a2111*Lam',
                   order = {'NP':1})

GC_1194 = Coupling(name = 'GC_1194',
                   value = 'complex(0,1)*I18a2112*Lam',
                   order = {'NP':1})

GC_1195 = Coupling(name = 'GC_1195',
                   value = 'complex(0,1)*I18a2113*Lam',
                   order = {'NP':1})

GC_1196 = Coupling(name = 'GC_1196',
                   value = 'complex(0,1)*I18a2121*Lam',
                   order = {'NP':1})

GC_1197 = Coupling(name = 'GC_1197',
                   value = 'complex(0,1)*I18a2122*Lam',
                   order = {'NP':1})

GC_1198 = Coupling(name = 'GC_1198',
                   value = 'complex(0,1)*I18a2123*Lam',
                   order = {'NP':1})

GC_1199 = Coupling(name = 'GC_1199',
                   value = 'complex(0,1)*I18a2131*Lam',
                   order = {'NP':1})

GC_1200 = Coupling(name = 'GC_1200',
                   value = 'complex(0,1)*I18a2132*Lam',
                   order = {'NP':1})

GC_1201 = Coupling(name = 'GC_1201',
                   value = 'complex(0,1)*I18a2133*Lam',
                   order = {'NP':1})

GC_1202 = Coupling(name = 'GC_1202',
                   value = 'complex(0,1)*I18a2211*Lam',
                   order = {'NP':1})

GC_1203 = Coupling(name = 'GC_1203',
                   value = 'complex(0,1)*I18a2212*Lam',
                   order = {'NP':1})

GC_1204 = Coupling(name = 'GC_1204',
                   value = 'complex(0,1)*I18a2213*Lam',
                   order = {'NP':1})

GC_1205 = Coupling(name = 'GC_1205',
                   value = 'complex(0,1)*I18a2221*Lam',
                   order = {'NP':1})

GC_1206 = Coupling(name = 'GC_1206',
                   value = 'complex(0,1)*I18a2222*Lam',
                   order = {'NP':1})

GC_1207 = Coupling(name = 'GC_1207',
                   value = 'complex(0,1)*I18a2223*Lam',
                   order = {'NP':1})

GC_1208 = Coupling(name = 'GC_1208',
                   value = 'complex(0,1)*I18a2231*Lam',
                   order = {'NP':1})

GC_1209 = Coupling(name = 'GC_1209',
                   value = 'complex(0,1)*I18a2232*Lam',
                   order = {'NP':1})

GC_1210 = Coupling(name = 'GC_1210',
                   value = 'complex(0,1)*I18a2233*Lam',
                   order = {'NP':1})

GC_1211 = Coupling(name = 'GC_1211',
                   value = 'complex(0,1)*I18a2311*Lam',
                   order = {'NP':1})

GC_1212 = Coupling(name = 'GC_1212',
                   value = 'complex(0,1)*I18a2312*Lam',
                   order = {'NP':1})

GC_1213 = Coupling(name = 'GC_1213',
                   value = 'complex(0,1)*I18a2313*Lam',
                   order = {'NP':1})

GC_1214 = Coupling(name = 'GC_1214',
                   value = 'complex(0,1)*I18a2321*Lam',
                   order = {'NP':1})

GC_1215 = Coupling(name = 'GC_1215',
                   value = 'complex(0,1)*I18a2322*Lam',
                   order = {'NP':1})

GC_1216 = Coupling(name = 'GC_1216',
                   value = 'complex(0,1)*I18a2323*Lam',
                   order = {'NP':1})

GC_1217 = Coupling(name = 'GC_1217',
                   value = 'complex(0,1)*I18a2331*Lam',
                   order = {'NP':1})

GC_1218 = Coupling(name = 'GC_1218',
                   value = 'complex(0,1)*I18a2332*Lam',
                   order = {'NP':1})

GC_1219 = Coupling(name = 'GC_1219',
                   value = 'complex(0,1)*I18a2333*Lam',
                   order = {'NP':1})

GC_1220 = Coupling(name = 'GC_1220',
                   value = 'complex(0,1)*I18a3111*Lam',
                   order = {'NP':1})

GC_1221 = Coupling(name = 'GC_1221',
                   value = 'complex(0,1)*I18a3112*Lam',
                   order = {'NP':1})

GC_1222 = Coupling(name = 'GC_1222',
                   value = 'complex(0,1)*I18a3113*Lam',
                   order = {'NP':1})

GC_1223 = Coupling(name = 'GC_1223',
                   value = 'complex(0,1)*I18a3121*Lam',
                   order = {'NP':1})

GC_1224 = Coupling(name = 'GC_1224',
                   value = 'complex(0,1)*I18a3122*Lam',
                   order = {'NP':1})

GC_1225 = Coupling(name = 'GC_1225',
                   value = 'complex(0,1)*I18a3123*Lam',
                   order = {'NP':1})

GC_1226 = Coupling(name = 'GC_1226',
                   value = 'complex(0,1)*I18a3131*Lam',
                   order = {'NP':1})

GC_1227 = Coupling(name = 'GC_1227',
                   value = 'complex(0,1)*I18a3132*Lam',
                   order = {'NP':1})

GC_1228 = Coupling(name = 'GC_1228',
                   value = 'complex(0,1)*I18a3133*Lam',
                   order = {'NP':1})

GC_1229 = Coupling(name = 'GC_1229',
                   value = 'complex(0,1)*I18a3211*Lam',
                   order = {'NP':1})

GC_1230 = Coupling(name = 'GC_1230',
                   value = 'complex(0,1)*I18a3212*Lam',
                   order = {'NP':1})

GC_1231 = Coupling(name = 'GC_1231',
                   value = 'complex(0,1)*I18a3213*Lam',
                   order = {'NP':1})

GC_1232 = Coupling(name = 'GC_1232',
                   value = 'complex(0,1)*I18a3221*Lam',
                   order = {'NP':1})

GC_1233 = Coupling(name = 'GC_1233',
                   value = 'complex(0,1)*I18a3222*Lam',
                   order = {'NP':1})

GC_1234 = Coupling(name = 'GC_1234',
                   value = 'complex(0,1)*I18a3223*Lam',
                   order = {'NP':1})

GC_1235 = Coupling(name = 'GC_1235',
                   value = 'complex(0,1)*I18a3231*Lam',
                   order = {'NP':1})

GC_1236 = Coupling(name = 'GC_1236',
                   value = 'complex(0,1)*I18a3232*Lam',
                   order = {'NP':1})

GC_1237 = Coupling(name = 'GC_1237',
                   value = 'complex(0,1)*I18a3233*Lam',
                   order = {'NP':1})

GC_1238 = Coupling(name = 'GC_1238',
                   value = 'complex(0,1)*I18a3311*Lam',
                   order = {'NP':1})

GC_1239 = Coupling(name = 'GC_1239',
                   value = 'complex(0,1)*I18a3312*Lam',
                   order = {'NP':1})

GC_1240 = Coupling(name = 'GC_1240',
                   value = 'complex(0,1)*I18a3313*Lam',
                   order = {'NP':1})

GC_1241 = Coupling(name = 'GC_1241',
                   value = 'complex(0,1)*I18a3321*Lam',
                   order = {'NP':1})

GC_1242 = Coupling(name = 'GC_1242',
                   value = 'complex(0,1)*I18a3322*Lam',
                   order = {'NP':1})

GC_1243 = Coupling(name = 'GC_1243',
                   value = 'complex(0,1)*I18a3323*Lam',
                   order = {'NP':1})

GC_1244 = Coupling(name = 'GC_1244',
                   value = 'complex(0,1)*I18a3331*Lam',
                   order = {'NP':1})

GC_1245 = Coupling(name = 'GC_1245',
                   value = 'complex(0,1)*I18a3332*Lam',
                   order = {'NP':1})

GC_1246 = Coupling(name = 'GC_1246',
                   value = 'complex(0,1)*I18a3333*Lam',
                   order = {'NP':1})

GC_1247 = Coupling(name = 'GC_1247',
                   value = '-(complex(0,1)*I1a1111*Lam)',
                   order = {'NP':1})

GC_1248 = Coupling(name = 'GC_1248',
                   value = '-(complex(0,1)*I1a1112*Lam)',
                   order = {'NP':1})

GC_1249 = Coupling(name = 'GC_1249',
                   value = '-(complex(0,1)*I1a1113*Lam)',
                   order = {'NP':1})

GC_1250 = Coupling(name = 'GC_1250',
                   value = '-(complex(0,1)*I1a1121*Lam)',
                   order = {'NP':1})

GC_1251 = Coupling(name = 'GC_1251',
                   value = '-(complex(0,1)*I1a1122*Lam)',
                   order = {'NP':1})

GC_1252 = Coupling(name = 'GC_1252',
                   value = '-(complex(0,1)*I1a1123*Lam)',
                   order = {'NP':1})

GC_1253 = Coupling(name = 'GC_1253',
                   value = '-(complex(0,1)*I1a1131*Lam)',
                   order = {'NP':1})

GC_1254 = Coupling(name = 'GC_1254',
                   value = '-(complex(0,1)*I1a1132*Lam)',
                   order = {'NP':1})

GC_1255 = Coupling(name = 'GC_1255',
                   value = '-(complex(0,1)*I1a1133*Lam)',
                   order = {'NP':1})

GC_1256 = Coupling(name = 'GC_1256',
                   value = '-(complex(0,1)*I1a1211*Lam)',
                   order = {'NP':1})

GC_1257 = Coupling(name = 'GC_1257',
                   value = '-(complex(0,1)*I1a1212*Lam)',
                   order = {'NP':1})

GC_1258 = Coupling(name = 'GC_1258',
                   value = '-(complex(0,1)*I1a1213*Lam)',
                   order = {'NP':1})

GC_1259 = Coupling(name = 'GC_1259',
                   value = '-(complex(0,1)*I1a1221*Lam)',
                   order = {'NP':1})

GC_1260 = Coupling(name = 'GC_1260',
                   value = '-(complex(0,1)*I1a1222*Lam)',
                   order = {'NP':1})

GC_1261 = Coupling(name = 'GC_1261',
                   value = '-(complex(0,1)*I1a1223*Lam)',
                   order = {'NP':1})

GC_1262 = Coupling(name = 'GC_1262',
                   value = '-(complex(0,1)*I1a1231*Lam)',
                   order = {'NP':1})

GC_1263 = Coupling(name = 'GC_1263',
                   value = '-(complex(0,1)*I1a1232*Lam)',
                   order = {'NP':1})

GC_1264 = Coupling(name = 'GC_1264',
                   value = '-(complex(0,1)*I1a1233*Lam)',
                   order = {'NP':1})

GC_1265 = Coupling(name = 'GC_1265',
                   value = '-(complex(0,1)*I1a1311*Lam)',
                   order = {'NP':1})

GC_1266 = Coupling(name = 'GC_1266',
                   value = '-(complex(0,1)*I1a1312*Lam)',
                   order = {'NP':1})

GC_1267 = Coupling(name = 'GC_1267',
                   value = '-(complex(0,1)*I1a1313*Lam)',
                   order = {'NP':1})

GC_1268 = Coupling(name = 'GC_1268',
                   value = '-(complex(0,1)*I1a1321*Lam)',
                   order = {'NP':1})

GC_1269 = Coupling(name = 'GC_1269',
                   value = '-(complex(0,1)*I1a1322*Lam)',
                   order = {'NP':1})

GC_1270 = Coupling(name = 'GC_1270',
                   value = '-(complex(0,1)*I1a1323*Lam)',
                   order = {'NP':1})

GC_1271 = Coupling(name = 'GC_1271',
                   value = '-(complex(0,1)*I1a1331*Lam)',
                   order = {'NP':1})

GC_1272 = Coupling(name = 'GC_1272',
                   value = '-(complex(0,1)*I1a1332*Lam)',
                   order = {'NP':1})

GC_1273 = Coupling(name = 'GC_1273',
                   value = '-(complex(0,1)*I1a1333*Lam)',
                   order = {'NP':1})

GC_1274 = Coupling(name = 'GC_1274',
                   value = '-(complex(0,1)*I1a2111*Lam)',
                   order = {'NP':1})

GC_1275 = Coupling(name = 'GC_1275',
                   value = '-(complex(0,1)*I1a2112*Lam)',
                   order = {'NP':1})

GC_1276 = Coupling(name = 'GC_1276',
                   value = '-(complex(0,1)*I1a2113*Lam)',
                   order = {'NP':1})

GC_1277 = Coupling(name = 'GC_1277',
                   value = '-(complex(0,1)*I1a2121*Lam)',
                   order = {'NP':1})

GC_1278 = Coupling(name = 'GC_1278',
                   value = '-(complex(0,1)*I1a2122*Lam)',
                   order = {'NP':1})

GC_1279 = Coupling(name = 'GC_1279',
                   value = '-(complex(0,1)*I1a2123*Lam)',
                   order = {'NP':1})

GC_1280 = Coupling(name = 'GC_1280',
                   value = '-(complex(0,1)*I1a2131*Lam)',
                   order = {'NP':1})

GC_1281 = Coupling(name = 'GC_1281',
                   value = '-(complex(0,1)*I1a2132*Lam)',
                   order = {'NP':1})

GC_1282 = Coupling(name = 'GC_1282',
                   value = '-(complex(0,1)*I1a2133*Lam)',
                   order = {'NP':1})

GC_1283 = Coupling(name = 'GC_1283',
                   value = '-(complex(0,1)*I1a2211*Lam)',
                   order = {'NP':1})

GC_1284 = Coupling(name = 'GC_1284',
                   value = '-(complex(0,1)*I1a2212*Lam)',
                   order = {'NP':1})

GC_1285 = Coupling(name = 'GC_1285',
                   value = '-(complex(0,1)*I1a2213*Lam)',
                   order = {'NP':1})

GC_1286 = Coupling(name = 'GC_1286',
                   value = '-(complex(0,1)*I1a2221*Lam)',
                   order = {'NP':1})

GC_1287 = Coupling(name = 'GC_1287',
                   value = '-(complex(0,1)*I1a2222*Lam)',
                   order = {'NP':1})

GC_1288 = Coupling(name = 'GC_1288',
                   value = '-(complex(0,1)*I1a2223*Lam)',
                   order = {'NP':1})

GC_1289 = Coupling(name = 'GC_1289',
                   value = '-(complex(0,1)*I1a2231*Lam)',
                   order = {'NP':1})

GC_1290 = Coupling(name = 'GC_1290',
                   value = '-(complex(0,1)*I1a2232*Lam)',
                   order = {'NP':1})

GC_1291 = Coupling(name = 'GC_1291',
                   value = '-(complex(0,1)*I1a2233*Lam)',
                   order = {'NP':1})

GC_1292 = Coupling(name = 'GC_1292',
                   value = '-(complex(0,1)*I1a2311*Lam)',
                   order = {'NP':1})

GC_1293 = Coupling(name = 'GC_1293',
                   value = '-(complex(0,1)*I1a2312*Lam)',
                   order = {'NP':1})

GC_1294 = Coupling(name = 'GC_1294',
                   value = '-(complex(0,1)*I1a2313*Lam)',
                   order = {'NP':1})

GC_1295 = Coupling(name = 'GC_1295',
                   value = '-(complex(0,1)*I1a2321*Lam)',
                   order = {'NP':1})

GC_1296 = Coupling(name = 'GC_1296',
                   value = '-(complex(0,1)*I1a2322*Lam)',
                   order = {'NP':1})

GC_1297 = Coupling(name = 'GC_1297',
                   value = '-(complex(0,1)*I1a2323*Lam)',
                   order = {'NP':1})

GC_1298 = Coupling(name = 'GC_1298',
                   value = '-(complex(0,1)*I1a2331*Lam)',
                   order = {'NP':1})

GC_1299 = Coupling(name = 'GC_1299',
                   value = '-(complex(0,1)*I1a2332*Lam)',
                   order = {'NP':1})

GC_1300 = Coupling(name = 'GC_1300',
                   value = '-(complex(0,1)*I1a2333*Lam)',
                   order = {'NP':1})

GC_1301 = Coupling(name = 'GC_1301',
                   value = '-(complex(0,1)*I1a3111*Lam)',
                   order = {'NP':1})

GC_1302 = Coupling(name = 'GC_1302',
                   value = '-(complex(0,1)*I1a3112*Lam)',
                   order = {'NP':1})

GC_1303 = Coupling(name = 'GC_1303',
                   value = '-(complex(0,1)*I1a3113*Lam)',
                   order = {'NP':1})

GC_1304 = Coupling(name = 'GC_1304',
                   value = '-(complex(0,1)*I1a3121*Lam)',
                   order = {'NP':1})

GC_1305 = Coupling(name = 'GC_1305',
                   value = '-(complex(0,1)*I1a3122*Lam)',
                   order = {'NP':1})

GC_1306 = Coupling(name = 'GC_1306',
                   value = '-(complex(0,1)*I1a3123*Lam)',
                   order = {'NP':1})

GC_1307 = Coupling(name = 'GC_1307',
                   value = '-(complex(0,1)*I1a3131*Lam)',
                   order = {'NP':1})

GC_1308 = Coupling(name = 'GC_1308',
                   value = '-(complex(0,1)*I1a3132*Lam)',
                   order = {'NP':1})

GC_1309 = Coupling(name = 'GC_1309',
                   value = '-(complex(0,1)*I1a3133*Lam)',
                   order = {'NP':1})

GC_1310 = Coupling(name = 'GC_1310',
                   value = '-(complex(0,1)*I1a3211*Lam)',
                   order = {'NP':1})

GC_1311 = Coupling(name = 'GC_1311',
                   value = '-(complex(0,1)*I1a3212*Lam)',
                   order = {'NP':1})

GC_1312 = Coupling(name = 'GC_1312',
                   value = '-(complex(0,1)*I1a3213*Lam)',
                   order = {'NP':1})

GC_1313 = Coupling(name = 'GC_1313',
                   value = '-(complex(0,1)*I1a3221*Lam)',
                   order = {'NP':1})

GC_1314 = Coupling(name = 'GC_1314',
                   value = '-(complex(0,1)*I1a3222*Lam)',
                   order = {'NP':1})

GC_1315 = Coupling(name = 'GC_1315',
                   value = '-(complex(0,1)*I1a3223*Lam)',
                   order = {'NP':1})

GC_1316 = Coupling(name = 'GC_1316',
                   value = '-(complex(0,1)*I1a3231*Lam)',
                   order = {'NP':1})

GC_1317 = Coupling(name = 'GC_1317',
                   value = '-(complex(0,1)*I1a3232*Lam)',
                   order = {'NP':1})

GC_1318 = Coupling(name = 'GC_1318',
                   value = '-(complex(0,1)*I1a3233*Lam)',
                   order = {'NP':1})

GC_1319 = Coupling(name = 'GC_1319',
                   value = '-(complex(0,1)*I1a3311*Lam)',
                   order = {'NP':1})

GC_1320 = Coupling(name = 'GC_1320',
                   value = '-(complex(0,1)*I1a3312*Lam)',
                   order = {'NP':1})

GC_1321 = Coupling(name = 'GC_1321',
                   value = '-(complex(0,1)*I1a3313*Lam)',
                   order = {'NP':1})

GC_1322 = Coupling(name = 'GC_1322',
                   value = '-(complex(0,1)*I1a3321*Lam)',
                   order = {'NP':1})

GC_1323 = Coupling(name = 'GC_1323',
                   value = '-(complex(0,1)*I1a3322*Lam)',
                   order = {'NP':1})

GC_1324 = Coupling(name = 'GC_1324',
                   value = '-(complex(0,1)*I1a3323*Lam)',
                   order = {'NP':1})

GC_1325 = Coupling(name = 'GC_1325',
                   value = '-(complex(0,1)*I1a3331*Lam)',
                   order = {'NP':1})

GC_1326 = Coupling(name = 'GC_1326',
                   value = '-(complex(0,1)*I1a3332*Lam)',
                   order = {'NP':1})

GC_1327 = Coupling(name = 'GC_1327',
                   value = '-(complex(0,1)*I1a3333*Lam)',
                   order = {'NP':1})

GC_1328 = Coupling(name = 'GC_1328',
                   value = 'complex(0,1)*I21a1111*Lam',
                   order = {'NP':1})

GC_1329 = Coupling(name = 'GC_1329',
                   value = 'complex(0,1)*I21a1112*Lam',
                   order = {'NP':1})

GC_1330 = Coupling(name = 'GC_1330',
                   value = 'complex(0,1)*I21a1113*Lam',
                   order = {'NP':1})

GC_1331 = Coupling(name = 'GC_1331',
                   value = 'complex(0,1)*I21a1121*Lam',
                   order = {'NP':1})

GC_1332 = Coupling(name = 'GC_1332',
                   value = 'complex(0,1)*I21a1122*Lam',
                   order = {'NP':1})

GC_1333 = Coupling(name = 'GC_1333',
                   value = 'complex(0,1)*I21a1123*Lam',
                   order = {'NP':1})

GC_1334 = Coupling(name = 'GC_1334',
                   value = 'complex(0,1)*I21a1131*Lam',
                   order = {'NP':1})

GC_1335 = Coupling(name = 'GC_1335',
                   value = 'complex(0,1)*I21a1132*Lam',
                   order = {'NP':1})

GC_1336 = Coupling(name = 'GC_1336',
                   value = 'complex(0,1)*I21a1133*Lam',
                   order = {'NP':1})

GC_1337 = Coupling(name = 'GC_1337',
                   value = 'complex(0,1)*I21a1211*Lam',
                   order = {'NP':1})

GC_1338 = Coupling(name = 'GC_1338',
                   value = 'complex(0,1)*I21a1212*Lam',
                   order = {'NP':1})

GC_1339 = Coupling(name = 'GC_1339',
                   value = 'complex(0,1)*I21a1213*Lam',
                   order = {'NP':1})

GC_1340 = Coupling(name = 'GC_1340',
                   value = 'complex(0,1)*I21a1221*Lam',
                   order = {'NP':1})

GC_1341 = Coupling(name = 'GC_1341',
                   value = 'complex(0,1)*I21a1222*Lam',
                   order = {'NP':1})

GC_1342 = Coupling(name = 'GC_1342',
                   value = 'complex(0,1)*I21a1223*Lam',
                   order = {'NP':1})

GC_1343 = Coupling(name = 'GC_1343',
                   value = 'complex(0,1)*I21a1231*Lam',
                   order = {'NP':1})

GC_1344 = Coupling(name = 'GC_1344',
                   value = 'complex(0,1)*I21a1232*Lam',
                   order = {'NP':1})

GC_1345 = Coupling(name = 'GC_1345',
                   value = 'complex(0,1)*I21a1233*Lam',
                   order = {'NP':1})

GC_1346 = Coupling(name = 'GC_1346',
                   value = 'complex(0,1)*I21a1311*Lam',
                   order = {'NP':1})

GC_1347 = Coupling(name = 'GC_1347',
                   value = 'complex(0,1)*I21a1312*Lam',
                   order = {'NP':1})

GC_1348 = Coupling(name = 'GC_1348',
                   value = 'complex(0,1)*I21a1313*Lam',
                   order = {'NP':1})

GC_1349 = Coupling(name = 'GC_1349',
                   value = 'complex(0,1)*I21a1321*Lam',
                   order = {'NP':1})

GC_1350 = Coupling(name = 'GC_1350',
                   value = 'complex(0,1)*I21a1322*Lam',
                   order = {'NP':1})

GC_1351 = Coupling(name = 'GC_1351',
                   value = 'complex(0,1)*I21a1323*Lam',
                   order = {'NP':1})

GC_1352 = Coupling(name = 'GC_1352',
                   value = 'complex(0,1)*I21a1331*Lam',
                   order = {'NP':1})

GC_1353 = Coupling(name = 'GC_1353',
                   value = 'complex(0,1)*I21a1332*Lam',
                   order = {'NP':1})

GC_1354 = Coupling(name = 'GC_1354',
                   value = 'complex(0,1)*I21a1333*Lam',
                   order = {'NP':1})

GC_1355 = Coupling(name = 'GC_1355',
                   value = 'complex(0,1)*I21a2111*Lam',
                   order = {'NP':1})

GC_1356 = Coupling(name = 'GC_1356',
                   value = 'complex(0,1)*I21a2112*Lam',
                   order = {'NP':1})

GC_1357 = Coupling(name = 'GC_1357',
                   value = 'complex(0,1)*I21a2113*Lam',
                   order = {'NP':1})

GC_1358 = Coupling(name = 'GC_1358',
                   value = 'complex(0,1)*I21a2121*Lam',
                   order = {'NP':1})

GC_1359 = Coupling(name = 'GC_1359',
                   value = 'complex(0,1)*I21a2122*Lam',
                   order = {'NP':1})

GC_1360 = Coupling(name = 'GC_1360',
                   value = 'complex(0,1)*I21a2123*Lam',
                   order = {'NP':1})

GC_1361 = Coupling(name = 'GC_1361',
                   value = 'complex(0,1)*I21a2131*Lam',
                   order = {'NP':1})

GC_1362 = Coupling(name = 'GC_1362',
                   value = 'complex(0,1)*I21a2132*Lam',
                   order = {'NP':1})

GC_1363 = Coupling(name = 'GC_1363',
                   value = 'complex(0,1)*I21a2133*Lam',
                   order = {'NP':1})

GC_1364 = Coupling(name = 'GC_1364',
                   value = 'complex(0,1)*I21a2211*Lam',
                   order = {'NP':1})

GC_1365 = Coupling(name = 'GC_1365',
                   value = 'complex(0,1)*I21a2212*Lam',
                   order = {'NP':1})

GC_1366 = Coupling(name = 'GC_1366',
                   value = 'complex(0,1)*I21a2213*Lam',
                   order = {'NP':1})

GC_1367 = Coupling(name = 'GC_1367',
                   value = 'complex(0,1)*I21a2221*Lam',
                   order = {'NP':1})

GC_1368 = Coupling(name = 'GC_1368',
                   value = 'complex(0,1)*I21a2222*Lam',
                   order = {'NP':1})

GC_1369 = Coupling(name = 'GC_1369',
                   value = 'complex(0,1)*I21a2223*Lam',
                   order = {'NP':1})

GC_1370 = Coupling(name = 'GC_1370',
                   value = 'complex(0,1)*I21a2231*Lam',
                   order = {'NP':1})

GC_1371 = Coupling(name = 'GC_1371',
                   value = 'complex(0,1)*I21a2232*Lam',
                   order = {'NP':1})

GC_1372 = Coupling(name = 'GC_1372',
                   value = 'complex(0,1)*I21a2233*Lam',
                   order = {'NP':1})

GC_1373 = Coupling(name = 'GC_1373',
                   value = 'complex(0,1)*I21a2311*Lam',
                   order = {'NP':1})

GC_1374 = Coupling(name = 'GC_1374',
                   value = 'complex(0,1)*I21a2312*Lam',
                   order = {'NP':1})

GC_1375 = Coupling(name = 'GC_1375',
                   value = 'complex(0,1)*I21a2313*Lam',
                   order = {'NP':1})

GC_1376 = Coupling(name = 'GC_1376',
                   value = 'complex(0,1)*I21a2321*Lam',
                   order = {'NP':1})

GC_1377 = Coupling(name = 'GC_1377',
                   value = 'complex(0,1)*I21a2322*Lam',
                   order = {'NP':1})

GC_1378 = Coupling(name = 'GC_1378',
                   value = 'complex(0,1)*I21a2323*Lam',
                   order = {'NP':1})

GC_1379 = Coupling(name = 'GC_1379',
                   value = 'complex(0,1)*I21a2331*Lam',
                   order = {'NP':1})

GC_1380 = Coupling(name = 'GC_1380',
                   value = 'complex(0,1)*I21a2332*Lam',
                   order = {'NP':1})

GC_1381 = Coupling(name = 'GC_1381',
                   value = 'complex(0,1)*I21a2333*Lam',
                   order = {'NP':1})

GC_1382 = Coupling(name = 'GC_1382',
                   value = 'complex(0,1)*I21a3111*Lam',
                   order = {'NP':1})

GC_1383 = Coupling(name = 'GC_1383',
                   value = 'complex(0,1)*I21a3112*Lam',
                   order = {'NP':1})

GC_1384 = Coupling(name = 'GC_1384',
                   value = 'complex(0,1)*I21a3113*Lam',
                   order = {'NP':1})

GC_1385 = Coupling(name = 'GC_1385',
                   value = 'complex(0,1)*I21a3121*Lam',
                   order = {'NP':1})

GC_1386 = Coupling(name = 'GC_1386',
                   value = 'complex(0,1)*I21a3122*Lam',
                   order = {'NP':1})

GC_1387 = Coupling(name = 'GC_1387',
                   value = 'complex(0,1)*I21a3123*Lam',
                   order = {'NP':1})

GC_1388 = Coupling(name = 'GC_1388',
                   value = 'complex(0,1)*I21a3131*Lam',
                   order = {'NP':1})

GC_1389 = Coupling(name = 'GC_1389',
                   value = 'complex(0,1)*I21a3132*Lam',
                   order = {'NP':1})

GC_1390 = Coupling(name = 'GC_1390',
                   value = 'complex(0,1)*I21a3133*Lam',
                   order = {'NP':1})

GC_1391 = Coupling(name = 'GC_1391',
                   value = 'complex(0,1)*I21a3211*Lam',
                   order = {'NP':1})

GC_1392 = Coupling(name = 'GC_1392',
                   value = 'complex(0,1)*I21a3212*Lam',
                   order = {'NP':1})

GC_1393 = Coupling(name = 'GC_1393',
                   value = 'complex(0,1)*I21a3213*Lam',
                   order = {'NP':1})

GC_1394 = Coupling(name = 'GC_1394',
                   value = 'complex(0,1)*I21a3221*Lam',
                   order = {'NP':1})

GC_1395 = Coupling(name = 'GC_1395',
                   value = 'complex(0,1)*I21a3222*Lam',
                   order = {'NP':1})

GC_1396 = Coupling(name = 'GC_1396',
                   value = 'complex(0,1)*I21a3223*Lam',
                   order = {'NP':1})

GC_1397 = Coupling(name = 'GC_1397',
                   value = 'complex(0,1)*I21a3231*Lam',
                   order = {'NP':1})

GC_1398 = Coupling(name = 'GC_1398',
                   value = 'complex(0,1)*I21a3232*Lam',
                   order = {'NP':1})

GC_1399 = Coupling(name = 'GC_1399',
                   value = 'complex(0,1)*I21a3233*Lam',
                   order = {'NP':1})

GC_1400 = Coupling(name = 'GC_1400',
                   value = 'complex(0,1)*I21a3311*Lam',
                   order = {'NP':1})

GC_1401 = Coupling(name = 'GC_1401',
                   value = 'complex(0,1)*I21a3312*Lam',
                   order = {'NP':1})

GC_1402 = Coupling(name = 'GC_1402',
                   value = 'complex(0,1)*I21a3313*Lam',
                   order = {'NP':1})

GC_1403 = Coupling(name = 'GC_1403',
                   value = 'complex(0,1)*I21a3321*Lam',
                   order = {'NP':1})

GC_1404 = Coupling(name = 'GC_1404',
                   value = 'complex(0,1)*I21a3322*Lam',
                   order = {'NP':1})

GC_1405 = Coupling(name = 'GC_1405',
                   value = 'complex(0,1)*I21a3323*Lam',
                   order = {'NP':1})

GC_1406 = Coupling(name = 'GC_1406',
                   value = 'complex(0,1)*I21a3331*Lam',
                   order = {'NP':1})

GC_1407 = Coupling(name = 'GC_1407',
                   value = 'complex(0,1)*I21a3332*Lam',
                   order = {'NP':1})

GC_1408 = Coupling(name = 'GC_1408',
                   value = 'complex(0,1)*I21a3333*Lam',
                   order = {'NP':1})

GC_1409 = Coupling(name = 'GC_1409',
                   value = '-(complex(0,1)*I2a1111*Lam)',
                   order = {'NP':1})

GC_1410 = Coupling(name = 'GC_1410',
                   value = '-(complex(0,1)*I2a1112*Lam)',
                   order = {'NP':1})

GC_1411 = Coupling(name = 'GC_1411',
                   value = '-(complex(0,1)*I2a1113*Lam)',
                   order = {'NP':1})

GC_1412 = Coupling(name = 'GC_1412',
                   value = '-(complex(0,1)*I2a1121*Lam)',
                   order = {'NP':1})

GC_1413 = Coupling(name = 'GC_1413',
                   value = '-(complex(0,1)*I2a1122*Lam)',
                   order = {'NP':1})

GC_1414 = Coupling(name = 'GC_1414',
                   value = '-(complex(0,1)*I2a1123*Lam)',
                   order = {'NP':1})

GC_1415 = Coupling(name = 'GC_1415',
                   value = '-(complex(0,1)*I2a1131*Lam)',
                   order = {'NP':1})

GC_1416 = Coupling(name = 'GC_1416',
                   value = '-(complex(0,1)*I2a1132*Lam)',
                   order = {'NP':1})

GC_1417 = Coupling(name = 'GC_1417',
                   value = '-(complex(0,1)*I2a1133*Lam)',
                   order = {'NP':1})

GC_1418 = Coupling(name = 'GC_1418',
                   value = '-(complex(0,1)*I2a1211*Lam)',
                   order = {'NP':1})

GC_1419 = Coupling(name = 'GC_1419',
                   value = '-(complex(0,1)*I2a1212*Lam)',
                   order = {'NP':1})

GC_1420 = Coupling(name = 'GC_1420',
                   value = '-(complex(0,1)*I2a1213*Lam)',
                   order = {'NP':1})

GC_1421 = Coupling(name = 'GC_1421',
                   value = '-(complex(0,1)*I2a1221*Lam)',
                   order = {'NP':1})

GC_1422 = Coupling(name = 'GC_1422',
                   value = '-(complex(0,1)*I2a1222*Lam)',
                   order = {'NP':1})

GC_1423 = Coupling(name = 'GC_1423',
                   value = '-(complex(0,1)*I2a1223*Lam)',
                   order = {'NP':1})

GC_1424 = Coupling(name = 'GC_1424',
                   value = '-(complex(0,1)*I2a1231*Lam)',
                   order = {'NP':1})

GC_1425 = Coupling(name = 'GC_1425',
                   value = '-(complex(0,1)*I2a1232*Lam)',
                   order = {'NP':1})

GC_1426 = Coupling(name = 'GC_1426',
                   value = '-(complex(0,1)*I2a1233*Lam)',
                   order = {'NP':1})

GC_1427 = Coupling(name = 'GC_1427',
                   value = '-(complex(0,1)*I2a1311*Lam)',
                   order = {'NP':1})

GC_1428 = Coupling(name = 'GC_1428',
                   value = '-(complex(0,1)*I2a1312*Lam)',
                   order = {'NP':1})

GC_1429 = Coupling(name = 'GC_1429',
                   value = '-(complex(0,1)*I2a1313*Lam)',
                   order = {'NP':1})

GC_1430 = Coupling(name = 'GC_1430',
                   value = '-(complex(0,1)*I2a1321*Lam)',
                   order = {'NP':1})

GC_1431 = Coupling(name = 'GC_1431',
                   value = '-(complex(0,1)*I2a1322*Lam)',
                   order = {'NP':1})

GC_1432 = Coupling(name = 'GC_1432',
                   value = '-(complex(0,1)*I2a1323*Lam)',
                   order = {'NP':1})

GC_1433 = Coupling(name = 'GC_1433',
                   value = '-(complex(0,1)*I2a1331*Lam)',
                   order = {'NP':1})

GC_1434 = Coupling(name = 'GC_1434',
                   value = '-(complex(0,1)*I2a1332*Lam)',
                   order = {'NP':1})

GC_1435 = Coupling(name = 'GC_1435',
                   value = '-(complex(0,1)*I2a1333*Lam)',
                   order = {'NP':1})

GC_1436 = Coupling(name = 'GC_1436',
                   value = '-(complex(0,1)*I2a2111*Lam)',
                   order = {'NP':1})

GC_1437 = Coupling(name = 'GC_1437',
                   value = '-(complex(0,1)*I2a2112*Lam)',
                   order = {'NP':1})

GC_1438 = Coupling(name = 'GC_1438',
                   value = '-(complex(0,1)*I2a2113*Lam)',
                   order = {'NP':1})

GC_1439 = Coupling(name = 'GC_1439',
                   value = '-(complex(0,1)*I2a2121*Lam)',
                   order = {'NP':1})

GC_1440 = Coupling(name = 'GC_1440',
                   value = '-(complex(0,1)*I2a2122*Lam)',
                   order = {'NP':1})

GC_1441 = Coupling(name = 'GC_1441',
                   value = '-(complex(0,1)*I2a2123*Lam)',
                   order = {'NP':1})

GC_1442 = Coupling(name = 'GC_1442',
                   value = '-(complex(0,1)*I2a2131*Lam)',
                   order = {'NP':1})

GC_1443 = Coupling(name = 'GC_1443',
                   value = '-(complex(0,1)*I2a2132*Lam)',
                   order = {'NP':1})

GC_1444 = Coupling(name = 'GC_1444',
                   value = '-(complex(0,1)*I2a2133*Lam)',
                   order = {'NP':1})

GC_1445 = Coupling(name = 'GC_1445',
                   value = '-(complex(0,1)*I2a2211*Lam)',
                   order = {'NP':1})

GC_1446 = Coupling(name = 'GC_1446',
                   value = '-(complex(0,1)*I2a2212*Lam)',
                   order = {'NP':1})

GC_1447 = Coupling(name = 'GC_1447',
                   value = '-(complex(0,1)*I2a2213*Lam)',
                   order = {'NP':1})

GC_1448 = Coupling(name = 'GC_1448',
                   value = '-(complex(0,1)*I2a2221*Lam)',
                   order = {'NP':1})

GC_1449 = Coupling(name = 'GC_1449',
                   value = '-(complex(0,1)*I2a2222*Lam)',
                   order = {'NP':1})

GC_1450 = Coupling(name = 'GC_1450',
                   value = '-(complex(0,1)*I2a2223*Lam)',
                   order = {'NP':1})

GC_1451 = Coupling(name = 'GC_1451',
                   value = '-(complex(0,1)*I2a2231*Lam)',
                   order = {'NP':1})

GC_1452 = Coupling(name = 'GC_1452',
                   value = '-(complex(0,1)*I2a2232*Lam)',
                   order = {'NP':1})

GC_1453 = Coupling(name = 'GC_1453',
                   value = '-(complex(0,1)*I2a2233*Lam)',
                   order = {'NP':1})

GC_1454 = Coupling(name = 'GC_1454',
                   value = '-(complex(0,1)*I2a2311*Lam)',
                   order = {'NP':1})

GC_1455 = Coupling(name = 'GC_1455',
                   value = '-(complex(0,1)*I2a2312*Lam)',
                   order = {'NP':1})

GC_1456 = Coupling(name = 'GC_1456',
                   value = '-(complex(0,1)*I2a2313*Lam)',
                   order = {'NP':1})

GC_1457 = Coupling(name = 'GC_1457',
                   value = '-(complex(0,1)*I2a2321*Lam)',
                   order = {'NP':1})

GC_1458 = Coupling(name = 'GC_1458',
                   value = '-(complex(0,1)*I2a2322*Lam)',
                   order = {'NP':1})

GC_1459 = Coupling(name = 'GC_1459',
                   value = '-(complex(0,1)*I2a2323*Lam)',
                   order = {'NP':1})

GC_1460 = Coupling(name = 'GC_1460',
                   value = '-(complex(0,1)*I2a2331*Lam)',
                   order = {'NP':1})

GC_1461 = Coupling(name = 'GC_1461',
                   value = '-(complex(0,1)*I2a2332*Lam)',
                   order = {'NP':1})

GC_1462 = Coupling(name = 'GC_1462',
                   value = '-(complex(0,1)*I2a2333*Lam)',
                   order = {'NP':1})

GC_1463 = Coupling(name = 'GC_1463',
                   value = '-(complex(0,1)*I2a3111*Lam)',
                   order = {'NP':1})

GC_1464 = Coupling(name = 'GC_1464',
                   value = '-(complex(0,1)*I2a3112*Lam)',
                   order = {'NP':1})

GC_1465 = Coupling(name = 'GC_1465',
                   value = '-(complex(0,1)*I2a3113*Lam)',
                   order = {'NP':1})

GC_1466 = Coupling(name = 'GC_1466',
                   value = '-(complex(0,1)*I2a3121*Lam)',
                   order = {'NP':1})

GC_1467 = Coupling(name = 'GC_1467',
                   value = '-(complex(0,1)*I2a3122*Lam)',
                   order = {'NP':1})

GC_1468 = Coupling(name = 'GC_1468',
                   value = '-(complex(0,1)*I2a3123*Lam)',
                   order = {'NP':1})

GC_1469 = Coupling(name = 'GC_1469',
                   value = '-(complex(0,1)*I2a3131*Lam)',
                   order = {'NP':1})

GC_1470 = Coupling(name = 'GC_1470',
                   value = '-(complex(0,1)*I2a3132*Lam)',
                   order = {'NP':1})

GC_1471 = Coupling(name = 'GC_1471',
                   value = '-(complex(0,1)*I2a3133*Lam)',
                   order = {'NP':1})

GC_1472 = Coupling(name = 'GC_1472',
                   value = '-(complex(0,1)*I2a3211*Lam)',
                   order = {'NP':1})

GC_1473 = Coupling(name = 'GC_1473',
                   value = '-(complex(0,1)*I2a3212*Lam)',
                   order = {'NP':1})

GC_1474 = Coupling(name = 'GC_1474',
                   value = '-(complex(0,1)*I2a3213*Lam)',
                   order = {'NP':1})

GC_1475 = Coupling(name = 'GC_1475',
                   value = '-(complex(0,1)*I2a3221*Lam)',
                   order = {'NP':1})

GC_1476 = Coupling(name = 'GC_1476',
                   value = '-(complex(0,1)*I2a3222*Lam)',
                   order = {'NP':1})

GC_1477 = Coupling(name = 'GC_1477',
                   value = '-(complex(0,1)*I2a3223*Lam)',
                   order = {'NP':1})

GC_1478 = Coupling(name = 'GC_1478',
                   value = '-(complex(0,1)*I2a3231*Lam)',
                   order = {'NP':1})

GC_1479 = Coupling(name = 'GC_1479',
                   value = '-(complex(0,1)*I2a3232*Lam)',
                   order = {'NP':1})

GC_1480 = Coupling(name = 'GC_1480',
                   value = '-(complex(0,1)*I2a3233*Lam)',
                   order = {'NP':1})

GC_1481 = Coupling(name = 'GC_1481',
                   value = '-(complex(0,1)*I2a3311*Lam)',
                   order = {'NP':1})

GC_1482 = Coupling(name = 'GC_1482',
                   value = '-(complex(0,1)*I2a3312*Lam)',
                   order = {'NP':1})

GC_1483 = Coupling(name = 'GC_1483',
                   value = '-(complex(0,1)*I2a3313*Lam)',
                   order = {'NP':1})

GC_1484 = Coupling(name = 'GC_1484',
                   value = '-(complex(0,1)*I2a3321*Lam)',
                   order = {'NP':1})

GC_1485 = Coupling(name = 'GC_1485',
                   value = '-(complex(0,1)*I2a3322*Lam)',
                   order = {'NP':1})

GC_1486 = Coupling(name = 'GC_1486',
                   value = '-(complex(0,1)*I2a3323*Lam)',
                   order = {'NP':1})

GC_1487 = Coupling(name = 'GC_1487',
                   value = '-(complex(0,1)*I2a3331*Lam)',
                   order = {'NP':1})

GC_1488 = Coupling(name = 'GC_1488',
                   value = '-(complex(0,1)*I2a3332*Lam)',
                   order = {'NP':1})

GC_1489 = Coupling(name = 'GC_1489',
                   value = '-(complex(0,1)*I2a3333*Lam)',
                   order = {'NP':1})

GC_1490 = Coupling(name = 'GC_1490',
                   value = 'complex(0,1)*I5a1111*Lam',
                   order = {'NP':1})

GC_1491 = Coupling(name = 'GC_1491',
                   value = 'complex(0,1)*I5a1112*Lam',
                   order = {'NP':1})

GC_1492 = Coupling(name = 'GC_1492',
                   value = 'complex(0,1)*I5a1113*Lam',
                   order = {'NP':1})

GC_1493 = Coupling(name = 'GC_1493',
                   value = 'complex(0,1)*I5a1121*Lam',
                   order = {'NP':1})

GC_1494 = Coupling(name = 'GC_1494',
                   value = 'complex(0,1)*I5a1122*Lam',
                   order = {'NP':1})

GC_1495 = Coupling(name = 'GC_1495',
                   value = 'complex(0,1)*I5a1123*Lam',
                   order = {'NP':1})

GC_1496 = Coupling(name = 'GC_1496',
                   value = 'complex(0,1)*I5a1131*Lam',
                   order = {'NP':1})

GC_1497 = Coupling(name = 'GC_1497',
                   value = 'complex(0,1)*I5a1132*Lam',
                   order = {'NP':1})

GC_1498 = Coupling(name = 'GC_1498',
                   value = 'complex(0,1)*I5a1133*Lam',
                   order = {'NP':1})

GC_1499 = Coupling(name = 'GC_1499',
                   value = 'complex(0,1)*I5a1211*Lam',
                   order = {'NP':1})

GC_1500 = Coupling(name = 'GC_1500',
                   value = 'complex(0,1)*I5a1212*Lam',
                   order = {'NP':1})

GC_1501 = Coupling(name = 'GC_1501',
                   value = 'complex(0,1)*I5a1213*Lam',
                   order = {'NP':1})

GC_1502 = Coupling(name = 'GC_1502',
                   value = 'complex(0,1)*I5a1221*Lam',
                   order = {'NP':1})

GC_1503 = Coupling(name = 'GC_1503',
                   value = 'complex(0,1)*I5a1222*Lam',
                   order = {'NP':1})

GC_1504 = Coupling(name = 'GC_1504',
                   value = 'complex(0,1)*I5a1223*Lam',
                   order = {'NP':1})

GC_1505 = Coupling(name = 'GC_1505',
                   value = 'complex(0,1)*I5a1231*Lam',
                   order = {'NP':1})

GC_1506 = Coupling(name = 'GC_1506',
                   value = 'complex(0,1)*I5a1232*Lam',
                   order = {'NP':1})

GC_1507 = Coupling(name = 'GC_1507',
                   value = 'complex(0,1)*I5a1233*Lam',
                   order = {'NP':1})

GC_1508 = Coupling(name = 'GC_1508',
                   value = 'complex(0,1)*I5a1311*Lam',
                   order = {'NP':1})

GC_1509 = Coupling(name = 'GC_1509',
                   value = 'complex(0,1)*I5a1312*Lam',
                   order = {'NP':1})

GC_1510 = Coupling(name = 'GC_1510',
                   value = 'complex(0,1)*I5a1313*Lam',
                   order = {'NP':1})

GC_1511 = Coupling(name = 'GC_1511',
                   value = 'complex(0,1)*I5a1321*Lam',
                   order = {'NP':1})

GC_1512 = Coupling(name = 'GC_1512',
                   value = 'complex(0,1)*I5a1322*Lam',
                   order = {'NP':1})

GC_1513 = Coupling(name = 'GC_1513',
                   value = 'complex(0,1)*I5a1323*Lam',
                   order = {'NP':1})

GC_1514 = Coupling(name = 'GC_1514',
                   value = 'complex(0,1)*I5a1331*Lam',
                   order = {'NP':1})

GC_1515 = Coupling(name = 'GC_1515',
                   value = 'complex(0,1)*I5a1332*Lam',
                   order = {'NP':1})

GC_1516 = Coupling(name = 'GC_1516',
                   value = 'complex(0,1)*I5a1333*Lam',
                   order = {'NP':1})

GC_1517 = Coupling(name = 'GC_1517',
                   value = 'complex(0,1)*I5a2111*Lam',
                   order = {'NP':1})

GC_1518 = Coupling(name = 'GC_1518',
                   value = 'complex(0,1)*I5a2112*Lam',
                   order = {'NP':1})

GC_1519 = Coupling(name = 'GC_1519',
                   value = 'complex(0,1)*I5a2113*Lam',
                   order = {'NP':1})

GC_1520 = Coupling(name = 'GC_1520',
                   value = 'complex(0,1)*I5a2121*Lam',
                   order = {'NP':1})

GC_1521 = Coupling(name = 'GC_1521',
                   value = 'complex(0,1)*I5a2122*Lam',
                   order = {'NP':1})

GC_1522 = Coupling(name = 'GC_1522',
                   value = 'complex(0,1)*I5a2123*Lam',
                   order = {'NP':1})

GC_1523 = Coupling(name = 'GC_1523',
                   value = 'complex(0,1)*I5a2131*Lam',
                   order = {'NP':1})

GC_1524 = Coupling(name = 'GC_1524',
                   value = 'complex(0,1)*I5a2132*Lam',
                   order = {'NP':1})

GC_1525 = Coupling(name = 'GC_1525',
                   value = 'complex(0,1)*I5a2133*Lam',
                   order = {'NP':1})

GC_1526 = Coupling(name = 'GC_1526',
                   value = 'complex(0,1)*I5a2211*Lam',
                   order = {'NP':1})

GC_1527 = Coupling(name = 'GC_1527',
                   value = 'complex(0,1)*I5a2212*Lam',
                   order = {'NP':1})

GC_1528 = Coupling(name = 'GC_1528',
                   value = 'complex(0,1)*I5a2213*Lam',
                   order = {'NP':1})

GC_1529 = Coupling(name = 'GC_1529',
                   value = 'complex(0,1)*I5a2221*Lam',
                   order = {'NP':1})

GC_1530 = Coupling(name = 'GC_1530',
                   value = 'complex(0,1)*I5a2222*Lam',
                   order = {'NP':1})

GC_1531 = Coupling(name = 'GC_1531',
                   value = 'complex(0,1)*I5a2223*Lam',
                   order = {'NP':1})

GC_1532 = Coupling(name = 'GC_1532',
                   value = 'complex(0,1)*I5a2231*Lam',
                   order = {'NP':1})

GC_1533 = Coupling(name = 'GC_1533',
                   value = 'complex(0,1)*I5a2232*Lam',
                   order = {'NP':1})

GC_1534 = Coupling(name = 'GC_1534',
                   value = 'complex(0,1)*I5a2233*Lam',
                   order = {'NP':1})

GC_1535 = Coupling(name = 'GC_1535',
                   value = 'complex(0,1)*I5a2311*Lam',
                   order = {'NP':1})

GC_1536 = Coupling(name = 'GC_1536',
                   value = 'complex(0,1)*I5a2312*Lam',
                   order = {'NP':1})

GC_1537 = Coupling(name = 'GC_1537',
                   value = 'complex(0,1)*I5a2313*Lam',
                   order = {'NP':1})

GC_1538 = Coupling(name = 'GC_1538',
                   value = 'complex(0,1)*I5a2321*Lam',
                   order = {'NP':1})

GC_1539 = Coupling(name = 'GC_1539',
                   value = 'complex(0,1)*I5a2322*Lam',
                   order = {'NP':1})

GC_1540 = Coupling(name = 'GC_1540',
                   value = 'complex(0,1)*I5a2323*Lam',
                   order = {'NP':1})

GC_1541 = Coupling(name = 'GC_1541',
                   value = 'complex(0,1)*I5a2331*Lam',
                   order = {'NP':1})

GC_1542 = Coupling(name = 'GC_1542',
                   value = 'complex(0,1)*I5a2332*Lam',
                   order = {'NP':1})

GC_1543 = Coupling(name = 'GC_1543',
                   value = 'complex(0,1)*I5a2333*Lam',
                   order = {'NP':1})

GC_1544 = Coupling(name = 'GC_1544',
                   value = 'complex(0,1)*I5a3111*Lam',
                   order = {'NP':1})

GC_1545 = Coupling(name = 'GC_1545',
                   value = 'complex(0,1)*I5a3112*Lam',
                   order = {'NP':1})

GC_1546 = Coupling(name = 'GC_1546',
                   value = 'complex(0,1)*I5a3113*Lam',
                   order = {'NP':1})

GC_1547 = Coupling(name = 'GC_1547',
                   value = 'complex(0,1)*I5a3121*Lam',
                   order = {'NP':1})

GC_1548 = Coupling(name = 'GC_1548',
                   value = 'complex(0,1)*I5a3122*Lam',
                   order = {'NP':1})

GC_1549 = Coupling(name = 'GC_1549',
                   value = 'complex(0,1)*I5a3123*Lam',
                   order = {'NP':1})

GC_1550 = Coupling(name = 'GC_1550',
                   value = 'complex(0,1)*I5a3131*Lam',
                   order = {'NP':1})

GC_1551 = Coupling(name = 'GC_1551',
                   value = 'complex(0,1)*I5a3132*Lam',
                   order = {'NP':1})

GC_1552 = Coupling(name = 'GC_1552',
                   value = 'complex(0,1)*I5a3133*Lam',
                   order = {'NP':1})

GC_1553 = Coupling(name = 'GC_1553',
                   value = 'complex(0,1)*I5a3211*Lam',
                   order = {'NP':1})

GC_1554 = Coupling(name = 'GC_1554',
                   value = 'complex(0,1)*I5a3212*Lam',
                   order = {'NP':1})

GC_1555 = Coupling(name = 'GC_1555',
                   value = 'complex(0,1)*I5a3213*Lam',
                   order = {'NP':1})

GC_1556 = Coupling(name = 'GC_1556',
                   value = 'complex(0,1)*I5a3221*Lam',
                   order = {'NP':1})

GC_1557 = Coupling(name = 'GC_1557',
                   value = 'complex(0,1)*I5a3222*Lam',
                   order = {'NP':1})

GC_1558 = Coupling(name = 'GC_1558',
                   value = 'complex(0,1)*I5a3223*Lam',
                   order = {'NP':1})

GC_1559 = Coupling(name = 'GC_1559',
                   value = 'complex(0,1)*I5a3231*Lam',
                   order = {'NP':1})

GC_1560 = Coupling(name = 'GC_1560',
                   value = 'complex(0,1)*I5a3232*Lam',
                   order = {'NP':1})

GC_1561 = Coupling(name = 'GC_1561',
                   value = 'complex(0,1)*I5a3233*Lam',
                   order = {'NP':1})

GC_1562 = Coupling(name = 'GC_1562',
                   value = 'complex(0,1)*I5a3311*Lam',
                   order = {'NP':1})

GC_1563 = Coupling(name = 'GC_1563',
                   value = 'complex(0,1)*I5a3312*Lam',
                   order = {'NP':1})

GC_1564 = Coupling(name = 'GC_1564',
                   value = 'complex(0,1)*I5a3313*Lam',
                   order = {'NP':1})

GC_1565 = Coupling(name = 'GC_1565',
                   value = 'complex(0,1)*I5a3321*Lam',
                   order = {'NP':1})

GC_1566 = Coupling(name = 'GC_1566',
                   value = 'complex(0,1)*I5a3322*Lam',
                   order = {'NP':1})

GC_1567 = Coupling(name = 'GC_1567',
                   value = 'complex(0,1)*I5a3323*Lam',
                   order = {'NP':1})

GC_1568 = Coupling(name = 'GC_1568',
                   value = 'complex(0,1)*I5a3331*Lam',
                   order = {'NP':1})

GC_1569 = Coupling(name = 'GC_1569',
                   value = 'complex(0,1)*I5a3332*Lam',
                   order = {'NP':1})

GC_1570 = Coupling(name = 'GC_1570',
                   value = 'complex(0,1)*I5a3333*Lam',
                   order = {'NP':1})

GC_1571 = Coupling(name = 'GC_1571',
                   value = '-(complex(0,1)*I6a1111*Lam)/4.',
                   order = {'NP':1})

GC_1572 = Coupling(name = 'GC_1572',
                   value = '(complex(0,1)*I6a1111*Lam)/2.',
                   order = {'NP':1})

GC_1573 = Coupling(name = 'GC_1573',
                   value = '-(complex(0,1)*I6a1112*Lam)/4.',
                   order = {'NP':1})

GC_1574 = Coupling(name = 'GC_1574',
                   value = '(complex(0,1)*I6a1112*Lam)/2.',
                   order = {'NP':1})

GC_1575 = Coupling(name = 'GC_1575',
                   value = '-(complex(0,1)*I6a1113*Lam)/4.',
                   order = {'NP':1})

GC_1576 = Coupling(name = 'GC_1576',
                   value = '(complex(0,1)*I6a1113*Lam)/2.',
                   order = {'NP':1})

GC_1577 = Coupling(name = 'GC_1577',
                   value = '-(complex(0,1)*I6a1121*Lam)/4.',
                   order = {'NP':1})

GC_1578 = Coupling(name = 'GC_1578',
                   value = '(complex(0,1)*I6a1121*Lam)/2.',
                   order = {'NP':1})

GC_1579 = Coupling(name = 'GC_1579',
                   value = '-(complex(0,1)*I6a1122*Lam)/4.',
                   order = {'NP':1})

GC_1580 = Coupling(name = 'GC_1580',
                   value = '(complex(0,1)*I6a1122*Lam)/2.',
                   order = {'NP':1})

GC_1581 = Coupling(name = 'GC_1581',
                   value = '-(complex(0,1)*I6a1123*Lam)/4.',
                   order = {'NP':1})

GC_1582 = Coupling(name = 'GC_1582',
                   value = '(complex(0,1)*I6a1123*Lam)/2.',
                   order = {'NP':1})

GC_1583 = Coupling(name = 'GC_1583',
                   value = '-(complex(0,1)*I6a1131*Lam)/4.',
                   order = {'NP':1})

GC_1584 = Coupling(name = 'GC_1584',
                   value = '(complex(0,1)*I6a1131*Lam)/2.',
                   order = {'NP':1})

GC_1585 = Coupling(name = 'GC_1585',
                   value = '-(complex(0,1)*I6a1132*Lam)/4.',
                   order = {'NP':1})

GC_1586 = Coupling(name = 'GC_1586',
                   value = '(complex(0,1)*I6a1132*Lam)/2.',
                   order = {'NP':1})

GC_1587 = Coupling(name = 'GC_1587',
                   value = '-(complex(0,1)*I6a1133*Lam)/4.',
                   order = {'NP':1})

GC_1588 = Coupling(name = 'GC_1588',
                   value = '(complex(0,1)*I6a1133*Lam)/2.',
                   order = {'NP':1})

GC_1589 = Coupling(name = 'GC_1589',
                   value = '-(complex(0,1)*I6a1211*Lam)/4.',
                   order = {'NP':1})

GC_1590 = Coupling(name = 'GC_1590',
                   value = '(complex(0,1)*I6a1211*Lam)/2.',
                   order = {'NP':1})

GC_1591 = Coupling(name = 'GC_1591',
                   value = '-(complex(0,1)*I6a1212*Lam)/4.',
                   order = {'NP':1})

GC_1592 = Coupling(name = 'GC_1592',
                   value = '(complex(0,1)*I6a1212*Lam)/2.',
                   order = {'NP':1})

GC_1593 = Coupling(name = 'GC_1593',
                   value = '-(complex(0,1)*I6a1213*Lam)/4.',
                   order = {'NP':1})

GC_1594 = Coupling(name = 'GC_1594',
                   value = '(complex(0,1)*I6a1213*Lam)/2.',
                   order = {'NP':1})

GC_1595 = Coupling(name = 'GC_1595',
                   value = '-(complex(0,1)*I6a1221*Lam)/4.',
                   order = {'NP':1})

GC_1596 = Coupling(name = 'GC_1596',
                   value = '(complex(0,1)*I6a1221*Lam)/2.',
                   order = {'NP':1})

GC_1597 = Coupling(name = 'GC_1597',
                   value = '-(complex(0,1)*I6a1222*Lam)/4.',
                   order = {'NP':1})

GC_1598 = Coupling(name = 'GC_1598',
                   value = '(complex(0,1)*I6a1222*Lam)/2.',
                   order = {'NP':1})

GC_1599 = Coupling(name = 'GC_1599',
                   value = '-(complex(0,1)*I6a1223*Lam)/4.',
                   order = {'NP':1})

GC_1600 = Coupling(name = 'GC_1600',
                   value = '(complex(0,1)*I6a1223*Lam)/2.',
                   order = {'NP':1})

GC_1601 = Coupling(name = 'GC_1601',
                   value = '-(complex(0,1)*I6a1231*Lam)/4.',
                   order = {'NP':1})

GC_1602 = Coupling(name = 'GC_1602',
                   value = '(complex(0,1)*I6a1231*Lam)/2.',
                   order = {'NP':1})

GC_1603 = Coupling(name = 'GC_1603',
                   value = '-(complex(0,1)*I6a1232*Lam)/4.',
                   order = {'NP':1})

GC_1604 = Coupling(name = 'GC_1604',
                   value = '(complex(0,1)*I6a1232*Lam)/2.',
                   order = {'NP':1})

GC_1605 = Coupling(name = 'GC_1605',
                   value = '-(complex(0,1)*I6a1233*Lam)/4.',
                   order = {'NP':1})

GC_1606 = Coupling(name = 'GC_1606',
                   value = '(complex(0,1)*I6a1233*Lam)/2.',
                   order = {'NP':1})

GC_1607 = Coupling(name = 'GC_1607',
                   value = '-(complex(0,1)*I6a1311*Lam)/4.',
                   order = {'NP':1})

GC_1608 = Coupling(name = 'GC_1608',
                   value = '(complex(0,1)*I6a1311*Lam)/2.',
                   order = {'NP':1})

GC_1609 = Coupling(name = 'GC_1609',
                   value = '-(complex(0,1)*I6a1312*Lam)/4.',
                   order = {'NP':1})

GC_1610 = Coupling(name = 'GC_1610',
                   value = '(complex(0,1)*I6a1312*Lam)/2.',
                   order = {'NP':1})

GC_1611 = Coupling(name = 'GC_1611',
                   value = '-(complex(0,1)*I6a1313*Lam)/4.',
                   order = {'NP':1})

GC_1612 = Coupling(name = 'GC_1612',
                   value = '(complex(0,1)*I6a1313*Lam)/2.',
                   order = {'NP':1})

GC_1613 = Coupling(name = 'GC_1613',
                   value = '-(complex(0,1)*I6a1321*Lam)/4.',
                   order = {'NP':1})

GC_1614 = Coupling(name = 'GC_1614',
                   value = '(complex(0,1)*I6a1321*Lam)/2.',
                   order = {'NP':1})

GC_1615 = Coupling(name = 'GC_1615',
                   value = '-(complex(0,1)*I6a1322*Lam)/4.',
                   order = {'NP':1})

GC_1616 = Coupling(name = 'GC_1616',
                   value = '(complex(0,1)*I6a1322*Lam)/2.',
                   order = {'NP':1})

GC_1617 = Coupling(name = 'GC_1617',
                   value = '-(complex(0,1)*I6a1323*Lam)/4.',
                   order = {'NP':1})

GC_1618 = Coupling(name = 'GC_1618',
                   value = '(complex(0,1)*I6a1323*Lam)/2.',
                   order = {'NP':1})

GC_1619 = Coupling(name = 'GC_1619',
                   value = '-(complex(0,1)*I6a1331*Lam)/4.',
                   order = {'NP':1})

GC_1620 = Coupling(name = 'GC_1620',
                   value = '(complex(0,1)*I6a1331*Lam)/2.',
                   order = {'NP':1})

GC_1621 = Coupling(name = 'GC_1621',
                   value = '-(complex(0,1)*I6a1332*Lam)/4.',
                   order = {'NP':1})

GC_1622 = Coupling(name = 'GC_1622',
                   value = '(complex(0,1)*I6a1332*Lam)/2.',
                   order = {'NP':1})

GC_1623 = Coupling(name = 'GC_1623',
                   value = '-(complex(0,1)*I6a1333*Lam)/4.',
                   order = {'NP':1})

GC_1624 = Coupling(name = 'GC_1624',
                   value = '(complex(0,1)*I6a1333*Lam)/2.',
                   order = {'NP':1})

GC_1625 = Coupling(name = 'GC_1625',
                   value = '-(complex(0,1)*I6a2111*Lam)/4.',
                   order = {'NP':1})

GC_1626 = Coupling(name = 'GC_1626',
                   value = '(complex(0,1)*I6a2111*Lam)/2.',
                   order = {'NP':1})

GC_1627 = Coupling(name = 'GC_1627',
                   value = '-(complex(0,1)*I6a2112*Lam)/4.',
                   order = {'NP':1})

GC_1628 = Coupling(name = 'GC_1628',
                   value = '(complex(0,1)*I6a2112*Lam)/2.',
                   order = {'NP':1})

GC_1629 = Coupling(name = 'GC_1629',
                   value = '-(complex(0,1)*I6a2113*Lam)/4.',
                   order = {'NP':1})

GC_1630 = Coupling(name = 'GC_1630',
                   value = '(complex(0,1)*I6a2113*Lam)/2.',
                   order = {'NP':1})

GC_1631 = Coupling(name = 'GC_1631',
                   value = '-(complex(0,1)*I6a2121*Lam)/4.',
                   order = {'NP':1})

GC_1632 = Coupling(name = 'GC_1632',
                   value = '(complex(0,1)*I6a2121*Lam)/2.',
                   order = {'NP':1})

GC_1633 = Coupling(name = 'GC_1633',
                   value = '-(complex(0,1)*I6a2122*Lam)/4.',
                   order = {'NP':1})

GC_1634 = Coupling(name = 'GC_1634',
                   value = '(complex(0,1)*I6a2122*Lam)/2.',
                   order = {'NP':1})

GC_1635 = Coupling(name = 'GC_1635',
                   value = '-(complex(0,1)*I6a2123*Lam)/4.',
                   order = {'NP':1})

GC_1636 = Coupling(name = 'GC_1636',
                   value = '(complex(0,1)*I6a2123*Lam)/2.',
                   order = {'NP':1})

GC_1637 = Coupling(name = 'GC_1637',
                   value = '-(complex(0,1)*I6a2131*Lam)/4.',
                   order = {'NP':1})

GC_1638 = Coupling(name = 'GC_1638',
                   value = '(complex(0,1)*I6a2131*Lam)/2.',
                   order = {'NP':1})

GC_1639 = Coupling(name = 'GC_1639',
                   value = '-(complex(0,1)*I6a2132*Lam)/4.',
                   order = {'NP':1})

GC_1640 = Coupling(name = 'GC_1640',
                   value = '(complex(0,1)*I6a2132*Lam)/2.',
                   order = {'NP':1})

GC_1641 = Coupling(name = 'GC_1641',
                   value = '-(complex(0,1)*I6a2133*Lam)/4.',
                   order = {'NP':1})

GC_1642 = Coupling(name = 'GC_1642',
                   value = '(complex(0,1)*I6a2133*Lam)/2.',
                   order = {'NP':1})

GC_1643 = Coupling(name = 'GC_1643',
                   value = '-(complex(0,1)*I6a2211*Lam)/4.',
                   order = {'NP':1})

GC_1644 = Coupling(name = 'GC_1644',
                   value = '(complex(0,1)*I6a2211*Lam)/2.',
                   order = {'NP':1})

GC_1645 = Coupling(name = 'GC_1645',
                   value = '-(complex(0,1)*I6a2212*Lam)/4.',
                   order = {'NP':1})

GC_1646 = Coupling(name = 'GC_1646',
                   value = '(complex(0,1)*I6a2212*Lam)/2.',
                   order = {'NP':1})

GC_1647 = Coupling(name = 'GC_1647',
                   value = '-(complex(0,1)*I6a2213*Lam)/4.',
                   order = {'NP':1})

GC_1648 = Coupling(name = 'GC_1648',
                   value = '(complex(0,1)*I6a2213*Lam)/2.',
                   order = {'NP':1})

GC_1649 = Coupling(name = 'GC_1649',
                   value = '-(complex(0,1)*I6a2221*Lam)/4.',
                   order = {'NP':1})

GC_1650 = Coupling(name = 'GC_1650',
                   value = '(complex(0,1)*I6a2221*Lam)/2.',
                   order = {'NP':1})

GC_1651 = Coupling(name = 'GC_1651',
                   value = '-(complex(0,1)*I6a2222*Lam)/4.',
                   order = {'NP':1})

GC_1652 = Coupling(name = 'GC_1652',
                   value = '(complex(0,1)*I6a2222*Lam)/2.',
                   order = {'NP':1})

GC_1653 = Coupling(name = 'GC_1653',
                   value = '-(complex(0,1)*I6a2223*Lam)/4.',
                   order = {'NP':1})

GC_1654 = Coupling(name = 'GC_1654',
                   value = '(complex(0,1)*I6a2223*Lam)/2.',
                   order = {'NP':1})

GC_1655 = Coupling(name = 'GC_1655',
                   value = '-(complex(0,1)*I6a2231*Lam)/4.',
                   order = {'NP':1})

GC_1656 = Coupling(name = 'GC_1656',
                   value = '(complex(0,1)*I6a2231*Lam)/2.',
                   order = {'NP':1})

GC_1657 = Coupling(name = 'GC_1657',
                   value = '-(complex(0,1)*I6a2232*Lam)/4.',
                   order = {'NP':1})

GC_1658 = Coupling(name = 'GC_1658',
                   value = '(complex(0,1)*I6a2232*Lam)/2.',
                   order = {'NP':1})

GC_1659 = Coupling(name = 'GC_1659',
                   value = '-(complex(0,1)*I6a2233*Lam)/4.',
                   order = {'NP':1})

GC_1660 = Coupling(name = 'GC_1660',
                   value = '(complex(0,1)*I6a2233*Lam)/2.',
                   order = {'NP':1})

GC_1661 = Coupling(name = 'GC_1661',
                   value = '-(complex(0,1)*I6a2311*Lam)/4.',
                   order = {'NP':1})

GC_1662 = Coupling(name = 'GC_1662',
                   value = '(complex(0,1)*I6a2311*Lam)/2.',
                   order = {'NP':1})

GC_1663 = Coupling(name = 'GC_1663',
                   value = '-(complex(0,1)*I6a2312*Lam)/4.',
                   order = {'NP':1})

GC_1664 = Coupling(name = 'GC_1664',
                   value = '(complex(0,1)*I6a2312*Lam)/2.',
                   order = {'NP':1})

GC_1665 = Coupling(name = 'GC_1665',
                   value = '-(complex(0,1)*I6a2313*Lam)/4.',
                   order = {'NP':1})

GC_1666 = Coupling(name = 'GC_1666',
                   value = '(complex(0,1)*I6a2313*Lam)/2.',
                   order = {'NP':1})

GC_1667 = Coupling(name = 'GC_1667',
                   value = '-(complex(0,1)*I6a2321*Lam)/4.',
                   order = {'NP':1})

GC_1668 = Coupling(name = 'GC_1668',
                   value = '(complex(0,1)*I6a2321*Lam)/2.',
                   order = {'NP':1})

GC_1669 = Coupling(name = 'GC_1669',
                   value = '-(complex(0,1)*I6a2322*Lam)/4.',
                   order = {'NP':1})

GC_1670 = Coupling(name = 'GC_1670',
                   value = '(complex(0,1)*I6a2322*Lam)/2.',
                   order = {'NP':1})

GC_1671 = Coupling(name = 'GC_1671',
                   value = '-(complex(0,1)*I6a2323*Lam)/4.',
                   order = {'NP':1})

GC_1672 = Coupling(name = 'GC_1672',
                   value = '(complex(0,1)*I6a2323*Lam)/2.',
                   order = {'NP':1})

GC_1673 = Coupling(name = 'GC_1673',
                   value = '-(complex(0,1)*I6a2331*Lam)/4.',
                   order = {'NP':1})

GC_1674 = Coupling(name = 'GC_1674',
                   value = '(complex(0,1)*I6a2331*Lam)/2.',
                   order = {'NP':1})

GC_1675 = Coupling(name = 'GC_1675',
                   value = '-(complex(0,1)*I6a2332*Lam)/4.',
                   order = {'NP':1})

GC_1676 = Coupling(name = 'GC_1676',
                   value = '(complex(0,1)*I6a2332*Lam)/2.',
                   order = {'NP':1})

GC_1677 = Coupling(name = 'GC_1677',
                   value = '-(complex(0,1)*I6a2333*Lam)/4.',
                   order = {'NP':1})

GC_1678 = Coupling(name = 'GC_1678',
                   value = '(complex(0,1)*I6a2333*Lam)/2.',
                   order = {'NP':1})

GC_1679 = Coupling(name = 'GC_1679',
                   value = '-(complex(0,1)*I6a3111*Lam)/4.',
                   order = {'NP':1})

GC_1680 = Coupling(name = 'GC_1680',
                   value = '(complex(0,1)*I6a3111*Lam)/2.',
                   order = {'NP':1})

GC_1681 = Coupling(name = 'GC_1681',
                   value = '-(complex(0,1)*I6a3112*Lam)/4.',
                   order = {'NP':1})

GC_1682 = Coupling(name = 'GC_1682',
                   value = '(complex(0,1)*I6a3112*Lam)/2.',
                   order = {'NP':1})

GC_1683 = Coupling(name = 'GC_1683',
                   value = '-(complex(0,1)*I6a3113*Lam)/4.',
                   order = {'NP':1})

GC_1684 = Coupling(name = 'GC_1684',
                   value = '(complex(0,1)*I6a3113*Lam)/2.',
                   order = {'NP':1})

GC_1685 = Coupling(name = 'GC_1685',
                   value = '-(complex(0,1)*I6a3121*Lam)/4.',
                   order = {'NP':1})

GC_1686 = Coupling(name = 'GC_1686',
                   value = '(complex(0,1)*I6a3121*Lam)/2.',
                   order = {'NP':1})

GC_1687 = Coupling(name = 'GC_1687',
                   value = '-(complex(0,1)*I6a3122*Lam)/4.',
                   order = {'NP':1})

GC_1688 = Coupling(name = 'GC_1688',
                   value = '(complex(0,1)*I6a3122*Lam)/2.',
                   order = {'NP':1})

GC_1689 = Coupling(name = 'GC_1689',
                   value = '-(complex(0,1)*I6a3123*Lam)/4.',
                   order = {'NP':1})

GC_1690 = Coupling(name = 'GC_1690',
                   value = '(complex(0,1)*I6a3123*Lam)/2.',
                   order = {'NP':1})

GC_1691 = Coupling(name = 'GC_1691',
                   value = '-(complex(0,1)*I6a3131*Lam)/4.',
                   order = {'NP':1})

GC_1692 = Coupling(name = 'GC_1692',
                   value = '(complex(0,1)*I6a3131*Lam)/2.',
                   order = {'NP':1})

GC_1693 = Coupling(name = 'GC_1693',
                   value = '-(complex(0,1)*I6a3132*Lam)/4.',
                   order = {'NP':1})

GC_1694 = Coupling(name = 'GC_1694',
                   value = '(complex(0,1)*I6a3132*Lam)/2.',
                   order = {'NP':1})

GC_1695 = Coupling(name = 'GC_1695',
                   value = '-(complex(0,1)*I6a3133*Lam)/4.',
                   order = {'NP':1})

GC_1696 = Coupling(name = 'GC_1696',
                   value = '(complex(0,1)*I6a3133*Lam)/2.',
                   order = {'NP':1})

GC_1697 = Coupling(name = 'GC_1697',
                   value = '-(complex(0,1)*I6a3211*Lam)/4.',
                   order = {'NP':1})

GC_1698 = Coupling(name = 'GC_1698',
                   value = '(complex(0,1)*I6a3211*Lam)/2.',
                   order = {'NP':1})

GC_1699 = Coupling(name = 'GC_1699',
                   value = '-(complex(0,1)*I6a3212*Lam)/4.',
                   order = {'NP':1})

GC_1700 = Coupling(name = 'GC_1700',
                   value = '(complex(0,1)*I6a3212*Lam)/2.',
                   order = {'NP':1})

GC_1701 = Coupling(name = 'GC_1701',
                   value = '-(complex(0,1)*I6a3213*Lam)/4.',
                   order = {'NP':1})

GC_1702 = Coupling(name = 'GC_1702',
                   value = '(complex(0,1)*I6a3213*Lam)/2.',
                   order = {'NP':1})

GC_1703 = Coupling(name = 'GC_1703',
                   value = '-(complex(0,1)*I6a3221*Lam)/4.',
                   order = {'NP':1})

GC_1704 = Coupling(name = 'GC_1704',
                   value = '(complex(0,1)*I6a3221*Lam)/2.',
                   order = {'NP':1})

GC_1705 = Coupling(name = 'GC_1705',
                   value = '-(complex(0,1)*I6a3222*Lam)/4.',
                   order = {'NP':1})

GC_1706 = Coupling(name = 'GC_1706',
                   value = '(complex(0,1)*I6a3222*Lam)/2.',
                   order = {'NP':1})

GC_1707 = Coupling(name = 'GC_1707',
                   value = '-(complex(0,1)*I6a3223*Lam)/4.',
                   order = {'NP':1})

GC_1708 = Coupling(name = 'GC_1708',
                   value = '(complex(0,1)*I6a3223*Lam)/2.',
                   order = {'NP':1})

GC_1709 = Coupling(name = 'GC_1709',
                   value = '-(complex(0,1)*I6a3231*Lam)/4.',
                   order = {'NP':1})

GC_1710 = Coupling(name = 'GC_1710',
                   value = '(complex(0,1)*I6a3231*Lam)/2.',
                   order = {'NP':1})

GC_1711 = Coupling(name = 'GC_1711',
                   value = '-(complex(0,1)*I6a3232*Lam)/4.',
                   order = {'NP':1})

GC_1712 = Coupling(name = 'GC_1712',
                   value = '(complex(0,1)*I6a3232*Lam)/2.',
                   order = {'NP':1})

GC_1713 = Coupling(name = 'GC_1713',
                   value = '-(complex(0,1)*I6a3233*Lam)/4.',
                   order = {'NP':1})

GC_1714 = Coupling(name = 'GC_1714',
                   value = '(complex(0,1)*I6a3233*Lam)/2.',
                   order = {'NP':1})

GC_1715 = Coupling(name = 'GC_1715',
                   value = '-(complex(0,1)*I6a3311*Lam)/4.',
                   order = {'NP':1})

GC_1716 = Coupling(name = 'GC_1716',
                   value = '(complex(0,1)*I6a3311*Lam)/2.',
                   order = {'NP':1})

GC_1717 = Coupling(name = 'GC_1717',
                   value = '-(complex(0,1)*I6a3312*Lam)/4.',
                   order = {'NP':1})

GC_1718 = Coupling(name = 'GC_1718',
                   value = '(complex(0,1)*I6a3312*Lam)/2.',
                   order = {'NP':1})

GC_1719 = Coupling(name = 'GC_1719',
                   value = '-(complex(0,1)*I6a3313*Lam)/4.',
                   order = {'NP':1})

GC_1720 = Coupling(name = 'GC_1720',
                   value = '(complex(0,1)*I6a3313*Lam)/2.',
                   order = {'NP':1})

GC_1721 = Coupling(name = 'GC_1721',
                   value = '-(complex(0,1)*I6a3321*Lam)/4.',
                   order = {'NP':1})

GC_1722 = Coupling(name = 'GC_1722',
                   value = '(complex(0,1)*I6a3321*Lam)/2.',
                   order = {'NP':1})

GC_1723 = Coupling(name = 'GC_1723',
                   value = '-(complex(0,1)*I6a3322*Lam)/4.',
                   order = {'NP':1})

GC_1724 = Coupling(name = 'GC_1724',
                   value = '(complex(0,1)*I6a3322*Lam)/2.',
                   order = {'NP':1})

GC_1725 = Coupling(name = 'GC_1725',
                   value = '-(complex(0,1)*I6a3323*Lam)/4.',
                   order = {'NP':1})

GC_1726 = Coupling(name = 'GC_1726',
                   value = '(complex(0,1)*I6a3323*Lam)/2.',
                   order = {'NP':1})

GC_1727 = Coupling(name = 'GC_1727',
                   value = '-(complex(0,1)*I6a3331*Lam)/4.',
                   order = {'NP':1})

GC_1728 = Coupling(name = 'GC_1728',
                   value = '(complex(0,1)*I6a3331*Lam)/2.',
                   order = {'NP':1})

GC_1729 = Coupling(name = 'GC_1729',
                   value = '-(complex(0,1)*I6a3332*Lam)/4.',
                   order = {'NP':1})

GC_1730 = Coupling(name = 'GC_1730',
                   value = '(complex(0,1)*I6a3332*Lam)/2.',
                   order = {'NP':1})

GC_1731 = Coupling(name = 'GC_1731',
                   value = '-(complex(0,1)*I6a3333*Lam)/4.',
                   order = {'NP':1})

GC_1732 = Coupling(name = 'GC_1732',
                   value = '(complex(0,1)*I6a3333*Lam)/2.',
                   order = {'NP':1})

GC_1733 = Coupling(name = 'GC_1733',
                   value = '-(complex(0,1)*I7a1111*Lam)/4.',
                   order = {'NP':1})

GC_1734 = Coupling(name = 'GC_1734',
                   value = '(complex(0,1)*I7a1111*Lam)/2.',
                   order = {'NP':1})

GC_1735 = Coupling(name = 'GC_1735',
                   value = '-(complex(0,1)*I7a1112*Lam)/4.',
                   order = {'NP':1})

GC_1736 = Coupling(name = 'GC_1736',
                   value = '(complex(0,1)*I7a1112*Lam)/2.',
                   order = {'NP':1})

GC_1737 = Coupling(name = 'GC_1737',
                   value = '-(complex(0,1)*I7a1113*Lam)/4.',
                   order = {'NP':1})

GC_1738 = Coupling(name = 'GC_1738',
                   value = '(complex(0,1)*I7a1113*Lam)/2.',
                   order = {'NP':1})

GC_1739 = Coupling(name = 'GC_1739',
                   value = '-(complex(0,1)*I7a1121*Lam)/4.',
                   order = {'NP':1})

GC_1740 = Coupling(name = 'GC_1740',
                   value = '(complex(0,1)*I7a1121*Lam)/2.',
                   order = {'NP':1})

GC_1741 = Coupling(name = 'GC_1741',
                   value = '-(complex(0,1)*I7a1122*Lam)/4.',
                   order = {'NP':1})

GC_1742 = Coupling(name = 'GC_1742',
                   value = '(complex(0,1)*I7a1122*Lam)/2.',
                   order = {'NP':1})

GC_1743 = Coupling(name = 'GC_1743',
                   value = '-(complex(0,1)*I7a1123*Lam)/4.',
                   order = {'NP':1})

GC_1744 = Coupling(name = 'GC_1744',
                   value = '(complex(0,1)*I7a1123*Lam)/2.',
                   order = {'NP':1})

GC_1745 = Coupling(name = 'GC_1745',
                   value = '-(complex(0,1)*I7a1131*Lam)/4.',
                   order = {'NP':1})

GC_1746 = Coupling(name = 'GC_1746',
                   value = '(complex(0,1)*I7a1131*Lam)/2.',
                   order = {'NP':1})

GC_1747 = Coupling(name = 'GC_1747',
                   value = '-(complex(0,1)*I7a1132*Lam)/4.',
                   order = {'NP':1})

GC_1748 = Coupling(name = 'GC_1748',
                   value = '(complex(0,1)*I7a1132*Lam)/2.',
                   order = {'NP':1})

GC_1749 = Coupling(name = 'GC_1749',
                   value = '-(complex(0,1)*I7a1133*Lam)/4.',
                   order = {'NP':1})

GC_1750 = Coupling(name = 'GC_1750',
                   value = '(complex(0,1)*I7a1133*Lam)/2.',
                   order = {'NP':1})

GC_1751 = Coupling(name = 'GC_1751',
                   value = '-(complex(0,1)*I7a1211*Lam)/4.',
                   order = {'NP':1})

GC_1752 = Coupling(name = 'GC_1752',
                   value = '(complex(0,1)*I7a1211*Lam)/2.',
                   order = {'NP':1})

GC_1753 = Coupling(name = 'GC_1753',
                   value = '-(complex(0,1)*I7a1212*Lam)/4.',
                   order = {'NP':1})

GC_1754 = Coupling(name = 'GC_1754',
                   value = '(complex(0,1)*I7a1212*Lam)/2.',
                   order = {'NP':1})

GC_1755 = Coupling(name = 'GC_1755',
                   value = '-(complex(0,1)*I7a1213*Lam)/4.',
                   order = {'NP':1})

GC_1756 = Coupling(name = 'GC_1756',
                   value = '(complex(0,1)*I7a1213*Lam)/2.',
                   order = {'NP':1})

GC_1757 = Coupling(name = 'GC_1757',
                   value = '-(complex(0,1)*I7a1221*Lam)/4.',
                   order = {'NP':1})

GC_1758 = Coupling(name = 'GC_1758',
                   value = '(complex(0,1)*I7a1221*Lam)/2.',
                   order = {'NP':1})

GC_1759 = Coupling(name = 'GC_1759',
                   value = '-(complex(0,1)*I7a1222*Lam)/4.',
                   order = {'NP':1})

GC_1760 = Coupling(name = 'GC_1760',
                   value = '(complex(0,1)*I7a1222*Lam)/2.',
                   order = {'NP':1})

GC_1761 = Coupling(name = 'GC_1761',
                   value = '-(complex(0,1)*I7a1223*Lam)/4.',
                   order = {'NP':1})

GC_1762 = Coupling(name = 'GC_1762',
                   value = '(complex(0,1)*I7a1223*Lam)/2.',
                   order = {'NP':1})

GC_1763 = Coupling(name = 'GC_1763',
                   value = '-(complex(0,1)*I7a1231*Lam)/4.',
                   order = {'NP':1})

GC_1764 = Coupling(name = 'GC_1764',
                   value = '(complex(0,1)*I7a1231*Lam)/2.',
                   order = {'NP':1})

GC_1765 = Coupling(name = 'GC_1765',
                   value = '-(complex(0,1)*I7a1232*Lam)/4.',
                   order = {'NP':1})

GC_1766 = Coupling(name = 'GC_1766',
                   value = '(complex(0,1)*I7a1232*Lam)/2.',
                   order = {'NP':1})

GC_1767 = Coupling(name = 'GC_1767',
                   value = '-(complex(0,1)*I7a1233*Lam)/4.',
                   order = {'NP':1})

GC_1768 = Coupling(name = 'GC_1768',
                   value = '(complex(0,1)*I7a1233*Lam)/2.',
                   order = {'NP':1})

GC_1769 = Coupling(name = 'GC_1769',
                   value = '-(complex(0,1)*I7a1311*Lam)/4.',
                   order = {'NP':1})

GC_1770 = Coupling(name = 'GC_1770',
                   value = '(complex(0,1)*I7a1311*Lam)/2.',
                   order = {'NP':1})

GC_1771 = Coupling(name = 'GC_1771',
                   value = '-(complex(0,1)*I7a1312*Lam)/4.',
                   order = {'NP':1})

GC_1772 = Coupling(name = 'GC_1772',
                   value = '(complex(0,1)*I7a1312*Lam)/2.',
                   order = {'NP':1})

GC_1773 = Coupling(name = 'GC_1773',
                   value = '-(complex(0,1)*I7a1313*Lam)/4.',
                   order = {'NP':1})

GC_1774 = Coupling(name = 'GC_1774',
                   value = '(complex(0,1)*I7a1313*Lam)/2.',
                   order = {'NP':1})

GC_1775 = Coupling(name = 'GC_1775',
                   value = '-(complex(0,1)*I7a1321*Lam)/4.',
                   order = {'NP':1})

GC_1776 = Coupling(name = 'GC_1776',
                   value = '(complex(0,1)*I7a1321*Lam)/2.',
                   order = {'NP':1})

GC_1777 = Coupling(name = 'GC_1777',
                   value = '-(complex(0,1)*I7a1322*Lam)/4.',
                   order = {'NP':1})

GC_1778 = Coupling(name = 'GC_1778',
                   value = '(complex(0,1)*I7a1322*Lam)/2.',
                   order = {'NP':1})

GC_1779 = Coupling(name = 'GC_1779',
                   value = '-(complex(0,1)*I7a1323*Lam)/4.',
                   order = {'NP':1})

GC_1780 = Coupling(name = 'GC_1780',
                   value = '(complex(0,1)*I7a1323*Lam)/2.',
                   order = {'NP':1})

GC_1781 = Coupling(name = 'GC_1781',
                   value = '-(complex(0,1)*I7a1331*Lam)/4.',
                   order = {'NP':1})

GC_1782 = Coupling(name = 'GC_1782',
                   value = '(complex(0,1)*I7a1331*Lam)/2.',
                   order = {'NP':1})

GC_1783 = Coupling(name = 'GC_1783',
                   value = '-(complex(0,1)*I7a1332*Lam)/4.',
                   order = {'NP':1})

GC_1784 = Coupling(name = 'GC_1784',
                   value = '(complex(0,1)*I7a1332*Lam)/2.',
                   order = {'NP':1})

GC_1785 = Coupling(name = 'GC_1785',
                   value = '-(complex(0,1)*I7a1333*Lam)/4.',
                   order = {'NP':1})

GC_1786 = Coupling(name = 'GC_1786',
                   value = '(complex(0,1)*I7a1333*Lam)/2.',
                   order = {'NP':1})

GC_1787 = Coupling(name = 'GC_1787',
                   value = '-(complex(0,1)*I7a2111*Lam)/4.',
                   order = {'NP':1})

GC_1788 = Coupling(name = 'GC_1788',
                   value = '(complex(0,1)*I7a2111*Lam)/2.',
                   order = {'NP':1})

GC_1789 = Coupling(name = 'GC_1789',
                   value = '-(complex(0,1)*I7a2112*Lam)/4.',
                   order = {'NP':1})

GC_1790 = Coupling(name = 'GC_1790',
                   value = '(complex(0,1)*I7a2112*Lam)/2.',
                   order = {'NP':1})

GC_1791 = Coupling(name = 'GC_1791',
                   value = '-(complex(0,1)*I7a2113*Lam)/4.',
                   order = {'NP':1})

GC_1792 = Coupling(name = 'GC_1792',
                   value = '(complex(0,1)*I7a2113*Lam)/2.',
                   order = {'NP':1})

GC_1793 = Coupling(name = 'GC_1793',
                   value = '-(complex(0,1)*I7a2121*Lam)/4.',
                   order = {'NP':1})

GC_1794 = Coupling(name = 'GC_1794',
                   value = '(complex(0,1)*I7a2121*Lam)/2.',
                   order = {'NP':1})

GC_1795 = Coupling(name = 'GC_1795',
                   value = '-(complex(0,1)*I7a2122*Lam)/4.',
                   order = {'NP':1})

GC_1796 = Coupling(name = 'GC_1796',
                   value = '(complex(0,1)*I7a2122*Lam)/2.',
                   order = {'NP':1})

GC_1797 = Coupling(name = 'GC_1797',
                   value = '-(complex(0,1)*I7a2123*Lam)/4.',
                   order = {'NP':1})

GC_1798 = Coupling(name = 'GC_1798',
                   value = '(complex(0,1)*I7a2123*Lam)/2.',
                   order = {'NP':1})

GC_1799 = Coupling(name = 'GC_1799',
                   value = '-(complex(0,1)*I7a2131*Lam)/4.',
                   order = {'NP':1})

GC_1800 = Coupling(name = 'GC_1800',
                   value = '(complex(0,1)*I7a2131*Lam)/2.',
                   order = {'NP':1})

GC_1801 = Coupling(name = 'GC_1801',
                   value = '-(complex(0,1)*I7a2132*Lam)/4.',
                   order = {'NP':1})

GC_1802 = Coupling(name = 'GC_1802',
                   value = '(complex(0,1)*I7a2132*Lam)/2.',
                   order = {'NP':1})

GC_1803 = Coupling(name = 'GC_1803',
                   value = '-(complex(0,1)*I7a2133*Lam)/4.',
                   order = {'NP':1})

GC_1804 = Coupling(name = 'GC_1804',
                   value = '(complex(0,1)*I7a2133*Lam)/2.',
                   order = {'NP':1})

GC_1805 = Coupling(name = 'GC_1805',
                   value = '-(complex(0,1)*I7a2211*Lam)/4.',
                   order = {'NP':1})

GC_1806 = Coupling(name = 'GC_1806',
                   value = '(complex(0,1)*I7a2211*Lam)/2.',
                   order = {'NP':1})

GC_1807 = Coupling(name = 'GC_1807',
                   value = '-(complex(0,1)*I7a2212*Lam)/4.',
                   order = {'NP':1})

GC_1808 = Coupling(name = 'GC_1808',
                   value = '(complex(0,1)*I7a2212*Lam)/2.',
                   order = {'NP':1})

GC_1809 = Coupling(name = 'GC_1809',
                   value = '-(complex(0,1)*I7a2213*Lam)/4.',
                   order = {'NP':1})

GC_1810 = Coupling(name = 'GC_1810',
                   value = '(complex(0,1)*I7a2213*Lam)/2.',
                   order = {'NP':1})

GC_1811 = Coupling(name = 'GC_1811',
                   value = '-(complex(0,1)*I7a2221*Lam)/4.',
                   order = {'NP':1})

GC_1812 = Coupling(name = 'GC_1812',
                   value = '(complex(0,1)*I7a2221*Lam)/2.',
                   order = {'NP':1})

GC_1813 = Coupling(name = 'GC_1813',
                   value = '-(complex(0,1)*I7a2222*Lam)/4.',
                   order = {'NP':1})

GC_1814 = Coupling(name = 'GC_1814',
                   value = '(complex(0,1)*I7a2222*Lam)/2.',
                   order = {'NP':1})

GC_1815 = Coupling(name = 'GC_1815',
                   value = '-(complex(0,1)*I7a2223*Lam)/4.',
                   order = {'NP':1})

GC_1816 = Coupling(name = 'GC_1816',
                   value = '(complex(0,1)*I7a2223*Lam)/2.',
                   order = {'NP':1})

GC_1817 = Coupling(name = 'GC_1817',
                   value = '-(complex(0,1)*I7a2231*Lam)/4.',
                   order = {'NP':1})

GC_1818 = Coupling(name = 'GC_1818',
                   value = '(complex(0,1)*I7a2231*Lam)/2.',
                   order = {'NP':1})

GC_1819 = Coupling(name = 'GC_1819',
                   value = '-(complex(0,1)*I7a2232*Lam)/4.',
                   order = {'NP':1})

GC_1820 = Coupling(name = 'GC_1820',
                   value = '(complex(0,1)*I7a2232*Lam)/2.',
                   order = {'NP':1})

GC_1821 = Coupling(name = 'GC_1821',
                   value = '-(complex(0,1)*I7a2233*Lam)/4.',
                   order = {'NP':1})

GC_1822 = Coupling(name = 'GC_1822',
                   value = '(complex(0,1)*I7a2233*Lam)/2.',
                   order = {'NP':1})

GC_1823 = Coupling(name = 'GC_1823',
                   value = '-(complex(0,1)*I7a2311*Lam)/4.',
                   order = {'NP':1})

GC_1824 = Coupling(name = 'GC_1824',
                   value = '(complex(0,1)*I7a2311*Lam)/2.',
                   order = {'NP':1})

GC_1825 = Coupling(name = 'GC_1825',
                   value = '-(complex(0,1)*I7a2312*Lam)/4.',
                   order = {'NP':1})

GC_1826 = Coupling(name = 'GC_1826',
                   value = '(complex(0,1)*I7a2312*Lam)/2.',
                   order = {'NP':1})

GC_1827 = Coupling(name = 'GC_1827',
                   value = '-(complex(0,1)*I7a2313*Lam)/4.',
                   order = {'NP':1})

GC_1828 = Coupling(name = 'GC_1828',
                   value = '(complex(0,1)*I7a2313*Lam)/2.',
                   order = {'NP':1})

GC_1829 = Coupling(name = 'GC_1829',
                   value = '-(complex(0,1)*I7a2321*Lam)/4.',
                   order = {'NP':1})

GC_1830 = Coupling(name = 'GC_1830',
                   value = '(complex(0,1)*I7a2321*Lam)/2.',
                   order = {'NP':1})

GC_1831 = Coupling(name = 'GC_1831',
                   value = '-(complex(0,1)*I7a2322*Lam)/4.',
                   order = {'NP':1})

GC_1832 = Coupling(name = 'GC_1832',
                   value = '(complex(0,1)*I7a2322*Lam)/2.',
                   order = {'NP':1})

GC_1833 = Coupling(name = 'GC_1833',
                   value = '-(complex(0,1)*I7a2323*Lam)/4.',
                   order = {'NP':1})

GC_1834 = Coupling(name = 'GC_1834',
                   value = '(complex(0,1)*I7a2323*Lam)/2.',
                   order = {'NP':1})

GC_1835 = Coupling(name = 'GC_1835',
                   value = '-(complex(0,1)*I7a2331*Lam)/4.',
                   order = {'NP':1})

GC_1836 = Coupling(name = 'GC_1836',
                   value = '(complex(0,1)*I7a2331*Lam)/2.',
                   order = {'NP':1})

GC_1837 = Coupling(name = 'GC_1837',
                   value = '-(complex(0,1)*I7a2332*Lam)/4.',
                   order = {'NP':1})

GC_1838 = Coupling(name = 'GC_1838',
                   value = '(complex(0,1)*I7a2332*Lam)/2.',
                   order = {'NP':1})

GC_1839 = Coupling(name = 'GC_1839',
                   value = '-(complex(0,1)*I7a2333*Lam)/4.',
                   order = {'NP':1})

GC_1840 = Coupling(name = 'GC_1840',
                   value = '(complex(0,1)*I7a2333*Lam)/2.',
                   order = {'NP':1})

GC_1841 = Coupling(name = 'GC_1841',
                   value = '-(complex(0,1)*I7a3111*Lam)/4.',
                   order = {'NP':1})

GC_1842 = Coupling(name = 'GC_1842',
                   value = '(complex(0,1)*I7a3111*Lam)/2.',
                   order = {'NP':1})

GC_1843 = Coupling(name = 'GC_1843',
                   value = '-(complex(0,1)*I7a3112*Lam)/4.',
                   order = {'NP':1})

GC_1844 = Coupling(name = 'GC_1844',
                   value = '(complex(0,1)*I7a3112*Lam)/2.',
                   order = {'NP':1})

GC_1845 = Coupling(name = 'GC_1845',
                   value = '-(complex(0,1)*I7a3113*Lam)/4.',
                   order = {'NP':1})

GC_1846 = Coupling(name = 'GC_1846',
                   value = '(complex(0,1)*I7a3113*Lam)/2.',
                   order = {'NP':1})

GC_1847 = Coupling(name = 'GC_1847',
                   value = '-(complex(0,1)*I7a3121*Lam)/4.',
                   order = {'NP':1})

GC_1848 = Coupling(name = 'GC_1848',
                   value = '(complex(0,1)*I7a3121*Lam)/2.',
                   order = {'NP':1})

GC_1849 = Coupling(name = 'GC_1849',
                   value = '-(complex(0,1)*I7a3122*Lam)/4.',
                   order = {'NP':1})

GC_1850 = Coupling(name = 'GC_1850',
                   value = '(complex(0,1)*I7a3122*Lam)/2.',
                   order = {'NP':1})

GC_1851 = Coupling(name = 'GC_1851',
                   value = '-(complex(0,1)*I7a3123*Lam)/4.',
                   order = {'NP':1})

GC_1852 = Coupling(name = 'GC_1852',
                   value = '(complex(0,1)*I7a3123*Lam)/2.',
                   order = {'NP':1})

GC_1853 = Coupling(name = 'GC_1853',
                   value = '-(complex(0,1)*I7a3131*Lam)/4.',
                   order = {'NP':1})

GC_1854 = Coupling(name = 'GC_1854',
                   value = '(complex(0,1)*I7a3131*Lam)/2.',
                   order = {'NP':1})

GC_1855 = Coupling(name = 'GC_1855',
                   value = '-(complex(0,1)*I7a3132*Lam)/4.',
                   order = {'NP':1})

GC_1856 = Coupling(name = 'GC_1856',
                   value = '(complex(0,1)*I7a3132*Lam)/2.',
                   order = {'NP':1})

GC_1857 = Coupling(name = 'GC_1857',
                   value = '-(complex(0,1)*I7a3133*Lam)/4.',
                   order = {'NP':1})

GC_1858 = Coupling(name = 'GC_1858',
                   value = '(complex(0,1)*I7a3133*Lam)/2.',
                   order = {'NP':1})

GC_1859 = Coupling(name = 'GC_1859',
                   value = '-(complex(0,1)*I7a3211*Lam)/4.',
                   order = {'NP':1})

GC_1860 = Coupling(name = 'GC_1860',
                   value = '(complex(0,1)*I7a3211*Lam)/2.',
                   order = {'NP':1})

GC_1861 = Coupling(name = 'GC_1861',
                   value = '-(complex(0,1)*I7a3212*Lam)/4.',
                   order = {'NP':1})

GC_1862 = Coupling(name = 'GC_1862',
                   value = '(complex(0,1)*I7a3212*Lam)/2.',
                   order = {'NP':1})

GC_1863 = Coupling(name = 'GC_1863',
                   value = '-(complex(0,1)*I7a3213*Lam)/4.',
                   order = {'NP':1})

GC_1864 = Coupling(name = 'GC_1864',
                   value = '(complex(0,1)*I7a3213*Lam)/2.',
                   order = {'NP':1})

GC_1865 = Coupling(name = 'GC_1865',
                   value = '-(complex(0,1)*I7a3221*Lam)/4.',
                   order = {'NP':1})

GC_1866 = Coupling(name = 'GC_1866',
                   value = '(complex(0,1)*I7a3221*Lam)/2.',
                   order = {'NP':1})

GC_1867 = Coupling(name = 'GC_1867',
                   value = '-(complex(0,1)*I7a3222*Lam)/4.',
                   order = {'NP':1})

GC_1868 = Coupling(name = 'GC_1868',
                   value = '(complex(0,1)*I7a3222*Lam)/2.',
                   order = {'NP':1})

GC_1869 = Coupling(name = 'GC_1869',
                   value = '-(complex(0,1)*I7a3223*Lam)/4.',
                   order = {'NP':1})

GC_1870 = Coupling(name = 'GC_1870',
                   value = '(complex(0,1)*I7a3223*Lam)/2.',
                   order = {'NP':1})

GC_1871 = Coupling(name = 'GC_1871',
                   value = '-(complex(0,1)*I7a3231*Lam)/4.',
                   order = {'NP':1})

GC_1872 = Coupling(name = 'GC_1872',
                   value = '(complex(0,1)*I7a3231*Lam)/2.',
                   order = {'NP':1})

GC_1873 = Coupling(name = 'GC_1873',
                   value = '-(complex(0,1)*I7a3232*Lam)/4.',
                   order = {'NP':1})

GC_1874 = Coupling(name = 'GC_1874',
                   value = '(complex(0,1)*I7a3232*Lam)/2.',
                   order = {'NP':1})

GC_1875 = Coupling(name = 'GC_1875',
                   value = '-(complex(0,1)*I7a3233*Lam)/4.',
                   order = {'NP':1})

GC_1876 = Coupling(name = 'GC_1876',
                   value = '(complex(0,1)*I7a3233*Lam)/2.',
                   order = {'NP':1})

GC_1877 = Coupling(name = 'GC_1877',
                   value = '-(complex(0,1)*I7a3311*Lam)/4.',
                   order = {'NP':1})

GC_1878 = Coupling(name = 'GC_1878',
                   value = '(complex(0,1)*I7a3311*Lam)/2.',
                   order = {'NP':1})

GC_1879 = Coupling(name = 'GC_1879',
                   value = '-(complex(0,1)*I7a3312*Lam)/4.',
                   order = {'NP':1})

GC_1880 = Coupling(name = 'GC_1880',
                   value = '(complex(0,1)*I7a3312*Lam)/2.',
                   order = {'NP':1})

GC_1881 = Coupling(name = 'GC_1881',
                   value = '-(complex(0,1)*I7a3313*Lam)/4.',
                   order = {'NP':1})

GC_1882 = Coupling(name = 'GC_1882',
                   value = '(complex(0,1)*I7a3313*Lam)/2.',
                   order = {'NP':1})

GC_1883 = Coupling(name = 'GC_1883',
                   value = '-(complex(0,1)*I7a3321*Lam)/4.',
                   order = {'NP':1})

GC_1884 = Coupling(name = 'GC_1884',
                   value = '(complex(0,1)*I7a3321*Lam)/2.',
                   order = {'NP':1})

GC_1885 = Coupling(name = 'GC_1885',
                   value = '-(complex(0,1)*I7a3322*Lam)/4.',
                   order = {'NP':1})

GC_1886 = Coupling(name = 'GC_1886',
                   value = '(complex(0,1)*I7a3322*Lam)/2.',
                   order = {'NP':1})

GC_1887 = Coupling(name = 'GC_1887',
                   value = '-(complex(0,1)*I7a3323*Lam)/4.',
                   order = {'NP':1})

GC_1888 = Coupling(name = 'GC_1888',
                   value = '(complex(0,1)*I7a3323*Lam)/2.',
                   order = {'NP':1})

GC_1889 = Coupling(name = 'GC_1889',
                   value = '-(complex(0,1)*I7a3331*Lam)/4.',
                   order = {'NP':1})

GC_1890 = Coupling(name = 'GC_1890',
                   value = '(complex(0,1)*I7a3331*Lam)/2.',
                   order = {'NP':1})

GC_1891 = Coupling(name = 'GC_1891',
                   value = '-(complex(0,1)*I7a3332*Lam)/4.',
                   order = {'NP':1})

GC_1892 = Coupling(name = 'GC_1892',
                   value = '(complex(0,1)*I7a3332*Lam)/2.',
                   order = {'NP':1})

GC_1893 = Coupling(name = 'GC_1893',
                   value = '-(complex(0,1)*I7a3333*Lam)/4.',
                   order = {'NP':1})

GC_1894 = Coupling(name = 'GC_1894',
                   value = '(complex(0,1)*I7a3333*Lam)/2.',
                   order = {'NP':1})

GC_1895 = Coupling(name = 'GC_1895',
                   value = 'complex(0,1)*I8a1111*Lam',
                   order = {'NP':1})

GC_1896 = Coupling(name = 'GC_1896',
                   value = 'complex(0,1)*I8a1112*Lam',
                   order = {'NP':1})

GC_1897 = Coupling(name = 'GC_1897',
                   value = 'complex(0,1)*I8a1113*Lam',
                   order = {'NP':1})

GC_1898 = Coupling(name = 'GC_1898',
                   value = 'complex(0,1)*I8a1121*Lam',
                   order = {'NP':1})

GC_1899 = Coupling(name = 'GC_1899',
                   value = 'complex(0,1)*I8a1122*Lam',
                   order = {'NP':1})

GC_1900 = Coupling(name = 'GC_1900',
                   value = 'complex(0,1)*I8a1123*Lam',
                   order = {'NP':1})

GC_1901 = Coupling(name = 'GC_1901',
                   value = 'complex(0,1)*I8a1131*Lam',
                   order = {'NP':1})

GC_1902 = Coupling(name = 'GC_1902',
                   value = 'complex(0,1)*I8a1132*Lam',
                   order = {'NP':1})

GC_1903 = Coupling(name = 'GC_1903',
                   value = 'complex(0,1)*I8a1133*Lam',
                   order = {'NP':1})

GC_1904 = Coupling(name = 'GC_1904',
                   value = 'complex(0,1)*I8a1211*Lam',
                   order = {'NP':1})

GC_1905 = Coupling(name = 'GC_1905',
                   value = 'complex(0,1)*I8a1212*Lam',
                   order = {'NP':1})

GC_1906 = Coupling(name = 'GC_1906',
                   value = 'complex(0,1)*I8a1213*Lam',
                   order = {'NP':1})

GC_1907 = Coupling(name = 'GC_1907',
                   value = 'complex(0,1)*I8a1221*Lam',
                   order = {'NP':1})

GC_1908 = Coupling(name = 'GC_1908',
                   value = 'complex(0,1)*I8a1222*Lam',
                   order = {'NP':1})

GC_1909 = Coupling(name = 'GC_1909',
                   value = 'complex(0,1)*I8a1223*Lam',
                   order = {'NP':1})

GC_1910 = Coupling(name = 'GC_1910',
                   value = 'complex(0,1)*I8a1231*Lam',
                   order = {'NP':1})

GC_1911 = Coupling(name = 'GC_1911',
                   value = 'complex(0,1)*I8a1232*Lam',
                   order = {'NP':1})

GC_1912 = Coupling(name = 'GC_1912',
                   value = 'complex(0,1)*I8a1233*Lam',
                   order = {'NP':1})

GC_1913 = Coupling(name = 'GC_1913',
                   value = 'complex(0,1)*I8a1311*Lam',
                   order = {'NP':1})

GC_1914 = Coupling(name = 'GC_1914',
                   value = 'complex(0,1)*I8a1312*Lam',
                   order = {'NP':1})

GC_1915 = Coupling(name = 'GC_1915',
                   value = 'complex(0,1)*I8a1313*Lam',
                   order = {'NP':1})

GC_1916 = Coupling(name = 'GC_1916',
                   value = 'complex(0,1)*I8a1321*Lam',
                   order = {'NP':1})

GC_1917 = Coupling(name = 'GC_1917',
                   value = 'complex(0,1)*I8a1322*Lam',
                   order = {'NP':1})

GC_1918 = Coupling(name = 'GC_1918',
                   value = 'complex(0,1)*I8a1323*Lam',
                   order = {'NP':1})

GC_1919 = Coupling(name = 'GC_1919',
                   value = 'complex(0,1)*I8a1331*Lam',
                   order = {'NP':1})

GC_1920 = Coupling(name = 'GC_1920',
                   value = 'complex(0,1)*I8a1332*Lam',
                   order = {'NP':1})

GC_1921 = Coupling(name = 'GC_1921',
                   value = 'complex(0,1)*I8a1333*Lam',
                   order = {'NP':1})

GC_1922 = Coupling(name = 'GC_1922',
                   value = 'complex(0,1)*I8a2111*Lam',
                   order = {'NP':1})

GC_1923 = Coupling(name = 'GC_1923',
                   value = 'complex(0,1)*I8a2112*Lam',
                   order = {'NP':1})

GC_1924 = Coupling(name = 'GC_1924',
                   value = 'complex(0,1)*I8a2113*Lam',
                   order = {'NP':1})

GC_1925 = Coupling(name = 'GC_1925',
                   value = 'complex(0,1)*I8a2121*Lam',
                   order = {'NP':1})

GC_1926 = Coupling(name = 'GC_1926',
                   value = 'complex(0,1)*I8a2122*Lam',
                   order = {'NP':1})

GC_1927 = Coupling(name = 'GC_1927',
                   value = 'complex(0,1)*I8a2123*Lam',
                   order = {'NP':1})

GC_1928 = Coupling(name = 'GC_1928',
                   value = 'complex(0,1)*I8a2131*Lam',
                   order = {'NP':1})

GC_1929 = Coupling(name = 'GC_1929',
                   value = 'complex(0,1)*I8a2132*Lam',
                   order = {'NP':1})

GC_1930 = Coupling(name = 'GC_1930',
                   value = 'complex(0,1)*I8a2133*Lam',
                   order = {'NP':1})

GC_1931 = Coupling(name = 'GC_1931',
                   value = 'complex(0,1)*I8a2211*Lam',
                   order = {'NP':1})

GC_1932 = Coupling(name = 'GC_1932',
                   value = 'complex(0,1)*I8a2212*Lam',
                   order = {'NP':1})

GC_1933 = Coupling(name = 'GC_1933',
                   value = 'complex(0,1)*I8a2213*Lam',
                   order = {'NP':1})

GC_1934 = Coupling(name = 'GC_1934',
                   value = 'complex(0,1)*I8a2221*Lam',
                   order = {'NP':1})

GC_1935 = Coupling(name = 'GC_1935',
                   value = 'complex(0,1)*I8a2222*Lam',
                   order = {'NP':1})

GC_1936 = Coupling(name = 'GC_1936',
                   value = 'complex(0,1)*I8a2223*Lam',
                   order = {'NP':1})

GC_1937 = Coupling(name = 'GC_1937',
                   value = 'complex(0,1)*I8a2231*Lam',
                   order = {'NP':1})

GC_1938 = Coupling(name = 'GC_1938',
                   value = 'complex(0,1)*I8a2232*Lam',
                   order = {'NP':1})

GC_1939 = Coupling(name = 'GC_1939',
                   value = 'complex(0,1)*I8a2233*Lam',
                   order = {'NP':1})

GC_1940 = Coupling(name = 'GC_1940',
                   value = 'complex(0,1)*I8a2311*Lam',
                   order = {'NP':1})

GC_1941 = Coupling(name = 'GC_1941',
                   value = 'complex(0,1)*I8a2312*Lam',
                   order = {'NP':1})

GC_1942 = Coupling(name = 'GC_1942',
                   value = 'complex(0,1)*I8a2313*Lam',
                   order = {'NP':1})

GC_1943 = Coupling(name = 'GC_1943',
                   value = 'complex(0,1)*I8a2321*Lam',
                   order = {'NP':1})

GC_1944 = Coupling(name = 'GC_1944',
                   value = 'complex(0,1)*I8a2322*Lam',
                   order = {'NP':1})

GC_1945 = Coupling(name = 'GC_1945',
                   value = 'complex(0,1)*I8a2323*Lam',
                   order = {'NP':1})

GC_1946 = Coupling(name = 'GC_1946',
                   value = 'complex(0,1)*I8a2331*Lam',
                   order = {'NP':1})

GC_1947 = Coupling(name = 'GC_1947',
                   value = 'complex(0,1)*I8a2332*Lam',
                   order = {'NP':1})

GC_1948 = Coupling(name = 'GC_1948',
                   value = 'complex(0,1)*I8a2333*Lam',
                   order = {'NP':1})

GC_1949 = Coupling(name = 'GC_1949',
                   value = 'complex(0,1)*I8a3111*Lam',
                   order = {'NP':1})

GC_1950 = Coupling(name = 'GC_1950',
                   value = 'complex(0,1)*I8a3112*Lam',
                   order = {'NP':1})

GC_1951 = Coupling(name = 'GC_1951',
                   value = 'complex(0,1)*I8a3113*Lam',
                   order = {'NP':1})

GC_1952 = Coupling(name = 'GC_1952',
                   value = 'complex(0,1)*I8a3121*Lam',
                   order = {'NP':1})

GC_1953 = Coupling(name = 'GC_1953',
                   value = 'complex(0,1)*I8a3122*Lam',
                   order = {'NP':1})

GC_1954 = Coupling(name = 'GC_1954',
                   value = 'complex(0,1)*I8a3123*Lam',
                   order = {'NP':1})

GC_1955 = Coupling(name = 'GC_1955',
                   value = 'complex(0,1)*I8a3131*Lam',
                   order = {'NP':1})

GC_1956 = Coupling(name = 'GC_1956',
                   value = 'complex(0,1)*I8a3132*Lam',
                   order = {'NP':1})

GC_1957 = Coupling(name = 'GC_1957',
                   value = 'complex(0,1)*I8a3133*Lam',
                   order = {'NP':1})

GC_1958 = Coupling(name = 'GC_1958',
                   value = 'complex(0,1)*I8a3211*Lam',
                   order = {'NP':1})

GC_1959 = Coupling(name = 'GC_1959',
                   value = 'complex(0,1)*I8a3212*Lam',
                   order = {'NP':1})

GC_1960 = Coupling(name = 'GC_1960',
                   value = 'complex(0,1)*I8a3213*Lam',
                   order = {'NP':1})

GC_1961 = Coupling(name = 'GC_1961',
                   value = 'complex(0,1)*I8a3221*Lam',
                   order = {'NP':1})

GC_1962 = Coupling(name = 'GC_1962',
                   value = 'complex(0,1)*I8a3222*Lam',
                   order = {'NP':1})

GC_1963 = Coupling(name = 'GC_1963',
                   value = 'complex(0,1)*I8a3223*Lam',
                   order = {'NP':1})

GC_1964 = Coupling(name = 'GC_1964',
                   value = 'complex(0,1)*I8a3231*Lam',
                   order = {'NP':1})

GC_1965 = Coupling(name = 'GC_1965',
                   value = 'complex(0,1)*I8a3232*Lam',
                   order = {'NP':1})

GC_1966 = Coupling(name = 'GC_1966',
                   value = 'complex(0,1)*I8a3233*Lam',
                   order = {'NP':1})

GC_1967 = Coupling(name = 'GC_1967',
                   value = 'complex(0,1)*I8a3311*Lam',
                   order = {'NP':1})

GC_1968 = Coupling(name = 'GC_1968',
                   value = 'complex(0,1)*I8a3312*Lam',
                   order = {'NP':1})

GC_1969 = Coupling(name = 'GC_1969',
                   value = 'complex(0,1)*I8a3313*Lam',
                   order = {'NP':1})

GC_1970 = Coupling(name = 'GC_1970',
                   value = 'complex(0,1)*I8a3321*Lam',
                   order = {'NP':1})

GC_1971 = Coupling(name = 'GC_1971',
                   value = 'complex(0,1)*I8a3322*Lam',
                   order = {'NP':1})

GC_1972 = Coupling(name = 'GC_1972',
                   value = 'complex(0,1)*I8a3323*Lam',
                   order = {'NP':1})

GC_1973 = Coupling(name = 'GC_1973',
                   value = 'complex(0,1)*I8a3331*Lam',
                   order = {'NP':1})

GC_1974 = Coupling(name = 'GC_1974',
                   value = 'complex(0,1)*I8a3332*Lam',
                   order = {'NP':1})

GC_1975 = Coupling(name = 'GC_1975',
                   value = 'complex(0,1)*I8a3333*Lam',
                   order = {'NP':1})

GC_1976 = Coupling(name = 'GC_1976',
                   value = 'complex(0,1)*I9a1111*Lam',
                   order = {'NP':1})

GC_1977 = Coupling(name = 'GC_1977',
                   value = 'complex(0,1)*I9a1112*Lam',
                   order = {'NP':1})

GC_1978 = Coupling(name = 'GC_1978',
                   value = 'complex(0,1)*I9a1113*Lam',
                   order = {'NP':1})

GC_1979 = Coupling(name = 'GC_1979',
                   value = 'complex(0,1)*I9a1121*Lam',
                   order = {'NP':1})

GC_1980 = Coupling(name = 'GC_1980',
                   value = 'complex(0,1)*I9a1122*Lam',
                   order = {'NP':1})

GC_1981 = Coupling(name = 'GC_1981',
                   value = 'complex(0,1)*I9a1123*Lam',
                   order = {'NP':1})

GC_1982 = Coupling(name = 'GC_1982',
                   value = 'complex(0,1)*I9a1131*Lam',
                   order = {'NP':1})

GC_1983 = Coupling(name = 'GC_1983',
                   value = 'complex(0,1)*I9a1132*Lam',
                   order = {'NP':1})

GC_1984 = Coupling(name = 'GC_1984',
                   value = 'complex(0,1)*I9a1133*Lam',
                   order = {'NP':1})

GC_1985 = Coupling(name = 'GC_1985',
                   value = 'complex(0,1)*I9a1211*Lam',
                   order = {'NP':1})

GC_1986 = Coupling(name = 'GC_1986',
                   value = 'complex(0,1)*I9a1212*Lam',
                   order = {'NP':1})

GC_1987 = Coupling(name = 'GC_1987',
                   value = 'complex(0,1)*I9a1213*Lam',
                   order = {'NP':1})

GC_1988 = Coupling(name = 'GC_1988',
                   value = 'complex(0,1)*I9a1221*Lam',
                   order = {'NP':1})

GC_1989 = Coupling(name = 'GC_1989',
                   value = 'complex(0,1)*I9a1222*Lam',
                   order = {'NP':1})

GC_1990 = Coupling(name = 'GC_1990',
                   value = 'complex(0,1)*I9a1223*Lam',
                   order = {'NP':1})

GC_1991 = Coupling(name = 'GC_1991',
                   value = 'complex(0,1)*I9a1231*Lam',
                   order = {'NP':1})

GC_1992 = Coupling(name = 'GC_1992',
                   value = 'complex(0,1)*I9a1232*Lam',
                   order = {'NP':1})

GC_1993 = Coupling(name = 'GC_1993',
                   value = 'complex(0,1)*I9a1233*Lam',
                   order = {'NP':1})

GC_1994 = Coupling(name = 'GC_1994',
                   value = 'complex(0,1)*I9a1311*Lam',
                   order = {'NP':1})

GC_1995 = Coupling(name = 'GC_1995',
                   value = 'complex(0,1)*I9a1312*Lam',
                   order = {'NP':1})

GC_1996 = Coupling(name = 'GC_1996',
                   value = 'complex(0,1)*I9a1313*Lam',
                   order = {'NP':1})

GC_1997 = Coupling(name = 'GC_1997',
                   value = 'complex(0,1)*I9a1321*Lam',
                   order = {'NP':1})

GC_1998 = Coupling(name = 'GC_1998',
                   value = 'complex(0,1)*I9a1322*Lam',
                   order = {'NP':1})

GC_1999 = Coupling(name = 'GC_1999',
                   value = 'complex(0,1)*I9a1323*Lam',
                   order = {'NP':1})

GC_2000 = Coupling(name = 'GC_2000',
                   value = 'complex(0,1)*I9a1331*Lam',
                   order = {'NP':1})

GC_2001 = Coupling(name = 'GC_2001',
                   value = 'complex(0,1)*I9a1332*Lam',
                   order = {'NP':1})

GC_2002 = Coupling(name = 'GC_2002',
                   value = 'complex(0,1)*I9a1333*Lam',
                   order = {'NP':1})

GC_2003 = Coupling(name = 'GC_2003',
                   value = 'complex(0,1)*I9a2111*Lam',
                   order = {'NP':1})

GC_2004 = Coupling(name = 'GC_2004',
                   value = 'complex(0,1)*I9a2112*Lam',
                   order = {'NP':1})

GC_2005 = Coupling(name = 'GC_2005',
                   value = 'complex(0,1)*I9a2113*Lam',
                   order = {'NP':1})

GC_2006 = Coupling(name = 'GC_2006',
                   value = 'complex(0,1)*I9a2121*Lam',
                   order = {'NP':1})

GC_2007 = Coupling(name = 'GC_2007',
                   value = 'complex(0,1)*I9a2122*Lam',
                   order = {'NP':1})

GC_2008 = Coupling(name = 'GC_2008',
                   value = 'complex(0,1)*I9a2123*Lam',
                   order = {'NP':1})

GC_2009 = Coupling(name = 'GC_2009',
                   value = 'complex(0,1)*I9a2131*Lam',
                   order = {'NP':1})

GC_2010 = Coupling(name = 'GC_2010',
                   value = 'complex(0,1)*I9a2132*Lam',
                   order = {'NP':1})

GC_2011 = Coupling(name = 'GC_2011',
                   value = 'complex(0,1)*I9a2133*Lam',
                   order = {'NP':1})

GC_2012 = Coupling(name = 'GC_2012',
                   value = 'complex(0,1)*I9a2211*Lam',
                   order = {'NP':1})

GC_2013 = Coupling(name = 'GC_2013',
                   value = 'complex(0,1)*I9a2212*Lam',
                   order = {'NP':1})

GC_2014 = Coupling(name = 'GC_2014',
                   value = 'complex(0,1)*I9a2213*Lam',
                   order = {'NP':1})

GC_2015 = Coupling(name = 'GC_2015',
                   value = 'complex(0,1)*I9a2221*Lam',
                   order = {'NP':1})

GC_2016 = Coupling(name = 'GC_2016',
                   value = 'complex(0,1)*I9a2222*Lam',
                   order = {'NP':1})

GC_2017 = Coupling(name = 'GC_2017',
                   value = 'complex(0,1)*I9a2223*Lam',
                   order = {'NP':1})

GC_2018 = Coupling(name = 'GC_2018',
                   value = 'complex(0,1)*I9a2231*Lam',
                   order = {'NP':1})

GC_2019 = Coupling(name = 'GC_2019',
                   value = 'complex(0,1)*I9a2232*Lam',
                   order = {'NP':1})

GC_2020 = Coupling(name = 'GC_2020',
                   value = 'complex(0,1)*I9a2233*Lam',
                   order = {'NP':1})

GC_2021 = Coupling(name = 'GC_2021',
                   value = 'complex(0,1)*I9a2311*Lam',
                   order = {'NP':1})

GC_2022 = Coupling(name = 'GC_2022',
                   value = 'complex(0,1)*I9a2312*Lam',
                   order = {'NP':1})

GC_2023 = Coupling(name = 'GC_2023',
                   value = 'complex(0,1)*I9a2313*Lam',
                   order = {'NP':1})

GC_2024 = Coupling(name = 'GC_2024',
                   value = 'complex(0,1)*I9a2321*Lam',
                   order = {'NP':1})

GC_2025 = Coupling(name = 'GC_2025',
                   value = 'complex(0,1)*I9a2322*Lam',
                   order = {'NP':1})

GC_2026 = Coupling(name = 'GC_2026',
                   value = 'complex(0,1)*I9a2323*Lam',
                   order = {'NP':1})

GC_2027 = Coupling(name = 'GC_2027',
                   value = 'complex(0,1)*I9a2331*Lam',
                   order = {'NP':1})

GC_2028 = Coupling(name = 'GC_2028',
                   value = 'complex(0,1)*I9a2332*Lam',
                   order = {'NP':1})

GC_2029 = Coupling(name = 'GC_2029',
                   value = 'complex(0,1)*I9a2333*Lam',
                   order = {'NP':1})

GC_2030 = Coupling(name = 'GC_2030',
                   value = 'complex(0,1)*I9a3111*Lam',
                   order = {'NP':1})

GC_2031 = Coupling(name = 'GC_2031',
                   value = 'complex(0,1)*I9a3112*Lam',
                   order = {'NP':1})

GC_2032 = Coupling(name = 'GC_2032',
                   value = 'complex(0,1)*I9a3113*Lam',
                   order = {'NP':1})

GC_2033 = Coupling(name = 'GC_2033',
                   value = 'complex(0,1)*I9a3121*Lam',
                   order = {'NP':1})

GC_2034 = Coupling(name = 'GC_2034',
                   value = 'complex(0,1)*I9a3122*Lam',
                   order = {'NP':1})

GC_2035 = Coupling(name = 'GC_2035',
                   value = 'complex(0,1)*I9a3123*Lam',
                   order = {'NP':1})

GC_2036 = Coupling(name = 'GC_2036',
                   value = 'complex(0,1)*I9a3131*Lam',
                   order = {'NP':1})

GC_2037 = Coupling(name = 'GC_2037',
                   value = 'complex(0,1)*I9a3132*Lam',
                   order = {'NP':1})

GC_2038 = Coupling(name = 'GC_2038',
                   value = 'complex(0,1)*I9a3133*Lam',
                   order = {'NP':1})

GC_2039 = Coupling(name = 'GC_2039',
                   value = 'complex(0,1)*I9a3211*Lam',
                   order = {'NP':1})

GC_2040 = Coupling(name = 'GC_2040',
                   value = 'complex(0,1)*I9a3212*Lam',
                   order = {'NP':1})

GC_2041 = Coupling(name = 'GC_2041',
                   value = 'complex(0,1)*I9a3213*Lam',
                   order = {'NP':1})

GC_2042 = Coupling(name = 'GC_2042',
                   value = 'complex(0,1)*I9a3221*Lam',
                   order = {'NP':1})

GC_2043 = Coupling(name = 'GC_2043',
                   value = 'complex(0,1)*I9a3222*Lam',
                   order = {'NP':1})

GC_2044 = Coupling(name = 'GC_2044',
                   value = 'complex(0,1)*I9a3223*Lam',
                   order = {'NP':1})

GC_2045 = Coupling(name = 'GC_2045',
                   value = 'complex(0,1)*I9a3231*Lam',
                   order = {'NP':1})

GC_2046 = Coupling(name = 'GC_2046',
                   value = 'complex(0,1)*I9a3232*Lam',
                   order = {'NP':1})

GC_2047 = Coupling(name = 'GC_2047',
                   value = 'complex(0,1)*I9a3233*Lam',
                   order = {'NP':1})

GC_2048 = Coupling(name = 'GC_2048',
                   value = 'complex(0,1)*I9a3311*Lam',
                   order = {'NP':1})

GC_2049 = Coupling(name = 'GC_2049',
                   value = 'complex(0,1)*I9a3312*Lam',
                   order = {'NP':1})

GC_2050 = Coupling(name = 'GC_2050',
                   value = 'complex(0,1)*I9a3313*Lam',
                   order = {'NP':1})

GC_2051 = Coupling(name = 'GC_2051',
                   value = 'complex(0,1)*I9a3321*Lam',
                   order = {'NP':1})

GC_2052 = Coupling(name = 'GC_2052',
                   value = 'complex(0,1)*I9a3322*Lam',
                   order = {'NP':1})

GC_2053 = Coupling(name = 'GC_2053',
                   value = 'complex(0,1)*I9a3323*Lam',
                   order = {'NP':1})

GC_2054 = Coupling(name = 'GC_2054',
                   value = 'complex(0,1)*I9a3331*Lam',
                   order = {'NP':1})

GC_2055 = Coupling(name = 'GC_2055',
                   value = 'complex(0,1)*I9a3332*Lam',
                   order = {'NP':1})

GC_2056 = Coupling(name = 'GC_2056',
                   value = 'complex(0,1)*I9a3333*Lam',
                   order = {'NP':1})

GC_2057 = Coupling(name = 'GC_2057',
                   value = 'Clq11x1x1x1*complex(0,1)*Lam + Clq31x1x1x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2058 = Coupling(name = 'GC_2058',
                   value = 'Clq11x1x1x2*complex(0,1)*Lam + Clq31x1x1x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2059 = Coupling(name = 'GC_2059',
                   value = 'Clq11x1x1x3*complex(0,1)*Lam + Clq31x1x1x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2060 = Coupling(name = 'GC_2060',
                   value = 'Clq11x1x2x1*complex(0,1)*Lam + Clq31x1x2x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2061 = Coupling(name = 'GC_2061',
                   value = 'Clq11x1x2x2*complex(0,1)*Lam + Clq31x1x2x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2062 = Coupling(name = 'GC_2062',
                   value = 'Clq11x1x2x3*complex(0,1)*Lam + Clq31x1x2x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2063 = Coupling(name = 'GC_2063',
                   value = 'Clq11x1x3x1*complex(0,1)*Lam + Clq31x1x3x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2064 = Coupling(name = 'GC_2064',
                   value = 'Clq11x1x3x2*complex(0,1)*Lam + Clq31x1x3x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2065 = Coupling(name = 'GC_2065',
                   value = 'Clq11x1x3x3*complex(0,1)*Lam + Clq31x1x3x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2066 = Coupling(name = 'GC_2066',
                   value = 'Clq11x2x1x1*complex(0,1)*Lam + Clq31x2x1x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2067 = Coupling(name = 'GC_2067',
                   value = 'Clq11x2x1x2*complex(0,1)*Lam + Clq31x2x1x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2068 = Coupling(name = 'GC_2068',
                   value = 'Clq11x2x1x3*complex(0,1)*Lam + Clq31x2x1x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2069 = Coupling(name = 'GC_2069',
                   value = 'Clq11x2x2x1*complex(0,1)*Lam + Clq31x2x2x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2070 = Coupling(name = 'GC_2070',
                   value = 'Clq11x2x2x2*complex(0,1)*Lam + Clq31x2x2x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2071 = Coupling(name = 'GC_2071',
                   value = 'Clq11x2x2x3*complex(0,1)*Lam + Clq31x2x2x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2072 = Coupling(name = 'GC_2072',
                   value = 'Clq11x2x3x1*complex(0,1)*Lam + Clq31x2x3x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2073 = Coupling(name = 'GC_2073',
                   value = 'Clq11x2x3x2*complex(0,1)*Lam + Clq31x2x3x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2074 = Coupling(name = 'GC_2074',
                   value = 'Clq11x2x3x3*complex(0,1)*Lam + Clq31x2x3x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2075 = Coupling(name = 'GC_2075',
                   value = 'Clq11x3x1x1*complex(0,1)*Lam + Clq31x3x1x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2076 = Coupling(name = 'GC_2076',
                   value = 'Clq11x3x1x2*complex(0,1)*Lam + Clq31x3x1x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2077 = Coupling(name = 'GC_2077',
                   value = 'Clq11x3x1x3*complex(0,1)*Lam + Clq31x3x1x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2078 = Coupling(name = 'GC_2078',
                   value = 'Clq11x3x2x1*complex(0,1)*Lam + Clq31x3x2x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2079 = Coupling(name = 'GC_2079',
                   value = 'Clq11x3x2x2*complex(0,1)*Lam + Clq31x3x2x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2080 = Coupling(name = 'GC_2080',
                   value = 'Clq11x3x2x3*complex(0,1)*Lam + Clq31x3x2x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2081 = Coupling(name = 'GC_2081',
                   value = 'Clq11x3x3x1*complex(0,1)*Lam + Clq31x3x3x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2082 = Coupling(name = 'GC_2082',
                   value = 'Clq11x3x3x2*complex(0,1)*Lam + Clq31x3x3x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2083 = Coupling(name = 'GC_2083',
                   value = 'Clq11x3x3x3*complex(0,1)*Lam + Clq31x3x3x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2084 = Coupling(name = 'GC_2084',
                   value = 'Clq12x1x1x1*complex(0,1)*Lam + Clq32x1x1x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2085 = Coupling(name = 'GC_2085',
                   value = 'Clq12x1x1x2*complex(0,1)*Lam + Clq32x1x1x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2086 = Coupling(name = 'GC_2086',
                   value = 'Clq12x1x1x3*complex(0,1)*Lam + Clq32x1x1x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2087 = Coupling(name = 'GC_2087',
                   value = 'Clq12x1x2x1*complex(0,1)*Lam + Clq32x1x2x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2088 = Coupling(name = 'GC_2088',
                   value = 'Clq12x1x2x2*complex(0,1)*Lam + Clq32x1x2x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2089 = Coupling(name = 'GC_2089',
                   value = 'Clq12x1x2x3*complex(0,1)*Lam + Clq32x1x2x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2090 = Coupling(name = 'GC_2090',
                   value = 'Clq12x1x3x1*complex(0,1)*Lam + Clq32x1x3x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2091 = Coupling(name = 'GC_2091',
                   value = 'Clq12x1x3x2*complex(0,1)*Lam + Clq32x1x3x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2092 = Coupling(name = 'GC_2092',
                   value = 'Clq12x1x3x3*complex(0,1)*Lam + Clq32x1x3x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2093 = Coupling(name = 'GC_2093',
                   value = 'Clq12x2x1x1*complex(0,1)*Lam + Clq32x2x1x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2094 = Coupling(name = 'GC_2094',
                   value = 'Clq12x2x1x2*complex(0,1)*Lam + Clq32x2x1x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2095 = Coupling(name = 'GC_2095',
                   value = 'Clq12x2x1x3*complex(0,1)*Lam + Clq32x2x1x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2096 = Coupling(name = 'GC_2096',
                   value = 'Clq12x2x2x1*complex(0,1)*Lam + Clq32x2x2x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2097 = Coupling(name = 'GC_2097',
                   value = 'Clq12x2x2x2*complex(0,1)*Lam + Clq32x2x2x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2098 = Coupling(name = 'GC_2098',
                   value = 'Clq12x2x2x3*complex(0,1)*Lam + Clq32x2x2x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2099 = Coupling(name = 'GC_2099',
                   value = 'Clq12x2x3x1*complex(0,1)*Lam + Clq32x2x3x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2100 = Coupling(name = 'GC_2100',
                   value = 'Clq12x2x3x2*complex(0,1)*Lam + Clq32x2x3x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2101 = Coupling(name = 'GC_2101',
                   value = 'Clq12x2x3x3*complex(0,1)*Lam + Clq32x2x3x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2102 = Coupling(name = 'GC_2102',
                   value = 'Clq12x3x1x1*complex(0,1)*Lam + Clq32x3x1x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2103 = Coupling(name = 'GC_2103',
                   value = 'Clq12x3x1x2*complex(0,1)*Lam + Clq32x3x1x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2104 = Coupling(name = 'GC_2104',
                   value = 'Clq12x3x1x3*complex(0,1)*Lam + Clq32x3x1x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2105 = Coupling(name = 'GC_2105',
                   value = 'Clq12x3x2x1*complex(0,1)*Lam + Clq32x3x2x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2106 = Coupling(name = 'GC_2106',
                   value = 'Clq12x3x2x2*complex(0,1)*Lam + Clq32x3x2x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2107 = Coupling(name = 'GC_2107',
                   value = 'Clq12x3x2x3*complex(0,1)*Lam + Clq32x3x2x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2108 = Coupling(name = 'GC_2108',
                   value = 'Clq12x3x3x1*complex(0,1)*Lam + Clq32x3x3x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2109 = Coupling(name = 'GC_2109',
                   value = 'Clq12x3x3x2*complex(0,1)*Lam + Clq32x3x3x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2110 = Coupling(name = 'GC_2110',
                   value = 'Clq12x3x3x3*complex(0,1)*Lam + Clq32x3x3x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2111 = Coupling(name = 'GC_2111',
                   value = 'Clq13x1x1x1*complex(0,1)*Lam + Clq33x1x1x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2112 = Coupling(name = 'GC_2112',
                   value = 'Clq13x1x1x2*complex(0,1)*Lam + Clq33x1x1x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2113 = Coupling(name = 'GC_2113',
                   value = 'Clq13x1x1x3*complex(0,1)*Lam + Clq33x1x1x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2114 = Coupling(name = 'GC_2114',
                   value = 'Clq13x1x2x1*complex(0,1)*Lam + Clq33x1x2x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2115 = Coupling(name = 'GC_2115',
                   value = 'Clq13x1x2x2*complex(0,1)*Lam + Clq33x1x2x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2116 = Coupling(name = 'GC_2116',
                   value = 'Clq13x1x2x3*complex(0,1)*Lam + Clq33x1x2x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2117 = Coupling(name = 'GC_2117',
                   value = 'Clq13x1x3x1*complex(0,1)*Lam + Clq33x1x3x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2118 = Coupling(name = 'GC_2118',
                   value = 'Clq13x1x3x2*complex(0,1)*Lam + Clq33x1x3x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2119 = Coupling(name = 'GC_2119',
                   value = 'Clq13x1x3x3*complex(0,1)*Lam + Clq33x1x3x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2120 = Coupling(name = 'GC_2120',
                   value = 'Clq13x2x1x1*complex(0,1)*Lam + Clq33x2x1x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2121 = Coupling(name = 'GC_2121',
                   value = 'Clq13x2x1x2*complex(0,1)*Lam + Clq33x2x1x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2122 = Coupling(name = 'GC_2122',
                   value = 'Clq13x2x1x3*complex(0,1)*Lam + Clq33x2x1x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2123 = Coupling(name = 'GC_2123',
                   value = 'Clq13x2x2x1*complex(0,1)*Lam + Clq33x2x2x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2124 = Coupling(name = 'GC_2124',
                   value = 'Clq13x2x2x2*complex(0,1)*Lam + Clq33x2x2x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2125 = Coupling(name = 'GC_2125',
                   value = 'Clq13x2x2x3*complex(0,1)*Lam + Clq33x2x2x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2126 = Coupling(name = 'GC_2126',
                   value = 'Clq13x2x3x1*complex(0,1)*Lam + Clq33x2x3x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2127 = Coupling(name = 'GC_2127',
                   value = 'Clq13x2x3x2*complex(0,1)*Lam + Clq33x2x3x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2128 = Coupling(name = 'GC_2128',
                   value = 'Clq13x2x3x3*complex(0,1)*Lam + Clq33x2x3x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2129 = Coupling(name = 'GC_2129',
                   value = 'Clq13x3x1x1*complex(0,1)*Lam + Clq33x3x1x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2130 = Coupling(name = 'GC_2130',
                   value = 'Clq13x3x1x2*complex(0,1)*Lam + Clq33x3x1x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2131 = Coupling(name = 'GC_2131',
                   value = 'Clq13x3x1x3*complex(0,1)*Lam + Clq33x3x1x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2132 = Coupling(name = 'GC_2132',
                   value = 'Clq13x3x2x1*complex(0,1)*Lam + Clq33x3x2x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2133 = Coupling(name = 'GC_2133',
                   value = 'Clq13x3x2x2*complex(0,1)*Lam + Clq33x3x2x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2134 = Coupling(name = 'GC_2134',
                   value = 'Clq13x3x2x3*complex(0,1)*Lam + Clq33x3x2x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2135 = Coupling(name = 'GC_2135',
                   value = 'Clq13x3x3x1*complex(0,1)*Lam + Clq33x3x3x1*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2136 = Coupling(name = 'GC_2136',
                   value = 'Clq13x3x3x2*complex(0,1)*Lam + Clq33x3x3x2*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2137 = Coupling(name = 'GC_2137',
                   value = 'Clq13x3x3x3*complex(0,1)*Lam + Clq33x3x3x3*complex(0,1)*Lam',
                   order = {'NP':1})

GC_2138 = Coupling(name = 'GC_2138',
                   value = 'complex(0,1)*I16a1111*Lam - complex(0,1)*I17a1111*Lam',
                   order = {'NP':1})

GC_2139 = Coupling(name = 'GC_2139',
                   value = 'complex(0,1)*I16a1112*Lam - complex(0,1)*I17a1112*Lam',
                   order = {'NP':1})

GC_2140 = Coupling(name = 'GC_2140',
                   value = 'complex(0,1)*I16a1113*Lam - complex(0,1)*I17a1113*Lam',
                   order = {'NP':1})

GC_2141 = Coupling(name = 'GC_2141',
                   value = 'complex(0,1)*I16a1121*Lam - complex(0,1)*I17a1121*Lam',
                   order = {'NP':1})

GC_2142 = Coupling(name = 'GC_2142',
                   value = 'complex(0,1)*I16a1122*Lam - complex(0,1)*I17a1122*Lam',
                   order = {'NP':1})

GC_2143 = Coupling(name = 'GC_2143',
                   value = 'complex(0,1)*I16a1123*Lam - complex(0,1)*I17a1123*Lam',
                   order = {'NP':1})

GC_2144 = Coupling(name = 'GC_2144',
                   value = 'complex(0,1)*I16a1131*Lam - complex(0,1)*I17a1131*Lam',
                   order = {'NP':1})

GC_2145 = Coupling(name = 'GC_2145',
                   value = 'complex(0,1)*I16a1132*Lam - complex(0,1)*I17a1132*Lam',
                   order = {'NP':1})

GC_2146 = Coupling(name = 'GC_2146',
                   value = 'complex(0,1)*I16a1133*Lam - complex(0,1)*I17a1133*Lam',
                   order = {'NP':1})

GC_2147 = Coupling(name = 'GC_2147',
                   value = 'complex(0,1)*I16a1211*Lam - complex(0,1)*I17a1211*Lam',
                   order = {'NP':1})

GC_2148 = Coupling(name = 'GC_2148',
                   value = 'complex(0,1)*I16a1212*Lam - complex(0,1)*I17a1212*Lam',
                   order = {'NP':1})

GC_2149 = Coupling(name = 'GC_2149',
                   value = 'complex(0,1)*I16a1213*Lam - complex(0,1)*I17a1213*Lam',
                   order = {'NP':1})

GC_2150 = Coupling(name = 'GC_2150',
                   value = 'complex(0,1)*I16a1221*Lam - complex(0,1)*I17a1221*Lam',
                   order = {'NP':1})

GC_2151 = Coupling(name = 'GC_2151',
                   value = 'complex(0,1)*I16a1222*Lam - complex(0,1)*I17a1222*Lam',
                   order = {'NP':1})

GC_2152 = Coupling(name = 'GC_2152',
                   value = 'complex(0,1)*I16a1223*Lam - complex(0,1)*I17a1223*Lam',
                   order = {'NP':1})

GC_2153 = Coupling(name = 'GC_2153',
                   value = 'complex(0,1)*I16a1231*Lam - complex(0,1)*I17a1231*Lam',
                   order = {'NP':1})

GC_2154 = Coupling(name = 'GC_2154',
                   value = 'complex(0,1)*I16a1232*Lam - complex(0,1)*I17a1232*Lam',
                   order = {'NP':1})

GC_2155 = Coupling(name = 'GC_2155',
                   value = 'complex(0,1)*I16a1233*Lam - complex(0,1)*I17a1233*Lam',
                   order = {'NP':1})

GC_2156 = Coupling(name = 'GC_2156',
                   value = 'complex(0,1)*I16a1311*Lam - complex(0,1)*I17a1311*Lam',
                   order = {'NP':1})

GC_2157 = Coupling(name = 'GC_2157',
                   value = 'complex(0,1)*I16a1312*Lam - complex(0,1)*I17a1312*Lam',
                   order = {'NP':1})

GC_2158 = Coupling(name = 'GC_2158',
                   value = 'complex(0,1)*I16a1313*Lam - complex(0,1)*I17a1313*Lam',
                   order = {'NP':1})

GC_2159 = Coupling(name = 'GC_2159',
                   value = 'complex(0,1)*I16a1321*Lam - complex(0,1)*I17a1321*Lam',
                   order = {'NP':1})

GC_2160 = Coupling(name = 'GC_2160',
                   value = 'complex(0,1)*I16a1322*Lam - complex(0,1)*I17a1322*Lam',
                   order = {'NP':1})

GC_2161 = Coupling(name = 'GC_2161',
                   value = 'complex(0,1)*I16a1323*Lam - complex(0,1)*I17a1323*Lam',
                   order = {'NP':1})

GC_2162 = Coupling(name = 'GC_2162',
                   value = 'complex(0,1)*I16a1331*Lam - complex(0,1)*I17a1331*Lam',
                   order = {'NP':1})

GC_2163 = Coupling(name = 'GC_2163',
                   value = 'complex(0,1)*I16a1332*Lam - complex(0,1)*I17a1332*Lam',
                   order = {'NP':1})

GC_2164 = Coupling(name = 'GC_2164',
                   value = 'complex(0,1)*I16a1333*Lam - complex(0,1)*I17a1333*Lam',
                   order = {'NP':1})

GC_2165 = Coupling(name = 'GC_2165',
                   value = 'complex(0,1)*I16a2111*Lam - complex(0,1)*I17a2111*Lam',
                   order = {'NP':1})

GC_2166 = Coupling(name = 'GC_2166',
                   value = 'complex(0,1)*I16a2112*Lam - complex(0,1)*I17a2112*Lam',
                   order = {'NP':1})

GC_2167 = Coupling(name = 'GC_2167',
                   value = 'complex(0,1)*I16a2113*Lam - complex(0,1)*I17a2113*Lam',
                   order = {'NP':1})

GC_2168 = Coupling(name = 'GC_2168',
                   value = 'complex(0,1)*I16a2121*Lam - complex(0,1)*I17a2121*Lam',
                   order = {'NP':1})

GC_2169 = Coupling(name = 'GC_2169',
                   value = 'complex(0,1)*I16a2122*Lam - complex(0,1)*I17a2122*Lam',
                   order = {'NP':1})

GC_2170 = Coupling(name = 'GC_2170',
                   value = 'complex(0,1)*I16a2123*Lam - complex(0,1)*I17a2123*Lam',
                   order = {'NP':1})

GC_2171 = Coupling(name = 'GC_2171',
                   value = 'complex(0,1)*I16a2131*Lam - complex(0,1)*I17a2131*Lam',
                   order = {'NP':1})

GC_2172 = Coupling(name = 'GC_2172',
                   value = 'complex(0,1)*I16a2132*Lam - complex(0,1)*I17a2132*Lam',
                   order = {'NP':1})

GC_2173 = Coupling(name = 'GC_2173',
                   value = 'complex(0,1)*I16a2133*Lam - complex(0,1)*I17a2133*Lam',
                   order = {'NP':1})

GC_2174 = Coupling(name = 'GC_2174',
                   value = 'complex(0,1)*I16a2211*Lam - complex(0,1)*I17a2211*Lam',
                   order = {'NP':1})

GC_2175 = Coupling(name = 'GC_2175',
                   value = 'complex(0,1)*I16a2212*Lam - complex(0,1)*I17a2212*Lam',
                   order = {'NP':1})

GC_2176 = Coupling(name = 'GC_2176',
                   value = 'complex(0,1)*I16a2213*Lam - complex(0,1)*I17a2213*Lam',
                   order = {'NP':1})

GC_2177 = Coupling(name = 'GC_2177',
                   value = 'complex(0,1)*I16a2221*Lam - complex(0,1)*I17a2221*Lam',
                   order = {'NP':1})

GC_2178 = Coupling(name = 'GC_2178',
                   value = 'complex(0,1)*I16a2222*Lam - complex(0,1)*I17a2222*Lam',
                   order = {'NP':1})

GC_2179 = Coupling(name = 'GC_2179',
                   value = 'complex(0,1)*I16a2223*Lam - complex(0,1)*I17a2223*Lam',
                   order = {'NP':1})

GC_2180 = Coupling(name = 'GC_2180',
                   value = 'complex(0,1)*I16a2231*Lam - complex(0,1)*I17a2231*Lam',
                   order = {'NP':1})

GC_2181 = Coupling(name = 'GC_2181',
                   value = 'complex(0,1)*I16a2232*Lam - complex(0,1)*I17a2232*Lam',
                   order = {'NP':1})

GC_2182 = Coupling(name = 'GC_2182',
                   value = 'complex(0,1)*I16a2233*Lam - complex(0,1)*I17a2233*Lam',
                   order = {'NP':1})

GC_2183 = Coupling(name = 'GC_2183',
                   value = 'complex(0,1)*I16a2311*Lam - complex(0,1)*I17a2311*Lam',
                   order = {'NP':1})

GC_2184 = Coupling(name = 'GC_2184',
                   value = 'complex(0,1)*I16a2312*Lam - complex(0,1)*I17a2312*Lam',
                   order = {'NP':1})

GC_2185 = Coupling(name = 'GC_2185',
                   value = 'complex(0,1)*I16a2313*Lam - complex(0,1)*I17a2313*Lam',
                   order = {'NP':1})

GC_2186 = Coupling(name = 'GC_2186',
                   value = 'complex(0,1)*I16a2321*Lam - complex(0,1)*I17a2321*Lam',
                   order = {'NP':1})

GC_2187 = Coupling(name = 'GC_2187',
                   value = 'complex(0,1)*I16a2322*Lam - complex(0,1)*I17a2322*Lam',
                   order = {'NP':1})

GC_2188 = Coupling(name = 'GC_2188',
                   value = 'complex(0,1)*I16a2323*Lam - complex(0,1)*I17a2323*Lam',
                   order = {'NP':1})

GC_2189 = Coupling(name = 'GC_2189',
                   value = 'complex(0,1)*I16a2331*Lam - complex(0,1)*I17a2331*Lam',
                   order = {'NP':1})

GC_2190 = Coupling(name = 'GC_2190',
                   value = 'complex(0,1)*I16a2332*Lam - complex(0,1)*I17a2332*Lam',
                   order = {'NP':1})

GC_2191 = Coupling(name = 'GC_2191',
                   value = 'complex(0,1)*I16a2333*Lam - complex(0,1)*I17a2333*Lam',
                   order = {'NP':1})

GC_2192 = Coupling(name = 'GC_2192',
                   value = 'complex(0,1)*I16a3111*Lam - complex(0,1)*I17a3111*Lam',
                   order = {'NP':1})

GC_2193 = Coupling(name = 'GC_2193',
                   value = 'complex(0,1)*I16a3112*Lam - complex(0,1)*I17a3112*Lam',
                   order = {'NP':1})

GC_2194 = Coupling(name = 'GC_2194',
                   value = 'complex(0,1)*I16a3113*Lam - complex(0,1)*I17a3113*Lam',
                   order = {'NP':1})

GC_2195 = Coupling(name = 'GC_2195',
                   value = 'complex(0,1)*I16a3121*Lam - complex(0,1)*I17a3121*Lam',
                   order = {'NP':1})

GC_2196 = Coupling(name = 'GC_2196',
                   value = 'complex(0,1)*I16a3122*Lam - complex(0,1)*I17a3122*Lam',
                   order = {'NP':1})

GC_2197 = Coupling(name = 'GC_2197',
                   value = 'complex(0,1)*I16a3123*Lam - complex(0,1)*I17a3123*Lam',
                   order = {'NP':1})

GC_2198 = Coupling(name = 'GC_2198',
                   value = 'complex(0,1)*I16a3131*Lam - complex(0,1)*I17a3131*Lam',
                   order = {'NP':1})

GC_2199 = Coupling(name = 'GC_2199',
                   value = 'complex(0,1)*I16a3132*Lam - complex(0,1)*I17a3132*Lam',
                   order = {'NP':1})

GC_2200 = Coupling(name = 'GC_2200',
                   value = 'complex(0,1)*I16a3133*Lam - complex(0,1)*I17a3133*Lam',
                   order = {'NP':1})

GC_2201 = Coupling(name = 'GC_2201',
                   value = 'complex(0,1)*I16a3211*Lam - complex(0,1)*I17a3211*Lam',
                   order = {'NP':1})

GC_2202 = Coupling(name = 'GC_2202',
                   value = 'complex(0,1)*I16a3212*Lam - complex(0,1)*I17a3212*Lam',
                   order = {'NP':1})

GC_2203 = Coupling(name = 'GC_2203',
                   value = 'complex(0,1)*I16a3213*Lam - complex(0,1)*I17a3213*Lam',
                   order = {'NP':1})

GC_2204 = Coupling(name = 'GC_2204',
                   value = 'complex(0,1)*I16a3221*Lam - complex(0,1)*I17a3221*Lam',
                   order = {'NP':1})

GC_2205 = Coupling(name = 'GC_2205',
                   value = 'complex(0,1)*I16a3222*Lam - complex(0,1)*I17a3222*Lam',
                   order = {'NP':1})

GC_2206 = Coupling(name = 'GC_2206',
                   value = 'complex(0,1)*I16a3223*Lam - complex(0,1)*I17a3223*Lam',
                   order = {'NP':1})

GC_2207 = Coupling(name = 'GC_2207',
                   value = 'complex(0,1)*I16a3231*Lam - complex(0,1)*I17a3231*Lam',
                   order = {'NP':1})

GC_2208 = Coupling(name = 'GC_2208',
                   value = 'complex(0,1)*I16a3232*Lam - complex(0,1)*I17a3232*Lam',
                   order = {'NP':1})

GC_2209 = Coupling(name = 'GC_2209',
                   value = 'complex(0,1)*I16a3233*Lam - complex(0,1)*I17a3233*Lam',
                   order = {'NP':1})

GC_2210 = Coupling(name = 'GC_2210',
                   value = 'complex(0,1)*I16a3311*Lam - complex(0,1)*I17a3311*Lam',
                   order = {'NP':1})

GC_2211 = Coupling(name = 'GC_2211',
                   value = 'complex(0,1)*I16a3312*Lam - complex(0,1)*I17a3312*Lam',
                   order = {'NP':1})

GC_2212 = Coupling(name = 'GC_2212',
                   value = 'complex(0,1)*I16a3313*Lam - complex(0,1)*I17a3313*Lam',
                   order = {'NP':1})

GC_2213 = Coupling(name = 'GC_2213',
                   value = 'complex(0,1)*I16a3321*Lam - complex(0,1)*I17a3321*Lam',
                   order = {'NP':1})

GC_2214 = Coupling(name = 'GC_2214',
                   value = 'complex(0,1)*I16a3322*Lam - complex(0,1)*I17a3322*Lam',
                   order = {'NP':1})

GC_2215 = Coupling(name = 'GC_2215',
                   value = 'complex(0,1)*I16a3323*Lam - complex(0,1)*I17a3323*Lam',
                   order = {'NP':1})

GC_2216 = Coupling(name = 'GC_2216',
                   value = 'complex(0,1)*I16a3331*Lam - complex(0,1)*I17a3331*Lam',
                   order = {'NP':1})

GC_2217 = Coupling(name = 'GC_2217',
                   value = 'complex(0,1)*I16a3332*Lam - complex(0,1)*I17a3332*Lam',
                   order = {'NP':1})

GC_2218 = Coupling(name = 'GC_2218',
                   value = 'complex(0,1)*I16a3333*Lam - complex(0,1)*I17a3333*Lam',
                   order = {'NP':1})

GC_2219 = Coupling(name = 'GC_2219',
                   value = 'complex(0,1)*I19a1111*Lam + complex(0,1)*I20a1111*Lam',
                   order = {'NP':1})

GC_2220 = Coupling(name = 'GC_2220',
                   value = 'complex(0,1)*I19a1112*Lam + complex(0,1)*I20a1112*Lam',
                   order = {'NP':1})

GC_2221 = Coupling(name = 'GC_2221',
                   value = 'complex(0,1)*I19a1113*Lam + complex(0,1)*I20a1113*Lam',
                   order = {'NP':1})

GC_2222 = Coupling(name = 'GC_2222',
                   value = 'complex(0,1)*I19a1121*Lam + complex(0,1)*I20a1121*Lam',
                   order = {'NP':1})

GC_2223 = Coupling(name = 'GC_2223',
                   value = 'complex(0,1)*I19a1122*Lam + complex(0,1)*I20a1122*Lam',
                   order = {'NP':1})

GC_2224 = Coupling(name = 'GC_2224',
                   value = 'complex(0,1)*I19a1123*Lam + complex(0,1)*I20a1123*Lam',
                   order = {'NP':1})

GC_2225 = Coupling(name = 'GC_2225',
                   value = 'complex(0,1)*I19a1131*Lam + complex(0,1)*I20a1131*Lam',
                   order = {'NP':1})

GC_2226 = Coupling(name = 'GC_2226',
                   value = 'complex(0,1)*I19a1132*Lam + complex(0,1)*I20a1132*Lam',
                   order = {'NP':1})

GC_2227 = Coupling(name = 'GC_2227',
                   value = 'complex(0,1)*I19a1133*Lam + complex(0,1)*I20a1133*Lam',
                   order = {'NP':1})

GC_2228 = Coupling(name = 'GC_2228',
                   value = 'complex(0,1)*I19a1211*Lam + complex(0,1)*I20a1211*Lam',
                   order = {'NP':1})

GC_2229 = Coupling(name = 'GC_2229',
                   value = 'complex(0,1)*I19a1212*Lam + complex(0,1)*I20a1212*Lam',
                   order = {'NP':1})

GC_2230 = Coupling(name = 'GC_2230',
                   value = 'complex(0,1)*I19a1213*Lam + complex(0,1)*I20a1213*Lam',
                   order = {'NP':1})

GC_2231 = Coupling(name = 'GC_2231',
                   value = 'complex(0,1)*I19a1221*Lam + complex(0,1)*I20a1221*Lam',
                   order = {'NP':1})

GC_2232 = Coupling(name = 'GC_2232',
                   value = 'complex(0,1)*I19a1222*Lam + complex(0,1)*I20a1222*Lam',
                   order = {'NP':1})

GC_2233 = Coupling(name = 'GC_2233',
                   value = 'complex(0,1)*I19a1223*Lam + complex(0,1)*I20a1223*Lam',
                   order = {'NP':1})

GC_2234 = Coupling(name = 'GC_2234',
                   value = 'complex(0,1)*I19a1231*Lam + complex(0,1)*I20a1231*Lam',
                   order = {'NP':1})

GC_2235 = Coupling(name = 'GC_2235',
                   value = 'complex(0,1)*I19a1232*Lam + complex(0,1)*I20a1232*Lam',
                   order = {'NP':1})

GC_2236 = Coupling(name = 'GC_2236',
                   value = 'complex(0,1)*I19a1233*Lam + complex(0,1)*I20a1233*Lam',
                   order = {'NP':1})

GC_2237 = Coupling(name = 'GC_2237',
                   value = 'complex(0,1)*I19a1311*Lam + complex(0,1)*I20a1311*Lam',
                   order = {'NP':1})

GC_2238 = Coupling(name = 'GC_2238',
                   value = 'complex(0,1)*I19a1312*Lam + complex(0,1)*I20a1312*Lam',
                   order = {'NP':1})

GC_2239 = Coupling(name = 'GC_2239',
                   value = 'complex(0,1)*I19a1313*Lam + complex(0,1)*I20a1313*Lam',
                   order = {'NP':1})

GC_2240 = Coupling(name = 'GC_2240',
                   value = 'complex(0,1)*I19a1321*Lam + complex(0,1)*I20a1321*Lam',
                   order = {'NP':1})

GC_2241 = Coupling(name = 'GC_2241',
                   value = 'complex(0,1)*I19a1322*Lam + complex(0,1)*I20a1322*Lam',
                   order = {'NP':1})

GC_2242 = Coupling(name = 'GC_2242',
                   value = 'complex(0,1)*I19a1323*Lam + complex(0,1)*I20a1323*Lam',
                   order = {'NP':1})

GC_2243 = Coupling(name = 'GC_2243',
                   value = 'complex(0,1)*I19a1331*Lam + complex(0,1)*I20a1331*Lam',
                   order = {'NP':1})

GC_2244 = Coupling(name = 'GC_2244',
                   value = 'complex(0,1)*I19a1332*Lam + complex(0,1)*I20a1332*Lam',
                   order = {'NP':1})

GC_2245 = Coupling(name = 'GC_2245',
                   value = 'complex(0,1)*I19a1333*Lam + complex(0,1)*I20a1333*Lam',
                   order = {'NP':1})

GC_2246 = Coupling(name = 'GC_2246',
                   value = 'complex(0,1)*I19a2111*Lam + complex(0,1)*I20a2111*Lam',
                   order = {'NP':1})

GC_2247 = Coupling(name = 'GC_2247',
                   value = 'complex(0,1)*I19a2112*Lam + complex(0,1)*I20a2112*Lam',
                   order = {'NP':1})

GC_2248 = Coupling(name = 'GC_2248',
                   value = 'complex(0,1)*I19a2113*Lam + complex(0,1)*I20a2113*Lam',
                   order = {'NP':1})

GC_2249 = Coupling(name = 'GC_2249',
                   value = 'complex(0,1)*I19a2121*Lam + complex(0,1)*I20a2121*Lam',
                   order = {'NP':1})

GC_2250 = Coupling(name = 'GC_2250',
                   value = 'complex(0,1)*I19a2122*Lam + complex(0,1)*I20a2122*Lam',
                   order = {'NP':1})

GC_2251 = Coupling(name = 'GC_2251',
                   value = 'complex(0,1)*I19a2123*Lam + complex(0,1)*I20a2123*Lam',
                   order = {'NP':1})

GC_2252 = Coupling(name = 'GC_2252',
                   value = 'complex(0,1)*I19a2131*Lam + complex(0,1)*I20a2131*Lam',
                   order = {'NP':1})

GC_2253 = Coupling(name = 'GC_2253',
                   value = 'complex(0,1)*I19a2132*Lam + complex(0,1)*I20a2132*Lam',
                   order = {'NP':1})

GC_2254 = Coupling(name = 'GC_2254',
                   value = 'complex(0,1)*I19a2133*Lam + complex(0,1)*I20a2133*Lam',
                   order = {'NP':1})

GC_2255 = Coupling(name = 'GC_2255',
                   value = 'complex(0,1)*I19a2211*Lam + complex(0,1)*I20a2211*Lam',
                   order = {'NP':1})

GC_2256 = Coupling(name = 'GC_2256',
                   value = 'complex(0,1)*I19a2212*Lam + complex(0,1)*I20a2212*Lam',
                   order = {'NP':1})

GC_2257 = Coupling(name = 'GC_2257',
                   value = 'complex(0,1)*I19a2213*Lam + complex(0,1)*I20a2213*Lam',
                   order = {'NP':1})

GC_2258 = Coupling(name = 'GC_2258',
                   value = 'complex(0,1)*I19a2221*Lam + complex(0,1)*I20a2221*Lam',
                   order = {'NP':1})

GC_2259 = Coupling(name = 'GC_2259',
                   value = 'complex(0,1)*I19a2222*Lam + complex(0,1)*I20a2222*Lam',
                   order = {'NP':1})

GC_2260 = Coupling(name = 'GC_2260',
                   value = 'complex(0,1)*I19a2223*Lam + complex(0,1)*I20a2223*Lam',
                   order = {'NP':1})

GC_2261 = Coupling(name = 'GC_2261',
                   value = 'complex(0,1)*I19a2231*Lam + complex(0,1)*I20a2231*Lam',
                   order = {'NP':1})

GC_2262 = Coupling(name = 'GC_2262',
                   value = 'complex(0,1)*I19a2232*Lam + complex(0,1)*I20a2232*Lam',
                   order = {'NP':1})

GC_2263 = Coupling(name = 'GC_2263',
                   value = 'complex(0,1)*I19a2233*Lam + complex(0,1)*I20a2233*Lam',
                   order = {'NP':1})

GC_2264 = Coupling(name = 'GC_2264',
                   value = 'complex(0,1)*I19a2311*Lam + complex(0,1)*I20a2311*Lam',
                   order = {'NP':1})

GC_2265 = Coupling(name = 'GC_2265',
                   value = 'complex(0,1)*I19a2312*Lam + complex(0,1)*I20a2312*Lam',
                   order = {'NP':1})

GC_2266 = Coupling(name = 'GC_2266',
                   value = 'complex(0,1)*I19a2313*Lam + complex(0,1)*I20a2313*Lam',
                   order = {'NP':1})

GC_2267 = Coupling(name = 'GC_2267',
                   value = 'complex(0,1)*I19a2321*Lam + complex(0,1)*I20a2321*Lam',
                   order = {'NP':1})

GC_2268 = Coupling(name = 'GC_2268',
                   value = 'complex(0,1)*I19a2322*Lam + complex(0,1)*I20a2322*Lam',
                   order = {'NP':1})

GC_2269 = Coupling(name = 'GC_2269',
                   value = 'complex(0,1)*I19a2323*Lam + complex(0,1)*I20a2323*Lam',
                   order = {'NP':1})

GC_2270 = Coupling(name = 'GC_2270',
                   value = 'complex(0,1)*I19a2331*Lam + complex(0,1)*I20a2331*Lam',
                   order = {'NP':1})

GC_2271 = Coupling(name = 'GC_2271',
                   value = 'complex(0,1)*I19a2332*Lam + complex(0,1)*I20a2332*Lam',
                   order = {'NP':1})

GC_2272 = Coupling(name = 'GC_2272',
                   value = 'complex(0,1)*I19a2333*Lam + complex(0,1)*I20a2333*Lam',
                   order = {'NP':1})

GC_2273 = Coupling(name = 'GC_2273',
                   value = 'complex(0,1)*I19a3111*Lam + complex(0,1)*I20a3111*Lam',
                   order = {'NP':1})

GC_2274 = Coupling(name = 'GC_2274',
                   value = 'complex(0,1)*I19a3112*Lam + complex(0,1)*I20a3112*Lam',
                   order = {'NP':1})

GC_2275 = Coupling(name = 'GC_2275',
                   value = 'complex(0,1)*I19a3113*Lam + complex(0,1)*I20a3113*Lam',
                   order = {'NP':1})

GC_2276 = Coupling(name = 'GC_2276',
                   value = 'complex(0,1)*I19a3121*Lam + complex(0,1)*I20a3121*Lam',
                   order = {'NP':1})

GC_2277 = Coupling(name = 'GC_2277',
                   value = 'complex(0,1)*I19a3122*Lam + complex(0,1)*I20a3122*Lam',
                   order = {'NP':1})

GC_2278 = Coupling(name = 'GC_2278',
                   value = 'complex(0,1)*I19a3123*Lam + complex(0,1)*I20a3123*Lam',
                   order = {'NP':1})

GC_2279 = Coupling(name = 'GC_2279',
                   value = 'complex(0,1)*I19a3131*Lam + complex(0,1)*I20a3131*Lam',
                   order = {'NP':1})

GC_2280 = Coupling(name = 'GC_2280',
                   value = 'complex(0,1)*I19a3132*Lam + complex(0,1)*I20a3132*Lam',
                   order = {'NP':1})

GC_2281 = Coupling(name = 'GC_2281',
                   value = 'complex(0,1)*I19a3133*Lam + complex(0,1)*I20a3133*Lam',
                   order = {'NP':1})

GC_2282 = Coupling(name = 'GC_2282',
                   value = 'complex(0,1)*I19a3211*Lam + complex(0,1)*I20a3211*Lam',
                   order = {'NP':1})

GC_2283 = Coupling(name = 'GC_2283',
                   value = 'complex(0,1)*I19a3212*Lam + complex(0,1)*I20a3212*Lam',
                   order = {'NP':1})

GC_2284 = Coupling(name = 'GC_2284',
                   value = 'complex(0,1)*I19a3213*Lam + complex(0,1)*I20a3213*Lam',
                   order = {'NP':1})

GC_2285 = Coupling(name = 'GC_2285',
                   value = 'complex(0,1)*I19a3221*Lam + complex(0,1)*I20a3221*Lam',
                   order = {'NP':1})

GC_2286 = Coupling(name = 'GC_2286',
                   value = 'complex(0,1)*I19a3222*Lam + complex(0,1)*I20a3222*Lam',
                   order = {'NP':1})

GC_2287 = Coupling(name = 'GC_2287',
                   value = 'complex(0,1)*I19a3223*Lam + complex(0,1)*I20a3223*Lam',
                   order = {'NP':1})

GC_2288 = Coupling(name = 'GC_2288',
                   value = 'complex(0,1)*I19a3231*Lam + complex(0,1)*I20a3231*Lam',
                   order = {'NP':1})

GC_2289 = Coupling(name = 'GC_2289',
                   value = 'complex(0,1)*I19a3232*Lam + complex(0,1)*I20a3232*Lam',
                   order = {'NP':1})

GC_2290 = Coupling(name = 'GC_2290',
                   value = 'complex(0,1)*I19a3233*Lam + complex(0,1)*I20a3233*Lam',
                   order = {'NP':1})

GC_2291 = Coupling(name = 'GC_2291',
                   value = 'complex(0,1)*I19a3311*Lam + complex(0,1)*I20a3311*Lam',
                   order = {'NP':1})

GC_2292 = Coupling(name = 'GC_2292',
                   value = 'complex(0,1)*I19a3312*Lam + complex(0,1)*I20a3312*Lam',
                   order = {'NP':1})

GC_2293 = Coupling(name = 'GC_2293',
                   value = 'complex(0,1)*I19a3313*Lam + complex(0,1)*I20a3313*Lam',
                   order = {'NP':1})

GC_2294 = Coupling(name = 'GC_2294',
                   value = 'complex(0,1)*I19a3321*Lam + complex(0,1)*I20a3321*Lam',
                   order = {'NP':1})

GC_2295 = Coupling(name = 'GC_2295',
                   value = 'complex(0,1)*I19a3322*Lam + complex(0,1)*I20a3322*Lam',
                   order = {'NP':1})

GC_2296 = Coupling(name = 'GC_2296',
                   value = 'complex(0,1)*I19a3323*Lam + complex(0,1)*I20a3323*Lam',
                   order = {'NP':1})

GC_2297 = Coupling(name = 'GC_2297',
                   value = 'complex(0,1)*I19a3331*Lam + complex(0,1)*I20a3331*Lam',
                   order = {'NP':1})

GC_2298 = Coupling(name = 'GC_2298',
                   value = 'complex(0,1)*I19a3332*Lam + complex(0,1)*I20a3332*Lam',
                   order = {'NP':1})

GC_2299 = Coupling(name = 'GC_2299',
                   value = 'complex(0,1)*I19a3333*Lam + complex(0,1)*I20a3333*Lam',
                   order = {'NP':1})

GC_2300 = Coupling(name = 'GC_2300',
                   value = 'complex(0,1)*I3a1111*Lam - complex(0,1)*I4a1111*Lam',
                   order = {'NP':1})

GC_2301 = Coupling(name = 'GC_2301',
                   value = 'complex(0,1)*I3a1112*Lam - complex(0,1)*I4a1112*Lam',
                   order = {'NP':1})

GC_2302 = Coupling(name = 'GC_2302',
                   value = 'complex(0,1)*I3a1113*Lam - complex(0,1)*I4a1113*Lam',
                   order = {'NP':1})

GC_2303 = Coupling(name = 'GC_2303',
                   value = 'complex(0,1)*I3a1121*Lam - complex(0,1)*I4a1121*Lam',
                   order = {'NP':1})

GC_2304 = Coupling(name = 'GC_2304',
                   value = 'complex(0,1)*I3a1122*Lam - complex(0,1)*I4a1122*Lam',
                   order = {'NP':1})

GC_2305 = Coupling(name = 'GC_2305',
                   value = 'complex(0,1)*I3a1123*Lam - complex(0,1)*I4a1123*Lam',
                   order = {'NP':1})

GC_2306 = Coupling(name = 'GC_2306',
                   value = 'complex(0,1)*I3a1131*Lam - complex(0,1)*I4a1131*Lam',
                   order = {'NP':1})

GC_2307 = Coupling(name = 'GC_2307',
                   value = 'complex(0,1)*I3a1132*Lam - complex(0,1)*I4a1132*Lam',
                   order = {'NP':1})

GC_2308 = Coupling(name = 'GC_2308',
                   value = 'complex(0,1)*I3a1133*Lam - complex(0,1)*I4a1133*Lam',
                   order = {'NP':1})

GC_2309 = Coupling(name = 'GC_2309',
                   value = 'complex(0,1)*I3a1211*Lam - complex(0,1)*I4a1211*Lam',
                   order = {'NP':1})

GC_2310 = Coupling(name = 'GC_2310',
                   value = 'complex(0,1)*I3a1212*Lam - complex(0,1)*I4a1212*Lam',
                   order = {'NP':1})

GC_2311 = Coupling(name = 'GC_2311',
                   value = 'complex(0,1)*I3a1213*Lam - complex(0,1)*I4a1213*Lam',
                   order = {'NP':1})

GC_2312 = Coupling(name = 'GC_2312',
                   value = 'complex(0,1)*I3a1221*Lam - complex(0,1)*I4a1221*Lam',
                   order = {'NP':1})

GC_2313 = Coupling(name = 'GC_2313',
                   value = 'complex(0,1)*I3a1222*Lam - complex(0,1)*I4a1222*Lam',
                   order = {'NP':1})

GC_2314 = Coupling(name = 'GC_2314',
                   value = 'complex(0,1)*I3a1223*Lam - complex(0,1)*I4a1223*Lam',
                   order = {'NP':1})

GC_2315 = Coupling(name = 'GC_2315',
                   value = 'complex(0,1)*I3a1231*Lam - complex(0,1)*I4a1231*Lam',
                   order = {'NP':1})

GC_2316 = Coupling(name = 'GC_2316',
                   value = 'complex(0,1)*I3a1232*Lam - complex(0,1)*I4a1232*Lam',
                   order = {'NP':1})

GC_2317 = Coupling(name = 'GC_2317',
                   value = 'complex(0,1)*I3a1233*Lam - complex(0,1)*I4a1233*Lam',
                   order = {'NP':1})

GC_2318 = Coupling(name = 'GC_2318',
                   value = 'complex(0,1)*I3a1311*Lam - complex(0,1)*I4a1311*Lam',
                   order = {'NP':1})

GC_2319 = Coupling(name = 'GC_2319',
                   value = 'complex(0,1)*I3a1312*Lam - complex(0,1)*I4a1312*Lam',
                   order = {'NP':1})

GC_2320 = Coupling(name = 'GC_2320',
                   value = 'complex(0,1)*I3a1313*Lam - complex(0,1)*I4a1313*Lam',
                   order = {'NP':1})

GC_2321 = Coupling(name = 'GC_2321',
                   value = 'complex(0,1)*I3a1321*Lam - complex(0,1)*I4a1321*Lam',
                   order = {'NP':1})

GC_2322 = Coupling(name = 'GC_2322',
                   value = 'complex(0,1)*I3a1322*Lam - complex(0,1)*I4a1322*Lam',
                   order = {'NP':1})

GC_2323 = Coupling(name = 'GC_2323',
                   value = 'complex(0,1)*I3a1323*Lam - complex(0,1)*I4a1323*Lam',
                   order = {'NP':1})

GC_2324 = Coupling(name = 'GC_2324',
                   value = 'complex(0,1)*I3a1331*Lam - complex(0,1)*I4a1331*Lam',
                   order = {'NP':1})

GC_2325 = Coupling(name = 'GC_2325',
                   value = 'complex(0,1)*I3a1332*Lam - complex(0,1)*I4a1332*Lam',
                   order = {'NP':1})

GC_2326 = Coupling(name = 'GC_2326',
                   value = 'complex(0,1)*I3a1333*Lam - complex(0,1)*I4a1333*Lam',
                   order = {'NP':1})

GC_2327 = Coupling(name = 'GC_2327',
                   value = 'complex(0,1)*I3a2111*Lam - complex(0,1)*I4a2111*Lam',
                   order = {'NP':1})

GC_2328 = Coupling(name = 'GC_2328',
                   value = 'complex(0,1)*I3a2112*Lam - complex(0,1)*I4a2112*Lam',
                   order = {'NP':1})

GC_2329 = Coupling(name = 'GC_2329',
                   value = 'complex(0,1)*I3a2113*Lam - complex(0,1)*I4a2113*Lam',
                   order = {'NP':1})

GC_2330 = Coupling(name = 'GC_2330',
                   value = 'complex(0,1)*I3a2121*Lam - complex(0,1)*I4a2121*Lam',
                   order = {'NP':1})

GC_2331 = Coupling(name = 'GC_2331',
                   value = 'complex(0,1)*I3a2122*Lam - complex(0,1)*I4a2122*Lam',
                   order = {'NP':1})

GC_2332 = Coupling(name = 'GC_2332',
                   value = 'complex(0,1)*I3a2123*Lam - complex(0,1)*I4a2123*Lam',
                   order = {'NP':1})

GC_2333 = Coupling(name = 'GC_2333',
                   value = 'complex(0,1)*I3a2131*Lam - complex(0,1)*I4a2131*Lam',
                   order = {'NP':1})

GC_2334 = Coupling(name = 'GC_2334',
                   value = 'complex(0,1)*I3a2132*Lam - complex(0,1)*I4a2132*Lam',
                   order = {'NP':1})

GC_2335 = Coupling(name = 'GC_2335',
                   value = 'complex(0,1)*I3a2133*Lam - complex(0,1)*I4a2133*Lam',
                   order = {'NP':1})

GC_2336 = Coupling(name = 'GC_2336',
                   value = 'complex(0,1)*I3a2211*Lam - complex(0,1)*I4a2211*Lam',
                   order = {'NP':1})

GC_2337 = Coupling(name = 'GC_2337',
                   value = 'complex(0,1)*I3a2212*Lam - complex(0,1)*I4a2212*Lam',
                   order = {'NP':1})

GC_2338 = Coupling(name = 'GC_2338',
                   value = 'complex(0,1)*I3a2213*Lam - complex(0,1)*I4a2213*Lam',
                   order = {'NP':1})

GC_2339 = Coupling(name = 'GC_2339',
                   value = 'complex(0,1)*I3a2221*Lam - complex(0,1)*I4a2221*Lam',
                   order = {'NP':1})

GC_2340 = Coupling(name = 'GC_2340',
                   value = 'complex(0,1)*I3a2222*Lam - complex(0,1)*I4a2222*Lam',
                   order = {'NP':1})

GC_2341 = Coupling(name = 'GC_2341',
                   value = 'complex(0,1)*I3a2223*Lam - complex(0,1)*I4a2223*Lam',
                   order = {'NP':1})

GC_2342 = Coupling(name = 'GC_2342',
                   value = 'complex(0,1)*I3a2231*Lam - complex(0,1)*I4a2231*Lam',
                   order = {'NP':1})

GC_2343 = Coupling(name = 'GC_2343',
                   value = 'complex(0,1)*I3a2232*Lam - complex(0,1)*I4a2232*Lam',
                   order = {'NP':1})

GC_2344 = Coupling(name = 'GC_2344',
                   value = 'complex(0,1)*I3a2233*Lam - complex(0,1)*I4a2233*Lam',
                   order = {'NP':1})

GC_2345 = Coupling(name = 'GC_2345',
                   value = 'complex(0,1)*I3a2311*Lam - complex(0,1)*I4a2311*Lam',
                   order = {'NP':1})

GC_2346 = Coupling(name = 'GC_2346',
                   value = 'complex(0,1)*I3a2312*Lam - complex(0,1)*I4a2312*Lam',
                   order = {'NP':1})

GC_2347 = Coupling(name = 'GC_2347',
                   value = 'complex(0,1)*I3a2313*Lam - complex(0,1)*I4a2313*Lam',
                   order = {'NP':1})

GC_2348 = Coupling(name = 'GC_2348',
                   value = 'complex(0,1)*I3a2321*Lam - complex(0,1)*I4a2321*Lam',
                   order = {'NP':1})

GC_2349 = Coupling(name = 'GC_2349',
                   value = 'complex(0,1)*I3a2322*Lam - complex(0,1)*I4a2322*Lam',
                   order = {'NP':1})

GC_2350 = Coupling(name = 'GC_2350',
                   value = 'complex(0,1)*I3a2323*Lam - complex(0,1)*I4a2323*Lam',
                   order = {'NP':1})

GC_2351 = Coupling(name = 'GC_2351',
                   value = 'complex(0,1)*I3a2331*Lam - complex(0,1)*I4a2331*Lam',
                   order = {'NP':1})

GC_2352 = Coupling(name = 'GC_2352',
                   value = 'complex(0,1)*I3a2332*Lam - complex(0,1)*I4a2332*Lam',
                   order = {'NP':1})

GC_2353 = Coupling(name = 'GC_2353',
                   value = 'complex(0,1)*I3a2333*Lam - complex(0,1)*I4a2333*Lam',
                   order = {'NP':1})

GC_2354 = Coupling(name = 'GC_2354',
                   value = 'complex(0,1)*I3a3111*Lam - complex(0,1)*I4a3111*Lam',
                   order = {'NP':1})

GC_2355 = Coupling(name = 'GC_2355',
                   value = 'complex(0,1)*I3a3112*Lam - complex(0,1)*I4a3112*Lam',
                   order = {'NP':1})

GC_2356 = Coupling(name = 'GC_2356',
                   value = 'complex(0,1)*I3a3113*Lam - complex(0,1)*I4a3113*Lam',
                   order = {'NP':1})

GC_2357 = Coupling(name = 'GC_2357',
                   value = 'complex(0,1)*I3a3121*Lam - complex(0,1)*I4a3121*Lam',
                   order = {'NP':1})

GC_2358 = Coupling(name = 'GC_2358',
                   value = 'complex(0,1)*I3a3122*Lam - complex(0,1)*I4a3122*Lam',
                   order = {'NP':1})

GC_2359 = Coupling(name = 'GC_2359',
                   value = 'complex(0,1)*I3a3123*Lam - complex(0,1)*I4a3123*Lam',
                   order = {'NP':1})

GC_2360 = Coupling(name = 'GC_2360',
                   value = 'complex(0,1)*I3a3131*Lam - complex(0,1)*I4a3131*Lam',
                   order = {'NP':1})

GC_2361 = Coupling(name = 'GC_2361',
                   value = 'complex(0,1)*I3a3132*Lam - complex(0,1)*I4a3132*Lam',
                   order = {'NP':1})

GC_2362 = Coupling(name = 'GC_2362',
                   value = 'complex(0,1)*I3a3133*Lam - complex(0,1)*I4a3133*Lam',
                   order = {'NP':1})

GC_2363 = Coupling(name = 'GC_2363',
                   value = 'complex(0,1)*I3a3211*Lam - complex(0,1)*I4a3211*Lam',
                   order = {'NP':1})

GC_2364 = Coupling(name = 'GC_2364',
                   value = 'complex(0,1)*I3a3212*Lam - complex(0,1)*I4a3212*Lam',
                   order = {'NP':1})

GC_2365 = Coupling(name = 'GC_2365',
                   value = 'complex(0,1)*I3a3213*Lam - complex(0,1)*I4a3213*Lam',
                   order = {'NP':1})

GC_2366 = Coupling(name = 'GC_2366',
                   value = 'complex(0,1)*I3a3221*Lam - complex(0,1)*I4a3221*Lam',
                   order = {'NP':1})

GC_2367 = Coupling(name = 'GC_2367',
                   value = 'complex(0,1)*I3a3222*Lam - complex(0,1)*I4a3222*Lam',
                   order = {'NP':1})

GC_2368 = Coupling(name = 'GC_2368',
                   value = 'complex(0,1)*I3a3223*Lam - complex(0,1)*I4a3223*Lam',
                   order = {'NP':1})

GC_2369 = Coupling(name = 'GC_2369',
                   value = 'complex(0,1)*I3a3231*Lam - complex(0,1)*I4a3231*Lam',
                   order = {'NP':1})

GC_2370 = Coupling(name = 'GC_2370',
                   value = 'complex(0,1)*I3a3232*Lam - complex(0,1)*I4a3232*Lam',
                   order = {'NP':1})

GC_2371 = Coupling(name = 'GC_2371',
                   value = 'complex(0,1)*I3a3233*Lam - complex(0,1)*I4a3233*Lam',
                   order = {'NP':1})

GC_2372 = Coupling(name = 'GC_2372',
                   value = 'complex(0,1)*I3a3311*Lam - complex(0,1)*I4a3311*Lam',
                   order = {'NP':1})

GC_2373 = Coupling(name = 'GC_2373',
                   value = 'complex(0,1)*I3a3312*Lam - complex(0,1)*I4a3312*Lam',
                   order = {'NP':1})

GC_2374 = Coupling(name = 'GC_2374',
                   value = 'complex(0,1)*I3a3313*Lam - complex(0,1)*I4a3313*Lam',
                   order = {'NP':1})

GC_2375 = Coupling(name = 'GC_2375',
                   value = 'complex(0,1)*I3a3321*Lam - complex(0,1)*I4a3321*Lam',
                   order = {'NP':1})

GC_2376 = Coupling(name = 'GC_2376',
                   value = 'complex(0,1)*I3a3322*Lam - complex(0,1)*I4a3322*Lam',
                   order = {'NP':1})

GC_2377 = Coupling(name = 'GC_2377',
                   value = 'complex(0,1)*I3a3323*Lam - complex(0,1)*I4a3323*Lam',
                   order = {'NP':1})

GC_2378 = Coupling(name = 'GC_2378',
                   value = 'complex(0,1)*I3a3331*Lam - complex(0,1)*I4a3331*Lam',
                   order = {'NP':1})

GC_2379 = Coupling(name = 'GC_2379',
                   value = 'complex(0,1)*I3a3332*Lam - complex(0,1)*I4a3332*Lam',
                   order = {'NP':1})

GC_2380 = Coupling(name = 'GC_2380',
                   value = 'complex(0,1)*I3a3333*Lam - complex(0,1)*I4a3333*Lam',
                   order = {'NP':1})

GC_2381 = Coupling(name = 'GC_2381',
                   value = '-((complex(0,1)*GW*Ul1x1)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2382 = Coupling(name = 'GC_2382',
                   value = '-((complex(0,1)*GW*Ul1x2)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2383 = Coupling(name = 'GC_2383',
                   value = '-((complex(0,1)*GW*Ul1x3)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2384 = Coupling(name = 'GC_2384',
                   value = '-((complex(0,1)*GW*Ul2x1)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2385 = Coupling(name = 'GC_2385',
                   value = '-((complex(0,1)*GW*Ul2x2)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2386 = Coupling(name = 'GC_2386',
                   value = '-((complex(0,1)*GW*Ul2x3)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2387 = Coupling(name = 'GC_2387',
                   value = '-((complex(0,1)*GW*Ul3x1)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2388 = Coupling(name = 'GC_2388',
                   value = '-((complex(0,1)*GW*Ul3x2)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2389 = Coupling(name = 'GC_2389',
                   value = '-((complex(0,1)*GW*Ul3x3)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2390 = Coupling(name = 'GC_2390',
                   value = '(complex(0,1)*GW**2*vev)/2.',
                   order = {'QED':2})

GC_2391 = Coupling(name = 'GC_2391',
                   value = '-3*complex(0,1)*hlambda*vev',
                   order = {'QED':1})

GC_2392 = Coupling(name = 'GC_2392',
                   value = '(complex(0,1)*G1**2*vev)/2. + (complex(0,1)*GW**2*vev)/2.',
                   order = {'QED':2})

GC_2393 = Coupling(name = 'GC_2393',
                   value = '-((complex(0,1)*mle*YO)/vev)',
                   order = {'QED':1})

GC_2394 = Coupling(name = 'GC_2394',
                   value = '-((complex(0,1)*mlm*YO)/vev)',
                   order = {'QED':1})

GC_2395 = Coupling(name = 'GC_2395',
                   value = '-((complex(0,1)*mlt*YO)/vev)',
                   order = {'QED':1})

GC_2396 = Coupling(name = 'GC_2396',
                   value = '-((complex(0,1)*mqb*YO)/vev)',
                   order = {'QED':1})

GC_2397 = Coupling(name = 'GC_2397',
                   value = '-((complex(0,1)*mqc*YO)/vev)',
                   order = {'QED':1})

GC_2398 = Coupling(name = 'GC_2398',
                   value = '-((complex(0,1)*mqd*YO)/vev)',
                   order = {'QED':1})

GC_2399 = Coupling(name = 'GC_2399',
                   value = '-((complex(0,1)*mqs*YO)/vev)',
                   order = {'QED':1})

GC_2400 = Coupling(name = 'GC_2400',
                   value = '-((complex(0,1)*mqt*YO)/vev)',
                   order = {'QED':1})

GC_2401 = Coupling(name = 'GC_2401',
                   value = '-((complex(0,1)*mqu*YO)/vev)',
                   order = {'QED':1})

GC_2402 = Coupling(name = 'GC_2402',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x1x1x1)',
                   order = {'NP':1})

GC_2403 = Coupling(name = 'GC_2403',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x1x1x2)',
                   order = {'NP':1})

GC_2404 = Coupling(name = 'GC_2404',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x1x1x3)',
                   order = {'NP':1})

GC_2405 = Coupling(name = 'GC_2405',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x1x2x1)',
                   order = {'NP':1})

GC_2406 = Coupling(name = 'GC_2406',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x1x2x2)',
                   order = {'NP':1})

GC_2407 = Coupling(name = 'GC_2407',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x1x2x3)',
                   order = {'NP':1})

GC_2408 = Coupling(name = 'GC_2408',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x1x3x1)',
                   order = {'NP':1})

GC_2409 = Coupling(name = 'GC_2409',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x1x3x2)',
                   order = {'NP':1})

GC_2410 = Coupling(name = 'GC_2410',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x1x3x3)',
                   order = {'NP':1})

GC_2411 = Coupling(name = 'GC_2411',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x2x1x1)',
                   order = {'NP':1})

GC_2412 = Coupling(name = 'GC_2412',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x2x1x2)',
                   order = {'NP':1})

GC_2413 = Coupling(name = 'GC_2413',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x2x1x3)',
                   order = {'NP':1})

GC_2414 = Coupling(name = 'GC_2414',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x2x2x1)',
                   order = {'NP':1})

GC_2415 = Coupling(name = 'GC_2415',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x2x2x2)',
                   order = {'NP':1})

GC_2416 = Coupling(name = 'GC_2416',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x2x2x3)',
                   order = {'NP':1})

GC_2417 = Coupling(name = 'GC_2417',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x2x3x1)',
                   order = {'NP':1})

GC_2418 = Coupling(name = 'GC_2418',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x2x3x2)',
                   order = {'NP':1})

GC_2419 = Coupling(name = 'GC_2419',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x2x3x3)',
                   order = {'NP':1})

GC_2420 = Coupling(name = 'GC_2420',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x3x1x1)',
                   order = {'NP':1})

GC_2421 = Coupling(name = 'GC_2421',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x3x1x2)',
                   order = {'NP':1})

GC_2422 = Coupling(name = 'GC_2422',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x3x1x3)',
                   order = {'NP':1})

GC_2423 = Coupling(name = 'GC_2423',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x3x2x1)',
                   order = {'NP':1})

GC_2424 = Coupling(name = 'GC_2424',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x3x2x2)',
                   order = {'NP':1})

GC_2425 = Coupling(name = 'GC_2425',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x3x2x3)',
                   order = {'NP':1})

GC_2426 = Coupling(name = 'GC_2426',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x3x3x1)',
                   order = {'NP':1})

GC_2427 = Coupling(name = 'GC_2427',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x3x3x2)',
                   order = {'NP':1})

GC_2428 = Coupling(name = 'GC_2428',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq1x3x3x3)',
                   order = {'NP':1})

GC_2429 = Coupling(name = 'GC_2429',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x1x1x1)',
                   order = {'NP':1})

GC_2430 = Coupling(name = 'GC_2430',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x1x1x2)',
                   order = {'NP':1})

GC_2431 = Coupling(name = 'GC_2431',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x1x1x3)',
                   order = {'NP':1})

GC_2432 = Coupling(name = 'GC_2432',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x1x2x1)',
                   order = {'NP':1})

GC_2433 = Coupling(name = 'GC_2433',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x1x2x2)',
                   order = {'NP':1})

GC_2434 = Coupling(name = 'GC_2434',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x1x2x3)',
                   order = {'NP':1})

GC_2435 = Coupling(name = 'GC_2435',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x1x3x1)',
                   order = {'NP':1})

GC_2436 = Coupling(name = 'GC_2436',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x1x3x2)',
                   order = {'NP':1})

GC_2437 = Coupling(name = 'GC_2437',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x1x3x3)',
                   order = {'NP':1})

GC_2438 = Coupling(name = 'GC_2438',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x2x1x1)',
                   order = {'NP':1})

GC_2439 = Coupling(name = 'GC_2439',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x2x1x2)',
                   order = {'NP':1})

GC_2440 = Coupling(name = 'GC_2440',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x2x1x3)',
                   order = {'NP':1})

GC_2441 = Coupling(name = 'GC_2441',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x2x2x1)',
                   order = {'NP':1})

GC_2442 = Coupling(name = 'GC_2442',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x2x2x2)',
                   order = {'NP':1})

GC_2443 = Coupling(name = 'GC_2443',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x2x2x3)',
                   order = {'NP':1})

GC_2444 = Coupling(name = 'GC_2444',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x2x3x1)',
                   order = {'NP':1})

GC_2445 = Coupling(name = 'GC_2445',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x2x3x2)',
                   order = {'NP':1})

GC_2446 = Coupling(name = 'GC_2446',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x2x3x3)',
                   order = {'NP':1})

GC_2447 = Coupling(name = 'GC_2447',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x3x1x1)',
                   order = {'NP':1})

GC_2448 = Coupling(name = 'GC_2448',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x3x1x2)',
                   order = {'NP':1})

GC_2449 = Coupling(name = 'GC_2449',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x3x1x3)',
                   order = {'NP':1})

GC_2450 = Coupling(name = 'GC_2450',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x3x2x1)',
                   order = {'NP':1})

GC_2451 = Coupling(name = 'GC_2451',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x3x2x2)',
                   order = {'NP':1})

GC_2452 = Coupling(name = 'GC_2452',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x3x2x3)',
                   order = {'NP':1})

GC_2453 = Coupling(name = 'GC_2453',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x3x3x1)',
                   order = {'NP':1})

GC_2454 = Coupling(name = 'GC_2454',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x3x3x2)',
                   order = {'NP':1})

GC_2455 = Coupling(name = 'GC_2455',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq2x3x3x3)',
                   order = {'NP':1})

GC_2456 = Coupling(name = 'GC_2456',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x1x1x1)',
                   order = {'NP':1})

GC_2457 = Coupling(name = 'GC_2457',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x1x1x2)',
                   order = {'NP':1})

GC_2458 = Coupling(name = 'GC_2458',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x1x1x3)',
                   order = {'NP':1})

GC_2459 = Coupling(name = 'GC_2459',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x1x2x1)',
                   order = {'NP':1})

GC_2460 = Coupling(name = 'GC_2460',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x1x2x2)',
                   order = {'NP':1})

GC_2461 = Coupling(name = 'GC_2461',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x1x2x3)',
                   order = {'NP':1})

GC_2462 = Coupling(name = 'GC_2462',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x1x3x1)',
                   order = {'NP':1})

GC_2463 = Coupling(name = 'GC_2463',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x1x3x2)',
                   order = {'NP':1})

GC_2464 = Coupling(name = 'GC_2464',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x1x3x3)',
                   order = {'NP':1})

GC_2465 = Coupling(name = 'GC_2465',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x2x1x1)',
                   order = {'NP':1})

GC_2466 = Coupling(name = 'GC_2466',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x2x1x2)',
                   order = {'NP':1})

GC_2467 = Coupling(name = 'GC_2467',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x2x1x3)',
                   order = {'NP':1})

GC_2468 = Coupling(name = 'GC_2468',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x2x2x1)',
                   order = {'NP':1})

GC_2469 = Coupling(name = 'GC_2469',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x2x2x2)',
                   order = {'NP':1})

GC_2470 = Coupling(name = 'GC_2470',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x2x2x3)',
                   order = {'NP':1})

GC_2471 = Coupling(name = 'GC_2471',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x2x3x1)',
                   order = {'NP':1})

GC_2472 = Coupling(name = 'GC_2472',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x2x3x2)',
                   order = {'NP':1})

GC_2473 = Coupling(name = 'GC_2473',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x2x3x3)',
                   order = {'NP':1})

GC_2474 = Coupling(name = 'GC_2474',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x3x1x1)',
                   order = {'NP':1})

GC_2475 = Coupling(name = 'GC_2475',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x3x1x2)',
                   order = {'NP':1})

GC_2476 = Coupling(name = 'GC_2476',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x3x1x3)',
                   order = {'NP':1})

GC_2477 = Coupling(name = 'GC_2477',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x3x2x1)',
                   order = {'NP':1})

GC_2478 = Coupling(name = 'GC_2478',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x3x2x2)',
                   order = {'NP':1})

GC_2479 = Coupling(name = 'GC_2479',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x3x2x3)',
                   order = {'NP':1})

GC_2480 = Coupling(name = 'GC_2480',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x3x3x1)',
                   order = {'NP':1})

GC_2481 = Coupling(name = 'GC_2481',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x3x3x2)',
                   order = {'NP':1})

GC_2482 = Coupling(name = 'GC_2482',
                   value = 'complex(0,1)*Lam*complexconjugate(Cledq3x3x3x3)',
                   order = {'NP':1})

GC_2483 = Coupling(name = 'GC_2483',
                   value = '-((complex(0,1)*GW*complexconjugate(Kq1x1))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2484 = Coupling(name = 'GC_2484',
                   value = '-((complex(0,1)*GW*complexconjugate(Kq1x2))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2485 = Coupling(name = 'GC_2485',
                   value = '-((complex(0,1)*GW*complexconjugate(Kq1x3))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2486 = Coupling(name = 'GC_2486',
                   value = '-((complex(0,1)*GW*complexconjugate(Kq2x1))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2487 = Coupling(name = 'GC_2487',
                   value = '-((complex(0,1)*GW*complexconjugate(Kq2x2))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2488 = Coupling(name = 'GC_2488',
                   value = '-((complex(0,1)*GW*complexconjugate(Kq2x3))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2489 = Coupling(name = 'GC_2489',
                   value = '-((complex(0,1)*GW*complexconjugate(Kq3x1))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2490 = Coupling(name = 'GC_2490',
                   value = '-((complex(0,1)*GW*complexconjugate(Kq3x2))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2491 = Coupling(name = 'GC_2491',
                   value = '-((complex(0,1)*GW*complexconjugate(Kq3x3))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2492 = Coupling(name = 'GC_2492',
                   value = '-((complex(0,1)*GW*complexconjugate(Ul1x1))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2493 = Coupling(name = 'GC_2493',
                   value = '-((complex(0,1)*GW*complexconjugate(Ul1x2))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2494 = Coupling(name = 'GC_2494',
                   value = '-((complex(0,1)*GW*complexconjugate(Ul1x3))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2495 = Coupling(name = 'GC_2495',
                   value = '-((complex(0,1)*GW*complexconjugate(Ul2x1))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2496 = Coupling(name = 'GC_2496',
                   value = '-((complex(0,1)*GW*complexconjugate(Ul2x2))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2497 = Coupling(name = 'GC_2497',
                   value = '-((complex(0,1)*GW*complexconjugate(Ul2x3))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2498 = Coupling(name = 'GC_2498',
                   value = '-((complex(0,1)*GW*complexconjugate(Ul3x1))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2499 = Coupling(name = 'GC_2499',
                   value = '-((complex(0,1)*GW*complexconjugate(Ul3x2))/cmath.sqrt(2))',
                   order = {'QED':1})

GC_2500 = Coupling(name = 'GC_2500',
                   value = '-((complex(0,1)*GW*complexconjugate(Ul3x3))/cmath.sqrt(2))',
                   order = {'QED':1})

