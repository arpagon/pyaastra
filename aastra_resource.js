var prmpt1 = "New Password Invalid.";
var prmpt2 = "New password must be 10 characters or less.";
var prmpt3 = "New password must be numeric.";
var prmpt4 = "Error";
var prmpt5 = "New password and confirm password do not match.";
var prmpt6 = "Are you sure you want to restart the phone?";
var prmpt7 = "This will restore the phone to default settings and cannot be undone.";
var prmpt8 = "Continue";
var prmpt9 = "This will remove the local configuration settings and cannot be undone.";
var prmpt10 = "Error: Intercom Settings";
var prmpt11 = "Please enter a prefix code for server-side intercom.";
var prmpt12 = "Value must be between";
var prmpt13 = "DSCP value";
var prmpt14 = "is mapped to multiple priorities.";
var prmpt15 = "Invalid IP address";
var prmpt16 = "Invalid subnet mask";
var prmpt17 = "Invalid gateway address";
var prmpt18 = "Invalid primary DNS address";
var prmpt19 = "Invalid secondary DNS address";
var disableNonippri = false;
var disableVlanid0 = false;
var disableSippri = false;
var disableRtppri = false;
var disableRtcppri = false;
var disableVlanid1 = false;
var disablePortlpri = false;
var disableHttpsExpires = false;
var disableHttpsHostname = false;
var disableIntercomPrefix = false;
var disableIntercomLine = false;
var disableNatIp = false;
var disableMWISub = false;
var disableDLprot = false;
var disableTFTPserver = false;
var disableTFTPpath = false;
var disableTFTPalt = false;
var disableTFTPaltpath = false;
var disableTFTPusealt = false;
var disableFTPserver = false;
var disableFTPpath = false;
var disableFTPusername = false;
var disableFTPpassword = false;
var disableHTTPserver = false;
var disableHTTPpath = false;
var disableHTTPport = false;
var disableHTTPSserver = false;
var disableHTTPSpath = false;
var disableHTTPSport = false;
var disableIPField = false;
var disableSMField = false;
var disableDGField = false;
var disableDNS1Field = false;
var disableDNS2Field = false;
var adNumberDisable = new Array();
var adTimeoutDisable = new Array();
adNumberDisable[0] = false;
adTimeoutDisable[0] = false;
adNumberDisable[1] = false;
adTimeoutDisable[1] = false;
adNumberDisable[2] = false;
adTimeoutDisable[2] = false;
adNumberDisable[3] = false;
adTimeoutDisable[3] = false;
adNumberDisable[4] = false;
adTimeoutDisable[4] = false;
adNumberDisable[5] = false;
adTimeoutDisable[5] = false;
adNumberDisable[6] = false;
adTimeoutDisable[6] = false;
adNumberDisable[7] = false;
adTimeoutDisable[7] = false;
adNumberDisable[8] = false;
adTimeoutDisable[8] = false;
var TimeSrvDisable = new Array();
TimeSrvDisable[0] = false;
TimeSrvDisable[1] = false;
TimeSrvDisable[2] = false;
var PriorityAlertDisable = new Array();
PriorityAlertDisable[0] = false;
PriorityAlertDisable[1] = false;
PriorityAlertDisable[2] = false;
var disableDNSField = true;
var js_is_9112 = false;
var js_lldp_use_vlan_info = false;

function updateFirmwareTable(i) {
    var f = document.getElementById('fwUpgradeForm');
    f.port.disabled = true;
    f.username.disabled = true;
    f.password.disabled = true;
    switch (i) {
    case 1:
        f.username.disabled = false;
        f.password.disabled = false;
        break;
    case 2:
    case 3:
        f.port.disabled = false;
        break
    }
}

function resetServerTable(f) {
    f.protocol.disabled = true;
    f.tftp.disabled = true;
    f.tftppath.disabled = true;
    f.ftpserv.disabled = true;
    f.ftppath.disabled = true;
    f.ftpuser.disabled = true;
    f.ftppass.disabled = true;
    f.httpserv.disabled = true;
    f.httppath.disabled = true;
    f.httpport.disabled = true;
    f.httpsserv.disabled = true;
    f.httpspath.disabled = true;
    f.httpsport.disabled = true
}

function updateServerTable(i) {
    var f = document.getElementById('configForm');
    resetServerTable(f);
    f.protocol.disabled = disableDLprot;
    f.alttftp.disabled = disableTFTPalt;
    f.alttftppath.disabled = disableTFTPaltpath;
    f.usealttftp.disabled = disableTFTPusealt;
    switch (i) {
    case 0:
        f.tftp.disabled = disableTFTPserver;
        f.tftppath.disabled = disableTFTPpath;
        break;
    case 1:
        f.ftpserv.disabled = disableFTPserver;
        f.ftppath.disabled = disableFTPpath;
        f.ftpuser.disabled = disableFTPusername;
        f.ftppass.disabled = disableFTPpassword;
        break;
    case 2:
        f.httpserv.disabled = disableHTTPserver;
        f.httppath.disabled = disableHTTPpath;
        f.httpport.disabled = disableHTTPport;
        break;
    case 3:
        f.httpsserv.disabled = disableHTTPSserver;
        f.httpspath.disabled = disableHTTPSpath;
        f.httpsport.disabled = disableHTTPSport;
        break
    }
}

function validatePassword() {
    var f = document.getElementById('passwordForm');
    var a = f.newPassword.value;
    var b = f.confirmPassword.value;
    if (a.length > 10) {
        alert(prmpt1 + "\n" + prmpt2);
        return false
    }
    for (i = 0; i < a.length; i++) {
        if (isNaN(a.charAt(i))) {
            alert(prmpt1 + "\n" + prmpt3);
            return false
        }
    }
    if (a != b) {
        alert(prmpt4 + "\n" + prmpt5);
        return false
    }
    return true
}

function confirmReset(t) {
    var a;
    var f = document.getElementById('resetForm');
    switch (t) {
    case 0:
        a = prmpt6;
        break;
    case 1:
        a = prmpt7 + "\n" + prmpt8 + "?";
        break;
    case 2:
        a = prmpt9 + "\n" + prmpt8 + "?"
    }
    if (confirm(a)) {
        f.resetOption.value = t;
        f.submit()
    }
}

function updateBasicNetworkSettings(a) {
    var b = document.getElementById('networkSettingsForm');
    if (a) {
        b.ip.disabled = true;
        b.subnet.disabled = true;
        b.gateway.disabled = true;
        b.dns1.disabled = disableDNSField || disableDNS1Field;
        b.dns2.disabled = disableDNSField || disableDNS2Field
    } else {
        b.ip.disabled = disableIPField;
        b.subnet.disabled = disableSMField;
        b.gateway.disabled = disableDGField;
        b.dns1.disabled = disableDNS1Field;
        b.dns2.disabled = disableDNS2Field
    }
}

function updateAutodialSetting(a, b) {
    var c = document.getElementById('sipLineSettingsForm');
    if (a) {
        c.adNumber.disabled = true;
        c.adTimeout.disabled = true
    } else {
        c.adNumber.disabled = adNumberDisable[b];
        c.adTimeout.disabled = adTimeoutDisable[b]
    }
}

function updatePriorityAlert() {
    var a = document.getElementById('preferencesForm');
    if (a && a.prioAlertingEn) {
        var b = a.prioAlertingEn.checked;
        a.palertingkeyword1.disabled = (b != true) || PriorityAlertDisable[0];
        a.palertingkeyword2.disabled = (b != true) || PriorityAlertDisable[1];
        a.palertingkeyword3.disabled = (b != true) || PriorityAlertDisable[2];
        a.palertingkeyword4.disabled = (b != true) || PriorityAlertDisable[3];
        a.palertingkeyword5.disabled = (b != true) || PriorityAlertDisable[4];
        a.palertingkeyword6.disabled = (b != true) || PriorityAlertDisable[5];
        a.palertingkeyword7.disabled = (b != true) || PriorityAlertDisable[6];
        a.palertingkeyword8.disabled = (b != true) || PriorityAlertDisable[7];
        a.palertingkeyword9.disabled = (b != true) || PriorityAlertDisable[8];
        a.palertingkeyword10.disabled = (b != true) || PriorityAlertDisable[9]
    }
}

function updateIntercomPrefix() {
    var a = document.getElementById('preferencesForm');
    if (a && a.intercomType) {
        var b = a.intercomType.selectedIndex;
        a.intercomPrefixCode.disabled = (b != 1) || disableIntercomPrefix;
        a.intercomLine.disabled = (b == 2) || disableIntercomLine
    }
}

function checkIntercomSetting() {
    var a = document.getElementById('preferencesForm');
    if (a && a.intercomType && a.intercomPrefixCode) {
        var b = a.intercomType.selectedIndex;
        var c = a.intercomPrefixCode.value;
        if (b == 1 && c == '') {
            alert(prmpt10 + "\n" + prmpt11);
            return false
        }
    }
    return true
}

function updateTimeServers(a) {
    var b = document.getElementById('preferencesForm');
    b.timeSrv1.disabled = !a || TimeSrvDisable[0];
    b.timeSrv2.disabled = !a || TimeSrvDisable[1];
    b.timeSrv3.disabled = !a || TimeSrvDisable[2]
}

function updateVlanSettings(a) {
    var b = document.getElementById('networkSettingsForm');
    b.nonippri.disabled = (!a && !js_lldp_use_vlan_info) || disableNonippri;
    b.vlanid0.disabled = !a || js_lldp_use_vlan_info || disableVlanid0;
    b.sippri.disabled = !a || js_lldp_use_vlan_info || disableSippri;
    b.rtppri.disabled = !a || js_lldp_use_vlan_info || disableRtppri;
    b.rtcppri.disabled = !a || js_lldp_use_vlan_info || disableRtcppri;
    if (b.vlanid1) {
        b.vlanid1.disabled = (!a && !js_lldp_use_vlan_info) || disableVlanid1;
        b.port1pri.disabled = (!a && !js_lldp_use_vlan_info) || disablePortlpri
    }
}

function updateCertSettings(a) {
    var b = document.getElementById('networkSettingsForm');
    b.https_validate_expires.disabled = !a || disableHttpsExpires;
    b.https_validate_hostname.disabled = !a || disableHttpsHostname
}

function initializeNetworkSettings() {
    var a = document.getElementById('networkSettingsForm');
    updateBasicNetworkSettings(a.dhcp.checked);
    if (a.upnp) {
        updateNatIp(a.upnp.checked)
    } else {
        updateNatIp(0)
    }
    updateVlanSettings(a.vlanEnabled.checked);
    updateCertSettings(a.https_validate_certificates.checked)
}

function initializeADSettings() {
    var a = document.getElementById('sipLineSettingsForm');
    updateAutodialSetting(a.adGlobal.checked)
}

function updateNatIp(a) {
    var b = document.getElementById('networkSettingsForm');
    b.natIp.disabled = a || disableNatIp
}

function rangeCheck(a, b, c, d) {
    if ((c < a) || (c > b)) {
        alert(d + ":\n" + prmpt12 + " " + a + " - " + b);
        return false
    }
    return true
}

function DscpPriorityCheck() {
    var f = document.getElementById('networkSettingsForm');
    if ((f.sipdscp.value == f.rtpdscp.value && f.sippri.vlaue != f.rtppri.value) || f.sipdscp.value == f.rtcpdscp.value && f.sippri.value != f.rtcppri.value) {
        alert(prmpt13 + " " + f.sipdscp.value + " " + prmpt14);
        return false
    } else if (f.rtpdscp.value == f.rtcpdscp.value && f.rtppri.value != f.rtcppri.value) {
        alert(prmpt13 + " " + f.rtpdscp.value + " " + prmpt14);
        return false
    }
    return true
}

function validateNetworkSettings() {
    var a = /((((1|2)\d{2})|\d{1,2})\.){3}(((1|2)\d{2})|\d{1,2})/;
    var b = document.getElementById('networkSettingsForm');
    if (!b.dhcp.checked) {
        if (!a.test(b.ip.value)) {
            alert(prmpt15);
            return false
        }
        if (!a.test(b.subnet.value)) {
            alert(prmpt16);
            return false
        }
        if (!a.test(b.gateway.value)) {
            alert(prmpt17);
            return false
        }
        if (!disableDNSField && !a.test(b.dns1.value)) {
            alert(prmpt18);
            return false
        }
        if (!disableDNSField && !a.test(b.dns2.value)) {
            alert(prmpt19);
            return false
        }
    }
    if (!rangeCheck(0, 63, b.sipdscp.value, "SIP DSCP")) {
        return false
    }
    if (!rangeCheck(0, 63, b.rtpdscp.value, "RTP DSCP")) {
        return false
    }
    if (!rangeCheck(0, 63, b.rtcpdscp.value, "RTCP DSCP")) {
        return false
    }
    if (b.vlanEnabled.checked) {
        if (!rangeCheck(1, 4094, b.vlanid0.value, "VLANId port 0")) {
            return false
        }
        if (!DscpPriorityCheck()) {
            return false
        }
        if (!(js_is_9112)) {
            if (!rangeCheck(1, 4095, b.vlanid1.value, "VLANId port 1")) {
                return false
            }
        }
    }
    b.https_validate_expires.disabled = disableHttpsExpires;
    b.https_validate_hostname.disabled = disableHttpsHostname;
    return true
}

function updateMWITimeout(a) {
    var f = document.getElementById('globalSIPform');
    f.explicitMWISubscriptionPeriod.disabled = !a || disableMWISub
}