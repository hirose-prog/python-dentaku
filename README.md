# Python CLI 電卓アプリ

## 概要

このアプリは、Pythonを使用して作成されたシンプルなコマンドライン（ターミナル）ベースの電卓です。基本的な四則演算（足し算、引き算、掛け算、割り算）をユーザーの入力に基づいて実行し、結果を表示します。

## 機能一覧

-   **数字の入力**: ユーザーから2つの数字の入力を受け付けます。
-   **四則演算**: 足し算（`+`）、引き算（`-`）、掛け算（`*`）、割り算（`/`）を実行します。
-   **結果表示**: 各演算の結果をターミナルに表示します。
-   **(今後の拡張予定)**: 割り算におけるゼロ除算エラーへの対応。

## 使用技術

-   Python

## 使い方

1.  このリポジトリをあなたのPCにクローンします。
    ```bash
    git clone [https://github.com/hirose-prog/python-dentaku.git](https://github.com/hirose-prog/python-dentaku.git)
    ```
2.  プロジェクトのフォルダに移動します。
    ```bash
    cd python-dentaku
    ```
3.  アプリを起動します。
    ```bash
    python calculator.py
    # または python3 calculator.py
    ```
4.  ターミナルに表示される指示に従って、数字を入力してください。

## このプロジェクトから学んだこと

この電卓アプリの作成を通して、以下のPythonプログラミングの基礎を実践的に習得しました。

-   **ユーザーからの入力受付（`input()`）と画面への情報出力（`print()`）**
-   **データ型変換**: 文字列（`str`）から整数（`int`）への変換
-   **基本的な算術演算子**: 足し算（`+`）、引き算（`-`）、掛け算（`*`）、割り算（`/`）の使い方
-   **変数**: 計算結果などを一時的に保存する方法
-   **簡単なCLI（コマンドラインインターフェース）アプリの開発経験**
-   **GitとGitHubの高度なワークフロー**:
    -   リポジトリの作成と初期化
    -   ファイルの追加とコミット（`git add`, `git commit`）
    -   リモートリポジトリの設定と管理（`git remote add`）
    -   GitHubへのコードのプッシュ（`git push`）
    -   **特に、コミット履歴の著者情報書き換え（`git filter-branch`）と強制プッシュ（`git push --force-with-lease`）**

---<img width="716" alt="スクリーンショット 2025-06-29 16 51 47" src="https://github.com/user-attachments/assets/4bf46470-2492-4da9-8ed7-8b869c67821e" />
