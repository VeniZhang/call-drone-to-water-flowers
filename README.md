# call-drone-to-water-flowers
## 某移动终端创新大赛未提交作品。

1. 地面树莓派负责采集温度和湿度信息，当超过预设置的阈值时，会通过websocket向机载树莓派发送报警信息和gps坐标信息。
2. 机载树莓派接收到信息后，在10米（预设置）的高空飞行至报警点，降落至2米的高度后，喷水，持续十秒钟后，返航。


## requirement：
  * python2
  * python3
  * mavlink
  * mavproxy
  * dronekit
  * websocket-client
  * websocket-server
  * Qgroundcontrol
  * 树莓派 * 2
  * pixhawk * 1
  * dht11 温度、湿度传感器
  * 继电器 RL01 * 1
  * 小水泵 * 1
  * 水管10cm
  * 小水箱 * 1
  * 温度、湿度传感器代码： https://github.com/VeniZhang/high-temperature-alert-by-raspberry

  
### Warning：代码已测试，未组装飞行。
