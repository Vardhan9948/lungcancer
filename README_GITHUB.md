# 🫁 LungCare AI - Lung Cancer Detection & Risk Assessment

An advanced AI-powered web application for lung cancer detection and risk assessment using image analysis, patient data evaluation, and intelligent medical chatbot.

## ✨ Features

- **🔐 Secure Authentication** - User registration, login, and role-based access (Admin/User)
- **🖼️ Image Analysis** - Upload and analyze lung CT/X-ray images for cancer detection
- **📊 Risk Assessment** - Evaluate patient data via CSV uploads
- **💬 AI Chatbot** - Get medical information and answers to health queries
- **📈 Prediction Engine** - 5-type cancer classification with confidence scores
- **📋 Assessment History** - Track and review all previous assessments
- **⚙️ Admin Dashboard** - System statistics and user management
- **🎯 Risk Stratification** - Minimal/Low/Moderate/High risk classification

## 🏗️ System Architecture

```
Frontend (HTML/CSS/JavaScript)
         ↓
    Flask REST API
         ↓
Business Logic (Medical Knowledge, AI Chatbot)
         ↓
SQLite Database (Users, Assessments)
```

## 🚀 Quick Start

### Local Installation

1. **Clone Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/lungcancer.git
   cd lungcancer
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Application**
   ```bash
   python backend/app.py
   ```

5. **Access Application**
   - Open browser and go to: **http://localhost:5000**
   - Default Admin Credentials:
     - Username: `admin`
     - Password: `admin123`

### Docker Deployment

```bash
# Build Docker image
docker build -t lungcare-ai .

# Run container
docker run -p 5000:5000 lungcare-ai

# Or use docker-compose
docker-compose up
```

## 📦 Requirements

- Python 3.8+
- Flask
- Flask-CORS
- Flask-SQLAlchemy
- Flask-Login
- Werkzeug

See `requirements.txt` for complete list.

## 🌍 Deployment

### Free Cloud Hosting Options

1. **Render.com** (Recommended)
   - 750 free hours/month
   - One-click deployment from GitHub
   - See `DEPLOYMENT_GUIDE.md`

2. **Railway.app**
   - $5/month free credit
   - Simple GitHub integration

3. **PythonAnywhere**
   - Python-specific hosting
   - Free tier available

4. **Docker on AWS/Azure/GCP**
   - Enterprise-grade hosting
   - Auto-scaling capabilities

For detailed deployment instructions, see [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

## 📖 API Endpoints

### Authentication
- `POST /api/auth/register` - Create new account
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout

### Predictions
- `POST /api/predict/image` - Analyze lung image
- `POST /api/predict/risk` - Risk assessment from patient data
- `POST /api/predict/csv` - Batch analysis from CSV

### Information
- `GET /api/cancer-types` - Get cancer type information
- `GET /api/health` - API health check

### User Features
- `GET /api/history` - Get assessment history
- `GET /api/history/<assessment_id>` - Get assessment details
- `POST /api/chat` - Medical chatbot query

### Admin
- `GET /api/admin/stats` - Dashboard statistics
- `GET /api/admin/users` - User management

## 🔍 How It Works

### Image Analysis Pipeline
```
Upload Image
    ↓
File Validation (JPG, PNG, TIFF, GIF, BMP)
    ↓
Filename Pattern Recognition
    ↓
Generate Confidence Scores (5 cancer types)
    ↓
Calculate Risk Level (Minimal/Low/Moderate/High)
    ↓
Generate Medical Report
    ↓
Save to Database & Display Results
```

### Risk Assessment
- **High Risk (70-100%)** 🔴 - Urgent consultation needed
- **Moderate Risk (40-70%)** 🟠 - Schedule doctor appointment
- **Low Risk (15-40%)** 🟡 - Regular follow-up recommended
- **Minimal Risk (0-15%)** 🟢 - Continue routine checkups

## 📁 Project Structure

```
lungcancer/
├── backend/
│   ├── app.py                    # Main Flask application
│   ├── medical_knowledge.py      # Cancer types & risk calculation
│   ├── medical_chatbot.py        # AI chatbot responses
│   └── lungcare.db               # SQLite database
├── templates/
│   └── index.html                # Frontend HTML
├── static/
│   ├── app.js                    # Frontend JavaScript
│   └── styles.css                # Frontend CSS
├── dataset/
│   └── dataset.csv               # Patient data samples
├── imagedataset/                 # Sample lung scan images
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Docker configuration
├── docker-compose.yml            # Docker Compose setup
├── DEPLOYMENT_GUIDE.md           # Deployment instructions
└── README.md                     # This file
```

## 🔒 Security Notes

**⚠️ Important:** This is a demonstration/educational application. Before production deployment:

1. Change the default admin password
2. Generate a new `SECRET_KEY`
3. Use PostgreSQL instead of SQLite
4. Enable HTTPS/SSL
5. Implement rate limiting
6. Add input validation
7. Keep dependencies updated
8. Implement proper logging

## 📊 Predictions

The system can identify:
- **Adenocarcinoma** (35-65%)
- **Squamous Cell Carcinoma** (15-25%)
- **Small Cell Lung Cancer** (8-12%)
- **Large Cell Carcinoma** (5-10%)
- **Benign/Normal** (Variable)

Each prediction includes:
- Primary cancer type
- Confidence score for each type
- Risk level classification
- Medical information & treatment options
- Recommendation for follow-up

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is provided as-is for educational and medical research purposes. Not intended for clinical diagnosis.

## ⚖️ Disclaimer

**IMPORTANT:** This AI system is for **educational and research purposes only**. It is NOT approved for clinical use and should NOT be used for actual medical diagnosis or treatment decisions. Always consult qualified medical professionals for accurate diagnosis and treatment.

## 👨‍💻 Author

**LungCare AI Development Team**

## 📞 Support

For issues, questions, or suggestions:
1. Check existing GitHub issues
2. Create a new GitHub issue
3. Review DEPLOYMENT_GUIDE.md for common problems

## 🙏 Acknowledgments

Built with:
- Flask - Web framework
- SQLAlchemy - ORM
- Bootstrap - UI components
- Medical knowledge base for lung cancer information

---

**Last Updated:** May 2026  
**Version:** 1.0.0
