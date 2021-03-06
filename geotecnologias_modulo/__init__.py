# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MasterGeotecnologias
                                 A QGIS plugin
 Complemento de prueba para el Máster
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-04-15
        copyright            : (C) 2021 by Carmen Cabeza
        email                : u149666@usal.es
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
    """Load MasterGeotecnologias class from file MasterGeotecnologias.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Geotecnologias_modulo import MasterGeotecnologias
    return MasterGeotecnologias(iface)
