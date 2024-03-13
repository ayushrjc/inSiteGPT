# inSiteGPT Project using Bert and OpenAI

## Workflow

- constants
- components
- pipeline
- main

## Create project folder

```bash
git init
```
```bash
git remote -v 
```
(to check if any git repository connected)

## Connect to git repository
```bash
git remote add origin https://github.com/ayushrjc/inSiteGPT.git
```
```bash
git pull origin main
```
## To push the changes
```bash
git add .
```
```bash
git commit -m "project structure updated"
```
```bash
git branch -M main
```
```bash
git push origin main
```

## Create environment

```bash
conda create -p venv python -y
```
```bash
source activate ./venv
```
OR 
```bash
conda activate ./venv
```

## Install Requirements
```bash
pip install -r requirements.txt
```

## To run ingest part of the code
### Elasticsearch application should be running
```bash
python main.py --ingest
```

## To run Streamlit app
```bash
streamlit run main.py
```