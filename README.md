# tiny_reaction_game

### pygameの勉強として小さなリアクションタイムの測定をするゲームを作ってみました

## 作成したときのバージョン
- Python: 3.12.5
- Pygame: 2.6.1

### セットアップ手順（仮想環境なし）

```bash
git clone https://github.com/rrr-bit00/tiny_react_game.git
cd tiny_react_game
pip install -r requirements.txt
python main.py
```
### 仮想環境を使用する場合(venv)
```bash
git clone https://github.com/rrr-bit00/tiny_react_game.git
cd tiny_react_game
python3 -m venv venv
source venv/bin/activate
# Windowsなら venv\Scripts\activate

pip install -r requirements.txt
python main.py

# 作業が終わったら、以下で仮想環境を終了できます
deactivate
```

## 🔤 フォントについて

日本語表示には「Noto Sans JP（Google Fonts）」を使用しています。  
フォントファイルはリポジトリには含まれていないため、以下の手順で追加してください：

1. [Noto Sans JP（Google Fonts）](https://fonts.google.com/specimen/Noto+Sans+JP) にアクセス
2. `NotoSansJP-VariableFont_wght.ttf` をダウンロード
3. このプロジェクトのルートディレクトリ（`tiny_react_game/`）に追加してください

※ フォントが存在しない場合は、システムフォントで代替されますが、日本語の表示崩れが起こる可能性があります。

### 🔘 操作方法
- 起動後、カウントダウン（3→2→1）のあと、白いボックスが表示されます  
- ランダムなタイミングでボックスが青色に変化します  
- **その瞬間、ボックス内でマウスクリック（右左どちらでも可）すると反応速度が記録されます**  
- 測定は5回行われ、終了後に平均反応速度が表示されます  
- 範囲外やタイミング外でのクリックは無効です
