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
  ###[count.py](https://github.com/YuusakuSugiyama/mypkg/blob/main/scripts/count.py)はパブリッシャを1つもちn+1を10Hzで実行し1秒間に10ずつ数字が増加するものです。
  ###[twice.py](https://github.com/YuusakuSugiyama/mypkg/blob/main/scripts/twice.py)はサブスクライバを1つもちcount_upというトピックを購読しdataという変数を2倍しログとして吐出すものです。
  
  - 実行する際には以下のコマンドを別々の端末に打ち込んみ実行します。
  
   ```bash
  roscore
  rosrun mypkg count.py
  rosrun mypkg twice.py
   ```
  
  ### その他の実行
  
  - 起動しているノードを確認する際は以下のコマンドを打ち込んで確認します。
  
 ```bash
  rosnode list
  ```
  -　ノードの終了は`Ctrl+c Enter`を押します。
  
  ## デモ動画
  
  - 実行した結果はこちらの動画からご覧ください。
  
  - [count.pyの実行動画](https://youtu.be/zr47Iegq6zg)
  
  - [twice.pyの実行動画](https://youtu.be/w6PfSjNVh38)
  
  
  ## 著者
  
  [Ryuichi Ueda](https://github.com/ryuichiueda)
  
  ROSのセットアップの手引き :
  [Ryuichi Ueda](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server)
  
  ## ライセンス
  
  [BSD 3-Clause "New" or "Revised" License](https://github.com/YuusakuSugiyama/mypkg/blob/main/LICENSE)
  
  
