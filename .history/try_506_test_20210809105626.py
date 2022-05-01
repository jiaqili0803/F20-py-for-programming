pokemon = [
{
'rattatas': 15,
'eevees': 2,
'ditto': 1,
'magikarps': 3,
'zubats': 8,
'pidgey': 12
},
{
'rattatas': 25,
'eevees': 1,
'magikarps': 7,
'zubats': 3,
'pidgey': 15
},
{
'rattatas':10,
'eevees': 3,
'ditto': 2,
'magikarps': 2,
'zubats': 3,
'pidgey': 20
},
{
'rattatas': 17,
'eevees': 1,
'magikarps': 9,
'zubats': 12,
'pidgey': 14
}
]

r=0
d=0
p=0 

for trainer in pokemon:
    r+=trainer['rattatas']
    p+=trainer['pidgey']
    if 'ditto' in trainer:
        d+=trainer['ditto']
print('total rattatas:',r)
print('total dittos:',d)
print('total pidgeys:',p)
