---
title: "Blog"
permalink: /blog/
layout: single
---
Welcome to my blog.

Here I write about travel, research, and notes. I jot down my experiences, some fun facts, some random thoughts. This is just a dumping yard.
---
## Kerala Series
{% assign kerala_posts = site.posts | where_exp: "p", "p.categories contains 'kerala'" %}
{% for post in kerala_posts %}
  {% include archive-single.html %}
{% endfor %}