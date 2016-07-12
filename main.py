import pip

retcode = pip.main(['install', '--disable-pip-version-check', '--no-cache-dir', '--cert=/tmp/cacert.pem', 'pandas'])

print(retcode)

import sys
print(sys.version_info)

import pandas as pd

df = pd.DataFrame({'a':{'A':13,'B':17},'b':{'A':19, 'B':23}})

with open('out/tables/example.csv', 'w') as f:
    f.write(df.to_csv(index=False, quoting=1))