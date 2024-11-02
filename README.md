# LinkedIn-Job-Postings-Data-Analysis

**Title**: LinkedIn Job Posting Data Analysis 2023-2024<br>
**Course**: Përgatitja dhe vizualizimi i të dhënave


This project is developed for academic purposes as part of the course "Përgatitja dhe vizualizimi i të dhënave"  in the University of Prishtina, under the 'Inxhinieri Kompjuterike dhe Softuerike' program.<br>
This project analyzes LinkedIn job postings data from 2023-2024 to reveal trends in job availability and company hiring practices. This analysis aims to support job seekers on LinkedIn, especially those “open to work,” by helping them identify companies with the highest job postings, the types of jobs offered, and the best times of year to apply for positions in their field.

Additionally, companies can gauge interest in their job postings by analyzing view and application rates, offering insights into how their listings attract potential applicants. Given LinkedIn’s global presence as a job platform, visualizing this data helps job seekers understand how the job market demands align with their skills and qualifications.<br>
The dataset is publicly available on Kaggle, and you can access it [here](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings).


<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/cloud.svg" width="20" height="20"> <strong>Notice</strong>: Due to size constraints, the postings.csv file is not included in this repository.

## Project Requirements

The key objectives and requirements for this project include:

- **Data Preparation**: Preprocessing data to ensure quality and consistency for analysis.
  - **Data Collection and Quality**: Loading datasets, defining data types, and ensuring data quality checks.
  - **Integration and Aggregation**: Merging datasets to link job details with company and skill information.
  - **Sampling and Cleaning**: Identifying and handling missing values with appropriate strategies (e.g., imputation, filtering).
  
- **Dimensionality Reduction and Feature Selection**:
  - **PCA**: Applied Principal Component Analysis (PCA) for dimensionality reduction.
  - **Feature Selection and Creation**: Selected relevant attributes and created new features, such as `salary_category`.

- **Discretization and Binarization**:
  - **Discretization**: Grouped salary data into `Low`, `Medium`, and `High` categories.
  - **Binarization**: Applied one-hot encoding to categorical columns like `salary_category`.

- **Transformation**:
  - Applied scaling and transformation as needed for numerical features to improve consistency and readability in analysis.

## Key Steps

1. **Data Preprocessing**: Defined data types, handled missing values, and integrated datasets.
2. **PCA for Dimensionality Reduction**: Reduced high-dimensional numerical data to principal components.
3. **Analysis**: Insights into salary levels.

## File Descriptions

- `postings.csv`: Raw LinkedIn job postings data.
- `PreprocessingData.ipynb`: Jupyter Notebook with data processing and analysis.
- `README.md`: Project documentation (this file).

## Getting Started

### Prerequisites

- Python 3.x
- Libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`,

### Installation

```bash
pip install pandas numpy scikit-learn matplotlib