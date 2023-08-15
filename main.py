import openai
import pandas as pd
import html

openai.api_key = "YOUR_OPENAI_API_KEY"

input_csv_path = "YOUR_PATH_TO_CSV"
output_csv_path = "results.csv"

df = pd.read_csv(input_csv_path)

filtered_df = df[df["JOB_TITLE"].apply(lambda title: isinstance(title, str) and len(title) > 20)]

df_subset = filtered_df.head(1000).copy()

job_titles = df_subset["JOB_TITLE"]

cleaned_titles = []

for title in job_titles:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Please extract just the core job title from: '{html.escape(title)}'.",
        max_tokens=50
    )
    cleaned_title = response.choices[0].text.strip()
    cleaned_titles.append(cleaned_title)

df_subset["CLEANED_JOB_TITLE"] = cleaned_titles

df_subset[["JOB_TITLE", "CLEANED_JOB_TITLE"]].to_csv(output_csv_path, index=False)
