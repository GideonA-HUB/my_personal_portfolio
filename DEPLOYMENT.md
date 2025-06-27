# Portfolio Deployment Guide

This guide will help you deploy your Django portfolio website to various platforms.

## 🚀 Quick Deploy Options

### Option 1: Railway (Recommended - Free & Easy)

1. **Create Railway Account**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Deploy from GitHub**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your portfolio repository

3. **Configure Environment Variables**
   - Go to your project settings
   - Add these environment variables:
   ```
   SECRET_KEY=your-generated-secret-key
   DEBUG=False
   ALLOWED_HOSTS=your-app-name.railway.app
   ```

4. **Deploy**
   - Railway will automatically detect Django and deploy
   - Your site will be live at `https://your-app-name.railway.app`

### Option 2: Render (Great Alternative)

1. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure Service**
   - **Name**: Your portfolio name
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate`
   - **Start Command**: `gunicorn portfolio.wsgi:application`

4. **Environment Variables**
   ```
   SECRET_KEY=your-generated-secret-key
   DEBUG=False
   ALLOWED_HOSTS=your-app-name.onrender.com
   ```

### Option 3: Heroku

1. **Install Heroku CLI**
   ```bash
   # Windows
   Download from: https://devcenter.heroku.com/articles/heroku-cli
   
   # Mac
   brew tap heroku/brew && brew install heroku
   ```

2. **Login and Create App**
   ```bash
   heroku login
   heroku create your-portfolio-name
   ```

3. **Set Environment Variables**
   ```bash
   heroku config:set SECRET_KEY=your-generated-secret-key
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
   ```

4. **Deploy**
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   heroku run python manage.py migrate
   ```

## 🔧 Pre-Deployment Checklist

### 1. Generate Secret Key
```python
# Run this in Python shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 2. Collect Static Files
```bash
python manage.py collectstatic --no-input
```

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Create Superuser (if needed)
```bash
python manage.py createsuperuser
```

## 📁 Important Files Created

- `Procfile` - Tells deployment platforms how to run your app
- `runtime.txt` - Specifies Python version
- `build_files.sh` - Build script for some platforms
- `env.example` - Example environment variables
- Updated `settings.py` - Production-ready settings
- Updated `requirements.txt` - All necessary dependencies

## 🔒 Security Notes

1. **Never commit your `.env` file** with real secrets
2. **Use environment variables** for sensitive data
3. **Generate a new SECRET_KEY** for production
4. **Set DEBUG=False** in production

## 🌐 Custom Domain (Optional)

After deployment, you can add a custom domain:

1. **Buy a domain** (Namecheap, GoDaddy, etc.)
2. **Configure DNS** to point to your deployment URL
3. **Update ALLOWED_HOSTS** with your domain
4. **Add SSL certificate** (most platforms do this automatically)

## 📊 Monitoring & Maintenance

### Check Logs
- Railway: Dashboard → Deployments → View logs
- Render: Dashboard → Your service → Logs
- Heroku: `heroku logs --tail`

### Update Your Site
1. Make changes locally
2. Test thoroughly
3. Commit and push to GitHub
4. Platform will auto-deploy (or trigger manual deploy)

## 🆘 Troubleshooting

### Common Issues:

1. **Static files not loading**
   - Run `python manage.py collectstatic`
   - Check STATIC_ROOT and STATIC_URL settings

2. **Database errors**
   - Run `python manage.py migrate`
   - Check database configuration

3. **500 errors**
   - Check logs for specific error messages
   - Verify environment variables are set correctly

4. **Media files not working**
   - Consider using cloud storage (AWS S3, Cloudinary) for production

## 🎉 Success!

Once deployed, your portfolio will be live and accessible worldwide!

### Next Steps:
1. **Test all functionality** on the live site
2. **Add your content** through the admin panel
3. **Share your portfolio** with potential employers/clients
4. **Set up monitoring** to track site performance

---

**Need help?** Check the platform's documentation or reach out to their support teams. 