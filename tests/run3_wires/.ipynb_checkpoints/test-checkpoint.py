#%%
from cpymad.madx import Madx 
import pandas as pd

madx = Madx()

#%%
madx.input("call, file=run3_collisions.mask;")

#%%

madx.input('''
use, sequence=lhcb1;
twiss;
''')

mytwiss = madx.table.twiss.dframe()
print(mytwiss[mytwiss['name'].str.contains('bbcw_')][['s','xma','yma','name','betx','bety']])

print(mytwiss.loc['ip1'][['betx','bety','s']])
print(mytwiss.loc['ip5'][['betx','bety','s']])