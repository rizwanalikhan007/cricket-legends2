# 🐍 Deploy Backend on PythonAnywhere (FREE)

## Why PythonAnywhere?
- ✅ 100% FREE forever (no credit card needed)
- ✅ Designed specifically for Python/Flask apps
- ✅ Supports SQLite databases
- ✅ Always-on (doesn't sleep like Render free tier)
- ✅ Super easy setup (5 minutes)

---

## 📋 Step-by-Step Deployment

### Step 1: Create Account (1 minute)

1. Go to: **https://www.pythonanywhere.com**
2. Click **"Pricing & signup"**
3. Click **"Create a Beginner account"** (FREE)
4. Fill in:
   - Username: (choose any username, e.g., `rizwanalikhan`)
   - Email: your email
   - Password: create a password
5. Click **"Register"**
6. Verify your email

---

### Step 2: Upload Your Code (2 minutes)

1. Once logged in, click **"Consoles"** tab
2. Click **"Bash"** to open a terminal
3. In the terminal, run these commands:

```bash
# Clone your repository
git clone https://github.com/rizwanalikhan007/cricket-legends2.git

# Navigate to backend
cd cricket-legends2/backend

# Install dependencies
pip3 install --user flask flask-cors gunicorn

# Initialize database
python3 init_db.py
```

Wait for it to finish. You should see "Database initialized with 118 cricketers."

---

### Step 3: Create Web App (2 minutes)

1. Click **"Web"** tab at the top
2. Click **"Add a new web app"**
3. Click **"Next"** (for your domain)
4. Choose **"Manual configuration"**
5. Choose **"Python 3.10"**
6. Click **"Next"**

---

### Step 4: Configure WSGI File

1. In the **"Code"** section, find **"WSGI configuration file"**
2. Click on the file path (something like `/var/www/YOUR_USERNAME_pythonanywhere_com_wsgi.py`)
3. **Delete ALL the content** in the file
4. Paste this code:

```python
import sys
import os

# Add your project directory to sys.path
project_home = '/home/YOUR_USERNAME/cricket-legends2/backend'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Import Flask app
from app import app as application

# Enable CORS
application.config['CORS_HEADERS'] = 'Content-Type'
```

5. **IMPORTANT**: Replace `YOUR_USERNAME` with your PythonAnywhere username
6. Click **"Save"** (top right)

---

### Step 5: Set Working Directory

1. Go back to **"Web"** tab
2. Scroll to **"Code"** section
3. Find **"Working directory"**
4. Set it to: `/home/YOUR_USERNAME/cricket-legends2/backend`
5. Replace `YOUR_USERNAME` with your actual username

---

### Step 6: Reload and Test

1. Scroll to the top of the **"Web"** tab
2. Click the big green **"Reload"** button
3. Your backend is now live at: `https://YOUR_USERNAME.pythonanywhere.com`

---

### Step 7: Test Your API

Open this URL in your browser:
```
https://YOUR_USERNAME.pythonanywhere.com/api/search?q=Sachin
```

You should see JSON data about Sachin Tendulkar! 🎉

---

## 🔗 Connect Frontend to Backend

Now update your Vercel frontend to use the PythonAnywhere backend:

1. Go to **Vercel Dashboard**
2. Click on your **cricket-legends2** project
3. Go to **Settings** → **Environment Variables**
4. Add a new variable:
   - **Name**: `VITE_API_URL`
   - **Value**: `https://YOUR_USERNAME.pythonanywhere.com/api`
5. Click **"Save"**
6. Go to **Deployments** tab
7. Click **"Redeploy"** on the latest deployment

---

## ✅ You're Done!

Your complete app is now live:
- **Frontend**: `https://cricket-legends2.vercel.app` (or your Vercel URL)
- **Backend**: `https://YOUR_USERNAME.pythonanywhere.com`

---

## 🐛 Troubleshooting

### If you see "Something went wrong" error:

1. Go to **"Web"** tab
2. Click **"Error log"** link
3. Check what the error is
4. Common fixes:
   - Make sure WSGI file has correct username
   - Make sure working directory is set correctly
   - Make sure you ran `pip3 install --user flask flask-cors`

### If database is empty:

1. Go to **"Consoles"** → **"Bash"**
2. Run:
```bash
cd cricket-legends2/backend
python3 init_db.py
```

---

## 💡 Pro Tips

1. **Free Tier Limits**:
   - Always-on (doesn't sleep!)
   - 512 MB storage
   - 100 seconds CPU time per day
   - Perfect for your project!

2. **Updating Your Code**:
   - Go to **"Consoles"** → **"Bash"**
   - Run:
   ```bash
   cd cricket-legends2
   git pull
   ```
   - Then click **"Reload"** on Web tab

3. **Custom Domain** (Optional):
   - You can add a custom domain in PythonAnywhere settings
   - Free tier supports custom domains!

---

## 🎉 Summary

**What you'll have:**
- ✅ Frontend on Vercel (FREE, unlimited)
- ✅ Backend on PythonAnywhere (FREE, always-on)
- ✅ 118 cricketers in database
- ✅ Beautiful, fast website
- ✅ $0/month cost

**Your live URLs:**
- Frontend: `https://cricket-legends2.vercel.app`
- Backend: `https://YOUR_USERNAME.pythonanywhere.com`
- API: `https://YOUR_USERNAME.pythonanywhere.com/api/search?q=Kohli`

---

**Need help? Let me know which step you're on!** 🚀
