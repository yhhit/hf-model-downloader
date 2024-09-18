from setuptools import setup, find_packages

setup(
    name="hf-model-downloader",
    version="0.1",
    py_modules=['hf_model_downloader'],  # 指定单一模块
    entry_points={
        'console_scripts': [
            'hf-model-downloader=hf_model_downloader:main',
        ],
    },
    install_requires=[
        "huggingface_hub>=0.11.0",
    ],
    author="yhhit",
    author_email="827077539@qq.com",
    description="A tool for downloading files or entire repositories from Hugging Face with support for resuming downloads.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yhhit/hf-model-downloader",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
