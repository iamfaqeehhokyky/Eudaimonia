-- create Table for underweight who eat daily
CREATE TABLE IF NOT EXISTS Under_weight3 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT
);

-- create Grocery table for underweight who eat daily
CREATE TABLE IF NOT EXISTS Under_weight3_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);

-- create table for Normal weight who eat daily
CREATE TABLE IF NOT EXISTS Normal_weight3 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT 
);

-- create Grocery table for uNormal weight who eat daily
CREATE TABLE IF NOT EXISTS Normal_weight3_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);

-- create table for Overweight who eat daily
CREATE TABLE IF NOT EXISTS Over_weight3 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT 
);

-- create Grocery table for Overweight who eat daily
CREATE TABLE IF NOT EXISTS Over_weight3_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);

-- create table for Vegetarian underweight who eat daily
CREATE TABLE IF NOT EXISTS Vegetarian_UW3 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT
);

-- create Grocery table for Vegetarian underweight who eat daily
CREATE TABLE IF NOT EXISTS Vegetarian_UW3_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);

-- create table for Vegetarian Normalweight who eat daily
CREATE TABLE IF NOT EXISTS Vegetarian_NW3 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT
);

-- create Grocery table for Vegetarian Normalweight who eat daily
CREATE TABLE IF NOT EXISTS Vegetarian_NW3_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);

-- create table for Vegetarian Overweight who eat daily
CREATE TABLE IF NOT EXISTS Vegetarian_OW3 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT
);

-- create Grocery table for Vegetarian Overweight who eat daily
CREATE TABLE IF NOT EXISTS Vegetarian_OW3_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);

-- create table for Allegies underweight who eat daily
CREATE TABLE IF NOT EXISTS Allegies_UW3 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT
);

-- create Grocery table for Allegies underweight who eat daily
CREATE TABLE IF NOT EXISTS Allegies_UW3_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);

-- create table for Allegies Normalweight who eat daily
CREATE TABLE IF NOT EXISTS Allegies_NW3 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT
);

-- create Grocery table for Allegies Normalweight who eat daily
CREATE TABLE IF NOT EXISTS Allegies_NW3_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);

-- create table for Allegies Overweight who eat daily
CREATE TABLE IF NOT EXISTS Allegies_OW3 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT
);

-- create Grocery table for Allegies Overweight who eat daily
CREATE TABLE IF NOT EXISTS Allegies_OW3_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);










-- ####################################################################################################
-- #####################People That Eat Twice Daily####################################################


-- create table for underweight who eat daily
CREATE TABLE IF NOT EXISTS Under_weight2 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT
);

-- create Grocery table for underweight who eat daily
CREATE TABLE IF NOT EXISTS Under_weight2_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);

-- create table for Normalweight who eat daily
CREATE TABLE IF NOT EXISTS Normal_weight2 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT 
);

-- create Grocery table for Normalweight who eat daily
CREATE TABLE IF NOT EXISTS Normal_weight2_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);

-- create table for Overweight who eat daily
CREATE TABLE IF NOT EXISTS Over_weight2 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT 
);

-- create Grocery table for Overweight who eat daily
CREATE TABLE IF NOT EXISTS Over_weight2_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);

-- create Grocery table for Vegetarian underweight who eat daily
CREATE TABLE IF NOT EXISTS Vegetarian_UW2 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT
);

-- create Grocery table for Vegetarian underweight who eat daily
CREATE TABLE IF NOT EXISTS Vegetarian_UW2_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);

-- create table for Vegetarian Normalweight who eat daily
CREATE TABLE IF NOT EXISTS Vegetarian_NW2 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT
);

-- create Grocery table for Vegetarian Normalweight who eat daily
CREATE TABLE IF NOT EXISTS Vegetarian_NW2_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);

-- create Grocery table for Vegetarian Overweight who eat daily
CREATE TABLE IF NOT EXISTS Vegetarian_OW2 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT
);

-- create Grocery table for Vegetarian Overweight who eat daily
CREATE TABLE IF NOT EXISTS Vegetarian_OW2_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);

-- create table for Allegies underweight who eat daily
CREATE TABLE IF NOT EXISTS Allegies_UW2 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT
);

-- create Grocery table for Allegies underweight who eat daily
CREATE TABLE IF NOT EXISTS Allegies_UW2_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);

-- create table for Allegies normalweight who eat daily
CREATE TABLE IF NOT EXISTS Allegies_NW2 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT
);

-- create Grocery table for Allegies normalweight who eat daily
CREATE TABLE IF NOT EXISTS Allegies_NW2_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);

-- create table for underweight who eat daily
CREATE TABLE IF NOT EXISTS Allegies_OW2 (
  Date TEXT Not NULL,
  BreakFast TEXT,
  Lunch TEXT,
  Dinner TEXT
);

-- create Grocery table for Allegies Overweight who eat daily
CREATE TABLE IF NOT EXISTS Allegies_OW2_Grocery (
  Date TEXT Not NULL,
  Item TEXT
);











-- ####################################################################################################
-- ##################### STRESS MANAGEMENT RESOURCES ####################################################

-- create stress management resources table 
CREATE TABLE IF NOT EXISTS stress_management_resources (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT NOT NULL
);