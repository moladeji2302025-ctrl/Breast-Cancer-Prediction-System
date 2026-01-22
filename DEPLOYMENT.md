# Vercel Deployment Guide

This guide will help you deploy the Breast Cancer Prediction System to Vercel.

## Prerequisites

- A Vercel account (free tier available)
- Git repository pushed to GitHub
- Vercel CLI (optional but recommended)

## Method 1: Deploy via Vercel Dashboard (Easiest)

### Step 1: Connect Repository
1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository: `moladeji2302025-ctrl/Breast-Cancer-Prediction-System`

### Step 2: Configure Project
1. **Framework Preset**: Select "Other"
2. **Build Command**: Leave empty
3. **Output Directory**: Leave as default
4. **Install Command**: `pip install -r requirements.txt`

### Step 3: Add vercel.json Configuration
Create a file named `vercel.json` in the root directory:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

### Step 4: Modify app.py for Vercel
Add this at the end of `app.py`:

```python
# For Vercel deployment
app_instance = app
```

### Step 5: Deploy
Click "Deploy" and wait for the build to complete.

## Method 2: Deploy via Vercel CLI

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Login to Vercel
```bash
vercel login
```

### Step 3: Deploy
```bash
cd Breast-Cancer-Prediction-System
vercel
```

Follow the prompts and your app will be deployed!

## Alternative: Render Deployment

Render is another excellent free hosting option that works well with Flask apps.

### Step 1: Create render.yaml
```yaml
services:
  - type: web
    name: breast-cancer-predictor
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: FLASK_DEBUG
        value: false
```

### Step 2: Add gunicorn to requirements.txt
```
gunicorn==21.2.0
```

### Step 3: Deploy
1. Go to [render.com](https://render.com)
2. Connect your GitHub repository
3. Select "Web Service"
4. Deploy!

## Alternative: Heroku Deployment

### Step 1: Create Procfile
```
web: gunicorn app:app
```

### Step 2: Create runtime.txt
```
python-3.11.0
```

### Step 3: Deploy
```bash
heroku login
heroku create breast-cancer-predictor
git push heroku main
```

## Post-Deployment

### Update Deployment Info
After successful deployment, update `BreastCancer_hosted_webGUI_link.txt`:

```
Name: Your Name
Matric Number: Your Matric Number
Machine Learning Algorithm Used: Logistic Regression
Model Persistence Method: Joblib
Live URL: https://your-app.vercel.app
GitHub Repository: https://github.com/moladeji2302025-ctrl/Breast-Cancer-Prediction-System
```

### Test Your Deployment
1. Visit your deployment URL
2. Enter sample values
3. Verify predictions work correctly

## Troubleshooting

### Issue: Module not found on Vercel
**Solution**: Ensure all dependencies are in requirements.txt with correct versions

### Issue: Model file not found
**Solution**: Verify model/breast_cancer_model.pkl is committed to git

### Issue: Build timeout
**Solution**: Use a smaller model or optimize dependencies

## Tips for Successful Deployment

1. **Keep dependencies minimal**: Only include what you need
2. **Test locally first**: Ensure app runs with `python app.py`
3. **Check logs**: Use platform logs to debug issues
4. **Set environment variables**: Configure FLASK_DEBUG=false
5. **Use HTTPS**: Most platforms provide free SSL

## Free Hosting Alternatives

If Vercel doesn't work, try:
- **Render.com**: Easy Python deployment
- **Railway.app**: Simple and fast
- **PythonAnywhere**: Python-specific hosting
- **Fly.io**: Global deployment
- **Cyclic.sh**: Modern deployment platform

---

**Good luck with your deployment! 🚀**
