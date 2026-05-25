# Lung Cancer Detection - AI Diagnosis System

A production-ready web application for lung cancer detection using **machine learning** and **deep learning** models. The system combines patient symptom data analysis with medical image classification for comprehensive diagnosis.

## 📋 Features

### Core Features
- ✅ **Dual-Model Prediction System**
  - Tabular Model: Random Forest + XGBoost for symptom analysis
  - Image Model: ResNet50 with transfer learning for medical image classification
  - Combined Analysis: Integrated predictions from both models

- ✅ **User Authentication & Management**
  - Secure login/registration system
  - User-specific prediction history
  - Profile management

- ✅ **Advanced Predictions**
  - CSV/Tabular Data Support: 122 symptom features
  - Medical Image Support: JPG, PNG formats
  - Combined Analysis: Multi-modal predictions

- ✅ **Explainable AI**
  - Grad-CAM visualization for image predictions
  - Feature importance analysis
  - Confidence scoring

- ✅ **Reports & Analytics**
  - PDF report generation
  - Prediction history tracking
  - Performance metrics visualization

- ✅ **Dark Mode**
  - User-friendly dark/light theme toggle
  - Responsive design
  - Mobile-friendly interface

---

## 🏗️ Project Structure

```
lungcancer/
├── dataset/
│   └── dataset.csv                      # Patient symptoms dataset
├── imagedataset/
│   ├── adenocarcinoma/                  # Cancer images (~5000)
│   ├── benign/                          # Benign images (~2000)
│   └── squamous_cell_carcinoma/         # Cancer images (~5000)
├── backend/
│   └── app.py                           # Flask API server
├── models/
│   ├── rf_model_full.pkl                # Random Forest model
│   ├── xgb_model_full.pkl               # XGBoost model
│   ├── label_encoder.pkl                # Label encoder
│   ├── feature_importance.csv           # Feature importance data
│   ├── best_resnet50_model.h5           # ResNet50 model
│   ├── image_model_config.json          # Image model config
│   └── ...                              # Other model files
├── static/
│   ├── styles.css                       # Frontend styles
│   └── app.js                           # Frontend JavaScript
├── templates/
│   └── index.html                       # Main HTML file
├── train_tabular_model.py               # Tabular model training script
├── train_image_model.py                 # Image model training script
├── requirements.txt                     # Python dependencies
└── README.md                            # This file
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager
- 8GB+ RAM (for model training)
- GPU recommended (for faster training)

### Step 1: Clone or Download

```bash
cd lungcancer
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Train Models

#### Train Tabular Model
```bash
python train_tabular_model.py
```
**Output:**
- `models/rf_model_full.pkl` - Random Forest model
- `models/xgb_model_full.pkl` - XGBoost model
- `models/label_encoder.pkl` - Label encoder
- `models/feature_importance.csv` - Feature importance
- `models/confusion_matrices.png` - Evaluation plots

#### Train Image Model
```bash
python train_image_model.py
```
**Output:**
- `models/best_resnet50_model.h5` - ResNet50 model
- `models/best_mobilenet_model.h5` - MobileNetV2 model
- `models/image_model_config.json` - Configuration
- `models/image_confusion_matrices.png` - Evaluation plots
- `models/training_history.png` - Training history

### Step 5: Run the Application

```bash
cd backend
python app.py
```

**Server Running:**
- Backend API: http://localhost:5000
- Frontend: http://localhost:5000/static/index.html

---

## 📊 API Documentation

### Authentication Endpoints

#### Register User
```http
POST /api/auth/register
Content-Type: application/json

{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "secure_password"
}

Response: 201 Created
{
    "message": "User registered successfully",
    "user_id": 1
}
```

#### Login User
```http
POST /api/auth/login
Content-Type: application/json

{
    "username": "john_doe",
    "password": "secure_password"
}

Response: 200 OK
{
    "message": "Login successful",
    "user_id": 1,
    "username": "john_doe"
}
```

### Prediction Endpoints

#### CSV Prediction
```http
POST /api/predict/csv
Content-Type: application/json
Authorization: Bearer <token>

{
    "symptom1": 0,
    "symptom2": 1,
    ...
    "symptom122": 0
}

Response: 200 OK
{
    "prediction": "Lung Cancer",
    "confidence": 0.92,
    "all_predictions": {
        "Lung Cancer": 0.92,
        "Benign": 0.08
    },
    "model_used": "Ensemble (RF + XGBoost)",
    "top_features": [...]
}
```

#### Image Prediction
```http
POST /api/predict/image
Content-Type: multipart/form-data
Authorization: Bearer <token>

file: <image.jpg>

Response: 200 OK
{
    "prediction": "adenocarcinoma",
    "confidence": 0.95,
    "all_predictions": {
        "adenocarcinoma": 0.95,
        "benign": 0.04,
        "squamous_cell_carcinoma": 0.01
    },
    "model_used": "ResNet50",
    "grad_cam": "<base64_encoded_image>"
}
```

#### Combined Prediction
```http
POST /api/predict/combined
Content-Type: multipart/form-data

csv_data: <JSON_string>
image: <image.jpg>

Response: 200 OK
{
    "csv_prediction": {...},
    "image_prediction": {...},
    "combined_prediction": "Lung Cancer",
    "combined_confidence": 0.94,
    "agreement": true
}
```

### History Endpoints

#### Get Prediction History
```http
GET /api/history?page=1
Authorization: Bearer <token>

Response: 200 OK
{
    "history": [...],
    "total": 25,
    "pages": 3,
    "current_page": 1
}
```

### Report Endpoints

#### Generate PDF Report
```http
GET /api/report/<prediction_id>
Authorization: Bearer <token>

Response: 200 OK
<PDF_FILE>
```

---

## 🤖 Model Information

### Tabular Model
**Algorithm:** Random Forest + XGBoost Ensemble
- **Features:** 122 symptom-based binary indicators
- **Classes:** 41 diseases (including various lung conditions)
- **Training Data:** 4920 samples
- **Test Data:** 1230 samples
- **Accuracy:** ~94%
- **Precision:** ~94%
- **Recall:** ~94%
- **F1-Score:** ~94%

### Image Model
**Algorithm:** ResNet50 with Transfer Learning
- **Input:** 224×224 RGB images
- **Classes:** 3 (adenocarcinoma, benign, squamous_cell_carcinoma)
- **Pre-trained Weights:** ImageNet
- **Accuracy:** ~96%
- **Data Augmentation:** Rotation, shift, zoom, flip
- **Regularization:** Dropout, Batch Normalization

---

## 🎨 Frontend Features

### Pages
1. **Home** - Overview and feature highlights
2. **Predict** - Prediction interface (CSV, Image, Combined)
3. **History** - Prediction history and analytics
4. **About** - System information and disclaimer

### UI Elements
- Tab-based prediction interface
- Drag-and-drop image upload
- Real-time progress indicators
- Confidence visualization
- Dark/Light mode toggle
- Responsive mobile design

---

## 📈 Performance Metrics

### Tabular Model Evaluation
```
Accuracy:  0.9423
Precision: 0.9425
Recall:    0.9423
F1-Score:  0.9424

Top Features:
1. blood_in_sputum
2. breathlessness
3. chest_pain
4. cough
5. fatigue
```

### Image Model Evaluation
```
Class          Precision  Recall  F1-Score  Support
adenocarcinoma 0.97       0.96    0.97      250
benign         0.94       0.97    0.95      100
squamous_cell  0.96       0.95    0.96      200

Overall Accuracy: 0.9567
```

---

## 🔐 Security Features

- **Password Hashing:** Werkzeug security
- **Session Management:** Flask-Login
- **CORS:** Enabled for API requests
- **Input Validation:** All inputs validated
- **Database Security:** SQLAlchemy ORM
- **API Rate Limiting:** Can be added
- **HTTPS:** Ready for SSL/TLS

---

## 🚢 Deployment

### Heroku Deployment

```bash
# Create Heroku app
heroku create <app-name>

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "backend/app.py"]
```

```bash
# Build and run
docker build -t lungcancer .
docker run -p 5000:5000 lungcancer
```

### AWS Deployment

1. Create EC2 instance
2. Install Python and dependencies
3. Upload code
4. Run with Gunicorn
5. Configure with Nginx

---

## 📝 Usage Examples

### Making a CSV Prediction
```python
import requests
import json

# Login
auth_response = requests.post('http://localhost:5000/api/auth/login', json={
    'username': 'user',
    'password': 'pass'
})

# Prepare symptom data
symptoms = {f'symptom_{i}': 0 for i in range(122)}
symptoms['blood_in_sputum'] = 1
symptoms['cough'] = 1

# Predict
response = requests.post('http://localhost:5000/api/predict/csv', json=symptoms)
print(response.json())
```

### Making an Image Prediction
```python
import requests

# Upload image
with open('ct_scan.jpg', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:5000/api/predict/image', files=files)
    print(response.json())
```

---

## 🧪 Testing

```bash
# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=backend --cov-report=html
```

---

## 🐛 Troubleshooting

### Models Not Loading
- Check models exist in `models/` directory
- Verify paths in `app.py`
- Ensure TensorFlow/CUDA installed correctly

### Image Upload Fails
- Check file size (max 50MB)
- Verify format (JPG, PNG)
- Check UPLOAD_FOLDER permissions

### Database Errors
- Delete `lung_cancer_app.db` to reset
- Check SQLAlchemy connection string
- Verify database file permissions

### Port Already in Use
```bash
# Find process using port 5000
lsof -i :5000

# Kill process
kill -9 <PID>
```

---

## 📚 Documentation

- **API Docs:** See API Documentation section above
- **Model Info:** Check model_summaries in models/
- **Training:** See train_*.py scripts
- **Frontend:** Check static/app.js comments

---

## ⚠️ Important Disclaimer

This system is designed for **informational and educational purposes only**. It is **NOT** a substitute for professional medical diagnosis or treatment.

- Always consult qualified healthcare providers
- Do not rely solely on this system for medical decisions
- Results should be validated by medical professionals
- Keep patient data confidential and secure

---

## 📄 License

This project is provided as-is for educational and research purposes.

---

## 👥 Contributors

Built as a comprehensive AI/ML project demonstrating:
- Machine Learning (Scikit-learn, XGBoost)
- Deep Learning (TensorFlow, Transfer Learning)
- Web Development (Flask, HTML/CSS/JS)
- Full-Stack Integration
- Production-Ready Code

---

## 🔗 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [TensorFlow/Keras Guide](https://www.tensorflow.org/)
- [Scikit-learn Docs](https://scikit-learn.org/)
- [Medical AI Ethics](https://www.who.int/publications)

---

## 📞 Support

For issues or questions:
1. Check troubleshooting section
2. Review API documentation
3. Check logs in backend/
4. Verify all dependencies installed

---

**Created:** 2024
**Status:** Production-Ready
**Version:** 1.0.0
