# Password Generator

## Description
This is a simple Python application built with `tkinter` that generates random passwords based on user-defined input length. Users can specify a password length (ranging from 1 to 25 characters), and the app will generate the password. The generated password can then be copied to the clipboard.

## Requirements
- Python 3.x+
- `tkinter`
- `funcs.py` file containing the `generatePassword` function

## How to Use

### Running the Application:
1. Ensure Python is installed on your system.
2. Save the script as `password_generator.py`.
3. Make sure the `funcs.py` file with the `generatePassword` function is in the same directory as the script.
4. Run the script with the following command:
   ```bash
   python password_generator.py

## Generating Passwords:
1. Enter the desired password length (between 1 and 25 characters) in the input field.
2. Click the **"Generate"** button to create a password.
3. Click the generated password to copy it to the clipboard.

## Resetting Results:
- Click **"Reset"** to clear the generated passwords.

## Exiting the Application:
- Click **"Exit"** to close the app.

## Code Overview
- **Password Generation**: The password is generated using the `generatePassword()` function, which is imported from the `funcs.py` file.
- **Copy to Clipboard**: The generated password can be copied by clicking on it.
- **Reset**: After 10 generations, old passwords are automatically cleared.
