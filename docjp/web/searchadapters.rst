.. _searchadapters:

.. currentmodule:: sphinx.websupport.search

.. Search Adapters
   ===============

検索アダプタ
============

.. To create a custom search adapter you will need to subclass the
   :class:`BaseSearch` class.  Then create an instance of the new class and pass
   that as the `search` keyword argument when you create the :class:`~.WebSupport`
   object:

カスタムの検索アダプタを作成したい場合にには、 :class:`BaseSearch` クラスのサブクラスを作成する必要があります。その後、新しいクラスのインスタンスを作成し、 :class:`~.WebSupport` オブジェクトのを作る時に、 `search` キーワード引数で渡します::

   support = WebSupport(srcdir=srcdir,
                        builddir=builddir,
                        search=MySearch())

.. For more information about creating a custom search adapter, please see the
   documentation of the :class:`BaseSearch` class below.

カスタムの検索アダプタを作る際のより詳しい情報は、これから説明する :class:`BaseSearch` クラスのドキュメントを参照してください。

.. class:: BaseSearch

   .. Defines an interface for search adapters.

   検索アダプタのインタフェースを定義しています。


.. BaseSearch Methods
   ~~~~~~~~~~~~~~~~~~

BaseSearchのメソッド
~~~~~~~~~~~~~~~~~~~~

   .. The following methods are defined in the BaseSearch class. Some methods do
      not need to be overridden, but some (:meth:`~BaseSearch.add_document` and
      :meth:`~BaseSearch.handle_query`) must be overridden in your subclass. For a
      working example, look at the built-in adapter for whoosh.

   これらのメソッドがBaseSearchクラスに定義されています。いくつかのメソッドはオーバーライドする必要はありませんが、サブクラスでオーバーライドしなければならないもの(:meth:`~BaseSearch.add_document` , :meth:`~BaseSearch.handle_query`)もあります。組み込みのwhoosh検索アダプタが、動作可能なサンプルとなっています。

.. automethod:: BaseSearch.init_indexing

.. automethod:: BaseSearch.finish_indexing

.. automethod:: BaseSearch.feed

.. automethod:: BaseSearch.add_document

.. automethod:: BaseSearch.query

.. automethod:: BaseSearch.handle_query

.. automethod:: BaseSearch.extract_context
