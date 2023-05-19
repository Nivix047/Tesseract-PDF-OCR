# Import necessary libraries
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv()

# Function to extract text from a PDF file


def extract_text_from_pdf(pdf_path):
    try:
        # Convert the PDF file into a sequence of images
        images = convert_from_path(pdf_path)

        # Initialize an empty string to hold the extracted text
        text = ""

        # Iterate over all the images
        for i, img in enumerate(images):
            # Extract the text from the current image and add it to the text string
            text += pytesseract.image_to_string(img)

        # Return the extracted text
        return text

    except Exception as e:
        print(f"Error: {str(e)}")
        return None


# Specify the path to the PDF file
pdf_path = "/Users/nivix047/Desktop/Learn MongoDB_ MongoDB CRUD I Cheatsheet _ Codecademy.pdf"

# Call the function to extract text and store the result in a variable
text = extract_text_from_pdf(pdf_path)

# Print the extracted text
print(text)

# OpenAI API Key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Generate a summary of the extracted text using OpenAI GPT-3.5 Turbo
try:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Summarize in human readable language the text of the following document: {text}"}]
    )
    # Print the generated summary
    print(completion.choices[0].message.content)

except Exception as e:
    print(f"Error: {str(e)}")
