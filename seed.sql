-- Create Timetable for Under_weight
INSERT INTO Under_weight3 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Bread and tea', 'Jollof rice and Chicke/Meat', 'Eba and Vegetable soup'),
  ('Monday', 'Yam and Egg', 'Beans', 'Pasta(White)'),
  ('Tueday', 'Oatmeal', 'Rice and Beef Stew', 'Tofu'),
  ('Wenesday', 'Bread and tea', 'Beans and Pap', 'Wheat and Egusi Soup'),
  ('Thursday', 'Fried Potatoes ', 'Watermellon', 'Rice and Tomatoe Stew'),
  ('Friday', 'Bread, Egg and tea', 'Jollof Spaghetti', 'Fufu and Edikang Ikang soup'),
  ('Saturday', 'Beans cake(Akara)', 'Pasta(white)', 'Eko and Vegetable Soup');

-- Create Grocery List
INSERT INTO Under_weight3_Grocery (Date, Item) VALUES 
  ('Sunday', 'Bread, Tea ,  Vegetable Leaf, rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat, Chicken, Garri'),
  ('Monday', 'Yam, Egg, Beans, Spaghetti,Tomatoes, Pepper, Maggi, Salt '),
  ('Tueday', 'Oatmeal, rice, Spaghetti/Indomie'),
  ('Wenesday', 'Bread, tea, Beans, Pap, Wheat, Melon,,Tomatoes, Pepper, Maggi, Salt '),
  ('Thursday', 'Potatoes, Watermellon, rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Friday', 'Bread, Egg , tea, Spaghetti, Tomatoes, Pepper, Maggi , Garri, Salt, Bitterleaf '),
  ('Saturday', 'Grounded beans, Tomatoes, Pepper, Maggi ,  Salt, Eko, Vegetable Leaf');

  
-- Create Timetable for Normal_weight
INSERT INTO Normal_weight3 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Bread and tea', 'Jollof rice and Chicke/Meat', 'Eba and Vegetable soup'),
  ('Monday', 'Yam and Egg', 'Beans', 'Pasta(White)'),
  ('Tueday', 'Apple Fruit', 'Rice and Beef Stew', 'Wheat and Vegetable soup'),
  ('Wenesday', 'Sweet Potatoes', 'Tofu', 'Semovita and Ogbono Soup'),
  ('Thursday', 'Bread and tea ', 'Beans', 'Rice and Tomatoe Stew'),
  ('Friday', 'Bread, Egg and tea', 'Jollof Spaghetti', 'FufU and Edi Ikiankon soup'),
  ('Saturday', 'Beans cake(Akara)', 'Cucumber(Fruit intake)', 'Jollof Rice');

-- Create Grocery List
INSERT INTO Normal_weight3_Grocery (Date, Item) VALUES 
  ('Sunday', 'Bread, Tea ,  Vegetable Leaf, rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat, Chicken, Garri'),
  ('Monday', 'Yam, Egg, Beans, Spaghetti,Tomatoes, Pepper, Maggi, Salt '),
  ('Tueday', 'Apple, rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat, Wheat flour'),
  ('Wenesday', 'Potatoes, Beans,rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Thursday', 'Bread, Tea, Beans, Rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Friday', 'Bread, Egg , tea, Spaghetti, Tomatoes, Pepper, Maggi , Garri,  Salt, Bitterleaf '),
  ('Saturday', 'Grounded beans, Tomatoes, Rice, Pepper, Maggi ,  Salt, Cucumber');

  

-- Create Timetable for Over_weight
INSERT INTO Over_weight3 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Beans cake(Akara)', 'Fruit Salad', 'Jollof Rice'),
  ('Monday', 'White Spaghetti with Beaf Stew', 'Yam and Garden Egg', 'Wheat and Vegetanble soup'),
  ('Tueday', 'Apple Fruit', 'Tofu', 'Jollof rice'),
  ('Wenesday', 'Beans Cake(Akara)', 'Cucumber', 'Vegetables'),
  ('Thursday', 'Bread and tea ', 'Peas/Almond', 'Eba and Egusi Soup'),
  ('Friday', 'Potatoes(Boiled)', 'Watermellon', 'Fufu and Edi Ikiankon soup'),
  ('Saturday', 'Healthy Body Fast', 'Cucumber(Fruit intakes)', 'Rice and Beans with Beaf Stew');

-- Create Grocery List
INSERT INTO Over_weight3_Grocery (Date, Item) VALUES 
  ('Sunday', 'Grounded beans ,  Fruits, Meat, Rice, Tomatoes, Pepper, Maggi ,  Salt'),
  ('Monday', 'Yam, Garden Egg, Spaghetti, Wheat flour, Vegetable Leaf  Pepper, Maggi, Salt '),
  ('Tueday', 'Apple, beans, Rice, Tomatoes, Pepper, Maggi, eat'),
  ('Wenesday', 'Grounded Beans, Cucumber, Vegetable Leaf'),
  ('Thursday', 'Fruits, Garri, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Friday', 'Watermellon, Garri, Tomatoes, Pepper, Maggi , Garri,  Salt, Bitterleaf '),
  ('Saturday', 'Rice, Tomatoes, Pepper, Maggi ,  Salt, Cucumber');



-- ####################################Vegetarian################################################################

-- Create Timetable for Under_weight
INSERT INTO Vegetarian_UW3 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Bread and tea', 'Jollof rice and Tofu', 'Eba and Vegetable soup'),
  ('Monday', 'Tofu Lettuce Wraps', 'Beans', 'Pasta(White)'),
  ('Tueday', 'Oatmeal', 'Rice and Beef Stew', 'Tofu'),
  ('Wenesday', 'Bread and tea', 'Beans and Pap', 'Wheat and Egusi Soup'),
  ('Thursday', 'Fried Potatoes ', 'Watermellon', 'Rice and Tomatoe Stew'),
  ('Friday', 'Bread and tea', 'Jollof Spaghetti', 'Fufu and Edikang Ikang soup'),
  ('Saturday', 'Beans cake(Akara)', 'Pasta(white)', 'Eko and Vegetable Soup');

-- Create Grocery List
INSERT INTO Vegetarian_UW3_Grocery (Date, Item) VALUES 
  ('Sunday', 'Bread, Tea ,  Vegetable Leaf, rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat, Chicken, Garri'),
  ('Monday', 'Beans, Spaghetti,Tomatoes, Pepper, Maggi, Salt '),
  ('Tueday', 'Oatmeal, rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat, Beans'),
  ('Wenesday', 'Bread, tea, Beans,Wheat flour, Grounded melon, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Thursday', 'Potatoes, Watermellon, Groundnut oil, Rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Friday', 'Bread, Egg , tea, Spaghetti, Tomatoes, Pepper, Maggi , Garri,  Salt, Bitterleaf, Garri'),
  ('Saturday', 'Grounded beans, Tomatoes,Eko, Spaghetti, Pepper, Maggi ,  Salt, Cucumber');

  
-- Create Timetable for Normal_weight
INSERT INTO Vegetarian_NW3 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Bread and tea', 'Jollof rice and Tofu', 'Eba and Vegetable soup'),
  ('Monday', 'Tofu Lettuce Wraps', 'Beans', 'Pasta(White)'),
  ('Tueday', 'Apple Fruit', 'Rice and Beef Stew', 'Wheat with Cream of Mushroom Soup'),
  ('Wenesday', 'Sweet Potatoes', 'Tofu', 'Semovita and Ogbono Soup'),
  ('Thursday', 'Tofu Lettuce Wraps', 'Beans', 'Rice and Tomatoe Stew'),
  ('Friday', 'Bread and tea', 'Jollof Spaghetti', 'Fufu and Edi Ikiankon soup'),
  ('Saturday', 'Beans cake(Akara)', 'Cucumber(Fruit intake)', 'Jollof Rice');

-- Create Grocery List
INSERT INTO Vegetarian_NW3_Grocery (Date, Item) VALUES 
  ('Sunday', 'Bread, Tea ,  Vegetable Leaf, rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat, Chicken, Garri'),
  ('Monday', 'Beans, Spaghetti,Tomatoes, Pepper, Maggi, Salt '),
  ('Tueday', 'Apple, rice, Tomatoes, Pepper, Maggi , Wheat flour, Salt,  Meat, Beans'),
  ('Wenesday', 'Potatoes, Beans,Wheat flour, Semolina, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Thursday', 'Beans, Groundnut oil, Rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Friday', 'Bread, tea, Spaghetti, Tomatoes, Pepper, Maggi , Garri, Salt, Bitterleaf, Garri'),
  ('Saturday', 'Grounded beans, Tomatoes,Eko, Cucumber, rice, Pepper, Maggi ,  Salt, Cucumber');


-- Create Timetable for Over_weight
INSERT INTO Vegetarian_OW3 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Beans cake(Akara)', 'Fruit Salad', 'Jollof Rice'),
  ('Monday', 'White Spaghetti with Beaf Stew', 'Tofu Lettuce Wraps', 'Wheat and Vegetanble soup'),
  ('Tueday', 'Apple Fruit', 'Tofu', 'Jollof rice'),
  ('Wenesday', 'Beans Cake(Akara)', 'Cucumber', 'Vegetables'),
  ('Thursday', 'Bread and tea ', 'Peas/Almond', 'Eba and Egusi Soup'),
  ('Friday', 'Potatoes(Boiled)', 'Watermellon', 'Semovita and Edi Ikiankon soup'),
  ('Saturday', 'Healthy Body Fast', 'Cucumber(Fruit intakes)', 'Rice and Beans with Beaf Stew');

-- Create Grocery List
INSERT INTO Vegetarian_OW3_Grocery (Date, Item) VALUES 
  ('Sunday', 'Grounded beans, Fruits, rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat, Chicken, Garri'),
  ('Monday', 'Beans, Spaghetti,Tomatoes, Pepper, Maggi, Salt, Wheat flour '),
  ('Tueday', 'Apple, rice, Tomatoes, Pepper, Maggi , Beans, Salt,  Meat, Beans'),
  ('Wenesday', 'Grounded beans, Cucumber, Vegetable Leaf'),
  ('Thursday', 'Bread and tea, Fruits, Garri, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Friday', 'Potatoes, Watermellon,Smolina, Tomatoes, Pepper, Maggi , Garri, Garri, Salt, Bitterleaf, Garri'),
  ('Saturday', 'Tomatoes,Eko, Cucumber, rice, Pepper, Maggi ,  Salt, Cucumber');


  -- ####################################Allegies################################################################

-- Create Timetable for Under_weight
INSERT INTO Allegies_UW3 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Bread and tea', 'Jollof rice and Tofu', 'Eba and Vegetable soup'),
  ('Monday', 'Tofu Lettuce Wraps', 'Beans', 'Pasta(White)'),
  ('Tueday', 'Akara(beans cake)', 'Rice and Beef Stew', 'Tofu'),
  ('Wenesday', 'Bread and tea', 'Beans and Pap', 'Amala and Egusi Soup'),
  ('Thursday', 'Fried Potatoes ', 'Watermellon', 'Rice and Tomatoe Stew'),
  ('Friday', 'Bread and tea', 'Jollof Spaghetti', 'Fufu and Edikang Ikang soup'),
  ('Saturday', 'Beans cake(Akara)', 'Pasta(white)', 'Eko and Vegetable Soup');

-- Create Grocery List
INSERT INTO Allegies_UW3_Grocery (Date, Item) VALUES 
  ('Sunday', 'Bread, Tea ,  Vegetable Leaf, rice, Tomatoes, Pepper, Maggi, Garri, Salt, Meat, Chicken'),
  ('Monday', 'Beans, Spaghetti,Tomatoes, Pepper, Maggi, Salt '),
  ('Tueday', 'Grounded beans, rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat, Beans'),
  ('Wenesday', 'Bread, tea, Beans, Grounded Plantain, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Thursday', 'Potatoes, Watermellon, Groundnut oil, Rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Friday', 'Bread, tea, Spaghetti, Tomatoes, Pepper, Maggi , Garri,  Salt, Bitterleaf, Garri'),
  ('Saturday', 'Grounded beans, Tomatoes, Eko, Spaghetti, Pepper, Maggi ,  Salt, Cucumber');


  
-- Create Timetable for Normal_weight
INSERT INTO Allegies_NW3 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Bread and tea', 'Jollof rice and Tofu', 'Eba and Vegetable soup'),
  ('Monday', 'Tofu Lettuce Wraps', 'Beans', 'Pasta(White)'),
  ('Tueday', 'Fruit Salad', 'Rice and Beef Stew', 'Eba with Cream of Beaf Soup'),
  ('Wenesday', 'Sweet Potatoes', 'Tofu', 'Semovita and Ogbono Soup'),
  ('Thursday', 'Tofu Lettuce Wraps', 'Beans', 'Rice and Tomatoe Stew'),
  ('Friday', 'Bread and tea', 'Jollof Spaghetti', 'Fufu and Edi Ikiankon soup'),
  ('Saturday', 'Beans cake(Akara)', 'Grape', 'Jollof Rice');

-- Create Grocery List
INSERT INTO Allegies_NW3_Grocery (Date, Item) VALUES 
  ('Sunday', 'Bread, Tea ,  Vegetable Leaf, rice, Tomatoes, Pepper, Maggi , Salt,  Meat, Chicken, Garri'),
  ('Monday', 'Beans, Spaghetti,Tomatoes, Pepper, Maggi, Salt '),
  ('Tueday', 'Fruit, rice, Tomatoes, Pepper, Maggi , Garri, Salt,  Meat, Beans'),
  ('Wenesday', 'Potatoes, Beans,Wheat flour, Semolina, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Thursday', 'Beans, Groundnut oil, Rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Friday', 'Bread, tea, Spaghetti, Tomatoes, Pepper, Maggi , Garri, Salt, Bitterleaf, Garri'),
  ('Saturday', 'Grounded beans, Tomatoes,Eko, Grape, rice, Pepper, Maggi ,  Salt, Cucumber');


-- Create Timetable for Over_weight
INSERT INTO Allegies_OW3 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Beans cake(Akara)', 'Fruit Salad', 'Jollof Rice'),
  ('Monday', 'White Spaghetti with Beaf Stew', 'Tofu Lettuce Wraps', 'Amala and Vegetanble soup'),
  ('Tueday', 'Fruit Salad', 'Tofu', 'Jollof rice'),
  ('Wenesday', 'Beans Cake(Akara)', 'Berry', 'Vegetables'),
  ('Thursday', 'Bread and tea ', 'Fruit Salad', 'Eba and Egusi Soup'),
  ('Friday', 'Potatoes(Boiled)', 'Orange', 'Fufu and Edi Ikiankon soup'),
  ('Saturday', 'Healthy Body Fast', 'Cucumber', 'Rice and Beans with Beaf Stew');

-- Create Grocery List
INSERT INTO Allegies_OW3_Grocery (Date, Item) VALUES 
  ('Sunday', 'Grounded beans, Fruits, rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat, Chicken, Garri'),
  ('Monday', 'Beans, Spaghetti,Tomatoes, Pepper, Maggi, Salt, Grounded Plantain '),
  ('Tueday', 'Fruit, rice, Tomatoes, Pepper, Maggi , Beans, Salt,  Meat, Beans'),
  ('Wenesday', 'Grounded beans, fruit, Vegetable Leaf'),
  ('Thursday', 'Bread and tea, Fruits, Garri, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Friday', 'Potatoes, Fruit ,Tomatoes, Pepper, Maggi , Garri, Salt, Bitterleaf, Garri'),
  ('Saturday', 'Tomatoes,Eko, Cucumber, rice, Pepper, Maggi ,  Salt, Cucumber');




-- ####################################################################################################
-- #####################People That Eat Twice Daily####################################################

-- Create Timetable for Under_weight
INSERT INTO Under_weight2 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Bread and tea', '', 'Eba and Vegetable soup'),
  ('Monday', 'Yam and Egg', '', 'Pasta(White)'),
  ('Tueday', 'Oatmeal', 'Rice and Beef Stew', ''),
  ('Wenesday', 'Bread and tea', '', 'Wheat and Egusi Soup'),
  ('Thursday', 'Fried Potatoes ', 'Watermellon', 'Rice and Beaf Stew'),
  ('Friday', 'Bread, Egg and tea', 'Jollof Spaghetti', ''),
  ('Saturday', '', 'Pasta(white)', 'Eko and Vegetable Soup');

-- Create Grocery List
INSERT INTO Under_weight2_Grocery (Date, Item) VALUES 
  ('Sunday', 'Bread, Tea ,  Vegetable Leaf, Meat, Chicken, Garri'),
  ('Monday', 'Yam, Egg, Spaghetti,Tomatoes, Pepper, Maggi, Salt '),
  ('Tueday', 'Oatmeal, rice, Tomatoes, Pepper, Maggi, Salt'),
  ('Wenesday', 'Bread, tea, Rice,,Tomatoes, Pepper, Maggi, Salt '),
  ('Thursday', 'Potatoes, Watermellon, rice, Tomatoes, Pepper, Maggi, Salt, Meat'),
  ('Friday', 'Bread, Egg , tea, Spaghetti, Tomatoes, Pepper, Maggi , Salt'),
  ('Saturday', 'Tomatoes, Pepper, Maggi ,  Salt, Eko, Vegetable Leaf');


  
-- Create Timetable for Normal_weight
INSERT INTO Normal_weight2 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', '', 'Jollof rice and Chicke/Meat', 'Eba and Vegetable soup'),
  ('Monday', 'Yam and Egg', 'Beans', ''),
  ('Tueday', 'Apple Fruit', 'Rice and Beef Stew', 'Wheat and Vegetable soup'),
  ('Wenesday', '', 'Tofu', 'Semovita and Ogbono Soup'),
  ('Thursday', ' ', 'Beans', 'Rice and Tomatoe Stew'),
  ('Friday', 'Bread, Egg and tea', '', 'Fufu and Edi Ikiankon soup'),
  ('Saturday', 'Beans cake(Akara)', 'Cucumber(Fruit intake)', 'Jollof Rice');

-- Create Grocery List
INSERT INTO Normal_weight2_Grocery (Date, Item) VALUES 
  ('Sunday', ' Vegetable Leaf, rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat, Chicken, Garri'),
  ('Monday', 'Yam, Egg, Beans,'),
  ('Tueday', 'Apple, Tomatoes, Pepper, Maggi ,  Salt,  Meat, Wheat flour'),
  ('Wenesday', 'Potatoes, Beans, Semolina, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Thursday', 'Beans, Rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Friday', 'Bread, Egg , tea, Tomatoes, Pepper, Maggi , Garri,  Salt, Bitterleaf '),
  ('Saturday', 'Grounded beans, Rice, Tomatoes, Pepper, Maggi ,  Salt, Cucumber');



-- Create Timetable for Over_weight
INSERT INTO Over_weight2 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Beans cake(Akara)', 'Fruit Salad', ''),
  ('Monday', '', 'Yam and Garden Egg', 'Wheat and Vegetanble soup'),
  ('Tueday', 'Apple Fruit', 'Tofu', ''),
  ('Wenesday', '', 'Cucumber', 'Vegetables'),
  ('Thursday', ' ', 'Peas/Almond', 'Eba and Egusi Soup'),
  ('Friday', '', 'Watermellon', 'Fufu and Edi Ikiankon soup'),
  ('Saturday', 'Healthy Body Fast', 'Cucumber(Fruit intakes)', 'Rice and Beans with Beaf Stew');

-- Create Grocery List
INSERT INTO Over_weight2_Grocery (Date, Item) VALUES 
  ('Sunday', 'Grounded beans ,  Fruits'),
  ('Monday', 'Yam, Garden Egg,Wheat flour, Vegetable Leaf  Pepper, Maggi, Salt '),
  ('Tueday', 'Apple, beans'),
  ('Wenesday', 'Cucumber, Vegetable Leaf'),
  ('Thursday', 'Fruits, Garri, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Friday', 'Watermellon, Garri, Tomatoes, Pepper, Maggi , Garri,  Salt, Bitterleaf '),
  ('Saturday', 'Rice, Tomatoes, Pepper, Maggi ,  Salt, Cucumber');


-- ####################################Vegetarian################################################################

-- Create Timetable for Under_weight
INSERT INTO Vegetarian_UW2 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Bread and tea', 'Jollof rice and Tofu', ''),
  ('Monday', 'Tofu Lettuce Wraps', '', 'Pasta(White)'),
  ('Tueday', '', 'Rice and Beef Stew', 'Tofu'),
  ('Wenesday', 'Bread and tea', 'Beans and Pap', ''),
  ('Thursday', '', 'Watermellon', 'Rice and Tomatoe Stew'),
  ('Friday', 'Bread, Egg and tea', '', 'Eba and Edikang Ikang soup'),
  ('Saturday', 'Beans cake(Akara)', '', 'Eko and Vegetable Soup');

-- Create Grocery List
INSERT INTO Vegetarian_UW2_Grocery (Date, Item) VALUES 
  ('Sunday', 'Bread, Tea , rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat, Chicken, Garri'),
  ('Monday', 'Beans, Spaghetti,Tomatoes, Pepper, Maggi, Salt '),
  ('Tueday', 'rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat, Beans'),
  ('Wenesday', 'Bread, tea, Beans, Pap'),
  ('Thursday', 'Watermellon, Groundnut oil, Rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Friday', 'Bread, Egg , tea, Tomatoes, Pepper, Maggi , Garri,  Salt, Bitterleaf, Garri'),
  ('Saturday', 'Grounded beans, Tomatoes,Eko, Pepper, Maggi ,  Salt, Cucumber');

  
-- Create Timetable for Normal_weight
INSERT INTO Vegetarian_NW2 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', '', 'Jollof rice and Tofu', 'Eba and Vegetable soup'),
  ('Monday', 'Tofu Lettuce Wraps', 'Beans', ''),
  ('Tueday', 'Apple Fruit', 'Rice and Beef Stew', 'Wheat with Cream of Mushroom Soup'),
  ('Wenesday', '', 'Tofu', 'Semovita and Ogbono Soup'),
  ('Thursday', 'Tofu Lettuce Wraps', '', 'Rice and Tomatoe Stew'),
  ('Friday', 'Bread and tea', 'Jollof Spaghetti', ''),
  ('Saturday', 'Beans cake(Akara)', 'Cucumber(Fruit intake)', 'Jollof Rice');

-- Create Grocery List
INSERT INTO Vegetarian_NW2_Grocery (Date, Item) VALUES 
  ('Sunday', 'Vegetable Leaf, rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat, Chicken, Garri'),
  ('Monday', 'Beans, Pepper, Maggi, Salt '),
  ('Tueday', 'Apple, rice, Tomatoes, Pepper, Maggi , Wheat flour, Salt,  Meat, Beans'),
  ('Wenesday', ' Beans, Semolina, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Thursday', 'Beans, Groundnut oil, Rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Friday', 'Bread, tea, Spaghetti, Tomatoes, Pepper, Maggi'),
  ('Saturday', 'Grounded beans, Tomatoes,Eko, Cucumber, rice, Pepper, Maggi ,  Salt, Cucumber');


-- Create Timetable for Over_weight
INSERT INTO Vegetarian_OW2 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Beans cake(Akara)', 'Fruit Salad', 'Jollof Rice'),
  ('Monday', '', 'Tofu Lettuce Wraps', 'Wheat and Vegetanble soup'),
  ('Tueday', 'Apple Fruit', 'Tofu', 'Jollof rice'),
  ('Wenesday', '', 'Cucumber', 'Vegetables'),
  ('Thursday', 'Bread and tea ', 'Peas/Almond', 'Eba and Egusi Soup'),
  ('Friday', 'Potatoes(Boiled)', 'Watermellon', ''),
  ('Saturday', 'Healthy Body Fast', 'Cucumber(Fruit intakes)', 'Rice and Beans with Beaf Stew');

-- Create Grocery List
INSERT INTO Vegetarian_OW2_Grocery (Date, Item) VALUES 
  ('Sunday', 'Grounded beans, Fruits, rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat, Chicken'),
  ('Monday', 'Beans, Tomatoes, Pepper, Maggi, Salt, Wheat flour '),
  ('Tueday', 'Apple, rice, Tomatoes, Pepper, Maggi , Beans, Salt,  Meat, Beans'),
  ('Wenesday', 'Cucumber, Vegetable Leaf'),
  ('Thursday', 'Bread and tea, Fruits, Garri, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Friday', 'Potatoes, Watermellon'),
  ('Saturday', 'Tomatoes, Cucumber, rice, Pepper, Maggi ,  Salt, Cucumber');




  -- ####################################Vegetarian################################################################

-- Create Timetable for Under_weight
INSERT INTO Allegies_UW2 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', '', 'Jollof rice and Tofu', 'Eba and Vegetable soup'),
  ('Monday', 'Tofu Lettuce Wraps', '', 'Pasta(White)'),
  ('Tueday', 'Akara(beans cake)', 'Rice and Beef Stew', ''),
  ('Wenesday', '', 'Beans and Pap', 'Amala and Egusi Soup'),
  ('Thursday', 'Fried Potatoes ', 'Watermellon', 'Rice and Tomatoe Stew'),
  ('Friday', '', 'Jollof Spaghetti', 'Fufu and Edikang Ikang soup'),
  ('Saturday', 'Beans cake(Akara)', '', 'Eko and Vegetable Soup');

-- Create Grocery List
INSERT INTO Allegies_UW2_Grocery (Date, Item) VALUES 
  ('Sunday', '  Vegetable Leaf, rice, Tomatoes, Pepper, Maggi, Salt, Meat, Chicken,'),
  ('Monday', 'Beans, Spaghetti,Tomatoes, Pepper, Maggi, Salt '),
  ('Tueday', 'Grounded beans, rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat, Beans'),
  ('Wenesday', ', Beans, Grounded Plantain, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Thursday', 'Potatoes, Watermellon, Vegetable, Rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Friday', 'Bread, tea, Spaghetti, Tomatoes, Pepper, Maggi , Garri,  Salt, Bitterleaf, Garri'),
  ('Saturday', 'Grounded beans, Tomatoes, Eko, Spaghetti, Pepper, Maggi ,  Salt, Cucumber');



  
-- Create Timetable for Normal_weight
INSERT INTO Allegies_NW2 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', '', 'Jollof rice and Tofu', 'Eba and Vegetable soup'),
  ('Monday', 'Tofu Lettuce Wraps', '', 'Pasta(White)'),
  ('Tueday', 'Fruit Salad', 'Rice and Beef Stew', 'Eba with Cream of Beaf Soup'),
  ('Wenesday', '', 'Tofu', 'Amala and Ogbono Soup'),
  ('Thursday', 'Tofu Lettuce Wraps', '', 'Rice and Tomatoe Stew'),
  ('Friday', '', 'Jollof Spaghetti', 'Fufu and Edi Ikiankon soup'),
  ('Saturday', 'Beans cake(Akara)', 'Grape', 'Jollof Rice');

-- Create Grocery List
INSERT INTO Allegies_NW2_Grocery (Date, Item) VALUES 
  ('Sunday', ' Vegetable Leaf, rice, Tomatoes, Pepper, Maggi , Salt,  Meat, Chicken, Garri'),
  ('Monday', 'Beans, Spaghetti,Tomatoes, Pepper, Maggi, Salt '),
  ('Tueday', 'Fruit, rice, Tomatoes, Pepper, Garri, Maggi , Garri, Salt,  Meat, Beans'),
  ('Wenesday', 'Potatoes, Beans, Grounded Plantain, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Thursday', 'Beans, vegetable, Rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Friday', 'Bread, tea, Spaghetti, Tomatoes, Pepper, Maggi , Garri, Salt, Bitterleaf, Garri'),
  ('Saturday', 'Grounded beans, Tomatoes,Eko, Grape, rice, Pepper, Maggi ,  Salt, Cucumber');


-- Create Timetable for Over_weight
INSERT INTO Allegies_OW2 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Beans cake(Akara)', 'Fruit Salad', 'Jollof Rice'),
  ('Monday', 'White Spaghetti with Beaf Stew', '', 'Amala and Vegetanble soup'),
  ('Tueday', 'Fruit Salad', '', 'Jollof rice'),
  ('Wenesday', 'Beans Cake(Akara)', 'Berry', 'Vegetables'),
  ('Thursday', '', 'Fruit Salad', 'Eba and Egusi Soup'),
  ('Friday', 'Potatoes(Boiled)', 'Orange', 'Eba and Edi Ikiankon soup'),
  ('Saturday', 'Healthy Body Fast', 'Cucumber', 'Rice and Beans with Beaf Stew');
  
  -- Create Grocery List
INSERT INTO Allegies_OW2_Grocery (Date, Item) VALUES 
  ('Sunday', 'Grounded beans, Fruits, rice, Tomatoes, Pepper, Maggi ,  Salt,  Meat, Chicken, Garri'),
  ('Monday', 'Beans, Spaghetti,Tomatoes, Pepper, Maggi, Salt, Grounded Plantain '),
  ('Tueday', 'Fruit, rice, Tomatoes, Pepper, Maggi , Beans, Salt,  Meat, Beans'),
  ('Wenesday', 'Grounded beans, fruit, Vegetable Leaf'),
  ('Thursday', ', Fruits, Garri, Tomatoes, Pepper, Maggi ,  Salt,  Meat'),
  ('Friday', 'Potatoes, Fruit ,Tomatoes, Pepper, Maggi , Garri, Salt, Bitterleaf, Garri'),
  ('Saturday', 'Tomatoes,Eko, Cucumber, rice, Pepper, Maggi ,  Salt, Cucumber');

-- Insert into stress_management_resources table
INSERT INTO stress_management_resources (title, description, link) VALUES 
('How to Relieve Stress', 'This video is made for you to relieve any form of stress or depression', 'https://youtu.be/xLd6PBx6xUI');
INSERT INTO stress_management_resources (title, description, link) VALUES 
('Relaxation', 'You just have to listen to this beautifull music to ace your mind and make you think clearly', 'https://youtu.be/FXcfQ0atNK4');
-- Insert into stress_management_resources table
INSERT INTO stress_management_resources (title, description, link) VALUES 
('Meditation', 'Help to meditate and concentrate on your surroundings', 'https://youtu.be/Lm4-VgILXJ0');
INSERT INTO stress_management_resources (title, description, link) VALUES 
('Meditation', 'Teaches on how to meditate', 'https://youtube.com/shorts/YbF-GvP4rxY?feature=share4');
-- Insert into stress_management_resources table
INSERT INTO stress_management_resources (title, description, link) VALUES 
('Stress Training', 'Teaches you  how to calm down nerves to prepare you for a task', 'https://youtu.be/w6qSTR1p0IY');
INSERT INTO stress_management_resources (title, description, link) VALUES 
('Relaxation', 'Make you feel relax with a wonderful sound for rest or sleep', 'https://youtu.be/mqa9pn7GsN4');