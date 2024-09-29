
 **Kenyatta Hospital Child Immunization Tracking System**

## **Project Overview**
The **Child Immunization Tracking System** is a web-based solution developed for Kenyatta Hospital, designed to streamline the immunization process. The system tracks child immunization schedules, sends reminders, and provides real-time data for healthcare workers and the Ministry of Health, aiming to improve immunization rates and ensure no child misses a vaccine.

## **Features**
- **Child and parent registration** with role-based access.
- **Vaccination scheduling** and automatic notifications/reminders.
- **Immunization history tracking** for individual children.
- **Reports and analytics** on vaccination coverage and growth tracking.
- **Dashboard** views for parents, healthcare workers, and MOH officials.
- **User roles** with different access levels.

## **Technology Stack**
- **Backend**: Python Django
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: MySQL and   (adapt to your setup)
- **Authentication**: Django's built-in authentication system
- **Email notifications**: SMTP or Django Allauth for sending reminders
- **Environment Management**: `python-decouple` for managing environment variables


## **Installation Instructions**

### Prerequisites
- **Python 3.x** installed on your machine.
- **Django** installed (`pip install django`).
- **MySQL or PostgreSQL** database installed and configured.
- **Git** for version control (optional).

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repository/child-immunization-tracker.git
   cd child-immunization-tracker
   ```

2. **Create a virtual environment** and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory (if using `python-decouple`):
     ```
     DB_NAME=your-database-name
     DB_USER=your-database-user
     DB_PASSWORD=your-database-password
     DB_HOST=localhost
     DB_PORT=3306  # or 5432 for PostgreSQL
     SECRET_KEY=your-django-secret-key
     EMAIL_HOST=your-smtp-host
     EMAIL_PORT=your-email-port
     EMAIL_HOST_USER=your-email-username
     EMAIL_HOST_PASSWORD=your-email-password
     ```

5. **Set up the database**:
   - Ensure your MySQL/PostgreSQL database is running and accessible.
   - Apply migrations:
     ```bash
     python manage.py migrate
     ```

6. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```
   The app will be available at `http://127.0.0.1:8000/`.

### Email Notifications Configuration
- Set up the SMTP configuration in the `.env` file to enable email notifications for upcoming vaccination reminders.

## **Usage**
1. **Register** as a parent or healthcare worker.
2. **Log in** to access the dashboard.
3. **Add children** and schedule their vaccinations.
4. **Receive notifications** about upcoming vaccinations.
5. **Track immunization history** and generate reports.

## **API Endpoints**
The system also provides a set of RESTful API endpoints for integration:

1. **User Registration**:
   - `POST /api/register/`
2. **User Login**:
   - `POST /api/login/`
3. **Add Child**:
   - `POST /api/children/`
4. **Schedule Vaccination**:
   - `POST /api/vaccinations/`
5. **Retrieve Immunization History**:
   - `GET /api/children/{id}/history/`

For a full list of API endpoints, please refer to the `API_DOCUMENTATION.md` file.

## **Testing**
To run tests:
```bash
python manage.py test
```

## **Contributing**
Contributions are welcome! Follow the steps below to contribute:
1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a Pull Request.

## **Deployment**
- The project can be deployed on platforms like **Heroku**, **AWS**, or **DigitalOcean**.
- For **Heroku**:
  1. Add a `Procfile` to specify your app’s entry point:
     ```
     web: gunicorn projectname.wsgi --log-file -
     ```
  2. Set environment variables using Heroku’s dashboard or CLI.
  3. Deploy your app (`git push heroku main`).

## **License**
This project is licensed under the **MIT License**.

## **Contact Information**
For any inquiries or support, contact:
- **Email**: mwandia.maghanga@example.com
- **Social Media**: [Insert social media handles]

---

This README provides a comprehensive guide for your Django-based immunization tracking system. You can adjust any details specific to your project setup, such as database configuration or deployment methods.

## **Project Overview**
This project is a web-based **Child Immunization Tracking System** designed for Kenyatta Hospital. The system helps automate the process of registering children, scheduling vaccinations, sending reminders, and maintaining immunization records. The primary goal is to improve the overall immunization coverage in Kenya by providing real-time data to parents, healthcare workers, and the Ministry of Health.

## **Features**
- **Registration** of children and parents.
- **Vaccination scheduling** with reminder notifications for upcoming vaccinations.
- **Immunization history tracking** for individual children.
- **Data analytics** for vaccination coverage, uptake rates, and growth tracking.
- **User roles** for parents, doctors, and healthcare officials.
- **Reports generation** to monitor county-based immunization coverage.

## **Technology Stack**
- **Frontend**: HTML5, CSS3, JavaScript (React/Angular)
- **Backend**: Node.js (Express.js)
- **Database**: MySQL
- **Authentication**: bcrypt for password hashing
- **Environment Management**: dotenv for secure environment variable handling
- **API**: RESTful services using Express.js
- **Deployment**: Hosted on a cloud platform (e.g., Heroku, AWS, DigitalOcean)

## **Installation Instructions**
### Prerequisites
- **Node.js** installed on your system.
- **MySQL** database setup.
- **Git** for version control (optional).

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repository/child-immunization-tracker.git
   cd child-immunization-tracker
   ```

2. **Install the dependencies**:
   ```bash
   npm install
   ```

3. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add the following variables:
     ```
     DB_HOST=your-database-host
     DB_USER=your-database-user
     DB_PASS=your-database-password
     DB_NAME=your-database-name
     SECRET_KEY=your-secret-key
     ```

4. **Set up the MySQL database**:
   - Create the database and run migrations (use Sequelize or your preferred migration tool).
   - Example:
     ```bash
     npx sequelize db:create
     npx sequelize db:migrate
     ```

5. **Run the server**:
   ```bash
   npm start
   ```
   The server will be running at `http://localhost:3000/`.

## **Usage**
- **Register** as a parent or healthcare worker.
- **Log in** to access your dashboard.
- **Add children** and schedule their vaccinations.
- **Receive notifications** when a vaccination is due.
- **Track immunization history** and generate reports on vaccination coverage.

## **API Endpoints**
1. **User Registration**:
   - `POST /api/users/register`
2. **User Login**:
   - `POST /api/users/login`
3. **Add Child**:
   - `POST /api/children/add`
4. **Schedule Vaccination**:
   - `POST /api/vaccinations/schedule`
5. **Get Immunization History**:
   - `GET /api/children/:id/history`

For a complete list of API endpoints and usage, refer to the `API_DOCUMENTATION.md` file.

## **Contributing**
If you wish to contribute to the project, follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## **License**
This project is licensed under the MIT License.

## **Contact Information**
For any inquiries or support:
- **Email**: mwadiajackson@gmail.com
- **Social Media**: github.com/jacksonmwadia

---

This template covers the essential details of your project, and you can adjust the content based on your specific setup or additional features.
