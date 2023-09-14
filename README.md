# WebsiteReviewsProcessing
Assignment1 of COMP20008, 2022, Semester 2


## Assignment Overview

### Background
Websites such as Amazon contain large numbers of product reviews. This presents a rich source of information that we can use to understand more about these products, as well as how people communicate positive and negative sentiments more generally.

In this assignment, you will be working on a dataset comprising reviews of more than 1000 products. Using this dataset, you will have an opportunity to learn how to identify positive and negative sentiments by analyzing the linguistic patterns in the reviews.

### Learning Outcomes
- Be able to read and write data in different formats and combine different data sources.
- Practice text processing techniques using Python.
- Practice data processing, exploration, and visualization techniques with Python.
- Practice visual analysis and written communication skills.

### Dataset
The dataset consists of reviews of more than 1,000 products. It is located at `/course/data/dataset.csv`.

#### Product Dataset
The dataset is a CSV file containing several fields:

- **ID:** Indicates a unique ID number for each product in the dataset.
- **Product Name:** The name of the product, as displayed on the Amazon website.
- **Category:** Each product is assigned to a single category indicating the type of product.
- **No Ratings:** This represents the number of positive or negative ratings (not reviews) of the product.
- **Cost:** How much the product sells for. Note that many products have a price range rather than a single price, typically meaning they can be customized when purchased.
- **Review List:** A list of reviews for the product, expressed as a JSON string.
- **Product URL:** A link to the product's page on Amazon.

**Note:** There are some data integrity issues present in the file. For example, some products are missing reviews and others are missing prices.

