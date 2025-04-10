import base64

def base64_to_textFile(base64_string, output_file):
    # Decode the Base64 string
    text = base64_to_string(base64_string)
    
    # Write the decoded data to a text file
    writeTextToFile(text, output_file)
    
def base64_to_string(base64_string):
    # Decode the Base64 string
    return base64.b64decode(base64_string)

def writeTextToFile(text, output_file):
    with open(output_file, 'wb') as bufferedWriter:
        bufferedWriter.write(text)

# Example usage
base64_string = "bWVyaGFiYQ=="
output_file = "output.txt"
base64_to_textFile(base64_string, output_file)
