

#2 is better and clean than 1
import PyPDF2
import re

# Open the PDF file in read-binary mode
pdf_file = open('example2.pdf', 'rb')

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

# Open the text file in read mode
with open("example.txt", "r") as file:
    # Read the content of the file
    content = file.read()

# Extract all the 4 digits numbers using regular expression
four_digits_numbers = re.findall(r"\b\d{4}\b", content)

# Find the repeated numbers and their count
repeated_numbers = {}
unique_numbers = set()

for number in four_digits_numbers:
    if number in unique_numbers:
        if number in repeated_numbers:
            repeated_numbers[number] += 1
        else:
            repeated_numbers[number] = 1
    else:
        unique_numbers.add(number)

if len(repeated_numbers) > 0:
    print("The repeated numbers are:")
    for number, count in repeated_numbers.items():
        print(f"{number}: {count}")
else:
    print("There are no repeated numbers in the list")

# Delete temporary text file
import os

# specify the filename to delete
filename = "example.txt"

# use the os module to delete the file
os.remove(filename)
