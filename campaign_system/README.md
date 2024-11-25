Campaign System API
Overview
This project is a Django REST Framework (DRF) application for managing agents, campaigns, and campaign results. It provides a set of CRUD APIs to perform operations like creating, retrieving, updating, and deleting records for these entities.

Key Features:
Agents Management:

Create, update, delete, and fetch agents.
Includes details like name, language, and unique voice ID.
Campaigns Management:

Create, update, delete, and fetch campaigns.
Associate campaigns with agents and manage details like type (Inbound/Outbound), phone number, and status (Running, Paused, Completed).
Campaign Results Management:

Create, update, delete, and fetch campaign results.
Includes details like call outcome, duration, transcription, and related campaigns.
Technologies Used
Backend: Python, Django, Django REST Framework
Database: SQLite (default for Django)
Tools: Postman for API testing
Installation and Setup
Follow these steps to set up and run the project locally:

Prerequisites
Python 3.10 or higher
Virtual environment (venv or similar)
Postman (optional, for testing)
Steps
Clone the Repository:



bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Apply Migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the Server:

bash
Copy code
python manage.py runserver
Access the API:

Open your browser and visit: http://127.0.0.1:8000/.
API Endpoints
1. Agents API
Method	Endpoint	Description
GET	/api/agents/	Fetch all agents
POST	/api/agents/	Create a new agent
GET	/api/agents/<id>/	Fetch a specific agent
PUT	/api/agents/<id>/	Update a specific agent
DELETE	/api/agents/<id>/	Delete a specific agent
2. Campaigns API
Method	Endpoint	Description
GET	/api/campaigns/	Fetch all campaigns
POST	/api/campaigns/	Create a new campaign
GET	/api/campaigns/<id>/	Fetch a specific campaign
PUT	/api/campaigns/<id>/	Update a specific campaign
DELETE	/api/campaigns/<id>/	Delete a specific campaign
3. Campaign Results API
Method	Endpoint	Description
GET	/api/campaignresults/	Fetch all campaign results
POST	/api/campaignresults/	Create a new campaign result
GET	/api/campaignresults/<id>/	Fetch a specific campaign result
PUT	/api/campaignresults/<id>/	Update a specific campaign result
DELETE	/api/campaignresults/<id>/	Delete a specific campaign result
Sample Data for Testing
POST /api/campaignresults/
json
Copy code
{
  "name": "Campaign Result 1",
  "type": "Outbound Call",
  "phone": "123-456-7890",
  "cost": 15.75,
  "outcome": "Success",
  "call_duration": 120.5,
  "recording": "https://example.com/recording1.mp3",
  "summary": "The call was successful. The customer showed interest in the product.",
  "transcription": "Customer: Yes, I am interested. Agent: Great! Let me send you more information.",
  "campaign": 1
}
Running Tests
To test the API endpoints, you can use Postman or any API testing tool. Import the Postman collection included in the project and execute the requests.

Project Structure
bash
Copy code
Campaign_System/
├── core/                  # Main app
│   ├── admin.py           # Django admin configurations
│   ├── models.py          # Database models for Agent, Campaign, and CampaignResult
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API viewsets
│   └── urls.py            # App-specific URL patterns
├── campaign_system/       # Project settings
│   ├── settings.py        # Django project settings
│   ├── urls.py            # Project-wide URL patterns
│   └── wsgi.py            # WSGI application
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
Author
Aman Singh

Email: [aman8882112318@gmail.com]
Phone: [8882112318]
Let me know if you need further assistance!