Here’s a **comprehensive README.md** file for your project, including a detailed guide for deploying both the **Streamlit frontend** and **Flask backend** on **Render**. This will serve as a complete documentation for your project.

---*Cold Email Generator**

# **Cold Email Generator**
The **Cold Email Generator** is a web application designed to automate the process of creating personalized cold emails for job applications. It simplifies the tedious task of writing tailored emails by leveraging AI, web scraping, and portfolio integration. The application consists of:
## **Overview** frontend** for user interaction.
The **Cold Email Generator** is a web application designed to automate the process of creating personalized cold emails for job applications. It simplifies the tedious task of writing tailored emails by leveraging AI, web scraping, and portfolio integration. The application consists of:
- A **Streamlit frontend** for user interaction.
- A **Flask backend** for API functionalities.

This tool is ideal for job seekers who want to save time while ensuring their emails are professional and personalized.**Features**
1. **Resume Parsing**:
---umes (PDF or DOCX) to extract candidate details such as name, skills, experience, and education.

## **Features**
1. **Resume Parsing**:   - Input job URLs to scrape job descriptions using web scraping.
   - Upload resumes in PDF or DOCX format.
   - Automatically extract candidate details such as:
     - Name   - Match extracted skills with relevant portfolio links stored in a ChromaDB collection.
     - Skills
     - Work experience
     - Education history   - Generate personalized cold emails using the Groq API (`ChatGroq`), incorporating job details, candidate information, and portfolio links.

2. **Job Description Scraping**:
   - Input job URLs from platforms like LinkedIn or Indeed.   - Expose functionalities like email generation, analytics, and health checks via RESTful APIs.
   - Scrape job descriptions using web scraping techniques to extract:
     - Job title
     - Required skills   - User-friendly interface for uploading resumes, inputting job URLs, and viewing generated emails.
     - Responsibilities

3. **Portfolio Integration**:   - View usage statistics and insights into popular skills and job types.
   - Match extracted skills with relevant portfolio links stored in a **ChromaDB** collection.
   - Automatically include portfolio links in the generated email.

4. **AI-Powered Email Generation**:**Technologies Used**
   - Use the **Groq API (`ChatGroq`)** to generate personalized cold emails.- **Frontend**: Streamlit
   - Emails incorporate:
     - Job details(for portfolio querying)
     - Candidate information API (`ChatGroq`)
     - Portfolio links

5. **Flask API**:
   - Expose functionalities like:
     - Email generation
     - Analytics
     - Health checks**Folder Structure**
   - Accessible via RESTful APIs.```

6. **Streamlit Frontend**: app/                      # Streamlit app folder
   - A user-friendly interface for:y               # Streamlit entry point
     - Uploading resumes
     - Inputting job URLsgic
     - Viewing and copying generated emailsons

7. **Analytics Dashboard**:app
   - View usage statistics and insights, such as:
     - Popular skills
     - Common job typestemplate
     - Email generation trendstemplate
lask
---

## **Technologies Used**py                # Flask application runner
- **Frontend**: Streamlitencies
- **Backend**: Flaskon control
- **Database**: ChromaDB (for portfolio querying)on
- **AI Model**: Groq API (`ChatGroq`)
- **Web Scraping**: BeautifulSoup
- **Programming Language**: Python
- **Deployment**: Render
**Setup Instructions**
---

## **Folder Structure**- Python 3.9 or higher
```system
coldemail-gen/r deployment)
├── app/                      # Streamlit app folderration)
│   ├── main.py               # Streamlit entry point
│   ├── chains.py             # AI chain logic
│   ├── portfolio.py          # Portfolio querying logic```bash
│   └── utils.py              # Utility functionsur-username/coldemail-gen.git
├── flask_api/                # Flask API folderemail-gen
│   ├── __init__.py           # Initialize Flask app
│   ├── routes.py             # API routes
├── templates/                # Flask templates **3. Create a Virtual Environment**
│   ├── dashboard.html        # Dashboard template```bash
│   └── analytics.html        # Analytics view template
├── static/                   # Static files for Flaskvenv/bin/activate  # On Windows: venv\Scripts\activate
│   └── css/
│       └── style.css         # Custom styles
├── run_api.py                # Flask application runner **4. Install Dependencies**
├── requirements.txt          # Python dependencies```bash
├── .gitignore                # Files to ignore in version control
├── README.md                 # Project documentation
```
 **5. Set Environment Variables**
---Create a `.env` file in the root directory and add the following:

## **Setup Instructions**
SK_API_URL=http://127.0.0.1:5000
### **1. Prerequisites**
Before starting, ensure you have the following:
- Python 3.9 or higher installed. **6. Run the Flask API**
- Git installed on your system.```bash
- A Render account (for deployment).
- A valid **Groq API key** for email generation.
l be available at `http://127.0.0.1:5000`.
### **2. Clone the Repository**
Clone the project repository to your local machine:
```bashIn a new terminal, run:
git clone https://github.com/your-username/coldemail-gen.git
cd coldemail-genpy
```
 available at `http://localhost:8501`.
### **3. Create a Virtual Environment**
Set up a virtual environment to isolate dependencies:
```bash
python -m venv venv**Deployment on Render**
source venv/bin/activate  # On Windows: venv\Scripts\activate
```PI**

### **4. Install Dependencies**
Install all required Python packages:   - Go to [Render](https://render.com/) and log in to your account.
```bash
pip install -r requirements.txt
```   - Click **New +** → **Web Service**.

### **5. Set Environment Variables**
Create a `.env` file in the root directory and add the following:   - Select the repository containing your project.
```ur code is stored (e.g., `main`).
GROQ_API_KEY=your_groq_api_key
FLASK_API_URL=http://127.0.0.1:5000
```   - **Name**: `coldemail-api`

### **6. Run the Flask API**
Start the Flask backend:
```bashuirements.txt
python run_api.py
```
The Flask API will be available at `http://127.0.0.1:5000`.bash
pp
### **7. Run the Streamlit App**
In a new terminal, start the Streamlit frontend:les**:
```bashdd your `GROQ_API_KEY` in the **Environment** section:
streamlit run app/main.py
```
The Streamlit app will be available at `http://localhost:8501`.

---y**:
   - Click **Create Web Service**.
## **Deployment on Render**ll build and deploy your Flask API. Once deployed, you’ll get a public URL (e.g., `https://coldemail-api.onrender.com`).

### **1. Deploy the Flask API**
   - Visit the public URL in your browser or test specific endpoints like `/api/health` using `curl`:
1. **Log in to Render**:
   - Go to [Render](https://render.com/) and log in.

2. **Create a New Web Service**:
   - Click **New +** → **Web Service**.

3. **Connect Your Repository**: **2. Deploy the Streamlit Frontend**
   - Select the repository containing your project.
   - Choose the branch where your code is stored (e.g., `main`).
   - Go to **New +** → **Web Service**.
4. **Configure the Web Service**:
   - **Name**: `coldemail-api`
   - **Environment**: Python   - Select the same repository as before.
   - **Build Command**:
     ```bash
     pip install -r requirements.txt   - **Name**: `coldemail-frontend`
     ```
   - **Start Command**:
     ```bash
     gunicorn run_api:appuirements.txt
     ```
   - **Environment Variables**:
     - Add your `GROQ_API_KEY` in the **Environment** section:bash
       ```.py --server.port $PORT --server.enableCORS false
       GROQ_API_KEY=your_groq_api_key
       ```
dd the `FLASK_API_URL` to point to your deployed Flask API:
5. **Deploy**:
   - Click **Create Web Service**.
   - Render will build and deploy your Flask API. Once deployed, you’ll get a public URL (e.g., `https://coldemail-api.onrender.com`).

6. **Test the API**:y**:
   - Visit the public URL in your browser or test specific endpoints like `/api/health` using `curl`:   - Click **Create Web Service**.
     ```bashll build and deploy your Streamlit app. Once deployed, you’ll get a public URL (e.g., `https://coldemail-frontend.onrender.com`).
     curl -X GET https://coldemail-api.onrender.com/api/health
     ```
   - Open the Streamlit app URL in your browser and test the app.
---

### **2. Deploy the Streamlit Frontend**
**API Endpoints**
1. **Create Another Web Service**:
   - Go to **New +** → **Web Service**.k**
- **Endpoint**: `/api/health`
2. **Connect Your Repository**:
   - Select the same repository as before.health of the Flask API.

3. **Configure the Web Service**:
   - **Name**: `coldemail-frontend`- **Endpoint**: `/api/generate-email`
   - **Environment**: Python
   - **Build Command**:ail based on job URL and candidate details.
     ```bash:
     pip install -r requirements.txt
     ```
   - **Start Command**:b_url": "https://example.com/job",
     ```bash   "candidate_details": {
     streamlit run app/main.py --server.port $PORT --server.enableCORS false
     ```", "AI/ML"],
   - **Environment Variables**:ars",
     - Add the `FLASK_API_URL` to point to your deployed Flask API:er Science"
       ```
       FLASK_API_URL=https://coldemail-api.onrender.com
       ```

4. **Deploy**:
   - Click **Create Web Service**.
   - Render will build and deploy your Streamlit app. Once deployed, you’ll get a public URL (e.g., `https://coldemail-frontend.onrender.com`).**Future Enhancements**
1. **Authentication**:
5. **Test the Frontend**:hentication for secure access to the Flask API.
   - Open the Streamlit app URL in your browser and test the app.

---   - Provide detailed insights into email generation trends, popular skills, and job types.

## **API Endpoints**
   - Develop a mobile app to interact with the Flask API.
### **1. Health Check**
- **Endpoint**: `/api/health`
- **Method**: GET   - Enable email generation in multiple languages.
- **Description**: Check the health of the Flask API.

### **2. Generate Email**   - Add more robust error handling and logging for better debugging.
- **Endpoint**: `/api/generate-email`
- **Method**: POST
- **Description**: Generate a cold email based on job URL and candidate details.
- **Request Body**:**Contributing**
```jsonContributions are welcome! Please follow these steps:
{ory.
    "job_url": "https://example.com/job",
    "candidate_details": {
        "name": "John Doe",
        "skills": ["Python", "AI/ML"],
        "experience": "5 years",
        "education": "B.Tech in Computer Science"
    }**License**
}This project is licensed under the MIT License. See the `LICENSE` file for details.
```

---
**Contact**
## **Future Enhancements**For any questions or feedback, feel free to reach out:
1. **Authentication**:our-email@example.com
   - Add API key-based authentication for secure access to the Flask API.username)
/linkedin.com/in/your-profile)
2. **Advanced Analytics**:
   - Provide detailed insights into email generation trends, popular skills, and job types.

3. **Mobile Integration**:s `README.md` provides a complete overview of your project, including deployment instructions for both the Flask API and Streamlit frontend on Render. Let me know if you need further adjustments! 🚀---
   - Develop a mobile app to interact with the Flask API.

4. **Multi-Language Support**:1. **Authentication**:
   - Enable email generation in multiple languages.hentication for secure access to the Flask API.

5. **Improved Error Handling**:
   - Add more robust error handling and logging for better debugging.   - Provide detailed insights into email generation trends, popular skills, and job types.

---
   - Develop a mobile app to interact with the Flask API.
## **Contributing**
Contributions are welcome! Please follow these steps:
1. Fork the repository.   - Enable email generation in multiple languages.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes.
4. Push to the branch and create a pull request.   - Add more robust error handling and logging for better debugging.

---

## **License****Contributing**
This project is licensed under the MIT License. See the `LICENSE` file for details.Contributions are welcome! Please follow these steps:
ory.
---

## **Contact**
For any questions or feedback, feel free to reach out:
- **Email**: jansh7784@gmail.com
- **GitHub**: [your-username](https://github.com/jansh7784)
- **LinkedIn**: [Your Name](https://linkedin.com/in/ansh--jain)**License**
This project is licensed under the MIT License. See the `LICENSE` file for details.
---

This `README.md` provides a complete overview of your project, including deployment instructions for both the Flask API and Streamlit frontend on Render. Let me know if you need further adjustments! 🚀
