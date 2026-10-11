# python-spacecraft-dynamics

JAXA『人工衛星の力学と制御：宇宙機ダイナミクス・姿勢制御技術ユニット』を手がかりに、
理論とPython実装を行き来しながら人工衛星の力学・制御を学ぶ教材です。
執筆者自身の理解を深め、後から読む人の学習や、実務でのアルゴリズムの試作にも役立つ教材を目指します。

## 学習の方針

- 原本PDFの章番号・節番号、記号、定義、式番号、用語を尊重します。
- 原本に基づく説明と、教材として追加する補足・解釈を区別します。
- 第1章「数学的準備」から、節や概念を小さく区切って進めます。
- 数式の前提と途中の変形を示し、コードとの対応と数値的な検証を確認します。
- まず章ごとのサンプルを育て、複数の章で必要になった処理について共通化を検討します。

原本の参照先：[JAXAリポジトリ](https://jaxa.repo.nii.ac.jp/records/6101)

## 開発環境

Pythonと依存関係はuvで管理します。使用するPythonの系列は`.python-version`、
直接の依存関係は`pyproject.toml`、解決されたバージョンは`uv.lock`に記録します。

```sh
cd python-spacecraft-dynamics
uv sync --locked
uv run --locked python --version
uv run --locked python -c "import numpy, matplotlib; print(numpy.__version__, matplotlib.__version__)"
```

`uv sync`はリポジトリ内の`.venv`を作成・同期します。
仮想環境を手動で有効化しなくても、`uv run`でその環境を使えます。
現在の直接の依存関係はNumPyとMatplotlibです。

将来のパッケージ化に備えてプロジェクト情報を管理します。
章ごとの構成は確認後に追加し、共通ライブラリやビルド設定は必要になった段階で整備します。
