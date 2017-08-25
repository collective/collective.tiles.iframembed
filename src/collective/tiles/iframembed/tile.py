#-*- encoding:utf-8 *-
from plone import tiles
from plone.app.uuid.utils import uuidToObject


class FrameEmbedTile(tiles.PersistentTile):

    @property
    def get_domain(self):
        domain = self.data.get('domain_to_embed')
        if not domain:
            return ''
        if domain.find('http') == -1:
            return 'http://%s' % domain
        return domain
