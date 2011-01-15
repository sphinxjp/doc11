.. _faq:

Sphinx FAQ
==========

.. This is a list of Frequently Asked Questions about Sphinx.  Feel free to
   suggest new entries!

このセクションでは、Sphinxについてよく聞かれる質問とその答えについてまとめています。新しいセクションを気軽に追加してください！

.. How do I...
   -----------

どのようにすれば...
-------------------

.. ... create PDF files without LaTeX?
       You can use `rst2pdf <http://rst2pdf.googlecode.com>`_ version 0.12 or greater
       which comes with built-in Sphinx integration.  See the :ref:`builders`
       section for details.

... LaTeXなしでPDFファイルを作成できますか？
    Sphinx統合機能が組み込まれている、 `rst2pdf <http://rst2pdf.googlecode.com>`_ のバージョン 0.12以降を使用することができます。詳細は、 :ref:`builders` のセクションをご覧下さい。

.. ... get section numbers?
       They are automatic in LaTeX output; for HTML, give a ``:numbered:`` option to
       the :dir:`toctree` directive where you want to start numbering.

... セクション番号を設定できますか？
   LaTeX出力では自動的に設定されます。HTML出力では、 :rst:dir:`toctree` ディレクティブに対して、ナンバリングをしたい位置に対して ``:numbered:`` オプションを付けると、設定することができます。

.. ... customize the look of the built HTML files?
       Use themes, see :doc:`theming`.

... ビルドするHTMLファイルの見た目をカスタマイズできますか？
   :doc:`theming` を読んで、テーマを利用すると、カスタマイズすることができます。

.. ... add global substitutions or includes?
       Add them in the :confval:`rst_epilog` config value.

... すべてのドキュメントで置換を行ったり、インクルードできますか？
   これらの定義を :confval:`rst_epilog` コンフィグ値を使って行ってください。

.. ... display the whole TOC tree in the sidebar?
    Use the :data:`toctree` callable in a custom layout template, probably in the
    ``sidebartoc`` block.

... すべての全体の目次をサイドバーに表示できますか？
    おそらく、 ``sidebartoc`` ブロックに、と想像しますが、カスタムのレイアウトテンプレートの中で、 :data:`toctree` を呼び出して使用することが可能です。

.. ... write my own extension?
       See the :ref:`extension tutorial <exttut>`.

... 自分用のSphinx拡張を作成できますか？
    :ref:`Sphinx拡張チュートリアル <exttut>` をご覧ください。

.. ... convert from my existing docs using MoinMoin markup?
       The easiest way is to convert to xhtml, then convert `xhtml to reST`_.  You'll
       still need to mark up classes and such, but the headings and code examples
       come through cleanly.

... MoinMoinというWikiのマークアップで書かれた既存のドキュメントから変換できますか？
    一番簡単の方法としてはレンダリング済みの `xhtmlからreST`_ に変換する方法でしょう。 
    見出しやコード例などがうまく変換できたとしても、クラスなどのマークアップはしなおす必要があるでしょう。

.. Using Sphinx with...
   --------------------

.. _usingwith:

Sphinxと一緒に ... を使うには？
-------------------------------

Epydoc
   `API ロール`_ を提供するサードパーティ製の拡張機能があります。このロールは、与えられた識別子を持つ要素のEpydocのAPIドキュメントへの参照を行うことができます。

.. There's a third-party extension providing an `api role`_ which refers to
   Epydoc's API docs for a given identifier.

Doxygen
   Michael Jones氏が reST/Sphinxからdoxygenへの橋渡しをする、 `breathe  <http://github.com/michaeljones/breathe/tree/master>`_ というツールを開発しています。

.. Michael Jones is developing a reST/Sphinx bridge to doxygen called `breathe
   <http://github.com/michaeljones/breathe/tree/master>`_.

SCons
   Glenn Hutchings氏が、SphinxのドキュメントをビルドするためのSConsビルドスクリプトを作成しています。このスクリプトは、次のURLのところで開発されています: http://bitbucket.org/zondo/sphinx-scons

.. Glenn Hutchings has written a SCons build script to build Sphinx
   documentation; it is hosted here: http://bitbucket.org/zondo/sphinx-scons

PyPI
    Jannis Leidelが `setuptoolsコマンド <http://pypi.python.org/pypi/Sphinx-PyPI-upload>`_ を作成しています。このコマンドを実行すると、自動的にSphinxで作られたドキュメントを、PyPIパッケージのドキュメント領域(http://packages.python.org/)にアップロードします。

..  Jannis Leidel wrote a `setuptools command
    <http://pypi.python.org/pypi/Sphinx-PyPI-upload>`_ that automatically uploads
    Sphinx documentation to the PyPI package documentation area at
    http://packages.python.org/.


GitHub pages
   .. Directories starting with underscores are ignored by default which breaks
      static files in Sphinx.  GitHub's preprocessor can be `disabled
      <https://github.com/blog/572-bypassing-jekyll-on-github-pages>`_ to support
      Sphinx HTML output properly.

   デフォルトでは、Sphinxが静的ファイルを置いているような、アンダースコアで始まるディレクトリは無視されます。SphinxのHTML出力を置くために、GitHubのプリプロセッサを `無効にする <https://github.com/blog/572-bypassing-jekyll-on-github-pages>`_ ことができます。


MediaWiki
   .. See http://bitbucket.org/kevindunn/sphinx-wiki, a project by Kevin Dunn.

   Kevin Dunnがプロジェクトを運営しています。 http://bitbucket.org/kevindunn/sphinx-wiki を参照してください。

.. _API ロール: http://git.savannah.gnu.org/cgit/kenozooid.git/tree/doc/extapi.py
.. _xhtmlからreST: http://docutils.sourceforge.net/sandbox/xhtml2rest/xhtml2rest.py



Google Analytics
   次のようなカスタムの ``layout.html`` テンプレートを使用することができます:

   .. code-block:: html+django

      {% extends "!layout.html" %}

      {%- block extrahead %}
      {{ super() }}
      <script type="text/javascript">
        var _gaq = _gaq || [];
        _gaq.push(['_setAccount', 'XXX アカウント番号 XXX']);
        _gaq.push(['_trackPageview']);
      </script>
      {% endblock %}

      {% block footer %}
      {{ super() }}
      <div class="footer">このページは統計情報を収集するために<a href="http://analytics.google.com/">
      Google Analytics</a>を使用しています。もしも無効にしたい場合には、www.google-analytics.com
      からロードされるJavaScriptをブロックして下さい。
      <script type="text/javascript">
        (function() {
          var ga = document.createElement('script');
          ga.src = ('https:' == document.location.protocol ?
                    'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
          ga.setAttribute('async', 'true');
          document.documentElement.firstChild.appendChild(ga);
       })();
      </script>
      </div>
      {% endblock %}

.. You can use a custom ``layout.html`` template, like this:

   .. code-block:: html+django

      {% extends "!layout.html" %}

      {%- block extrahead %}
      {{ super() }}
      <script type="text/javascript">
        var _gaq = _gaq || [];
        _gaq.push(['_setAccount', 'XXX account number XXX']);
        _gaq.push(['_trackPageview']);
      </script>
      {% endblock %}

      {% block footer %}
      {{ super() }}
      <div class="footer">This page uses <a href="http://analytics.google.com/">
      Google Analytics</a> to collect statistics. You can disable it by blocking
      the JavaScript coming from www.google-analytics.com.
      <script type="text/javascript">
        (function() {
          var ga = document.createElement('script');
          ga.src = ('https:' == document.location.protocol ?
                    'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
          ga.setAttribute('async', 'true');
          document.documentElement.firstChild.appendChild(ga);
       })();
      </script>
      </div>
      {% endblock %}

.. 
   .. _api role: http://git.savannah.gnu.org/cgit/kenozooid.git/tree/doc/extapi.py
   .. _xhtml to reST: http://docutils.sourceforge.net/sandbox/xhtml2rest/xhtml2rest.py

.. Epub info
   ---------

.. _epub-faq:

Epub情報
--------

.. The epub builder is currently in an experimental stage.  It has only been tested
   with the Sphinx documentation itself.  If you want to create epubs, here are
   some notes:

現在、epubビルダーはまだ実験的実装の段階です。まだSphinx本体のドキュメントでしかテストされていません。もしもepubファイルを生成したいのであれば、次の注意点をご覧になってください:

.. * Split the text into several files. The longer the individual HTML files are,
     the longer it takes the ebook reader to render them.  In extreme cases, the
     rendering can take up to one minute.

* テキストはいくつかのファイルに分割されます。長さの長いHTMLファイルの場合、電子ブックリーダーによってはレンダリングに長い時間がかかります。極端な場合には、1分ほどかかることもあります。

.. * Try to minimize the markup.  This also pays in rendering time.

* マークアップは少なくなるようにしてください。これはレンダリング時間に関わってきます。

.. * For some readers you can use embedded or external fonts using the CSS
     ``@font-face`` directive.  This is *extremely* useful for code listings which
     are often cut at the right margin.  The default Courier font (or variant) is
     quite wide and you can only display up to 60 characters on a line.  If you
     replace it with a narrower font, you can get more characters on a line.  You
     may even use `FontForge <http://fontforge.sourceforge.net/>`_ and create
     narrow variants of some free font.  In my case I get up to 70 characters on a
     line.

* いくつかのリーダーでは、CSSの ``@font-face`` ディレクティブを使うことで、組み込みフォントや外部フォントを使用することができます。ソースコードのリストを表現する場合には、正しいマージンが行われるようになるため、 **非常に** これが役立ちます。デフォルトのCourierフォント(もしくはvariant)の場合には、一行につき60文字しか表現できません。もしもより狭いフォントを指定すると、一行の表示文字数を増やせます。 `FontForge <http://fontforge.sourceforge.net/>`_ を使用して、フリーフォントの幅を短くしたバージョンを作成することができます。私が試した限りでは一行あたり70文字まで増やすことができました。

  納得のいく結果を得るためには、多少の試行錯誤が必要になるでしょう。  

.. * Test the created epubs. You can use several alternatives.  The ones I am aware
     of are Epubcheck_, Calibre_, FBreader_ (although it does not render the CSS),
     and Bookworm_.  For bookworm you can download the source from
     http://code.google.com/p/threepress/ and run your own local server.

* 作成されたepubファイルはテストしてください。いくつかの選択肢があります。私が確認するようにしているのは、 Epubcheck_, Calibre_, FBreader_ (これはCSSをレンダリングできません), Bookworm_ です。Bookwormは、 http://code.google.com/p/threepress/ からダウンロードして、ローカルのサーバ上で実行します。

.. * Large floating divs are not displayed properly.
     If they cover more than one page, the div is only shown on the first page.
     In that case you can copy the :file:`epub.css` from the
     ``sphinx/themes/epub/static/`` directory to your local ``_static/``
     directory and remove the float settings.

* 大きなフローティング指定のdiv要素は適切に表示されません。もしも複数ページにわたるdiv要素があったとしても、最初のページにしか表示されません。もしこのような場合には、 ``sphinx/themes/epub/static/`` にある :file:`epub.css` をローカルの ``_static/`` にコピーして、float設定を削除してください。

.. * Files that are inserted outside of the ``toctree`` directive must be manually
     included. This sometimes applies to appendixes, e.g. the glossary or
     the indices.  You can add them with the :confval:`epub_post_files` option.

 * ``toctree`` ディレクティブ外のファイルは、手動でインクルードしなければなりません。用語集、索引などのAppendixが、時々これに該当します。 :confval:`epub_post_files` オプションを使うと、これらのファイルを追加することができます。 

.. _Epubcheck: http://code.google.com/p/epubcheck/
.. _Calibre: http://calibre-ebook.com/
.. _FBreader: http://www.fbreader.org/
.. _Bookworm: http://bookworm.oreilly.com/

.. Texinfo info
   ------------

.. _texinfo-faq:

Texinfo情報
------------

.. The Texinfo builder is currently in an experimental stage but has successfully
   been used to build the documentation for both Sphinx and Python.  The intended
   use of this builder is to generate Texinfo that is then processed into Info
   files.

Texinfoビルダーはまだ実験段階ですが、SphinxとPythonの両方のドキュメントのビルドには成功しています。このビルダーは、Texinfo向けのファイルを生成して、Infoファイルを作ることを目的としています。

.. There are two main programs for reading Info files, ``info`` and GNU Emacs.  The
   ``info`` program has less features but is available in most Unix environments
   and can be quickly accessed from the terminal.  Emacs provides better font and
   color display and supports extensive customization (of course).

Infoファイルを読むプログラムは、 ``info`` とGNU Emacsの2つあります。 ``info`` プログラムは機能は少ないのですが、ほとんどのUNIX環境で利用可能であり、ターミナルからのアクセスは簡単です。Emacsはフォントや色の表示がターミナルよりも優れており、(もちろん)様々なカスタマイズが可能です。

.. Displaying Links
   ~~~~~~~~~~~~~~~~

.. _texinfo-links:

リンクの表示
~~~~~~~~~~~~

.. One noticeable problem you may encounter with the generated Info files is how
   references are displayed.  If you read the source of an Info file, a reference
   to this section would look like:

      * note Displaying Links: target-id

Infoファイルの生成時の問題は、参照をどのように表示するか、です。もし、Infoファイルのソースを見ると、このセクションへのリンクは次のように書かれます::

    * note リンクの表示: target-id

.. In the stand-alone reader, ``info``, references are displayed just as they
   appear in the source.  Emacs, on the other-hand, will by default replace
   ``\*note:`` with ``see`` and hide the ``target-id``.  For example:

       :ref:`texinfo-links`

スタンドアローンの ``info`` リーダーの場合、参照はソースコードに表示されている通りに表示されます。Emacsの場合は、デフォルトで ``\*note:`` は ``see`` に置換され、 ``target-id`` は非表示になります。サンプル:

    :ref:`texinfo-links`

.. The exact behavior of how Emacs displays references is dependent on the variable
   ``Info-hide-note-references``.  If set to the value of ``hide``, Emacs will hide
   both the ``\*note:`` part and the ``target-id``.  This is generally the best way
   to view Sphinx-based documents since they often make frequent use of links and
   do not take this limitation into account.  However, changing this variable
   affects how all Info documents are displayed and most due take this behavior
   into account.

Emacsで参照をどのように表示するかは、 ``Info-hide-note-references`` 変数の定義で変わります。もしこの変数に ``hide`` を設定刷ると、Emacsは ``\*note:`` 部分と、 ``target-id`` の両方を非表示にします。もしこの制限を気にせず、リンクを多用してSphinxベースのドキュメントを見るのであれば、この設定がベストでしょう。しかし、この変数を変えた場合に、すべてのInfoドキュメントの表示が変わってしまうことに注意が必要です。

.. If you want Emacs to display Info files produced by Sphinx using the value
   ``hide`` for ``Info-hide-note-references`` and the default value for all other
   Info files, try adding the following Emacs Lisp code to your start-up file,
   ``~/.emacs.d/init.el``.

もし、Sphinxで作られたInfoファイルのときだけ、 ``Info-hide-note-references`` を ``hide`` にしたい場合には、次のEmacs Lispのコードをスタートアップファイル :file:`~/.emacs.d/init.el` に追加してください。

::

   (defadvice info-insert-file-contents (after
                                         sphinx-info-insert-file-contents
                                         activate)
     "Hack to make `Info-hide-note-references' buffer-local and
   automatically set to `hide' iff it can be determined that this file
   was created from a Texinfo file generated by Docutils or Sphinx."
     (set (make-local-variable 'Info-hide-note-references)
          (default-value 'Info-hide-note-references))
     (save-excursion
       (save-restriction
         (widen) (goto-char (point-min))
         (when (re-search-forward
                "^Generated by \\(Sphinx\\|Docutils\\)"
                (save-excursion (search-forward "^_" nil t)) t)
           (set (make-local-variable 'Info-hide-note-references)
                'hide)))))


.. Notes
   ~~~~~

メモ 
~~~~

.. The following notes may be helpful if you want to create Texinfo files:

以下のメモは、Texinfoファイルを作る時の参考となるメモです。

.. - Each section corresponds to a different ``node`` in the Info file.

- それぞれのセクションは、Infoファイルの ``node`` となります。

.. - Some characters cannot be properly escaped in menu entries and xrefs.  The
     following characters are replaced by spaces in these contexts: ``@``, ``{``,
     ``}``, ``.``, ``,``, and ``:``.

- いくつかの文字はメニューのエントリーやクロスリファレンスの中でエスケープすることができません。以下の文字はスペースに置き換えられます: ``@``, ``{``,
     ``}``, ``.``, ``,``, ``:``.

.. - In the HTML and Tex output, the word ``see`` is automatically inserted before
     all xrefs.

- HTMLとTex出力の中では ``see`` という言葉が自動的にすべてのクロスリファレンスの前に挿入されます。

.. - Links to external Info files can be created using the somewhat official URI
     scheme ``info``.  For example::

        info:Texinfo#makeinfo_options

     which produces:

        info:Texinfo#makeinfo_options

- 外部のInfoファイルへの参照は、 ``info`` という公式なURIスキームを使用して作成されます。例えば::

     info:Texinfo#makeinfo_options

  この表示は以下のようになります:

     info:Texinfo#makeinfo_options

.. - Inline markup appears as follows in Info:

     * strong -- \*strong\*
     * emphasis -- _emphasis_
     * literal -- \`literal'

     It is possible to change this behavior using the Texinfo command
     ``@definfoenclose``.  For example, to make inline markup more closely resemble
     reST, add the following to your :file:`conf.py`::

        texinfo_elements = {'preamble': """\
        @definfoenclose strong,**,**
        @definfoenclose emph,*,*
        @definfoenclose code,`@w{}`,`@w{}`
        """}

- インラインマークアップは次のように表示されます。

  * strong -- \*strong\*
  * emphasis -- _emphasis_
  * literal -- \`literal'

  この動作は、 ``@definfoenclose`` コマンドを使用して変更することができます。もし、表現をreSTに近づけたい場合には、次のように :file:`conf.py` にオプションを設定します::   

        texinfo_elements = {'preamble': """\
        @definfoenclose strong,**,**
        @definfoenclose emph,*,*
        @definfoenclose code,`@w{}`,`@w{}`
        """}