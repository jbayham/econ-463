---
layout: page
title: Modules
permalink: /modules/
---

Lectures and materials will be organized by module here.

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
  <strong>📝 Problem Set:</strong>
  <ul>
    {% for a in modules.ps %}
      <li><a href="{{ site.url }}{{ site.baseurl }}/{{ modules.dirname }}/{{ a.url }}">{{ a.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}

{% if modules.materials %}
  <strong>Additional Materials:</strong>
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
