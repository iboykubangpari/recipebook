def init():
    print("###############################")
    print(f"## weloceme to recipe book app ###" )
    print("###############################")

ingridients = []
recipes = []

def ingred():
    while True:
        foodIngridient = input("please input ingridients, type exit to close ")
        if foodIngridient == 'exit':
            break
        ingridients.append(foodIngridient)
    return ingridients

def rec():
    while True:
        recipe = input("please input reciepe, type exit to close")
        if recipe == 'exit':
            break
        recipes.append(recipe)
    return recipes

def namefood():
    foodname = input("insert food name")
    return foodname

if __name__ == "__main__":
    init()
    foodname = namefood()
    ingreds = ingred()
    reci = rec()

    recipe = {"foodName":foodname,
              "ingredients":ingreds,
              "recipe":reci}

    print(recipe)

