# Black-Litterman model應用

## Visualization
### Input
* Step1: 使用11檔ETF 2010/01~2017/12之adjusted close，以及事先設定的權重，計算各ETF每月買多少單位以及Rebalance之NAV
* 流程二
* 流程二
* 流程二
* 流程二
* 流程二

### Output
* NAV of portfolio rebalance each month
![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW2%20Black-Litterman%20model%20應用/Result%20Graph/NAV_adj_all.png)

* Rebalance buy units - Fixed weights
![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW2%20Black-Litterman%20model%20應用/Result%20Graph/Fixed_units.png)

* Rebalance buy units - Adjust with CP spread
![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW2%20Black-Litterman%20model%20應用/Result%20Graph/CP_adj_units.png)

* Rebalance buy units - Adjust with RI spread
![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW2%20Black-Litterman%20model%20應用/Result%20Graph/RI_adj_units.png)

* If the BL result weights did not adjust to a sum of 1, the Rebalanced NAV looks like:
![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW2%20Black-Litterman%20model%20應用/Result%20Graph/NAV_unadj_all.png)
