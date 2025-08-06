# 🤖 LLM Projects Portfolio

A comprehensive collection of AI and Large Language Model (LLM) projects showcasing practical applications of modern AI technologies.

## 📋 Project Overview

This repository contains a curated selection of AI-powered applications built using cutting-edge LLM technologies. Each project demonstrates real-world problem-solving capabilities and showcases different aspects of AI integration.

## 🚀 Featured Projects

### 📧 [Cold Email Generator](./ColdEmailGenerator/)
**AI-Powered Job Application Email Generator**

An intelligent application that automatically generates personalized cold emails for job applications by analyzing job postings and matching them with relevant portfolio items.

**Key Features:**
- 🔍 **Smart Job Analysis**: Extracts job requirements, skills, and descriptions from web pages
- 📝 **Personalized Email Generation**: Creates tailored emails using AI
- 🎯 **Portfolio Matching**: Matches job requirements with relevant portfolio items
- 🌐 **Web Scraping**: Automatically extracts content from job posting URLs
- 💼 **Professional Templates**: Generates business-ready email content

**Technologies:** Streamlit, LangChain, Google Gemini AI, FAISS Vector Database, Sentence Transformers

**[View Project Details →](./ColdEmailGenerator/)**

---

## 🛠 Technology Stack

### Core Technologies
- **Python 3.13+**: Primary programming language
- **Streamlit**: Web application framework
- **LangChain**: LLM orchestration framework
- **Google Gemini AI**: Advanced language model integration

### AI/ML Libraries
- **FAISS**: Vector similarity search
- **Sentence Transformers**: Text embedding generation
- **Pandas**: Data manipulation and analysis

### Development Tools
- **Git**: Version control
- **Virtual Environments**: Dependency management
- **Requirements.txt**: Package management

## 📁 Project Structure

```
LLM_Projects/
├── README.md                    # This file - Main portfolio overview
├── requirements.txt             # Global dependencies
├── ColdEmailGenerator/         # Cold Email Generator Project
│   ├── README.md              # Project-specific documentation
│   ├── main.py                # Streamlit application entry point
│   ├── chains.py              # LangChain processing logic
│   ├── portfolio.py           # FAISS vector database management
│   ├── utils.py               # Utility functions
│   ├── resources/             # Project resources
│   │   └── my_portfolio.csv   # Portfolio data
│   └── vectorstore/           # FAISS index storage
└── [Future Projects]          # Additional projects will be added here
```

## 🚀 Getting Started

### Prerequisites
- Python 3.13 or higher
- Git
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/LLM_Projects.git
   cd LLM_Projects
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install global dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to specific project**
   ```bash
   cd ColdEmailGenerator
   pip install -r requirements.txt
   ```

## 🔧 Environment Setup

### Required Environment Variables
Create a `.env` file in each project directory with the following variables:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

### API Keys Setup
1. **Google Gemini AI**: Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Add the API key to your project's `.env` file

## 📊 Project Status

| Project | Status | Last Updated | Version |
|---------|--------|--------------|---------|
| [Cold Email Generator](./ColdEmailGenerator/) | ✅ Active | 2024-08-06 | v1.0.0 |
| [Project 2] | 🚧 Coming Soon | - | - |
| [Project 3] | 🚧 Coming Soon | - | - |

## 🎯 Project Goals

- **Demonstrate AI Integration**: Show practical applications of LLM technologies
- **Solve Real Problems**: Address actual business and personal use cases
- **Educational Value**: Provide learning resources for AI/ML enthusiasts
- **Portfolio Showcase**: Display technical capabilities and project management skills

## 🤝 Contributing

We welcome contributions! Please feel free to:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Contribution Guidelines
- Follow PEP 8 Python style guidelines
- Add comprehensive documentation
- Include tests for new features
- Update README files as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

- **Developer**: Sabbir
- **Email**: [your-email@example.com]
- **LinkedIn**: [Your LinkedIn Profile]
- **Portfolio**: [Your Portfolio Website]

## 🙏 Acknowledgments

- **Google Gemini AI** for providing the language model capabilities
- **Streamlit** for the excellent web application framework
- **LangChain** for the powerful LLM orchestration tools
- **FAISS** for efficient vector similarity search

---

<div align="center">

**Made with ❤️ and ☕ by Sabbir**

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.48.0-red.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.27-green.svg)](https://langchain.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>