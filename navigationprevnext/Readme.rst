####################
Navigation Prev/Next
####################

:author: Moisès Gómez Girón

This plug in adds the possibility to declare navigation information as
metadata.

It activates when *next-entry* tag is present in the entry.

The *next_entry* tag should be assigned to a filename with or without
category.

For example:

    :next_entry: mynextarticle.rst
    :next_entry: mycat/mynextarticle.rst

If no category is included, the same as the article is assumed.

The plug in will add the following metadata to the corresponding
article:

    :next_url:      url for the next article
    :next_title:    title of the next article

It also includes the following metadata on the next article:

    :prev_url:      url for the previous article
    :prev_title:    title of the previous article

