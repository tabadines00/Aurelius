import re
import json

file_path = "meditations-raw.txt"
output_file_path = "output.json"

# Regular expression to clean the text and remove \n and Unicode characters
def cleanText(text):
    # Remove \n
    text = re.sub(r'\n', ' ', text)
    
    # Remove Unicode characters
    text = re.sub(r'[^\x00-\x7F]', '', text)
    
    return text

def split_text_by_dot(lines, max_length=1111):
    result = []

    for line in lines:
        while len(line) > max_length:
            # Find the next '.' character within the maximum length
            next_dot = line.rfind('.', 0, max_length)
            
            if next_dot == -1:
                # If there is no '.' within the maximum length, split at the maximum length
                next_dot = max_length

            # Split the line at the found '.' character
            result.append(line[:next_dot + 1])
            line = line[next_dot + 1:].strip()

        if line:
            result.append(line.strip())
    return result

try:
    with open(file_path, 'r') as file:
        # Read the entire contents of the file into a buffer
        text_buffer = file.read()

        # Regex pattern to extract text between Roman numerals and empty lines
        pattern = r'([IVXLCDM]+\.)(.*?)\n\n'
        matches = re.findall(pattern, text_buffer, re.MULTILINE | re.DOTALL)

        # Extracted text from the matches
        extracted_text = [cleanText(match[1].strip()) for match in matches]
        extracted_text = split_text_by_dot(extracted_text)

        # Save the extracted text to a JSON file
        with open(output_file_path, 'w') as json_file:
            json.dump(extracted_text, json_file, indent=4)

except FileNotFoundError:
    print(f"File not found at path: {file_path}")

except Exception as e:
    print(f"An error occurred: {str(e)}")