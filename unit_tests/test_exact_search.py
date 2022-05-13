import pytest
from pathlib import Path
from modules.recipe import Recipe
from modules.recipelist import RecipeList
from modules.esearch import exact_search


USER_INPUT = ['flour', 'sugar', 'butter', 'apples']
ANNOYING_USER_INPUT = ['Flour', 'SUGAR', 'butTeR', 'blueBERRIES']
SINGULAR_USER_INPUT = ['Flour', 'sugar', 'Butter', 'apple']
ONION_ENJOYER_INPUT = ['bread', 'onion', 'ham', 'lettuce']
ONION_SOUP_ENJOYER_INPUT = ['bread', 'onion soup', 'ham', 'lettuce']
WEIRD_USER_INPUT = ['strawberry', 'chicken', 'broccoli']


@pytest.fixture
def rlist():
    path = Path("./unit_tests/example.json")
    recipelist = RecipeList([path])
    return recipelist


@pytest.fixture
def search(rlist):
    result = exact_search(USER_INPUT, rlist)
    return result 


def test_exact_search(search):
    """
    Output should be a list
    Each item in the list should be a Recipe instance
    Capitalization shouldn't matter for the user input
    """
    #The first argument is the user's input, this user input is a list of ingredients, the second argument is the list of dictionaries
    assert isinstance(search, list) == True

    #To access the ingredients key inside the RECIPES_LIST, iterate over it and use .ingredients with the iterated dictionary eg.for recipe in RECIPE_LIST, if recipe['ingredients']...       


def test_exact_search_output_item(search):
    #The list should contain only dictionaries
    assert isinstance(search[0], Recipe) == True



def test_exact_search_working(search):
    #Checks if the exact match function worked, since only one item in the list matches those same ingredients
    assert search[0].name == "Apple Pie"  


def test_irregular_input(rlist):
    #Checks if the exact match function works even if the user doesn't know how to turn off their caps or stop holding shift
    result = exact_search(ANNOYING_USER_INPUT, rlist)
    assert isinstance(result, list) == True
    assert result[0].name == "Blueberry Pie"


def test_plural_input(rlist):
    #Checks if the exact_search function works even if the user forgets to make the word plural
    result = exact_search(SINGULAR_USER_INPUT, rlist)
    assert isinstance(result, list) == True
    assert result[0].name == "Apple Pie"


def test_exact_ingredient(rlist):
    #Checks if it only matches with the ingredient and not ingredients with that share the same ingredient, eg. onions and onion soup
    result = exact_search(ONION_ENJOYER_INPUT, rlist)
    assert isinstance(result, list) == True
    assert len(result) == 1
    assert result[0].name == "Sandwich with Onions"


def test_exact_ingredient_two(rlist):
    #Checks if it only matches with the ingredient and not ingredients with that share the same ingredient, eg. onions and onion soup
    result = exact_search(ONION_SOUP_ENJOYER_INPUT, rlist)
    assert isinstance(result, list) == True
    assert len(result) == 1
    assert result[0].name == "Onion Soup & Bread"


def test_for_punctuated_ingredients(rlist):
    #Checks for weirdly punctuated recipes, if any
    result = exact_search(WEIRD_USER_INPUT, rlist)
    assert isinstance(result, list) == True
    assert len(result) == 1
    assert result[0].name == "Weirdly Punctuated Recipe"
