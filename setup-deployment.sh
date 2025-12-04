#!/bin/bash

# Cricket Legends - Quick Deployment Setup Script

echo "🏏 Cricket Legends - Deployment Setup"
echo "======================================"
echo ""

# Check if git is initialized
if [ ! -d .git ]; then
    echo "📦 Initializing Git repository..."
    git init
    git branch -M main
else
    echo "✅ Git repository already initialized"
fi

# Add all files
echo "📝 Adding files to git..."
git add .

# Commit
echo "💾 Creating commit..."
git commit -m "Prepare for deployment - Cricket Legends app with 118 cricketers"

echo ""
echo "✅ Setup complete!"
echo ""
echo "📋 Next Steps:"
echo "1. Create a new repository on GitHub: https://github.com/new"
echo "2. Run these commands with your repository URL:"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/cricket-legends.git"
echo "   git push -u origin main"
echo ""
echo "3. Follow the deployment guide in DEPLOYMENT.md"
echo ""
echo "🚀 Recommended free hosting:"
echo "   - Backend: https://render.com (FREE)"
echo "   - Frontend: https://vercel.com (FREE)"
echo ""
