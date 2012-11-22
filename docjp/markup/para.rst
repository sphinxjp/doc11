.. highlight:: rest

.. Paragraph-level markup

パラグラフ階層のマークアップ
----------------------------

.. index:: note, warning
        pair: changes; in version

.. These directives create short paragraphs and can be used inside information 
   units as well as normal text:

これらのディレクティブは短いパラグラフ(段落)を作成します。通常のテキスト同様、情報の固まりに対して使用できます。

.. rst:directive:: .. note::

   .. An especially important bit of information about an API that a user should be 
      aware of when using whatever bit of API the note pertains to.  The content of 
      the directive should be written in complete sentences and include all 
      appropriate punctuation.

　 特別に重要な情報が少しだけある場合に使用します。APIを使用する際に、ユーザが気をつけなければならないことの説明をする場合などに使うと良いでしょう。このディレクティブの中身には、適切に句読点が付いた、完全な文章を書くべきです。

   .. Example:

      .. note::
         This function is not suitable for sending spam e-mails.

   サンプル::

      .. note::
         この関数はspamの電子メールを送付するには適しません。



.. rst:directive:: .. warning::

   .. An important bit of information about an API that a user should be very aware 
      of when using whatever bit of API the warning pertains to.  The content of 
      the directive should be written in complete sentences and include all 
      appropriate punctuation. This differs from :rst:dir:`note` in that it is 
      recommended over :rst:dir:`note` for information regarding security.

   noteよりも重要な情報があり、APIを使用する際に、気をつけなければならない警告情報をユーザに伝えるために使用するのに適しています。このディレクティブの中身には、適切に句読点が付いた、完全な文章を書くべきです。 :rst:dir:`note` との違いで言えば、セキュリティに関する情報は :rst:dir:`note` よりもこのディレクティブを使用する方が良いでしょう。


.. 
   .. rst:directive:: .. versionadded:: version

.. rst:directive:: .. versionadded:: バージョン

   .. This directive documents the version of the project which added the 
      described feature to the library or C API. When this applies to an 
      entire module, it should be placed at the top of the module section 
      before any prose.

   このディレクティブは説明している機能がライブラリ、もしくはC APIに追加された時のプロジェクトのバージョンについて記述するのに使用します。このディレクティブがモジュール全体に対して適用する場合には、モジュールセクションの先頭の、文章が始まる前の位置に置くべきです。

   .. The first argument must be given and is the version in question; you 
      can add a second argument consisting of a *brief* explanation of the change.

   最初の引数は必須で、バージョン番号を書く必要があります。2番目の引数も追加することができ、変化に対する *短い* 説明を書くことができます。

   .. Example
      .. versionadded:: 2.5
         The *spam* parameter.

   サンプル::

      .. versionadded:: 2.5
         *spam* パラメータ

   .. Note that there must be no blank line between the directive head and 
      the explanation; this is to make these blocks visually continuous in 
      the markup.

   ディレクティブヘッドと説明の間には空行を入れてはいけません。マークアップの中では見た目上つながっているようにしなければなりません。


.. 
   .. rst:directive:: .. versionchanged:: version

.. rst:directive:: .. versionchanged:: バージョン

   .. Similar to :rst:dir:`versionadded`, but describes when and what changed in 
      the named feature in some way (new parameters, changed side effects, etc.).

   :rst:dir:`versionadded` と似ていますが、現在説明している機能がいつどのように変化したのか(新しい引数、副作用の変更など)を説明するのに使用します。


.. 
   rst:directive:: .. deprecated:: version

.. rst:directive:: .. deprecated:: バージョン

   .. Similar to :rst:dir:`versionchanged`, but describes when the feature was
      deprecated.  An explanation can also be given, for example to inform the
      reader what should be used instead.  Example::

      .. deprecated:: 3.1
         Use :func:`spam` instead.

   
   :rst:dir:`versionchanged` と似ていますが、このディレクティブは、この機能がすでに古くて非推奨になったことを示しています。代替として、今後何を使っていくべきなのかといった説明文を付けることができます::

      .. deprecated:: 3.1
         今後は代わりに :func:`spam` を使用すること

--------------

.. rst:directive:: .. seealso::

   .. Many sections include a list of references to module documentation or 
      external documents.  These lists are created using the :rst:dir:`seealso` 
      directive.

   多くのセクションがモジュールのドキュメントへの参照やが、外部ドキュメントへの参照を含む場合、このようなリストは :rst:dir:`seealso` ディレクティブを使用して作ることができます。

   .. The :rst:dir:`seealso` directive is typically placed in a section just before any 
      sub-sections.  For the HTML output, it is shown boxed off from the main flow 
      of the text.

   :rst:dir:`seealso` ディレクティブはサブセクションの直前のセクションに置かれることが多いです。HTMLアウトプットにおいては、メインのテキストの流れから離されて、箱に囲まれて表示されます。

   .. The content of the :rst:dir:`seealso` directive should be a reST definition list.
   .. Example:

      .. seealso::

         Module :py:mod:`zipfile`
            Documentation of the :py:mod:`zipfile` standard module.

         `GNU tar manual, Basic Tar Format <http://link>`_
            Documentation for tar archive files, including GNU tar extensions.

   :rst:dir:`seealso` の中身は、reSTの定義リストを使用しなければなりません。
   サンプル::

      .. seealso::

         Module :py:mod:`zipfile`
            標準モジュールの :py:mod:`zipfile` のドキュメント。

         `GNU tar マニュアル, 基本Tarフォーマット <http://link>`_
            GNUによるtar拡張も含む、tarアーカイブファイルのドキュメント。

   .. There's also a "short form" allowed that looks like this::

      .. seealso:: modules :py:mod:`zipfile`, :mod:`tarfile`

   "短縮形"の書き方もサポートされており、以下のように書くことができます::

      .. seealso:: modules :py:mod:`zipfile`, :py:mod:`tarfile`

   .. 
      .. versionadded:: 0.5
         The short form.

   .. versionadded:: 0.5
      短縮形の追加


.. 
   .. rst:directive:: .. rubric:: title

.. rst:directive:: .. rubric:: タイトル

   .. This directive creates a paragraph heading that is not used to create a
      table of contents node.

   このディレクティブは、目次に表示されないパラグラフの見出しを作成します。(訳注:rubricは注釈の意味です)

   .. note::

      .. If the *title* of the rubric is "Footnotes" (or the selected language's
         equivalent), this rubric is ignored by the LaTeX writer, since it is 
         assumed to only contain footnote definitions and therefore would create an 
         empty heading.

      もし rubricディレクティブの *タイトル* が"Footnotes"(もしくは選択された言語で指定されている、同様の言葉)だった場合には、脚注の定義だけが含まれていると見なして、LaTeXライターでは無視されます。この場合は空の見出しだけが作成されます。


.. rst:directive:: centered

   .. This directive creates a centered boldfaced line of text.  Use it as 
      follows:

      .. centered:: LICENSE AGREEMENT

   このディレクティブはセンターに置かれた、太字のテキストを作成するのに使用します。以下のように使用されます::

      .. centered:: ラインセンス契約

   .. deprecated:: 1.1

      この表現のみのディレクティブはレガシーなディレクティブになりますので、今後は、 :rst:dir:`rst-class` ディレクティブを代わりに使い、適切なスタイルを与えてください。

      .. This presentation-only directive is a legacy from older versions.  Use a
         :rst:dir:`rst-class` directive instead and add an appropriate style.

.. rst:directive:: hlist

   このディレクティブは短い文章のリストを含みます。このディレクティブは、水平にも数カラム展開することで、よりコンパクトなリストに変換するか、アイテム間のスペースを小さくします。どちらになるかはビルダー次第です。

   水平に展開する機能をサポートしたビルダーでは、 ``columns`` オプションを使用して、水平のカラム数の設定をすることができます。デフォルトでは2になっています。サンプルを示します::

      .. hlist::
         :columns: 3

         * このリストの
         * 短い項目は
         * 表示するときに
         * 水平に
         * 表示されるべきです。

   .. versionadded:: 0.6

..   This directive must contain a bullet list.  It will transform it into a more compact list by either distributing more than one item horizontally, or reducing spacing between items, depending on the builder.

..   For builders that support the horizontal distribution, there is a ``columns`` option that specifies the number of columns; it defaults to 2.  Example

..         * A list of
..         * short items
..         * that should be
..         * displayed
..         * horizontally


.. Table-of-contents markup

目次のマークアップ
------------------

.. The :rst:dir:`toctree` directive, which generates tables of contents of 
   subdocuments, is described in :ref:`toctree-directive`.

サブドキュメントの目次を作る :rst:dir:`toctree` ディレクティブに関しては :ref:`toctree-directive` のドキュメントを読んでください。

.. For local tables of contents, use the standard reST :dudir:`contents directive 
   <contents>`.

ローカルな目次を作成する場合には、標準reSTの :dudir:`contentsディレクティブ <contents>` ディレクティブを使用してください。

.. Index-generating markup


.. Glossary

用語集
------

.. rst:directive:: .. glossary::

   .. This directive must contain a reST definition list with terms and 
      definitions.  The definitions will then be referencable with the :rst:role:`term` 
      role.  

   .. This directive must contain a reST definition-list-like markup with terms and
      definitions.  The definitions will then be referencable with the
      :rst:role:`term` role.  Example:

      .. glossary::

         environment
            A structure where information about all documents under the root is 
            saved, and used for cross-referencing.  The environment is pickled 
            after the parsing stage, so that successive runs only need to read 
            and parse new and changed documents.

         source directory
            The directory which, including its subdirectories, contains all 
            source files for one Sphinx project.

   どのディレクティブは、用語と定義が一緒になった、マークアップのようなreST定義リストを含みます。定義は :rst:role:`term` というロールを利用することで参照が可能になります。
   サンプル::

      .. glossary::

         環境
            ルート以下のすべてのドキュメントの情報が格納される場所です。この情報は
            クロスリファレンスを作成する際に利用されます。この環境には、パース段階の
            後の結果のpickleされたものが入ります。ソースファイルが新規で作成されたり、
            変更されて、読み込んだりパースしたりする必要がない限りはこの中のデータが
            更新されることはありません。
   
         ソースディレクトリ
            ひとつのSphinxプロジェクトにおいて、すべてのソースファイルを含むディレクトリ。
            このディレクトリ直下だけではなく、サブディレクトリを使用してソースファイルを
            分類して入れておくことも可能です。

   .. In contrast to regular definition lists, *multiple* terms per entry are
      allowed, and inline markup is allowed in terms.  You can link to all of the
      terms.  For example:

      .. glossary::

         term 1
         term 2
            Definition of both terms.

      (When the glossary is sorted, the first term determines the sort order.)

   通常の定義リストとは異なり、一つのエントリーに対して、複数の用語を定義することができます。それぞれの用語に対してインラインマークアップを使うことができます。また、すべての用語への参照も可能です::

      .. glossary::

         用語1
         用語2
            両方の単語の定義

   .. versionadded:: 0.6
      glossaryディレクティブに ``:sorted:`` というフラッグを与えることができるようになりました。これを指定すると、自動的にエントリーをアルファベット順に並べることができます。

      .. You can now give the glossary directive a ``:sorted:`` flag that will
         automatically sort the entries alphabetically.

   .. versionchanged:: 1.1
 
      複数用語の定義と、用語に対するインラインマークアップが可能になりました。
      
      .. Now supports multiple terms and inline markup in terms.



.. Grammar production displays


文法規則表示
------------

(訳注: grammar productionを文法規則と意訳してます)

.. Special markup is available for displaying the productions of a formal grammar. The markup is simple and does not attempt to model all aspects of BNF (or any derived forms), but provides enough to allow context-free grammars to be displayed in a way that causes uses of a symbol to be rendered as hyperlinks to the definition of the symbol.  There is this directive:

形式がきちんとした文法の規則を表示するための特別なマークアップを利用することができます。マークアップはシンプルに作られています。その代わりに、BNFや、BNFの派生の記法をすべてのモデル化することは目標とされていませんが、文脈自由文法を表現するには十分な機能を持っていて、シンボルを書くと、定義にリンクが張られるようにレンダリングされます。以下のディレクティブがあります:

..
   .. rst:directive:: .. productionlist:: [name]

.. rst:directive:: .. productionlist:: [名前]

   .. This directive is used to enclose a group of productions.  Each production is 
      given on a single line and consists of a name, separated by a colon from the 
      following definition. If the definition spans multiple lines, each 
      continuation line must begin with a colon placed at the same column as in the 
      first line.

   このディレクティブは文法の規則を表現するためのものです。それぞれの規則は一行で表現され、コロン(:)の前が名前で、その後ろが定義になります。定義を複数行で書くこともできますが、この場合は、それぞれの定義の行の先頭に、最初の行と同じ高さにそろえてコロンを書く必要があります。

   .. The argument to :rst:dir:`productionlist` serves to distinguish different sets of
      production lists that belong to different grammars.

   :rst:dir:`productionlist` に与える名前によって、異なる文法に属する、異なる規則セットのグループと区別することができるようになります。

   .. Blank lines are not allowed within ``productionlist`` directive arguments.

   ディレクティブの引数の ``規則リスト`` の中には空行を入れることはできません。

   .. The definition can contain token names which are marked as interpreted text 
      (e.g. ``sum ::= `integer` "+" `integer```) -- this generates cross-references 
      to the productions of these tokens.  Outside of the production list, you can
      reference to token productions using :rst:role:`token`.

   定義には解釈済みのテキストとしてマークされたトークン名を含むことができます。これらのトークンの規則との間にクロスリファレンスが生成されます。(例 ``sum ::= `integer` "+" `integer```) 文法規則のリストその外では、 :rst:role:`token` ロールを使って、文法への参照を取ることができます。

   .. Note that no further reST parsing is done in the production, so that you 
      don't have to escape ``*`` or ``|`` characters.

   規則の中ではreSTパーサは動作しないため、 ``*`` や、 ``|`` といった文字をエスケープすることはできません。

.. The following is an example taken from the Python Reference Manual:

次のサンプルは、Pythonのリファレンスマニュアルにあった構文をSphinxで表現したものです::

   .. productionlist::
      try_stmt: try1_stmt | try2_stmt
      try1_stmt: "try" ":" `suite`
               : ("except" [`expression` ["," `target`]] ":" `suite`)+
               : ["else" ":" `suite`]
               : ["finally" ":" `suite`]
      try2_stmt: "try" ":" `suite`
               : "finally" ":" `suite`







