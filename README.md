# python-spacecraft-dynamics

JAXA『人工衛星の力学と制御：宇宙機ダイナミクス・姿勢制御技術ユニット』を手がかりに、
理論とPython実装を行き来しながら人工衛星の力学・制御を学ぶ教材です。
執筆者自身の理解を深め、後から読む人の学習や、実務でのアルゴリズムの試作にも役立つ教材を目指します。

原本の参照先：[JAXAリポジトリ](https://jaxa.repo.nii.ac.jp/records/6101)

## 学習内容と対応コード

### 第1章 数学的準備

学習記事：

- [人工衛星の力学と制御に必要な数学の基礎：座標系・ベクトル](https://watlab-blog.com/2026/10/11/sapacecraft-dynamics-math/)
- [人工衛星の力学と制御に必要な数学の基礎：ダイアディック](https://watlab-blog.com/2026/10/25/python-spacecraft-dyadic/)

現在のサンプルが扱う内容を、原本PDFの節番号に対応させて整理しています。
コードは[chapter_01](chapter_01/)にあります。

<table>
  <thead>
    <tr>
      <th>原本PDFの節</th>
      <th>学習内容・コードで確認できること</th>
      <th>対応コード</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1.1 座標系と座標</td>
      <td>右手系の直交座標系、原点O、点Pとその座標を図で確認する。3次元の座標系を2次元の図に投影して描画する。</td>
      <td><a href="chapter_01/01_coordinate_system.py">01_coordinate_system.py</a></td>
    </tr>
    <tr>
      <td rowspan="2">1.2 ベクトル</td>
      <td>スカラー三重積と、その絶対値で表される平行六面体の体積を計算する。3次元の図と数値出力で、底面積×高さとの対応を確認する。</td>
      <td><a href="chapter_01/02_scalar_triple_product.py">02_scalar_triple_product.py</a></td>
    </tr>
    <tr>
      <td>入力ベクトル <code>v = (3, 4)</code> と、x軸への射影ベクトル <code>v_x = (3, 0)</code> を2次元の図に描く。入力ベクトルの終点からx軸への垂線と射影点を確認する。</td>
      <td><a href="chapter_01/03_projection_example.py">03_projection_example.py</a></td>
    </tr>
    <tr>
      <td>1.3 ダイアディック</td>
      <td>標準基底ベクトルのダイアドを <code>np.outer</code> で求め、係数付きで足し合わせてダイアディックの行列表現を構成する。入力ベクトルへの作用 <code>w = D @ v</code> を計算し、各入力成分の寄与ベクトルの和が出力ベクトルになることを3次元の図と数値出力で確認する。</td>
      <td><a href="chapter_01/04_dyadic.py">04_dyadic.py</a></td>
    </tr>
  </tbody>
</table>

## 学習の方針

- 原本PDFの章番号・節番号、記号、定義、用語を尊重します。
- 原本に基づく説明と、教材として追加する補足・解釈を区別します。
- 第1章「数学的準備」から、節や概念を小さく区切って進めます。
- 数式の前提と途中の変形を示し、コードとの対応と数値的な検証を確認します。
- まず章ごとのサンプルを育て、複数の章で必要になった処理について共通化を検討します。

## 原本PDFとの相違内容

- ブログ記事では独自の式番号を付けているため、原本PDFの式番号とは一致しません。
- 式番号を参照する際は、原本PDFとブログ記事のどちらの番号かを明示します。

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

### サンプルの実行

リポジトリのルートで、確認したい内容に対応するコードを実行します。

```sh
# 1.1 座標系と座標
uv run --locked python chapter_01/01_coordinate_system.py

# 1.2 ベクトル：スカラー三重積と平行六面体の体積
uv run --locked python chapter_01/02_scalar_triple_product.py

# 1.2 ベクトル：x軸への射影
uv run --locked python chapter_01/03_projection_example.py

# 1.3 ダイアディック：入力ベクトルへの作用と各入力成分の寄与
uv run --locked python chapter_01/04_dyadic.py
```

いずれもMatplotlibのウィンドウに図を表示します。
`02_scalar_triple_product.py`は、ウィンドウを閉じた後に計算結果をターミナルにも出力します。
`04_dyadic.py`は、図を表示する前に入力ベクトル、出力ベクトル、各寄与ベクトルをターミナルにも出力します。

将来のパッケージ化に備えてプロジェクト情報を管理します。
章ごとのサンプルを育てながら、共通ライブラリやビルド設定は必要になった段階で整備します。
