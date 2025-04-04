import os
import requests
from flask import Blueprint, request, jsonify, render_template
from bs4 import BeautifulSoup

# Adjust the import path for the app module
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.chains import Chain
from app.portfolio import Portfolio
from app.utils import clean_text, get_default_candidate_details

api_bp = Blueprint('api', __name__)
chain = Chain()
portfolio = Portfolio()

def scrape_job_description(url: str) -> str:
    """Scrape job description from URL."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
            
        text = soup.get_text()
        return clean_text(text)
        
    except Exception as e:
        raise Exception(f"Error scraping job description: {str(e)}")

@api_bp.route('/')
def index():
    """Home page."""
    return render_template('dashboard.html')

@api_bp.route('/api/generate-email', methods=['POST'])
def generate_email():
    """Generate email from job URL."""
    try:
        data = request.json
        job_url = data.get('job_url')
        candidate_details = data.get('candidate_details', get_default_candidate_details())

        if not job_url:
            return jsonify({'error': 'Job URL is required'}), 400

        # Scrape and process job posting
        job_text = scrape_job_description(job_url)
        
        # Extract job descriptions
        jobs = chain.extract_jobs(job_text)
        if not jobs:
            return jsonify({'error': 'No job descriptions found'}), 404

        job = jobs[0]
        
        # Get portfolio links
        portfolio.load_portfolio()
        links = portfolio.query_links(job.get('skills', []))

        # Generate email
        email = chain.write_mail(job, links, candidate_details)

        return jsonify({
            'success': True,
            'job_details': job,
            'generated_email': email,
            'portfolio_links': links
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/api/analytics', methods=['GET'])
def get_analytics():
    """Get analytics data."""
    try:
        analytics_data = {
            'total_emails': 100,
            'popular_skills': [
                {'skill': 'Python', 'count': 45},
                {'skill': 'JavaScript', 'count': 35},
                {'skill': 'React', 'count': 30}
            ],
            'job_types': [
                {'type': 'Software Engineer', 'count': 50},
                {'type': 'Data Scientist', 'count': 30},
                {'type': 'Full Stack Developer', 'count': 20}
            ]
        }
        return jsonify(analytics_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/api/health')
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'services': {
            'groq_api': bool(os.getenv('GROQ_API_KEY')),
            'portfolio_db': portfolio.collection.count() > 0
        }
    })