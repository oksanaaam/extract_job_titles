import openai
import pandas as pd

openai.api_key = "YOUR_OPENAI_API_KEY"

input_csv_path = "YOUR_PATH_TO_CSV"
output_csv_path = "results.csv"

df = pd.read_csv(input_csv_path)

df_subset = df.head(50).copy()

job_titles = df_subset["JOB_TITLE"]

cleaned_titles = []

for title in job_titles:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Clean the job title: {title}.",
        max_tokens=50
    )
    cleaned_title = response.choices[0].text.strip()
    cleaned_titles.append(cleaned_title)

df_subset["CLEANED_JOB_TITLE"] = cleaned_titles

df_subset[["JOB_TITLE", "CLEANED_JOB_TITLE"]].to_csv(output_csv_path, index=False)
