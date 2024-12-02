#!/bin/bash

# Node.jsの確認
if ! command -v node >/dev/null 2>&1; then
    echo "Error: Node.js is not installed"
    exit 1
fi

echo "Node.js version:"
node --version

# npmの確認
if ! command -v npm >/dev/null 2>&1; then
    echo "Error: npm is not installed"
    exit 1
fi

echo "npm version:"
npm --version

# 作業ディレクトリに移動
echo "Moving to frontend directory..."
cd WebApp/frontend || { echo "Error: Could not change to frontend directory"; exit 1; }

# 依存関係のインストール
echo "Installing dependencies..."
npm install || { echo "Error: Failed to install dependencies"; exit 1; }

# 開発サーバーの起動
echo "Starting development server..."
npm run serve 