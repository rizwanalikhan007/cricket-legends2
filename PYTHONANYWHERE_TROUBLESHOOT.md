# 🔧 Troubleshooting PythonAnywhere Backend

## ❌ Error: "Something went wrong"

This means there's an issue with the backend configuration. Let's fix it!

---

## 🛠️ **Fix Steps:**

### **Step 1: Check Error Logs**

1. Go to your PythonAnywhere **"Web"** tab
2. Scroll down to find **"Log files"** section
3. Click on **"Error log"** (red link)
4. Look at the latest errors

**Common errors and fixes:**

---

### **Error 1: "No module named 'app'"**

**Fix:** Update your WSGI file

1. Go to **"Web"** tab
2. Click on the **WSGI configuration file** link
3. Make sure it looks EXACTLY like this:

```python
import sys
import os

# Add your project directory to sys.path
project_home = '/home/rizwan786/cricket-legends2/backend'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set working directory
os.chdir(project_home)

# Import Flask app
from app import app as application
```

4. Click **"Save"**
5. Go back to **"Web"** tab and click **"Reload"**

---

### **Error 2: "No module named 'flask'"**

**Fix:** Install dependencies

1. Go to **"Consoles"** tab
2. Click **"Bash"**
3. Run these commands:

```bash
cd cricket-legends2/backend
pip3 install --user flask flask-cors
python3 init_db.py
```

4. Go back to **"Web"** tab and click **"Reload"**

---

### **Error 3: Database not found**

**Fix:** Initialize database

1. Go to **"Consoles"** tab → **"Bash"**
2. Run:

```bash
cd cricket-legends2/backend
python3 init_db.py
ls -la cricketers.db
```

You should see the database file listed.

3. Go to **"Web"** tab and click **"Reload"**

---

### **Error 4: Working directory not set**

**Fix:** Set the working directory

1. Go to **"Web"** tab
2. Scroll to **"Code"** section
3. Find **"Working directory"**
4. Set it to: `/home/rizwan786/cricket-legends2/backend`
5. Click **"Reload"**

---

## ✅ **Complete WSGI Configuration**

Here's the complete, tested WSGI configuration:

```python
import sys
import os

# Path to your project
project_home = '/home/rizwan786/cricket-legends2/backend'

# Add to Python path
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Change to project directory
os.chdir(project_home)

# Import the Flask app
from app import app as application

# Configure for production
application.config['DEBUG'] = False
```

---

## 🧪 **Test Your Backend**

After fixing, test these URLs:

1. **Homepage**: https://rizwan786.pythonanywhere.com/
2. **API Test**: https://rizwan786.pythonanywhere.com/api/search?q=Sachin

You should see JSON data for Sachin Tendulkar!

---

## 📋 **Quick Checklist:**

- [ ] WSGI file is configured correctly with username `rizwan786`
- [ ] Working directory is set to `/home/rizwan786/cricket-legends2/backend`
- [ ] Flask and flask-cors are installed
- [ ] Database is initialized (cricketers.db exists)
- [ ] Clicked "Reload" button on Web tab

---

## 🆘 **Still Not Working?**

Share the error from the **Error log** and I'll help you fix it!

To get the error:
1. **"Web"** tab → **"Log files"** section
2. Click **"Error log"**
3. Copy the last few lines
4. Share them with me

---

**Let me know what error you see in the logs!** 🔍
