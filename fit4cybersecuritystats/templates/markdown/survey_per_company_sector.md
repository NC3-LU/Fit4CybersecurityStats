## {{ instance_name }}

{% for section, score in stats_data.items() %}
    {{ section }} {{ score }}
{% endfor %}

![Chart description](generated_chart_with_bokeh.jpg)
