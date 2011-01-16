.. _websupportapi:

.. currentmodule:: sphinx.websupport

.. The WebSupport Class
   ====================

WebSupportクラス
================

.. class:: WebSupport

   .. The main API class for the web support package.  All interactions with the
      web support package should occur through this class.

   ウェブサポートパッケージのメインとなるAPIクラスです。ウェブサポートパッケージに対して行われる、すべてのインタラクションは、このクラスを通じて行われます。

   .. The class takes the following keyword arguments:

   このクラスは、次のようなキーワード引数を取ります:

   srcdir
      reStructuredTextのソースファイルを含むディレクトリです。

      .. The directory containing reStructuredText source files.

   builddir
      ビルド済みのデータや、静的ファイルを置くべきディレクトリです。これはデータをビルドする :class:`WebSupport` オブジェクトを作る時に使用されます。

      .. The directory that build data and static files should be placed in.  This
         should be used when creating a :class:`WebSupport` object that will be
         used to build data.

   datadir
      ウェブサポートのデータが置かれるディレクトリです。このデータを読み込む :class:`WebSupport` オブジェクトが作成されるときに使用されます。

      .. The directory that the web support data is in.  This should be used when
         creating a :class:`WebSupport` object that will be used to retrieve data.


   search
      これは組み込みの検索アダプタを参照するための文字列(例: 'xapian')か、 :class:`~.search.BaseSearch` クラスのサブクラスのインスタンスを指定します。

      .. This may contain either a string (e.g. 'xapian') referencing a built-in
          search adapter to use, or an instance of a subclass of
          :class:`~.search.BaseSearch`.

   storage
       これはデータベースのURIを表す文字列、もしくは :class:`~.storage.StorageBackend` のサブクラスのインスタンスを指定します。もしどちらも指定されなかった場合には、新しいsqliteデータベースが作られます。

       .. This may contain either a string representing a database uri, or an
          instance of a subclass of :class:`~.storage.StorageBackend`.  If this is
          not provided, a new sqlite database will be created.

   moderation_callback
      非表示の新しいコメントが追加されたときに呼び出されるコールバックです。この関数には、追加されたコメントを表す引数が1つ渡されます。

      .. A callable to be called when a new comment is added that is not
         displayed.  It must accept one argument: a dictionary representing the
         comment that was added.

   staticdir
      静的ファイルが提供される場所が、 ``'/tatic'`` 以外の場合には、その場所の名前を表す文字列(例: ``'/static_files'``)を指定します。

      .. If static files are served from a location besides ``'/static'``, this
         should be a string with the name of that location
         (e.g. ``'/static_files'``).

   docroot
      ドキュメントがURLのベースパスから送信されない場合には、そのパスを表す文字(例: ``'docs'``)を指定します。

      .. If the documentation is not served from the base path of a URL, this
         should be a string specifying that path (e.g. ``'docs'``).


.. Methods
   ~~~~~~~

メソッド
~~~~~~~~

.. automethod:: sphinx.websupport.WebSupport.build

.. automethod:: sphinx.websupport.WebSupport.get_document

.. automethod:: sphinx.websupport.WebSupport.get_data

.. automethod:: sphinx.websupport.WebSupport.add_comment

.. automethod:: sphinx.websupport.WebSupport.process_vote

.. automethod:: sphinx.websupport.WebSupport.get_search_results
