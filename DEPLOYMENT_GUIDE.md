# LungCare AI - Deployment Guide

## 🚀 Quick Deployment Options

### **OPTION 1: RENDER.COM (Recommended - Simplest)**

**Steps:**
1. Create GitHub repository:
   ```bash
   git init
   git add .
   git commit -m "LungCare AI Application"
   git remote add origin https://github.com/YOUR_USERNAME/lungcancer.git
   git push -u origin main
   ```

2. Go to https://render.com
3. Sign in with GitHub
4. Click "New +" → "Web Service"
5. Connect your lungcancer repository
6. Configure:
   - **Name:** lungcare-ai
   - **Runtime:** Python
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python backend/app.py`
   - **Instance Type:** Free
7. Deploy!

**Your app will be live at:** `https://lungcare-ai.onrender.com`

---

### **OPTION 2: RAILWAY.APP**

**Steps:**
1. Go to https://railway.app
2. Sign in with GitHub
3. Click "Deploy from GitHub repo"
4. Select your lungcancer repository
5. Add environment variables:
   - `FLASK_ENV=production`
   - `FLASK_DEBUG=0`
6. Deploy automatically

**Your app will be live at:** `https://lungcare-ai.railway.app`

---

### **OPTION 3: DOCKER (Local or Cloud)**

**Build Docker Image:**
```bash
docker build -t lungcare-ai .
```

**Run Container:**
```bash
docker run -p 5000:5000 lungcare-ai
```

**Or use Docker Compose:**
```bash
docker-compose up
```

---

### **OPTION 4: PYTHONYWHERE (Best for Python Apps)**

1. Go to https://www.pythonanywhere.com
2. Create free account
3. Upload files via Git or Web UI
4. Configure WSGI file for Flask
5. Visit: `https://yourusername.pythonanywhere.com`

---

## 📦 GITHUB SHARING (Code Only)

1. **Create GitHub Repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/lungcancer.git
   cd lungcancer
   git add .
   git commit -m "LungCare AI - Lung Cancer Detection System"
   git push origin main
   ```

2. **Create README.md** with:
   - Features
   - Installation instructions
   - Local setup
   - Demo credentials

3. **Add .gitignore:**
   ```
   __pycache__/
   *.pyc
   *.db
   .env
   venv/
   .DS_Store
   ```

4. **Share GitHub link with others:**
   ```
   https://github.com/YOUR_USERNAME/lungcancer
   ```

---

## 🔧 PRODUCTION CONFIGURATION

Before deploying, update `backend/app.py`:

```python
# Change from
app.run(debug=True, host='0.0.0.0', port=5000)

# To
import os
debug_mode = os.environ.get('FLASK_DEBUG', 'False') == 'True'
port = int(os.environ.get('PORT', 5000))
app.run(debug=debug_mode, host='0.0.0.0', port=port)
```

---

## 📝 ENVIRONMENT VARIABLES

Create `.env` file (add to .gitignore):
```
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:pass@localhost/lungcare
```

---

## 🔐 SECURITY CHECKLIST

- [ ] Change admin password from 'admin123'
- [ ] Update `SECRET_KEY` in app.py
- [ ] Use PostgreSQL instead of SQLite for production
- [ ] Enable HTTPS
- [ ] Add rate limiting
- [ ] Validate all user inputs
- [ ] Keep dependencies updated

---

## 📊 ESTIMATED COSTS

| Platform | Free | Paid |
|----------|------|------|
| **Render** | 750 hrs/month | $7/month+ |
| **Railway** | $5/month credit | $5/month+ |
| **PythonAnywhere** | Limited | $5/month+ |
| **Heroku** | ❌ Removed | $7/month+ |
| **AWS** | 1 year free tier | $1+/month |

---

## ✅ LOCAL SETUP (For Others to Run)

Users can install locally:

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/lungcancer.git
cd lungcancer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python backend/app.py

# Visit http://localhost:5000
```

---

## 🎯 RECOMMENDED DEPLOYMENT PATH

**Best Option:** Render.com
- ✅ Free tier available
- ✅ Easy GitHub integration
- ✅ Auto-deploys on push
- ✅ No credit card required
- ✅ Scalable when needed

---

## 📞 SUPPORT

For issues:
1. Check logs on Render/Railway dashboard
2. Verify requirements.txt installed
3. Ensure port 5000 is available
4. Check environment variables
