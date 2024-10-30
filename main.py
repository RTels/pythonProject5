import pandas as pd

# Path to your input CSV file (replace with your actual file path)
input_file = 'emails/leads-megalist.csv'  # Update with your file path

try:
    # Read the CSV file with UTF-16 encoding
    df = pd.read_csv(input_file, encoding='utf-16')

    # Display the first few rows for verification
    print("Preview of the data:")
    print(df.head())
    print("Columns in the file:", df.columns.tolist())

    # Check if the 'Email' column exists and handle case sensitivity
    email_column = 'Email'  # Adjust if your column name is different
    if email_column in df.columns:
        # Count occurrences of each email address
        email_counts = df[email_column].value_counts()

        # Identify duplicates (more than 1 occurrence)
        duplicates = email_counts[email_counts > 1]

        # Display duplicate emails and their counts
        if not duplicates.empty:
            print("\nDuplicate email addresses found:")
            for email, count in duplicates.items():
                print(f"Email: {email}, Count: {count}")
        else:
            print("\nNo duplicate email addresses found.")

        # Remove duplicates and strip whitespace from the email addresses
        unique_emails_df = df.drop_duplicates(subset=email_column).copy()
        unique_emails_df[email_column] = unique_emails_df[email_column].str.strip()

        # Save the unique emails to a new CSV file
        unique_emails_df.to_csv('unique_emails.csv', index=False, encoding='utf-16')

        # Display the number of unique emails found
        print(f"\nTotal unique emails: {len(unique_emails_df)}")
    else:
        print(f"'{email_column}' column not found in the file. Please check the column name.")
except Exception as e:
    print(f"An error occurred: {e}")


# Path to your input UTF-16 CSV file
input_file = 'unique_emails.csv'  # Update with your actual file path
output_file = 'converted_to_utf8.csv'  # Name of the output UTF-8 file

try:
    # Read the CSV file with UTF-16 encoding
    df = pd.read_csv(input_file, encoding='utf-16')

    # Save it to a new CSV file with UTF-8 encoding
    df.to_csv(output_file, index=False, encoding='utf-8')

    print(f"File converted to UTF-8 and saved as '{output_file}'.")
except Exception as e:
    print(f"An error occurred: {e}")