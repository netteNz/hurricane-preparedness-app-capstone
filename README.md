# Hurricane Preparedness and Response System

## Introduction
This project, developed as part of our senior design initiative at UAGM Gurabo, is a web application designed to significantly enhance the resilience and readiness of Puerto Rico against natural disasters, particularly hurricanes. Leveraging Django, this system aims to provide real-time updates, resource tracking, and personalized alerts to help residents prepare and respond effectively to hurricanes.

## Background
Puerto Rico's geographical position makes it prone to frequent and severe hurricanes. The devastating impact of Hurricane Maria highlighted the urgent need for improved disaster preparedness and response strategies. Our project addresses this need by integrating modern technology to provide a robust platform for disaster management.

## Features

### Real-time Weather Updates
- Utilizes NOAA and OpenWeatherMap APIs to fetch and display up-to-date weather information.
- Offers personalized weather forecasts and alerts based on user's geolocation.

### Resource Allocation and Tracking
- Interactive maps show locations of shelters, medical facilities, and food distribution centers.
- Users can view real-time status of resources, including availability and capacity.

### User-Specific Notifications
- System sends notifications based on specific weather alerts like advisories, watches, and warnings.
- Allows users to customize notification types and frequency according to their preferences.

### Community Collaboration Tools
- Features a community section where users can share updates, tips, and personal experiences.
- Enables users to contribute to the accuracy of resource statuses by submitting real-time updates.

### Preparation Guides
- Provides checklists tailored to different types of weather events (e.g., hurricanes, floods).
- Users can track their preparation steps and access historical data to improve readiness for future events.

## Design Rationale

### Why Django?
- Chosen for its robustness and scalability which is crucial for handling real-time data and high user loads.
- Django's ORM and administrative interface allow for efficient data management and quicker feature integrations.

### Frontend Technologies
- **Bootstrap**: Ensures a responsive and aesthetically pleasing interface across all devices.
- **HTMX**: Enhances HTML to enable AJAX capabilities directly within the markup, facilitating a dynamic and interactive user experience without full page reloads.

### Future Work
- Integration with mobile platforms to expand accessibility and user engagement.
- Implementation of machine learning algorithms for predictive analytics on weather patterns.

## Setup and Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/hurricane-preparedness-app.git
```
# Navigate to the project directory
```bash
cd hurricane-preparedness-app
```

# Install dependencies
```bash
pip install -r requirements.txt
```

# Run the application
```bash
python manage.py runserver
```
