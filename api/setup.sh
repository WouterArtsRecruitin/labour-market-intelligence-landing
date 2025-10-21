#!/bin/bash

# Labour Market Intelligence API - Setup Script
# This script helps you configure the API quickly

echo "=================================================="
echo "Labour Market Intelligence API - Setup"
echo "=================================================="
echo ""

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js >= 18.0.0"
    exit 1
fi

echo "✅ Node.js version: $(node --version)"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "✅ .env file created"
else
    echo "✅ .env file already exists"
fi

echo ""
echo "=================================================="
echo "CONFIGURATION REQUIRED"
echo "=================================================="
echo ""
echo "Please edit the .env file and configure:"
echo ""
echo "1. 🔑 ANTHROPIC_API_KEY (REQUIRED)"
echo "   - Get your API key from: https://console.anthropic.com/"
echo "   - Replace 'your_anthropic_api_key_here' with your actual key"
echo ""
echo "2. 📧 EMAIL CONFIGURATION (Optional but recommended)"
echo "   - EMAIL_USER: Your email address"
echo "   - EMAIL_PASSWORD: Your email app password"
echo "   - For Gmail: Generate app password at https://myaccount.google.com/apppasswords"
echo ""
echo "3. 🌐 ALLOWED_ORIGINS (Optional)"
echo "   - Add your frontend URLs if needed"
echo ""

# Install dependencies
echo "=================================================="
echo "INSTALLING DEPENDENCIES"
echo "=================================================="
echo ""

npm install

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Dependencies installed successfully"
else
    echo ""
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "=================================================="
echo "SETUP COMPLETE!"
echo "=================================================="
echo ""
echo "Next steps:"
echo "1. Edit .env and add your ANTHROPIC_API_KEY"
echo "2. (Optional) Configure email settings in .env"
echo "3. Run: npm run dev"
echo ""
echo "The server will start on http://localhost:3002"
echo ""
echo "Test with: curl http://localhost:3002/api/status"
echo ""
