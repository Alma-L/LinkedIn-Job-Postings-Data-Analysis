import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport

# Define paths for each CSV file
job_postings_path = 'Raw_Data/postings.csv'
job_skills_path = 'Raw_Data/jobs/job_skills.csv'
companies_path = 'Raw_Data/companies/companies.csv'
mapping_skills_path = 'Raw_Data/mappings/skills.csv'

# Load each file if it exists, otherwise print an error
file_paths = {
    "job_postings": job_postings_path,
    "job_skills": job_skills_path,
    "companies": companies_path,
    "mapping_skills": mapping_skills_path
}

dataframes = {}
for name, path in file_paths.items():
    if os.path.exists(path):
        dataframes[name] = pd.read_csv(path)
        print(f"{name.capitalize()} DataFrame loaded successfully.\n")
    else:
        print(f"File not found: {path}")

# Make copies of original data for before-and-after comparisons
original_dataframes = {name: df.copy() for name, df in dataframes.items()}

# Check if all DataFrames are loaded
if len(dataframes) < len(file_paths):
    print("One or more files are missing. Please ensure all files are present.")
else:
    # Preprocessing Steps
    print("Starting data preprocessing...\n")

    # 1. Handle Missing Values
    for name, df in dataframes.items():
        for column in df.columns:
            if (df[column].dtype ==
                    'object'):
                df[column] = df[column].fillna("N/A")
            else:
                df[column] = df[column].fillna(df[column].median())

    # 2. Data Type Conversion
    for df in dataframes.values():
        if 'company_id' in df.columns:
            df['company_id'] = df['company_id'].astype(str)
        if 'job_id' in df.columns:
            df['job_id'] = df['job_id'].astype(str)
        if 'skill_id' in df.columns:
            df['skill_id'] = df['skill_id'].astype(str)

    # 3. Merge DataFrames for Analysis
    merged_df = dataframes["job_postings"] \
        .merge(dataframes["job_skills"], on="job_id", how="left") \
        .merge(dataframes["companies"], on="company_id", how="left") \
        .merge(dataframes["mapping_skills"], on="skill_id", how="left")

    # 4. Remove Duplicates
    for name, df in dataframes.items():
        duplicate_count = df.duplicated().sum()
        if duplicate_count > 0:
            df.drop_duplicates(inplace=True)
            print(f"Removed {duplicate_count} duplicate rows from {name} DataFrame.")

    # 5. Display Final Summaries
    print("\nPreprocessing complete. Summary of each DataFrame:\n")
    for name, df in dataframes.items():
        print(f"{name.capitalize()} DataFrame (first 10 rows):")
        print(df.head(10))

    # Display summary for merged DataFrame
    print("\nMerged DataFrame (first 10 rows):")
    print(merged_df.head(10))

    # 6. Save Processed DataFrames to CSV Files
    output_folder = 'Processed_Data'
    os.makedirs(output_folder, exist_ok=True)

    for name, df in dataframes.items():
        df.to_csv(f'{output_folder}/{name}_processed.csv', index=False)
        print(f"{name.capitalize()} DataFrame saved to {output_folder}/{name}_processed.csv")

    # Save the merged DataFrame
    merged_df.to_csv(f'{output_folder}/merged_data_processed.csv', index=False)
    print(f"Merged DataFrame saved to {output_folder}/merged_data_processed.csv")

    # 7. Generate and Save Profile Reports for Each DataFrame
    for name, df in dataframes.items():
        profile = ProfileReport(df, title=f"{name.capitalize()} Data Profile")
        profile.to_file(f"{output_folder}/{name}_profile.html")
        print(f"{name.capitalize()} Data Profile saved to {output_folder}/{name}_profile.html")

    # Generate a profile report for the merged DataFrame
    merged_profile = ProfileReport(merged_df, title="Merged Data Profile")
    merged_profile.to_file(f"{output_folder}/merged_data_profile.html")
    print(f"Merged Data Profile saved to {output_folder}/merged_data_profile.html")

    # Visualization - Before and After Preprocessing
    # 1. Missing Values Heatmap
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    sns.heatmap(original_dataframes["job_postings"].isnull(), cbar=False, cmap="viridis")
    plt.title("Missing Values - Before Preprocessing (Job Postings)")
    plt.subplot(1, 2, 2)
    sns.heatmap(dataframes["job_postings"].isnull(), cbar=False, cmap="viridis")
    plt.title("Missing Values - After Preprocessing (Job Postings)")
    plt.tight_layout()
    plt.show()

    # 2. Distribution of Numerical Data - Salary (example)
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    sns.histplot(original_dataframes["job_postings"]['salary'], kde=True)
    plt.title("Salary Distribution - Before Preprocessing")
    plt.subplot(1, 2, 2)
    sns.histplot(dataframes["job_postings"]['salary'], kde=True)
    plt.title("Salary Distribution - After Preprocessing")
    plt.tight_layout()
    plt.show()

    # 3. Count Plot for Categorical Data - Job Type
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    sns.countplot(data=original_dataframes["job_postings"], x="job_type")
    plt.title("Job Type Counts - Before Preprocessing")
    plt.xticks(rotation=45)
    plt.subplot(1, 2, 2)
    sns.countplot(data=dataframes["job_postings"], x="job_type")
    plt.title("Job Type Counts - After Preprocessing")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

