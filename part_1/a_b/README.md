# POM - Behave - selenium - python

This test was development using the Page Object Model design pattern, using the behave framework, selenium and python. The test was developed using chrome, but it can be run on other browsers by changing the browser in the `config.ini` file.

The search results belong to the first page of the search results, using google.com. In the region of Colombia.

## Local Setup

1. Create a virtual environment, if you don't have one already

        py -m venv POM_BDD_env

2. Activate the virtual environment

    On Windows powershell

        .\POM_BDD_env\Scripts\activate

    On Windows using git bash

        source POM_BDD_env/Scripts/activate

    On linux

        source POM_BDD_env/bin/activate

3. To add the required packages to the requirements.txt file, run the following command

        pip freeze > requirements.txt

3. Install the dependencies

       py -m pip install -r requirements.txt

4. Exit the virtual environment

        deactivate

5. To run the tests, run the following command

        behave features --tags=completed