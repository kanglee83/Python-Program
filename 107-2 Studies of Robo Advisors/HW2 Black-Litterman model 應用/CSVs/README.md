## CSV解說
0. 主要是ETF價格資料、Libor 3m利率，來源為網路抓取
1. 是採取固定權重，每月再平衡的Portfolio NAV，以及在此權重下，每檔ETF要買多少單位
2. 利用老師上課所給資料，計算出的每日各檔ETF call-put spread, realized-implied spread
3. 是long short所分配的權重，若某檔ETF該月無交易則以0取代，無論當月有11/10/9檔ETF交易均是以下權重（避免權重波動過大），此csv即BL model逐月的P
   >   權重：[0.4, 0.3, 0.2, 0.1, 0, 0, 0, -0.1, -0.2, -0.3, -0.4]
4. 此為透過BL model算出之個檔ETF逐月權重，剛算出來的逐月各檔權重總和約為0.95，調整為總和1後，兩者都輸出為csv
5. 透過4之權重總和1的資料，CP/RI分別每月重分配計算NAV，各月各檔ETF買入單位數
   >   因第一筆月call-put spread, realized-implied spread都是2010/01月底，造成2010/01無前一筆資料可用來重分配，故將該月全NAV全數設為10000
6. 此為將5之逐日NAV
