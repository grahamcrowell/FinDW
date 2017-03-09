# Stock Trading Strategy Backtesting

Define a stock price time series as a function with a date parameter $T$ that returns daily stock prices $x_t\in\mathbb{R}^+$ for all days up until $T$.

$$x_t:=t\to\mathbb{R}^+$$ for $M$ descrete dates $t=(t_0,t_1,\ldots,t_i,..,t_M=T)$ where $T$ is most recent/current date.

Define lag operator (function) $L$ and parameter $\tau$
$$L^\tau(x_t)=L^\tau x_t=x_{t-\tau}$$

Define trailing summation operator (function) $S$ and parameter $\tau$
$$S^\tau(L(x_t))=S^\tau(L)x_t=\sum_{i=0}^{\tau} L^i x_t=x_{t-\tau}$$

The $\tau-$day simple moving average
$$\text{sma}^{\tau}(x_t)=\frac{S^\tau(L)x_t}{\tau}\in\mathbb{R}^{+}$$

In general, an indicator is a $f$ is a (parameterized) function that takes a time series and a returns a single number
$$f:=x_t\to\mathbb{R}^+$$


## Indicator Comparison Strategy

Specifiy 2 indicators $f$ and $g$ and input time series $x_t$ and define binary recommender that returns: BUY or SELL.

$$r(x_t,f,g)=\begin{cases}\text{if:  }f(x_t)<g(x_t)\text{ then BUY}\\\text{else: SELL}\end{cases}$$

## Naive Binary Bot

`input: `
- binary recommender $r(\cdot,f,g)$
- set of all available assets $A=\{a_j\}$ and their associated time series $X_t=\{x_{j,t}:a_j\in A\}$

