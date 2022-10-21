from typing import Dict, Any
from .constants import CSS_STYLE

HTML = f"""
<html>
    {CSS_STYLE}
    <head>
        <title>Cyphers</title>
    </head>
    <h2>Cyphers</h2>
    <body>
        %PLUGINS%
    </body>
</html>
"""
def render(input: Dict[str, Any]) -> str:
    table_plugins = """<table cellspacing=0 cellpadding=0>
    <thead><tr>
        <td>ID</td>
        <td>PLUGIN</td>
    </tr></thead>
    """
    for k in input['plugins']:
        table_plugins += f"""
        <tr>
            <td>{k['key']}</td>
            <td>{k['name']}</td>
        </tr>
        """
    table_plugins += "</table>"
    rendered = HTML.replace("%PLUGINS%",table_plugins)
    return rendered

