#-*- encoding:utf-8 *-
from plone import tiles
from plone import api
from plone.app.uuid.utils import uuidToObject
from collective.tiles.iframembed.interfaces import IIFrameEmbedTilesSettings


class FrameEmbedTile(tiles.PersistentTile):

    def iframe_validation(self):
        url_to_embed = self.data.get('url_to_embed')
        if not url_to_embed:
            return False

        valid_domains = api.portal.get_registry_record(
            'available_domains',
            interface=IIFrameEmbedTilesSettings)

        for domain in valid_domains:
            if url_to_embed.find(domain) != -1:
                return True

        api.portal.show_message("L'url indicato non e' valido per i domini ammessi", self.request, 'error')
        return False
