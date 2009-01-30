# This file is part of Moksha.
#
# Moksha is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Moksha is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Moksha.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2008, Red Hat, Inc.
# Authors: Luke Macken <lmacken@redhat.com>

import moksha
from moksha.api.menus import MokshaMenu, MokshaContextualMenu

class MokshaContextMenu(MokshaContextualMenu):

    def default(self, *args, **kw):
        return """
            <a rel="text">
                <img src="/images/moksha-icon.png" style="position:absolute;margin-top:-20px; margin-left:-25px;margin-bottom:10px"/><br/>
            </a>
            <a href="http://moksha.fedorahosted.org" target="_blank">Moksha Homepage</a>
            <a href="http://lmacken.fedorapeople.org/moksha/">Documentation</a>
            <a href="https://fedorahosted.org/moksha/report/3">Tickets</a>
            <a href="https://fedorahosted.org/moksha/">Wiki</a>
        """

class MokshaDefaultMenu(MokshaMenu):
    menus = ['Moksha', 'Applications', 'Widgets', 'Fedora']

    def applications(self, *args, **kw):
        menu = """
        <a rel="text">
            <img src="/images/gears.png" style="position:absolute;margin-top:-20px; margin-left:-25px;margin-bottom:10px"/><br>
        </a>
        """
        for app in moksha.apps:
            menu += '<a href="#">%s</a>' % moksha.apps[app]['name']
        return menu

    def widgets(self, *args, **kw):
        menu = """
        <a rel="text">
            <img src="/images/block.png" style="position:absolute;margin-top:-20px; margin-left:-25px;margin-bottom:10px"/>
            <br/>
        </a>
        """
        for id, widget in moksha._widgets.iteritems():
            menu += """
                <a href="#" onclick="$('<div/>').appendTo('#content').load('/widgets/%s'); return false;">%s</a>
            """ % (id, widget['name'])
        return menu

    def moksha(self, *args, **kw):
        return """
        <a rel="text">
            <img src="/images/moksha-icon.png" style="position:absolute;margin-top:-20px; margin-left:-25px;margin-bottom:10px"/><br>
            <br>Moksha is a platform for creating live collaborative web applications.<br><br>
        </a>
        <a rel="separator"></a>
        <a href="http://moksha.fedorahosted.org" target="_blank">Moksha Homepage</a>
        <a href="http://lmacken.fedorapeople.org/moksha/">Documentation</a>
        <a href="https://fedorahosted.org/moksha/report/3">Tickets</a>
        <a href="https://fedorahosted.org/moksha/">Wiki</a>
        """
