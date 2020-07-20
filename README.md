# Visualization-of-Pareto-80-20
A quick visualization on the asymptotic behaviour of Pareto 80-20. Pareto 80-20 is a principle that can be applied to many socio-economic phenomena. More: https://python.quantecon.org/heavy_tails.html

Pareto 80-20 has the Pareto tail index log4(5), around 1.16. This means that the mean exists (roughly 7.21), the variance is infinite, while the skewness and kurtosis are undefined. Nonetheless, the law of large number works very slowly for Pareto 80-20, and as demonstration the sample mean fails to converge for N = 10000000 (10^7). Similar properties hold for distributions with Pareto tail index within (1; 2).

![Test Image 2](https://github.com/fallintoplace/Visualizing-Pareto-80-20/blob/master/sample_mean.gif)

Future maxima cannot be predicted based on past maxima since Chernoff bound no longer holds.

![Test Image 1](https://github.com/fallintoplace/Visualizing-Pareto-80-20/blob/master/samples_generated.gif)

This is the reason why one cannot directly compare a Gaussianly distributed variable (Traffic fatalities) to a Pareto distributed variable (Pandemic fatalities) from the samples.
