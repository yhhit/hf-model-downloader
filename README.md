# Hugging Face Model Downloader

这是一个命令行工具，用于从 Hugging Face 下载单个文件或整个存储库。该工具支持自定义保存目录、自定义 Hugging Face Hub 的 endpoint 以及代理设置。

## 功能

- 下载 Hugging Face 存储库中的单个文件。
- 下载整个 Hugging Face 存储库。
- 支持断点续传。
- 支持自定义保存目录、endpoint 和代理设置。

## 安装

### 一键安装

你可以使用以下步骤一键安装依赖并设置工具：

1. 克隆或下载此仓库。
2. 运行 `install.sh`（对于 Linux/macOS 用户）或 `install.bat`（对于 Windows 用户）。

#### Linux/macOS

```bash
bash install.sh
```

#### Windows

```cmd
install.bat
```

### 手动安装

如果你希望手动安装，也可以按以下步骤操作：

1. 创建虚拟环境并激活：

```bash
python3 -m venv venv
source venv/bin/activate
```

2. 安装依赖项：

```bash
pip install -r requirements.txt
```

3. 安装工具：

```bash
pip install .
```

## 使用

一旦安装完成，你可以使用以下命令从 Hugging Face 下载单个文件或整个存储库：

### 下载单个文件

```bash
hf-model-downloader --repo_id bert-base-uncased --filename pytorch_model.bin --save_dir ./my_model_files
```

### 下载整个存储库

```bash
hf-model-downloader --repo_id bert-base-uncased --save_dir ./my_model_repo
```

### 参数说明

- `--repo_id`：模型库的路径或模型名称，例如 `bert-base-uncased`。
- `--filename`：可选参数，指定要下载的文件名称。如果未指定，将下载整个存储库。
- `--save_dir`：可选参数，指定保存下载文件的目录。
- `--cache_dir`：可选参数，指定缓存目录路径。
- `--endpoint`：可选参数，自定义 Hugging Face Hub 的 endpoint。
- `--proxies`：可选参数，设置代理。
- `--no_resume`：可选参数，禁用断点续传。

## 退出虚拟环境

安装和使用完成后，你可以通过运行以下命令退出虚拟环境：

```bash
deactivate
```

## 许可

此项目使用 MIT 许可证。详情请参阅 `LICENSE` 文件。