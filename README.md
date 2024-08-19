# Schedule Projet

The Schedule Project is a web application developed with Django that allows users to efficiently and securely manage contacts. Django, one of the most robust and popular frameworks for web development in Python, provides a solid structure for creating scalable and secure applications. This project is designed with a focus on contact organization, offering features such as creating, updating, and deleting records in an intuitive way.

## How to Use

- Register: Create an account to start managing your contacts.
- Login: Access the system using your credentials.
- Create Contacts: Add new contacts through a simple form.
- Edit Contacts: Update your contacts' information as needed.
- Delete Contacts: Remove contacts that are no longer necessary.

## Features

- Access Control: Only authenticated users can create, edit, or delete contacts.
- Contact Association with User: Each contact created is associated with the user who created it, ensuring that only the owner can manage it.
- Simple and Efficient Interface: The interface is built based on Django templates, allowing quick and intuitive navigation.
- Feedback Messages: The system provides clear success or error messages after operations such as login, registration, and contact management.

## Main Project Componentes

- Authentication and Authorization: Using Django's integrated functionalities, the project ensures that only authenticated users can access critical functions like creating, updating, and deleting contacts. The @login_required decorator ensures that sensitive pages are protected.
- Forms: The project uses custom forms, such as cls_registerform and cls_contactform, to capture and validate user data. These forms are essential for ensuring that information is collected correctly and securely.
- Models: The cls_contact model represents the structure of contacts in the database, including fields like first name, last name, and the contact owner. The relationship between the contact and the user is established through the owner field, ensuring that each contact belongs to a specific user.
- Templates: The project uses Django templates to render HTML pages, ensuring a clear separation between business logic and visual presentation. This makes the application easier to maintain and scale.




Schedule project with some interesting technologies. Project under construction.


## Images of the Schedule Project
![main](https://github.com/ecopque/schedule_project/blob/main/prints/Screenshot%20from%202024-08-19%2010-23-48.png)