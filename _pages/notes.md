---
layout: archive
title: "Notes"
permalink: /notes/
classes: wide
---

{% assign grouped_notes = site.notes | group_by: "subject" %}

{% for group in grouped_notes %}
  <h2>{{ group.name }}</h2>

  <ul>
  {% for post in group.items %}
    <li>
      <a href="{{ post.url | relative_url }}"><strong>{{ post.title }}</strong></a>
      {% if post.date %}
        <small>— {{ post.date | date: "%B %d, %Y" }}</small>
      {% endif %}
    </li>
  {% endfor %}
  </ul>

  <hr>
{% endfor %}