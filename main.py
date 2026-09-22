import os
import json
from parser import parse_resume

if __name__ == "__main__":
    resumes_folder = "resumes"

    # Check if resumes folder exists
    if not os.path.exists(resumes_folder):
        print(f"Error: '{resumes_folder}' folder not found. Please create it inside your project.")
    else:
        # Loop through all PDF files in the resumes folder
        for file in os.listdir(resumes_folder):
            if file.endswith(".pdf"):
                file_path = os.path.join(resumes_folder, file)
                result = parse_resume(file_path)

                print(f"\nExtracted Resume Data from {file}:")
                print(result)

                # Save each resume's data into its own JSON file
                json_name = file.replace(".pdf", ".json")
                json_path = os.path.join(resumes_folder, json_name)
                with open(json_path, "w") as f:
                    json.dump(result, f, indent=4)

                print(f"Data saved to {json_path}")
