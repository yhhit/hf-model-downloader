#!/bin/bash

# 检查 Python 是否已安装
if ! command -v python3 &>/dev/null; then
    echo "Python3 未安装。请先安装 Python3。"
    exit 1
fi

# # 创建虚拟环境（可选）
# echo "创建虚拟环境..."
# python3 -m venv venv

# # 激活虚拟环境
# source venv/bin/activate

# 安装依赖项
echo "安装依赖项..."
pip install --upgrade pip
pip install -r requirements.txt

# 安装 hf-model-downloader 工具
echo "安装 hf-model-downloader 工具..."
pip install .

echo "安装完成。要使用工具，请运行 hf-model-downloader"
# echo "安装完成。要使用工具，请激活虚拟环境并运行 hf-model-downloader"
echo "例如："
echo "source venv/bin/activate"
echo "hf-model-downloader --repo_id nvidia/canary-1b --filename README.md --save_dir ./canary-1b --endpoint https://hf-mirror.com"
echo "或"
echo "hf-model-downloader --repo_id nvidia/canary-1b --save_dir ./canary-1b --endpoint https://hf-mirror.com"

# # 提示用户如何退出虚拟环境
# echo "要退出虚拟环境，请运行 'deactivate'。"