# Hospital Management System

This project, developed by **Group 03** for the course **CSE327.07**, is a **Hospital Management System**. If you're interested in setting it up, follow the steps below:

1. **Install Django and Python**:
    - Ensure that **Django** and **Python** are installed on your device.
    - If Django is not installed, run the following command:
        ```
        pip install django
        ```
    - Make sure you install Django in the project directory.

2. **Install Pillow Package**:
    - The project also requires the **Pillow** package. To install it, run:
        ```
        pip install Pillow
        ```

3. **Database Migration**:
    - Navigate to the `HOSPITAL_MANAGEMENT_SYSTEM/Hospital` directory.
    - Execute the following commands to create and apply database migrations:
        ```
        python manage.py makemigrations
        python manage.py migrate
        ```

4. **Activate the Server**:
    - Start the development server with the following command:
        ```
        python manage.py runserver
        ```
    - If you encounter any "static" folder errors during migration, you can safely ignore them.
    - If you're using Python 3, replace `pip` with `pip3` when installing packages.

5. **Documentation**:
    - For detailed documentation, refer to the `index.html` file located in `Hospital Management/Hospital/docs/build/html`.

6. **Unit Testing**:
    - To run unit tests, execute the following command:
        ```
        python manage.py test
        ```

