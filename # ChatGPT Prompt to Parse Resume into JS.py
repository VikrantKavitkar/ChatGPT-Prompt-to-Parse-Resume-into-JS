# ChatGPT Prompt to Parse Resume into JSON

def parse_resume_to_json(resume_text):
    import json
    import re

    resume_data = {}

    # Extracting Name
    name_match = re.search(r'\bVikrant Kavitkar\b', resume_text, re.IGNORECASE)
    resume_data['Name'] = name_match.group() if name_match else ''

    # Extracting Contact Information
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', resume_text)
    phone_match = re.search(r'\+91-\d{10}', resume_text)
    linkedin_match = re.search(r'https://www.linkedin.com/in/[\w-]+', resume_text)

    resume_data['Contact Information'] = {
        'Email': email_match.group() if email_match else '',
        'Phone': phone_match.group() if phone_match else '',
        'LinkedIn': linkedin_match.group() if linkedin_match else ''
    }

    # Extracting Education
    education_section = re.search(r'EDUCATION\s*(.*?)(?=\s*ACHIEVEMENT)', resume_text, re.DOTALL)
    if education_section:
        education_text = education_section.group(1).strip()
        education_entries = re.split(r'\n\s*\n', education_text)
        education_details = []
        for entry in education_entries:
            lines = entry.split('\n')
            degree = lines[0].strip() if lines else ''
            institute = lines[1].strip() if len(lines) > 1 else ''
            grade = re.search(r'\bCGPA: \d\.\d+\b', entry) if 'CGPA' in entry else re.search(r'\b\d{2}\.\d{2}%\b', entry)
            education_details.append({
                'Degree': degree,
                'Institute': institute,
                'Grade': grade.group() if grade else ''
            })
        resume_data['Education'] = education_details

    # Extracting Projects
    project_section = re.search(r'PROJECTS\s*(.*?)(?=\s*EDUCATION)', resume_text, re.DOTALL)
    if project_section:
        project_text = project_section.group(1).strip()
        project_entries = re.split(r'\n\s*\n', project_text)
        project_details = []
        for entry in project_entries:
            lines = entry.split('\n')
            title = lines[0].strip() if lines else ''
            description = ' '.join(lines[1:]).strip() if len(lines) > 1 else ''
            project_details.append({
                'Title': title,
                'Description': description
            })
        resume_data['Projects'] = project_details

    # Extracting Skills
    skills_section = re.search(r'SKILLS\s*(.*?)(?=\s*HOBBIES)', resume_text, re.DOTALL)
    if skills_section:
        skills_text = skills_section.group(1).strip()
        skills_list = [skill.strip() for skill in skills_text.split(',')]
        resume_data['Skills'] = skills_list

    # Extracting Hobbies
    hobbies_section = re.search(r'HOBBIES\s*(.*?)(?=\s*LANGUAGES)', resume_text, re.DOTALL)
    if hobbies_section:
        hobbies_text = hobbies_section.group(1).strip()
        hobbies_list = [hobby.strip() for hobby in hobbies_text.split(',')]
        resume_data['Hobbies'] = hobbies_list

    # Extracting Languages
    languages_section = re.search(r'LANGUAGES\s*(.*)', resume_text, re.DOTALL)
    if languages_section:
        languages_text = languages_section.group(1).strip()
        languages_list = [language.strip() for language in languages_text.split(',')]
        resume_data['Languages'] = languages_list

    return json.dumps(resume_data, indent=4)

# Example resume text
resume_text = """
Vikrant Kavitkar
Email: vikrantkavitkar05@gmail.com
Phone: +91-9146593789
LinkedIn: https://www.linkedin.com/in/vikrant-kavitkar-30a428222

PROJECTS
BANK MANAGEMENT SYSTEM
Bank Management System using Java, demonstrating proficiency in object-oriented programming and software development.
Implemented key features including customer account management, transaction processing, and user authentication, ensuring
secure and efficient banking operations.
Technologies used: Java

VOICE CALCULATOR
We developed a Voice Calculator using Python, enabling users to input their voice to obtain the required calculations.
Technologies used include Python, Math, Parser, Tkinter, Tkinter.messagebox, SpeechRecognition, and Operator. The
application features a graphical user interface created with Tkinter, incorporating a calculator logo, display entry field, and
functional buttons. A microphone button captures user audio input for real-time voice-based calculations.
Technologies used: Python

...

EDUCATION
B.TECH IN Electronics and Telecommunication Engineering |VIIT, Kondhwa Bk., Pune
CGPA: 7.89
SSC |City International School Kothrud
80.80%
HSC |Dr. Kalmadi Shamarao Junior College, Erandwane Pune
84.33%

...

SKILLS
Machine Learning, Explainable AI, Mathematics(Probability and Statistics, Algebra, Calculus), Data Structure, Chatbot Development, Python, Web Development, App Development, Research and Innovation, HTML, CSS & Bootstrap, JavaScript, MySQL, php, Laravel ,Composer, vue.js, Email Marketing, Azure, Github Repository, Java, C++ & C, Technical Documentation, Filling, Canva, Excel, MS Word, MS PowerPoint, MS Office, Communication, Team Player, Critical Thinking, Multitasking

HOBBIES
Playing Casio, Painting & Sketching

LANGUAGES
ENGLISH Professional Proficiency, HINDI Native Proficiency, MARATHI Native Proficiency
"""

# Parsing the resume
parsed_resume_json = parse_resume_to_json(resume_text)
print(parsed_resume_json)
