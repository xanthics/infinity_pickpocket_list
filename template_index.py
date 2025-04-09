index = '''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{1} Pickpocket List</title>
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.9/brython.min.js"></script>
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.9/brython_stdlib.js"></script>
        <link href="css/layout.css" rel="stylesheet" type="text/css" />
        <link rel="shortcut icon" type="image/x-icon" href="favicon.ico">
    </head>
    <body onload="brython(1)">
        <section class="main">
            <p>Stealing from a store is 1% chance of success per point above store skill, capping at 100%.  EG if the store has 15, then 16 gives you 1% chance to succeed.</p>
            <p>Stealing from a target is 1% chance of success per point above target skill, minus 1%, capping at 99%. EG if the target has 15, then 17 gives you 1% chance to succeed. </p>
            <p>Slot difficulty is the minimum required skill for any chance of success on that item.</p>
            <p><a href="https://github.com/xanthics/infinity_pickpocket_list/issues/1">per this conversation</a></p>
            <div id="show_hide"></div>
            <div id="loading">
                This page requires javascript in order to work correctly.
                <br><br>
                This page may take a moment to load.
            </div>
            <span id="table_view"></span><span id="options"></span>
 			<div id="buttons"></div>
			<div id="pages">
                <section id="Table">
                    <table id="pick_data" >
                        <thead id="nav_target" b-on="click:sort">
                            <tr>
                                <th b-code="for field in header:">
                                        {{field}} <span class="arrows">&uparrow;&downarrow;</span>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr b-code="for item in items">
                                <td b-code="for field in item:">{{field}}</td>
                            </tr>
                        </tbody>
                    </table>
                </section>
            </div>
            <div id="opts" style="display: none;"></div>
            <p><a href="https://github.com/xanthics/infinity_pickpocket_list/discussions" target="_blank">Suggestions</a><br /><a href="https://github.com/xanthics/infinity_pickpocket_list/issues" target="_blank">Bugs</a></p>
            <div id="sponsor">
                <div id="github_image"><a href="https://github.com/sponsors/xanthics"><img alt="Sponsor me on Github!" src="img/github_sponsor.png" class="sponsor_img"></a></div>
                <div id="patreon_image"><a href="https://www.patreon.com/xanthics"><img alt="Become a Patron!" src="img/become_a_patron_button@2x.png" class="sponsor_img"></a></div>
            </div>
        </section>
        <script type="text/python" src="{0}_handle_page.py"></script>
    </body>
</html>'''
