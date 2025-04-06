import pandas as pd
# Mock data representing SHL assessments
data = [
    {
        "Assessment Name": "Cognitive Ability Test",
        "URL": "https://www.shl.com/product/cognitive-ability-test/",
        "Description": "Measures problem-solving, logical reasoning, and learning agility.",
        "Remote Support": "Yes",
        "Adaptive Support": "Yes",
        "Duration": 30,
        "Test Type": "Cognitive"
    },
    {
        "Assessment Name": "Personality Questionnaire",
        "URL": "https://www.shl.com/product/personality-questionnaire/",
        "Description": "Assesses traits and behavioral styles for workplace fit.",
        "Remote Support": "Yes",
        "Adaptive Support": "No",
        "Duration": 25,
        "Test Type": "Personality"
    },
    {
        "Assessment Name": "Java Developer Test",
        "URL": "https://www.shl.com/product/java-developer-test/",
        "Description": "Assesses Java programming skills including algorithms and OOP.",
        "Remote Support": "Yes",
        "Adaptive Support": "No",
        "Duration": 40,
        "Test Type": "Technical"
    },
    {
        "Assessment Name": "Business Communication Skills",
        "URL": "https://www.shl.com/product/business-communication-test/",
        "Description": "Evaluates writing and verbal communication in business context.",
        "Remote Support": "Yes",
        "Adaptive Support": "Yes",
        "Duration": 35,
        "Test Type": "Soft Skills"
    },
    {
        "Assessment Name": "Data Analyst Assessment",
        "URL": "https://www.shl.com/product/data-analyst-assessment/",
        "Description": "Tests SQL, Excel, data interpretation and problem-solving.",
        "Remote Support": "Yes",
        "Adaptive Support": "Yes",
        "Duration": 45,
        "Test Type": "Technical"
    },
]

# Extend to 30 rows by duplicating and slightly altering descriptions
mock_data = []
for i in range(30):
    entry = data[i % len(data)].copy()
    entry["Assessment Name"] += f" v{i+1}"
    entry["URL"] = entry["URL"].replace(".com", f".com/v{i+1}")
    entry["Description"] += f" Version {i+1} tailored for different levels."
    mock_data.append(entry)

df = pd.DataFrame(mock_data)
csv_path = "/mnt/data/shl_catalog.csv"
df.to_csv(csv_path, index=False)
csv_path
