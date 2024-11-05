import pandas as pd
import mysql.connector

# Database connection parameters
host = 'localhost'
user = 'root'
password = 'naman'
database = 'project'  

# Read the Excel file
df = pd.read_excel('EMPLOYEE_DATA.xlsx')

# Print the DataFrame columns 
print("DataFrame columns:", df.columns.tolist())

# Strip whitespace from column names
df.columns = df.columns.str.strip()

# Convert 'doj' column to datetime format and then to string in 'YYYY-MM-DD' format
df['doj'] = pd.to_datetime(df['doj'], format='%d/%m/%Y', errors='coerce').dt.strftime('%Y-%m-%d')

# Normalize 'gender' values
gender_mapping = {
    'male': 'Male',
    'female': 'Female',
    'other': 'Other',
    'Male': 'Male',
    'Female': 'Female',
    'Other': 'Other'
}
df['gender'] = df['gender'].str.strip().map(gender_mapping).fillna('Other')  

# Check for any conversion issues
if df['doj'].isnull().any():
    print("There are invalid dates in the 'doj' column. Please check the data.")

if df['gender'].isnull().any():
    print("There are invalid values in the 'gender' column. Please check the data.")

# Establish the database connection
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    print("Connection established successfully!")

    # Create a cursor object
    cursor = connection.cursor()

    # Prepare the SQL insert statement
    sql = """
    INSERT INTO employees (username, first_name, last_name, email, gender, doj, department, is_active, language, address)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    for index, row in df.iterrows():
        values = (
            row['username'], 
            row['first_name'], 
            row['last_name'], 
            row['email'], 
            row['gender'], 
            row['doj'], 
            row['department'], 
            row['is_active'], 
            row['language'], 
            row['address']
        )
        cursor.execute(sql, values)

    # Commit the transaction
    connection.commit()
    print("Data imported successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed.")
