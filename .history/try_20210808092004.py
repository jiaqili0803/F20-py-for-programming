cars = [
    {'name':'exploer', 'marker':'ford', 'price':34104},   
    {'name':'bolt', 'marker':'cglevrolet', 'price':37495}, 
    {'name':'camry', 'marker':'toyota', 'price':25380}, 
    {'name':'civic', 'marker':'honda', 'price':20805}
]


carprices = {}

for c in cars:
    n = c['name']
    p = c['price']
    carprices[n] = p  
    
print(carprices)

    
