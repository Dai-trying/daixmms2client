
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


def pre_amp_change(var1):
    if xmmsfun.xmms_change_config_value("equalizer.preamp", str(var1 / 10.0)):
        myself.lbl_pre_amp_2.setText(str(var1 / 10.0))

def eq_25_changed(var1):
    if xmmsfun.xmms_change_config_value("equalizer.gain00", str(var1 / 10.0)):
        myself.lbl_a1.setText(str(var1 / 10.0))


def eq_40_changed(var1):
    if xmmsfun.xmms_change_config_value("equalizer.gain01", str(var1 / 10.0)):
        myself.lbl_b1.setText(str(var1 / 10.0))


def eq_63_changed(var1):
    if xmmsfun.xmms_change_config_value("equalizer.gain02", str(var1 / 10.0)):
        myself.lbl_c1.setText(str(var1 / 10.0))


def eq_100_changed(var1):
    if xmmsfun.xmms_change_config_value("equalizer.gain03", str(var1 / 10.0)):
        myself.lbl_d1.setText(str(var1 / 10.0))


def eq_160_changed(var1):
    if xmmsfun.xmms_change_config_value("equalizer.gain04", str(var1 / 10.0)):
        myself.lbl_e1.setText(str(var1 / 10.0))


def eq_250_changed(var1):
    if xmmsfun.xmms_change_config_value("equalizer.gain05", str(var1 / 10.0)):
        myself.lbl_f1.setText(str(var1 / 10.0))


def eq_400_changed(var1):
    if xmmsfun.xmms_change_config_value("equalizer.gain06", str(var1 / 10.0)):
        myself.lbl_g1.setText(str(var1 / 10.0))


def eq_630_changed(var1):
    if xmmsfun.xmms_change_config_value("equalizer.gain07", str(var1 / 10.0)):
        myself.lbl_h1.setText(str(var1 / 10.0))


def eq_1k_changed(var1):
    if xmmsfun.xmms_change_config_value("equalizer.gain08", str(var1 / 10.0)):
        myself.lbl_i1.setText(str(var1 / 10.0))


def eq_1_6k_changed(var1):
    if xmmsfun.xmms_change_config_value("equalizer.gain09", str(var1 / 10.0)):
        myself.lbl_j1.setText(str(var1 / 10.0))


def eq_2_5k_changed(var1):
    if xmmsfun.xmms_change_config_value("equalizer.gain10", str(var1 / 10.0)):
        myself.lbl_k1.setText(str(var1 / 10.0))


def eq_4k_changed(var1):
    if xmmsfun.xmms_change_config_value("equalizer.gain11", str(var1 / 10.0)):
        myself.lbl_l1.setText(str(var1 / 10.0))


def eq_6_3k_changed(var1):
    if xmmsfun.xmms_change_config_value("equalizer.gain12", str(var1 / 10.0)):
        myself.lbl_m1.setText(str(var1 / 10.0))


def eq_10k_changed(var1):
    if xmmsfun.xmms_change_config_value("equalizer.gain13", str(var1 / 10.0)):
        myself.lbl_n1.setText(str(var1 / 10.0))


def eq_16k_changed(var1):
    if xmmsfun.xmms_change_config_value("equalizer.gain14", str(var1 / 10.0)):
        myself.lbl_o1.setText(str(var1 / 10.0))


def set_eq_enabled():
    print("gathering and applying settings")
    try:
        myself.eq_h_slider_1.setDisabled(False)
        myself.eq_h_slider_1.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.preamp")) * 10))
        myself.v_slider_a.setDisabled(False)
        myself.v_slider_a.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain00")) * 10))
        myself.v_slider_b.setDisabled(False)
        myself.v_slider_b.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain01")) * 10))
        myself.v_slider_c.setDisabled(False)
        myself.v_slider_c.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain02")) * 10))
        myself.v_slider_d.setDisabled(False)
        myself.v_slider_d.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain03")) * 10))
        myself.v_slider_e.setDisabled(False)
        myself.v_slider_e.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain04")) * 10))
        myself.v_slider_f.setDisabled(False)
        myself.v_slider_f.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain05")) * 10))
        myself.v_slider_g.setDisabled(False)
        myself.v_slider_g.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain06")) * 10))
        myself.v_slider_h.setDisabled(False)
        myself.v_slider_h.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain07")) * 10))
        myself.v_slider_i.setDisabled(False)
        myself.v_slider_i.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain08")) * 10))
        myself.v_slider_j.setDisabled(False)
        myself.v_slider_j.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain09")) * 10))
        myself.v_slider_k.setDisabled(False)
        myself.v_slider_k.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain10")) * 10))
        myself.v_slider_l.setDisabled(False)
        myself.v_slider_l.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain11")) * 10))
        myself.v_slider_m.setDisabled(False)
        myself.v_slider_m.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain12")) * 10))
        myself.v_slider_n.setDisabled(False)
        myself.v_slider_n.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain13")) * 10))
        myself.v_slider_o.setDisabled(False)
        myself.v_slider_o.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain14")) * 10))
    except AttributeError:
        print("Error setting equalizer")
        set_eq_disabled()


def set_eq_disabled():
    myself.eq_h_slider_1.setDisabled(True)
    myself.v_slider_a.setDisabled(True)
    myself.v_slider_b.setDisabled(True)
    myself.v_slider_c.setDisabled(True)
    myself.v_slider_d.setDisabled(True)
    myself.v_slider_e.setDisabled(True)
    myself.v_slider_f.setDisabled(True)
    myself.v_slider_g.setDisabled(True)
    myself.v_slider_h.setDisabled(True)
    myself.v_slider_i.setDisabled(True)
    myself.v_slider_j.setDisabled(True)
    myself.v_slider_k.setDisabled(True)
    myself.v_slider_l.setDisabled(True)
    myself.v_slider_m.setDisabled(True)
    myself.v_slider_n.setDisabled(True)
    myself.v_slider_o.setDisabled(True)
    myself.enable_button.setChecked(False)


def toggle_equalizer():
    if myself.enable_button.isChecked():
        if xmmsfun.xmms_get_config_value("equalizer.enabled") == "0":
            if xmmsfun.xmms_change_config_value("equalizer.enabled", "1"):
                print("equalizer enabled")
            else:
                myself.enable_button.setChecked(False)
                return
        if xmmsfun.xmms_get_config_value("equalizer.use_legacy") == "1":
            if xmmsfun.xmms_change_config_value("equalizer.use_legacy", "0"):
                pass
        set_eq_enabled()
    else:
        if xmmsfun.xmms_get_config_value("equalizer.enabled") == "1":
            xmmsfun.xmms_change_config_value("equalizer.enabled", "0")
        set_eq_disabled()
