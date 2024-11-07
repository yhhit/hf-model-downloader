@echo off
SETLOCAL

REM 检查 Python 是否已安装
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python 未安装。请先安装 Python。
    pause
    EXIT /B 1
)

@REM REM 创建虚拟环境
@REM echo 正在创建虚拟环境...
@REM python -m venv venv

@REM REM 激活虚拟环境
@REM echo 正在激活虚拟环境...
@REM call venv\Scripts\activate

REM 升级 pip 并安装依赖项
echo 正在安装依赖项...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM 安装 hf-model-downloader 工具
echo 正在安装 hf-model-downloader 工具...
pip install .

echo 安装完成。要使用工具，请运行 hf-model-downloader
@REM echo 安装完成。要使用工具，请激活虚拟环境并运行 hf-model-downloader
echo 例如：
echo venv\Scripts\activate
echo hf-model-downloader --repo_id nvidia/canary-1b --save_dir ./canary-1b --endpoint https://hf-mirror.com
echo 或
echo hf-model-downloader --repo_id nvidia/canary-1b --filename README.md --save_dir ./canary-1b --endpoint https://hf-mirror.com

@REM REM 提示用户如何退出虚拟环境
@REM echo 要退出虚拟环境，请运行 deactivate。

ENDLOCAL
pause