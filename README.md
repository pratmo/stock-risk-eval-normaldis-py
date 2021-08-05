## stock-risk-eval-normaldis-py

We use daily resturns of stocks in BSE (Bombay Stock Exchange) from BSE website (www.bseindia.com) to understand the risks and returns associated with two stocks- BEML and GLAXO, so that a future investor could use this data to make a better business decisions.

The dataset contains daily open and close price along with daily high and low prices, total trade quality, and turnover (in lakhs). We then explore the close price and do the daily returns calculation based on the previous day closing price. We get the gain using pct_change Pandas method then plot the gain vs density plot and calculate the normal distribution on that density curve.

The below questions are answered to help the investor make his decision:
1. What is the expected daily rate of return of these two stocks?
2. Which stocks have higher risk or volatility as far as daily returns are concerned?
3. Which stock has higher probablity of making a daily return of 2% or more?
4. Which stock has higher probablity of making a loss (risk) of 2% or more?

We only use the concepts of normal distribution and descriptive statistics to achieve this task (no ML model). The idea is to understand the working of probability and normal distribution in a real world example.

Tool: Exported .py from Jupyter Notebook (conda 4.9.2)

System: Linux (Ubuntu) 20.04.01 Focal Fossa
