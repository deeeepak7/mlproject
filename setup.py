from setuptools import find_packages, setup

setup(
    name="mlproject",
    version="0.0.1",
    author="deepak",
    author_email="deepakreturns7@gmail.com",
    description="Machine Learning Student Performance Prediction",
    packages=find_packages(),
    install_requires=[
        "Flask==2.3.3",
        "pandas==2.0.3",
        "numpy==1.24.3",
        "scikit-learn==1.3.0",
        "catboost==1.2",
        "xgboost==1.7.6",
        "Werkzeug==2.3.7",
        "Jinja2==3.1.2",
        "MarkupSafe==2.1.3",
        "itsdangerous==2.1.2",
        "click==8.1.7",
        "gunicorn==21.2.0",
        "setuptools>=58.0.0",
        "wheel",
        "matplotlib",
        "seaborn"
    ],
    python_requires=">=3.8",
)