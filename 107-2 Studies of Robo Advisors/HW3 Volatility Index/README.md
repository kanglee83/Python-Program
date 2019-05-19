# 編制Volatility Index

### Output

* 設定target volatility為7%，利用前六個月各資產(SHY,VTI,EFA,EEM,TLT,LQD,IYR)資料，在符合各資產權重上下界下，逐月隨機1000次，計算AACRV(Annualized Assets Combination Realized Volatility)以及AACR(Annualized Assets Combination Return)。紀錄AACRV小於等於target volatility之情況下最大的AACR以及該次的各資產權種組合，作為每個月rebalance之權重。
![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW3%20Volatility%20Index/Graphs/MonteCarlo%20output.png)
