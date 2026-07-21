---
title: "Blog"
permalink: /blog/
layout: single
classes: wide
---

Welcome to my blog. Here I write about travel, research, thoughts, and experiences.

---

{% assign grouped_by_category = site.posts | group_by: "category" %}

{% for cat_group in grouped_by_category %}
{% if cat_group.name != "" %}

## {{ cat_group.name | capitalize }}

{% assign sub_grouped = cat_group.items | group_by: "subcategory" %}

{% for sub_group in sub_grouped %}

{% if sub_group.name != "" %}
### {{ sub_group.name }}
{% endif %}

{% for post in sub_group.items %}
* [{{ post.title }}]({{ post.url | relative_url }}){% if post.date %} — *{{ post.date | date: "%B %d, %Y" }}*{% endif %}
{% endfor %}

{% endfor %}

---

{% endif %}
{% endfor %}