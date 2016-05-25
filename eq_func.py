
#  Copyright 2016 by Dai Trying
#
#  This file is part of daixmms2client.
#
#     daixmms2client is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     daixmms2client is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with daixmms2client.  If not, see <http://www.gnu.org/licenses/>.


import xmmsfun

sliders = ["preamp", "gain00", "gain01", "gain02", "gain03", "gain04", "gain05", "gain06", "gain07", "gain08",
           "gain09", "gain10", "gain11", "gain12", "gain13", "gain14"]


def set_eq_enabled():
    try:
        for slide in sliders:
            this_ref = eval("myself." + slide + "_slider")
            this_ref.setDisabled(False)
            this_ref.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer." + slide)) * 10))
    except AttributeError:
        print("Error setting equalizer")
        set_eq_disabled()


def set_eq_disabled():
    for slide in sliders:
        this_ref = eval("myself." + slide + "_slider")
        this_ref.setDisabled(True)


def toggle_equalizer():
    is_on = xmmsfun.xmms_get_config_value("equalizer.enabled")
    if myself.enable_button.isChecked():
        if is_on is False:
            myself.enable_button.setChecked(False)
            return
        if is_on == "0":
            xmmsfun.xmms_change_config_value("equalizer.enabled", "1")
        if xmmsfun.xmms_get_config_value("equalizer.use_legacy") == "1":
            xmmsfun.xmms_change_config_value("equalizer.use_legacy", "0")
        set_eq_enabled()
    else:
        if is_on == "1":
            xmmsfun.xmms_change_config_value("equalizer.enabled", "0")
        set_eq_disabled()
