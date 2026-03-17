#!/usr/bin/env python
"""
Script to trigger Vercel redeployment to run migrations on Neon database
"""
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"{description} completed successfully")
        if result.stdout:
            print(f"Output: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{description} failed")
        print(f"Error: {e.stderr}")
        return False

def main():
    print("Triggering Vercel deployment to run migrations on Neon database...")
    
    # Check if Vercel CLI is installed
    if not run_command("vercel --version", "Checking Vercel CLI"):
        print("Vercel CLI not found. Please install it with: npm i -g vercel")
        sys.exit(1)
    
    # Trigger deployment
    if run_command("vercel --prod --yes", "Deploying to production"):
        print("\nDeployment triggered successfully!")
        print("The migration will run automatically during the build process.")
        print("Tables will be created in your Neon database on Vercel.")
    else:
        print("\nDeployment failed. Please check your Vercel configuration.")
        sys.exit(1)

if __name__ == "__main__":
    main()
