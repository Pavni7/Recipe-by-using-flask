from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample recipe data (you can use a database in a real-world application)
recipes = [
    {
        'id': 1,
        'title': 'Biryani',
        'ingredients': '1 kg chicken, cut into pieces,1 cup yogurt,1 tablespoon ginger paste,1 tablespoon garlic paste,1 teaspoon red chili powder,1/2 teaspoon turmeric powder,Salt, to taste,2 cups basmati rice,Water for soaking and cooking,Whole spices (bay leaves, cloves, cardamom pods, cinnamon sticks)',
        'instructions': 'Marinating the chicken,Cooking the rice,Assembling the Biriyani,Dum cooking,Serving.... ',
    },
    {
        'id': 2,
        'title': 'Lemon rice',
        'ingredients': ' 2 cups cooked and cooled rice (preferably day-old,)1 lemon,2 tablspoons vegetable oil,1/2 teaspoon mustard seeds,1/2 teaspoon cumin seeds,1/4 teaspoon asafoetida (hing) powder (optional),1/4 teaspoon turmeric powder,1-2 green chilies, choppedA few curry leavesSalt, to tasteRoasted peanuts, for garnish (optional),Chopped cilantro (coriander leaves), for garnish...',
        'instructions': ' Prepration,Tempering,Chillies and Curry leaves,Mixing rice,Lemon Juice,Salt and Garnishes,Finishing Touch,Garnish and serve...',

    },
    {
        'id': 3,
        'title': 'Payasam',
        'ingredients': '1/2 cup basmati rice (you can also use broken rice),4 cups whole milk,1/2 cup sugar (adjust to taste),1/4 teaspoon cardamom powder,A pinch of saffron strands (optional),2 tablespoons ghee (clarified butter),Assorted nuts (almonds, cashews, and raisins), chopped',
        'instructions': 'Rinse the rise,fry the nuts,cook the rice,Add Milk,Add Saffron,Simmer,Add Sugar,Add Carddamom,Add Fried Nuts,final touches,Serve.....',
        'image_url': '/static/payasam.webp',
        'category': 'veg'
    },
    {
        'id': 4,
        'title': 'Tandoori Chicken',
        'ingredients': '4 boneless chicken breasts, 1 cup plain yogurt, 2 tablespoons tandoori masala, 1 tablespoon lemon juice, 1 tablespoon ginger paste, 1 tablespoon garlic paste, 1 teaspoon red chili powder, 1/2 teaspoon turmeric powder, Salt, to taste, 2 tablespoons vegetable oil, Chopped cilantro and lemon wedges for garnish',
        'instructions': '1. In a bowl, mix yogurt, tandoori masala, lemon juice, ginger paste, garlic paste, red chili powder, turmeric powder, salt, and vegetable oil.\n2. Make shallow cuts on the chicken breasts and coat them with the marinade. Marinate for at least 2 hours, or preferably overnight.\n3. Preheat the oven to 400°F (200°C).\n4. Place the marinated chicken on a baking sheet lined with parchment paper.\n5. Bake in the preheated oven for about 25-30 minutes or until the chicken is cooked through and slightly charred on the edges.\n6. Garnish with chopped cilantro and serve with lemon wedges.',
        'image_url': '/static/tandoori.jpeg',
        'category': 'non_veg'

    },
    {
        'id': 5,
        'title': 'Mango Pickle',
        'ingredients': '3 raw mangoes, 1/4 cup mustard oil, 2 tablespoons mustard seeds, 1 teaspoon fenugreek seeds, 1/2 teaspoon turmeric powder, 1 tablespoon red chili powder, Salt, to taste',
        'instructions': '1. Wash and dry the mangoes thoroughly. Cut them into small pieces and remove the seeds.\n2. In a dry skillet, lightly roast the mustard seeds and fenugreek seeds. Allow them to cool and then grind them to a fine powder.\n3. In a mixing bowl, combine the mango pieces, mustard-fenugreek powder, turmeric powder, red chili powder, and salt.\n4. Heat the mustard oil in a pan until it starts to smoke. Remove it from the heat and let it cool slightly.\n5. Pour the cooled oil over the mango mixture and mix well.\n6. Transfer the pickle to a clean and dry glass jar. Close the lid and let it sit in a warm place for a day.\n7. Stir the pickle once or twice a day for the next few days.\n8. After a week, the mango pickle will be ready to enjoy. Store it in the refrigerator.',
        'image_url': '/static/avakai-mango-pickle.webp',
        'category': 'veg'
    },
    {
        'id': 6,
        'title': 'Momos (Dumplings)',
        'ingredients': 'For the dough:\n2 cups all-purpose flour, Water, as needed, Salt, to taste\nFor the filling:\n1 cup ground chicken or vegetables, 1 small onion, finely chopped, 2 cloves garlic, minced, 1/2 teaspoon ginger paste, 1/2 teaspoon soy sauce, 1/2 teaspoon sesame oil, Salt and pepper, to taste, Chopped cilantro, for garnish',
        'instructions': '1. In a bowl, mix the all-purpose flour and a pinch of salt. Gradually add water and knead to form a smooth dough. Cover and let it rest for about 30 minutes.\n2. For the filling, combine the ground chicken or vegetables, chopped onion, minced garlic, ginger paste, soy sauce, sesame oil, salt, and pepper in a bowl.\n3. Roll out small portions of the dough into thin circles.\n4. Place a spoonful of the filling in the center of each dough circle.\n5. Fold the dough over the filling and pinch the edges to seal the momos. You can shape them into half-moon or circular dumplings.\n6. Steam the momos in a steamer for about 8-10 minutes or until the dough becomes translucent and the filling is cooked.\n7. Garnish with chopped cilantro and serve hot with dipping sauces like soy sauce or chili sauce.',
        'image_url': '/static/momos.jpeg',
        'category': 'non_veg'
    },
    {
        'id': 7,
        'title': 'Pasta with Tomato Sauce',
        'ingredients': '2 cups pasta, 1 cup tomato sauce, 1/2 cup grated Parmesan cheese, 2 tablespoons olive oil, 2 cloves garlic, minced, 1/2 teaspoon dried basil, 1/2 teaspoon dried oregano, Salt and pepper, to taste, Chopped fresh basil, for garnish',
        'instructions': '1. Cook the pasta according to package instructions until al dente. Drain and set aside.\n2. In a saucepan, heat the olive oil over medium heat. Add minced garlic and sauté for about 1 minute until fragrant.\n3. Add the tomato sauce, dried basil, dried oregano, salt, and pepper. Simmer for 5-10 minutes.\n4. Toss the cooked pasta in the tomato sauce.\n5. Serve the pasta in bowls, topped with grated Parmesan cheese and chopped fresh basil.',
        'image_url': '/static/pasta.jpeg',
        'category': 'veg'
    },
    {
        'id': 8,
        'title': 'Chicken Curry',
        'ingredients': '1 lb boneless chicken, cut into pieces, 1 onion, finely chopped, 2 tomatoes, chopped, 2 cloves garlic, minced, 1 teaspoon ginger paste, 1 teaspoon curry powder, 1/2 teaspoon turmeric powder, 1/2 teaspoon cumin powder, 1/2 teaspoon coriander powder, 1/4 teaspoon red chili powder (adjust to taste), Salt, to taste, 2 tablespoons cooking oil, Chopped fresh cilantro, for garnish',
        'instructions': '1. Heat oil in a pan over medium heat. Add chopped onions and sauté until golden brown.\n2. Add minced garlic and ginger paste. Sauté for a minute until fragrant.\n3. Add chopped tomatoes and cook until they turn soft.\n4. Stir in curry powder, turmeric, cumin, coriander, red chili powder, and salt.\n5. Add chicken pieces and cook until they are cooked through and the curry thickens.\n6. Garnish with chopped cilantro and serve with rice or bread.',
        'image_url': '/static/chicken.jpeg',
        'category': 'non_veg'

    },
    {
        'id': 9,
        'title': 'Chocolate Chip Cookies',
        'ingredients': '1 cup butter, softened, 3/4 cup granulated sugar, 3/4 cup packed brown sugar, 1 teaspoon vanilla extract, 2 large eggs, 2 1/4 cups all-purpose flour, 1 teaspoon baking soda, 1/2 teaspoon salt, 2 cups chocolate chips',
        'instructions': '1. Preheat the oven to 375°F (190°C).\n2. In a mixing bowl, cream together the softened butter, granulated sugar, brown sugar, and vanilla extract until creamy.\n3. Add eggs, one at a time, beating well after each addition.\n4. In a separate bowl, whisk together the flour, baking soda, and salt. Gradually add this dry mixture to the butter mixture, mixing until well combined.\n5. Stir in the chocolate chips.\n6. Drop rounded tablespoons of cookie dough onto ungreased baking sheets.\n7. Bake for 9-11 minutes or until the edges are golden brown.\n8. Allow the cookies to cool on the baking sheets for a few minutes, then transfer them to wire racks to cool completely.',
        'image_url': '/static/chocolate_chip.jpeg',
        'category': 'veg'
    },
    {
        'id': 10,
        'title': 'Vegetable Fried Rice',
        'ingredients': '2 cups cooked rice (preferably day-old), 1 cup mixed vegetables (carrots, peas, bell peppers, etc.), 2 eggs, beaten, 3 tablespoons soy sauce, 1 tablespoon oyster sauce, 1/2 teaspoon sesame oil, 1/4 teaspoon white pepper, 2 tablespoons cooking oil, 2 cloves garlic, minced, Salt, to taste, Chopped green onions, for garnish',
        'instructions': '1. Heat 1 tablespoon of cooking oil in a pan over medium heat. Add beaten eggs and scramble them. Set the scrambled eggs aside.\n2. In the same pan, add another tablespoon of cooking oil. Add minced garlic and sauté for a minute.\n3. Add the mixed vegetables and stir-fry until they are cooked but still slightly crunchy.\n4. Push the vegetables to one side of the pan and add the cooked rice to the other side. Pour soy sauce, oyster sauce, sesame oil, and white pepper over the rice.\n5. Mix everything together and stir-fry for a few minutes until the rice is heated through.\n6. Stir in the scrambled eggs.\n7. Season with salt, if needed.\n8. Garnish with chopped green onions and serve.',
        'image_url': '/static/fried rice.webp',
        'category': 'veg'
    },

    {
        'id': 11,
        'title': 'Paneer Tikka',
        'ingredients': '250g paneer (cottage cheese), 1 cup yogurt, 1 tablespoon ginger-garlic paste, 1 tablespoon red chili powder, 1/2 teaspoon turmeric powder, 1 teaspoon garam masala, Salt, to taste, 1 tablespoon lemon juice, 1 tablespoon oil, Chopped cilantro, for garnish',
        'instructions': '1. Cut paneer into cubes.\n2. Mix yogurt, ginger-garlic paste, red chili powder, turmeric powder, garam masala, salt, lemon juice, and oil in a bowl.\n3. Marinate the paneer cubes in this mixture for at least 30 minutes.\n4. Preheat the oven to 400°F (200°C).\n5. Thread the marinated paneer cubes onto skewers.\n6. Place the skewers on a baking sheet and bake for about 15-20 minutes or until the paneer is slightly charred on the edges.\n7. Garnish with chopped cilantro and serve with mint chutney.',
        'image_url': '/static/tikka.jpeg',

        'category': 'veg'
    },
    {
        'id': 12,
        'title': 'Fish Curry',
        'ingredients': '1 lb fish fillets (any firm fish), 1 onion, finely chopped, 2 tomatoes, chopped, 2 cloves garlic, minced, 1 teaspoon ginger paste, 1 teaspoon curry powder, 1/2 teaspoon turmeric powder, 1/2 teaspoon cumin powder, 1/2 teaspoon coriander powder, 1/4 teaspoon red chili powder (adjust to taste), Salt, to taste, 2 tablespoons cooking oil, Chopped fresh cilantro, for garnish',
        'instructions': '1. Heat oil in a pan over medium heat. Add chopped onions and sauté until golden brown.\n2. Add minced garlic and ginger paste. Sauté for a minute until fragrant.\n3. Add chopped tomatoes and cook until they turn soft.\n4. Stir in curry powder, turmeric, cumin, coriander, red chili powder, and salt.\n5. Add fish fillets and cook until they are cooked through and the curry thickens.\n6. Garnish with chopped cilantro and serve with rice or bread.',
        'image_url': '/static/fish.jpeg',
        'category': 'non_veg'
    },

    {
        'id': 13,
        'title': 'Classic Margherita Pizza',
        'ingredients': 'Pizza dough, Tomato sauce, Fresh mozzarella cheese, Fresh basil leaves, Olive oil, Salt and pepper',
        'instructions': '1. Preheat the oven and roll out the pizza dough.\n2. Spread tomato sauce over the dough.\n3. Top with slices of fresh mozzarella cheese.\n4. Bake until the crust is golden and the cheese is bubbly.\n5. Remove from the oven, sprinkle fresh basil leaves.\n6. Drizzle olive oil, season with salt and pepper.\n7. Slice and enjoy!',
        'image_url': '/static/pizza.jpeg',
        'category': 'veg'
    },
    {
        'id': 14,
        'title': 'Sushi Rolls',
        'ingredients': 'Sushi rice, Nori seaweed sheets, Fresh fish (salmon, tuna, etc.), Avocado, Cucumber, Soy sauce, Wasabi, Pickled ginger',
        'instructions': '1. Prepare sushi rice and cool it.\n2. Lay a nori sheet on a bamboo mat.\n3. Spread rice over the nori, leaving an edge.\n4. Add slices of fish, avocado, and cucumber.\n5. Roll tightly using the bamboo mat.\n6. Slice into bite-sized pieces.\n7. Serve with soy sauce, wasabi, and pickled ginger.',
        'image_url': '/static/sushi.jpeg',
        'category': 'non_veg'
    },
    {
        'id': 15,
        'title': 'Palak Paneer',
        'ingredients': 'Paneer (cottage cheese), Spinach, Onion, Tomato, Ginger-garlic paste, Green chilies, Garam masala, Turmeric powder, Cumin seeds, Cream, Salt, Oil',
        'instructions': '1. Blanch spinach and blend into a puree.\n2. Sauté cumin seeds, add chopped onions, ginger-garlic paste, and green chilies.\n3. Add tomato and spices, cook until the oil separates.\n4. Pour in the spinach puree and cook.\n5. Add cubed paneer and garam masala.\n6. Finish with cream, simmer, and serve with roti or rice.',
        'image_url': '/static/chana.webp',
        'category': 'veg'
    },
    {
        'id': 16,
        'title': 'Chana Masala',
        'ingredients': 'Chickpeas, Onion, Tomato, Ginger-garlic paste, Green chilies, Cumin seeds, Garam masala, Turmeric powder, Coriander powder, Amchur (dried mango powder), Fresh coriander leaves, Oil',
        'instructions': '1. Cook chickpeas until tender.\n2. Sauté cumin seeds, add chopped onions, ginger-garlic paste, and green chilies.\n3. Add tomato and spices, cook until the oil separates.\n4. Add cooked chickpeas and amchur.\n5. Garnish with fresh coriander leaves.\n6. Serve with roti, rice, or puri.',
        'image_url': '/static/chana.webp',
        'category': 'veg'
    },
    {
        'id': 17,
        'title': 'Aloo Gobi',
        'ingredients': 'Potatoes, Cauliflower, Onion, Tomato, Ginger-garlic paste, Turmeric powder, Cumin seeds, Garam masala, Coriander powder, Red chili powder, Fresh coriander leaves, Oil',
        'instructions': '1. Heat oil, add cumin seeds, sauté onions.\n2. Add ginger-garlic paste, tomato, and spices.\n3. Add potatoes and cauliflower florets.\n4. Cook covered until vegetables are tender.\n5. Garnish with fresh coriander leaves.\n6. Serve with roti or rice.',
        'category': 'veg',
        'image_url': '/static/mushroom.jpeg'

    },
    {
        'id': 18,
        'title': 'Butter Chicken',
        'ingredients': 'Boneless chicken, Butter, Onion, Tomato, Ginger-garlic paste, Cream, Garam masala, Red chili powder, Kasuri methi (dried fenugreek leaves), Fresh coriander leaves, Oil',
        'instructions': '1. Marinate chicken with yogurt and spices.\n2. Grill or cook the chicken until done.\n3. Sauté onions, ginger-garlic paste, tomato.\n4. Blend and strain the mixture.\n5. Add butter, cream, garam masala, and kasuri methi.\n6. Add grilled chicken and cook until coated.\n7. Garnish with fresh coriander leaves.\n8. Serve with naan or rice.',
        'category': 'non_veg',
        'image_url': '/static/butter.jpeg'
    },
    {
        'id': 19,
        'title': 'Mushroom Tikka Masala',
        'ingredients': 'Button mushrooms, Onion, Tomato, Ginger-garlic paste, Yogurt, Cashew nuts, Garam masala, Turmeric powder, Red chili powder, Fresh coriander leaves, Oil',
        'instructions': '1. Marinate mushrooms with yogurt, spices, and ginger-garlic paste.\n2. Grill or cook the marinated mushrooms.\n3. Sauté onions, ginger-garlic paste, and tomato.\n4. Blend and strain the mixture with soaked cashews.\n5. Add garam masala, turmeric, red chili powder.\n6. Add cooked mushrooms and simmer.\n7. Garnish with fresh coriander leaves.\n8. Serve with naan or rice.',
        'image_url': '/static/mushroom.jpeg',
        'category': 'veg'
    },
    {
        'id': 20,
        'title': 'Mutton Biryani',
        'ingredients': 'Mutton, Basmati rice, Onion, Tomato, Ginger-garlic paste, Biryani masala, Turmeric powder, Red chili powder, Saffron strands, Fresh coriander leaves, Ghee',
        'instructions': '1. Marinate Mutton with yogurt, biryani masala, and spices.\n2. Parboil basmati rice with whole spices.\n3. Sauté onions, ginger-garlic paste, and tomato.\n4. Add marinated chicken and cook.\n5. Layer cooked rice and chicken in a pot.\n6. Add saffron-infused milk and ghee.\n7. Dum cook until the rice is fully cooked.\n8. Garnish with fresh coriander leaves.\n9. Serve the aromatic biryani.',
        'image_url': '/static/MuttonBiryani.webp',
        'category': 'non_veg'
    }

]
vegetarian_recipes = []  # List to store vegetarian recipes
# type: ignore # List to store non-vegetarian recipes

non_veg_recipes = []  # type: ignore


@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)


'''
@app.route('/veg')
def veg_recipes():
    veg_recipes = [
        recipe for recipe in recipes if recipe.get('category') == 'veg']
    return render_template('veg_recipes.html', recipes=veg_recipes)


@app.route('/non_veg')
def non_veg_recipes():
    non_veg_recipes = [
        recipe for recipe in recipes if recipe.get('category') == 'non_veg']
    return render_template('non_veg_recipes.html', recipes=non_veg_recipes)

'''


@app.route('/vegetarian_recipes')
def veg_recipes():
    veg_recipes = [
        recipe for recipe in recipes if recipe.get('category') == 'veg'
    ]
    return render_template('veg_recipes.html', recipes=veg_recipes)


@app.route('/non_veg_recipes')
def non_veg_recipes():
    non_veg_recipes = [
        recipe for recipe in recipes if recipe.get('category') == 'non_veg'
    ]
    return render_template('non_veg_recipes.html', recipes=non_veg_recipes)


@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    if recipe:

        return render_template('recipe.html', recipe=recipe)
    else:
        return "Recipe not found.", 404


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        category = request.form['category']

        new_recipe = {
            'id': len(recipes) + 1,
            'title': title,
            'ingredients': ingredients,
            'instructions': instructions,
            'category': category
        }
        recipes.append(new_recipe)
        if category == 'veg':
            # Append to the vegetarian_recipes list
            vegetarian_recipes.append(new_recipe)
        elif category == 'non_veg':
            non_veg_recipes.append(new_recipe)
        return redirect(url_for('index'))

    return render_template('add_recipe.html')


@app.route('/veg_recipes')
def vegg_recipes():
    veg_recipes = [recipe for recipe in recipes if recipe['category'] == 'veg']
    return render_template('veg_recipes.html', recipes=veg_recipes)


@app.route('/non_veg_recipes')
def non_vegg_recipes():
    non_vegg_recipes = [
        recipe for recipe in recipes if recipe['category'] == 'non_veg']
    return render_template('non_veg_recipes.html', recipes=non_vegg_recipes)


if __name__ == '__main__':
    app.run(debug=True)
# project sucess