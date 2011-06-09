.. highlight:: rest

.. Miscellaneous markup
.. ====================

その他のマークアップ
=====================

.. _metadata:

ファイルに関するメタデータ
--------------------------

.. File-wide metadata
   ------------------

.. reST has the concept of "field lists"; these are a sequence of fields marked up
   like this:

      :fieldname: Field content

reSTには "フィールドリスト"という考えがあります。以下のようなものが、このフィールドのマークアップのリストのサンプルになります::

   :フィールド名: フィールドの内容

.. A field list near the very top of a file is parsed by docutils as the "docinfo",
   which is normally used to record the author, date of publication and other
   metadata.  *In Sphinx*, a field list preceding any other markup is moved from
   the docinfo to the Sphinx environment as document metadata and is not displayed
   in the output; a field list appearing after the document title will be part of
   the docinfo as normal and will be displayed in the output.

docutilsは、ファイルの先頭付近のフィールドリストを "docinfo" としてパースします。これは通常のドキュメントでは著者名や、公開日などのメタデータを記録するのに使用されます。 **Sphinxでは**, docinfoはメタデータとして使用されますが、出力はされません。フィールドリストは、ドキュメントのタイトルの後に、いつものように表示されます。

.. At the moment, these metadata fields are recognized:

このタイミングでは、以下のメタデータのフィールドが識別されています:

``tocdepth``
   .. The maximum depth for a table of contents of this file.

   このファイルに表示する目次の最大の深さ

   .. versionadded:: 0.4


``nocomments``
   .. If set, the web application won't display a comment form for a page generated
      from this source file.

   もし設定されていれば、このソースファイルから生成されたページをウェブアプリケーションが表示する際には、コメントフォームが表示されなくなります。


``orphan``
   .. If set, warnings about this file not being included in any toctree will be
      suppressed.

   もしこれが設定されると、toctreeから参照されていない時に出力される警告が抑制されます。

   .. versionadded:: 1.0


.. Meta-information markup
.. -----------------------

メタ情報マークアップ
--------------------

..
  .. rst:directive:: .. sectionauthor:: 名前 <Eメール>

.. rst:directive:: .. sectionauthor:: name <email>

   .. Identifies the author of the current section.  The argument should include
      the author's name such that it can be used for presentation and email
      address.  The domain name portion of the address should be lower case.

   現在のセクションの著者名を指定します。引数には必ず、表示するための著者の名前と、電子メールのアドレスを入れます。アドレスのドメイン名の部分は小文字でなければなりません。

   .. Example:

   サンプル::

     .. sectionauthor:: Guido van Rossum <guido@python.org>

   .. By default, this markup isn't reflected in the output in any way (it helps
      keep track of contributions), but you can set the configuration value
      :confval:`show_authors` to True to make them produce a paragraph in the
      output.

   デフォルトでは、このマークアップは出力に反映されません(貢献者の名前を調べる手助けにはなります)。しかし、設定ファイルの :confval:`show_authors` をTrueに設定すると、出力ファイルの中にこの情報に関する段落が作成されます。

      .. sectionauthor:: Guido van Rossum <guido@python.org>

..
   .. rst:directive:: .. codeauthor:: name <email>

.. rst:directive:: .. codeauthor:: 名前 <Eメール>

   .. The :rst:dir:`codeauthor` directive, which can appear multiple times, names the
      authors of the described code, just like :rst:dir:`sectionauthor` names the
      author(s) of a piece of documentation.  It too only produces output if the
      :confval:`show_authors` configuration value is True.

   :rst:dir:`codeauthor` ディレクティブは、 :rst:dir:`sectionauthor` の名前と同じく、説明しているコードの作者名について、複数人書くことができます。 :confval:`show_authors` 設定値をTrueにしないかぎり、出力はされません。


インデックス生成のためのマークアップ
------------------------------------

.. Sphinx automatically creates index entries from all object description (like 
   functions, classes or attributes) like discussed :ref:`domains`.

Sphinxはすべてのオブジェクトの説明(関数、クラス、属性)から、自動的にインデックスのエントリーを作成します。オブジェクトの説明に関しては、 :ref:`domains` で詳しく説明しています。

.. However, there is also an explicit directive available, to make the index more 
   comprehensive and enable index entries in documents where information is not 
   mainly contained in information units, such as the language reference.

しかし、これ以外に明示的に指定するディレクティブもあります。これを使用することで、言語のリファレンスのように、メインの情報のユニットが存在しない情報をドキュメントの中に書いてインデックスのエントリーを作ることができるようになります。より包括的なインデックスを作成することができるようになります。

.. 
   .. rst:directive:: .. index:: <entries>

.. rst:directive:: .. index:: <エントリー>

   .. This directive contains one or more index entries.  Each entry consists of a 
      type and a value, separated by a colon.

   このディレクティブは一つ以上のインデックスのエントリーを含みます。それぞれのエントリーはコロン(:)で区切られた、タイプ、値を含みます。

   .. For example:

      .. index
         single: 実行; コンテキスト
         module: __main__
         module: sys
         triple: モジュール; 検索; パス

      The execution context
      ---------------------

      ...

   サンプル::

      .. index::
         single: execution; context
         module: __main__
         module: sys
         triple: module; search; path

      実行時のコンテキスト
      ---------------------

      ...

   .. This directive contains five entries, which will be converted to entries in 
      the generated index which link to the exact location of the index statement 
      (or, in case of offline media, the corresponding page number).

   このディレクティブは5つのエントリーを含んでいます。これらは生成されたインデックスのエントリーに変換され、index文の正確な位置へのリンクが張られることになります。オフラインのメディアに出力される場合には、リンクの代わりに対応するページ番号が出力されます。

   .. Since index directives generate cross-reference targets at their location in 
      the source, it makes sense to put them *before* the thing they refer to -- 
      e.g. a heading, as in the example above.

   indexディレクティブはそのソースの位置のターゲットとのクロスリファレンスを生成するため、それらが参照するものの *前の位置* に置くことが大切になります。上記のサンプルコードの例では、リンクを張りたい見出しの前に配置されています。

   .. The possible entry types are:

   設定可能なエントリーのタイプは以下の通りです:

   .. single
      Creates a single index entry.  Can be made a subentry by separating the
      subentry text with a semicolon (this notation is also used below to 
      describe what entries are created).

   single
      単体のインデックスのエントリーを作成します。 サブエントリーのテキストとの間をセミコロンで区切ることにより、サブエントリーをサブエントリーを作ることもできます。この記法はどのエントリーが作成されたのか、という説明のところで詳しく説明します。

   .. pair
      ``pair: loop; statement`` is a shortcut that creates two index entries, 
      namely ``loop; statement`` and ``statement; loop``.

   pair
      ``pair: loop; statement`` はインデックスエントリーを2つ作成します。
      ``loop; statement`` と ``statement; loop`` の2つのエントリーが作成されます。

   .. triple
      Likewise, ``triple: module; search; path`` is a shortcut that creates 
      three index entries, which are ``module; search path``, ``search; path, 
      module`` and ``path; module search``.

   triple
      pairと似ていますが ``triple: module; search; path`` は3つのエントリーを作成します。 ``module; search path``, ``search; path, module``, ``path; module search`` が作成されます。

   .. see
      ``see: entry; other`` creates an index entry that refers from ``entry`` to
      ``other``.

   see
      ``see: entry; other`` という項目があると、``entry`` から ``other`` を参照するインデックスエントリーが作成されます。

   .. seealso
      Like ``see``, but inserts "see also" instead of "see".

   seealso
      ``see`` と似ていますが、 "see" の代わりに、 "see also" を挿入します。

   .. module, keyword, operator, object, exception, statement, builtin
      These all create two index entries.  For example, ``module: hashlib``
      creates the entries ``module; hashlib`` and ``hashlib; module``.  (These
      are Python-specific and therefore deprecated.)

   module, keyword, operator, object, exception, statement, builtin
      これらはすべて、2つのエントリーを作成します。例えば、 ``module: hashlib`` という項目があると、 ``module; hashlib`` と ``hashlib; module`` の2つのエントリーが作成されます。(これらはPython固有で、deperecatedになっています。)

   .. You can mark up "main" index entries by prefixing them with an exclamation
      mark.  The references to "main" entries are emphasized in the generated
      index.  For example, if two pages contain :

   もしエクスクラメーションマーク(!)を前に付けると、主要なインデックスエントリーである、ということを表現することができます。主要なインデックスは、生成されたインデックスの中で強調されます。例えば、2つのページが次のようなディレクティブを持っていたとします::

      .. index:: Python

   .. and one page contains :

   そして、次の内容を含むページがあったとします::

      .. index:: ! Python

   .. then the backlink to the latter page is emphasized among the three backlinks.

   この場合、最後のページへのバックリンクが3つの中では強調されて表示されます。

   .. For index directives containing only "single" entries, there is a shorthand notation:

   "single"のエントリーだけが含まれるindexディレクティブの場合、以下のように短縮記法で簡単に作成することもできます::

      .. index:: BNF, grammar, syntax, notation

   .. This creates four index entries.

   これは4つのインデックスのエントリーが作成されます。

   .. 
      versionchanged:: 1.1
      Added ``see`` and ``seealso`` types, as well as marking main entries.

   .. versionchanged:: 1.1
      ``see`` と ``seealso`` と、メインエントリーのマークが追加されました。

.. rst:role:: index

   .. While the :rst:dir:`index` directive is a block-level markup and links to the
      beginning of the next paragraph, there is also a corresponding role that sets
      the link target directly where it is used.

   :rst:dir:`index` ディレクティブは、ブロックレベルのマークアップで、次のパラグラフの先頭に対するリンクを生成します。これとは別に、直接リンクターゲットに設定するロールもあります。

   .. The content of the role can be a simple phrase, which is then kept in the
      text and used as an index entry.  It can also be a combination of text and
      index entry, styled like with explicit targets of cross-references.  In that
      case, the "target" part can be a full entry as described for the directive
      above.  For example:

      This is a normal reST :index:`paragraph` that contains several
      :index:`index entries <pair: index; entry>`.

   ロールのコンテンツは、文章の中にあるシンプルなフレーズで、そのままインデックスのエントリーとして使用されます。テキストと入力エントリーの組み合わせになっていて、明示的なクロスリファレンスのターゲットになります。この場合、ターゲットの部分は上記で説明したディレクティブの機能をフルに使うことができます::

      これは、いくつかの :index:`インデックスエントリー <pair: index; entry>` を含む通常のreSTの :index`段落` です。


   .. versionadded:: 1.1


.. _tags:

タグを使用したインクルード
--------------------------

.. Including content based on tags
   -------------------------------

.. .. rst:directive:: .. only:: <expression>

   Include the content of the directive only if the *expression* is true.  The
   expression should consist of tags, like this::

      .. only:: html and draft

   Undefined tags are false, defined tags (via the ``-t`` command-line option or
   within :file:`conf.py`) are true.  Boolean expressions, also using
   parentheses (like ``html and (latex or draft)``) are supported.

   The format of the current builder (``html``, ``latex`` or ``text``) is always
   set as a tag.

.. rst:directive:: .. only:: <式>

   *<式>* が真のときだけ、ディレクティブの内容をインクルードします。式は以下のようにタグで構成されます。

   ::

      .. only:: html and draft

   未定義のタグはfalseになります。コマンドラインの ``-t`` オプションもしくは :file:`conf.py` によって定義されたタグはtrueとして扱われます。カッコも含めて、ブール演算も使用することができます。 ``html and (latex or draft)`` というような表現がサポートされています。

   現在のビルダーのフォーマットのタグ (``html``, ``latex``, ``text``) は常にタグとしてセットされます。

   .. versionadded:: 0.6


.. Tables
.. ------

テーブル
--------

.. Use :ref:`standard reStructuredText tables <rst-tables>`.  They work fine in
   HTML output, however there are some gotchas when using tables in LaTeX: the
   column width is hard to determine correctly automatically.  For this reason, the
   following directive exists:

:ref:`標準のreStructuredTextの表 <rst-tables>` を使用すると、HTML出力では非常にきれいな表を作成することができますが、LaTeXで出力すると、ちょっとがっかりしてしまうでしょう。現在の仕様ではカラムを自動で正しく決定するのは簡単ではありません。このような理由から、それをサポートするディレクティブがいくつか用意されています:

.. .. rst:directive:: .. tabularcolumns:: column spec

   This directive gives a "column spec" for the next table occurring in the
   source file.  The spec is the second argument to the LaTeX ``tabulary``
   package's environment (which Sphinx uses to translate tables).  It can have
   values like ::

      |l|l|l|

   which means three left-adjusted, nonbreaking columns.  For columns with
   longer text that should automatically be broken, use either the standard
   ``p{width}`` construct, or tabulary's automatic specifiers:

   +-----+------------------------------------------+
   |``L``| ragged-left column with automatic width  |
   +-----+------------------------------------------+
   |``R``| ragged-right column with automatic width |
   +-----+------------------------------------------+
   |``C``| centered column with automatic width     |
   +-----+------------------------------------------+
   |``J``| justified column with automatic width    |
   +-----+------------------------------------------+

   The automatic width is determined by rendering the content in the table, and
   scaling them according to their share of the total width.

   By default, Sphinx uses a table layout with ``L`` for every column.

   .. versionadded:: 0.3

.. rst:directive:: .. tabularcolumns:: カラム 仕様

   このディレクティブは次に作成するテーブルの "カラム仕様" を設定します。仕様はSphinxがテーブルの変換に使用している、LaTeXの ``tabulary`` パッケージ環境のためのものです。2番目の引数として設定します。以下のような値を設定します::

      |l|l|l|

   これは、３つの左寄せの、改行なしのカラムの意味になります。それぞれのカラムで、長いテキストを適切に自動的に改行させるためには、標準の ``p{width}`` 構造体を使用するか、tabularyの自動設定を使用します。

   +-----+------------------------------------------+
   |``L``| 左寄せのカラム。長さは自動調整。         |
   +-----+------------------------------------------+
   |``R``| 右寄せのカラム。長さは自動調整。         |
   +-----+------------------------------------------+
   |``C``| 中央寄せのカラム。長さは自動調整。       |
   +-----+------------------------------------------+
   |``J``| テキストを広げるカラム。長さは自動調整。 |
   +-----+------------------------------------------+

   長さが自動調整となっているものは、全体の長さのうち、それぞれのカラムが占める幅の割合に応じて列の大きさはスケールします。

   デフォルトでは、Sphinxはすべてのカラムに対して ``L`` を適用したレイアウトを自動で行います。

.. warning::

   .. Tables that contain list-like elements such as object descriptions,
      blockquotes or any kind of lists cannot be set out of the box with
      ``tabulary``.  They are therefore set with the standard LaTeX ``tabular``
      environment if you don't give a ``tabularcolumns`` directive.  If you do, the
      table will be set with ``tabulary``, but you must use the ``p{width}``
      construct for the columns that contain these elements.

   オブジェクトの説明などのリストのような要素や、ブロッククオート、リストなどを含むテーブルは、 ``tabulary`` 環境では、箱に並べることはできません。``tabularcolumns`` ディレクティブを与えていない場合は、LaTeX標準の ``tabular`` 環境が使用されます。このような要素を含めようとしている場合、テーブルに ``tabulary`` がセットされますが、これらの要素ほ含むカラムには、 ``p{width}`` コンストラクタを使うようにしてください。

   .. Literal blocks do not work with ``tabulary`` at all, so tables containing a
      literal block are always set with ``tabular``.  Also, the verbatim
      environment used for literal blocks only works in ``p{width}`` columns, which
      means that by default, Sphinx generates such column specs for such tables.
      Use the :rst:dir:`tabularcolumns` directive to get finer control over such
      tables.

   リテラルブロックは ``tabulary`` と一緒にしても、まったく動作しませんが、リテラルブロックを含むテーブルは ``tabular`` をセットします。また、 ``p{width}`` を設定しないと、同様な環境は使用することはできません。デフォルトでは、というのは、Sphinxはそのようなテーブルのためには、そのようなカラムを生成します。 :rst:dir:`tabularcolums` ディレクティブを使用することで、テーブルに対して細かい制御ができるようになります。






