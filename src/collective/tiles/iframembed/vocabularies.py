# -*- coding: utf-8 -*-
from plone import api
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from collective.tiles.iframembed.interfaces import IIFrameEmbedTilesSettings


class DomainsVocabulary(object):
    """
    Vocabulary factory
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        try:
            axes = api.portal.get_registry_record(
                'available_domains',
                interface=IIFrameEmbedTilesSettings)
        except KeyError:
            return SimpleVocabulary([])
        axes = sorted([x for x in axes])
        voc_values = [
            SimpleTerm(
                title=x,
                value=x.encode('utf-8'),
                token=x.encode('utf-8')) for x in axes]
        return SimpleVocabulary(voc_values)


DomainsVocabularyFactory = DomainsVocabulary()
