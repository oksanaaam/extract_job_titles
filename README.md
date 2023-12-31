## Job Title Cleaning with OpenAI's GPT-3
This script demonstrates how to clean 1000 job titles using OpenAI's GPT-3 language model.  
It takes a CSV file containing job titles, processes them using GPT-3, and then saves the cleaned job titles to a new CSV file.

### Prerequisites
Python 3.11
OpenAI Python library (openai)
pandas library (pandas)

### Installation
Install the required Python libraries if you haven't already:

`pip install openai pandas`

Replace YOUR_OPENAI_API_KEY with your actual OpenAI API key.

Modify YOUR_PATH_TO_CSV to point to your input CSV file containing job titles.

Usage
Clone the repository or download the script.

Run the script using:

`python main.py`

This will process the job titles using GPT-3 and save the cleaned 1000 job titles to results.csv.

### Script Overview

Imports the necessary libraries (openai, pandas).
Sets your OpenAI API key for authentication.
Specifies the input and output file paths.
Reads the input CSV file into a pandas DataFrame.
Takes the first 50 job titles for processing (you can adjust this as needed).
Calls OpenAI's GPT-3 to clean each job title while retaining its essence.
Appends the cleaned job titles to the DataFrame.
Saves the cleaned job titles along with the original job titles to a new CSV file.
Remember to replace placeholders such as YOUR_OPENAI_API_KEY and YOUR_PATH_TO_CSV with your actual API key and file path.
