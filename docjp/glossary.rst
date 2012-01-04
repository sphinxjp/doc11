.. Glossary
.. ========

.. _glossary:

用語集
======

..
   .. builder
         A class (inheriting from :class:`~sphinx.builders.Builder`) that takes
         parsed documents and performs an action on them.  Normally, builders
         translate the documents to an output format, but it is also possible to
         use the builder builders that e.g. check for broken links in the
         documentation, or build coverage information.
 
         See :ref:`builders` for an overview over Sphinx' built-in builders.

   .. directive
         A reStructuredText markup element that allows marking a block of content
         with special meaning.  Directives are supplied not only by docutils, but
         Sphinx and custom extensions can add their own.  The basic directive
         syntax looks like this::
   
            .. directivename:: argument ...
               :option: value

               Content of the directive.

         See :ref:`directives` for more information.

   .. document name
         Since reST source files can have different extensions (some people like
         ``.txt``, some like ``.rst`` -- the extension can be configured with
         :confval:`source_suffix`) and different OSes have different path separators,
         Sphinx abstracts them: :dfn:`document names` are always relative to the
         :term:`source directory`, the extension is stripped, and path separators
         are converted to slashes.  All values, parameters and such referring to
         "documents" expect such document names.

         Examples for document names are ``index``, ``library/zipfile``, or
         ``reference/datamodel/types``.  Note that there is no leading or trailing
         slash.

   .. domain
         A domain is a collection of markup (reStructuredText :term:`directive`\ s
         and :term:`role`\ s) to describe and link to :term:`object`\ s belonging
         together, e.g. elements of a programming language.  Directive and role
         names in a domain have names like ``domain:name``, e.g. ``py:function``.

         Having domains means that there are no naming problems when one set of
         documentation wants to refer to e.g. C++ and Python classes.  It also
         means that extensions that support the documentation of whole new
         languages are much easier to write.  For more information about domains,
         see the chapter :ref:`domains`.

   .. environment
      A structure where information about all documents under the root is saved, and used for cross-referencing.  The environment is pickled after the parsing stage, so that successive runs only need to read and parse new and changed documents.

   .. master document
         The document that contains the root :rst:dir:`toctree` directive.

   .. object
       The basic building block of Sphinx documentation.  Every "object
       directive" (e.g. :rst:dir:`function` or :rst:dir:`object`) creates such a block;
       and most objects can be cross-referenced to.

   .. role
         A reStructuredText markup element that allows marking a piece of text.
         Like directives, roles are extensible.  The basic syntax looks like this:
         ``:rolename:`content```.  See :ref:`inlinemarkup` for details.

   .. source directory
       The directory which, including its subdirectories, contains all source files for one Sphinx project.

   .. configuration directory
       The directory containing :file:`conf.py`.  By default, this is the same as the :term:`source directory`, but can be set differently with the **-c** command-line option.

.. glossary::

   ビルダー
      :class:`~sphinx.builders.Builder` を継承したクラスで、パースされたドキュメントを受け取り、それに対してアクションをします。通常、ビルダーは他の出力フォーマットへ、ドキュメントを変換しますが、壊れたリンクのチェックを行ったり、情報のカバレッジを計測したり、といった用途にも使用することができます。

      Sphinxの内蔵のビルダーに関しては、 :ref:`builders` のドキュメントを参照してください。

   ディレクティブ
      reSturcturedTextのマークアップの要素で、特別な意味を持つコンテンツのブロックを表現することができます。ディレクティブはDocutils由来のものだけでなく、Sphinx、カスタムの拡張機能によって定義されたものも使用できます。基本的なディレクティブの文法は次のようになります::

         .. ディレクティブ名:: 引数 ...
            :オプション: 値

            ディレクティブのコンテンツ

      .. より詳しい情報は :ref:`directives` を参照してください。

   ドキュメント名
      reSTのソースファイルにはいくつかの拡張子を付けることができます。 ``.txt`` と付けるのが好きな人もいますし、 ``.rst`` を好む人もいます。Sphinxの中では :confval:`source_suffix` で拡張子を設定できます。また、OSによっては、パスの区切り文字が変わります。そのため、Sphinxではこれを抽象化して、 :dfn:`ドキュメント名` として、 :term:`ソースディレクトリ` からの相対パスで、拡張子は省略し、区切り文字にスラッシュを利用するように変換されます。ドキュメントが来ることを期待する値、パラメータなどは、すべてこのようなドキュメント名が渡されるのを期待します。

      ドキュメント名のサンプルとしては、 ``index``, ``library/zipfile``, ``reference/datamodel/types`` などがあります。前後のスラッシュは完全に省略されることに注意して下さい。

   ドメイン
      ドメインは、特定のプログラミング言語の要素などの :term:`オブジェクト` の説明をしたり、リンクを張ったりするような、マークアップ(reSturucturedTextの :term:`ディレクティブ`, :term:`ロール`)を集めたものです。ドメインに属するディレクティブとロールの名前は、 ``py:function`` のように ``ドメイン:名前`` となります。

      ドメインを使用すると、ドキュメント内でC++とPythonの両方のクラスに言及したい場合などに、名前の衝突の問題を避けることができます。また、まったく新しい言語のドキュメント作成をサポートする拡張機能も作りやすくなります。ドメインに関する詳細な情報は、 :ref:`domains` の章を参照してください。
 
   環境
      ルート以下のすべてのドキュメントの情報が格納される場所です。この情報はクロスリファレンスを作成する際に利用されます。この環境には、パース段階の後の結果のpickleされたものが入ります。ソースファイルが新規で作成されたり、変更されて、読み込んだりパースしたりする必要がない限りはこの中のデータが更新されることはありません。

   マスタードキュメント
      ルートとなる :rst:dir:`toctree` ディレクティブを含むドキュメントです。
   
   オブジェクト
      Sphinxドキュメントを構築する、基本構成単位です。すべての "オブジェクトディレクティブ"(:rst:dir:`function`, :rst:dir:`object`)はこのユニットを作成します。ほとんどのオブジェクトに対して、クロスリファレンスを行うことができます。

   ロール
      reStuructredTextのマークアップの要素で、テキスト片にマーキングを行うことができます。ディレクティブと同様に、ロールも拡張することができます。基本的な文法は次のようになります: ``:ロール名:`コンテンツ``` 。詳しくは :ref:`inlinemarkup` を参照してください。

   ソースディレクトリ
      ひとつのSphinxプロジェクトにおいて、すべてのソースファイルを含むディレクトリ。このディレクトリ直下だけではなく、サブディレクトリを使用してソースファイルを分類して入れておくことも可能です。

   設定ディレクトリ
      :file:`conf.py` を含むディレクトリ。デフォルトでは :term:`ソースディレクトリ` と同じですが、 **-c** コマンドラインオプションを使用することで変更することができます。





