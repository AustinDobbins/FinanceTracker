DROP TABLE expense_category;
DROP TABLE income_category;

CREATE TABLE expense_category (
	exp_cat_id SERIAL PRIMARY KEY,
	exp_cat_name VARCHAR(12)
);

CREATE TABLE income_category (
	inc_cat_id SERIAL PRIMARY KEY,
	inc_cat_name VARCHAR(12)
);

CREATE TABLE income (
	inc_id SERIAL PRIMARY KEY, 
	inc_cat_id SMALLINT,
	inc_source VARCHAR(150),
	inc_date DATE,
	inc_amount SMALLINT,
	FOREIGN KEY (inc_cat_id) REFERENCES income_category (inc_cat_id)
);

CREATE TABLE expense (
	exp_id SERIAL PRIMARY KEY, 
	exp_cat_id SMALLINT,
	exp_statement VARCHAR(150),
	exp_merchant VARCHAR(50),
	exp_amount SMALLINT,
	exp_datetime TIMESTAMP,
	FOREIGN KEY (exp_cat_id) REFERENCES expense_category (exp_cat_id)
);
