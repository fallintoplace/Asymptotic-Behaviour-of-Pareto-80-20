# Visualizing-Pareto-80-20
A quick visualization  on the asymptotic behaviour of Pareto 80-20. 2 main points: New maxima can be much larger than past maxima; Even though the mean exists, the sample mean failed to converge even for large N = 10000000 (10^7)

Pareto 80-20 has the Pareto tail index log4(5), around 1.16. This means that the mean exists (roughly 7.21), the variance is infinite, while the skewness and kurtosis are undefined. Nonetheless, the law of large number works very slowly for Pareto 80-20, and as demonstration the sample mean fails to converge for N = 10000000 (10^7).

This is the reason why the tail index is a good indicator to estimate the actual mean and variance when dealing with heavy-tailed distribution.

![Test Image 1](https://github.com/fallintoplace/Visualizing-Pareto-80-20/blob/master/samples_generated.gif)
![Test Image 2](https://github.com/fallintoplace/Visualizing-Pareto-80-20/blob/master/sample_mean.gif)
