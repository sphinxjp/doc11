.. _websupportquickstart:

Webサポートクイックスタート
============================

.. Web Support Quick Start
   =======================

.. Building Documentation Data
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~

ドキュメントデータのビルド
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. To make use of the web support package in your application you'll need to build
   the data it uses.  This data includes pickle files representing documents,
   search indices, and node data that is used to track where comments and other
   things are in a document.  To do this you will need to create an instance of the
   :class:`~.WebSupport` class and call its :meth:`~.WebSupport.build` method::

アプリケーションの中でウェブサポートパッケージを使用する場合は、まずはデータを作る必要があります。データには、pickle化されたドキュメントや検索インデックス、コメントなどがどのドキュメントに付加されたのかを追跡するためのノードデータが含まれます。これを行うためには、　:class:`~.WebSupport` クラスのインスタンスを作り、 :meth:`~.WebSupport.build` メソッドを呼ぶ必要があります::

   from sphinx.websupport import WebSupport

   support = WebSupport(srcdir='/path/to/rst/sources/',
                        builddir='/path/to/build/outdir',
                        search='xapian')

   support.build()

.. This will read reStructuredText sources from `srcdir` and place the necessary
   data in `builddir`.  The `builddir` will contain two sub-directories: one named
   "data" that contains all the data needed to display documents, search through
   documents, and add comments to documents.  The other directory will be called
   "static" and contains static files that should be served from "/static".

このコードは、reStructuredTextのソースコードを `srcdir` から読み込み、必要なデータを `builddir` に書き出します。 `builddir` は二つのサブディレクトリを含みます。 :file:`data` には、ドキュメントを表示したり、ドキュメントを検索したり、ドキュメントにコメントを付けるのに必要なデータがすべて含まれます。もう一つの :file:`static` ディレクトリは、 :file:`'/static'` からファイルを配信するための、静的ファイルを含みます。

.. note::

   .. If you wish to serve static files from a path other than "/static", you can
      do so by providing the *staticdir* keyword argument when creating the
      :class:`~.WebSupport` object.

   もし "/static" 以外のパスから静的ファイルの配信をしたい場合には、 :class:`~.WebSupport` オブジェクトを作る時に、 **staticdir** キーワード引数を指定してください。


.. Integrating Sphinx Documents Into Your Webapp
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sphinxドキュメントをウェブアプリケーションに統合
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. Now that the data is built, it's time to do something useful with it.  Start off
   by creating a :class:`~.WebSupport` object for your application:

データができましたので、次はこれを使う番です。アプリケーションのための :class:`~.WebSupport` オブジェクトを作るところから始めます::

   from sphinx.websupport import WebSupport

   support = WebSupport(datadir='/path/to/the/data',
                        search='xapian')

.. You'll only need one of these for each set of documentation you will be working
   with.  You can then call it's :meth:`~.WebSupport.get_document` method to access
   individual documents:

次に、個々のドキュメントに対する処理を作っていきます。 :meth:`~.WebSupport.get_document` メソッドを呼ぶと、個々のドキュメントにアクセスすることができます::

   contents = support.get_document('contents')

このメソッドは、次のキーを持つ辞書を返します:

.. This will return a dictionary containing the following items:

.. * **body**: The main body of the document as HTML
   * **sidebar**: The sidebar of the document as HTML
   * **relbar**: A div containing links to related documents
   * **title**: The title of the document
   * **css**: Links to css files used by Sphinx
   * **js**: Javascript containing comment options

* **body**: HTML形式のドキュメント本体です。
* **sidebar**: HTML形式のサイドバーです。
* **relbar**: このdivは、関連ドキュメントへのリンクを含んでいます。
* **title**: ドキュメントのタイトルです。
* **css**: Sphinxが使用するCSSファイルへのリンクです。
* **js**: コメントオプションを含むJavascriptです。

.. This dict can then be used as context for templates.  The goal is to be easy to
   integrate with your existing templating system.  An example using `Jinja2
   <http://jinja.pocoo.org/>`_ is:

この辞書は、テンプレートのコンテキストとして使用することができます。既存のどのテンプレートシステムとも簡単に統合できるようにすることを目標としています。例えば、 `Jinja2 <http://jinja.pocoo.org/>`_ を使用する場合は、以下のようになります。

.. sourcecode:: html+jinja

   {%- extends "layout.html" %}

   {%- block title %}
       {{ document.title }}
   {%- endblock %}

   {% block css %}
       {{ super() }}
       {{ document.css|safe }}
       <link rel="stylesheet" href="/static/websupport-custom.css" type="text/css">
   {% endblock %}

   {%- block js %}
       {{ super() }}
       {{ document.js|safe }}
   {%- endblock %}

   {%- block relbar %}
       {{ document.relbar|safe }}
   {%- endblock %}

   {%- block body %}
       {{ document.body|safe }}
   {%- endblock %}

   {%- block sidebar %}
       {{ document.sidebar|safe }}
   {%- endblock %}


.. Authentication
   --------------

認証
----

.. To use certain features such as voting, it must be possible to authenticate
   users.  The details of the authentication are left to your application.  Once a
   user has been authenticated you can pass the user's details to certain
   :class:`~.WebSupport` methods using the *username* and *moderator* keyword
   arguments.  The web support package will store the username with comments and
   votes.  The only caveat is that if you allow users to change their username you
   must update the websupport package's data:

投票のような機能を実装する場合、ユーザ認証ができる必要があります。認証をどのように実装するかはアプリケーションに任されています。ユーザが認証されたら、ユーザの情報を :class:`~.WebSupport` のメソッドの *username* と *moderator* キーワード引数に渡すことができます。ウェブサポートパッケージはユーザ名を、コメントや投票と一緒に保存します。注意点を1つあげるとすれば、もしユーザに対して名前の変更を行えるようにするのであれば、ウェブサポートパッケージの内部のユーザ名のデータも更新する必要があります::

   support.update_username(old_username, new_username)

.. *username* should be a unique string which identifies a user, and *moderator*
   should be a boolean representing whether the user has moderation privilieges.
   The default value for *moderator* is *False*.

*username* はユーザを特定するためのユニークな文字列でなければなりません。また、 *moderator* はユーザがモデレート権限を持っているかどうかを表すブール型でなければなりません。 *moderator* のデフォルト値は ``False`` です。

.. An example `Flask <http://flask.pocoo.org/>`_ function that checks whether a
   user is logged in and then retrieves a document is::

例えば、 `Flask <http://flask.pocoo.org/>`_ を使用して、ユーザがログインしているかどうかを確認し、ドキュメントを読めるようにするには、次のようなコードで行えます::

   from sphinx.websupport.errors import *

   @app.route('/<path:docname>')
   def doc(docname):
       username = g.user.name if g.user else ''
       moderator = g.user.moderator if g.user else False
       try:
           document = support.get_document(docname, username, moderator)
       except DocumentNotFoundError:
           abort(404)
       return render_template('doc.html', document=document)

.. The first thing to notice is that the *docname* is just the request path.  This
   makes accessing the correct document easy from a single view.  If the user is
   authenticated, then the username and moderation status are passed along with the
   docname to :meth:`~.WebSupport.get_document`.  The web support package will then
   add this data to the ``COMMENT_OPTIONS`` that are used in the template.

まず、 *docname* が要求されたパスを表すことに気づきます。これにより、正しいドキュメントへのアクセスが行えます。もしユーザの認証が行われていたら、ユーザ名とモデレート権限情報が :meth:`~.WebSupport.get_document` に渡されます。ウェブサポートパッケージは、テンプレートの中で使用される ``COMMENT_OPTIONS`` をこのデータに付加します。

.. note::

   .. This only works works if your documentation is served from your
      document root. If it is served from another directory, you will
      need to prefix the url route with that directory, and give the `docroot`
      keyword argument when creating the web support object:

   このプログラムはドキュメントがルートで提供される場合にのみ動作します。もし、他のディレクトリからドキュメントを提供したい場合には、URLのプリフィックスを指定する必要があります。これは、ウェブサポートオブジェクトを作成する時に、 `docroot` キーワード引数として与えます::

      support = WebSupport(..., docroot='docs')

      @app.route('/docs/<path:docname>')


.. Performing Searches
   ~~~~~~~~~~~~~~~~~~~

検索の実行
~~~~~~~~~~

.. To use the search form built-in to the Sphinx sidebar, create a function to
   handle requests to the url 'search' relative to the documentation root.  The
   user's search query will be in the GET parameters, with the key `q`.  Then use
   the :meth:`~sphinx.websupport.WebSupport.get_search_results` method to retrieve
   search results. In `Flask <http://flask.pocoo.org/>`_ that would be like this::

Sphinxサイドバーの検索機能を使うと、ドキュメントルート以下の 'search' というパスに対するリクエストが発生します。ユーザの検索クエリーは、GETパラメータの `q` キーに格納されています。 :meth:`~sphinx.websupport.WebSupport.get_search_results` メソッドに渡すと、検索結果が得られます。 `Flask <http://flask.pocoo.org/>`_ では次のようになります::

   @app.route('/search')
   def search():
       q = request.args.get('q')
       document = support.get_search_results(q)
       return render_template('doc.html', document=document)

.. Note that we used the same template to render our search results as we did to
   render our documents.  That's because :meth:`~.WebSupport.get_search_results`
   returns a context dict in the same format that :meth:`~.WebSupport.get_document`
   does.

ドキュメントと検索結果の表示には、同じテンプレートを使用しています。これは、 :meth:`~.WebSupport.get_search_results` メソッドが、 :meth:`~.WebSupport.get_document` と同じ形式のコンテキスト辞書を返すからです。


.. Comments & Proposals
   ~~~~~~~~~~~~~~~~~~~~

コメント＆提案
~~~~~~~~~~~~~~

.. Now that this is done it's time to define the functions that handle the AJAX
   calls from the script.  You will need three functions.  The first function is
   used to add a new comment, and will call the web support method
   :meth:`~.WebSupport.add_comment`::

それでは、コメントなどをAJAXで処理するための関数を定義します。3つの関数を定義する必要があります。1つ目は、新しいコメントが投稿されたときに、ウェブサポートオブジェクトの :meth:`~.WebSupport.add_comment` メソッドを呼び出すものです::

   @app.route('/docs/add_comment', methods=['POST'])
   def add_comment():
       parent_id = request.form.get('parent', '')
       node_id = request.form.get('node', '')
       text = request.form.get('text', '')
       proposal = request.form.get('proposal', '')
       username = g.user.name if g.user is not None else 'Anonymous'
       comment = support.add_comment(text, node_id='node_id',
                                     parent_id='parent_id',
                                     username=username, proposal=proposal)
       return jsonify(comment=comment)

.. You'll notice that both a `parent_id` and `node_id` are sent with the
   request. If the comment is being attached directly to a node, `parent_id`
   will be empty. If the comment is a child of another comment, then `node_id`
   will be empty. Then next function handles the retrieval of comments for a
   specific node, and is aptly named
   :meth:`~sphinx.websupport.WebSupport.get_data`:

リクエストには、 `parent_id` と `node_id` を送っています。コメントが他のノードに直接追加された場合には、 `parent_id` は空になります。また、コメントが他のコメントの子供として付加された場合には、 `node_id` が空になります。次の関数は、 :meth:`~sphinx.websupport.WebSupport.get_data` メソッドを利用して、特定のノードに対するコメントを取り扱います::

    @app.route('/docs/get_comments')
    def get_comments():
        username = g.user.name if g.user else None
        moderator = g.user.moderator if g.user else False
        node_id = request.args.get('node', '')
        data = support.get_data(parent_id, node_id)
        return jsonify(**data)

.. The final function that is needed will call :meth:`~.WebSupport.process_vote`,
   and will handle user votes on comments::

最後の関数は、 :meth:`~.WebSupport.process_vote` を呼び出して、コメントに対するユーザの投票を取り扱う関数です::

   @app.route('/docs/process_vote', methods=['POST'])
   def process_vote():
       if g.user is None:
           abort(401)
       comment_id = request.form.get('comment_id')
       value = request.form.get('value')
       if value is None or comment_id is None:
           abort(400)
       support.process_vote(comment_id, g.user.id, value)
       return "success"


.. Comment Moderation
   ~~~~~~~~~~~~~~~~~~

コメントのモデレート
~~~~~~~~~~~~~~~~~~~~

.. By default, all comments added through :meth:`~.WebSupport.add_comment` are
   automatically displayed.  If you wish to have some form of moderation, you can
   pass the `displayed` keyword argument:

デフォルトでは、 :meth:`~.WebSupport.add_comment` を使って追加したすべてのコメントは表示されます。もし、モデレーションを行って、承認されたコメントだけを表示したいのであれば、 `displayed` キーワード引数を渡します::

   comment = support.add_comment(text, node_id='node_id',
                                 parent_id='parent_id',
                                 username=username, proposal=proposal,
                                 displayed=False)

.. You can then create a new view to handle the moderation of comments.  It
   will be called when a moderator decides a comment should be accepted and
   displayed::

コメントのモデレートを取り扱うビューを追加する必要があります。モデレータがコメントを受け入れて、表示するかどうかを決定するときに、この関数が呼び出されます::

   @app.route('/docs/accept_comment', methods=['POST'])
   def accept_comment():
       moderator = g.user.moderator if g.user else False
       comment_id = request.form.get('id')
       support.accept_comment(comment_id, moderator=moderator)
       return 'OK'

.. Rejecting comments happens via comment deletion.

リジェクトされると、コメントは削除されます。

.. To perform a custom action (such as emailing a moderator) when a new comment is
   added but not displayed, you can pass callable to the :class:`~.WebSupport`
   class when instantiating your support object:

非表示の新しいコメントが追加されたときに、Eメールによるモデレートなど、カスタムのアクションを行いたい場合には、 :class:`~.WebSupport` のインスタンスを作る時に、呼び出し可能なオブジェクトを渡します::

   def moderation_callback(comment):
       """Do something..."""

   support = WebSupport(..., moderation_callback=moderation_callback)

.. The moderation callback must take one argument, which will be the same comment
   dict that is returned by :meth:`add_comment`.

このコールバック関数は、 :meth:`add_comment` が返すのと同じ形式の辞書を引数として受け取ります。

