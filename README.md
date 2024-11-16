# RMNCH_coverage_patterns
This repository has code for clustering analysis of Reproductive,  Maternal, Newborn, and Child Health (RMNCH) coverage patterns using UMAP and KMeans.

Software dependencies and operating systems (including version numbers)

Python Environment: 
Python (3·11·5) and (JupyterLab 4.2.4)

Packages: 
umap-learn (0.5.4)
scikit-learn (1.5.2)
pandas (2.2.3)
numpy (2.0.2)
matplotlib (3.9.2)
seaborn (latest)
tqdm (4.67.0)

Installation instructions: pip3 can be used to install all the packages
Typical install time: under a minute per package

Reproduction instructions:
In order to reproduce the results in the manuscript, please follow the following steps to obtain access to the datasets:
- Visit https://dhsprogram.com/, and apply for access to datasets for the following countries: 
Angola, Burkina Faso, Benin, Burundi, Dem. Rep. Congo, Cote d'Ivoire, Cameroon, Ethiopia, Gabon, Ghana, Gambia, Guinea, Kenya, Liberia, Lesotho, Madagascar, Mali, Mauritania, Malawi, Mozambique, Nigeria, Rwanda, Sierra Leone, Senegal, Chad, Togo, Tanzania, Uganda, South Africa, Zambia, Zimbabwe
- Then please run the jupyter notebook "Feature Engineering" to perform the feature engineering and then use the resulting dataset for further analysis with the UMAP and KMeans clustering notebooks.





