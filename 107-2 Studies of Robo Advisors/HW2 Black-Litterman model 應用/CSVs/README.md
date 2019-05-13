## CSV解說
0. 主要是ETF價格資料、Libor 3m利率，來源為網路抓取
1. 是採取固定權重，每月再平衡的Portfolio NAV，以及在此權重下，每檔ETF要買多少單位
2. 利用老師上課所給資料，計算出的每日各檔ETF call-put spread, realized-implied spread
3. 是long short所分配的權重，若某檔ETF該月無交易則以0取代，無論當月有11/10/9檔ETF交易均是此權重，此csv即BL model逐月的P
   >  [0.4, 0.3, 0.2, 0.1, 0, 0, 0, -0.1, -0.2, -0.3, -0.4]
4. 
5. 
6. 
