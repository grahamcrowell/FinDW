# Stock Trading Strategy Backtesting

Define stock choosing algorithm(s) that 

## Input Data: Time Series

Define a stock price time series as a function with a date parameter $T$ that returns daily stock prices $x_t\in\mathbb{R}^+$ for all days up until $T$.

$$x_t:=t\to\mathbb{R}^+$$ for $M$ descrete dates $t=(t_0,t_1,\ldots,t_i,..,t_{M-1}=T)$ where $T$ is most recent/current date.

## Time Series Operators

Define lag operator (function) $L$ and parameter $\tau$
$$L^\tau(x_t)=L^\tau x_t=x_{t-\tau}$$

Define trailing summation operator (function) $S$ and parameter $\tau$
$$S^\tau(L(x_t))=S^\tau(L)x_t=\sum_{i=0}^{\tau} L^i x_t$$

### Indicator

The $\tau-$day simple moving average
$$\text{sma}^{\tau}(x_t)=\frac{S^\tau(L)x_t}{\tau}\in\mathbb{R}^{+}$$

In general, an **indicator** is a $f$ is a (parameterized) function that takes a time series and a returns a single number
$$f:=x_t\to\mathbb{R}^+$$


## Indicator Comparison Strategy

Specifiy 2 indicators $f$ and $g$ and input time series $x_t$ and define binary recommender that returns: BUY or SELL.

$$r(x_t,f,g)=\begin{cases}\text{if:  }f(x_t)<g(x_t)\text{ then BUY}\\\text{else: SELL}\end{cases}$$

## Naive Binary Bot

`inputs:`

- backtest date interval containing: $t=(t_0,t_1,\ldots,t_i,..,t_{M-1}=T)$; sequence of dates containing $M$ dates indexed by $i=(0,1,\ldots,M)$
- binary recommender $r(~\cdot~,f,g)$
- for every date $t$ in back testing interval, we need the set of available stocks: $A_t=\{a_{t,j}\}_{j=0}^{N_t-1}$; where $N_t$ is the number of assets
- for each $i$ and $j$ each stock $a_j$ has an associated stock price time series $x_t$


`initial:`

- set of all available assets $A=\{a_j\}$ and associated set of time series $X_t=\{x_{j,t}:a_j\in A\}$
- go to input

`input:`

- point in time $t\in(t_a,t_b)$
- $A$ universe of stocks
- previous day's portfolio of $N$ holdings $P_{t-1}=(a_k,w_k)_{k=0}^{N-1}$


## Source Code Organization

This is the root of our [git repo](https://git-scm.com/about).  No code here, just docs.

### FinDW/Database/ folder

`*.sql` database code

### FinDW/pyFinDW/ folder

- "main" entry point
- top level of python code base.

#### FinDW/pyFinDW/pyFin

top level of python package named: `pyFin`