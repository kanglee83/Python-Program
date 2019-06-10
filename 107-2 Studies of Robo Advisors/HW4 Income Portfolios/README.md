# Income Portfolios

### Output

* 使用基金EEM, EFA, IYR, LQD, VTI從2003/04/14到2019/04/30的資料，分別使用最早6個月、1年、2年資料來做出蒙地卡羅資產報酬/標準差點狀散布圖（效率前緣），將標準差均分為10等分取出各等分標準差下最大報酬率所隱含的資產投資權重共十個。
>     蒙地卡羅隨機納入高次方(10次)算法    

* 各自接續下去直到2009/03/09，逐日展開投資，在5%及7%配息率之下，每月初固定配息（考量通貨膨脹率），記錄下各日開始十年後的資產價格，整理並計算各統計值。
>     通貨膨脹率使用美國核心CPI指數換算成yoy (https://fred.stlouisfed.org/series/CPILFESL)

* Core CPI ＆ 五檔ETF

![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW4%20Income%20Portfolios/Inputs/CPI.png)
![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW4%20Income%20Portfolios/Inputs/ETFs.png)

* 5%配息使用前6個月資料畫效率前緣

![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW4%20Income%20Portfolios/Scatter_graph/five_percent_six_months_IP_MC.png)
![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW4%20Income%20Portfolios/Result_form/five_percent_six_months_IP.png)

* 5%配息使用前1年資料畫效率前緣

![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW4%20Income%20Portfolios/Scatter_graph/five_percent_one_year_IP_MC.png)
![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW4%20Income%20Portfolios/Result_form/five_percent_one_year_IP.png)

* 5%配息使用前2年資料畫效率前緣

![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW4%20Income%20Portfolios/Scatter_graph/five_percent_two_years_IP_MC.png)
![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW4%20Income%20Portfolios/Result_form/five_percent_two_years_IP.png)

* 7%配息使用前6個月資料畫效率前緣

![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW4%20Income%20Portfolios/Scatter_graph/seven_percent_six_months_IP_MC.png)
![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW4%20Income%20Portfolios/Result_form/seven_percent_six_months_IP.png)

* 7%配息使用前1年資料畫效率前緣

![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW4%20Income%20Portfolios/Scatter_graph/seven_percent_one_year_IP_MC.png)
![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW4%20Income%20Portfolios/Result_form/seven_percent_one_year_IP.png)

* 7%配息使用前2年資料畫效率前緣

![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW4%20Income%20Portfolios/Scatter_graph/seven_percent_two_years_IP_MC.png)
![image](https://github.com/kanglee83/Python-Program/blob/master/107-2%20Studies%20of%20Robo%20Advisors/HW4%20Income%20Portfolios/Result_form/seven_percent_two_years_IP.png)

