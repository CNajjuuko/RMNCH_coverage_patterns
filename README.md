# RMNCH_utilization_patterns
This repository has code for latent class analysis of Reproductive,  Maternal, Newborn, and Child Health services using multilevel latent class analyis.

Software dependencies and operating systems (including version numbers)

1) R Environment:
R version 4.3.1 (2023-06-16)

Packages and Libraries:
dplyr (1.1.4)
tidyverse (2.0.0)
multilevLCA (2.0.1)
survey (4.4.2)
svrepmisc (0.2.2)
knitr (1.43)
healthequal (1.0.1)

install.packages() can be used to install these packages
Typical install time: under a minute per package


2) Python Environment: 
Python (3·11·5) and (JupyterLab 4.2.4)

Packages: 
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
Angola, Burkina Faso, Benin, Burundi, Dem. Rep. Congo, Cote d'Ivoire, Cameroon, Ethiopia, Gabon, Ghana, Gambia, Guinea, Kenya, Liberia, Lesotho, Madagascar, Mali, Mauritania, Malawi, Mozambique, Nigeria, Rwanda, Sierra Leone, Senegal, Chad, Togo, Tanzania, Uganda, South Africa, Zambia, Zimbabwe between 2014 and 2024
- Then please run the jupyter notebook "Data Fetching.ipynb" to fetch each countries birth recode file and merge them, followed by "Feature Engineering.ipynb" to perform the feature engineering and then the "Data Preprocessing.ipynb" to perform the feature imputation and obtain descriptive statistics, and then use the resulting dataset for analysis using the "multiLevelLCA.Rmd" and then followed by the "Visualizations.ipynb" file to plot the visualizations.





