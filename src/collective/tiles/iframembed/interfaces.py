# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.app.textfield import RichText
from collective.tiles.iframembed import _
from zope import schema
from plone.supermodel import model
from zope.interface import Interface


class ICollectiveTilesIframembedLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IFrameEmbedTile(model.Schema):
    title = schema.TextLine(
        title=_('label_tile_title', u'Tile title'),
        required=True
    )

    domain_to_embed = schema.Choice(
        title=_('label_tile_domain', u'Domain'),
        description=_('help_tile_domain', u'Choose a domain to embed into a iframe'),
        required=False,
        vocabulary='collective.tiles.iframembed.vocabularies.DomainsVocabulary'
    )


class IIFrameEmbedTilesSettings(Interface):
    """ """
    available_domains = schema.Tuple(
        title=_(u'Allowed domains'),
        description=_(u"One value for row"),
        missing_value=None,

        value_type=schema.TextLine()
    )
