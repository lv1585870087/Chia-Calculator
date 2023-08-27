# Chia-Calculator
Calculate XCH income

HDD=65                        #开始的硬盘个数
toTiB=0.9                     #实际容量/标签容量 比值
COMPRESS=0.77                 #压缩图压缩率 （K32=101G gh_C8=71.3G 官方C7=77.9G）  爆块收入占总收入：20%  gh_手续费[爆块1/4概率打入开发者钱包] 20%/4=5%
HDD_price=590                 #14T硬盘价格(HC620) CNY
XCHUSDT=30                    #XCH价格
USDtoCNY=7.2                  #汇率
HDD_lable_TB=14               #硬盘标签容量
XCH_revenue_per_10TiB=0.00298 #每10TiB 一天收入的XCH
XCH_revenue_per_thisHDD=(HDD_lable_TB*toTiB/COMPRESS)/10*XCH_revenue_per_10TiB   #每天这款一块硬盘的XCH收入
CNY_revenue_per_oneHDD=XCH_revenue_per_thisHDD*XCHUSDT*USDtoCNY                  #每天这款一块硬盘的当地货币收入

<img width="470" alt="image" src="https://github.com/lv1585870087/Chia-Calculator/assets/45760920/5f058b22-6cea-4748-86f2-06a4664d177d">
