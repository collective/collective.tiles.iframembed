from collective.tiles.iframembed.setuphandlers import post_install
from plone import api


def add_default_domains(context):
    """ """
    context.runAllImportStepsFromProfile('profile-collective.tiles.iframembed:cleanup')
    post_install(context)
