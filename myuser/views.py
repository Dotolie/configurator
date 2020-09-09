from django.shortcuts import render, redirect
from .models import Myuser
from django.http import HttpResponse

from configparser import ConfigParser
import subprocess 
from django.contrib.auth import login as dlogin, logout as dlogout, authenticate

# Create your views here.

# path ="/home/odroid/IOTEdge/iotedge/Configs/ssengine/config_ssengine.ini"
path = './myuser/config_ssengine.ini'



def ConfigRead():
    data = {}
    
    config_parser = ConfigParser()
    res = config_parser.read(path)

    if res:
        ftpaddress = config_parser.get('COMMON', 'FTPADDRESS', fallback='10.166.101.49')
        ftpport = config_parser.get('COMMON', 'FTPPORT', fallback=21)
        samplerate = config_parser.get('COMMON', 'samplerate', fallback=20282)
        signaltype = config_parser.get('COMMON', 'Signaltype', fallback=1)
        cutoff = config_parser.get('COMMON', 'cutoff', fallback=10141)
        usefilter = config_parser.get('COMMON', 'use filter', fallback=1)
        window = config_parser.get('COMMON', 'window', fallback=3)
        taps = config_parser.get('COMMON', 'taps', fallback=16)

        ch_count = config_parser.get('CHANNEL', 'CH_count', fallback=4)
        ch0 = config_parser.get('CHANNEL', 'ch0', fallback=1)
        ch1 = config_parser.get('CHANNEL', 'ch1', fallback=1)
        ch2 = config_parser.get('CHANNEL', 'ch2', fallback=1)
        ch3 = config_parser.get('CHANNEL', 'ch3', fallback=1)

        busedopposite = config_parser.get('DATA', 'bUsedOpposite', fallback=0)
        ch0_gravity_calc = config_parser.get('DATA', 'ch0_Gravity_Calc', fallback=5)
        ch0_gravity_base = config_parser.get('DATA', 'ch0_Gravity_Base', fallback=5)
        ch0_const_current = config_parser.get('DATA', 'ch0_Const_Current', fallback=51.5)
        ch1_gravity_calc = config_parser.get('DATA', 'ch1_Gravity_Calc', fallback=5)
        ch1_gravity_base = config_parser.get('DATA', 'ch1_Gravity_Base', fallback=5)
        ch1_const_current = config_parser.get('DATA', 'ch1_Const_Current', fallback=51.5)
        ch2_gravity_calc = config_parser.get('DATA', 'ch2_Gravity_Calc', fallback=5)
        ch2_gravity_base = config_parser.get('DATA', 'ch2_Gravity_Base', fallback=5)
        ch2_const_current = config_parser.get('DATA', 'ch2_Const_Current', fallback=51.5)
        ch3_gravity_calc = config_parser.get('DATA', 'ch3_Gravity_Calc', fallback=5)
        ch3_gravity_base = config_parser.get('DATA', 'ch3_Gravity_Base', fallback=5)
        ch3_const_current = config_parser.get('DATA', 'ch3_Const_Current', fallback=51.5)
        ch4_gravity_calc = config_parser.get('DATA', 'ch4_Gravity_Calc', fallback=5)
        ch4_gravity_base = config_parser.get('DATA', 'ch4_Gravity_Base', fallback=5)
        ch4_const_current = config_parser.get('DATA', 'ch4_Const_Current', fallback=51.5)
        ch5_gravity_calc = config_parser.get('DATA', 'ch5_Gravity_Calc', fallback=5)
        ch5_gravity_base = config_parser.get('DATA', 'ch5_Gravity_Base', fallback=5)
        ch5_const_current = config_parser.get('DATA', 'ch5_Const_Current', fallback=51.5)
        ch6_gravity_calc = config_parser.get('DATA', 'ch6_Gravity_Calc', fallback=5)
        ch6_gravity_base = config_parser.get('DATA', 'ch6_Gravity_Base', fallback=5)
        ch6_const_current = config_parser.get('DATA', 'ch6_Const_Current', fallback=51.5)
        ch7_gravity_calc = config_parser.get('DATA', 'ch7_Gravity_Calc', fallback=5)
        ch7_gravity_base = config_parser.get('DATA', 'ch7_Gravity_Base', fallback=5)
        ch7_const_current = config_parser.get('DATA', 'ch7_Const_Current', fallback=51.5)
        ch8_gravity_calc = config_parser.get('DATA', 'ch8_Gravity_Calc', fallback=5)
        ch8_gravity_base = config_parser.get('DATA', 'ch8_Gravity_Base', fallback=5)
        ch8_const_current = config_parser.get('DATA', 'ch8_Const_Current', fallback=51.5)
        ch9_gravity_calc = config_parser.get('DATA', 'ch9_Gravity_Calc', fallback=5)
        ch9_gravity_base = config_parser.get('DATA', 'ch9_Gravity_Base', fallback=5)
        ch9_const_current = config_parser.get('DATA', 'ch9_Const_Current', fallback=51.5)
        ch10_gravity_calc = config_parser.get('DATA', 'ch10_Gravity_Calc', fallback=5)
        ch10_gravity_base = config_parser.get('DATA', 'ch10_Gravity_Base', fallback=5)
        ch10_const_current = config_parser.get('DATA', 'ch10_Const_Current', fallback=51.5)
        ch11_gravity_calc = config_parser.get('DATA', 'ch11_Gravity_Calc', fallback=5)
        ch11_gravity_base = config_parser.get('DATA', 'ch11_Gravity_Base', fallback=5)
        ch11_const_current = config_parser.get('DATA', 'ch11_Const_Current', fallback=51.5)
        ch12_gravity_calc = config_parser.get('DATA', 'ch12_Gravity_Calc', fallback=5)
        ch12_gravity_base = config_parser.get('DATA', 'ch12_Gravity_Base', fallback=5)
        ch12_const_current = config_parser.get('DATA', 'ch12_Const_Current', fallback=51.5)
        ch13_gravity_calc = config_parser.get('DATA', 'ch13_Gravity_Calc', fallback=5)
        ch13_gravity_base = config_parser.get('DATA', 'ch13_Gravity_Base', fallback=5)
        ch13_const_current = config_parser.get('DATA', 'ch13_Const_Current', fallback=51.5)
        ch14_gravity_calc = config_parser.get('DATA', 'ch14_Gravity_Calc', fallback=5)
        ch14_gravity_base = config_parser.get('DATA', 'ch14_Gravity_Base', fallback=5)
        ch14_const_current = config_parser.get('DATA', 'ch14_Const_Current', fallback=51.5)
        ch15_gravity_calc = config_parser.get('DATA', 'ch15_Gravity_Calc', fallback=5)
        ch15_gravity_base = config_parser.get('DATA', 'ch15_Gravity_Base', fallback=5)
        ch15_const_current = config_parser.get('DATA', 'ch15_Const_Current', fallback=51.5)

        eqpid = config_parser.get('VIB_Setting', 'EQPID', fallback='MVT')
        chid = config_parser.get('VIB_Setting', 'CHID', fallback='B')
        debug_mode_enable = config_parser.get('VIB_Setting', 'Debug_Mode_Enable', fallback=0)
        ftp_log_enable = config_parser.get('VIB_Setting', 'FTP_Log_Enable', fallback=0)
        ftp_log_raw_enable = config_parser.get('VIB_Setting', 'FTP_Log_Raw_Enable', fallback=0)
        ftp_log_feat_enable = config_parser.get('VIB_Setting', 'FTP_Log_Feat_Enable', fallback=0)
        ftp_log_buffer = config_parser.get('VIB_Setting', 'FTP_Log_Buffer', fallback=300)
        ftp_log_split = config_parser.get('VIB_Setting', 'FTP_Log_Split', fallback=2)
        sample_n = config_parser.get('VIB_Setting', 'Sample_N', fallback=20280)
        iot_send_interval = config_parser.get('VIB_Setting', 'IoT_Send_Interval', fallback=0)
        feat_t_set = config_parser.get('VIB_Setting', 'Feat_T_Set', fallback='11111111')
        feat_f_set = config_parser.get('VIB_Setting', 'Feat_F_Set', fallback='1111111444')
        ffeat_t_set = config_parser.get('VIB_Setting', 'FFeat_T_Set', fallback='11111111')
        ffeat_f_set = config_parser.get('VIB_Setting', 'FFeat_F_Set', fallback='1111111444')
        freq_band_num = config_parser.get('VIB_Setting', 'Freq_Band_Num', fallback=3)
        freq_band_1_center = config_parser.get('VIB_Setting', 'Freq_Band_1_Center', fallback=61)
        freq_band_1_range = config_parser.get('VIB_Setting', 'Freq_Band_1_Range', fallback=10)
        freq_band_2_center = config_parser.get('VIB_Setting', 'Freq_Band_2_Center', fallback=100)
        freq_band_2_range = config_parser.get('VIB_Setting', 'Freq_Band_2_Range', fallback=10)
        freq_band_3_center = config_parser.get('VIB_Setting', 'Freq_Band_3_Center', fallback=159)
        freq_band_3_range = config_parser.get('VIB_Setting', 'Freq_Band_3_Range', fallback=10)
        freq_band_4_center = config_parser.get('VIB_Setting', 'Freq_Band_4_Center', fallback=200)
        freq_band_4_range = config_parser.get('VIB_Setting', 'Freq_Band_4_Range', fallback=10)
        freq_band_5_center = config_parser.get('VIB_Setting', 'Freq_Band_5_Center', fallback=250)
        freq_band_5_range = config_parser.get('VIB_Setting', 'Freq_Band_5_Range', fallback=10)
        freq_band_6_center = config_parser.get('VIB_Setting', 'Freq_Band_6_Center', fallback=300)
        freq_band_6_range = config_parser.get('VIB_Setting', 'Freq_Band_6_Range', fallback=10)
        freq_band_7_center = config_parser.get('VIB_Setting', 'Freq_Band_7_Center', fallback=350)
        freq_band_7_range = config_parser.get('VIB_Setting', 'Freq_Band_7_Range', fallback=10)
        freq_band_8_center = config_parser.get('VIB_Setting', 'Freq_Band_8_Center', fallback=400)
        freq_band_8_range = config_parser.get('VIB_Setting', 'Freq_Band_8_Range', fallback=10)
        freq_band_9_center = config_parser.get('VIB_Setting', 'Freq_Band_9_Center', fallback=450)
        freq_band_9_range = config_parser.get('VIB_Setting', 'Freq_Band_9_Range', fallback=10)
        freq_band_10_center = config_parser.get('VIB_Setting', 'Freq_Band_10_Center', fallback=500)
        freq_band_10_range = config_parser.get('VIB_Setting', 'Freq_Band_10_Range', fallback=10)

        
    else:
        samplerate = 20282
        ftpaddress = '10.166.101.49'
        ftpport = 21
        signaltype = 1
        cutoff = 10141
        usefilter = 1
        window = 3
        taps = 16

        ch_count = 4
        ch0 = 1
        ch1 = 1
        ch2 = 1
        ch3 = 1
        
        busedopposite = 0
        ch0_gravity_calc = 5
        ch0_gravity_base = 5
        ch0_const_current = 51.5
        ch1_gravity_calc = 5
        ch1_gravity_base = 5
        ch1_const_current = 51.5
        ch2_gravity_calc = 5
        ch2_gravity_base = 5
        ch2_const_current = 51.5
        ch3_gravity_calc = 5
        ch3_gravity_base = 5
        ch3_const_current = 51.5
        ch4_gravity_calc = 5
        ch4_gravity_base = 5
        ch4_const_current = 51.5
        ch5_gravity_calc = 5
        ch5_gravity_base = 5
        ch5_const_current = 51.5
        ch6_gravity_calc = 5
        ch6_gravity_base = 5
        ch6_const_current = 51.5
        ch7_gravity_calc = 5
        ch7_gravity_base = 5
        ch7_const_current = 51.5
        ch8_gravity_calc = 5
        ch8_gravity_base = 5
        ch8_const_current = 51.5
        ch9_gravity_calc = 5
        ch9_gravity_base = 5
        ch9_const_current = 51.5
        ch10_gravity_calc = 5
        ch10_gravity_base = 5
        ch10_const_current = 51.5
        ch11_gravity_calc = 5
        ch11_gravity_base = 5
        ch11_const_current = 51.5
        ch12_gravity_calc = 5
        ch12_gravity_base = 5
        ch12_const_current = 51.5
        ch13_gravity_calc = 5
        ch13_gravity_base = 5
        ch13_const_current = 51.5
        ch14_gravity_calc = 5
        ch14_gravity_base = 5
        ch14_const_current = 51.5
        ch15_gravity_calc = 5
        ch15_gravity_base = 5
        ch15_const_current = 51.5

        eqpid = 'MVT'
        chid = 'B'
        debug_mode_enable = 0
        ftp_log_enable = 0
        ftp_log_raw_enable = 0
        ftp_log_feat_enable = 0
        ftp_log_buffer = 300
        ftp_log_split = 2
        sample_n = 20280
        iot_send_interval =0 
        feat_t_set = '11111111'
        feat_f_set = '1111111444'
        ffeat_t_set = '11111111'
        ffeat_f_set = '1111111444'
        freq_band_num = 3
        freq_band_1_center = 61
        freq_band_1_range = 10
        freq_band_2_center = 100
        freq_band_2_range = 10
        freq_band_3_center = 159
        freq_band_3_range = 10
        freq_band_4_center = 200
        freq_band_4_range = 10
        freq_band_5_center = 250
        freq_band_5_range = 10
        freq_band_6_center = 300
        freq_band_6_range = 10
        freq_band_7_center = 350
        freq_band_7_range = 10
        freq_band_8_center = 400
        freq_band_8_range = 10
        freq_band_9_center = 450
        freq_band_9_range = 10
        freq_band_10_center = 500
        freq_band_10_range = 10
        
        
    data['ftpaddress'] = ftpaddress
    data['ftpport'] = ftpport
    data['samplerate'] = samplerate
    data['signaltype'] = signaltype
    data['cutoff'] = cutoff
    data['usefilter'] = usefilter
    data['window'] = window
    data['taps'] = taps
    
    data['ch_count'] = ch_count
    data['ch0'] = ch0
    data['ch1'] = ch1
    data['ch2'] = ch2
    data['ch3'] = ch3

    data['busedopposite'] = busedopposite
    data['ch0_gravity_calc'] = ch0_gravity_calc
    data['ch0_gravity_base'] = ch0_gravity_base
    data['ch0_const_current'] = ch0_const_current

    data['ch1_gravity_calc'] = ch1_gravity_calc
    data['ch1_gravity_base'] = ch1_gravity_base
    data['ch1_const_current'] = ch1_const_current

    data['ch2_gravity_calc'] = ch2_gravity_calc
    data['ch2_gravity_base'] = ch2_gravity_base
    data['ch2_const_current'] = ch2_const_current

    data['ch3_gravity_calc'] = ch3_gravity_calc
    data['ch3_gravity_base'] = ch3_gravity_base
    data['ch3_const_current'] = ch3_const_current

    data['ch4_gravity_calc'] = ch4_gravity_calc
    data['ch4_gravity_base'] = ch4_gravity_base
    data['ch4_const_current'] = ch4_const_current

    data['ch5_gravity_calc'] = ch5_gravity_calc
    data['ch5_gravity_base'] = ch5_gravity_base
    data['ch5_const_current'] = ch5_const_current

    data['ch6_gravity_calc'] = ch6_gravity_calc
    data['ch6_gravity_base'] = ch6_gravity_base
    data['ch6_const_current'] = ch6_const_current
    
    data['ch7_gravity_calc'] = ch7_gravity_calc
    data['ch7_gravity_base'] = ch7_gravity_base
    data['ch7_const_current'] = ch7_const_current

    data['ch8_gravity_calc'] = ch8_gravity_calc
    data['ch8_gravity_base'] = ch8_gravity_base
    data['ch8_const_current'] = ch8_const_current

    data['ch9_gravity_calc'] = ch9_gravity_calc
    data['ch9_gravity_base'] = ch9_gravity_base
    data['ch9_const_current'] = ch9_const_current

    data['ch10_gravity_calc'] = ch10_gravity_calc
    data['ch10_gravity_base'] = ch10_gravity_base
    data['ch10_const_current'] = ch10_const_current

    data['ch11_gravity_calc'] = ch11_gravity_calc
    data['ch11_gravity_base'] = ch11_gravity_base
    data['ch11_const_current'] = ch11_const_current

    data['ch12_gravity_calc'] = ch12_gravity_calc
    data['ch12_gravity_base'] = ch12_gravity_base
    data['ch12_const_current'] = ch12_const_current

    data['ch13_gravity_calc'] = ch13_gravity_calc
    data['ch13_gravity_base'] = ch13_gravity_base
    data['ch13_const_current'] = ch13_const_current
    
    data['ch14_gravity_calc'] = ch14_gravity_calc
    data['ch14_gravity_base'] = ch14_gravity_base
    data['ch14_const_current'] = ch14_const_current

    data['ch15_gravity_calc'] = ch15_gravity_calc
    data['ch15_gravity_base'] = ch15_gravity_base
    data['ch15_const_current'] = ch15_const_current
    
    data['eqpid'] = eqpid;
    data['chid'] = chid;
    data['debug_mode_enable'] = debug_mode_enable
    data['ftp_log_raw_enable'] = ftp_log_raw_enable
    data['ftp_log_raw_enable'] = ftp_log_raw_enable
    data['ftp_log_feat_enable'] = ftp_log_feat_enable
    data['ftp_log_buffer'] = ftp_log_buffer
    data['ftp_log_split'] = ftp_log_split
    data['sample_n'] = sample_n
    data['iot_send_interval'] = iot_send_interval
    data['feat_t_set'] = feat_t_set
    data['feat_f_set'] = feat_f_set
    data['ffeat_t_set'] = ffeat_t_set
    data['ffeat_f_set'] = ffeat_f_set
    data['freq_band_num'] = freq_band_num
    data['freq_band_1_center'] = freq_band_1_center
    data['freq_band_1_range'] = freq_band_1_range
    data['freq_band_2_center'] = freq_band_2_center 
    data['freq_band_2_range'] = freq_band_2_range
    data['freq_band_3_center'] = freq_band_3_center
    data['freq_band_3_range'] = freq_band_3_range
    data['freq_band_4_center'] = freq_band_4_center
    data['freq_band_4_range'] = freq_band_4_range
    data['freq_band_5_center'] = freq_band_5_center
    data['freq_band_5_range'] = freq_band_5_range
    data['freq_band_6_center'] = freq_band_6_center
    data['freq_band_6_range'] = freq_band_6_range
    data['freq_band_7_center'] = freq_band_7_center
    data['freq_band_7_range'] = freq_band_7_range
    data['freq_band_8_center'] = freq_band_8_center
    data['freq_band_8_range'] = freq_band_8_range
    data['freq_band_9_center'] = freq_band_9_center
    data['freq_band_9_range'] = freq_band_9_range
    data['freq_band_10_center'] = freq_band_10_center
    data['freq_band_10_range'] = freq_band_10_range

    return data


def ConfigWrite(data):
    config_writer = ConfigParser()
    config_writer.optionxform = lambda option: option
    config_writer['COMMON'] = {
			'FTPADDRESS': data['ftpaddress'],
			'FTPPORT': data['ftpport'],
			'samplerate': data['samplerate'], 
			'Signaltype': data['signaltype'],
            'cutoff' : data['cutoff'],
            'use filter' : data['usefilter'],
            'window' : data['window'],
            'taps' : data['taps'],
	} 
    config_writer['CHANNEL'] = {
            'CH_count' : data['ch_count'],
            'CH0' : data['ch0'],
            'CH1' : data['ch1'],
            'CH2' : data['ch2'],
            'CH3' : data['ch3'],
    }
    config_writer['DATA'] = {
            'bUsedOpposite' : data['busedopposite'],
            'ch0_Gravity_Calc' : data['ch0_gravity_calc'],
            'ch0_Gravity_Base' : data['ch0_gravity_base'],
            'ch0_Const_Current' : data['ch0_const_current'],
            'ch1_Gravity_Calc' : data['ch1_gravity_calc'],
            'ch1_Gravity_Base' : data['ch1_gravity_base'],
            'ch1_Const_Current' : data['ch1_const_current'],
            'ch2_Gravity_Calc' : data['ch2_gravity_calc'],
            'ch2_Gravity_Base' : data['ch2_gravity_base'],
            'ch2_Const_Current' : data['ch2_const_current'],
            'ch3_Gravity_Calc' : data['ch3_gravity_calc'],
            'ch3_Gravity_Base' : data['ch3_gravity_base'],
            'ch3_Const_Current' : data['ch3_const_current'],
            'ch4_Gravity_Calc' : data['ch4_gravity_calc'],
            'ch4_Gravity_Base' : data['ch4_gravity_base'],
            'ch4_Const_Current' : data['ch4_const_current'],
            'ch5_Gravity_Calc' : data['ch4_gravity_calc'],
            'ch5_Gravity_Base' : data['ch5_gravity_base'],
            'ch5_Const_Current' : data['ch5_const_current'],
            'ch6_Gravity_Calc' : data['ch6_gravity_calc'],
            'ch6_Gravity_Base' : data['ch6_gravity_base'],
            'ch6_Const_Current' : data['ch6_const_current'],
            'ch7_Gravity_Calc' : data['ch7_gravity_calc'],
            'ch7_Gravity_Base' : data['ch7_gravity_base'],
            'ch7_Const_Current' : data['ch7_const_current'],
            'ch8_Gravity_Calc' : data['ch8_gravity_calc'],
            'ch8_Gravity_Base' : data['ch8_gravity_base'],
            'ch8_Const_Current' : data['ch8_const_current'],
            'ch9_Gravity_Calc' : data['ch9_gravity_calc'],
            'ch9_Gravity_Base' : data['ch9_gravity_base'],
            'ch9_Const_Current' : data['ch9_const_current'],
            'ch10_Gravity_Calc' : data['ch10_gravity_calc'],
            'ch10_Gravity_Base' : data['ch10_gravity_base'],
            'ch10_Const_Current' : data['ch10_const_current'],
            'ch11_Gravity_Calc' : data['ch11_gravity_calc'],
            'ch11_Gravity_Base' : data['ch11_gravity_base'],
            'ch11_Const_Current' : data['ch11_const_current'],
            'ch12_Gravity_Calc' : data['ch12_gravity_calc'],
            'ch12_Gravity_Base' : data['ch12_gravity_base'],
            'ch12_Const_Current' : data['ch12_const_current'],
            'ch13_Gravity_Calc' : data['ch13_gravity_calc'],
            'ch13_Gravity_Base' : data['ch13_gravity_base'],
            'ch13_Const_Current' : data['ch13_const_current'],
            'ch14_Gravity_Calc' : data['ch14_gravity_calc'],
            'ch14_Gravity_Base' : data['ch14_gravity_base'],
            'ch14_Const_Current' : data['ch14_const_current'],
            'ch15_Gravity_Calc' : data['ch15_gravity_calc'],
            'ch15_Gravity_Base' : data['ch15_gravity_base'],
            'ch15_Const_Current' : data['ch15_const_current'],
        }    

    config_writer['VIB_Setting'] = {
            'EQPID' : data['eqpid'],
            'CHID' : data['chid'],
            'Debug_Mode_Enable' : data['debug_mode_enable'],
            'FTP_Log_Raw_Enable' : data['ftp_log_raw_enable'],
            'FTP_Log_Feat_Enable' : data['ftp_log_feat_enable'],
            'FTP_Log_Buffer' : data['ftp_log_buffer'],
            'FTP_Log_Split' : data['ftp_log_split'],
            'Sample_N' : data['sample_n'],
            'IoT_Send_Interval' : data['iot_send_interval'],
            'Feat_T_Set' : data['feat_t_set'],
            'Feat_F_Set' : data['feat_f_set'],
            'FFeat_T_Set' : data['ffeat_t_set'],
            'FFeat_F_Set' : data['ffeat_f_set'],
            'Freq_Band_Num' : data['freq_band_num'],
            'Freq_Band_1_Center' : data['freq_band_1_center'],
            'Freq_Band_1_Range' : data['freq_band_1_range'],
            'Freq_Band_2_Center' : data['freq_band_2_center'],
            'Freq_Band_2_Range' : data['freq_band_2_range'],
            'Freq_Band_3_Center' : data['freq_band_3_center'],
            'Freq_Band_3_Range' : data['freq_band_3_range'],
            'Freq_Band_4_Center' : data['freq_band_4_center'],
            'Freq_Band_4_Range' : data['freq_band_4_range'],
            'Freq_Band_5_Center' : data['freq_band_5_center'],
            'Freq_Band_5_Range' : data['freq_band_5_range'],
            'Freq_Band_6_Center' : data['freq_band_6_center'],
            'Freq_Band_6_Range' : data['freq_band_6_range'],
            'Freq_Band_7_Center' : data['freq_band_7_center'],
            'Freq_Band_7_Range' : data['freq_band_7_range'],
            'Freq_Band_8_Center' : data['freq_band_8_center'],
            'Freq_Band_8_Range' : data['freq_band_8_range'],
            'Freq_Band_9_Center' : data['freq_band_9_center'],
            'Freq_Band_9_Range' : data['freq_band_9_range'],
            'Freq_Band_10_Center' : data['freq_band_10_center'],
            'Freq_Band_10_Range' : data['freq_band_10_range'],
        }
#    for key in data.keys():
#        print(key, ":", data[key])
 
    with open(path, 'w') as configfile:
        config_writer.write(configfile)



def index(request):
    response_data = {}

    if  request.user.is_authenticated:
        response_data = ConfigRead() 

        response_data['username'] = request.user.username
        return render( request, 'home.html', response_data ) 

    return redirect('/user/login')

def save(request):
    response_data = {}
    response_data['error'] = '' 

    if request.user.is_authenticated:      
        response_data['ftpaddress'] = request.POST.get('ftpaddress', "10.166.101.49")
        response_data['ftpport'] = request.POST.get('ftpport', 21)
        response_data['samplerate'] = request.POST.get('samplerate', 20282)
        if int(request.POST.get('samplerate')) > 65536:
            response_data['error'] = "Wrong value of samplerate," + request.POST.get('samplerate')

        response_data['signaltype'] = request.POST.get('signaltype', 1)
        response_data['cutoff'] = request.POST.get('cutoff', 10141)
        response_data['usefilter'] = request.POST.get('usefilter', 1)
        response_data['window'] = request.POST.get('window', 3)
        if int(request.POST.get('window')) > 100:
            response_data['error'] = "Wrong value of window," + request.POST.get('window')

        response_data['taps'] = request.POST.get('taps', 64)
        if int(request.POST.get('taps')) > 100:
            response_data['error'] = "Wrong value of taps," + request.POST.get('taps')

        response_data['ch_count'] = request.POST.get('ch_count', 4)
        if int(request.POST.get('ch_count')) > 4:
            response_data['error'] = "Wrong value of CH_count," + request.POST.get('ch_count')
        response_data['ch0'] = request.POST.get('ch0', 1)
        response_data['ch1'] = request.POST.get('ch1', 1)
        response_data['ch2'] = request.POST.get('ch2', 1)
        response_data['ch3'] = request.POST.get('ch3', 1)

        response_data['busedopposite'] = request.POST.get('busedopposite', 0)
        response_data['ch0_gravity_calc'] = request.POST.get('ch0_gravity_calc', 5)
        response_data['ch0_gravity_base'] = request.POST.get('ch0_gravity_base', 5)
        response_data['ch0_const_current'] = request.POST.get('ch0_const_current', 51.5)
        response_data['ch1_gravity_calc'] = request.POST.get('ch1_gravity_calc', 5)
        response_data['ch1_gravity_base'] = request.POST.get('ch1_gravity_base', 5)
        response_data['ch1_const_current'] = request.POST.get('ch1_const_current', 51.5)
        response_data['ch2_gravity_calc'] = request.POST.get('ch2_gravity_calc', 5)
        response_data['ch2_gravity_base'] = request.POST.get('ch2_gravity_base', 5)
        response_data['ch2_const_current'] = request.POST.get('ch2_const_current', 51.5)
        response_data['ch3_gravity_calc'] = request.POST.get('ch3_gravity_calc', 5)
        response_data['ch3_gravity_base'] = request.POST.get('ch3_gravity_base', 5)
        response_data['ch3_const_current'] = request.POST.get('ch3_const_current', 51.5)
        response_data['ch4_gravity_calc'] = request.POST.get('ch4_gravity_calc', 5)
        response_data['ch4_gravity_base'] = request.POST.get('ch4_gravity_base', 5)
        response_data['ch4_const_current'] = request.POST.get('ch4_const_current', 51.5)
        response_data['ch5_gravity_calc'] = request.POST.get('ch5_gravity_calc', 5)
        response_data['ch5_gravity_base'] = request.POST.get('ch5_gravity_base', 5)
        response_data['ch5_const_current'] = request.POST.get('ch5_const_current', 51.5)
        response_data['ch6_gravity_calc'] = request.POST.get('ch6_gravity_calc', 5)
        response_data['ch6_gravity_base'] = request.POST.get('ch6_gravity_base', 5)
        response_data['ch6_const_current'] = request.POST.get('ch6_const_current', 51.5)
        response_data['ch7_gravity_calc'] = request.POST.get('ch7_gravity_calc', 5)
        response_data['ch7_gravity_base'] = request.POST.get('ch7_gravity_base', 5)
        response_data['ch7_const_current'] = request.POST.get('ch7_const_current', 51.5)
        response_data['ch8_gravity_calc'] = request.POST.get('ch8_gravity_calc', 5)
        response_data['ch8_gravity_base'] = request.POST.get('ch8_gravity_base', 5)
        response_data['ch8_const_current'] = request.POST.get('ch8_const_current', 51.5)
        response_data['ch9_gravity_calc'] = request.POST.get('ch9_gravity_calc', 5)
        response_data['ch9_gravity_base'] = request.POST.get('ch9_gravity_base', 5)
        response_data['ch9_const_current'] = request.POST.get('ch9_const_current', 51.5)
        response_data['ch10_gravity_calc'] = request.POST.get('ch10_gravity_calc', 5)
        response_data['ch10_gravity_base'] = request.POST.get('ch10_gravity_base', 5)
        response_data['ch10_const_current'] = request.POST.get('ch10_const_current', 51.5)
        response_data['ch11_gravity_calc'] = request.POST.get('ch11_gravity_calc', 5)
        response_data['ch11_gravity_base'] = request.POST.get('ch11_gravity_base', 5)
        response_data['ch11_const_current'] = request.POST.get('ch11_const_current', 51.5)
        response_data['ch12_gravity_calc'] = request.POST.get('ch12_gravity_calc', 5)
        response_data['ch12_gravity_base'] = request.POST.get('ch12_gravity_base', 5)
        response_data['ch12_const_current'] = request.POST.get('ch12_const_current', 51.5)
        response_data['ch13_gravity_calc'] = request.POST.get('ch13_gravity_calc', 5)
        response_data['ch13_gravity_base'] = request.POST.get('ch13_gravity_base', 5)
        response_data['ch13_const_current'] = request.POST.get('ch13_const_current', 51.5)
        response_data['ch14_gravity_calc'] = request.POST.get('ch14_gravity_calc', 5)
        response_data['ch14_gravity_base'] = request.POST.get('ch14_gravity_base', 5)
        response_data['ch14_const_current'] = request.POST.get('ch14_const_current', 51.5)
        response_data['ch15_gravity_calc'] = request.POST.get('ch15_gravity_calc', 5)
        response_data['ch15_gravity_base'] = request.POST.get('ch15_gravity_base', 5)
        response_data['ch15_const_current'] = request.POST.get('ch15_const_current', 51.5)

        response_data['eqpid'] = request.POST.get('eqpid', 'MVT')
        response_data['chid'] = request.POST.get('chid', 'B')
        response_data['debug_mode_enable'] = request.POST.get('debug_mode_enable', 0)
        response_data['ftp_log_raw_enable'] = request.POST.get('ftp_log_raw_enable', 0)
        response_data['ftp_log_feat_enable'] = request.POST.get('ftp_log_feat_enable', 0)
        response_data['ftp_log_buffer'] = request.POST.get('ftp_log_buffer', 300)
        response_data['ftp_log_split'] = request.POST.get('ftp_log_split', 2)
        response_data['sample_n'] = request.POST.get('sample_n', 20280)
        response_data['iot_send_interval'] = request.POST.get('iot_send_interval', 0)
        response_data['feat_t_set'] = request.POST.get('feat_t_set', '11111111')
        response_data['feat_f_set'] = request.POST.get('feat_f_set', '1111111444')
        response_data['ffeat_t_set'] = request.POST.get('ffeat_t_set', '11111111')
        response_data['ffeat_f_set'] = request.POST.get('ffeat_f_set', '1111111444')
        response_data['freq_band_num'] = request.POST.get('freq_band_num', 3)
        response_data['freq_band_1_center'] = request.POST.get('freq_band_1_center', 61)
        response_data['freq_band_1_range'] = request.POST.get('freq_band_1_range', 10)
        response_data['freq_band_2_center'] = request.POST.get('freq_band_2_center', 100)
        response_data['freq_band_2_range'] = request.POST.get('freq_band_2_range', 10)
        response_data['freq_band_3_center'] = request.POST.get('freq_band_3_center', 159)
        response_data['freq_band_3_range'] = request.POST.get('freq_band_3_range', 10)
        response_data['freq_band_4_center'] = request.POST.get('freq_band_4_center', 200)
        response_data['freq_band_4_range'] = request.POST.get('freq_band_4_range', 10)
        response_data['freq_band_5_center'] = request.POST.get('freq_band_5_center', 250)
        response_data['freq_band_5_range'] = request.POST.get('freq_band_5_range', 10)
        response_data['freq_band_6_center'] = request.POST.get('freq_band_6_center', 300)
        response_data['freq_band_6_range'] = request.POST.get('freq_band_6_range', 10)
        response_data['freq_band_7_center'] = request.POST.get('freq_band_7_center', 350)
        response_data['freq_band_7_range'] = request.POST.get('freq_band_7_range', 10)
        response_data['freq_band_8_center'] = request.POST.get('freq_band_8_center', 400)
        response_data['freq_band_8_range'] = request.POST.get('freq_band_8_range', 10)
        response_data['freq_band_9_center'] = request.POST.get('freq_band_9_center', 450)
        response_data['freq_band_9_range'] = request.POST.get('freq_band_9_range', 10)
        response_data['freq_band_10_center'] = request.POST.get('freq_band_10_center', 500)
        response_data['freq_band_10_range'] = request.POST.get('freq_band_10_range', 10)
   

        response_data['username'] = request.user.username
        if response_data['error'] != '' :
            return render( request, 'home.html', response_data ) 
		
        ConfigWrite(response_data)	
        return render( request, 'saved.html', response_data)

    return redirect('/user/login')


def login(request):
    response_data = {}

    if request.method == "GET" :
        return render(request, 'login.html')

    elif request.method == "POST":
        login_username = request.POST.get('username', None)
        login_password = request.POST.get('password', None)

        if not (login_username and login_password):
            response_data['error']="Please, Input your id & password."
        else : 
            user = authenticate(username=login_username, password=login_password)
            if user is not None:
                dlogin(request,user)
                return redirect('/')
            else:
                response_data['error'] = "Wrong password !!"

        return render(request, 'login.html',response_data)



def logout(request):
    dlogout(request)

    return redirect('/')



def restart(request):
    response_data = {}

    if request.user.is_authenticated:
        run = subprocess.check_output('./compose.sh')
        print('run=',run)
        response_data['username'] = request.user.username
        return render(request, 'restart.html', response_data)
        
    return redirect('/user/login')

