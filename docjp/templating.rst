.. highlight:: html+jinja

.. Templating

.. _templating:

テンプレート
============

.. Sphinx uses the `Jinja <http://jinja.pocoo.org>`_ templating engine for its HTML
   templates.  Jinja is a text-based engine, and inspired by Django templates, so
   anyone having used Django will already be familiar with it.  It also has
   excellent documentation for those who need to make themselves familiar with it.

SphinxはHTMLのテンプレートとして `Jinja <http://jinja.pocoo.org>`_ テンプレートエンジンを利用しています。Jinjaは、Djangoのテンプレートにインスパイアされた、テキストベースのテンプレートエンジンです。Djangoを触ったことがある人ならば、すぐに慣れるでしょう。つまり、Djangoテンプレート用に書かれた、既存のすばらしいドキュメントは、Jinjaを学ぼうとしている人にも役に立つということを意味しています。

.. Do I need to use Sphinx' templates to produce HTML?

HTMLを生成するのにSphinxのテンプレートを使用する必要があるのか？
----------------------------------------------------------------

.. No.  You have several other options:

必要はありません。いくつか別の選択肢を選ぶことができます。

.. * You can write a :class:`~sphinx.application.TemplateBridge` subclass that
     calls your template engine of choice, and set the :confval:`template_bridge`
     configuration value accordingly.

* 読者が使用したいテンプレートエンジンを呼び出すような :class:`~sphinx.application.TemplateBridge` クラスのサブクラスを書いて、それが呼ばれるように :confval:`template_bridge` 設定値に設定します。

.. * You can :ref:`write a custom builder <writing-builders>` that derives from
     :class:`~sphinx.builders.StandaloneHTMLBuilder` and calls your template engine
     of choice.

* :class:`~sphinx.builders.StandaloneHTMLBuilder` を継承して :ref:`カスタムビルダーを書いて <writing-builders>` 好きなテンプレートエンジンを呼ぶようにします。

.. * You can use the :class:`~sphinx.builders.PickleHTMLBuilder` that produces
     pickle files with the page contents, and postprocess them using a custom tool,
     or use them in your Web application.

* ページの内容を含むpickleファイルを生成する :class:`~sphinx.builders.PickleHTMLBuilder` を使用して、自分でカスタムしたツールや、ウェブアプリケーション内などで後処理を行います。


.. Jinja/Sphinx Templating Primer

Jinja/Sphinxテンプレートの基礎
------------------------------

.. The default templating language in Sphinx is Jinja.  It's Django/Smarty inspired
   and easy to understand.  The most important concept in Jinja is :dfn:`template
   inheritance`, which means that you can overwrite only specific blocks within a
   template, customizing it while also keeping the changes at a minimum.

Sphinxのデフォルトのテンプレート言語はJinjaです。これはDjango/Smartyにインスパイアされて作成されたもので、理解しやすくなっています。Jinjaにおける最も重要なコンセプトは :dfn:`テンプレート継承` です。これは、テンプレートの特定のブロックのみをオーバーライドして、変更箇所を最小限にしたカスタマイズを可能にします。

.. To customize the output of your documentation you can override all the templates
   (both the layout templates and the child templates) by adding files with the
   same name as the original filename into the template directory of the structure
   the Sphinx quickstart generated for you.

ドキュメントの出力をカスタマイズするには、Sphinxのquickstartコマンドが生成したテンプレートのディレクトリに、オリジナルファイル名と同じ名前のテンプレートを追加して、すべてのテンプレート(レイアウトのテンプレートと子供のテンプレート)をオーバーライドするという方法があります。

.. Sphinx will look for templates in the folders of :confval:`templates_path`
   first, and if it can't find the template it's looking for there, it falls back
   to the selected theme's templates.

Sphinxはまず最初に、 :confval:`templates_path` で設定されたフォルダのテンプレートを見に行きます。そして、そこで見つからなければ、選択しているテーマのテンプレートを探しに行きます。

.. A template contains **variables**, which are replaced with values when the
   template is evaluated, **tags**, which control the logic of the template and
   **blocks** which are used for template inheritance.

テンプレートは、テンプレートが評価される時に値が置き換えられる **変数** と、テンプレートのロジックを制御する **タグ**, テンプレートの継承に使用される **ブロック** の3種類の要素を含みます。

.. Sphinx' *basic* theme provides base templates with a couple of blocks it will
   fill with data.  These are located in the :file:`themes/basic` subdirectory of
   the Sphinx installation directory, and used by all builtin Sphinx themes.
   Templates with the same name in the :confval:`templates_path` override templates
   supplied by the selected theme.

Sphinxの *basic* テーマでは2つのブロックを持つ基本となるテンプレートを提供しています。このブロックはデータで埋められます。これらのファイルはSphinxのインストールディレクトリの中の :file:`themes/basic` サブディレクトリ内に置かれています。このテーマはすべてのSphinxの組み込みのテーマから使用されています。 :confval:`tempates_path` に入っている同名のテンプレートは、選択されたテーマのテンプレートよりも優先的に使用されるので、既存のテーマのテンプレートをオーバーライドします。

.. For example, to add a new link to the template area containing related links all
   you have to do is to add a new template called ``layout.html`` with the
   following contents

例えば、新しいリンクをテンプレートの関連リンクを含む領域に追加する場合には、 ``layout.html`` と呼ばれる新しいテンプレートを作成して、以下の内容を書き込みます::

    {% extends "!layout.html" %}
    {% block rootrellink %}
        <li><a href="http://project.invalid/">Project Homepage</a> &raquo;</li>
        {{ super() }}
    {% endblock %}

.. By prefixing the name of the overridden template with an exclamation mark,
   Sphinx will load the layout template from the underlying HTML theme.

オーバーライドされるテンプレート名の前にエクスクラメーションマーク(!)を付けることで、SphinxはベースとなるHTMLテーマのテンプレートをロードします。

.. **Important**: If you override a block, call ``{{ super() }}`` somewhere to
   render the block's content in the extended template -- unless you don't want
   that content to show up.

**重要**: もしブロックをオーバーライドするときは、拡張される側の内容を表示したくない場合以外の場合には、 ``{{ super() }}`` をコールすると、拡張される方のテンプレートのブロックの内容をレンダリングすることができます。


.. Working the the builtin templates

組み込みテンプレートの働き
--------------------------

.. The builtin **basic** theme supplies the templates that all builtin Sphinx
   themes are based on.  It has the following elements you can override or use:

組み込みの **basic** テーマはすべての組み込みSphinxテーマの骨組みとなるテンプレートを提供しています。このうち、以下の要素オーバーライドしたり、使用したりすることができます。

.. Blocks

ブロック
~~~~~~~~

.. The following blocks exist in the ``layout.html`` template:

``layout.html`` テンプレートの中には、次のようなブロックが定義されています。

.. `doctype`
    The doctype of the output format.  By default this is XHTML 1.0 Transitional
    as this is the closest to what Sphinx and Docutils generate and it's a good
    idea not to change it unless you want to switch to HTML 5 or a different but
    compatible XHTML doctype.

`doctype`
    出力フォーマットのドキュメントのタイプです。デフォルトでは、SphinxとDocutilsが生成する結果にもっとも近いXHTML 1.0 Transitionalになっています。HTML 5やその他のXHTMLと互換性のあるdoctype以外のタイプには変更しない方がいいでしょう。

.. `linktags`
    This block adds a couple of ``<link>`` tags to the head section of the
    template.

`linktags`
   このブロックは、テンプレートのheadセクションに ``<link>`` タグをいくつか追加するものです。

.. `extrahead`
    This block is empty by default and can be used to add extra contents into
    the ``<head>`` tag of the generated HTML file.  This is the right place to
    add references to JavaScript or extra CSS files.

`extrahead`
   このブロックはデフォルトでは空です。このブロックを使うと、追加の内容を生成されたHTMLファイルの ``<head>`` タグに追加の情報を出力することができます。JavaScriptや追加のCSSファイルへの参照を追加する場合にはこのブロックを使用します。

.. `relbar1` / `relbar2`
    This block contains the *relation bar*, the list of related links (the
    parent documents on the left, and the links to index, modules etc. on the
    right).  `relbar1` appears before the document, `relbar2` after the
    document.  By default, both blocks are filled; to show the relbar only
    before the document, you would override `relbar2` like this

`relbar1` / `relbar2`
    このブロックは、 *リレーションバー* を含みます。リレーションバーは左側に親ドキュメントを、右側に索引、モジュール索引などを含みます。 `relbar1` はドキュメントの前に、 `relbar2` はドキュメントの後に表示されます。デフォルトではそれぞれのブロックの内容が表示されます。もしも、ドキュメントの前だけ表示したい場合には、以下のように `relbar2` をオーバーライドします::

       {% block relbar2 %}{% endblock %}

.. `rootrellink` / `relbaritems`
    Inside the relbar there are three sections: The `rootrellink`, the links
    from the documentation and the custom `relbaritems`.  The `rootrellink` is a
    block that by default contains a list item pointing to the master document
    by default, the `relbaritems` is an empty block.  If you override them to
    add extra links into the bar make sure that they are list items and end with
    the :data:`reldelim1`.

`rootrellink` / `relbaritems`
    リレーションバーは３つのセクションで構成されています。 `rootrellink` と、ドキュメントからのリンク, カスタムの `relbaritems` の３つです。デフォルトでは `rootrellink` はマスタードキュメントへのリンクを含むリストアイテムを含みます。 `relbarimtes` はデフォルトでは空のブロックです。もしもこれらを上書きして、バーの中に追加のリンクを含める場合には、リストアイテムの末尾には :data:`reldelim1` を付けるようにしてください。

.. `document`
    The contents of the document itself.  It contains the block "body" where the
    individual content is put by subtemplates like ``page.html``.

`document`
    ドキュメントのコンテンツそのものです。これはそれぞれのコンテンツが ``page.html`` などのサブのテンプレートで整形して置かれる "body" ブロックを含みます。

.. `sidebar1` / `sidebar2`
    A possible location for a sidebar.  `sidebar1` appears before the document
    and is empty by default, `sidebar2` after the document and contains the
    default sidebar.  If you want to swap the sidebar location override this and
    call the `sidebar` helper:

    (The `sidebar2` location for the sidebar is needed by the ``sphinxdoc.css``
    stylesheet, for example.)

`sidebar1` / `sidebar2`
    サイドバーが入る可能性のある場所を示すブロックです。 `sidebar1` はドキュメントの前にあり、デフォルトでは空です。 `sidebar2` はドキュメントの後ろにあり、デフォルトのサイドバーを含んでいます。もし、サイドバーの位置を入れ替えたい場合には以下のようにオーバーライドして、 `sidebar` ヘルパーを呼び出します:

    .. sourcecode:: html+jinja

        {% block sidebar1 %}{{ sidebar() }}{% endblock %}
        {% block sidebar2 %}{% endblock %}

    サイドバーが置かれる `sidebar2` の位置も ``sphinxdoc.css`` といったスタイルシートから必要になります。

.. `sidebarlogo`
    The logo location within the sidebar.  Override this if you want to place
    some content at the top of the sidebar.

`sidebarlogo`
    サイドバーの中にロゴを置くための位置を示すブロックです。もしもサイドバーの最上段に何かコンテンツを置きたい場合には、このブロックをオーバーライドします。

.. `sidebartoc`
    The table of contents within the sidebar.

`sidebartoc`
    サイドバー内部の目次です。

.. `sidebarrel`
    The relation links (previous, next document) within the sidebar.

`sidebarrel`
    サイドバー内の関連リンク(前後のトピックへのリンク)です。

.. `sidebarsourcelink`
    The "Show source" link within the sidebar (normally only shown if this is
    enabled by :confval:`html_show_sourcelink`).

`sidebarsourcelink`
    サイドバー内の "ソースコードを表示" へのリンクです。通常は設定の :confval:`html_show_sourcelink` が有効になっている時にだけ表示されます。

.. `sidebarsearch`
    The search box within the sidebar.  Override this if you want to place some
    content at the bottom of the sidebar.

`sidebarsearch`
    サイドバー内の検索ボックスです。いくつかのコンテンツをサイドバーの下部に追加したい場合には、このブロックをオーバーライドします。

.. `footer`
    The block for the footer div.  If you want a custom footer or markup before
    or after it, override this one.

`footer`
    フッターのブロックです。フッターをカスタマイズしたり、フッターの前後にマークアップを追加したりしたい時には、このブロックをオーバーライドします。


.. Configuration Variables
   ~~~~~~~~~~~~~~~~~~~~~~~

設定値
~~~~~~

.. Inside templates you can set a couple of variables used by the layout template
   using the ``{% set %}`` tag:

テンプレート内では、 ``{% set %}`` タグを利用して、テンプレートのレイアウトに使用される変数をセットすることができます。

.. data:: reldelim1

   .. The delimiter for the items on the left side of the related bar.  This
      defaults to ``' &raquo;'`` Each item in the related bar ends with the value
      of this variable.

   リレーションバーの左側アイテムの区切り文字です。デフォルトは ``' &raquo;'`` です。リレーションバーに含まれるアイテムはすべて、ここで指定した変数の値で区切られます。

.. data:: reldelim2

   .. The delimiter for the items on the right side of the related bar.  This
      defaults to ``' |'``.  Each item except of the last one in the related bar
      ends with the value of this variable.

   リレーションバーの右側のアイテムの区切り文字になります。デフォルトは ``' |'`` です。最後の要素を除くすべてのリレーションバーのアイテムは、ここで指定された変数の値で区切られます。

   .. Overriding works like this

   以下のようにオーバーライドします::

       {% extends "!layout.html" %}
       {% set reldelim1 = ' &gt;' %}


.. data:: script_files

   .. Add additional script files here, like this

   以下のように記述すると、追加のスクリプトファイルをここで追加することができます::

      {% set script_files = script_files + [pathto("_static/myscript.js", 1)] %}

.. Helper Functions
   ~~~~~~~~~~~~~~~~

ヘルパー関数
~~~~~~~~~~~~

.. Sphinx provides various Jinja functions as helpers in the template.  You can use
   them to generate links or output multiply used elements.

Sphinxはテンプレートで使用できるJinja関数をいくつか提供しています。これを使用すると、リンクを生成したり、構成要素を使用した出力を何度も行ったりできるようになります。

.. function:: pathto(ドキュメント)

   .. Return the path to a Sphinx document as a URL.  Use this to refer to built
      documents.

   SphinxドキュメントへのURLを返します。これは組み込みのドキュメントを参照する場合に使用します。

.. function:: pathto(ファイル, 1)

   .. Return the path to a *file* which is a filename relative to the root of the
      generated output.  Use this to refer to static files.

   *ファイル* に対する、生成されたドキュメントのルートからの相対パスによるリンクを返します。静的なファイルを参照するのに使用します。

.. function:: hasdoc(ドキュメント)

   .. Check if a document with the name *document* exists.

   *ドキュメント* で指定された名前のドキュメントが存在するかどうかチェックします。

.. function:: sidebar()

   .. Return the rendered sidebar.

   レンダリングされたサイドバーを返します。

.. function:: relbar()

   .. Return the rendered relation bar.

   レンダリングリレーションバーを返します。


.. Global Variables
   ~~~~~~~~~~~~~~~~

グローバル変数
~~~~~~~~~~~~~~

.. These global variables are available in every template and are safe to use.
   There are more, but most of them are an implementation detail and might change
   in the future.

これらのグローバル変数はすべてのテンプレートで利用可能で、安全に使用できる変数です。ここで説明されているよりも多くの変数がありますが、それらの変数は、実装に根ざした内部変数であったり、将来挙動が変更される予定のものになります。

.. data:: builder

   .. The name of the builder (e.g. ``html`` or ``htmlhelp``).

   ビルダーの名前が格納されている変数です。 ``html``, ``htmlhelp`` などの値が入ります。


.. data:: copyright

   .. The value of :confval:`copyright`.

   :confval:`copyright` の値が入ります。


.. data:: docstitle

   .. The title of the documentation (the value of :confval:`html_title`).

   ドキュメントのタイトルです。 :confval:`html_title` で設定した値が入ります。
   

.. data:: embedded

   .. True if the built HTML is meant to be embedded in some viewing application
      that handles navigation, not the web browser, such as for HTML help or Qt
      help formats.  In this case, the sidebar is not included.

   ウェブブラウザではなく、HTMLヘルプや、Qtヘルプフォーマットなどの、専用のビューアーアプリケーション内で使用される組み込みのHTMLの場合にTrueとなります。これがTrueの場合には、サイドバーが含まれなくなります。


.. data:: favicon

   .. The path to the HTML favicon in the static path, or ``''``.

   HTMLのfaviconを表す静的パスです。設定されない場合には ``''`` となります。


.. data:: file_suffix

   .. The value of the builder's :attr:`out_suffix` attribute, i.e. the file name
      extension that the output files will get.  For a standard HTML builder, this
      is usually ``.html``.

   ビルダーの :attr:`out_suffix` アトリビュートの値です。出力ファイル名に付く拡張子などです。標準のHTMLビルダーの場合には、通常は ``.html`` になります。


.. data:: has_source

   .. True if the reST document sources are copied (if :confval:`html_copy_source`
      is true).

   もしreSTドキュメントソースがコピーされている場合にTrueになります。 :confval:`html_copy_source` がtrueに設定されるとコピーされます。


.. data:: last_updated

   .. The build date.

   ビルドされた日時です。


.. data:: logo

   .. The path to the HTML logo image in the static path, or ``''``.

   HTMLに貼り付けられるロゴ画像の静的なパスです。指定されていない場合には ``''`` になります。


.. data:: master_doc

   .. The value of :confval:`master_doc`, for usage with :func:`pathto`.

   :confval:`master_doc` の値が入ります。 :func:`pathto` と一緒に使用します。


.. data:: next

   .. The next document for the navigation.  This variable is either false or has
      two attributes `link` and `title`.  The title contains HTML markup.  For
      example, to generate a link to the next page, you can use this snippet

   ナビゲーションで「次のトピック」にあたるドキュメントです。この変数は ``false`` か、 `link` と `title` の二つの属性を持つオブジェクトのどちらかになります。タイトルにはHTMLのマークアップが含まれます。例えば、次のページへのリンクを生成するには、以下のようなコードを利用します::

      {% if next %}
      <a href="{{ next.link|e }}">{{ next.title }}</a>
      {% endif %}


.. data:: pagename

   .. The "page name" of the current file, i.e. either the document name if the
      file is generated from a reST source, or the equivalent hierarchical name
      relative to the output directory (``[directory/]filename_without_extension``).

   現在のファイルの "ページ名" です。reSTのソースから生成されていたらドキュメント名になります。あるいは出力ディレクトリからの相対パス名から拡張子を抜いた名前 (``[ディレクトリ/]拡張子なしのファイル名``) となる、階層名付きの名前になります。


.. data:: parents

   .. A list of parent documents for navigation, structured like the :data:`next`
      item.

   ナビゲーションのための、親のドキュメントのリストです。それぞれの要素は :data:`next` と同じような構造体になっています。


.. data:: prev

   .. Like :data:`next`, but for the previous page.

   「前のトピック」にあたるページの情報です。 :data`next` と似ています。


.. data:: project

   .. The value of :confval:`project`.

   :confval:`project` の値になります。


.. data:: release

   .. The value of :confval:`release`.

   :confval:`release` の値になります。


.. data:: rellinks

   .. A list of links to put at the left side of the relbar, next to "next" and
      "prev".  This usually contains links to the index and the modindex.  If you
      add something yourself, it must be a tuple ``(pagename, link title,
      accesskey, link text)``.

   リレーションバーの左側(?)、 "次", "前" のとなりに置かれるリンクのリストです。通常では、索引とモジュール索引へのリンクが含まれています。もしここに何かを追加する場合には、 ``(ページ名, リンクタイトル, アクセスキー, リンクテキスト)`` というタプルを追加します。


.. data:: shorttitle

   .. The value of :confval:`html_short_title`.

   :confval:`html_short_title` の値になります。


.. data:: show_source

   .. True if :confval:`html_show_sourcelink` is true.

   :confval:`html_show_sourcelink` がtrueの場合にTrueになります。


.. data:: sphinx_version

   .. The version of Sphinx used to build.

   ビルドに使用されたSphinxのバージョンです。


.. data:: style

   .. The name of the main stylesheet, as given by the theme or
      :confval:`html_style`.

   メインのスタイルシートの名前です。テーマで設定されたものか、あるいは :confval:`html_style` で設定されている値になります。


.. data:: title

   .. The title of the current document, as used in the ``<title>`` tag.

   現在のドキュメントのタイトルです。これは ``<title>`` タグで使用されます。


.. data:: use_opensearch

   .. The value of :confval:`html_use_opensearch`... The value of :confval:`html_use_opensearch`.

   :confval:`html_use_opensearch` の値が入ります。


.. data:: version

   .. The value of :confval:`version`.

   :confval:`version` の値が入ります。


.. In addition to these values, there are also all **theme options** available
   (prefixed by ``theme_``), as well as the values given by the user in
   :confval:`html_context`.

これらの値に加えて、すべての **テーマオプション** も利用可能です。テーマオプションには ``theme_`` という文字列が先頭に付きます。ユーザが :confval:`html_context` を通じて設定した値も同じように利用可能です。

.. In documents that are created from source files (as opposed to
   automatically-generated files like the module index, or documents that already
   are in HTML form), these variables are also available:

ソースファイルから生成されるドキュメント内では、以下のオプションも利用可能です。ただし、モジュール索引などの自動生成されるファイルや、最初からHTMLとして生成されるものについては利用できません。

.. data:: meta

   .. Document metadata (a dictionary), see :ref:`metadata`.

   ドキュメントのメタデータの辞書です。 :ref:`metadata` を参照してください。


.. data:: sourcename

   .. The name of the copied source file for the current document.  This is only
      nonempty if the :confval:`html_copy_source` value is true.

   現在のドキュメントのコピーされたソースファイル名です。 :confval:`html_copy_source` の値がtrueでない場合には 空になります。


.. data:: toc

   .. The local table of contents for the current page, rendered as HTML bullet
      lists.

   現在のページのためのローカルの目次です。HTMLのリストとしてレンダリングされています。


.. data:: toctree

   .. A callable yielding the global TOC tree containing the current page, rendered
      as HTML bullet lists.  If the optional keyword argument ``collapse`` is true,
      all TOC entries that are not ancestors of the current page are collapsed.



   .. A callable yielding the global TOC tree containing the current page, rendered
      as HTML bullet lists.  Optional keyword arguments:

      * ``collapse`` (true by default): if true, all TOC entries that are not
        ancestors of the current page are collapsed

      * ``maxdepth`` (defaults to the max depth selected in the toctree directive):
        the maximum depth of the tree; set it to ``-1`` to allow unlimited depth

      * ``titles_only`` (false by default): if true, put only toplevel document
        titles in the tree

   現在のページを含むグローバルな目次ツリーを生成する、呼び出し可能オブジェクトです。HTMLリストとしてレンダリングされています。次のようなオプションのキーワード引数があります:

      * ``collapse`` (デフォルトはtrue): trueの場合には、現在のページの祖先にあたる目次のエントリー以外は折りたたまれます。

      * ``maxdepth`` (デフォルトではそのtoctreeディレクティブの最大値): 表示されるツリーの深さの最大値を設定します。 ``-1`` を設定すると深さの制限がなくなります。

      * ``titles_only`` (デフォルトはfalse): もしtrueが設定されると、ドキュメント内のトップレベルのタイトルだけがツリーに置かれます。



