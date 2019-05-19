# 編制Volatility Index

### Output

* 設定target volatility為7%，利用前六個月各資產(SHY,VTI,EFA,EEM,TLT,LQD,IYR)資料，在符合各資產權重上下界下，逐月隨機1000次，計算AACRV(Annualized Assets Combination Realized Volatility)以及AACR(Annualized Assets Combination Return)。紀錄AACRV小於等於target volatility之情況下最大的AACR以及該次的各資產權種組合，作為每個月rebalance之權重。

>   其中有9個月份的1000次蒙地卡羅最大期望報酬依然小於0

![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW3%20Volatility%20Index/Graphs/MonteCarlo%20output.png)

* 運用上述逐月權重，在每月第一個交易日rebalance，並扣除無風險利率（使用Federal Funds Rate）以及每年0.5%的費用率。如下圖，藍線是未扣除無風險利率以及費用率之情況，橘線則是已扣除，兩線相差不大。

![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW3%20Volatility%20Index/Graphs/Base%20index.png)

* 計算完從2003/11 ~ 2019/04之所有Base index後，取每日之前20日的Base index，逐日計算波動度（標準差）並年化。如下圖，逐日波動度全部小於一開始設定的7% target volatility，故沒有因為超過volatility cap(>target volatility)而需要在月中rebalance之事件。

![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW3%20Volatility%20Index/Graphs/Daily%20realized%20vol.png)

