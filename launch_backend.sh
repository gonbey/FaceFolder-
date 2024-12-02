#!/bin/bash

# Pythonパスの設定
PYTHON_PATHS=(
    "/c/Users/$USER/AppData/Local/Programs/Python/Python39/python.exe"
    "/c/Users/$USER/AppData/Local/Programs/Python/Python310/python.exe"
    "/c/Users/$USER/AppData/Local/Programs/Python/Python311/python.exe"
    "/c/Python39/python.exe"
    "/c/Python310/python.exe"
    "/c/Python311/python.exe"
    "python"
)

PYTHON_CMD=""
for path in "${PYTHON_PATHS[@]}"; do
    if command -v "$path" >/dev/null 2>&1 || [ -f "$path" ]; then
        PYTHON_CMD="$path"
        break
    fi
done

if [ -z "$PYTHON_CMD" ]; then
    echo "Error: Python not found. Please install Python 3.9 or later"
    exit 1
fi

echo "Using Python: $PYTHON_CMD"
"$PYTHON_CMD" --version

# 作業ディレクトリに移動
echo "Moving to backend directory..."
cd WebApp/backend || { echo "Error: Could not change to backend directory"; exit 1; }

# 仮想環境が存在しない場合のみ作成
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    "$PYTHON_CMD" -m venv venv || { echo "Error: Failed to create virtual environment"; exit 1; }
    echo "Virtual environment created successfully"
fi

# Git Bash用のactivateスクリプトを使用
ACTIVATE_SCRIPT="venv/Scripts/activate"
if [ -f "$ACTIVATE_SCRIPT" ]; then
    echo "Activating virtual environment..."
    source "$ACTIVATE_SCRIPT" || { echo "Error: Failed to activate virtual environment"; exit 1; }
    echo "Virtual environment activated successfully"
else
    echo "Error: Virtual environment activation script not found at: $ACTIVATE_SCRIPT"
    echo "Current directory: $(pwd)"
    echo "Contents of venv/Scripts:"
    ls -la venv/Scripts || echo "Scripts directory not found"
    exit 1
fi

# 依存関係のインストールと実行
echo "Installing dependencies..."
pip install -r requirements.txt || { echo "Error: Failed to install dependencies"; exit 1; }
echo "Starting backend server..."
python app.py 