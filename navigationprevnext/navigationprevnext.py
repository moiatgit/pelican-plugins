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
    if os.path.dirname(entry) == "":
        composed_entry = os.path.join(category, entry)
    else:
        composed_entry = entry
    return composed_entry

def list_articles(generator):
    """ returns a dictionary with articles keyed by its relative source path """
    articles = {}
    for article in generator.articles:
        articles[article.get_relative_source_path()] = article
    return articles

def insert_prev_next(articles):
    """ insert prev/next information into articles """
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

def insert_top(articles):
    """ insert top information into articles """
    for article in articles.values():
        if hasattr(article, 'next_url') and not hasattr(article, 'prev_url'):
            top_url = article.url
            category_name = article.category.name
            next_entry = compose_entry_with_category(article.next_entry, category_name)
            current_article = articles.get(article.next_entry, None)
            while current_article != None:
                current_article.top_url = top_url
                current_article.top_title = "inici"
                if hasattr(current_article, 'next_entry'):
                    category_name = current_article.category.name
                    next_entry = compose_entry_with_category(current_article.next_entry, category_name)
                    current_article = articles.get(next_entry, None)
                else:
                    current_article = None

def translate_metaslug(generator):
    """ translate the references in source to final """
    articles = list_articles(generator)
    insert_prev_next(articles)
    insert_top(articles)

def register():
    signals.article_generator_finalized.connect(translate_metaslug)

