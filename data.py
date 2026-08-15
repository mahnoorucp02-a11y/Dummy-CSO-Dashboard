# data.py

FACULTIES = [
    "Faculty of Information Technology & Computer Science",
    "Faculty of Engineering",
    "Faculty of Management Sciences",
    "Faculty of Media & Mass Communication",
    "Faculty of Pharmacy",
    "Faculty of Law",
    "Faculty of Humanities & Social Sciences",
    "Faculty of Sciences",
    "Faculty of Languages & Literature"
]

JOB_LISTINGS = {
    "Faculty of Information Technology & Computer Science": [
        {
            "id": 1,
            "title": "Junior Python / Streamlit Developer",
            "company": "Systems Limited",
            "location": "Lahore (On-site)",
            "type": "Full-Time",
            "deadline": "2026-09-15",
            "reqs": "Basic Python, Streamlit, Git, REST APIs."
        },
        {
            "id": 2,
            "title": "AI/ML Engineering Intern",
            "company": "10Pearls",
            "location": "Lahore (Hybrid)",
            "type": "Internship",
            "deadline": "2026-09-01",
            "reqs": "Python, PyTorch/TensorFlow, Scikit-Learn."
        }
    ],
    "Faculty of Engineering": [
        {
            "id": 3,
            "title": "Embedded Systems Trainee",
            "company": "PEL Pakistan",
            "location": "Lahore",
            "type": "Full-Time",
            "deadline": "2026-09-20",
            "reqs": "C/C++, Microcontrollers, Circuit Design."
        }
    ],
    "Faculty of Management Sciences": [
        {
            "id": 4,
            "title": "Management Trainee Officer (MTO)",
            "company": "Nestlé Pakistan",
            "location": "Lahore",
            "type": "Full-Time",
            "deadline": "2026-09-10",
            "reqs": "BBA/BS Management, Strong Communication."
        }
    ]
}

# Add default placeholders for remaining faculties
for fac in FACULTIES:
    if fac not in JOB_LISTINGS:
        JOB_LISTINGS[fac] = [
            {
                "id": 99,
                "title": f"Graduate Intern - {fac.split()[-1]}",
                "company": "Partner Enterprise",
                "location": "Lahore",
                "type": "Internship",
                "deadline": "2026-09-30",
                "reqs": "Relevant Degree background, Strong analytical skills."
            }
        ]

COUNSELORS = [
    {"name": "Dr. Sarah Ahmed", "role": "Senior Placement Advisor", "specialty": "Tech & Engineering"},
    {"name": "Ali Raza", "role": "Career Consultant", "specialty": "Management & Business"},
    {"name": "Fatima Malik", "role": "Resume & Interview Coach", "specialty": "General & Soft Skills"}
]
