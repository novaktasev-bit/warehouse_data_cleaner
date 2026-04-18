Warehouse Data Validator
Automated Python tool for inventory dataset validation and sanitization.

1. Functionality
The script processes inventory records to ensure data integrity before system integration. Key operations include:

SKU Validation: Enforces 6-character formatting and applies FIX_ prefixes where necessary.

Price/Qty Correction: Replaces negative values and zero-entries with baseline defaults.

Record Recovery: Identifies missing names and assigns UNKNOWN tags to prevent data loss.

Audit Logging: Generates a comprehensive modification trail in error_log.txt.

2. Project Components
main.py – Core application logic and OOP structure.

warehouse.csv – Source input dataset.

warehouse_fixed.csv – Cleaned and validated output.

error_log.txt – Detailed QA audit report.

3. Technical Implementation
Object-Oriented Programming: Business logic is encapsulated within the Product class.

Defensive Programming: Robust error handling via try-except blocks for data conversion and I/O.

ETL Workflow: Systematic Extraction, Transformation, and Loading of CSV records.

4. Setup and Execution
Place warehouse.csv in the root directory.

Run the following command in your terminal:

python main.py
