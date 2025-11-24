#!/bin/bash

# Security Fix Script - Remove exposed secrets from Git history
# This script removes sensitive data from the Git repository history

echo "🔒 Security Fix: Removing exposed secrets from Git history"
echo "============================================================"
echo ""

# Create a backup first
echo "📦 Creating backup..."
cd ..
cp -r lead_gen_0ae77895 lead_gen_0ae77895_backup_$(date +%Y%m%d_%H%M%S)
cd lead_gen_0ae77895

echo "✅ Backup created"
echo ""

# Check if git-filter-repo is installed
if ! command -v git-filter-repo &> /dev/null; then
    echo "⚠️  git-filter-repo not found. Installing..."
    brew install git-filter-repo || pip3 install git-filter-repo
fi

echo "🧹 Removing sensitive data from Git history..."
echo ""

# Create a file with patterns to remove
cat > /tmp/secrets-to-remove.txt << 'EOF'
8574716516:AAEzjpntgYn3vtrmg0TNK-lV1MuE7pLY7gM
zgwk ayba taud xebq
ihortovstoles@gmail.com
EOF

# Use git filter-repo to remove the secrets
git filter-repo --replace-text /tmp/secrets-to-remove.txt --force

# Clean up
rm /tmp/secrets-to-remove.txt

echo ""
echo "✅ Git history cleaned!"
echo ""
echo "⚠️  IMPORTANT NEXT STEPS:"
echo "1. Review the changes with: git log"
echo "2. Force push to GitHub: git push origin --force --all"
echo "3. Revoke the old Telegram bot token via @BotFather"
echo "4. Create a new bot token and set it via: wrangler secret put TELEGRAM_BOT_TOKEN"
echo ""
echo "⚠️  WARNING: Force push will rewrite history on GitHub!"
echo "   Make sure no one else is working on this repository."
echo ""
