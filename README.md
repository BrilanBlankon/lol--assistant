# LOL assistant

## 動機
打LOL時，有時想查詢有關英雄的相關資訊，但是若沒有雙螢幕或兩台以上電腦，要看資訊就只能切換螢幕，不太方便，因此想藉由這次期末專題的機會，建立一個聊天機器人來協助查詢資訊。

## 架構
使用者先輸入要查詢的英雄名稱(目前僅限中文名稱)，接著選擇要使用的功能（核心裝備、符文配置、技能點法、背景故事）即可獲取內容，也可以輸入exit或離開來重新選擇英雄。

## 環境
* window 10 64bit
* python 3.7.2

## 重點技術

* Beautifulsoup4
	* 解析request到的內容，用於爬取英雄頭像與背景故事
* Selenium
	* 自動化網頁控制，雖然速度較慢，但是對於不好用bs4解析的內容有奇效，用於爬取核心裝備、符文配置與技能點法
	
## 使用教學
* 關於pygraphviz安裝
	1. 安裝graphviz
	`pip install graph`
	2. 將bin資料夾加入環境路徑
	3. 依照作業系統版本與python版本下載對應的whl檔 [傳送門](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygraphviz "傳送門")
	4. 到工作路徑中安裝剛下載好的whl檔
	`pip install pygraphviz-1.6-cp37-cp37m-win_amd64.whl`
**參考連結**
[[Python]Windows下安装Graphviz和pygraphviz的方法](https://blog.csdn.net/u013250416/article/details/72790754 "[Python]Windows下安装Graphviz和pygraphviz的方法")

* 關於Selenium安裝
	1. 安裝Selenium
	`pip install selenium`
	2. 根據目前使用的瀏覽器版本，選擇對應的webdriver(僅支援firefox與google chrome)
		* [firefox geckodriver](https://github.com/mozilla/geckodriver/releases "firefox geckodriver")
		* [google chromedriver](https://chromedriver.chromium.org/downloads "google chromedriver")
	3. 將剛安裝好的執行檔加入環境路徑或是在執行時指定執行檔路徑
**參考連結**
[python網路爬蟲教學-Selenium基本操作](https://freelancerlife.info/zh/blog/python%E7%B6%B2%E8%B7%AF%E7%88%AC%E8%9F%B2%E6%95%99%E5%AD%B8-selenium%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C/ "python網路爬蟲教學-Selenium基本操作")

* 關於line chatbot 上傳本地圖片
	* 由於傳送圖片給使用者會需要圖片連結，我使用的是上傳到imgur，方法應該還有很多，僅供參考。以下連結講解的很詳細，步驟也比較繁瑣，因此在此就不再贅述。
	**參考連結**
	* [Imgur API：upload, load 上傳、讀取 心得筆記](https://letswrite.tw/imgur-api-upload-load/ "Imgur API：upload, load 上傳、讀取 心得筆記")
	* [在python中使用imgur](https://ithelp.ithome.com.tw/questions/10193987 "在python中使用imgur")

* 關於.env設定
	* Line
		* LINE_CHANNEL_SECRET
		* LINE_CHANNEL_ACCESS_TOKEN
	* Imgur
		* Client_ID
	* 小提醒：如果使用pipenv協助開發，記得每次更新.env後，要重新啟動shell，才會將變更後的環境變數讀入

* 啟動http server
	* `python app.py`

* 在本地端測試
	* 使用ngrok [載點](https://ngrok.com/download "載點")
	* 載好後輸入以下指令，將本地端指定的PORT掛接到外網
	`ngrok http {PORT}`

## 使用教學

* 基本操作
	* 英雄名稱目前僅支援中文，不含玩家常用暱稱
		* 納瑟斯(o)，狗頭(x)
	* 若輸入的指令不符合目前指定的輸入，系統會提示

* 整體架構
	1. 輸入欲查詢的英雄名稱
	2. 選擇要使用的功能：
		* 查詢核心裝備 -> 輸入`核心裝備`或`1`
		* 查詢推薦符文 -> 輸入`符文點法`或`2`
		* 查詢推薦技能點法 -> 輸入`技能點法`或`3`
		* 閱讀傳記故事 -> 輸入`傳記故事`或`4`
		* 重新選擇英雄 -> 輸入`離開`或`exit`
	3. 資訊呈現後回到step 1

## 使用範例

### 剛加入好友
![](https://imgur.com/HRjSWvu.jpg)

### 輸入欲查詢的英雄名稱
![](https://imgur.com/IqiRV0S.jpg)

### 查詢核心裝備
![](https://imgur.com/e3Q1woP.jpg)

### 查詢推薦符文
![](https://imgur.com/NvfvREG.jpg)

### 查詢推薦技能點法
![](https://imgur.com/eyDoLEd.jpg)

### 閱讀傳記故事
![](https://imgur.com/NTKMgKf.jpg)

### 重新選擇英雄
![](https://imgur.com/eZSEoC3.jpg)

## FSM

### FSM
![](https://imgur.com/LW2UYMq.jpg)

### state說明
* user : 輸入任意鍵開始使用LOL小幫手
* lobby : 選擇英雄
* champions : 選擇要查詢的內容
* story : 查詢傳記故事
* items : 查詢核心裝備
* skills : 查詢推薦技能點法
* runes : 查詢推薦符文


## Line 

![](https://imgur.com/Pppv8tn.jpg)
 ID : @620lvksl