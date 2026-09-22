import pdfplumber
import re

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def parse_resume(file_path):
    resume_text = extract_text_from_pdf(file_path)

    # Extract email
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', resume_text)
    email = email_match.group(0) if email_match else None

    # Extract phone number (basic pattern for 10 digits)
    phone_match = re.search(r'\b\d{10}\b', resume_text)
    phone = phone_match.group(0) if phone_match else None

    # Extract skills (simple keyword-based approach)
    skills_keywords = ["Python", "Java", "C++", "Machine Learning", "SQL", "HTML", "CSS"]
    skills = [skill for skill in skills_keywords if skill.lower() in resume_text.lower()]

    # Extract Education section
    education_match = re.search(r'(Education|Qualifications|Academic)[\s\S]*?(Experience|Projects|Skills|$)', resume_text, re.IGNORECASE)
    education = education_match.group(0).strip() if education_match else None

    # Extract Experience section
    experience_match = re.search(r'(Experience|Work History|Employment)[\s\S]*?(Education|Projects|Skills|$)', resume_text, re.IGNORECASE)
    experience = experience_match.group(0).strip() if experience_match else None

    # Extract Projects section
    projects_match = re.search(r'(Projects|Achievements)[\s\S]*?(Education|Experience|Skills|$)', resume_text, re.IGNORECASE)
    projects = projects_match.group(0).strip() if projects_match else None

    return {
        "email": email,
        "phone": phone,
        "skills": skills,
        "education": education,
        "experience": experience,
        "projects": projects
    }
