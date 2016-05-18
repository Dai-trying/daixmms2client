import xmmsfun

def pre_amp_change(var1):
    myself.lbl_pre_amp_2.setText(str(var1 / 10.0))
    xmmsfun.xmms_change_config_value("equalizer.preamp", str(var1 / 10.0))


def eq_32_changed(var1):
    myself.lbl_a1.setText(str(var1 / 10.0))
    xmmsfun.xmms_change_config_value("equalizer.gain00", str(var1 / 10.0))

def eq_64_changed(var1):
    myself.lbl_b1.setText(str(var1 / 10.0))
    xmmsfun.xmms_change_config_value("equalizer.gain01", str(var1 / 10.0))


def eq_128_changed(var1):
    myself.lbl_c1.setText(str(var1 / 10.0))
    xmmsfun.xmms_change_config_value("equalizer.gain02", str(var1 / 10.0))


def eq_256_changed(var1):
    myself.lbl_d1.setText(str(var1 / 10.0))
    xmmsfun.xmms_change_config_value("equalizer.gain03", str(var1 / 10.0))


def eq_512_changed(var1):
    myself.lbl_e1.setText(str(var1 / 10.0))
    xmmsfun.xmms_change_config_value("equalizer.gain04", str(var1 / 10.0))


def eq_1k_changed(var1):
    myself.lbl_f1.setText(str(var1 / 10.0))
    xmmsfun.xmms_change_config_value("equalizer.gain05", str(var1 / 10.0))


def eq_2k_changed(var1):
    myself.lbl_g1.setText(str(var1 / 10.0))
    xmmsfun.xmms_change_config_value("equalizer.gain06", str(var1 / 10.0))


def eq_4k_changed(var1):
    myself.lbl_h1.setText(str(var1 / 10.0))
    xmmsfun.xmms_change_config_value("equalizer.gain07", str(var1 / 10.0))


def eq_8k_changed(var1):
    myself.lbl_i1.setText(str(var1 / 10.0))
    xmmsfun.xmms_change_config_value("equalizer.gain08", str(var1 / 10.0))


def eq_16k_changed(var1):
    myself.lbl_j1.setText(str(var1 / 10.0))
    xmmsfun.xmms_change_config_value("equalizer.gain09", str(var1 / 10.0))


def set_eq_enabled():
    myself.eq_h_slider_1.setDisabled(False)
    myself.eq_h_slider_1.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.preamp").value()) * 10))
    myself.v_slider_a.setDisabled(False)
    myself.v_slider_a.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain00").value()) * 10))
    myself.v_slider_b.setDisabled(False)
    myself.v_slider_b.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain01").value()) * 10))
    myself.v_slider_c.setDisabled(False)
    myself.v_slider_c.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain02").value()) * 10))
    myself.v_slider_d.setDisabled(False)
    myself.v_slider_d.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain03").value()) * 10))
    myself.v_slider_e.setDisabled(False)
    myself.v_slider_e.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain04").value()) * 10))
    myself.v_slider_f.setDisabled(False)
    myself.v_slider_f.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain05").value()) * 10))
    myself.v_slider_g.setDisabled(False)
    myself.v_slider_g.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain06").value()) * 10))
    myself.v_slider_h.setDisabled(False)
    myself.v_slider_h.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain07").value()) * 10))
    myself.v_slider_i.setDisabled(False)
    myself.v_slider_i.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain08").value()) * 10))
    myself.v_slider_j.setDisabled(False)
    myself.v_slider_j.setValue(int(float(xmmsfun.xmms_get_config_value("equalizer.gain09").value()) * 10))


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


def eq_enabled():
    if myself.enable_button.isChecked() == True:
        xmmsfun.xmms_change_config_value("equalizer.enabled", "0")
        set_eq_disabled()
    else:
        xmmsfun.xmms_change_config_value("equalizer.enabled", "1")
        xmmsfun.xmms_change_config_value("equalizer.use_legacy", "0")
        set_eq_enabled()
