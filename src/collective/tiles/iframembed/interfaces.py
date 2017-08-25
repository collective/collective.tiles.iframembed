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

    # url_to_embed = schema.Choice(
    #     title=_('label_tile_domain', u'Domain'),
    #     description=_('help_tile_domain', u'Choose a domain to embed into a iframe'),
    #     required=False,
    #     vocabulary='collective.tiles.iframembed.vocabularies.DomainsVocabulary'
    # )

    url_to_embed = schema.TextLine(
        title=_('label_tile_width', u'Url to embed'),
        required=False
    )

    width = schema.TextLine(
        title=_('label_tile_width', u'Iframe width'),
        required=False
    )

    height = schema.TextLine(
        title=_('label_tile_heigth', u'Iframe height'),
        required=False
    )

    frameborder = schema.TextLine(
        title=_('label_tile_heigth', u'Iframe frameborder'),
        required=False
    )

    allowfullscreen = schema.TextLine(
        title=_('label_tile_heigth', u'Iframe allowfullscreen'),
        required=False
    )

    style = schema.TextLine(
        title=_('label_tile_heigth', u'Iframe style'),
        required=False
    )

    scrolling = schema.TextLine(
        title=_('label_tile_heigth', u'Iframe scrolling'),
        required=False
    )

    allowTransparency = schema.TextLine(
        title=_('label_tile_heigth', u'Iframe allowTransparency'),
        required=False
    )


class IIFrameEmbedTilesSettings(Interface):
    """ """
    available_domains = schema.Tuple(
        title=_(u'Allowed domains'),
        description=_(u"One value for row"),
        missing_value=None,

        value_type=schema.TextLine()
    )
