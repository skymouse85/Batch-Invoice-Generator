import pandas as pd     
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os

spreadsheet_path = '../data/spreadsheet.xlsx'  # Update this path if necessary
data = pd.read_excel(spreadsheet_path)

# Group data by household
grouped_data = data.groupby('Household')

# Set up Jinja2 template environment
env = Environment(loader=FileSystemLoader('../templates'))
template = env.get_template('invoice_template.html')

# Function to generate invoice PDFs
def generate_invoice(household_name, household_data):
    lessons = household_data.to_dict(orient='records')
    total_amount_due = household_data['Amount Due'].apply(lambda x: float(x.replace('$', ''))).sum()
    invoice_number = household_data['Invoice No.'].values[0]
    
    invoice_html = template.render(
        invoice_number=invoice_number,
        date=pd.to_datetime('today').strftime('%Y-%m-%d'),
        teacher_name="Your Name",
        teacher_address="Your Address",
        teacher_email="Your Email",
        household_name=household_name,
        lessons=lessons,
        total_amount_due=total_amount_due
    )
    
    html = HTML(string=invoice_html)
    pdf_path = f"../invoices/invoice_{household_name}_{invoice_number}.pdf"
    html.write_pdf(pdf_path)

# Create output directory if it doesn't exist
os.makedirs('../invoices', exist_ok=True)

# Generate invoices for all households
for household_name, household_data in grouped_data:
    generate_invoice(household_name, household_data)

print("Invoices generated successfully!")