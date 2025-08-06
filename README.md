# 🤖 LLM Projects Portfolio

A comprehensive collection of AI and Large Language Model (LLM) projects showcasing practical applications of modern AI technologies.

## 🚀 Featured Projects

### 📧 [Cold Email Generator](./ColdEmailGenerator/)
**AI-Powered Job Application Email Generator**

An intelligent application that automatically generates personalized cold emails for job applications by analyzing job postings and matching them with relevant portfolio items.


*Technologies:* Streamlit, LangChain, Google Gemini AI, FAISS Vector Database, Sentence Transformers

**[Live Link →](https://cold-mail-sabbir.streamlit.app/)**
---


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
| [MultiLingual RAG System] | 🚧 Coming Soon | - | - |
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

- **Developer**: Mohammad Sabbir Musfique
- **Email**: sabbir.musfique01.com
- **LinkedIn**: [https://www.linkedin.com/in/msmusfique063/]
- **Portfolio**: [https://sabbir-portfolio-five.vercel.app/]

---

<div align="center">

**Made with ❤️ and ☕ by Sabbir**

</div>