# Railway Deployment Guide

## Quick Fix for 500 Error

If you're getting a 500 error after upgrading to Railway's hobby plan, follow these steps:

### 1. Set Environment Variables

In your Railway dashboard, go to your project settings and add these environment variables:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=gideon-portfolio.up.railway.app
DATABASE_URL=your-postgresql-url-from-railway
```

**Important:** Make sure to copy the exact `DATABASE_URL` from Railway's database tab. It should look like:
`postgresql://username:password@host:port/database_name`

### 2. Database Setup

Railway provides a PostgreSQL database. Make sure to:
- Copy the `DATABASE_URL` from Railway's database tab
- Set it as an environment variable
- The build script will automatically run migrations

### 3. Cloudinary Setup (Optional)

If you want to use Cloudinary for image storage, add these variables:

```
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

### 4. Redeploy

After setting the environment variables:
1. Go to Railway dashboard
2. Click "Deploy" to trigger a new deployment
3. The build script will automatically:
   - Install dependencies
   - Collect static files
   - Run database migrations
   - Set up initial data

## Troubleshooting

### Check Logs
1. Go to Railway dashboard
2. Click on your deployment
3. Check the logs for specific error messages

### Common Issues

1. **Database Connection Error**
   - Ensure `DATABASE_URL` is set correctly
   - Check if the database is provisioned in Railway

2. **Static Files Error**
   - The build script automatically collects static files
   - Check if `STATIC_ROOT` is set correctly

3. **Missing Environment Variables**
   - Ensure all required variables are set
   - Double-check variable names and values

4. **Migration Errors**
   - The build script runs migrations automatically
   - Check logs for specific migration errors

### Manual Commands

If you need to run commands manually, you can use Railway's shell:

```bash
# Connect to Railway shell
railway shell

# Check database connection
python manage.py check_db

# Run migrations
python manage.py migrate

# Set up initial data
python manage.py setup_initial_data

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

## Environment Variables Reference

| Variable | Required | Description |
|----------|----------|-------------|
| `SECRET_KEY` | Yes | Django secret key |
| `DEBUG` | Yes | Set to `False` for production |
| `ALLOWED_HOSTS` | Yes | Your Railway domain |
| `DATABASE_URL` | Yes | PostgreSQL connection string |
| `CLOUDINARY_CLOUD_NAME` | No | Cloudinary cloud name |
| `CLOUDINARY_API_KEY` | No | Cloudinary API key |
| `CLOUDINARY_API_SECRET` | No | Cloudinary API secret |

## Support

If you're still experiencing issues:
1. Check Railway's status page
2. Review the deployment logs
3. Ensure all environment variables are set correctly
4. Try redeploying the application 