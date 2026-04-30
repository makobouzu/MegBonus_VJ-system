# MegBonus ライブ演出システム

[MegBonus（メグボーナス）のライブイベント](https://e.usen.com/news/news-event/meg-bonus429.html)にて、実際の映像演出・リアルタイム制御に使用されたシステムファイル群です。

## 📂 ファイル構成

本プロジェクトは以下の主要ファイルで構成されています。

### 1. メインシステム
* **`MegBonus.toe`**
    * システムの核となるファイルです。
    * 映像出力、映像エフェクトの処理、および全体のルーティングを管理します。

### 2. コントローラー設定
* **`midi-controller.maxpat`** (Max/MSP)
    * ライブ演奏・演出中に使用するMIDIキーボードやコントローラーのキーアサインを定義しています。

### 3. 映像演出コンポーネント
* **`subMegBonus_ver2.toe`**
    * Windows PC上で動作させる個別の映像演出パートです。
* **`streamdiffusiontd_0.3.1.toe`**
    * **生成AI演出用**: StreamDiffusionを用いたリアルタイム画像生成による映像演出を行います。

---

## 💻 動作環境 (Windows PC)

本システムを安定して動作させるためには、以下のバージョン環境が必要です。

| 項目 | 指定バージョン |
| :--- | :--- |
| **OS** | Windows 10/11 |
| **TouchDesigner** | 2023.12370 |
| **Python** | 3.11.9 |
| **CUDA** | 12.8 |

---

## ⚠️ 注意事項：リアルタイム生成AIについて

`streamdiffusiontd_0.3.1.toe` を使用する際は、以下の点に十分注意してください。

1. **ライセンスとアクセス権**
   * 本演出機能（StreamDiffusion TD）を利用するには、**DotSimulateのPatreonへの加入（課金）**が必要です。
   * [DotSimulate Patreon ポータル](https://www.patreon.com/c/dotsimulate/posts)
2. **バージョンの互換性**
   * 最新のバージョンを使用するようにしてください。古いバージョンを使用すると、モデルの参照エラー（参照先が古い、または存在しない等）によりシステムが正常に起動しない恐れがあります。

---

## 🔗 参考リンク
- [USEN ニュースリリース - MegBonus](https://e.usen.com/news/news-event/meg-bonus429.html)
