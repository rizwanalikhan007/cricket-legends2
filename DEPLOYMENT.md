# 🚀 Free Deployment Guide - Cricket Legends

This guide will help you deploy your Cricket Legends application for **FREE** using popular hosting platforms.

## 📋 Overview

We'll deploy:
- **Frontend (React)** → Vercel or Netlify (FREE)
- **Backend (Flask + SQLite)** → Render (FREE)

---

## 🎯 Option 1: Recommended Deployment (Render + Vercel)

### **Step 1: Deploy Backend on Render**

Render offers free hosting for web services with 750 hours/month.

#### 1.1 Create a Render Account
1. Go to [render.com](https://render.com)
2. Sign up with GitHub (recommended)

#### 1.2 Create a New Web Service
1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository (or use manual deployment)
3. Configure the service:
   - **Name**: `cricket-legends-api`
   - **Region**: Choose closest to you
   - **Branch**: `main` (or your branch name)
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && python init_db.py`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: `Free`

#### 1.3 Add Environment Variables (Optional)
- Click **"Advanced"**
- Add any environment variables if needed

#### 1.4 Deploy
1. Click **"Create Web Service"**
2. Wait for deployment (5-10 minutes)
3. Copy your backend URL (e.g., `https://cricket-legends-api.onrender.com`)

**Important Notes:**
- Free tier sleeps after 15 minutes of inactivity
- First request after sleep takes ~30 seconds to wake up
- 750 hours/month free (enough for most use cases)

---

### **Step 2: Deploy Frontend on Vercel**

Vercel offers unlimited free hosting for frontend applications.

#### 2.1 Prepare Frontend
1. Update `.env.production` file with your Render backend URL:
   ```
   VITE_API_URL=https://cricket-legends-api.onrender.com
   ```

#### 2.2 Create a Vercel Account
1. Go to [vercel.com](https://vercel.com)
2. Sign up with GitHub (recommended)

#### 2.3 Deploy
1. Click **"Add New..."** → **"Project"**
2. Import your GitHub repository
3. Configure:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
   - **Install Command**: `npm install`

#### 2.4 Add Environment Variable
1. Go to **Settings** → **Environment Variables**
2. Add:
   - **Key**: `VITE_API_URL`
   - **Value**: `https://cricket-legends-api.onrender.com` (your Render URL)
   - **Environment**: Production

#### 2.5 Deploy
1. Click **"Deploy"**
2. Wait for deployment (2-3 minutes)
3. Your site will be live at `https://your-project.vercel.app`

---

## 🎯 Option 2: Alternative - Netlify + Render

### **Step 1: Deploy Backend on Render**
(Same as Option 1 - Step 1)

### **Step 2: Deploy Frontend on Netlify**

#### 2.1 Create a Netlify Account
1. Go to [netlify.com](https://netlify.com)
2. Sign up with GitHub

#### 2.2 Deploy
1. Click **"Add new site"** → **"Import an existing project"**
2. Connect to GitHub and select your repository
3. Configure:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `frontend/dist`

#### 2.3 Add Environment Variable
1. Go to **Site settings** → **Environment variables**
2. Add:
   - **Key**: `VITE_API_URL`
   - **Value**: `https://cricket-legends-api.onrender.com`

#### 2.4 Redeploy
1. Go to **Deploys** → **Trigger deploy**
2. Your site will be live at `https://your-site.netlify.app`

---

## 🎯 Option 3: Railway (Backend Alternative)

Railway offers $5 free credit per month (enough for small projects).

### Deploy Backend on Railway

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. Select your repository
5. Configure:
   - **Root Directory**: `backend`
   - **Start Command**: `gunicorn app:app`
6. Railway will auto-detect Python and install dependencies
7. Click on your service → **Settings** → **Generate Domain**
8. Copy the domain URL

---

## 📝 Quick Setup Checklist

### Before Deployment:

- [ ] Create a GitHub repository for your project
- [ ] Push your code to GitHub:
  ```bash
  cd /Users/rizwan/.gemini/antigravity/scratch/cricketer_search
  git init
  git add .
  git commit -m "Initial commit - Cricket Legends app"
  git branch -M main
  git remote add origin https://github.com/YOUR_USERNAME/cricket-legends.git
  git push -u origin main
  ```

### Backend Deployment:

- [ ] Sign up for Render/Railway
- [ ] Create new web service
- [ ] Set root directory to `backend`
- [ ] Set build command: `pip install -r requirements.txt && python init_db.py`
- [ ] Set start command: `gunicorn app:app`
- [ ] Deploy and copy the URL

### Frontend Deployment:

- [ ] Update `.env.production` with backend URL
- [ ] Sign up for Vercel/Netlify
- [ ] Import GitHub repository
- [ ] Set root directory to `frontend`
- [ ] Add environment variable `VITE_API_URL`
- [ ] Deploy

---

## 🔧 Troubleshooting

### Backend Issues:

**Problem**: Database not initialized
- **Solution**: Make sure build command includes `python init_db.py`

**Problem**: CORS errors
- **Solution**: Backend already has CORS enabled. If issues persist, check the backend URL in frontend env variables

**Problem**: Service sleeps (Render free tier)
- **Solution**: First request will be slow (~30s). Consider using a cron job to ping your service every 14 minutes

### Frontend Issues:

**Problem**: API calls failing
- **Solution**: Check that `VITE_API_URL` environment variable is set correctly in Vercel/Netlify

**Problem**: Build fails
- **Solution**: Make sure Node version is compatible. Add `engines` field to `package.json`:
  ```json
  "engines": {
    "node": "18.x"
  }
  ```

---

## 💰 Cost Breakdown

### Completely FREE Options:

| Service | Free Tier | Limitations |
|---------|-----------|-------------|
| **Render** | 750 hrs/month | Sleeps after 15 min inactivity |
| **Vercel** | Unlimited | 100GB bandwidth/month |
| **Netlify** | Unlimited | 100GB bandwidth/month |
| **Railway** | $5 credit/month | ~500 hours |

### Recommended Combination:
- ✅ **Backend**: Render (FREE)
- ✅ **Frontend**: Vercel (FREE)
- ✅ **Total Cost**: $0/month

---

## 🚀 Custom Domain (Optional)

### Vercel:
1. Go to **Settings** → **Domains**
2. Add your custom domain
3. Update DNS records as instructed

### Netlify:
1. Go to **Domain settings**
2. Add custom domain
3. Update DNS records

### Free Domain Options:
- [Freenom](https://www.freenom.com) - Free .tk, .ml, .ga domains
- [InfinityFree](https://infinityfree.net) - Free subdomain

---

## 📊 Performance Tips

1. **Backend Wake-up**: On Render free tier, first request takes ~30s. Consider:
   - Using a service like [UptimeRobot](https://uptimerobot.com) to ping every 14 minutes
   - Showing a loading message on frontend

2. **Database**: SQLite works fine for read-heavy apps like this. For production with many writes, consider:
   - PostgreSQL on Render (free tier available)
   - Supabase (free tier with PostgreSQL)

3. **CDN**: Vercel/Netlify automatically use CDN for fast global access

---

## 🎉 Next Steps

After deployment:
1. Test all functionality on the live site
2. Share your live URL!
3. Monitor usage in Render/Vercel dashboards
4. Set up custom domain (optional)
5. Add analytics (Google Analytics, Vercel Analytics)

---

## 📞 Support

If you encounter issues:
- **Render**: [render.com/docs](https://render.com/docs)
- **Vercel**: [vercel.com/docs](https://vercel.com/docs)
- **Netlify**: [docs.netlify.com](https://docs.netlify.com)

---

## 🎊 You're Done!

Your Cricket Legends app is now live and accessible worldwide for FREE! 🏏

Example URLs:
- Frontend: `https://cricket-legends.vercel.app`
- Backend: `https://cricket-legends-api.onrender.com`
