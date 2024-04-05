# Mining-quality-prediction

## About
Predictive Analytics: The aim is to predict the % of Silica in the end of the process, which is the impure concentrate of iron ore in a flotation plant. 

Prescriptive Analytics: The aim is to use the model to suggest the best operating parameters of the flotation plant to minimize the % of Silica in the end of the process.

Data Reference: [Kaggle](https://www.kaggle.com/edumagalhaes/quality-prediction-in-a-mining-process)

## Tech Stack
![Tech Stack](images/tech_stack.png)

### DATA ENGINEERING
- Data Profiling: Great Expectations
- Data Versioning: DVC
- Feature Store: Feast


### DATA SCIENCE
- Data Exploration and Preprocessing: Pandas, Matplotlib, Seaborn
- Model Training: LightGBM, Optuna, SHAP
- Experiment Tracking: MLflow


### DEVOPS
- Automation and Orchestration: GitHub Actions, Kedro
- Model Monitoring: Evidently, Prometheus, Grafana
- Model Serving: FastAPI, Docker, Kubernetes