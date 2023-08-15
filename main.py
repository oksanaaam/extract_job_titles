import openai
import pandas as pd
import random

openai.api_key = "YOUR_OPENAI_API_KEY"

input_csv_path = "YOUR_PATH_TO_CSV"
output_csv_path = "results.csv"

df = pd.read_csv(input_csv_path)

random_subset = random.sample(range(len(df)), 100)
df_subset = df.loc[random_subset].copy()

job_titles = df_subset["JOB_TITLE"]

cleaned_titles = []

for title in job_titles:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Please extract just the core job title from: '{title}'.",
        max_tokens=50
    )
    cleaned_title = response.choices[0].text.strip()
    cleaned_titles.append(cleaned_title)

df_subset["CLEANED_JOB_TITLE"] = cleaned_titles

df_subset[["JOB_TITLE", "CLEANED_JOB_TITLE"]].to_csv(output_csv_path, index=False)
