# ecoding:utf-8
import cx_Oracle
import pandas as pd


class OracleService:
    def __init__(self):
        self.conn = cx_Oracle.connect('WBXDIAGNS/pass@10.29.42.50/teodb.webex.com')
        self.cur = self.conn.cursor()

    # def create_table(self):


    def insert(self, meetingDF, participantDF, day):
        sql = "SELECT count(*) as count from DAP_JMFUSER WHERE DATATIME='" + day + "'"
        print sql
        self.cur.execute(sql)  # 使用cursor进行各种操作
        dap_jmfuser_row = self.cur.fetchone()
        sql = "SELECT * from DAP_JMFOVERALL WHERE DATATIME='" + day + "'"
        print sql
        self.cur.execute(sql)  # 使用cursor进行各种操作
        dap_jmfoverall_row = self.cur.fetchone()
        self.cur.close()  # 关闭cursor
        self.conn.close()
        return dap_jmfuser_row[0], dap_jmfoverall_row


if __name__ == '__main__':
    import glob

    files = glob.glob('~/source/csv/userLevelAllInOnedata_AllSites_*')
    for file in files:
        print file

    # result = pd.concat([pd.read_csv(file, sep="	") for file in files], ignore_index=True)
    # print result.shape


    # colnum="""STARTDATE,SITEID,CONFID,MEETINGNUMBER,UID,GID,ISCMR,STARTTIME,ENDTIME,DURATION,USEROS,USERBROWSER,COUNTRY,TCPPERCENT,UDPPERCENT,LATENCY,PACKETLOSS,TCP,UDP,CALLQUALITY,USERJMT"""
    # print colnum.split(",")
    # print len(colnum.split(","))
    #
    # str = """2017-09-06	12345701	71926045754833266	342893190	0	2091679162	N	21:34	21:52	18	intel mac
    # os x 10.11	Chrome 60	UNKNOWN	0%	100%	299.6932881673177	0.0	0	3	Good	54"""
    # print str.split("	")
    # print len(str.split("	"))
    #
    # str1="""2017-09-05	12345701	58288414518196695	342609148	0	2091370502	Y	07:24	07:25	2			UNKNOWN"""
    # print str1.split("	")
    # print len(str1.split("	"))
    #
    # str2="""2017-09-02	12345701	71968144347919589	342619517	492545182	0	Y	09:35	09:35	1			UNKNOWN"""
    # print str2.split("	")
    # print len(str2.split("	"))
    #
    # str3="""2017-09-03	12345701	72029769969988896	152724043	0	175083513	Y	02:13	02:15	2	WbxTPAgent	wbxtpgw	UNITED STATES								1"""
    # print str3.split("	")
    # print len(str3.split("	"))
    #
    # print "======================================================================================="
    # colnum="""STARTDATE,SITEID,CONFID,MEETINGNUMBER,HOSTID,STARTTIME,ENDTIME,VOIPUSER,VOIPMINUTES,CCATOTALMIN,PSTNTOTALMIN,PSTNCIN,PSTNCOUT,CCACIN,CCACOUT,MEETINGMINUTES,NUMBEROFPARTICIPANTS,PSTNCUSER,CCACUSER"""
    # print colnum.split(",")
    # print len(colnum.split(","))
    #
    # str = """2017-10-23	12363752	425590274		494518192	10:01	12:01	1	121	0	0	0.0	0.0	0.0	0.0	0	0	0	0"""
    # print str.split("	")
    # print len(str.split("	"))
    #
    # str1="""2017-10-23	12345701	76163652050270259	346483712	481155612	15:57	16:36	1	35	0	71	0.0	71.0	0.0	0.0	108	3	2	0"""
    # print str1.split("	")
    # print len(str1.split("	"))
    #
    # str2="""2017-10-23	12363752	425590211		494518192	04:41	06:41	1	121	0	0	0.0	0.0	0.0	0.0	0	0	0	0"""
    # print str2.split("	")
    # print len(str2.split("	"))











