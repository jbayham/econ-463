---
layout: page
title: Modules
permalink: /modules/
---

Lecture slides, student readers, R examples, and data are organized by module below. Reading page numbers refer to the printed pages in the course editions.

<ul id="archive">
{% for modules in site.data.modules %}
      <li class="archiveposturl">
        {% if modules.filename %}
        <span><a href="{{ site.url }}{{ site.baseurl }}/{{ modules.dirname }}/{{ modules.filename }}.pdf">{{ modules.title }}</a></span>
        {% else %}
        <span>{{ modules.title }}</span>
        {% endif %}<br>
<span class = "postlower">
{{ modules.desc }}</span>
{% if modules.readings %}
  <br><strong>📖 Readings:</strong>
  <ul>
    {% for r in modules.readings %}
      <li>{{ r.title }}</li>
    {% endfor %}
  </ul>
{% endif %}

{% if modules.ps %}
  <strong>📝 Problem Sets:</strong>
  <ul>
    {% for a in modules.ps %}
      <li><a href="{{ site.url }}{{ site.baseurl }}/{{ modules.dirname }}/{{ a.url }}">{{ a.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}

{% if modules.materials %}
  <strong>Materials:</strong>
  <ul>
    {% for c in modules.materials %}
      <li><a href="{{ site.url }}{{ site.baseurl }}/{{ modules.dirname }}/{{ c.url }}">{{ c.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}

<br>
      </li>
{% endfor %}
</ul>
