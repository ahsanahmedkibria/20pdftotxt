
import PyPDF2

# Open the PDF file in read-binary mode
pdf_file = open('example.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)


# Initialize an empty string to store the extracted text
text = ""

# Loop through each page of the PDF and extract the text
for i in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[i]
    text += page.extract_text()

# Close the PDF file
pdf_file.close()

# Open a new text file in write mode
text_file = open('example.txt', 'w')

# Write the extracted text to the text file
text_file.write(text)

# Close the text file
text_file.close()

#text file created now working with txt fipe
import re


# Open the text file in read mode
with open("example.txt", "r") as file:
    # Read the content of the file
    content = file.read()

# Extract all the 4 digits numbers using regular expression
four_digits_numbers = re.findall(r"\b\d{4}\b", content)

# Print the extracted 4 digits numbers
print(four_digits_numbers)

# Find the repeated numbers
repeated_numbers = set()
unique_numbers = set()

for number in four_digits_numbers:
    if number in unique_numbers:
        repeated_numbers.add(number)
    else:
        unique_numbers.add(number)

if len(repeated_numbers) > 0:
    print("The repeated numbers are:", list(repeated_numbers))
else:
    print("There are no repeated numbers in the list")

#Delete temporary text file
import os

# specify the filename to delete
filename = "example.txt"

# use the os module to delete the file
os.remove(filename)

#print(f"{filename} has been deleted.")

