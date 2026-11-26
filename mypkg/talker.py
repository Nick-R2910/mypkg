import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）
from person_msgs.srv import Query

rclpy.init()                     #rclpyの初期化（最初に1回）
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成

def cb(request, response):          #変更: 依頼が来るたびに呼ばれる
    if request.name == "鈴木太郎":   #変更: 依頼（request）のnameを見る
        response.age = 41           #変更: 返事（response）のageに年齢を入れる
    elif request.name == "古谷凌大":
        response.age = 20
    else:
        response.age = 255          #変更: 知らない人なら255
    return response

def main():
    srv = node.create_service(Query, "query", cb)
    rclpy.spin(node)            #実行（無限ループ。タイマーや送受信を処理し続ける）

