# -*- coding: utf-8 -*-
"""
Navigation Plugin for Pelican
=============================

This plugin reads the source filename assigned to
metadata *next_entry* and translates it into the url of
the corresponding article.

"""
from pelican import signals
import os

def compose_entry_with_category(entry, category):
    """ returns entry prepending category if not already there """
    catpath = os.path.join(category, "")
    return entry if entry.startswith(catpath) else os.path.join(category, entry)

def translate_metaslug(generator):
    """ translate the references in source to final """
    articles = {}
    for article in generator.articles:
        articles[article.get_relative_source_path()] = article

    for article in articles.values():
        if hasattr(article, 'next_entry'):
            category_name = article.category.name
            next_entry = compose_entry_with_category(article.next_entry, category_name)
            next_article = articles.get(next_entry, None)
            if next_article == None:
                print "WARNING: next article %s not found for %s"%(next_article, article.get_relative_source_path())
                continue
            article.next_url = next_article.url
            article.next_title = next_article.title
            next_article.prev_url = article.url
            next_article.prev_title = article.title

def register():
    signals.article_generator_finalized.connect(translate_metaslug)

