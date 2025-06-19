# Mail Merge Automation Project 📩

## Description
This Python project automates the creation of personalized letters using a mail merge technique. It reads a list of names and a letter template, then generates custom letters for each name by replacing placeholders in the template.

## Features
- Reads names from a `.txt` file
- Loads a letter template containing placeholder `[name]`
- Replaces the placeholder with each person's name
- Saves the output letters as `.docx` files in a target folder
- Efficient use of file handling and string replacement

## How It Works
1. The program reads a file of names (`invited_names.txt`).
2. It also loads a template letter (`starting_letter.txt`) that contains `[name]` as a placeholder.
3. For each name, it:
   - Removes any whitespace
   - Replaces `[name]` with the actual name
   - Saves the result as a new file: `letter_for_<Name>.docx` in the `Output/ReadyToSend` folder

## Folder Structure
📁 Input
├── 📁 Names
│ └── invited_names.txt
└── 📁 Letters
└── starting_letter.txt
📁 Output
└── 📁 ReadyToSend
└── letter_for_<Name>.docx


## Technologies Used
- Python 3
- File I/O
- String manipulation
- Looping & logic

## Installation & Usage
1. Clone the repository
2. Replace the invited_names.txt and starting_letter.txt with your own data.
3. Run the script:
     - main.py
## License
- This project is open source and available under the MIT License.

## Contact
- tolgayilmaz1377@gmail.com
