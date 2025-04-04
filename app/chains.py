import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from typing import Dict, Any, List
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.3-70b-versatile"
        )

    def extract_jobs(self, cleaned_text: str) -> List[Dict[str, Any]]:
        """Extract job descriptions from text."""
        try:
            prompt_extract = PromptTemplate.from_template(
                """
                ### SCRAPED JOB TEXT:
                {page_data}

                ### INSTRUCTIONS:
                Extract job postings and return a JSON with these keys: 
                - `role` (job title)
                - `company` (company name if available)
                - `experience` (required experience level)
                - `skills` (list of required skills)
                - `description` (full job description)
                - `requirements` (list of key requirements)
                - `responsibilities` (list of key responsibilities)

                ### OUTPUT FORMAT:
                Return a JSON array containing multiple jobs if found.
                Only return valid JSON.

                ### VALID JSON (NO PREAMBLE):
                """
            )

            chain_extract = prompt_extract | self.llm
            res = chain_extract.invoke({"page_data": cleaned_text})

            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)

            return res if isinstance(res, list) else [res]

        except Exception as e:
            print(f"Error extracting jobs: {str(e)}")
            return []

    def write_mail(self, job: Dict[str, Any], links: List[str], candidate_details: Dict[str, Any]) -> str:
        """Generate personalized cold email."""
        try:
            prompt_email = PromptTemplate.from_template(
                """
                ### JOB DETAILS:
                Role: {job_role}
                Company: {company}
                Description: {job_description}
                Required Skills: {required_skills}
                
                ### CANDIDATE DETAILS:
                Name: {candidate_name}
                Skills: {candidate_skills}
                Experience: {candidate_experience}
                Education: {candidate_education}
                
                ### PORTFOLIO LINKS:
                {portfolio_links}

                ### INSTRUCTIONS:
                Write a professional cold email for applying to the job above.
                The email should:
                1️⃣ Start with a proper greeting and introduction
                2️⃣ Show enthusiasm for the role and company
                3️⃣ Highlight matching skills and relevant experience
                4️⃣ Mention specific projects/portfolio items that demonstrate expertise
                5️⃣ Explain why the candidate is a perfect fit
                6️⃣ Include a clear call-to-action
                7️⃣ End with a professional closing

                Keep the email:
                - Concise (3-4 paragraphs)
                - Professional but personable
                - Focused on value proposition
                - Error-free and well-structured

                ### EMAIL (NO PREAMBLE):
                """
            )

            # Prepare input data
            input_data = {
                "job_role": job.get("role", "the position"),
                "company": job.get("company", "your company"),
                "job_description": job.get("description", ""),
                "required_skills": ", ".join(job.get("skills", [])),
                "candidate_name": candidate_details.get("name", ""),
                "candidate_skills": ", ".join(candidate_details.get("skills", [])),
                "candidate_experience": " | ".join(candidate_details.get("experience", [])),
                "candidate_education": " | ".join(candidate_details.get("education", [])),
                "portfolio_links": "\n".join([f"- {link}" for link in links]) if links else "No specific portfolio links available."
            }

            chain_email = prompt_email | self.llm
            res = chain_email.invoke(input_data)

            return res.content if res and res.content else "⚠️ Error: Failed to generate email."

        except Exception as e:
            print(f"Error generating email: {str(e)}")
            return f"❌ An error occurred during email generation: {str(e)}"