import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API key from .env
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Error: API_KEY not found in .env file")
    exit()

# Create Gemini client
client = genai.Client(api_key=API_KEY)

print("======= AI Resume Builder =======\n")

name = input("Enter Name: ")
email = input("Enter Email: ")
phone = input("Enter Phone: ")
education = input("Enter Education: ")
skills = input("Enter Skills: ")
experience = input("Enter Experience: ")
project = input("Enter Project Name: ")
career_goal = input("Enter Career Goal: ")

prompt = f"""
Create a professional ATS-friendly resume.

Candidate Details:

Name: {name}
Email: {email}
Phone: {phone}
Education: {education}
Skills: {skills}
Experience: {experience}
Project: {project}
Career Goal: {career_goal}

Generate the resume with the following sections:
1. Professional Summary
2. Skills
3. Education
4. Experience
5. Project
6. Career Goal
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\n===== Generated Resume =====\n")
print(response.text)


textResponse = response.text

file2 = open("resume.txt", "w", encoding="utf-8")
file2.write(textResponse)
file2.close()

print("Resume saved successfully as resume.txt")