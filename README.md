!!! A file containing the database structure in PDF format is attached to this commit.

# EduContentManager
A platform for creating, editing education courses, as well as assigning teachers to courses, 
and reassigning teachers to different courses.

This is a Django-based web application designed to facilitate collaboration 
between instructors delivering online programming courses. 
The platform streamlines course management, lesson organization, and teacher coordination.

## Project Overview

The core purpose of this application is to provide a structured, 
user-friendly environment where programming instructors can collaborate, 
manage course content, and streamline online education delivery.

### Key Features

- Teacher Management: Create and manage teacher profiles.
- Course Management: Define programming courses with a many-to-many relationship to teachers, 
- allowing flexible collaboration.
- Lesson Organization: Associate lessons with specific courses using foreign key relationships.
- CRUD Functionality: Fully implemented views and URLs for creating, editing, and deleting teachers, 
- courses, and lessons.
- Advanced Search:
  - Search for lessons by their content.
  - Search for courses by title.
- Authentication: Password input page implemented to protect restricted areas.
- Enhanced UI/UX: Improved visual design for a better user experience using modern front-end styling.

## Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS (custom styling and possibly Bootstrap or similar)
- Database: Default Django ORM with SQLite or configurable with PostgreSQL/MySQL
- Deployment: Compatible with WSGI/ASGI servers

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Ngayka/EduContentManager/pull/1
   
2. cd django_project

### Environment Variables

To run this project, you will need to add the following environment variable to your `.env` file:
SECRET_KEY=your-secret-key
DEBUG=True