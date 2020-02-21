def cakes(recipe, available):
    '''Function returns the maximum number of cakes that pete can bake based on the recipe and ingredients'''
    if len(recipe) > len(available):
        return 0
    else: 
        ratio = []
        for ingredient in recipe:
            ratio.append(int(available[ingredient]/recipe[ingredient]))
        return min(ratio)
print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))
