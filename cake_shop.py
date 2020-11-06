
# Uncomment the following line for debugging
# import pdb

cakes = [
    {
      "name": "Brownie",
      "ingredients":[ "chocolate", "cocoa powder", "flour", "eggs", "sugar", "butter" ],
      "rating": 5
    },
    {
      "name": "Carrot Cake",
      "ingredients":[ "carrots", "raisins", "cinnamon", "flour", "eggs", "sugar", "butter" ],
      "rating": 2.5
    },
    {
      "name": "Lemon Drizzle",
      "ingredients":[ "lemon juice", "flour", "eggs", "sugar", "butter" ],
      "rating": 1.5
    }
]

def get_average_rating(cakes):

    # Uncomment the following line in order to debug the program...
    # pdb.set_trace()

    # Could have coded the above line as:
    # import pdb; pdb.set_trace()

    ratings = []

    for cake in cakes:
        ratings.append(cake["rating"])

    ratings_total = sum(ratings)
    number_of_cakes = len(cakes)
    average = ratings_total / number_of_cakes

    return average

print(get_average_rating(cakes))

# n - next lineof code
# l - code listing, pointing out current line
# any variable name - shows value (if the variable exists)
# c - to get you out of the loop
