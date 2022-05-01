pokemon_go_data = [
    {
    'Rattata':203, 'b':2, 'c':7, 
    'd':14, 'e':17, 'f':8, 
    'g':7, 'h':8, 'i':14
    },   
    {
    'a':8, 'Rattata':245, 'c':7, 
    'd':14, 'e':17, 'f':8, 
    'g':7, 'h':8, 'i':14
    },
    {
    'Rattata':32, 'Rattata':245, 'c':7, 
    'd':14, 'e':17, 'f':8, 
    'g':7, 'h':8, 'i':14
    },
    {
    'a':8, 'Rattata':245, 'Rattata':107, 
    'd':14, 'e':17, 'f':8, 
    'g':7, 'h':8, 'i':14
    }
]

candy_count = {}
for dict in pokemon_go_data:
    
    
    most_candied_pokemon = list(candy_count.keys())[0]
    for pokemon in candy_count.keys():
        
        if candy_count[pokemon] > candy_count[most_candied_pokemon]:
            most_candied_pokemon = pokemon
            
            print(most_candied_pokemon)
            
        else:
            candy_count[key] += dict[key]