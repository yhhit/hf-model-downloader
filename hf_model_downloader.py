import os
import argparse
import shutil
from huggingface_hub import hf_hub_download, snapshot_download

def download_hf_file(repo_id, filename, save_dir=None, cache_dir=None, endpoint=None, proxies=None, resume=True):
    """
    下载 Hugging Face 存储库中的单个文件，并将其保存到指定路径。

    参数:
    - repo_id: str, 模型库的路径或模型名称，例如 "bert-base-uncased"。
    - filename: str, 需要下载的文件名称，例如 "pytorch_model.bin"。
    - save_dir: str, 可选，下载文件保存的目录。如果未指定，则保存到当前目录。
    - cache_dir: str, 可选，指定缓存目录路径，默认情况下使用系统默认缓存路径。
    - endpoint: str, 可选，自定义 Hugging Face Hub 的 endpoint。
    - proxies: dict, 可选，设置代理。
    - resume: bool, 是否支持断点续传，默认为 True。

    返回:
    - str, 下载并保存的文件完整路径。
    """
    # 下载文件到缓存目录
    cached_file_path = hf_hub_download(
        repo_id=repo_id,
        filename=filename,
        resume_download=resume,
        cache_dir=cache_dir,
        endpoint=endpoint,
        proxies=proxies
    )

    # 如果指定了保存目录，将文件移动到该目录
    if save_dir:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        save_path = os.path.join(save_dir, filename)
        shutil.move(cached_file_path, save_path)
    else:
        save_path = cached_file_path

    print(f"File downloaded and saved to: {save_path}")
    return save_path

def download_hf_repository(repo_id, save_dir=None, cache_dir=None, endpoint=None, proxies=None, resume=True):
    """
    下载 Hugging Face 存储库的所有文件，并将其保存到指定路径。

    参数:
    - repo_id: str, 模型库的路径或模型名称，例如 "bert-base-uncased"。
    - save_dir: str, 可选，下载文件保存的目录。如果未指定，则保存到当前目录。
    - cache_dir: str, 可选，指定缓存目录路径，默认情况下使用系统默认缓存路径。
    - endpoint: str, 可选，自定义 Hugging Face Hub 的 endpoint。
    - proxies: dict, 可选，设置代理。
    - resume: bool, 是否支持断点续传，默认为 True。

    返回:
    - str, 下载并保存的存储库目录路径。
    """
    # 下载整个存储库
    repo_dir = snapshot_download(
        repo_id=repo_id,
        cache_dir=cache_dir,
        resume_download=resume,
        local_dir=save_dir,
        endpoint=endpoint,
        proxies=proxies
    )

    print(f"Repository downloaded and saved to: {repo_dir}")
    return repo_dir

def main():
    parser = argparse.ArgumentParser(description="Hugging Face Model Downloader")

    parser.add_argument("--repo_id", type=str, required=True, help="Model repository ID, e.g., 'bert-base-uncased'")
    parser.add_argument("--filename", type=str, help="Filename to download, e.g., 'pytorch_model.bin'. If not provided, the entire repository will be downloaded.")
    parser.add_argument("--save_dir", type=str, default=None, help="Directory to save the downloaded file(s)")
    parser.add_argument("--cache_dir", type=str, default=None, help="Directory to use as cache")
    parser.add_argument("--endpoint", type=str, default=None, help="Custom Hugging Face Hub endpoint")
    parser.add_argument("--proxies", type=str, default=None, help="Proxy settings, e.g., '{\"http\": \"http://10.10.1.10:3128\", \"https\": \"http://10.10.1.10:1080\"}'")
    parser.add_argument("--no_resume", action='store_true', help="Disable resume download feature")

    args = parser.parse_args()

    proxies = eval(args.proxies) if args.proxies else None

    if args.filename:
        download_hf_file(
            repo_id=args.repo_id,
            filename=args.filename,
            save_dir=args.save_dir,
            cache_dir=args.cache_dir,
            endpoint=args.endpoint,
            proxies=proxies,
            resume=not args.no_resume
        )
    else:
        download_hf_repository(
            repo_id=args.repo_id,
            save_dir=args.save_dir,
            cache_dir=args.cache_dir,
            endpoint=args.endpoint,
            proxies=proxies,
            resume=not args.no_resume
        )

if __name__ == "__main__":
    main()
