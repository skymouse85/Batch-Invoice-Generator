import pandas as pd
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os

spreadsheet_path = './data/lesson_tracker.xlsx'  # Update this path if necessary
data = pd.read_excel(spreadsheet_path)

# Group data by household
grouped_data = data.groupby('Household')

# Set up Jinja2 template environment
env = Environment(loader=FileSystemLoader('./templates'))
template = env.get_template('invoice_template.html')

# Function to generate invoice PDFs
def generate_invoice(household_name, household_data):
    lessons = household_data.to_dict(orient='records')
    total_amount_due = household_data['Amount Due'].apply(lambda x: float(str(x).replace('$', ''))).sum()
    total_amount_due_formatted = "${:,.2f}".format(total_amount_due)
    invoice_number = household_data['Invoice No.'].values[0]
    household_fullname = household_data['household_fullname1'].values[0]
    household_email = household_data['household_email1'].values[0]
    
    # Extract month and year
    month = household_data['Month'].values[0]
    year = pd.to_datetime('today').year
    
    context = {
        'invoice_number': invoice_number,
        'date': pd.to_datetime('today').strftime('%Y-%m-%d'),
        'teacher_name': "Mark Clifford",
        'teacher_address': "3007 Peralta St",
        'teacher_city': "Oakland, CA 94618",
        'teacher_phone': "415.368.1448",
        'teacher_email': "markmclifford@gmail.com",
        'household_fullname': household_fullname,
        'household_email': household_email,
        'household_name': household_name,
        'lessons': lessons,
        'total_amount_due': total_amount_due_formatted
    }
    print(context)  # Print context to verify

    invoice_html = template.render(**context)
    
    # Generate filename
    pdf_filename = f"invoice_{household_name}_{month}_{year}.pdf"
    pdf_path = os.path.join('./invoices', pdf_filename)
    html = HTML(string=invoice_html)
    html.write_pdf(pdf_path)

# Create output directory if it doesn't exist
os.makedirs('./invoices', exist_ok=True)

# Generate invoices for all households
for household_name, household_data in grouped_data:
    generate_invoice(household_name, household_data)

print("Invoices generated successfully!")
