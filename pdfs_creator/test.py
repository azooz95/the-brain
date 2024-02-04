import subprocess

# Specify the path to your JavaScript file
javascript_file = r"E:\joe13\the brain\pdfs_creator\pdf2html.js"

# Run the JavaScript code using Node.js
try:
    result = subprocess.check_output(["node", javascript_file], stderr=subprocess.STDOUT, text=True)
    print(result)
except subprocess.CalledProcessError as e:
    print("Error:", e.output)
