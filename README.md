# Simple DevOps Project with SRE Responsibility

## Project Overview
This project is a simple web application built with Flask (Python) and deployed on Vercel. It includes a CI/CD pipeline using GitHub Actions and basic monitoring with UptimeRobot.

## Table of Contents
- Setup
- Running the Application
- CI/CD Pipeline
- Monitoring and Alerting
- Deployment
- Contributing
- License

## Setup
1. **Clone the repository**:
   ```bash
   git clone <https://github.com/PreciousEddy/Simple-DevOps-Project-with-SRE-Responsibility.git>
   cd Simple-DevOps-Project-with-SRE-Responsibility
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
1. **Run the Flask app**:
   ```bash
   python app.py
   ```
2. **Access the application**: Open your browser and go to `http://127.0.0.1:5000/`.

## CI/CD Pipeline
This project uses GitHub Actions for continuous integration and deployment.

1. **GitHub Actions Workflow**:
   - The workflow is defined in `.github/workflows/ci.yml`.
   - It sets up Python, installs dependencies, and runs tests on every push and pull request.

## Monitoring and Alerting
We use UptimeRobot to monitor the health of the application.

1. **Create an account on UptimeRobot**: Go to UptimeRobot and sign up.
2. **Add a new monitor**:
   - Monitor Type: HTTP(s)
   - Friendly Name: My Flask App Health Check
   - URL: `http://yourapp.com/health`
   - Monitoring Interval: Every 5 minutes
3. **Configure alerting**:
   - Set up alert contacts in UptimeRobot settings.
   - Assign alert contacts to your monitor to receive notifications via email or SMS if the endpoint is down.

## Deployment
The application is deployed on Vercel.

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Deploy the application**:
   ```bash
   vercel
   ```

3. **Configure environment variables** (if needed):
   - Go to your Vercel dashboard.
   - Navigate to your project settings.
   - Add necessary environment variables.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

---