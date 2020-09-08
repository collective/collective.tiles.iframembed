# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from plone import api


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'collective.tiles.iframembed:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something during the installation of this package
    USED_DOMAINS = api.portal.get_registry_record(
        'collective.tiles.iframembed.interfaces.IIFrameEmbedTilesSettings.available_domains'
    )

    if not USED_DOMAINS:
        USED_DOMAINS = ()

    DOMAINS = (
        u'https://www.facebook.com',
        u'https://www.youtube.com',
        u'https://www.regione.emilia-romagna.it',
        u'https://www2.regione.emilia-romagna.it',
    )

    FILTERED = [x for x in DOMAINS if x not in USED_DOMAINS]
    
    if not FILTERED:
        return

    USED_DOMAINS = USED_DOMAINS + tuple(FILTERED)

    api.portal.set_registry_record(
        'collective.tiles.iframembed.interfaces.IIFrameEmbedTilesSettings.available_domains',
        USED_DOMAINS
    )


def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('collectivetilesiframembed_uninstall.txt') is None:
        return
    # Do something during the uninstallation of this package
