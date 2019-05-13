# Black-Litterman model應用

## Visualization
### Input
* Step1: 使用11檔ETF 2010/01~2017/12之adjusted close，以及事先設定的權重，計算各ETF每月買多少單位以及Rebalance之NAV
* Step2: 計算CVol - PVol以及RVol - IVol
* Step3: 將逐日spread採月平均成月spread，再根據大小順序分配予有view之權重
* Step4: 以各ETF的當月前25個月均股價報酬率計算Var-Cov matrix，將Step3之結果作為P，套用Black-Litterman model，計算W-star
  >    Omega以5%代入
* Step5: 以Step4之W-star，分別在CP spread及RI spread之方法下，計算各ETF每月買多少單位以及Rebalance之NAV，與Step1之結果相對比
* Step6: 以幾何平均將NAV換成月報酬率，以算術平均將Libor_3m換成月利率，(月報酬率平均-月rf平均)/月報酬率標準差計算Sharpe Ratio

### Output
* Sharpe Ratios using date 2010/01 ~ 2017/12
  >     NAV       0.241041
  >
  >     NAV_CP    0.252825
  >
  >     NAV_RI    0.255849

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
