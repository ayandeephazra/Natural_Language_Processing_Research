import json
with open('lattice') as a:
    p=json.load(a)
print(json.dumps(p,indent=1))

with open('bulk') as a:
    p=json.load(a)
print(json.dumps(p,indent=1))

with open('bandgap') as a:
    p=json.load(a)
print(json.dumps(p,indent=1))

