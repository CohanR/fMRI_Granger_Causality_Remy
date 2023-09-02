
### Analysis of Correlations Between Regions of Interest (ROIs) in Resting State fMRI

# Introduction: 
In resting state fMRI, correlations between the activity of different regions of the brain can provide insights into their functional connectivity. These correlations indicate how synchronised the BOLD signals are between pairs of ROIs.

# Results:
Strong Functional Connectivity Between ROI 1 and ROI 2:
    - The correlation coefficient between ROI 1 and ROI 2 is 0.901. This indicates a strong positive functional connectivity between these two regions during the resting state. 
      Such a high correlation suggests that these regions may be part of the same functional network or might be involved in related cognitive or physiological processes.

Weak Functional Connectivity Between ROI 1 and ROI 3, and Between ROI 2 and ROI 3:
    - The correlation coefficients between ROI 1 and ROI 3, and between ROI 2 and ROI 3 are 0.152 and 0.137, respectively. These low values indicate weak functional connectivity 
      between these pairs of regions during the resting state. This implies that while there is some level of communication or coordination between these regions, they might not be as tightly integrated in their activity as ROI 1 and ROI 2 are.


As you know, causation and corelation are vastly different. While two regions might be highly correlated, it doesn't mean one region's activity causes the other's. To infer causation, methods such as Granger causality or dynamic causal modeling would be required.

In this code I used Granger causation with the following two Granger's principle assumptions :

# The cause happens prior to its effect.
# The cause has unique information about the future values of its effect. (source: wikipedia) 

# The output of the Granger Causality Analysis of these three ROIs:
The Granger causality test essentially checks whether past values of one time series provide any information about the future values of another time series. Let's break down the results you provided:

### ROI 2 Granger-causing ROI 1:
For all lags (1 through 5), the p-values are much larger than typical significance levels (e.g., 0.05 or 0.01). This means that there's no statistical evidence to suggest that ROI 2 Granger-causes ROI 1.

### ROI 3 Granger-causing ROI 1:
- For lag 1, the p-value is large, indicating no significant Granger causality.
- For lags 2 through 5, all tests give p-values of 0.0000. This is highly significant and indicates that ROI 3 does Granger-cause ROI 1, especially with these lags.

### ROI 1 Granger-causing ROI 2:
For all lags (1 through 5), the p-values are again large, indicating no evidence that ROI 1 Granger-causes ROI 2.

### ROI 3 Granger-causing ROI 2:
- For lag 1, the p-value is relatively large, suggesting no significant Granger causality.
- For lags 2 through 5, all tests give p-values of 0.0000, indicating a significant Granger causality from ROI 3 to ROI 2.

### ROI 1 Granger-causing ROI 3:
The part you provided shows that for lag 1, there's no significant evidence of Granger causality (based on the p-value). The remaining lags are not fully presented, but given the trend in the values, it appears that there might not be significant evidence for those lags either.

### What does it all mean:
- ROI 2: does not seem to influence ROI 1 or ROI 2 in a way that's detectable via Granger causality.
  
## - ROI 3:  seems to have a significant influence on both ROI 1 and ROI 2, especially at lags 2 through 5. In Granger causality "lags" refer to previous time points. i.e.,  activity in Region A at time point t and activity in Region B at time point 
t are compared.

- ROI 1: does not seem to have a significant influence on ROI 2 or ROI 3 at the given lags.

 ### This suggests that ROI 3 might be sending information or driving activity in both ROI 1 and ROI 2, but the reverse isn't true. ROI 1 and ROI 2, based on this analysis, don't seem to be driving activity in any of the other regions over the lags tested. 

*Note: the Granger causality test doesn't prove actual causation but rather a predictive relationship. In other words, ROI 3 provides information that could help predict future values of ROI 1 and ROI 2, but it doesn't necessarily mean ROI 3 is causing changes in those regions.

