import smtplib
from email.message import EmailMessage
import streamlit as st

def send_email(name, score, receiver):
    sender = 'thejobsdriver@outlook.com'  # Replace with your actual email
    password = st.secrets["EMAIL_PASSWORD"]   # This should be handled securely
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587  # Replace with your SMTP port
    
    message = EmailMessage()
    message.set_content(f"{name} completed TheJobsDriver Product Knowledge Test with a score of {score}/10.")
    message['Subject'] = 'Test Completion Notification'
    message['From'] = sender
    message['To'] = receiver
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender, password)
        server.send_message(message)
        server.quit()
        message_sent = 'Email sent successfully.'
    except Exception as e:
        message_sent = f'Failed to send email: {e}'
    
    return message_sent

# Full list of 10 questions
questions = [
    {
        "question": "What is the core strategy of TheJobsDriver in reaching job seekers?",
        "choices": ["Multi-channel approach", "Direct mailing", "Power-platform advertising", "Cold calling techniques"],
        "answer": 0
    },
    {
        "question": "What type of job seekers does TheJobsDriver excel at attracting for their clients?",
        "choices": ["Primarily active job seekers", "Only passive job seekers", "Both active and passive job seekers", "None of the above"],
        "answer": 2
    },
    {
        "question": "What kind of contracts does TheJobsDriver offer to clients?",
        "choices": ["Affordable annual contracts", "Fixed long-term contracts", "Month-to-month contracts", "Cancel anytime contracts"],
        "answer": 2
    },
    {
        "question": "What does TheJobsDriver prioritize to ensure client satisfaction?",
        "choices": ["Number of job posts", "Volume of website traffic", "Quality of leads generated", "Quantity of clicks on ads"],
        "answer": 2
    },
    {
        "question": "How does TheJobsDriver's multi-channel approach benefit clients?",
        "choices": ["Levels advertising costs", "Increases job post duration", "Mitigates risks from source performance changes", "Focuses the pool of applicants"],
        "answer": 2
    },
    {
        "question": "What is TheJobsDriver's approach to contracts and client retention?",
        "choices": ["Helpful long-term commitments", "Month-to-month contracts", "Open-rate contracts", "Prepaid annual subscriptions"],
        "answer": 1
    },
    {
        "question": "How does TheJobsDriver ensure the generation of high-quality leads?",
        "choices": ["Focus on vanity metrics", "Targeting candidates who could start quickly", "Continuously optimized media-mix", "Providing free job post templates"],
        "answer": 2
    },
    {
        "question": "What differentiates TheJobsDriver from a job board?",
        "choices": ["Lower pricing for job listings", "TheJobsDriver is not a job board", "Exclusive access to a secret job board", "Guaranteed job placements"],
        "answer": 1
    },
    {
        "question": "TheJobsDriver's approach is deeply rooted in?",
        "choices": ["Long-term price locking", "Technology and human insight", "More job posts per month", "Maximum exposure to job seekers"],
        "answer": 1
    },
    {
        "question": "What key performance indicator does TheJobsDriver focus on for recruitment advertising?",
        "choices": ["Number of job post views", "Number of potential hires", "Click-through rates of job ads", "Overall client satisfaction scores"],
        "answer": 1
    }
]
# test send email
# name = input("Please enter your name: ")
# response = send_email('jesus', 2, 'jesussanchezd@hotmail.es')
# print(response)
