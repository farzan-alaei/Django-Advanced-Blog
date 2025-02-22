{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ name }}
{% endblock %}

{% block html %}
This is an <strong>html</strong> message.
<img src='https://www.w3schools.com/images/lamp.jpg'>
{% endblock %}
