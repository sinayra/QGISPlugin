# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Hello
                                 A QGIS plugin
 Print Hello Wolrd message
                             -------------------
        begin                : 2018-02-22
        copyright            : (C) 2018 by Sinayra
        email                : sinayra@outlook.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Hello class from file Hello.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .hello import Hello
    return Hello(iface)
