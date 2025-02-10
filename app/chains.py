import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.3-70b-versatile"
        )

    def extract_jobs(self, cleaned_text):
        """
        Extracts job descriptions from a given text using AI.
        """
        try:
            prompt_extract = PromptTemplate.from_template(
                """
                ### SCRAPED JOB TEXT:
                {page_data}

                ### INSTRUCTIONS:
                Extract job postings and return a JSON with these keys: 
                - `role` (job title)
                - `experience` (required experience level)
                - `skills` (list of required skills)
                - `description` (full job description)

                ### OUTPUT FORMAT:
                Return a JSON array containing multiple jobs if found.
                Only return valid JSON.

                ### VALID JSON (NO PREAMBLE):
                """
            )

            chain_extract = prompt_extract | self.llm
            res = chain_extract.invoke({"page_data": cleaned_text})

            # Parse JSON output
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)

            return res if isinstance(res, list) else [res]

        except OutputParserException:
            raise OutputParserException("⚠️ Context too big. Unable to parse jobs.")

    def write_mail(self, job, links):
        """
        Generates a personalized cold email for the extracted job description.
        """
        try:
            prompt_email = PromptTemplate.from_template(
                """
                ### JOB DESCRIPTION:
                {job_description}

                ### RELEVANT PORTFOLIO LINKS:
                {link_list}

                ### INSTRUCTIONS:
                Write a professional cold email for applying to the job above.
                The email should:
                1️⃣ **Introduce the candidate** (Ansh Jain, pre-final year IT student at SKIT Jaipur).
                2️⃣ **Highlight key technical skills** (AI/ML, Full-Stack Development, Python, JavaScript).
                3️⃣ **Mention relevant projects** (Use portfolio links as reference).
                4️⃣ **Explain why Ansh is a perfect fit for the role** (Align experience with job requirements).
                5️⃣ **End with a compelling call-to-action** (e.g., requesting an interview or further discussion).

                Keep the email concise, impactful, and well-structured.

                ### EMAIL (NO PREAMBLE):
                """
            )

            # Debugging Output
            print(f"🔹 Generating email for job: {job}")
            print(f"🔹 Relevant links: {links}")

            chain_email = prompt_email | self.llm
            res = chain_email.invoke({"job_description": str(job), "link_list": links})

            return res.content if res and res.content else "⚠️ Error: Failed to generate email."

        except Exception as e:
            print(f"❌ Error in write_mail: {e}")
            return f"❌ An error occurred during email generation: {e}"
