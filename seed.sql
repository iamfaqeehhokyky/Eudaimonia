-- Create Timetable for Under_weight
INSERT INTO Under_weight3 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Bread and tea', 'Jollof rice and Chicke/Meat', 'Eba and Vegetable soup'),
  ('Monday', 'Yam and Egg', 'Beans', 'Pasta(White)'),
  ('Tueday', 'Oatmeal', 'Rice and Beef Stew', 'Tofu'),
  ('Wenesday', 'Bread and tea', 'Beans and Pap', 'Wheat and Egusi Soup'),
  ('Thursday', 'Fried Potatoes ', 'Watermellon', 'Rice and Tomatoe Stew'),
  ('Friday', 'Bread, Egg and tea', 'Jollof Spaghetti', 'Eba and Edikang Ikang soup'),
  ('Saturday', 'Beans cake(Akara)', 'Pasta(white)', 'Eko and Vegetable Soup');

  
-- Create Timetable for Normal_weight
INSERT INTO Normal_weight3 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Bread and tea', 'Jollof rice and Chicke/Meat', 'Eba and Vegetable soup'),
  ('Monday', 'Yam and Egg', 'Beans', 'Pasta(White)'),
  ('Tueday', 'Apple Fruit', 'Rice and Beef Stew', 'Wheat'),
  ('Wenesday', 'Sweet Potatoes', 'Tofu', 'Semovita and Ogbono Soup'),
  ('Thursday', 'Bread and tea ', 'Beans', 'Rice and Tomatoe Stew'),
  ('Friday', 'Bread, Egg and tea', 'Jollof Spaghetti', 'Eba and Edi Ikiankon soup'),
  ('Saturday', 'Beans cake(Akara)', 'Cucumber(Fruit intake)', 'Jollof Rice');

-- Create Timetable for Over_weight
INSERT INTO Over_weight3 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Beans cake(Akara)', 'Fruit Salad', 'Jollof Rice'),
  ('Monday', 'White Spaghetti with Beaf Stew', 'Yam and Garden Egg', 'Wheat and Vegetanble soup'),
  ('Tueday', 'Apple Fruit', 'Tofu', 'Jollof rice'),
  ('Wenesday', 'Beans Cake(Akara)', 'Cucumber', 'Vegetables'),
  ('Thursday', 'Bread and tea ', 'Peas/Almond', 'Eba and Egusi Soup'),
  ('Friday', 'Potatoes(Boiled)', 'Watermellon', 'Eba and Edi Ikiankon soup'),
  ('Saturday', 'Healthy Body Fast', 'Cucumber(Fruit intakes)', 'Rice and Beans with Beaf Stew');

-- ####################################Vegetarian################################################################

-- Create Timetable for Under_weight
INSERT INTO Vegetarian_UW3 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Bread and tea', 'Jollof rice and Tofu', 'Eba and Vegetable soup'),
  ('Monday', 'Tofu Lettuce Wraps', 'Beans', 'Pasta(White)'),
  ('Tueday', 'Oatmeal', 'Rice and Beef Stew', 'Tofu'),
  ('Wenesday', 'Bread and tea', 'Beans and Pap', 'Wheat and Egusi Soup'),
  ('Thursday', 'Fried Potatoes ', 'Watermellon', 'Rice and Tomatoe Stew'),
  ('Friday', 'Breadand tea', 'Jollof Spaghetti', 'Eba and Edikang Ikang soup'),
  ('Saturday', 'Beans cake(Akara)', 'Pasta(white)', 'Eko and Vegetable Soup');

  
-- Create Timetable for Normal_weight
INSERT INTO Vegetarian_NW3 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Bread and tea', 'Jollof rice and Tofu', 'Eba and Vegetable soup'),
  ('Monday', 'Tofu Lettuce Wraps', 'Beans', 'Pasta(White)'),
  ('Tueday', 'Apple Fruit', 'Rice and Beef Stew', 'Wheat with Cream of Mushroom Soup'),
  ('Wenesday', 'Sweet Potatoes', 'Tofu', 'Semovita and Ogbono Soup'),
  ('Thursday', 'Tofu Lettuce Wraps', 'Beans', 'Rice and Tomatoe Stew'),
  ('Friday', 'Bread and tea', 'Jollof Spaghetti', 'Eba and Edi Ikiankon soup'),
  ('Saturday', 'Beans cake(Akara)', 'Cucumber(Fruit intake)', 'Jollof Rice');

-- Create Timetable for Over_weight
INSERT INTO Vegetarian_OW3 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Beans cake(Akara)', 'Fruit Salad', 'Jollof Rice'),
  ('Monday', 'White Spaghetti with Beaf Stew', 'Tofu Lettuce Wraps', 'Wheat and Vegetanble soup'),
  ('Tueday', 'Apple Fruit', 'Tofu', 'Jollof rice'),
  ('Wenesday', 'Beans Cake(Akara)', 'Cucumber', 'Vegetables'),
  ('Thursday', 'Bread and tea ', 'Peas/Almond', 'Eba and Egusi Soup'),
  ('Friday', 'Potatoes(Boiled)', 'Watermellon', 'Eba and Edi Ikiankon soup'),
  ('Saturday', 'Healthy Body Fast', 'Cucumber(Fruit intakes)', 'Rice and Beans with Beaf Stew');

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

  
-- Create Timetable for Normal_weight
INSERT INTO Normal_weight2 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', '', 'Jollof rice and Chicke/Meat', 'Eba and Vegetable soup'),
  ('Monday', 'Yam and Egg', 'Beans', ''),
  ('Tueday', 'Apple Fruit', 'Rice and Beef Stew', 'Wheat'),
  ('Wenesday', '', 'Tofu', 'Semovita and Ogbono Soup'),
  ('Thursday', ' ', 'Beans', 'Rice and Tomatoe Stew'),
  ('Friday', 'Bread, Egg and tea', '', 'Eba and Edi Ikiankon soup'),
  ('Saturday', 'Beans cake(Akara)', 'Cucumber(Fruit intake)', 'Jollof Rice');

-- Create Timetable for Over_weight
INSERT INTO Over_weight2 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Beans cake(Akara)', 'Fruit Salad', ''),
  ('Monday', '', 'Yam and Garden Egg', 'Wheat and Vegetanble soup'),
  ('Tueday', 'Apple Fruit', 'Tofu', ''),
  ('Wenesday', '', 'Cucumber', 'Vegetables'),
  ('Thursday', ' ', 'Peas/Almond', 'Eba and Egusi Soup'),
  ('Friday', '', 'Watermellon', 'Eba and Edi Ikiankon soup'),
  ('Saturday', 'Healthy Body Fast', 'Cucumber(Fruit intakes)', 'Rice and Beans with Beaf Stew');

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

  
-- Create Timetable for Normal_weight
INSERT INTO Vegetarian_NW2 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', '', 'Jollof rice and Tofu', 'Eba and Vegetable soup'),
  ('Monday', 'Tofu Lettuce Wraps', 'Beans', ''),
  ('Tueday', 'Apple Fruit', 'Rice and Beef Stew', 'Wheat with Cream of Mushroom Soup'),
  ('Wenesday', '', 'Tofu', 'Semovita and Ogbono Soup'),
  ('Thursday', 'Tofu Lettuce Wraps', '', 'Rice and Tomatoe Stew'),
  ('Friday', 'Bread and tea', 'Jollof Spaghetti', ''),
  ('Saturday', 'Beans cake(Akara)', 'Cucumber(Fruit intake)', 'Jollof Rice');

-- Create Timetable for Over_weight
INSERT INTO Vegetarian_OW2 (Date, BreakFast, Lunch, Dinner) VALUES 
  ('Sunday', 'Beans cake(Akara)', 'Fruit Salad', 'Jollof Rice'),
  ('Monday', '', 'Tofu Lettuce Wraps', 'Wheat and Vegetanble soup'),
  ('Tueday', 'Apple Fruit', 'Tofu', 'Jollof rice'),
  ('Wenesday', '', 'Cucumber', 'Vegetables'),
  ('Thursday', 'Bread and tea ', 'Peas/Almond', 'Eba and Egusi Soup'),
  ('Friday', 'Potatoes(Boiled)', 'Watermellon', ''),
  ('Saturday', 'Healthy Body Fast', 'Cucumber(Fruit intakes)', 'Rice and Beans with Beaf Stew');