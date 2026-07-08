import os
from dotenv import load_dotenv
from google import genai
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def buildResume():

    # Load environment variables
    load_dotenv()

    # Get API Key
    API_KEY = os.getenv("API_KEY")

    if not API_KEY:
        print("Error: API_KEY not found")
        return

    # Create Gemini Client
    client = genai.Client(api_key=API_KEY)

    print("======= AI Resume Builder =======")

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

Name: {name}
Email: {email}
Phone: {phone}
Education: {education}
Skills: {skills}
Experience: {experience}
Project: {project}
Career Goal: {career_goal}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\n===== Generated Resume =====\n")
    print(response.text)

    # Create PDF
    doc = SimpleDocTemplate("resume.pdf")
    styles = getSampleStyleSheet()
    story = []

    for line in response.text.split("\n"):
        story.append(Paragraph(line, styles["Normal"]))

    doc.build(story)

    print("Resume saved successfully as resume.pdf")