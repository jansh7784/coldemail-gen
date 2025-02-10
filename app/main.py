import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

# Configure Streamlit page settings
st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")

# Initialize LLM chain and portfolio
chain = Chain()
portfolio = Portfolio()

def create_streamlit_app():
    st.title("📧 Cold Mail Generator")
    st.markdown("**Generate tailored cold emails for job applications using AI!**")

    # User Input
    url_input = st.text_input("🔗 Enter Job URL:", value="https://jobs.nike.com/job/R-33460")
    submit_button = st.button("🚀 Generate Email")

    if submit_button:
        try:
            # Load and clean job description
            st.info("🔄 Extracting job details, please wait...")
            loader = WebBaseLoader([url_input])
            raw_data = loader.load().pop().page_content
            cleaned_data = clean_text(raw_data)

            # Load portfolio
            portfolio.load_portfolio()

            # Extract job descriptions
            jobs = chain.extract_jobs(cleaned_data)
            if not jobs:
                st.warning("⚠️ No job descriptions found. Please check the URL.")
                return

            # Display Job Descriptions and Generate Emails
            st.subheader("📄 Extracted Job Descriptions")
            for i, job in enumerate(jobs, start=1):
                st.write(f"### 🏆 Job {i}")
                st.json(job)

                # Extract skills and fetch portfolio links
                skills = job.get("skills", [])
                links = portfolio.query_links(skills)

                # Generate email using AI
                email = chain.write_mail(job, links)
                if not email:
                    email = "⚠️ Error generating email. Please check input data."

                # Show Email in Expander
                with st.expander(f"📧 Generated Email for Job {i}"):
                    st.markdown(email, unsafe_allow_html=True)

                # Feedback Section
                feedback = st.text_area(f"✍️ Provide Feedback for Email {i}", key=f"feedback_{i}")
                if st.button(f"Submit Feedback for Email {i}", key=f"submit_feedback_{i}"):
                    st.success("✅ Thank you for your feedback!")

        except Exception as e:
            st.error(f"❌ An Error Occurred: {e}")

# Run Streamlit app
if __name__ == "__main__":
    create_streamlit_app()
