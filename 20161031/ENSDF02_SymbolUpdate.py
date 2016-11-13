# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 23:19:55 2016
@author: soma0sd
"""

base = """'NN': 0, 'H ': 1, 'HE': 2, 'LI': 3, 'BE': 4, 'B ': 5, 'C ': 6, 'N ': 7, 'O ': 8, 'F ': 9, 'NE': 10, 'NA': 11, 'MG': 12, 'AL': 13, 'SI': 14, 'P ': 15, 'S ': 16, 'CL': 17, 'AR': 18, 'K ': 19, 'CA': 20, 'SC': 21, 'TI': 22, 'V ': 23, 'CR': 24, 'MN': 25, 'FE': 26, 'CO': 27, 'NI': 28, 'CU': 29, 'ZN': 30, 'GA': 31, 'GE': 32, 'AS': 33, 'SE': 34, 'BR': 35, 'KR': 36, 'RB': 37, 'SR': 38, 'Y ': 39, 'ZR': 40, 'NB': 41, 'MO': 42, 'TC': 43, 'RU': 44, 'RH': 45, 'PD': 46, 'AG': 47, 'CD': 48, 'IN': 49, 'SN': 50, 'SB': 51, 'TE': 52, 'I ': 53, 'XE': 54, 'CS': 55, 'BA': 56, 'LA': 57, 'CE': 58, 'PR': 59, 'ND': 60, 'PM': 61, 'SM': 62, 'EU': 63, 'GD': 64, 'TB': 65, 'Dy': 66, 'DY': 66, 'HO': 67, 'ER': 68, 'TM': 69, 'YB': 70, 'LU': 71, 'HF': 72, 'TA': 73, 'W ': 74, 'RE': 75, 'OS': 76, 'IR': 77, 'PT': 78, 'AU': 79, 'HG': 80, 'TL': 81, 'PB': 82, 'BI': 83, 'PO': 84, 'AT': 85, 'RN': 86, 'FR': 87, 'RA': 88, 'AC': 89, 'TH': 90, 'PA': 91, 'U ': 92, 'NP': 93, 'PU': 94, 'AM': 95, 'CM': 96, 'BK': 97, 'CF': 98, 'ES': 99, 'FM': 100, 'MD': 101, 'NO': 102, 'LR': 103, 'RF': 104, 'DB': 105, 'SG': 106, 'BH': 107, 'HS': 108, 'MT': 109, '10': 110, 'DS': 110, 'RG': 111, 'CN': 112, '12': 112, '13': 113, '14': 114, 'FL': 114, '15': 115, '16': 116, '17': 117, '18': 118"""

newn = """'NN': , 'H ': , 'HE': , 'LI': , 'C ': , 'BE': , 'B ': , 'N ': , 'O ': , 'F ': , 'NE': , 'NA': , 'MG': , 'AL': , 'SI': , 'P ': , 'S ': , 'AR': , 'CL': , 'K ': , 'CA': , 'SC': , 'TI': , 'V ': , 'CR': , 'FE': , 'MN': , 'NI': , 'CO': , 'ZN': , 'CU': , 'GA': , 'GE': , 'AS': , 'SE': , 'BR': , 'KR': , 'RB': , 'SR': , 'Y ': , 'ZR': , 'NB': , 'MO': , 'CM': , 'CF': , 'TC': , 'RU': , 'RH': , 'PD': , 'AG': , 'CD': , 'IN': , 'SN': , 'TE': , 'SB': , 'XE': , 'I ': , 'CS': , 'BA': , 'LA': , 'CE': , 'PR': , 'ND': , 'PM': , 'SM': , 'EU': , 'GD': , 'TB': , 'DY': , 'Dy': , 'HO': , 'ER': , 'TM': , 'YB': , 'LU': , 'HF': , 'TA': , 'W ': , 'RE': , 'OS': , 'IR': , 'PT': , 'AU': , 'HG': , 'TL': , 'PB': , 'BI': , 'PO': , 'AT': , 'RN': , 'FR': , 'RA': , 'AC': , 'TH': , 'PA': , 'U ': , 'NP': , 'PU': , 'AM': , 'BK': , 'ES': , 'FM': , 'MD': , 'NO': , 'LR': , 'RF': , 'DB': , 'SG': , 'BH': , 'HS': , 'MT': , '10': , 'DS': , 'RG': , '12': , '13': , 'CN': , 'FL': , '14': , '15': , '16': , '17': , '18': """

base_c = {}
for d1 in base.split(','):
  item = d1.strip().split(':')
  base_c[item[0]] = item[1]

newn_c = {}
for d1 in newn.split(','):
  item = d1.strip().split(':')
  newn_c[item[0]] = item[1]

newn_c.update(base_c)
print('{', end='')
for k in newn_c.keys():
  print("{}:{}".format(k,newn_c[k]), end=', ')
print('}')

del base, base_c, d1, item, k, newn, newn_c

rev = {'BH': 107, 'GE': 32, 'PM': 61, 'AC': 89, '14': 114, 'RB': 37, 'FM': 100, '16': 116, 'RU': 44, 'N ': 7, 'CF': 98, 'TC': 43, 'RE': 75, 'NN': 0, 'HS': 108, 'BE': 4, 'LR': 103, 'NI': 28, 'XE': 54, 'SB': 51, 'PU': 94, 'NO': 102, 'ND': 60, 'S ': 16, 'CA': 20, 'SE': 34, 'SG': 106, 'F ': 9, 'PA': 91, 'SN': 50, 'SR': 38, 'OS': 76, 'MN': 25, 'TM': 69, 'DB': 105, 'YB': 70, 'SI': 14, 'AL': 13, 'HG': 80, 'LA': 57, 'K ': 19, 'RF': 104, 'NP': 93, 'KR': 36, 'CO': 27, 'FE': 26, 'MD': 101, '12': 112, 'LU': 71, 'RN': 86, 'PR': 59, 'IN': 49, 'TH': 90, 'ER': 68, 'RA': 88, 'MO': 42, 'B ': 5, 'ES': 99, 'HF': 72, 'AG': 47, 'TE': 52, 'Dy': 66, 'CR': 24, 'CS': 55, 'U ': 92, 'SM': 62, 'P ': 15, 'MT': 109, 'PD': 46, '10': 110, 'DY': 66, 'CN': 112, 'AR': 18, 'TI': 22, 'PT': 78, 'FL': 114, 'TA': 73, 'HE': 2, 'BI': 83, 'V ': 23, 'SC': 21, 'O ': 8, 'ZN': 30, 'FR': 87, 'IR': 77, 'W ': 74, '18': 118, 'TB': 65, '15': 115, 'ZR': 40, 'CE': 58, 'AS': 33, 'NE': 10, 'HO': 67, 'PB': 82, 'AM': 95, 'RH': 45, 'NA': 11, 'H ': 1, '17': 117, 'BK': 97, 'BA': 56, 'BR': 35, 'CU': 29, 'AT': 85, 'CD': 48, 'MG': 12, '13': 113, 'Y ': 39, 'CM': 96, 'EU': 63, 'C ': 6, 'NB': 41, 'LI': 3, 'AU': 79, 'I ': 53, 'DS': 110, 'CL': 17, 'GA': 31, 'RG': 111, 'GD': 64, 'TL': 81, 'PO': 84}

print()

print('{', end='')
for i in range(119):
  for k in rev.keys():
    if rev[k] == i:
      print("'{}': {}".format(k, rev[k]), end=', ')
print('}')