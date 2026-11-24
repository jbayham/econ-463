---
layout: page
title: Modules
permalink: /modules/
---

See the [course schedule]({{ '/schedule/' | relative_url }}) for reading dates.

<ul id="archive">
{% assign sections = 'Required reading|Materials|Supplemental reading|Optional reading' | split: '|' %}
{% for modules in site.data.modules %}
  <li class="archiveposturl">
  <h2 class="module-title">
    {% if modules.filename %}
      <a href="{{ site.url }}{{ site.baseurl }}/{{ modules.dirname }}/{{ modules.filename }}.pdf">{{ modules.title }}</a>
    {% else %}
      {{ modules.title }}
    {% endif %}
  </h2>
{% if modules.desc %}
  <span class="postlower">{{ modules.desc }}</span>
{% endif %}
{% for section in sections %}
  {% if section == 'Materials' %}
    {% assign entries = modules.materials %}
  {% else %}
    {% assign entries = modules.readings[section] %}
  {% endif %}
  {% if entries.size > 0 %}
    <div><strong>{{ section }}</strong></div>
    <ul>
      {% for entry in entries %}
        {% if section == 'Materials' %}
          <li><a href="{% unless entry.url contains '://' %}{{ site.url }}{{ site.baseurl }}/{{ modules.dirname }}/{% endunless %}{{ entry.url }}">{{ entry.title }}</a></li>
        {% else %}
          {% assign source = site.data.readings[entry.source] %}
          <li>{% if source.url %}<a href="{{ source.url | escape }}">{{ source.title | escape }}</a>{% else %}{{ source.title | escape }}{% endif %} — {{ entry.selection | escape }}</li>
        {% endif %}
      {% endfor %}
    </ul>
  {% endif %}
{% endfor %}

{% if modules.ps %}
  <strong>📝 Problem Sets:</strong>
  <ul>
    {% for a in modules.ps %}
      <li><a href="{{ site.url }}{{ site.baseurl }}/{{ modules.dirname }}/{{ a.url }}">{{ a.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}

<br>
  </li>
{% endfor %}
</ul>
