from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "name": "Orkhan Iskandarov",
        "summary": "I am an IT Manager/Supervisor with over 15 years of experience in project management, system administration, and DevOps practices.",
        "contact": {
            "location": "Baku, Azerbaijan",
            "email": "oiskenderov@gmail.com",
            "phone": "+994 (55) 3060504",
            "linkedin": "https://www.linkedin.com/in/orkhan-iskandarov/",
            "github": "https://github.com/oiskenderov",
            "facebook": "https://facebook.com/oiskenderov",
        },
        "profile_pic": "/static/img/profile.jpg",
        "skills": [
            "Linux (Ubuntu, CentOS), Windows Server",
            "MS SQL Server, PostgreSQL",
            "Docker, Kubernetes, Ansible, Terraform",
            "Python, Bash scripting",
            "Zabbix, Grafana, PRTG",
            "DNS configuration, VPS/VDS setup",
            "Information security systems"
        ],
        "work_experience": [
            {
                "role": "Venue Technology Manager",
                "company": "COP29 Azerbaijan - United Nations Climate Change",
                "dates": "June 2024 - November 2024",
                "responsibilities": [
                    "Led the planning, design, delivery, and implementation of technology services.",
                    "Ensured technical requirements were incorporated into venue designs.",
                    "Collaborated with key stakeholders for smooth technology deployment."
                ]
            },
            {
                "role": "Project Team Leader",
                "company": "Qvant Technologies LTD.",
                "dates": "June 2023 - Present",
                "responsibilities": [
                    "Defined project scope, objectives, and timelines.",
                    "Managed resources and budgets to meet project goals.",
                    "Ensured quality assurance through testing and validation processes."
                ]
            },
            {
                "role": "Pre-Sales Engineer",
                "company": "Dinex Technologic LTD.",
                "dates": "January 2024 - Present",
                "responsibilities": [
                    "Managed product POC and POV cycles.",
                    "Designed solutions and participated in customer meetings.",
                    "Maintained communication with vendors to update expertise."
                ]
            },
            {
                "role": "Tutor & Mentor",
                "company": "Algoritmika School / ADNSU / AZTU / BDU / Ministry of Technologies",
                "dates": "February 2021 - Present",
                "responsibilities": [
                    "Instructed students on system administration and DevOps practices.",
                    "Taught Ansible for configuration management and automation.",
                    "Provided personalized mentoring to ensure practical application of skills."
                ]
            },
            {
                "role": "IT Supervisor / CTO",
                "company": "Panalpina CIS",
                "dates": "March 2016 - June 2020",
                "responsibilities": [
                    "Managed IT operations for Azerbaijan and Georgia offices.",
                    "Implemented DevOps methodologies and CI/CD pipelines using GitHub and Docker.",
                    "Conducted staff training programs to enhance skills."
                ]
            },
            {
                "role": "Director of Area IT System / System Audit",
                "company": "Panalpina CIS",
                "dates": "June 2012 - March 2016",
                "responsibilities": [
                    "Designed and implemented IT infrastructure solutions.",
                    "Introduced containerization with Docker for streamlined deployment.",
                    "Led a team responsible for Linux, MS Server, and automation."
                ]
            },
            {
                "role": "Head of IT Department / Database Administrator",
                "company": "State Agency on Standardization, Metrology, and Patents",
                "dates": "February 2006 - May 2012",
                "responsibilities": [
                    "Supervised IT operations, including MSSQL and PostgreSQL administration.",
                    "Configured DNS servers and implemented secure hosting environments.",
                    "Developed alerting systems for timely incident response."
                ]
            },
            {
                "role": "IT Helpdesk / IT Support / Network Support",
                "company": "Technip Maritime Overseas Ltd",
                "dates": "October 2001 - January 2005",
                "responsibilities": [
                    "Provided comprehensive IT support for end-users.",
                    "Assisted in setting up and maintaining network infrastructure.",
                    "Resolved technical issues and enhanced system performance."
                ]
            }
        ],
        "education": [
            {"degree": "Master's in Finance & Credit", "institution": "Azerbaijan State Economic University", "year": "2007"},
            {"degree": "Bachelor's in Economics and Management", "institution": "Azerbaijan State Oil Academy", "year": "2001"},
            {"degree": "DevOps Engineer Qualification", "institution": "GeekBrains University", "year": "2021"}
        ],
        "languages": [
            {"language": "Azerbaijani", "proficiency": "Native"},
            {"language": "English", "proficiency": "B2 (Upper-Intermediate)"},
            {"language": "Russian", "proficiency": "C2 (Fluent)"}
        ]
    })

