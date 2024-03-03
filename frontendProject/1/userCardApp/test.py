def fruitImgUrl(fruit):
    fruits={"banana":"url1","pineapple":"url2","pear":"url3"}
    if fruit.lower() in fruits:
        return fruits[fruit.lower()]
    else:
        return "no image"