# Conversion Uplift Study Reproduction
This project reproduces a conversion uplift study similar to those commonly conducted by digital advertising platforms like Meta, or Reddit.  Using randomised treatment/control set, I estimated the impact of treatment (advertising) on conversions. 

## Key Takeaways
In this experiment I hypothesised that treatment would positively impact conversions. I observed a treatment CVR of 0.32% versus the control CVR of 0.19%, representing an absolute lift of 0.13 percentage points and a relative lift of 68%. A two-proportion z-test found my hypothesis to be correct with a P-value of < 0.001. The 95% confidence interval for the absolute lift ranges from 0.097 to 0.165 percentage points. For this study, treatment resulted in 598 incremental conversions, and assuming a £55 AOV (for illustrative purposes), an incremental increase in revenue of £32,912. 

## Objectives

- Sample dataset
- Validate randomisation
- Estimate conversion lift and relative lift
- Test statistical significance using two-proportion z-test
- Calculate lower and upper confidence intervals
- Estimate incremental conversions
- Estimate incremental revenue

## Dataset

I used the Criteo Uplift Modeling dataset, found on [Kaggle](https://www.kaggle.com/datasets/arashnic/uplift-modeling/data)  
I sampled 500,000 users of the 13M total rows - using a laptop so limited RAM usage by sampling  
Treatment / Control was binary
Conversion had binary treatment

## Methods

- Random sampling
- Randomisation checks
- CVR analysis
- Absolute & Relative Lift
- Two proportion z-test
- Analytical confidence intervals

## Results

Control cvr     0.19%  
Treatment cvr   0.32%  
Absolute lift   0.13%  
Relative lift  68.58%  
Z-stat         6.2457  
P-value        0.0000  
95% CI lower   0.097%  
95% CI upper   0.165%  
