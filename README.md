# OSCscript
some python-osc script personal use

# timer.py 定時ギミック退社システム
VRChatのアバターパラメータをOSCに通して一定時間に変更する 特定時間にギミックをオフするように想定しています。
## 動作
timerパラメータ(bool) 24時間内に6時以下ならflase ７時以上ならtrue
## Requirements
python-osc
## Tested Envirement
Windows 11 21H2 , Python 3.10.2

# furifuri.py しっぽfurifuriアニメーション
しっぽをふりふりします
## 動作
TailToggleもしくはTailBoolを設定されているアバターのtailコントロールを有効化、0.1秒間にTailX,TailH,TailBlendHなどの横軸のpuppetアニメーションを操作する
## Requirements
python-osc
## Tested Envirement
Windows 11 21H2 , Python 3.10.2



