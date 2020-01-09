# Spendie

**Spendie** by JaJeJu

## Roster

* Jackson Zou
  * Project Manager
  * Back-end
    * Flask Routes
    * Database Actions
* Jeff Lin
  * Front-end
    * Templates
    * CSS Styling
* Jun Tao Lei
  * Front-end
    * Javascript Functionalities
  * Back-end
    * Setup Database and File System Transfer
    * Setup Authentication

## What is Spendie

Spendie is a budget/money management web application designed to track your spending and visualize it in a intuitive way.

## API Dependencies

* [Google Maps Embed API](../blob/master/doc/api_googlemapsembed.pdf)
* [Google Sheets API](../blob/master/doc/api_googlesheets.pdf)

## Run Instruction

1. Procure any necessary API keys and secrets.
2. Clone the repository with Git.

   ```bash
   git clone https://github.com/jacksonzou123/moneymanager.git
   ```

3. Change into the project directory.

   ```bash
   cd moneymanager/
   ```

4. Create a Python virtual environment in Python3. Visit <https://www.python.org/> for instructions on installing and setting up python3, pip3, and venv on your target operating system.

   ```bash
   python3 -m venv venv
   . venv/bin/activate
   ```

5. Install the required third party packages.

   ```bash
   pip3 install -r doc/requirements.txt
   ```

6. Export any required enviroment variables(skip for now).

   ```bash
   to be determined...
   ```

7. Run the Flask app.

   ```bash
   python3 app.py
   ```
