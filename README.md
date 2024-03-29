# Visualization-of-Pareto-80-20
A quick visualization on the asymptotic behaviour of Pareto 80-20. Pareto 80-20 is a principle that can be applied to many socio-economic phenomena.

Pareto 80-20 has the Pareto tail index log4(5), around 1.16. This means that the mean exists (roughly 7.21), the variance is infinite, while the skewness and kurtosis are undefined (Similar properties hold for distributions with Pareto tail index within (1; 2) ). Nonetheless, the law of large number works very slowly for Pareto 80-20, and as demonstration the sample mean fails to converge for N = 10000000 (10^7). 

![Test Image 2](https://github.com/fallintoplace/Visualizing-Pareto-80-20/blob/master/sample_mean.gif)

Pareto 80-20 requires 10^12 more data for the sample mean to converge to the same level of error as a normal distribution.

Future maxima cannot be predicted purely based on past maxima since tail bound no longer holds.

![Test Image 1](https://github.com/fallintoplace/Visualizing-Pareto-80-20/blob/master/samples_generated.gif)

This is the reason why one cannot directly compare a Gaussian distributed variable (Traffic fatalities) to a Pareto distributed variable (Pandemic fatalities) from the samples.

More: An Introduction to Statistical Modeling of Extreme Values by Stuart Coles.
![SPF](https://github.com/fallintoplace/Asymptotic-Behaviour-of-Pareto-80-20/blob/master/single_point_forecast.jpg)
