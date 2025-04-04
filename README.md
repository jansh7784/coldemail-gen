Here's the corrected and aligned `README.md` file for your project:

```markdown
# **Cold Email Generator**

The **Cold Email Generator** is a web application designed to automate the process of creating personalized cold emails for job applications. It simplifies the tedious task of writing tailored emails by providing a user-friendly interface and leveraging AI and machine learning techniques.

## **Overview**
- A **Streamlit frontend** for user interaction.
- A **Flask backend** for API functionalities.

This tool is ideal for job seekers who want to save time while ensuring their emails are professional and personalized.

## **Features**
1. **Resume Parsing**:
   - Upload resumes in PDF or DOCX format.
   - Automatically extract candidate details such as:
     - Name
     - Skills
     - Work experience
     - Education history
2. **Job Description Scraping**:
   - Input job URLs from platforms like LinkedIn or Indeed.
   - Scrape job descriptions using web scraping techniques to extract:
     - Job title
     - Required skills
     - Responsibilities
3. **Portfolio Integration**:
   - Match extracted skills with relevant portfolio links stored in a **ChromaDB** collection.
   - Automatically include portfolio links in the generated email.
4. **AI-Powered Email Generation**:
   - Use the **Groq API (`ChatGroq`)** to generate personalized cold emails.
   - Emails incorporate:
     - Job details
     - Candidate information
     - Portfolio links
5. **Flask API**:
   - Expose functionalities like:
     - Email generation
     - Analytics
     - Health checks
   - Accessible via RESTful APIs.
6. **Streamlit Frontend**:
   - A user-friendly interface for:
     - Uploading resumes
     - Inputting job URLs
     - Viewing and copying generated emails
7. **Analytics Dashboard**:
   - View usage statistics and insights, such as:
     - Popular skills
     - Common job types
     - Email generation trends

## **Technologies Used**
- **Frontend**: Streamlit
- **Backend**: Flask
- **Database**: ChromaDB (for portfolio querying)
- **AI Model**: Groq API (`ChatGroq`)
- **Web Scraping**: BeautifulSoup
- **Programming Language**: Python
- **Deployment**: Render

## **Folder Structure**
```plaintext
coldemail-gen/
├── app/                      # Streamlit app folder
│   ├── main.py               # Streamlit entry point
│   ├── chains.py             # AI chain logic
│   ├── portfolio.py          # Portfolio querying logic
│   └── utils.py              # Utility functions
├── flask_api/                # Flask API folder
│   ├── __init__.py           # Initialize Flask app
│   ├── routes.py             # API routes
├── templates/                # Flask templates
│   ├── dashboard.html        # Dashboard template
│   └── analytics.html        # Analytics view template
├── static/                   # Static files for Flask
│   └── css/
│       └── style.css         # Custom styles
├── run_api.py                # Flask application runner
├── requirements.txt          # Python dependencies
├── .gitignore                # Files to ignore in version control
├── README.md                 # Project documentation
```

## **Setup Instructions**

### **1. Prerequisites**
Before starting, ensure you have the following:
- Python 3.9 or higher installed.
- Git installed on your system.
- A Render account (for deployment).
- A valid **Groq API key** for email generation.

### **2. Clone the Repository**
Clone the project repository to your local machine:
```bash
git clone https://github.com/your-username/coldemail-gen.git
cd coldemail-gen
```

### **3. Create a Virtual Environment**
Set up a virtual environment to isolate dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **4. Install Dependencies**
Install all required Python packages:
```bash
pip install -r requirements.txt
```

### **5. Set Environment Variables**
Create a `.env` file in the root directory and add the following:
```plaintext
GROQ_API_KEY=your_groq_api_key
FLASK_API_URL=http://127.0.0.1:5000
```

### **6. Run the Flask API**
Start the Flask backend:
```bash
python run_api.py
```
The Flask API will be available at `http://127.0.0.1:5000`.

### **7. Run the Streamlit App**
In a new terminal, start the Streamlit frontend:
```bash
streamlit run app/main.py
```
The Streamlit app will be available at `http://localhost:8501`.

## **Deployment on Render**

### **1. Deploy the Flask API**
1. **Log in to Render**:
   - Go to [Render](https://render.com/) and log in to your account.
2. **Create a New Web Service**:
   - Click **New +** → **Web Service**.
3. **Connect Your Repository**:
   - Select the repository containing your project.
   - Choose the branch where your code is stored (e.g., `main`).
4. **Configure the Web Service**:
   - **Name**: `coldemail-api`
   - **Environment**: Python
   - **Build Command**:
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command**:
     ```bash
     gunicorn run_api:app
     ```
   - **Environment Variables**:
     - Add your `GROQ_API_KEY` in the **Environment** section:
       ```plaintext
       GROQ_API_KEY=your_groq_api_key
       ```
5. **Deploy**:
   - Click **Create Web Service**.
   - Render will build and deploy your Flask API. Once deployed, you’ll get a public URL (e.g., `https://coldemail-api.onrender.com`).

6. **Test the API**:
   - Visit the public URL in your browser or test specific endpoints like `/api/health` using `curl`:
     ```bash
     curl -X GET https://coldemail-api.onrender.com/api/health
     ```

### **2. Deploy the Streamlit Frontend**
1. **Create Another Web Service**:
   - Go to **New +** → **Web Service**.
2. **Connect Your Repository**:
   - Select the same repository as before.
3. **Configure the Web Service**:
   - **Name**: `coldemail-frontend`
   - **Environment**: Python
   - **Build Command**:
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command**:
     ```bash
     streamlit run app/main.py --server.port $PORT --server.enableCORS false
     ```
   - **Environment Variables**:
     - Add the `FLASK_API_URL` to point to your deployed Flask API:
       ```plaintext
       FLASK_API_URL=https://coldemail-api.onrender.com
       ```
4. **Deploy**:
   - Click **Create Web Service**.
   - Render will build and deploy your Streamlit app. Once deployed, you’ll get a public URL (e.g., `https://coldemail-frontend.onrender.com`).

5. **Test the Frontend**:
   - Open the Streamlit app URL in your browser and test the app.

## **API Endpoints**

### **1. Health Check**
- **Endpoint**: `/api/health`
- **Method**: GET
- **Description**: Check the health of the Flask API.

### **2. Generate Email**
- **Endpoint**: `/api/generate-email`
- **Method**: POST
- **Description**: Generate a cold email based on job URL and candidate details.
- **Request Body**:
  ```json
  {
      "job_url": "https://example.com/job",
      "candidate_details": {
          "name": "John Doe",
          "skills": ["Python", "AI/ML"],
          "experience": "5 years",
          "education": "B.Tech in Computer Science"
      }
  }
  ```

## **Future Enhancements**
1. **Authentication**:
   - Add API key-based authentication for secure access to the Flask API.
2. **Advanced Analytics**:
   - Provide detailed insights into email generation trends, popular skills, and job types.
3. **Mobile Integration**:
   - Develop a mobile app to interact with the Flask API.
4. **Multi-Language Support**:
   - Enable email generation in multiple languages.
5. **Improved Error Handling**:
   - Add more robust error handling and logging for better debugging.

## **Contributing**
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes.
4. Push to the branch and create a pull request.

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

## **Contact**
For any questions or feedback, feel free to reach out:
- **Email**: jansh7784@gmail.com
- **GitHub**: [your-username](https://github.com/jansh7784)
- **LinkedIn**: [Your Name](https://linkedin.com/in/ansh--jain)

---

This `README.md` provides a complete overview of your project, including deployment instructions for both the Flask API and Streamlit frontend on Render. Let me know if you need further adjustments.
```

You can copy and replace the content of your current `README.md` file with the above improved version.
