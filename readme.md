# はじめに

gitコマンドの拡張です。githubのwikiリポジトリをトップディレクトリに展開し、マークダウン資料などに使うイメージのアップロードに使用します。

# インストール

pipでインストールしてください。

```
$ pip install git+https://github.com/mountcedar/github-images.git
```

# 使い方

以下のようにgit imagesから各サブコマンドを実行します。

```
$ git images [init|list|upload|remove]
```

それぞれの役割は以下の通りです。

* init: 既存のgithubリポジトリからwikiリポジトリをcloneし、imagesディレクトリを作成します。
* list: 現状、wiki/imagesにアップロードされているファイルをリストアップします。
* upload: 指定したパスのイメージをwiki/imagesにアップロードし、そのパスを返します。
* remove: 指定したファイルを削除します。
