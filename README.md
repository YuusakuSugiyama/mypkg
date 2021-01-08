# mypkg

ロボットシステム学の課題2のROSパッケージです。

---

## 動作環境

以下の環境にて動作します。

-ROS Noetic
 - OS: Ubuntu 20.04.1 LTS
 - Device: Raspberry Pi 4 Model B
 
## インストール方法

- [ros_setup_scripts_Ubuntu20.04_server](http://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server)を参照しROSをインストールします。

- [ロボットシステム学第10回](https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/)を参照しワークスペースを準備します。

- `git`を使用して本パッケージをダウンロードします。

  ```bash
  cd ~/catkin_ws/src
  git clone https://github.com/YuusakuSugiyama/mypkg.git
  ```

- `catkin_make`を使用して本パッケージをビルドします。

  ```bash
  cd ~/catkin_ws && catkin_make
  ```
  
  ##パッケージについて
  - count.pyはパブリッシャを1つもちn+1を10Hzで実行し1秒間に10ずつ数字が増加するものです。
  - twice.pyはサブスクライバを1つもちcount_upというトピックを購読しdataという変数を2倍しログとして吐出すものです。
  
  
