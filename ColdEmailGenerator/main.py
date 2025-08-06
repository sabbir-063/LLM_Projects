import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
import time
import requests
from urllib.parse import urlparse
import re

from chains import Chain #class
from portfolio import Portfolio #class
from utils import clean_text  #function


def validate_url(url):
    """Validate if the URL is properly formatted"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False


def check_url_accessibility(url):
    """Check if the URL is accessible and returns proper response"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        
        if response.status_code == 404:
            return False, "Page not found (404 error)"
        elif response.status_code == 403:
            return False, "Access forbidden (403 error)"
        elif response.status_code >= 500:
            return False, f"Server error ({response.status_code})"
        elif response.status_code != 200:
            return False, f"HTTP error {response.status_code}"
        else:
            return True, "URL is accessible"
    except requests.exceptions.ConnectionError:
        return False, "Connection error - unable to reach the website"
    except requests.exceptions.Timeout:
        return False, "Request timeout - website took too long to respond"
    except requests.exceptions.InvalidURL:
        return False, "Invalid URL format"
    except Exception as e:
        return False, f"Network error: {str(e)}"


def add_custom_css():
    """Add custom CSS for beautiful loading animation"""
    st.markdown("""
    <style>
    .loading-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
    }
    
    .loading-spinner {
        width: 50px;
        height: 50px;
        border: 4px solid #f3f3f3;
        border-top: 4px solid #3498db;
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin: 0 auto;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .loading-text {
        text-align: center;
        color: #666;
        margin-top: 10px;
        font-size: 16px;
    }
    
    .progress-container {
        background: linear-gradient(90deg, #3498db, #2ecc71);
        height: 6px;
        border-radius: 3px;
        overflow: hidden;
        margin: 10px 0;
    }
    
    .progress-bar {
        height: 100%;
        background: linear-gradient(90deg, #2ecc71, #3498db);
        animation: progress 2s ease-in-out infinite;
    }
    
    @keyframes progress {
        0% { width: 0%; }
        50% { width: 100%; }
        100% { width: 0%; }
    }
    
    .error-box {
        background: linear-gradient(135deg, #ff6b6b, #ee5a52);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
    }
    
    .warning-box {
        background: linear-gradient(135deg, #feca57, #ff9ff3);
        color: #2c3e50;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(254, 202, 87, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)


def show_loading_animation():
    """Show a beautiful loading animation"""
    st.markdown("""
    <div class="loading-container">
        <div>
            <div class="loading-spinner"></div>
            <div class="loading-text">🔄 Processing your request...</div>
        </div>
    </div>
    <div class="progress-container">
        <div class="progress-bar"></div>
    </div>
    """, unsafe_allow_html=True)


def show_error_message(error_type, message, details=""):
    """Show a beautiful error message"""
    if error_type == "error":
        st.markdown(f"""
        <div class="error-box">
            <h3>❌ {message}</h3>
            {f'<p><strong>Details:</strong> {details}</p>' if details else ''}
            <p><strong>💡 Tip:</strong> Please check the URL and try again with a valid job posting link.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="warning-box">
            <h3>⚠️ {message}</h3>
            {f'<p><strong>Details:</strong> {details}</p>' if details else ''}
        </div>
        """, unsafe_allow_html=True)


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")
    
    # Add custom CSS for loading animation
    add_custom_css()
    
    # Create a form to handle both Enter key and button click
    with st.form("email_generator_form"):
        url_input = st.text_input("Enter a URL:", value="")
        submit_button = st.form_submit_button("Submit")
        
        # This will trigger when user hits Enter OR clicks the button
        if submit_button:
            # Validate URL format first
            if not url_input.strip():
                show_error_message("error", "Please enter a URL", "The URL field cannot be empty.")
                return
            
            if not validate_url(url_input):
                show_error_message("error", "Invalid URL Format", 
                                "Please enter a valid URL starting with http:// or https://")
                return
            
            # Create a placeholder for the loading animation
            loading_placeholder = st.empty()
            
            try:
                # Show loading animation
                with loading_placeholder.container():
                    show_loading_animation()
                
                # Step 1: Check URL accessibility
                with st.spinner("🔍 Checking URL accessibility..."):
                    is_accessible, accessibility_message = check_url_accessibility(url_input)
                    if not is_accessible:
                        loading_placeholder.empty()
                        show_error_message("error", "URL Not Accessible", accessibility_message)
                        return
                
                # Step 2: Loading webpage
                with st.spinner("📥 Loading webpage..."):
                    try:
                        loader = WebBaseLoader([url_input])
                        documents = loader.load()
                        
                        if not documents:
                            loading_placeholder.empty()
                            show_error_message("error", "No Content Found", 
                                            "The webpage appears to be empty or inaccessible.")
                            return
                        
                        data = clean_text(documents[0].page_content)
                        
                        if not data or len(data.strip()) < 50:
                            loading_placeholder.empty()
                            show_error_message("warning", "Limited Content Found", 
                                            "The webpage content seems too short to extract job information.")
                            return
                            
                    except Exception as e:
                        loading_placeholder.empty()
                        if "404" in str(e).lower():
                            show_error_message("error", "Page Not Found (404)", 
                                            "The URL you provided doesn't exist or has been moved.")
                        elif "403" in str(e).lower():
                            show_error_message("error", "Access Forbidden (403)", 
                                            "The website is blocking access to this page.")
                        elif "timeout" in str(e).lower():
                            show_error_message("error", "Request Timeout", 
                                            "The website took too long to respond.")
                        else:
                            show_error_message("error", "Failed to Load Webpage", 
                                            f"Error: {str(e)}")
                        return
                
                # Step 3: Extracting job information
                with st.spinner("🔍 Extracting job information..."):
                    try:
                        jobs = llm.extract_jobs(data)
                    except Exception as e:
                        loading_placeholder.empty()
                        show_error_message("error", "Failed to Extract Job Information", 
                                        f"Error processing the webpage content: {str(e)}")
                        return
                
                # Clear loading animation
                loading_placeholder.empty()
                
                # Step 4: Generate emails with progress
                if jobs and len(jobs) > 0:
                    st.success(f"✅ Found {len(jobs)} job(s) to process")
                    
                    for i, job in enumerate(jobs, 1):
                        with st.spinner(f"📧 Generating email {i}/{len(jobs)}..."):
                            try:
                                skills = job.get('skills', [])
                                links = portfolio.query_links(skills)
                                email = llm.write_mail(job, links)
                                
                                # Display the email with a nice header
                                st.markdown(f"### 📧 Generated Email {i}")
                                st.code(email, language='markdown')
                                st.divider()
                            except Exception as e:
                                st.error(f"❌ Failed to generate email {i}: {str(e)}")
                else:
                    show_error_message("warning", "No Jobs Found", 
                                    "No job postings were detected on this webpage. Please try a different URL that contains job listings.")
                    
            except Exception as e:
                loading_placeholder.empty()
                show_error_message("error", "Unexpected Error", 
                                f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)


