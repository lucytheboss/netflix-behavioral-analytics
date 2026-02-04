# Netflix Behavioral Analytics Lab

Behavior-first analysis of streaming decisions: what signals predict bingeing, completion, and early drop-off?

## Project Questions
- What content + behavioral signals predict completion vs early abandonment?
- What patterns characterize binge sessions and fatigue?
- What viewer segments exist, and what interventions could improve retention?

## Repo Structure
- `notebooks/` step-by-step analysis
- `src/` reusable code for loading, features, modeling
- `reports/` stakeholder-style writeup + figures
- `docs/` definitions + methodology

## Notebooks
1. `01_data_audit.ipynb` – data audit + behavioral label definitions  
2. `02_content_eda.ipynb` – catalog trends  
3. `03_behavior_features.ipynb` – build retention/binge metrics  
4. `04_behavior_eda.ipynb` – drop-off curves, cohorts  
5. `05_modeling.ipynb` – predict behavior outcomes  
6. `06_segmentation.ipynb` – viewer clusters  
7. `07_simulation.ipynb` – product intervention simulation  

## Outputs
- `reports/analysis_report.md`
- (optional) Tableau dashboard in `dashboards/tableau/`
# netflix-behavioral-analytics
