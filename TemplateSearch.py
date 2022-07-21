import pprint
import pandas as pd

input_json = 'myJson.json'
df = pd.read_json(input_json)
first = len(df['publications'])
indilist = []
for x in range(0,first):
    indicators = (df['publications'][x]['indicators'])
    indilist.append(indicators)
with open('MyList.txt', 'w') as fp:
    for ind in indilist:
      fp.write("%s\n" % ind)