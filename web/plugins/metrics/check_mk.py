#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

# Metric definitions for Check_MK's checks

#   .--Units---------------------------------------------------------------.
#   |                        _   _       _ _                               |
#   |                       | | | |_ __ (_) |_ ___                         |
#   |                       | | | | '_ \| | __/ __|                        |
#   |                       | |_| | | | | | |_\__ \                        |
#   |                        \___/|_| |_|_|\__|___/                        |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  Definition of units of measurement.                                 |
#   '----------------------------------------------------------------------'

# TODO: Move fundamental units like "" to main file.

unit_info[""] = {
    "title"  : "",
    "symbol" : "",
    "render" : lambda v: "%.1f" % v,
}

unit_info["count"] = {
    "title"  : _("Count"),
    "symbol" : "",
    "render" : lambda v: "%d" % v,
}

unit_info["sessions"] = {
    "title"  : _("Sessions"),
    "symbol" : "",
    "render" : lambda v: "%d" % v,
}

unit_info["locks"] = {
    "title"  : _("Locks"),
    "symbol" : "",
    "render" : lambda v: "%d" % v,
}

# value ranges from 0.0 ... 100.0
unit_info["%"] = {
    "title"  : _("%"),
    "symbol" : _("%"),
    "render" : lambda v: "%s%%" % drop_dotzero(v),
}

# Similar as %, but value ranges from 0.0 ... 1.0
unit_info["ratio"] = {
    "title"  : _("%"),
    "symbol" : _("%"),
    "render_scale" : 100.0, # Scale by this before rendering if "render" not being used
    "render" : lambda v: "%s%%" % drop_dotzero(100.0 * v),
}

unit_info["s"] = {
    "title" : _("sec"),
    "symbol" : _("s"),
    "render" : age_human_readable,
}

unit_info["1/s"] = {
    "title" : _("per second"),
    "symbol" : _("/s"),
    "render" : lambda v: "%s%s" % (drop_dotzero(v), _("/s")),
}

unit_info["bytes"] = {
    "title"  : _("Bytes"),
    "symbol" : _("B"),
    "render" : bytes_human_readable,
}

unit_info["bytes/s"] = {
    "title"  : _("Bytes per second"),
    "symbol" : _("B/s"),
    "render" : lambda v: bytes_human_readable(v) + _("/s"),
}

# Output in bytes/days, value is in bytes/s
unit_info["bytes/d"] = {
    "title"  : _("Bytes per day"),
    "symbol" : _("B/d"),
    "render" : lambda v: bytes_human_readable(v * 86400.0) + _("/d"),
}

unit_info["c"] = {
    "title"  : _("Degree Celsius"),
    "symbol" : u"°C",
    "render" : lambda v: "%s %s" % (drop_dotzero(v), u"°C"),
}

unit_info["a"] = {
    "title"  : _("Electrical Current (Amperage)"),
    "symbol" : _("A"),
    "render" : lambda v: physical_precision(v, 3, _("A")),
}

unit_info["v"] = {
    "title"  : _("Electrical Tension (Voltage)"),
    "symbol" : _("V"),
    "render" : lambda v: physical_precision(v, 3, _("V")),
}

unit_info["w"] = {
    "title"  : _("Electrical Power"),
    "symbol" : _("W"),
    "render" : lambda v: physical_precision(v, 3, _("W")),
}

unit_info["va"] = {
    "title"  : _("Electrical Apparent Power"),
    "symbol" : _("VA"),
    "render" : lambda v: physical_precision(v, 3, _("VA")),
}

unit_info["wh"] = {
    "title"  : _("Electrical Energy"),
    "symbol" : _("Wh"),
    "render" : lambda v: physical_precision(v, 3, _("Wh")),
}

unit_info["dbm"] = {
    "title" : _("Decibel-milliwatts"),
    "symbol" : _("dBm"),
    "render" : lambda v: "%s %s" % (drop_dotzero(v), _("dBm")),
}

unit_info["db"] = {
    "title" : _("Decibel"),
    "symbol" : _("dB"),
    "render" : lambda v: physical_precision(v, 3, _("dB")),
}



#.
#   .--Metrics-------------------------------------------------------------.
#   |                   __  __      _        _                             |
#   |                  |  \/  | ___| |_ _ __(_) ___ ___                    |
#   |                  | |\/| |/ _ \ __| '__| |/ __/ __|                   |
#   |                  | |  | |  __/ |_| |  | | (__\__ \                   |
#   |                  |_|  |_|\___|\__|_|  |_|\___|___/                   |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  Definitions of metrics                                              |
#   '----------------------------------------------------------------------'

# Title are always lower case - except the first character!

metric_info["rta"] = {
    "title" : _("Round trip average"),
    "unit"  : "s",
    "color" : "#40a0b0",
}

metric_info["pl"] = {
    "title" : _("Packet loss"),
    "unit"  : "%",
    "color" : "#ffc030",
}

metric_info["uptime"] = {
    "title" : _("Uptime"),
    "unit"  : "s",
    "color" : "#80f000",
}

metric_info["hit_ratio"] = {
    "title" : _("Cache hit ratio"),
    "unit"  : "ratio",
    "color" : "#60c0c0",
}

metric_info["database_size"] = {
    "title" : _("Database size"),
    "unit"  : "bytes",
    "color" : "#00868B",
}

metric_info["mem_used"] = {
    "title" : _("Used RAM"),
    "unit"  : "bytes",
    "color" : "#80ff40",
}

metric_info["mem_free"] = {
    "title" : _("Free RAM"),
    "unit"  : "bytes",
    "color" : "#ffffff",
}

metric_info["swap_used"] = {
    "title" : _("Used swap space"),
    "unit"  : "bytes",
    "color" : "#008030",
}

metric_info["caches"] = {
    "title" : _("Memory used by caches"),
    "unit"  : "bytes",
    "color" : "#ffffff",
}

metric_info["swap_free"] = {
    "title" : _("Free swap space"),
    "unit"  : "bytes",
    "color" : "#eeeeee",
}

metric_info["execution_time"] = {
    "title" : _("Execution time"),
    "unit"  : "s",
    "color" : "#22dd33",
}

metric_info["load1"] = {
    "title" : _("CPU load average of last minute"),
    "unit"  : "",
    "color" : "#60c0e0",
}

metric_info["load5"] = {
    "title" : _("CPU load average of last 5 minutes"),
    "unit"  : "",
    "color" : "#428399",
}

metric_info["load15"] = {
    "title" : _("CPU load average of last 15 minutes"),
    "unit"  : "",
    "color" : "#2c5766",
}

metric_info["fs_used"] = {
    "title" : _("Used filesystem space"),
    "unit"  : "bytes",
    "color" : "#00ffc6",
}

metric_info["inodes_used"] = {
    "title" : _("Used inodes"),
    "unit"  : "count",
    "color" : "#a0608f",
}

metric_info["fs_size"] = {
    "title" : _("Filesystem size"),
    "unit"  : "bytes",
    "color" : "#006040",
}

metric_info["fs_growth"] = {
    "title" : _("Filesystem growth"),
    "unit"  : "bytes/d",
    "color" : "#29cfaa",
}

metric_info["fs_trend"] = {
    "title" : _("Trend of filesystem growth"),
    "unit"  : "bytes/d",
    "color" : "#808080",
}


metric_info["fs_provisioning"] = {
    "title" : _("Provisioned filesystem space"),
    "unit"  : "bytes",
    "color" : "#ff8000",
}


metric_info["temp"] = {
    "title" : _("Temperature"),
    "unit"  : "c",
    "color" : "#f0a040"
}

metric_info["ctxt"] = {
    "title" : _("Context switches"),
    "unit"  : "1/s",
    "color" : "#ddaa66",
}

metric_info["pgmajfault"] = {
    "title" : _("Major page faults"),
    "unit"  : "1/s",
    "color" : "#ddaa22",
}

metric_info["proc_creat"] = {
    "title" : _("Process creations"),
    "unit"  : "1/s",
    "color" : "#ddaa99",
}

metric_info["threads"] = {
    "title" : _("Number of threads"),
    "unit"  : "count",
    "color" : "#aa44ff",
}

metric_info["user"] = {
    "title" : _("User"),
    "help"  : _("Percentage of CPU time spent in user space"),
    "unit"  : "%",
    "color" : "#60f020",
}

metric_info["system"] = {
    "title" : _("System"),
    "help"  : _("Percentage of CPU time spent in kernel space"),
    "unit"  : "%",
    "color" : "#ff6000",
}

metric_info["util"] = {
    "title" : _("CPU utilization"),
    "help"  : _("Percentage of CPU time used"),
    "unit"  : "%",
    "color" : "#60f020",
}

metric_info["io_wait"] = {
    "title" : _("IO-wait"),
    "help"  : _("Percentage of CPU time spent waiting for IO"),
    "unit"  : "%",
    "color" : "#00b0c0",
}

metric_info["time_offset"] = {
    "title" : _("Time offset"),
    "unit"  : "s",
    "color" : "#9a52bf",
}

metric_info["connection_time"] = {
    "title" : _("Connection time"),
    "unit"  : "s",
    "color" : "#94b65a",
}

metric_info["input_signal_power_dbm"] = {
    "title" : _("Input power"),
    "unit"  : "dbm",
    "color" : "#20c080",
}

metric_info["output_signal_power_dbm"] = {
    "title" : _("Output power"),
    "unit"  : "dbm",
    "color" : "#2080c0",
}

metric_info["tablespace_wasted"] = {
    "title" : _("Tablespace wasted"),
    "unit"  : "bytes",
    "color" : "#a02020",
}

metric_info["indexspace_wasted"] = {
    "title" : _("Indexspace wasted"),
    "unit"  : "bytes",
    "color" : "#20a080",
}

metric_info["current"] = {
    "title" : _("Electrical current"),
    "unit"  : "a",
    "color" : "#ffb030",
}

metric_info["voltage"] = {
    "title" : _("Electrical voltage"),
    "unit"  : "v",
    "color" : "#ffc060",
}

metric_info["power"] = {
    "title" : _("Electrical power"),
    "unit"  : "w",
    "color" : "#8848c0",
}

metric_info["appower"] = {
    "title" : _("Electrical apparent power"),
    "unit"  : "va",
    "color" : "#aa68d80",
}

metric_info["energy"] = {
    "title" : _("Electrical energy"),
    "unit"  : "wh",
    "color" : "#aa80b0",
}

metric_info["output_load"] = {
    "title" : _("Output load"),
    "unit"  : "%",
    "color" : "#c83880",
}

metric_info["voltage_percent"] = {
    "title" : _("Electrical tension in % of normal value"),
    "unit"  : "%",
    "color" : "#ffc020",
}

metric_info["humidity"] = {
    "title" : _("Relative humidity"),
    "unit"  : "%",
    "color" : "#90b0b0",
}

metric_info["requests_per_second"] = {
    "title" : _("Requests per second"),
    "unit"  : "1/s",
    "color" : "#4080a0",
}

metric_info["busy_workers"] = {
    "title" : _("Busy workers"),
    "unit"  : "count",
    "color" : "#a080b0",
}

metric_info["connections"] = {
    "title" : _("Connections"),
    "unit"  : "count",
    "color" : "#a080b0",
}

metric_info["signal_noise"] = {
    "title" : _("Signal/Noise ratio"),
    "unit"  : "db",
    "color" : "#aadd66",
}

metric_info["codewords_corrected"] = {
    "title" : _("Corrected codewords"),
    "unit"  : "ratio",
    "color" : "#ff8040",
}

metric_info["codewords_uncorrectable"] = {
    "title" : _("Uncorrectable codewords"),
    "unit"  : "ratio",
    "color" : "#ff4020",
}

metric_info["total_sessions"] = {
    "title" : _("Total"),
    "unit"  : "sessions",
    "color" : "#94b65a",
}

metric_info["running_sessions"] = {
    "title" : _("Running"),
    "unit"  : "sessions",
    "color" : "#999b94",
}

metric_info["shared_locks"] = {
    "title" : _("Shared"),
    "unit"  : "locks",
    "color" : "#92ec89",
}

metric_info["exclusive_locks"] = {
    "title" : _("Exclusive"),
    "unit"  : "locks",
    "color" : "#ca5706",
}

metric_info["disk_read_throughput"] = {
    "title" : _("Read throughput"),
    "unit"  : "bytes/s",
    "color" : "#40c080",
}

metric_info["disk_write_throughput"] = {
    "title" : _("Write throughput"),
    "unit"  : "bytes/s",
    "color" : "#4080c0",
}

metric_info["disk_read_ios"] = {
    "title" : _("Read operations"),
    "unit"  : "1/s",
    "color" : "#60e0a0",
}

metric_info["disk_write_ios"] = {
    "title" : _("Write operations"),
    "unit"  : "1/s",
    "color" : "#60a0e0",
}

metric_info["disk_average_read_wait"] = {
    "title" : _("Read wait Time"),
    "unit"  : "s",
    "color" : "#20e8c0",
}

metric_info["disk_average_write_wait"] = {
    "title" : _("Write wait time"),
    "unit"  : "s",
    "color" : "#20c0e8",
}

metric_info["disk_average_wait"] = {
    "title" : _("Request wait time"),
    "unit"  : "s",
    "color" : "#4488cc",
}

metric_info["disk_average_read_request_size"] = {
    "title" : _("Average read request size"),
    "unit"  : "bytes",
    "color" : "#409c58",
}

metric_info["disk_average_write_request_size"] = {
    "title" : _("Average write request size"),
    "unit"  : "bytes",
    "color" : "#40589c",
}

metric_info["disk_average_request_size"] = {
    "title" : _("Average request size"),
    "unit"  : "bytes",
    "color" : "#4488cc",
}

metric_info["disk_latency"] = {
    "title" : _("Average disk latency"),
    "unit"  : "s",
    "color" : "#c04080",
}

metric_info["disk_queue_length"] = {
    "title" : _("Disk IO-queue length"),
    "unit"  : "",
    "color" : "#7060b0",
}

metric_info["disk_utilization"] = {
    "title" : _("Disk utilization"),
    "unit"  : "ratio",
    "color" : "#a05830",
}

metric_info["xda_hitratio"] = {
    "title" : _("XDA hitratio"),
    "unit"  : "%",
    "color" : "#0ae86d",
}

metric_info["data_hitratio"] = {
    "title" : _("Data hitratio"),
    "unit"  : "%",
    "color" : "#2828de",
}

metric_info["index_hitratio"] = {
    "title" : _("Index hitratio"),
    "unit"  : "%",
    "color" : "#dc359f",
}

metric_info["total_hitratio"] = {
    "title" : _("Total hitratio"),
    "unit"  : "%",
    "color" : "#2e282c",
}

metric_info["deadlocks"] = {
    "title" : _("Deadlocks"),
    "unit"  : "1/s",
    "color" : "#dc359f",
}

metric_info["lockwaits"] = {
    "title" : _("Waitlocks"),
    "unit"  : "1/s",
    "color" : "#2e282c",
}

metric_info["sort_overflow"] = {
    "title" : _("Sort overflow"),
    "unit"  : "%",
    "color" : "#e72121",
}

metric_info["tablespace_size"] = {
    "title" : _("Tablespace size"),
    "unit"  : "bytes",
    "color" : "#092507",
}

metric_info["tablespace_used"] = {
    "title" : _("Tablespace used"),
    "unit"  : "bytes",
    "color" : "#e59d12",
}

metric_info["tablespace_max_size"] = {
    "title" : _("Tablespace max size"),
    "unit"  : "bytes",
    "color" : "#172121",
}

metric_info["hours_operation"] = {
    "title" : _("Hours of operation"),
    "unit"  : "s",
    "color" : "#94b65a",
}

metric_info["hours_since_service"] = {
    "title" : _("Hours since service"),
    "unit"  : "s",
    "color" : "#94b65a",
}

metric_info["execution_time"] = {
    "title" : _("Total execution time"),
    "unit"  : "s",
    "color" : "#d080af",
}

metric_info["user_time"] = {
    "title" : _("CPU time spent in user space"),
    "unit"  : "s",
    "color" : "#60f020",
}

metric_info["system_time"] = {
    "title" : _("CPU time spent in system space"),
    "unit"  : "s",
    "color" : "#ff6000",
}

metric_info["children_user_time"] = {
    "title" : _("CPU time of childs in user space"),
    "unit"  : "s",
    "color" : "#aef090",
}

metric_info["children_system_time"] = {
    "title" : _("CPU time of childs in system space"),
    "unit"  : "s",
    "color" : "#ffb080",
}


#.
#   .--Checks--------------------------------------------------------------.
#   |                    ____ _               _                            |
#   |                   / ___| |__   ___  ___| | _____                     |
#   |                  | |   | '_ \ / _ \/ __| |/ / __|                    |
#   |                  | |___| | | |  __/ (__|   <\__ \                    |
#   |                   \____|_| |_|\___|\___|_|\_\___/                    |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  How various checks' performance data translate into the known       |
#   |  metrics                                                             |
#   '----------------------------------------------------------------------'

check_metrics["check-mk"]                                       = {}
check_metrics["check-mk-ping"]                                  = {}
check_metrics["check-mk"]                                       = {}

check_metrics["check_mk-uptime"]                                = {}
check_metrics["check_mk-esx_vsphere_counters.uptime"]           = {}
check_metrics["check_mk-fritz.uptime"]                          = {}
check_metrics["check_mk-jolokia_metrics.uptime"]                = {}
check_metrics["check_mk-snmp_uptime"]                           = {}

check_metrics["check_mk-cpu.loads"]                             = {}
check_metrics["check_mk-ucd_cpu_load"]                          = {}
check_metrics["check_mk-statgrab_load"]                         = {}
check_metrics["check_mk-hpux_cpu"]                              = {}
check_metrics["check_mk-blade_bx_load"]                         = {}

check_metrics["check_mk-cpu.threads"]                           = {}

check_metrics["check_mk-mem.linux"]                             = {}
check_metrics["check_mk-aix_memory"]                            = { "ramused" : { "name" : "mem_used", "scale": MB }, "swapused" : { "name" : "swap_used", "scale": MB }}
check_metrics["check_mk-mem.win"]                               = { "memory" : { "name" : "mem_used", "scale" : MB }, "pagefile" : { "name" : "pagefile_used", "scale" : MB }}

df_translation = {
    0         : { "name"  : "fs_used", "scale" : MB },
    "fs_size" : { "scale" : MB },
    "growth"  : { "name"  : "fs_growth", "scale" : MB / 86400.0 },
    "trend"   : { "name"  : "fs_trend", "scale" : MB / 86400.0 },
}
check_metrics["check_mk-df"]                                    = df_translation
check_metrics["check_mk-vms_df"]                                = df_translation
check_metrics["check_mk-vms_diskstat.df"]                       = df_translation
check_metrics["check_disk"]                                     = df_translation
check_metrics["check_mk-df_netapp"]                             = df_translation
check_metrics["check_mk-df_netapp32"]                           = df_translation
check_metrics["check_mk-zfsget"]                                = df_translation
check_metrics["check_mk-hr_fs"]                                 = df_translation
check_metrics["check_mk-oracle_asm_diskgroup"]                  = df_translation
check_metrics["check_mk-esx_vsphere_counters.ramdisk"]          = df_translation
check_metrics["check_mk-hitachi_hnas_span"]                     = df_translation
check_metrics["check_mk-hitachi_hnas_volume"]                   = df_translation
check_metrics["check_mk-emcvnx_raidgroups.capacity"]            = df_translation
check_metrics["check_mk-emcvnx_raidgroups.capacity_contiguous"] = df_translation
check_metrics["check_mk-ibm_svc_mdiskgrp"]                      = df_translation
check_metrics["check_mk-fast_lta_silent_cubes.capacity"]        = df_translation
check_metrics["check_mk-fast_lta_volumes"]                      = df_translation
check_metrics["check_mk-libelle_business_shadow.archive_dir"]   = df_translation

check_metrics["check_mk-diskstat"]                              = {}

check_metrics["check_mk-apc_symmetra_ext_temp"]                 = {}
check_metrics["check_mk-adva_fsp_temp"]                         = {}
check_metrics["check_mk-akcp_daisy_temp"]                       = {}
check_metrics["check_mk-akcp_exp_temp"]                         = {}
check_metrics["check_mk-akcp_sensor_temp"]                      = {}
check_metrics["check_mk-allnet_ip_sensoric.temp"]               = {}
check_metrics["check_mk-apc_inrow_temperature"]                 = {}
check_metrics["check_mk-apc_symmetra_temp"]                     = {}
check_metrics["check_mk-arris_cmts_temp"]                       = {}
check_metrics["check_mk-bintec_sensors.temp"]                   = {}
check_metrics["check_mk-brocade.temp"]                          = {}
check_metrics["check_mk-brocade_mlx_temp"]                      = {}
check_metrics["check_mk-carel_sensors"]                         = {}
check_metrics["check_mk-casa_cpu_temp"]                         = {}
check_metrics["check_mk-cisco_temp_perf"]                       = {}
check_metrics["check_mk-cisco_temp_sensor"]                     = {}
check_metrics["check_mk-climaveneta_temp"]                      = {}
check_metrics["check_mk-cmciii.temp"]                           = {}
check_metrics["check_mk-cmctc.temp"]                            = {}
check_metrics["check_mk-cmctc_lcp.temp"]                        = {}
check_metrics["check_mk-dell_chassis_temp"]                     = {}
check_metrics["check_mk-dell_om_sensors"]                       = {}
check_metrics["check_mk-dell_poweredge_temp"]                   = {}
check_metrics["check_mk-decru_temps"]                           = {}
check_metrics["check_mk-emc_datadomain_temps"]                  = {}
check_metrics["check_mk-enterasys_temp"]                        = {}
check_metrics["check_mk-f5_bigip_chassis_temp"]                 = {}
check_metrics["check_mk-f5_bigip_cpu_temp"]                     = {}
check_metrics["check_mk-fsc_temp"]                              = {}
check_metrics["check_mk-hitachi_hnas_temp"]                     = {}
check_metrics["check_mk-hp_proliant_temp"]                      = {}
check_metrics["check_mk-hwg_temp"]                              = {}
check_metrics["check_mk-ibm_svc_enclosurestats.temp"]           = {}
check_metrics["check_mk-innovaphone_temp"]                      = {}
check_metrics["check_mk-juniper_screenos_temp"]                 = {}
check_metrics["check_mk-kentix_temp"]                           = {}
check_metrics["check_mk-knuerr_rms_temp"]                       = {}
check_metrics["check_mk-lnx_thermal"]                           = {}
check_metrics["check_mk-netapp_api_temp"]                       = {}
check_metrics["check_mk-netscaler_health.temp"]                 = {}
check_metrics["check_mk-nvidia.temp"]                           = {}
check_metrics["check_mk-ups_bat_temp"]                          = {}
check_metrics["check_mk-qlogic_sanbox.temp"]                    = {}
check_metrics["check_mk-rms200_temp"]                           = {}
check_metrics["check_mk-sensatronics_temp"]                     = {}
check_metrics["check_mk-smart.temp"]                            = {}
check_metrics["check_mk-viprinet_temp"]                         = {}
check_metrics["check_mk-wagner_titanus_topsense.temp"]          = {}
check_metrics["check_mk-cmciii.phase"]                          = {}
check_metrics["check_mk-ucs_bladecenter_fans.temp"]             = {}
check_metrics["check_mk-ucs_bladecenter_psu.chassis_temp"]      = {}
check_metrics["check_mk-mysql_capacity"]                        = {}

check_metrics["check_mk-kernel"]                                = { "processes" : { "name" : "proc_creat", } }

check_metrics["check_mk-hr_cpu"]                                = {}
check_metrics["check_mk-kernel.util"]                           = { "wait" : { "name" : "io_wait" } }
check_metrics["check_mk-lparstat_aix.cpu_util"]                 = { "wait" : { "name" : "io_wait" } }
check_metrics["check_mk-ucd_cpu_util"]                          = { "wait" : { "name" : "io_wait" } }
check_metrics["check_mk-vms_cpu"]                               = { "wait" : { "name" : "io_wait" } }
check_metrics["check_mk-vms_sys.util"]                          = { "wait" : { "name" : "io_wait" } }

check_metrics["check_mk-mbg_lantime_state"]                     = { "offset" : { "name" : "time_offset", "scale" : 0.000001 }} # convert us -> sec
check_metrics["check_mk-mbg_lantime_ng_state"]                  = { "offset" : { "name" : "time_offset", "scale" : 0.000001 }} # convert us -> sec
check_metrics["check_mk-systemtime"]                            = { "offset" : { "name" : "time_offset" }}

check_metrics["check_mk-adva_fsp_if"]                           = { "output_power" : { "name" : "output_signal_power_dbm" },
                                                                    "input_power" : { "name" : "input_signal_power_dbm" }}

check_metrics["check_mk-allnet_ip_sensoric.tension"]            = { "tension" : { "name" : "voltage_percent" }}
check_metrics["check_mk-adva_fsp_current"]                      = {}

check_metrics["check_mk-akcp_exp_humidity"]                     = {}
check_metrics["check_mk-apc_humidity"]                          = {}
check_metrics["check_mk-hwg_humidity"]                          = {}


check_metrics["check_mk-apache_status"]                         = { "ReqPerSec" : { "name" : "requests_per_second" }, "BusyWorkers" : { "name" : "busy_workers" }}

check_metrics["check_mk-bintec_sensors.voltage"]                = {}
check_metrics["check_mk-hp_blade_psu"]                          = { "output" : { "name" : "power" }}
check_metrics["check_mk-apc_rackpdu_power"]                     = { "amperage" : { "name" : "current" }}
check_metrics["check_mk-apc_ats_output"]                        = { "volt" : { "name" : "voltage" }, "watt" : { "name" : "power"}, "ampere": { "name": "current"}, "load_perc" : { "name": "output_load" }}
check_metrics["check_mk-raritan_pdu_inlet"]                     = {}
check_metrics["check_mk-raritan_pdu_inlet_summary"]             = {}
check_metrics["check_mk-ups_socomec_outphase"]                  = {}
check_metrics["check_mk-ucs_bladecenter_psu.switch_power"]      = {}

check_metrics["check_mk-bluecoat_sensors"]                      = {}

check_metrics["check_mk-zfs_arc_cache"]                         = { "hit_ratio" : { "scale" : 0.01 }}
check_metrics["check_mk-docsis_channels_upstream"]              = {}

check_metrics["check_mk-postgres_bloat"]                        = {}
check_metrics["check_mk-postgres_connections"]                  = {}
check_metrics["check_mk-postgres_locks"]                        = {}
check_metrics["check_mk-postgres_conn_time"]                    = {}
check_metrics["check_mk-postgres_sessions"]                     = { "total": {"name": "total_sessions"}, "running": {"name": "running_sessions"} }

check_metrics["check_mk-db2_bp_hitratios"]                      = {}
check_metrics["check_mk-db2_connections"]                       = {}
check_metrics["check_mk-db2_counters"]                          = {}
check_metrics["check_mk-db2_logsize"]                           = { 0: { "name": "fs_used", "scale" : MB } }
check_metrics["check_mk-db2_sort_overflow"]                     = {}
check_metrics["check_mk-db2_tablespaces"]                       = {}
check_metrics["check_mk-siemens_plc.temp"]                      = {}
check_metrics["check_mk-siemens_plc.hours"]                     = {}

#.
#   .--Perf-O-Meters-------------------------------------------------------.
#   |  ____            __        ___        __  __      _                  |
#   | |  _ \ ___ _ __ / _|      / _ \      |  \/  | ___| |_ ___ _ __ ___   |
#   | | |_) / _ \ '__| |_ _____| | | |_____| |\/| |/ _ \ __/ _ \ '__/ __|  |
#   | |  __/  __/ |  |  _|_____| |_| |_____| |  | |  __/ ||  __/ |  \__ \  |
#   | |_|   \___|_|  |_|        \___/      |_|  |_|\___|\__\___|_|  |___/  |
#   |                                                                      |
#   +----------------------------------------------------------------------+
#   |  Definition of Perf-O-Meters                                         |
#   '----------------------------------------------------------------------'

# Types of Perf-O-Meters:
# linear      -> multiple values added from left to right
# logarithmic -> one value in a logarithmic scale
# dual        -> two Perf-O-Meters next to each other, the first one from right to left
# stacked     -> two Perf-O-Meters of type linear, logarithmic or dual, stack vertically
# The label of dual and stacked is taken from the definition of the contained Perf-O-Meters

perfometer_info.append({
    "type"     : "linear",
    "segments" : [ "execution_time" ],
    "total"    : 90.0,
})

perfometer_info.append({
    "type"       : "logarithmic",
    "metric"     : "uptime",
    "half_value" : 2592000.0,
    "exponent"   : 2,
})

perfometer_info.append(("logarithmic",  ( "rta", 0.1, 4)))
perfometer_info.append(("linear",       ( ["execution_time"], 90.0, None)))
perfometer_info.append(("logarithmic",  ( "load1",         4.0, 2.0)))
perfometer_info.append(("logarithmic",  ( "temp",         40.0, 1.2)))
perfometer_info.append(("logarithmic",  ( "ctxt",       1000.0, 2.0)))
perfometer_info.append(("logarithmic",  ( "pgmajfault", 1000.0, 2.0)))
perfometer_info.append(("logarithmic",  ( "proc_creat", 1000.0, 2.0)))
perfometer_info.append(("logarithmic",  ( "threads",     400.0, 2.0)))
perfometer_info.append(("linear",       ( [ "user", "system", "io_wait" ],                               100.0,       None)))
perfometer_info.append(("linear",       ( [ "util", ],                                                   100.0,       None)))
perfometer_info.append(("logarithmic",  ( "database_size", GB, 5.0 )))

# Filesystem check with over-provisioning
perfometer_info.append({
    "type"      : "linear",
    "condition" : "fs_provisioning(%),100,>",
    "segments"  : [
        "fs_used(%)",
        "100,fs_used(%),-#e3fff9",
        "fs_provisioning(%),100.0,-#ffc030",
    ],
    "total"     : "fs_provisioning(%)",
    "label"     : ( "fs_used(%)", "%" ),
})

# Filesystem check with provisioning, but not over-provisioning
perfometer_info.append({
    "type"      : "linear",
    "condition" : "fs_provisioning(%),100,<=",
    "segments"  : [
        "fs_used(%)",
        "fs_provisioning(%),fs_used(%),-#ffc030",
        "100,fs_provisioning(%),fs_used(%),-,-#e3fff9",
    ],
    "total"     : 100,
    "label"     : ( "fs_used(%)", "%" ),
})

# Filesystem without over-provisioning
perfometer_info.append({
    "type"      : "linear",
    "segments"  : [
        "fs_used(%)",
        "100.0,fs_used(%),-#e3fff9",
    ],
    "total"     : 100,
    "label"     : ( "fs_used(%)", "%" ),
})


perfometer_info.append(("linear",      ( [ "mem_used", "swap_used", "caches", "mem_free", "swap_free" ], None,
("mem_total,mem_used,+,swap_used,/", "ratio"))))
perfometer_info.append(("linear",      ( [ "mem_used" ],                                                "mem_total", None)))
perfometer_info.append(("linear",      ( [ "mem_used(%)" ],                                              100.0, None)))
perfometer_info.append(("logarithmic",  ( "time_offset",  1.0, 10.0)))

perfometer_info.append(("stacked", [
   ( "logarithmic", ( "tablespace_wasted", 1000000, 2)),
   ( "logarithmic", ( "indexspace_wasted", 1000000, 2)),
]))

perfometer_info.append(("linear",      ( [ "running_sessions" ],                                        "total_sessions", None)))
perfometer_info.append(("linear",      ( [ "shared_locks", "exclusive_locks" ],                         None, None)))

perfometer_info.append(("linear",      ( [ "connections" ], 100, None)))
perfometer_info.append(("logarithmic", ( "connection_time", 0.2, 2)))

perfometer_info.append(("dual", [
   ( "logarithmic", ( "input_signal_power_dbm", 4, 2)),
   ( "logarithmic", ( "output_signal_power_dbm", 4, 2)),
]))


perfometer_info.append(("dual", [
   ( "logarithmic", ( "deadlocks", 50, 2)),
   ( "logarithmic", ( "lockwaits", 50, 2)),
]))


perfometer_info.append({
    "type"      : "linear",
    "segments"  : [
        "sort_overflow",
    ],
})

perfometer_info.append({
    "type"      : "linear",
    "segments"  : [
        "tablespace_used",
    ],
    "total"     : "tablespace_size",
})

perfometer_info.append(("stacked", [
("dual", [ {"type": "linear", "label": None, "segments": [ "total_hitratio" ], "total": 100},
           {"type": "linear", "label": None, "segments": [ "data_hitratio" ],  "total": 100}]),
("dual", [ {"type": "linear", "label": None, "segments": [ "index_hitratio" ], "total": 100},
           {"type": "linear", "label": None, "segments": [ "xda_hitratio" ],   "total": 100}])
]))

perfometer_info.append(("linear",      ( [ "output_load" ], 100.0, None)))
perfometer_info.append(("logarithmic", ( "power", 1000, 2)))
perfometer_info.append(("logarithmic", ( "current", 10, 4)))
perfometer_info.append(("logarithmic", ( "voltage", 220.0, 2)))
perfometer_info.append(("linear",      ( [ "voltage_percent" ], 100.0, None)))
perfometer_info.append(("linear",      ( [ "humidity" ], 100.0, None)))

perfometer_info.append(("stacked",    [
  ( "logarithmic", ( "requests_per_second", 10, 5)),
  ( "logarithmic", ( "busy_workers",        10, 2))]))

perfometer_info.append(("linear",      ( [ "hit_ratio" ], 1.0, None)))
perfometer_info.append(("stacked",  [
   ("logarithmic",  ( "signal_noise", 50.0, 2.0)),
   ("linear",       ( [ "codewords_corrected", "codewords_uncorrectable" ], 1.0, None)),
]))
perfometer_info.append(("logarithmic",  ( "signal_noise", 50.0, 2.0))) # Fallback if no codewords are available

perfometer_info.append(("dual", [
   ( "logarithmic", ( "disk_read_throughput", 5000000, 10)),
   ( "logarithmic", ( "disk_write_throughput", 5000000, 10)),
]))

#.
#   .--Graphs--------------------------------------------------------------.
#   |                    ____                 _                            |
#   |                   / ___|_ __ __ _ _ __ | |__  ___                    |
#   |                  | |  _| '__/ _` | '_ \| '_ \/ __|                   |
#   |                  | |_| | | | (_| | |_) | | | \__ \                   |
#   |                   \____|_|  \__,_| .__/|_| |_|___/                   |
#   |                                  |_|                                 |
#   +----------------------------------------------------------------------+
#   |  Definitions of time series graphs                                   |
#   '----------------------------------------------------------------------'

graph_info.append({
    "metrics" : [
        ( "execution_time", "area" )
    ]
})

graph_info.append({
    "title" : _("Used CPU Time"),
    "metrics" : [
        ( "user_time",            "area" ),
        ( "children_user_time",   "stack" ),
        ( "system_time",          "stack" ),
        ( "children_system_time", "stack" ),
    ],
})

graph_info.append({
    "metrics" : [
        ( "uptime", "area" ),
    ]
})

graph_info.append({
    "title"   : _("CPU Load - %(load1:max@count) CPU Cores"),
    "metrics" : [
        ( "load1", "area" ),
        ( "load15", "line" ),
    ],
    "scalars" : [
        "load1:warn",
        "load1:crit",
    ]
})


graph_info.append({
    "metrics" : [
        ( "fs_used", "area" ),
        ( "fs_size,fs_used,-#e3fff9", "stack", _("Free space") ),
        ( "fs_size", "line" ),
    ],
    "scalars" : [
        "fs_used:warn",
        "fs_used:crit",
    ],
    "range" : (0, "fs_used:max"),
})


graph_info.append({
    "title" : _("Growing / Shrinking"),
    "metrics" : [
       ( "fs_growth.max,0,MAX",             "area",  _("Growth"), ),
       ( "fs_growth.min,0,MIN,-1,*#299dcf", "-area", _("Shrinkage") ),
    ],
})

graph_info.append({
    "metrics" : [
       ( "fs_trend", "line" ),
    ],
    "range" : (0, 0),
})

graph_info.append({
    "metrics" : [
       ( "inodes_used", "area" ),
    ],
    "scalars" : [
        "inodes_used:warn",
        "inodes_used:crit",
    ],
})


graph_info.append({
    "metrics" : [
        ( "temp", "area" ),
    ]
})

graph_info.append({
    "title"   : _("CPU utilization"),
    "metrics" : [
        ( "user",                           "area"  ),
        ( "system",                         "stack" ),
        ( "io_wait",                        "stack" ),
        ( "user,system,io_wait,+,+#004080", "line", _("Total") ),
    ],
    "mirror_legend" : True,
    # "range" : (0, 100),
})

graph_info.append({
    "metrics" : [
        ( "time_offset", "area" ),
    ]
})

graph_info.append({
    "title"   : _("Wasted space of tables and indexes"),
    "metrics" : [
        ( "tablespace_wasted", "area" ),
        ( "indexspace_wasted", "stack" ),
    ],
    "legend_scale" : MB,
    "legend_precision" : 2,
})

graph_info.append({
    "title": _("Time to connect"),
    "metrics" : [
        ( "connection_time", "area" ),
    ],
    "legend_scale" : m,
})

graph_info.append({
    "title": _("Number of connections"),
    "metrics" : [
        ( "connections", "line" ),
    ],
})

graph_info.append({
    "title": _("Number of total and running sessions"),
    "metrics" : [
        ( "running_sessions", "line" ),
        ( "total_sessions",   "line" ),
    ],
    "legend_precision" : 0
})

graph_info.append({
    "title": _("Number of shared and exclusive locks"),
    "metrics" : [
        ( "shared_locks",    "area" ),
        ( "exclusive_locks", "stack" ),
    ],
    "legend_precision" : 0
})

# diskstat checks

graph_info.append({
    "metrics" : [
        ( "disk_utilization",  "area" ),
    ],
    "range" : (0, 1),
})

graph_info.append({
    "title" : _("Disk Throughput"),
    "metrics" : [
        ( "disk_read_throughput",  "area" ),
        ( "disk_write_throughput", "-area" ),
    ],
    "legend_scale" : MB,
})

graph_info.append({
    "title" : _("Disk I/O Operations"),
    "metrics" : [
        ( "disk_read_ios",  "area" ),
        ( "disk_write_ios", "-area" ),
    ],
})

graph_info.append({
    "title" : _("Average request size"),
    "metrics" : [
        ( "disk_average_read_request_size",  "area" ),
        ( "disk_average_write_request_size", "-area" ),
    ],
    "legend_scale" : KB,
})


graph_info.append({
    "title" : _("Average end to end wait time"),
    "metrics" : [
        ( "disk_average_read_wait",  "area" ),
        ( "disk_average_write_wait", "-area" ),
    ],
})

graph_info.append({
    "metrics" : [
        ( "disk_latency",  "area" ),
    ],
})

graph_info.append({
    "metrics" : [
        ( "disk_queue_length",  "area" ),
    ],
})

graph_info.append({
    "metrics" : [
        ( "database_size",  "area" ),
    ],
    "legend_scale" : MB,
})

graph_info.append({
    "title" : _("Bufferpool Hitratios"),
    "metrics" : [
        ( "total_hitratio", "line" ),
        ( "data_hitratio",  "line" ),
        ( "index_hitratio", "line" ),
        ( "xda_hitratio",   "line" ),
    ],
})

graph_info.append({
    "metrics" : [
        ( "deadlocks",  "line" ),
        ( "lockwaits",  "line" ),
    ],
})

graph_info.append({
    "metrics" : [
        ( "sort_overflow",  "line" ),
    ],
})

graph_info.append({
    "metrics" : [
        ( "tablespace_size",  "line" ),
        ( "tablespace_used",  "line" ),
    ],
})

