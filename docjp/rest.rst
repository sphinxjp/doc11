.. highlightlang:: rest

.. reStructuredText Primer
   =======================

.. _rst-primer:

reStructuredText入門
====================

.. This section is a brief introduction to reStructuredText (reST) concepts and syntax, intended to provide authors with enough information to author documents productively.  Since reST was designed to be a simple, unobtrusive markup language, this will not take too long.

このセクションは、reStructuredText(reST)の考え方や文法についての短いイントロダクションです。Sphinxユーザがドキュメントを作成するために十分な情報を提供します。reSTはシンプルに設計された、控えめなマークアップ言語ですので、理解するのにそれほど時間はかからないでしょう。

.. seealso::
    
    .. The authoritative `reStructuredText User Documentation
       <http://docutils.sourceforge.net/rst.html>`_. The "ref" links in this
       document link to the description of the individual constructs in the reST
       reference.

    本家 `reStructuredTextユーザドキュメント <http://docutils.sourceforge.net/rst.html>`_
    このドキュメント中の参照リンクは、reSTのリファレンスの個々の要素の説明にリンクしています。


.. Paragraphs
   ----------

段落(パラグラフ)
----------------

.. The paragraph (:duref:`ref <paragraphs>`) is the most basic block in a reST 
   document.  Paragraphs are simply chunks of text separated by one or more blank 
   lines.  As in Python, indentation is significant in reST, so all lines of the 
   same paragraph must be left-aligned to the same level of indentation.

段落(:duref:`ref <paragraphs>`)はreSTドキュメントにおける、もっとも基本的な要素です。段落は1行以上の空行で区切られた、シンプルなテキストの固まりです。 Pythonにおいてインデントが重要な意味を持つのと同様、reSTでもインデントは重要です。同じ段落のすべての行は、インデントを同じ高さにそろえて、左揃えにしなければなりません。

.. Inline markup
   -------------

.. _inlinemarkup:

インラインマークアップ
--------------------------------

.. The standard reST inline markup is quite simple: use

標準のreSTインラインマークアップは極めてシンプルです。

.. * one asterisk: ``*text*`` for emphasis (italics),
   * two asterisks: ``**text**`` for strong emphasis (boldface), and
   * backquotes: ````text```` for code samples.

* アスタリスク1つ: ``*テキスト*`` 強調( *イタリック* )
* アスタリスク2つ: ``**テキスト**`` 強い強調( **太文字** )
* バッククオート: ````テキスト```` コードサンプル( ``固定長`` )

.. If asterisks or backquotes appear in running text and could be confused with
   inline markup delimiters, they have to be escaped with a backslash.

もしも、アスタリスクかバッククオートがテキスト中に使用する場合は、インラインマークアップの区切り文字と間違ってしまうことがあります。そのような場合には、バックスラッシュ(訳注:日本語フォントだと円記号)を使ってエスケープしてください。

.. Be aware of some restrictions of this markup:

このマークアップにはいくつかの制限があります。

.. * it may not be nested,
   * content may not start or end with whitespace: ``* text*`` is wrong,
   * it must be separated from surrounding text by non-word characters.  Use a
     backslash escaped space to work around that: ``thisis\ *one*\ word``.

* ネストすることはできません
* 中のテキストの最初、もしくは最後にスペースを入れることもできません。 ``* text*`` と書くことはできません
* 周囲のテキストとは、テキスト以外の文字(スペース、カッコなど)で区切る必要があります。もしも空白を空けずに、続けて表記したい場合には、 ``thisis\ *one*\ word`` と、バックスラッシュでエスケープしたテキスト(スペースは表示されません)を使用してください。

.. These restrictions may be lifted in future versions of the docutils.

これらの制限は、docutilsの将来のバージョンでも残るでしょう。

.. reST also allows for custom "interpreted text roles"', which signify that the
   enclosed text should be interpreted in a specific way.  Sphinx uses this to
   provide semantic markup and cross-referencing of identifiers, as described in
   the appropriate section.  The general syntax is ``:rolename:`content```.

reSTには、"解釈済みテキストロール"というものが許されています。これは、 ``:ロール名:`解釈済みテキスト``` という文法になります。これは、囲まれているテキストは特別な方法で解釈させることができる、というものです。Sphinxはこれをつかって、意味のマークアップと、識別子のマークアップを行っています。これに関しては別のセクションで説明します。

.. Standard reST provides the following roles:

標準のreSTは次のようなロールを提供しています:

.. * :durole:`emphasis` -- alternate spelling for ``*emphasis*``
   * :durole:`strong` -- alternate spelling for ``**strong**``
   * :durole:`literal` -- alternate spelling for ````literal````
   * :durole:`subscript` -- subscript text
   * :durole:`superscript` -- superscript text
   * :durole:`title-reference` -- for titles of books, periodicals, and other
     materials

* :durole:`emphasis` -- ``*emphasis*`` の代替表現
* :durole:`strong` -- ``**strong**`` の代替表現
* :durole:`literal` -- ````literal```` の代替表現
* :durole:`subscript` -- 下付き文字
* :durole:`superscript` -- 上付き文字
* :durole:`title-reference` -- 書籍、定期刊行物などのタイトル

.. See :ref:`inline-markup` for roles added by Sphinx.

Sphinxによって追加されたロールに関しては :ref:`inline-markup` を参照してください。

.. Lists and Quotes-like blocks
   ----------------------------

リストと引用のようなブロック
----------------------------

.. List markup (:duref:`ref <bullet-lists>`) is natural: just place an asterisk at 
   the start of a paragraph and indent properly.  The same goes for numbered lists; 
   they can also be autonumbered using a ``#`` sign::

リストを表現するマークアップ (:duref:`ref <bullet-lists>`) はほぼ結果の見た目通りです。パラグラフの最初をアスタリスクで開始して、適切にインデントをしてやるだけです。ナンバー付きのリストも同様です。 ``#`` を使うことで、ナンバリングを自動で行うこともできます::

   * これは丸が行頭に付くリストです
   * このリストには2つの項目があります。2つめの
     項目は2行にまたがっています。

   1. これはナンバー付きリストです。
   2. これも2つの項目があります。

   #. これはナンバー付きリストです。
   #. これも2つの項目があります。

.. * This is a bulleted list.
   * It has two items, the second
     item uses two lines.

   1. This is a numbered list.
   2. It has two items too.

   #. This is a numbered list.
   #. It has two items too.

.. Nested lists are possible, but be aware that they must be separated from the
   parent list items by blank lines::

ネストされたリストも使用することができますが、親のリストとは空白行で区切る必要があります::

   * これは
   * リストです

     * ネストされたリストです
     * サブ項目です

   * こうやって、親のリストを継続することもできます

.. * this is
   * a list

     * with a nested list
     * and some subitems

   * and here the parent list continues

.. Definition (:duref:`ref <definition-lists>`) lists are created as follows::

      term (up to a line of text)
         Definition of the term, which must be indented

         and can even consist of multiple paragraphs

      next term
         Description.

定義リスト(:duref:`ref <definition-lists>`)は以下のようにして作成します::

   用語 (行末までが用語です)
      用語の定義です。定義はインデントする必要があります。

      空白行で区切ることで、定義に複数のパラグラフを書くことができます。

   次の用語
      説明


.. Note that the term cannot have more than one line of text.

用語のテキストは複数行書くことができないことに注意してください。
 
.. Quoted paragraphs (:duref:`ref <block-quotes>`) are created by just indenting
   them more than the surrounding paragraphs.

引用パラグラフ(:duref:`ref <block-quotes>`)は周囲のパラグラフよりもインデントすることで作成できます。

.. Line blocks (:duref:`ref <line-blocks>`) are a way of preserving line breaks::

   | These lines are
   | broken exactly like in
   | the source file.

ラインブロック(:duref:`ref <line-blocks>`)を利用すると、改行状態をそのまま維持したまま出力できます::

   | これらの行は、
   | ソースファイルと同じように
   | 改行されます。

.. There are also several more special blocks available:

次のような特別なブロックも利用できます:

.. * field lists (:duref:`ref <field-lists>`)
   * option lists (:duref:`ref <option-lists>`)
   * quoted literal blocks (:duref:`ref <quoted-literal-blocks>`)
   * doctest blocks (:duref:`ref <doctest-blocks>`)

* フィールドリスト (:duref:`ref <field-lists>`)
* オプションリスト (:duref:`ref <option-lists>`)
* 引用リテラルブロック (:duref:`ref <quoted-literal-blocks>`)
* doctestブロック (:duref:`ref <doctest-blocks>`)
 
.. Source Code
   -----------

ソースコード
------------

.. Literal code blocks (:duref:`ref <literal-blocks>`) are introduced by ending a
   paragraph with the special marker ``::``.  The literal block must be indented
   (and, like all paragraphs, separated from the surrounding ones by blank lines)::


リテラルコードブロック(:duref:`ref <literal-blocks>`)は、前の段落の行末を特別な記号 ``::`` にすることで開始することができます。リテラルコードブロックはインデントする必要があります。また、他のパラグラフ同様、空白行で前後をかこう必要があります::

   これは通常のテキストのパラグラフです。次のパラグラフはコードサンプルです::

      この中はreSTで処理されません。そのまま出力されます。
      ただし、コードブロックのインデントだけは削除されます。

      複数行記述することもできます。

   ここからは通常のテキストのパラグラフに戻ります。

.. This is a normal text paragraph. The next paragraph is a code sample::

      It is not processed in any way, except
      that the indentation is removed.

      It can span multiple lines.

   This is a normal text paragraph again.

.. The handling of the ``::`` marker is smart:

``::`` マーカーの扱いはとてもスマートです:

* もしマーカーがリテラルコードブロックのパラグラフの中に出てきた場合には、そのパラグラフは完全にそのままドキュメント中に残されます。
* もしもマーカーの前がホワイトスペースだった場合には、マーカー自身は非表示になります。
* もしもマーカーの前がホワイトスペース以外だった場合には、コロン(:)1つだけが表示されます。

.. * If it occurs as a paragraph of its own, that paragraph is completely left
     out of the document.
   * If it is preceded by whitespace, the marker is removed.
   * If it is preceded by non-whitespace, the marker is replaced by a single
  colon.

.. That way, the second sentence in the above example's first paragraph would be
   rendered as "The next paragraph is a code sample:".

3つ目のルールが適用されるため、上記のサンプルの最初の段落中の２つめの文をレンダリングすると、 "次のパラグラフはコードサンプルです:" という表記になります。

.. _rst-tables:

.. Tables
   ------

テーブル
--------

.. Two forms of tables are supported.  For *grid tables* (:duref:`ref
   <grid-tables>`), you have to "paint" the cell grid yourself.  They look like
   this:

テーブルの表現方法には2通りあります。 **グリッドテーブル** (:duref:`ref <grid-tables>`)は、セルのグリッドを自分で線描する必要があります。これは次のようになります::

   +------------------------+------------+----------+----------+
   | Header row, column 1   | Header 2   | Header 3 | Header 4 |
   | (header rows optional) |            |          |          |
   +========================+============+==========+==========+
   | body row 1, column 1   | column 2   | column 3 | column 4 |
   +------------------------+------------+----------+----------+
   | body row 2             | ...        | ...      |          |
   +------------------------+------------+----------+----------+

.. *Simple tables* (:duref:`ref <simple-tables>`) are easier to write, but
   limited: they must contain more than one row, and the first column cannot
   contain multiple lines.  They look like this:

**シンプルテーブル** (:duref:`ref <simple-tables>`)はより書くのが簡単な方法ですが、制限があります。1つ以上の列を含み、最初のカラムには複数行のテキストを書くことができません。次のように表現されます::

   =====  =====  =======
   A      B      A and B
   =====  =====  =======
   False  False  False
   True   False  False
   False  True   False
   True   True   True
   =====  =====  =======


.. Hyperlinks
   ----------

ハイパーリンク
--------------

.. External links
.. ^^^^^^^^^^^^^^

外部リンク
^^^^^^^^^^

.. Use ```Link text <http://example.com>`_`` for inline web links.  If the link 
   text should be the web address, you don't need special markup at all, the parser
   finds links and mail addresses in ordinary text.

```リンクテキスト <http://ターゲットURL>`_`` という書くことで、外部のウェブサイトへのリンクを埋め込むことができます。もしリンクテキストがウェブのアドレスである場合には、特別なマークアップは必要ありません。パーサーが通常のテキスト中でリンクか、メールアドレスを見つけると、そのままそれにリンクを埋め込んでくれます。

.. You can also separate the link and the target definition (:duref:`ref
   <hyperlink-targets>`), like this::

      This is a paragraph that contains `a link`_.

      .. _a link: http://example.com/

次のようにして、ターゲット定義(:duref:`ref <hyperlink-target>`)と、リンクを分割することもできます::

   このパラグラフは `リンク`_ を含みます。

   .. _リンク: http://example.com

.. Internal links
   ^^^^^^^^^^^^^^

内部リンク
^^^^^^^^^^

.. Internal linking is done via a special reST role provided by Sphinx, see the
   section on specific markup, :ref:`ref-role`.

内部リンクはSphinxの提供する、特別なreSTのロールを通じて行われます。詳しくは、特別なマークアップ :ref:`ref-role` のセクションを見てください。

.. Sections
   --------

セクション
----------

.. Section headers (:duref:`ref <sections>`) are created by underlining (and 
   optionally overlining) the section title with a punctuation character, at least 
   as long as the text::

セクションのヘッダ(:duref:`ref <sections>`)は、セクションのタイトルを句読点などの記号の文字でアンダーラインを引くことで設定します。必要に応じてでオーバーラインも併用することができます。アンダーラインはテキストと同じか、それ以上の長さにする必要があります::

   ================
   これは見出しです
   ================

.. Normally, there are no heading levels assigned to certain characters as the
   structure is determined from the succession of headings.  However, for the
   Python documentation, this convention is used which you may follow:

通常は、文字の種類と見出しのレベルは関係ないため、どの文字でも使用することができます。使用していない種類のアンダーラインが出てくると、見出しのレベルが一段変わる、というルールになっています。参考までに、Pythonドキュメントで使っている慣例について紹介しておきます

.. * ``#`` with overline, for parts
   * ``*`` with overline, for chapters
   * ``=``, for sections
   * ``-``, for subsections
   * ``^``, for subsubsections
   * ``"``, for paragraphs

* ``#`` 部: オーバーライン付き
* ``*`` 章: オーバーライン付き
* ``=``, セクション
* ``-``, サブセクション
* ``^``, サブサブセクション
* ``"``, パラグラフ

.. Of course, you are free to use your own marker characters (see the reST
   documentation), and use a deeper nesting level, but keep in mind that most
   target formats (HTML, LaTeX) have a limited supported nesting depth.

もちろん、どのようなマークアップ文字を選択しても自由ですし、組み合わせることで、より深い、ネストレベルを使用することもできます。reSTの文章を参照してください。ただし、ほとんどの対象となる出力フォーマット(HTML, LaTeX)は、ネストできる深さには限界が設定されている、ということは忘れないでください。


.. Explicit Markup
   ---------------

明示的なマークアップ
--------------------

.. "Explicit markup" (:duref:`ref <explicit-markup-blocks>`) is used in reST for 
   most constructs that need special handling, such as footnotes, 
   specially-highlighted paragraphs, comments, and generic directives.

"明示的なマークアップ"(:duref:`ref <explicit-markup-blocks>`)というのは、reSTの中では特別な操作の必要な多くの構成要素のために使用されます。例えば脚注や、言語別のハイライトをする特別な段落、コメントや処理系(Sphinx)に対する指示などです。

.. An explicit markup block begins with a line starting with ``..`` followed by
   whitespace and is terminated by the next paragraph at the same level of
   indentation.  (There needs to be a blank line between explicit markup and 
   normal paragraphs.  This may all sound a bit complicated, but it is 
   intuitive enough when you write it.)

明示的なマークアップのブロックは ``..`` で始まる行から始まります。先頭の記号の後ろにはホワイトスペースが一つ入ります。そして、インデントが同じレベルになる次の段落までが１つのブロックとして扱われます。通常のパラグラフと、明示的なマークアップのブロックの間には一行以上のスペースを空ける必要があります。このような説明を聞くとわかりにくいと感じる人も多いと思いますが、実際に自分で書いてみると十分に直感的であるということがわかるでしょう。

.. Directives
   ----------

.. _directives:

ディレクティブ
--------------

.. A directive (:duref:`ref <directives>`) is a generic block of explicit markup.
   Besides roles, it is one of the extension mechanisms of reST, and Sphinx makes 
   heavy use of it.

ディレクティブ(:duref:`ref <directives>`)は汎用の明示的マークアップです。reSTの拡張のためのメカニズムの一つで、ロールが指定されることがあります。Sphinxはこのディレクティブをかなり多用しています。

.. Docutils supports the following directives:

Docutilsは次のようなディレクティブを含みます:

.. * Admonitions: :dudir:`attention`, :dudir:`caution`, :dudir:`danger`,
  :dudir:`error`, :dudir:`hint`, :dudir:`important`, :dudir:`note`,
  :dudir:`tip`, :dudir:`warning` and the generic :dudir:`admonition`.
  (Most themes style only "note" and "warning" specially.)

* 忠告: :dudir:`attention`, :dudir:`caution`, :dudir:`danger`,
  :dudir:`error`, :dudir:`hint`, :dudir:`important`, :dudir:`note`,
  :dudir:`tip`, :dudir:`warning` ,および、一般的な用途の :dudir:`admonition`.
  (ほとんどのテーマは、"note"と"warning"にだけスタイルを適用します)

.. * Images:

     - :dudir:`image` (see also Images_ below)
     - :dudir:`figure` (an image with caption and optional legend)

* イメージ:

  - :dudir:`image` (images_ も参照してください)
  - :dudir:`figure` (キャプション、反例を含むイメージ)

.. * Additional body elements:

  - :dudir:`contents` (a local, i.e. for the current file only, table of
    contents)
  - :dudir:`container` (a container with a custom class, useful to generate an
    outer ``<div>`` in HTML)
  - :dudir:`rubric` (a heading without relation to the document sectioning)
  - :dudir:`topic`, :dudir:`sidebar` (special highlighted body elements)
  - :dudir:`parsed-literal` (literal block that supports inline markup)
  - :dudir:`epigraph` (a block quote with optional attribution line)
  - :dudir:`highlights`, :dudir:`pull-quote` (block quotes with their own
    class attribute)
  - :dudir:`compound` (a compound paragraph)

* 追加の本体要素:

  - :dudir:`contents` (現在のファイル内だけの目次)
  - :dudir:`container` (カスタムのクラスを付加できるコンテナ。HTMLで外部の ``<div>`` を生成するのに便利)
  - :dudir:`rubric` (ドキュメントのセクションと関係のない見出し)
  - :dudir:`topic`, :dudir:`sidebar` (特別に強調されたなボディ要素)
  - :dudir:`parsed-literal` (インラインマークアップをサポートしたリテラルブロック)
  - :dudir:`epigraph` (追加の属性行を付加できるブロック引用)
  - :dudir:`highlights`, :dudir:`pull-quote` (特有のクラス属性を持つブロック引用)
  - :dudir:`compound` (複合パラグラフ)

.. * Special tables:

  - :dudir:`table` (a table with title)
  - :dudir:`csv-table` (a table generated from comma-separated values)
  - :dudir:`list-table` (a table generated from a list of lists)

* 特別なテーブル:

  - :dudir:`table` (タイトル付きのテーブル)
  - :dudir:`csv-table` (カンマ区切りの値からテーブル生成)
  - :dudir:`list-table` (リストのリストからテーブル生成)

.. * Special directives:

  - :dudir:`raw` (include raw target-format markup)
  - :dudir:`include` (include reStructuredText from another file)
    -- in Sphinx, when given an absolute include file path, this directive takes
    it as relative to the source directory
  - :dudir:`class` (assign a class attribute to the next element) [1]_

* 特別なディレクティブ:

  - :dudir:`raw` (ターゲットの書式のマークアップを挿入)
  - :dudir:`include` (他のファイルからreStructuredTextを取り込み)
    -- Sphinxでは、絶対パスが指定されると、ソースディレクトリからの相対パスが利用されます。
  - :dudir:`class` (次の要素へのクラス属性の設定) [1]_

.. * HTML specifics:

  - :dudir:`meta` (generation of HTML ``<meta>`` tags)
  - :dudir:`title` (override document title)

* HTML定義

  - :dudir:`meta` (HTMLの ``<meta>`` タグの生成)
  - :dudir:`title` (ドキュメントのタイトルの上書き)

.. * Influencing markup:

  - :dudir:`default-role` (set a new default role)
  - :dudir:`role` (create a new role)

  Since these are only per-file, better use Sphinx' facilities for setting the
  :confval:`default_role`.

* 疑似命令マークアップ:

  - :dudir:`default-role` (デフォルトのロールをセット)
  - :dudir:`role` (新しいロールの作成)

  これらのマークアップの影響範囲は、そのマークアップが書かれたファイルだけに限定されるため、Sphinxが提供する :confval:`default_role` を設定する方が良いでしょう。

.. Do *not* use the directives :dudir:`sectnum`, :dudir:`header` and
   :dudir:`footer`.

:dudir:`sectnum`, :dudir:`header`, :dudir:`footer` の3つのディレクティブは使用 **しない** で下さい。

.. Directives added by Sphinx are described in :ref:`sphinxmarkup`.

Sphinxによって追加されたディレクティブに関しては :ref:`sphinxmarkup` を参照してください。
 
.. Basically, a directive consists of a name, arguments, options and content. 
   (Keep this terminology in mind, it is used in the next chapter describing 
   custom directives.)  Looking at this example, ::

   .. function:: foo(x)
                 foo(y, z)
      :module: some.module.name

      Return a line of text input from the user.

基本的に、ディレクティブは名前、引数、オプション、コンテンツなどで構成されています。これらの用語を覚えておいてください。これらは次の章でカスタムディレクティブの紹介を行う際に利用します。以下にサンプルを示します::

   .. function:: foo(x)
                 foo(y, z)
      :module: some.module.name

      ユーザから入力されたテキストのうち、１行を返します。

.. ``function`` is the directive name.  It is given two arguments here, the
   remainder of the first line and the second line, as well as one option 
   ``module`` (as you can see, options are given in the lines immediately following 
   the arguments and indicated by the colons). Options must be indented to the
   same level as the directive content.


``function`` がディレクティブの名前です。ここでは二つの引数が与えられています。1行目の残りの部分と、2行目が引数です。そして1つのオプション ``module`` も同様に設定されています。見ての通り、オプションは引数のある行のすぐ次の行に書かれていています。そして、目印としてコロンが付いています。オプションは、ディレクティブのコンテンツと同じインデントの高さにします。

.. The directive content follows after a blank line and is indented relative 
   to the directive start.

ディレクティブのコンテンツというのは、空白行の後に続くブロックで、ディレクティブが開始された地点よりも深いインデントでくくられています。

.. Images
   ------

.. _images:

画像
--------

.. reST supports an image directive(:dudir:`ref <image>`), used like so

   .. image:: gnu.png
      (options)


reSTは画像に関するディレクティブ(:dudir:`ref <image>`)もサポートしています。以下のように使用します。::

   .. image:: gnu.png
      (オプション)

.. When used within Sphinx, the file name given (here ``gnu.png``) must either be
   relative to the source file, or absolute which means that they are relative to
   the top source directory.  For example, the file ``sketch/spam.rst`` could refer
   to the image ``images/spam.png`` as ``../images/spam.png`` or
   ``/images/spam.png``.

Sphinx内で使用する場合には、ソースファイルからの相対パスか、トップのソースディレクトリからの絶対パスでファイル名(ここでは ``gnu.png``)を指定します。例えば、 ``sketch/spam.rst`` というソースファイルからは、 ``images/spam.png``, ``../images/spam.png``, ``/images/spam.png`` というように書くことができます。

.. Sphinx will automatically copy image files over to a subdirectory of the output
   directory on building (e.g. the ``_static`` directory for HTML output.)

このディレクティブを使用すると、Sphinxはビルド時に、指定された画像ファイルを出力ディレクトリのサブディレクトリにコピーします。HTML出力の場合には、 ``_static`` といったディレクトリにコピーされます。

.. Interpretation of image size options (``width`` and ``height``) is as follows:
   if the size has no unit or the unit is pixels, the given size will only be
   respected for output channels that support pixels (i.e. not in LaTeX output).
   Other units (like ``pt`` for points) will be used for HTML and LaTeX output.

イメージサイズに関するオプション(``width`` と ``height``)は以下のように解釈されます。もし単位が無い、もしくは単位がpixelsの場合には、与えられたサイズは出力するチャンネルがピクセルをサポートしているかどうかだけが考慮されます。例えば、LaTeX出力はこれをサポートしていません。他の単位(ポイントを表す ``pt`` など)はHTMLでもLaTeXでも使用されます。

.. Sphinx extends the standard docutils behavior by allowing an asterisk for the
   extension::

Sphinxは標準のdocutilsを拡張していて、拡張子としてアスタリスク(*)を受け取れるようになっています::

   .. image:: gnu.*

.. Sphinx then searches for all images matching the provided pattern and determines
   their type.  Each builder then chooses the best image out of these candidates.
   For instance, if the file name ``gnu.*`` was given and two files :file:`gnu.pdf`
   and :file:`gnu.png` existed in the source tree, the LaTeX builder would choose
   the former, while the HTML builder would prefer the latter.

アスタリスクが指定されると、Sphinxは指定されたパターンにマッチするすべての画像フォーマットを検索して、使用するタイプを決定します。それぞれのビルダーは、候補となるベストのイメージを選択します。 ``gnu.*`` にマッチするファイル名として、 :file:`gnu.pdf` と、 :file:`gnu.png` がソースツリーの中に存在していたとします。LaTeXビルダーは前者のPDFを、HTMLビルダーは後者のPNGを優先的に利用します。

.. .. versionchanged:: 0.4
   Added the support for file names ending in an asterisk.

.. versionchanged:: 0.4
   ファイル名の末尾をアスタリスク(*)にできる機能が追加されました。

.. .. versionchanged:: 0.6
   Image paths can now be absolute.

.. versionchanged:: 0.6
   イメージパスとして、ソースフォルダのルートからの絶対パスが指定できるようになりました。

.. Footnotes
   ---------

脚注
----

.. For footnotes(:duref:`ref <footnotes>`), use ``[#name]_`` to mark the footnote 
   location, and add the footnote body at the bottom of the document after a 
   "Footnotes" rubric heading, like so::

   Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

   .. rubric:: Footnotes

   .. [#f1] Text of the first footnote.
   .. [#f2] Text of the second footnote.

脚注(:duref:`ref <footnotes>`)を作成するためには、脚注を書きたい場所で ``[#name]_`` というマークアップを書きます。そして、脚注の本体をドキュメントの下の方の "脚注" のためのrubric見出しの中に書きます::

   Lorem ipsum [#f1]_ dolor sit amet	      ... [#f2]_

   .. rubric:: 脚注

   .. [#f1] 最初の脚注のテキストです。
   .. [#f2] ２番目の脚注のテキストです。

.. You can also explicitly number the footnotes (``[1]_``) or use auto-numbered
   footnotes without names (``[#]_``).

脚注の数値を明示的に指定(``[1]_``)することもできますし、名前を指定しないで脚注の自動採番(``[#]``)をさせることも可能です。


.. Citations
   ---------

引用
----

.. Standard reST citations (:duref:`ref <citations>`) are supported, with the 
   additional feature that they are "global", i.e. all citations can be referenced 
   from all files. Use them like so:

   Lorem ipsum [Ref]_ dolor sit amet.

   .. [Ref] Book or article reference, URL or whatever.

標準のreSTでも引用(:duref:`ref <citations>`)はサポートしていますが、Sphinx独自の追加の機能としては、引用が"グローバル"ということです。そのため、全ての引用はすべてのファイルから参照することができます。以下のように使用します::

   Lorem ipsum [Ref]_ dolor sit amet.

   .. [Ref] 参考になった書籍、論文、URL、その他

.. Citation usage is similar to footnote usage, but with a label that is not
   numeric or begins with ``#``.

引用は、脚注と同じように使用できますが、ラベルは数字ではありませんし、 ``#`` でも始まりません。


.. Substitutions
   -------------

置換
----

.. reST supports "substitutions" (:duref:`ref <substitution-definitions>`), which 
   are pieces of text and/or markup referred to in the text by ``|name|``.  They 
   are defined like footnotes with explicit markup blocks, like this::

   .. |name| replace:: replacement *text*

reSTは"置換"(:duref:`ref <substitution-definitions>`)をサポートしています。これは、テキスト中の ``|名前|`` で指定された箇所に、テキストや、マークアップを挿入します。脚注と同じように明示的なマークアップブロックを使って定義します::

   .. |name| replace:: リプレースされる *テキスト*

.. or this::

   .. |caution| image:: warning.png
                :alt: Warning!

もしくはこのように書きます::

   .. |caution| image:: warning.png
                :alt: 警告!

.. See the :duref:`reST reference for substitutions <substitution-definitions>`
   for details.

詳しくは `reSTリファレンスの置換の説明 <substitution-definitions>`_ を参照してください。

.. If you want to use some substitutions for all documents, put them into
   :confval:`rst_prolog` or put them into a separate file and include it into all 
   documents you want to use them in, using the :rst:dir:`include` directive.  (Be 
   sure to give the include file a file name extension differing from that of other 
   source files, to avoid Sphinx finding it as a standalone document.)

いくつかの置換をすべてのドキュメントで使用したい場合には、置換の宣言を別のファイルに切り出して、 :confval:`rst_prolog` に書くか、その置換を行いたいすべてのドキュメントの冒頭で :rst:dir:`include` ディレクティブを使用してインクルードする方法があります。この場合は、他のソースファイルとは別の拡張子を付けるようにしましょう。同じ拡張子にすると、Sphinxはリンクされていないドキュメントとして警告を出力してしまいます。

.. Sphinx defines some default substitutions, see :ref:`default-substitutions`.

Sphinxはデフォルトの置換をいくつか定義しています。詳しくは :ref:`default-substitutions` を参照してください。


.. Comments
.. --------

コメント
--------

.. Every explicit markup block which isn't a valid markup construct (like the
   footnotes above) is regarded as a comment (:duref:`ref <comments>`). For example::

   .. This is a comment.

上記の脚注のような適切な構造をしていない明示的マークアップのブロックはすべてコメント(:duref:`ref <comments>`)とみなされます::

   .. これはコメントです。

.. You can indent text after a comment start to form multiline comments::

   ..
      This whole indented block
      is a comment.

      Still in the comment.

コメントがスタートした行からインデントすることによって、複数行コメントにすることができます::

   ..
      このインデントされたブロック
      全体がコメントです

      この行もまだコメントです

.. Source encoding
   ---------------

ソースエンコーディング
----------------------

.. Since the easiest way to include special characters like em dashes or copyright
   signs in reST is to directly write them as Unicode characters, one has to
   specify an encoding.  Sphinx assumes source files to be encoded in UTF-8 by
   default; you can change this with the :confval:`source_encoding` config value.

エムダッシュ(アルファベットのMと同じ幅を持つダッシュ)や、コピーライトの記号などの特殊記号をreSTに入れる場合にはユニコードの文字として直接入れるのが一番簡単な方法です。Sphinxはデフォルトでは、UTF-8であるとみないしてソースコードを読み込みます。 :confval:`source_encoding` の設定値を変更することで、このデフォルトのエンコーディングを変更することができます。

.. Gotchas
   -------

分かっていること
----------------

.. There are some problems one commonly runs into while authoring reST documents:

reSTのドキュメントを書いていると、良く遭遇する問題がいくつかあります:

.. * **Separation of inline markup:** As said above, inline markup spans must be
     backslash-escaped space to get around that.  See `the reference
     <http://docutils.sf.net/docs/ref/rst/restructuredtext.html#inline-markup>`_
     for the details.

* **インラインマークアップの分離:** 上記の説明でも触れていますが、インラインマークアップを付ける領域の前後はテキスト以外の文字(スペース、カッコなど)や、バックスラッシュ(日本語フォントだと円記号)でエスケープしたスペースでくくる必要があります。詳しくは、 `the reference <http://docutils.sf.net/docs/ref/rst/restructuredtext.html#inline-markup>`_ を参照してください。

.. * **No nested inline markup:** Something like ``*see :func:`foo`*`` is not
     possible.

* **インラインマークアップのネストはできない:** ``*:func:`foo`* 参照`` といった書き方はできません。


.. .. rubric:: Footnotes

   .. [1] When the default domain contains a :rst:dir:`class` directive, this directive
          will be shadowed.  Therefore, Sphinx re-exports it as :rst:dir:`rst-class`.

.. rubric:: 脚注
.. [1] デフォルトドメインに :rst:dir:`class` ディレクティブが存在するため、このディレクティブはそのままでは使用することができません。そのため、Sphinxでは、 :rst:dir:`rst-class` という名前で再定義しています。

