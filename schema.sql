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
  description TEXT NOT NULL,
  link TEXT NOT NULL
);

-- ################################################################################################
-- create usage_history  table 
CREATE TABLE IF NOT EXISTS usage_history (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  route TEXT,
  timestamp DATETIME
);


-- create goal table
CREATE TABLE IF NOT EXISTS goals (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  title TEXT,
  description TEXT,
  notification_enabled INTEGER,
  completed INTEGER
);

-- create milestones table
CREATE TABLE IF NOT EXISTS milestones (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  goal_id INTEGER,
  user_id INTEGER,
  title TEXT,
  description TEXT,
  notification_enabled INTEGER,
  completed INTEGER,
  FOREIGN KEY (goal_id) REFERENCES goals(id)
);

-- create community group chat table
CREATE TABLE IF NOT EXISTS community_chat (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username Text,
  content TEXT,
  notification_enabled INTEGER,
  timestamp DATETIME
);


-- ####################################################################################################
-- ##################### STRESS MANAGEMENT RESOURCES ####################################################

-- create table name for contact us on the landing page 
CREATE TABLE IF NOT EXISTS contact_us (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT UNIQUE,
  university_name TEXT NOT NULL,
  faculty_name TEXT,
  department_name TEXT,
  subject TEXT NOT NULL,
  message TEXT NOT NULL
);

-- create table name for contact us on the landing page 
CREATE TABLE IF NOT EXISTS feature_suggestion (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT UNIQUE,
  university_name TEXT NOT NULL,
  faculty_name TEXT,
  department_name TEXT,
  subject TEXT NOT NULL,
  message TEXT NOT NULL
);