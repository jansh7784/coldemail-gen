import re
import PyPDF2
from docx import Document  # Changed import statement
from typing import Dict, Any, Optional

def clean_text(text: str) -> str:
    """Clean text by removing HTML tags, URLs, and special characters."""
    # Remove HTML tags
    text = re.sub(r'<[^>]*?>', '', text)
    # Remove URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    # Remove special characters but keep periods and commas
    text = re.sub(r'[^a-zA-Z0-9\s.,]', '', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s{2,}', ' ', text)
    # Trim leading and trailing whitespace
    return text.strip()

def extract_name_from_text(text: str) -> str:
    """Extract name from the first few lines of text using simple heuristics."""
    # Look for common name patterns in the first few lines
    lines = text.split('\n')[:5]  # Check first 5 lines
    
    # Common name indicators
    name_indicators = ['name:', 'Name:', 'NAME:']
    
    for line in lines:
        # Check for explicit name indicators
        for indicator in name_indicators:
            if indicator in line:
                return line.split(indicator)[1].strip()
        
        # Check for a line with 2-3 words that might be a name
        words = line.strip().split()
        if 2 <= len(words) <= 3 and all(word.isalpha() for word in words):
            return line.strip()
    
    return "Unknown"

def extract_text_from_pdf(file) -> str:
    """Extract text from a PDF file."""
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        raise Exception(f"Error extracting text from PDF: {str(e)}")

def extract_text_from_docx(file) -> str:
    """Extract text from a DOCX file."""
    try:
        doc = Document(file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        raise Exception(f"Error extracting text from DOCX: {str(e)}")

def extract_skills(text: str) -> list:
    """Extract skills from text using keyword matching."""
    # Common technical skills keywords
    skill_keywords = {
        'languages': [
            'python', 'java', 'javascript', 'c++', 'ruby', 'php', 'typescript',
            'html', 'css', 'sql', 'rust', 'golang', 'swift'
        ],
        'frameworks': [
            'django', 'flask', 'fastapi', 'react', 'angular', 'vue', 'spring',
            'express', 'node.js', 'next.js', 'bootstrap', 'tailwind'
        ],
        'databases': [
            'mysql', 'postgresql', 'mongodb', 'redis', 'elasticsearch',
            'sqlite', 'oracle', 'cassandra'
        ],
        'tools': [
            'git', 'docker', 'kubernetes', 'jenkins', 'aws', 'azure', 'gcp',
            'jira', 'confluence', 'linux', 'nginx', 'ci/cd'
        ],
        'concepts': [
            'api', 'rest', 'graphql', 'microservices', 'agile', 'scrum',
            'testing', 'debugging', 'optimization'
        ]
    }
    
    found_skills = set()
    text_lower = text.lower()
    
    # Extract skills using keyword matching
    for category in skill_keywords.values():
        for skill in category:
            if skill in text_lower:
                found_skills.add(skill.title())  # Capitalize skill names
    
    return list(found_skills)

def parse_resume(file) -> Dict[str, Any]:
    """Parse resume to extract candidate details."""
    try:
        # Extract text based on file type
        if file.name.lower().endswith('.pdf'):
            text = extract_text_from_pdf(file)
        elif file.name.lower().endswith(('.docx', '.doc')):
            text = extract_text_from_docx(file)
        else:
            raise ValueError("Unsupported file format. Please upload PDF or DOCX file.")

        # Clean extracted text
        text = clean_text(text)

        # Extract information
        name = extract_name_from_text(text)
        skills = extract_skills(text)

        # Extract education (simple pattern matching)
        education = []
        education_keywords = ['bachelor', 'master', 'phd', 'b.tech', 'm.tech', 'degree']
        for line in text.lower().split('\n'):
            if any(keyword in line for keyword in education_keywords):
                education.append(line.strip().title())

        # Extract experience (looking for years/months patterns)
        experience = []
        exp_pattern = r'\d+\s*(?:year|yr|month)s?\s+(?:of\s+)?experience'
        experience_matches = re.finditer(exp_pattern, text.lower())
        for match in experience_matches:
            experience.append(match.group().title())

        return {
            'name': name,
            'skills': skills,
            'education': education,
            'experience': experience or ["No explicit experience mentioned"],
            'raw_text': text
        }

    except Exception as e:
        return get_default_candidate_details()

def get_default_candidate_details() -> Dict[str, Any]:
    """Return default candidate details."""
    return {
        'name': "Ansh Jain",
        'skills': [
            'Python',
            'JavaScript',
            'React',
            'Node.js',
            'SQL',
            'Machine Learning'
        ],
        'education': [
            'Pre-final Year IT Student at SKIT Jaipur'
        ],
        'experience': [
            'Full-Stack Development',
            'AI/ML Projects',
            'Web Development'
        ],
        'raw_text': ""
    }