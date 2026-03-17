# Migration Instructions for Neon Database on Vercel

## Current Status
- Migration files exist for the `tasks` app
- Authentication app has no models (no migrations needed)
- DATABASE_URL is configured to use Neon when available

## To Run Migration on Vercel

### Option 1: Through Vercel Dashboard (Recommended)
1. Go to your Vercel dashboard: https://vercel.com/dashboard
2. Find your task-manager-back project
3. Click on the project
4. Click "Redeploy" or trigger a new deployment
5. The migration will run automatically during the build process

### Option 2: Using Vercel CLI (after login)
1. Login to Vercel:
   ```
   vercel login
   ```
2. Trigger deployment:
   ```
   vercel --prod
   ```

### Option 3: Git Push (if connected to Git)
1. Make a small change to any file
2. Commit and push to trigger deployment
3. Migration will run automatically

## What Happens During Deployment
The `vercel.json` file contains:
```json
{
  "buildCommand": "python migrate.py && python manage.py collectstatic --noinput"
}
```

This means:
1. `python migrate.py` runs Django migrations
2. Tables are created in your Neon database
3. Static files are collected

## Environment Variables
Make sure your Vercel project has:
- `DATABASE_URL` - Your Neon database connection string
- `SECRET_KEY` - Django secret key
- `DEBUG` - Set to False for production
- `ALLOWED_HOSTS` - Your Vercel domain

## Verification
After deployment, you can check if tables were created by:
1. Checking your Neon database dashboard
2. Testing API endpoints that require database access
