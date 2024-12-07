from PyPDF2 import PdfReader, PdfWriter

def remove_pdf_password():
    try:
        # Prompt user for input and output file paths
        input_path = input("Enter the path to the password-protected PDF: ").strip()
        output_path = input("Enter the path to save the decrypted PDF: ").strip()
        password = input("Enter the password for the PDF: ").strip()

        # Open the encrypted PDF
        reader = PdfReader(input_path)
        
        # Check if the PDF is encrypted
        if reader.is_encrypted:
            # Try to decrypt the PDF using the provided password
            if reader.decrypt(password):
                print("PDF decrypted successfully!")
            else:
                print("Failed to decrypt PDF. Check the password.")
                return
        else:
            print("The PDF is not encrypted.")
            return

        # Create a new PDF writer object
        writer = PdfWriter()
        
        # Add all pages from the reader to the writer
        for page in reader.pages:
            writer.add_page(page)
        
        # Write the decrypted PDF to the output file
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        
        print(f"Decrypted PDF saved to: {output_path}")
    
    except FileNotFoundError:
        print("Error: The file was not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
remove_pdf_password()
