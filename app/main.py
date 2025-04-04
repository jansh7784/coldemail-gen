import os
import streamlit as st
import requests
from bs4 import BeautifulSoup
from chains import Chain
from portfolio import Portfolio
from utils import clean_text, parse_resume, get_default_candidate_details

# Set USER_AGENT environment variable
os.environ['USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# Configure Streamlit page settings
st.set_page_config(
    layout="wide",
    page_title="Cold Email Generator",
    page_icon="📧"
)

# Initialize LLM chain and portfolio
chain = Chain()
portfolio = Portfolio()

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.8rem;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 10px;
        font-weight: bold;
    }
    .sub-title {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton>button {
        width: 100%;
    }
    .feedback-box {
        border: 1px solid #ddd;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def scrape_job_description(url: str) -> str:
    """Scrape job description from URL."""
    try:
        headers = {
            'User-Agent': os.getenv('USER_AGENT'),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
            
        # Get text content
        text = soup.get_text()
        
        # Clean the text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return text
        
    except Exception as e:
        raise Exception(f"Error scraping job description: {str(e)}")

def create_streamlit_app():
    # Centered Title and Subtitle
    st.markdown('<div class="main-title">📧 Cold Mail Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Generate personalized cold emails for job applications using AI!</div>', unsafe_allow_html=True)

    # Layout with two columns: Main content and Instructions
    col1, col2 = st.columns([3, 1])

    # Main Content Section (Left)
    with col1:
        # Resume Upload Section
        st.markdown("### 📄 Upload Your Resume")
        uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=['pdf', 'docx'])
        
        if uploaded_file:
            candidate_details = parse_resume(uploaded_file)
            st.success(f"✅ Resume parsed successfully for {candidate_details['name']}")
            
            # Display extracted information
            with st.expander("View Extracted Details"):
                st.write("**Name:**", candidate_details['name'])
                st.write("**Skills:**", ", ".join(candidate_details['skills']))
                st.write("**Education:**", "\n".join(candidate_details['education']))
                st.write("**Experience:**", "\n".join(candidate_details['experience']))
        else:
            candidate_details = get_default_candidate_details()
            st.info("ℹ️ Using default candidate details")

        # Job URLs Input Section
        st.markdown("### 🔗 Enter Job Details")
        url_input = st.text_area(
            "Enter Job URLs (one per line):", 
            placeholder="https://example.com/job1\nhttps://example.com/job2"
        )
        
        submit_button = st.button("🚀 Generate Emails")

        if submit_button:
            try:
                # Split URLs into a list
                urls = url_input.splitlines()
                if not urls:
                    st.warning("⚠️ Please enter at least one job URL.")
                    return

                # Load portfolio data
                portfolio.load_portfolio()

                for url in urls:
                    if not url.strip():
                        continue
                        
                    st.info(f"🔄 Processing job posting from {url}")
                    
                    try:
                        # Scrape and process job posting
                        job_text = scrape_job_description(url)
                        cleaned_data = clean_text(job_text)

                        # Extract job descriptions
                        jobs = chain.extract_jobs(cleaned_data)
                        if not jobs:
                            st.warning(f"⚠️ No job descriptions found for {url}")
                            continue

                        # Process each job
                        for i, job in enumerate(jobs, start=1):
                            st.subheader(f"📄 Job {i} from {url}")
                            
                            # Display job details
                            with st.expander("View Job Details"):
                                st.json(job)

                            # Get relevant portfolio links
                            links = portfolio.query_links(job.get('skills', []))

                            # Generate email
                            email = chain.write_mail(job, links, candidate_details)
                            
                            # Display generated email
                            with st.expander(f"📧 Generated Email for Job {i}"):
                                st.markdown(email)

                            # Feedback section
                            with st.expander("✍️ Provide Feedback"):
                                feedback = st.text_area(
                                    "How can we improve this email?",
                                    key=f"feedback_{i}_{url}"
                                )
                                if st.button("Submit Feedback", key=f"submit_{i}_{url}"):
                                    st.success("✅ Thank you for your feedback!")
                                    
                    except Exception as e:
                        st.error(f"❌ Error processing {url}: {str(e)}")
                        continue

            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")

    # Instructions Section (Right)
    with col2:
        with st.expander("📋 Instructions", expanded=True):
            st.write("1. **Upload your resume (optional)**")
            st.write("2. **Enter job URLs (one per line)**")
            st.write("3. **Click 'Generate Emails'**")
            st.write("4. **Review and customize emails**")
            st.write("5. **Provide feedback for improvement**")

        # Footer with LinkedIn link
        st.markdown("---")
        st.markdown(
            """
            <div style='text-align: center'>
                <p>Created by Ansh Jain</p>
                <a href='https://www.linkedin.com/in/ansh--jain' target='_blank'>
                    Connect on LinkedIn
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

# Run Streamlit app
if __name__ == "__main__":
    create_streamlit_app()
