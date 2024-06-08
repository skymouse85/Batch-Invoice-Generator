# Batch Invoice Generator

This project generates PDF invoices for music students based on data from a spreadsheet.

## Project Structure

batch_invoice_generator/
├── data/
│ └── spreadsheet.xlsx
├── invoices/
├── scripts/
│ └── invoice_generator.py
├── templates/
│ └── invoice_template.html
├── venv/
├── README.md
├── requirements.txt
└── .gitignore

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place your spreadsheet file (`spreadsheet.xlsx`) in the `data/` directory.
2. Run the invoice generator script:
    ```bash
    python scripts/invoice_generator.py
    ```
3. Generated invoices will be saved in the `invoices/` directory.

## Dependencies

- pandas
- jinja2
- weasyprint
- reportlab

## License

This project is licensed under the MIT License.