# 🚀 Quick Deployment Guide

## Fastest Way to Deploy (5 minutes)

### 1. **Push to GitHub**
```bash
# Navigate to project
cd /Users/rizwan/.gemini/antigravity/scratch/cricketer_search

# Make setup script executable
chmod +x setup-deployment.sh

# Run setup script
./setup-deployment.sh

# Create a new repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/cricket-legends.git
git push -u origin main
```

### 2. **Deploy Backend (Render - FREE)**
1. Go to [render.com](https://render.com) → Sign up with GitHub
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repo
4. Settings:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt && python init_db.py`
   - **Start Command**: `gunicorn app:app`
5. Click **"Create Web Service"**
6. **Copy your backend URL** (e.g., `https://cricket-legends-api.onrender.com`)

### 3. **Deploy Frontend (Vercel - FREE)**
1. Go to [vercel.com](https://vercel.com) → Sign up with GitHub
2. Click **"Add New..."** → **"Project"**
3. Import your GitHub repo
4. Settings:
   - **Root Directory**: `frontend`
   - **Framework**: Vite
5. Add Environment Variable:
   - **Key**: `VITE_API_URL`
   - **Value**: Your Render backend URL from step 2
6. Click **"Deploy"**

### 4. **Done! 🎉**
Your app is now live and free!

---

## Alternative: One-Click Deploy

### Backend Options:
- [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)
- [Railway](https://railway.app) - $5 free credit/month
- [Fly.io](https://fly.io) - Free tier available

### Frontend Options:
- [Vercel](https://vercel.com) - Unlimited free hosting ⭐ Recommended
- [Netlify](https://netlify.com) - Unlimited free hosting
- [Cloudflare Pages](https://pages.cloudflare.com) - Unlimited free hosting

---

## 💡 Pro Tips

1. **Keep Backend Awake**: Use [UptimeRobot](https://uptimerobot.com) to ping your Render backend every 14 minutes (prevents sleep)

2. **Custom Domain**: Both Vercel and Netlify support free custom domains

3. **Analytics**: Add Vercel Analytics (free) to track visitors

4. **Database**: SQLite works great for this read-heavy app. Database is created automatically on deployment.

---

## 📊 What You Get (FREE)

✅ **Backend**: 750 hours/month on Render  
✅ **Frontend**: Unlimited on Vercel  
✅ **SSL**: Automatic HTTPS  
✅ **CDN**: Global edge network  
✅ **Database**: SQLite with 118 cricketers  
✅ **Total Cost**: $0/month  

---

For detailed instructions, see [DEPLOYMENT.md](./DEPLOYMENT.md)
