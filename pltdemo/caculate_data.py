# coding=utf-8
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd

myfont = FontProperties(fname='/Library/Fonts/Songti.ttc')
plt.figure(figsize=(10, 4))


douban_cpcUgu_MAE = pd.Series(
    [0.57183, 0.56407, 0.56022, 0.55821, 0.55708, 0.55802, 0.55435, 0.55894, 0.55895, 0.55875])
douban_cpcUgu_RMSE = pd.Series([0.73382, 0.72378, 0.72045, 0.71644, 0.71714, 0.71624, 0.71124, 0.7137, 0.71754, 0.7169])

douban_cpc_MAE = pd.Series([0.5725, 0.56399, 0.56164, 0.55829, 0.55884, 0.5588, 0.55686, 0.55855, 0.55853, 0.55902])
douban_cpc_RMSE = pd.Series([0.73468, 0.72431, 0.72111, 0.71712, 0.71342, 0.71832, 0.71439, 0.71699, 0.71776, 0.71678])

douban_ugu_MAE = (douban_cpcUgu_MAE - 0.4 * douban_cpc_MAE) / 0.6
douban_ugu_RMSE = (douban_cpcUgu_RMSE - 0.4 * douban_cpc_RMSE) / 0.6

print 'MAE\t\t', ' '.join(str(e) for e in douban_ugu_MAE.values)
print 'RMSE\t', ' '.join(str(e) for e in douban_ugu_RMSE.values)


# print '0.1*cpc+0.9*ugu'
# douban_cpcUgu_MAE_1_9 = 0.1 * douban_cpc_MAE + 0.9 * douban_ugu_MAE
# douban_cpcUgu_RMSE_1_9 = 0.1 * douban_cpc_RMSE + 0.9 * douban_ugu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in douban_cpcUgu_MAE_1_9.values)
# print 'RMSE\t', ' '.join(str(e) for e in douban_cpcUgu_RMSE_1_9.values)
# # douban_cpcUgu_MAE_1_9.plot(label='0.1*cpc+0.9*ugu')
# # douban_cpcUgu_RMSE_1_9.plot(label='0.1*cpc+0.9*ugu')
#
#
# print '0.2*cpc+0.8*ugu'
# douban_cpcUgu_MAE_2_8 = 0.2 * douban_cpc_MAE + 0.8 * douban_ugu_MAE
# douban_cpcUgu_RMSE_2_8 = 0.2 * douban_cpc_RMSE + 0.8 * douban_ugu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in douban_cpcUgu_MAE_2_8.values)
# print 'RMSE\t',' '.join(str(e) for e in douban_cpcUgu_RMSE_2_8.values)
# # douban_cpcUgu_MAE_2_8.plot(label='0.2*cpc+0.8*ugu')
# # douban_cpcUgu_RMSE_2_8.plot(label='0.2*cpc+0.8*ugu')
#
#
# print '0.3*cpc+0.7*ugu'
# douban_cpcUgu_MAE_3_7 = 0.3 * douban_cpc_MAE + 0.7 * douban_ugu_MAE
# douban_cpcUgu_RMSE_3_7 = 0.3 * douban_cpc_RMSE + 0.7 * douban_ugu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in douban_cpcUgu_MAE_3_7.values)
# print 'RMSE\t',' '.join(str(e) for e in douban_cpcUgu_RMSE_3_7.values)
# # douban_cpcUgu_MAE_3_7.plot(label='0.3*cpc+0.7*ugu')
# # douban_cpcUgu_RMSE_3_7.plot(label='0.3*cpc+0.7*ugu')
#
#
# print '0.4*cpc+0.6*ugu'
# douban_cpcUgu_MAE_4_6 = 0.4 * douban_cpc_MAE + 0.6 * douban_ugu_MAE
# douban_cpcUgu_RMSE_4_6 = 0.4 * douban_cpc_RMSE + 0.6 * douban_ugu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in douban_cpcUgu_MAE_4_6.values)
# print 'RMSE\t',' '.join(str(e) for e in douban_cpcUgu_RMSE_4_6.values)
# # douban_cpcUgu_MAE_4_6.plot(label='0.4*cpc+0.6*ugu')
# # douban_cpcUgu_RMSE_4_6.plot(label='0.4*cpc+0.6*ugu')
#
#
# print '0.5*cpc+0.5*ugu'
# douban_cpcUgu_MAE_5_5 = 0.5 * douban_cpc_MAE + 0.5 * douban_ugu_MAE
# douban_cpcUgu_RMSE_5_5 = 0.5 * douban_cpc_RMSE + 0.5 * douban_ugu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in douban_cpcUgu_MAE_5_5.values)
# print 'RMSE\t',' '.join(str(e) for e in douban_cpcUgu_RMSE_5_5.values)
# # douban_cpcUgu_MAE_5_5.plot(label='0.5*cpc+0.5*ugu')
# # douban_cpcUgu_RMSE_5_5.plot(label='0.5*cpc+0.5*ugu')
#
# print '0.6*cpc+0.4*ugu'
# douban_cpcUgu_MAE_6_4 = 0.6 * douban_cpc_MAE + 0.4 * douban_ugu_MAE
# douban_cpcUgu_RMSE_6_4 = 0.6 * douban_cpc_RMSE + 0.4 * douban_ugu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in douban_cpcUgu_MAE_6_4.values)
# print 'RMSE\t',' '.join(str(e) for e in douban_cpcUgu_RMSE_6_4.values)
# # douban_cpcUgu_MAE_6_4.plot(label='0.6*cpc+0.4*ugu')
# # douban_cpcUgu_RMSE_6_4.plot(label='0.6*cpc+0.4*ugu')
#
#
# print '0.7*cpc+0.3*ugu'
# douban_cpcUgu_MAE_7_3 = 0.7 * douban_cpc_MAE + 0.3 * douban_ugu_MAE
# douban_cpcUgu_RMSE_7_3 = 0.7 * douban_cpc_RMSE + 0.3 * douban_ugu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in douban_cpcUgu_MAE_7_3.values)
# print 'RMSE\t',' '.join(str(e) for e in douban_cpcUgu_RMSE_7_3.values)
# # douban_cpcUgu_MAE_7_3.plot(label='0.7*cpc+0.3*ugu')
# # douban_cpcUgu_RMSE_7_3.plot(label='0.7*cpc+0.3*ugu')
#
#
# print '0.8*cpc+0.2*ugu'
# douban_cpcUgu_MAE_8_2 = 0.8 * douban_cpc_MAE + 0.2 * douban_ugu_MAE
# douban_cpcUgu_RMSE_8_2 = 0.8 * douban_cpc_RMSE + 0.2 * douban_ugu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in douban_cpcUgu_MAE_8_2.values)
# print 'RMSE\t',' '.join(str(e) for e in douban_cpcUgu_RMSE_8_2.values)
# # douban_cpcUgu_MAE_8_2.plot(label='0.8*cpc+0.2*ugu')
# # douban_cpcUgu_RMSE_8_2.plot(label='0.8*cpc+0.2*ugu')
#
#
# print '0.9*cpc+0.1*ugu'
# douban_cpcUgu_MAE_9_1 = 0.1 * douban_cpc_MAE + 0.9 * douban_ugu_MAE
# douban_cpcUgu_RMSE_9_1 = 0.1 * douban_cpc_RMSE + 0.9 * douban_ugu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in douban_cpcUgu_MAE_9_1.values)
# print 'RMSE\t',' '.join(str(e) for e in douban_cpcUgu_RMSE_9_1.values)
# # douban_cpcUgu_MAE_9_1.plot(label='0.9*cpc+0.1*ugu')
# # douban_cpcUgu_RMSE_9_1.plot(label='0.9*cpc+0.1*ugu')
#
#
#
# # 当训练集合测试集比为50%时，在MAE评价指标上采用：0.9*cpc+0.1*ugu，效果最好 CPSIm: 0.5562 。cpc:0.55884 pcc:0.5581
# # 当训练集合测试集比为50%时，在RMSE评价指标上采用：0.8*cpc+0.2*ugu，效果最好 CPSIm:0.71466。 cpc:0.71342 pcc:0.72004
#
# # douban_cpcUgu_MAE_9_1.plot(label="CPSIm(0.9*cpc+0.1*ugu)")
# # douban_cpc_MAE.plot(label="cpc")
# # douban_ugu_MAE.plot(label="ugu")
#
# douban_cpcUgu_RMSE_8_2.plot(label="CPSIm(0.8*cpc+0.2*ugu)")
# douban_cpc_RMSE.plot(label="cpc")
# douban_ugu_RMSE.plot(label="ugu")
#
# # plt.title("douban RMSE")
# plt.legend()
# plt.show()
#
#
# print "=" * 20
#
# yelp_cpcUcu_MAE = pd.Series(
#     [0.857232, 0.84854, 0.848683, 0.847211, 0.842211, 0.845398, 0.843259, 0.844101, 0.847134, 0.853053])
# yelp_cpcUcu_RMSE = pd.Series(
#     [1.116654, 1.103245, 1.10383, 1.102918, 1.096491, 1.08729, 1.100096, 1.099613, 1.100597, 1.110463])
# yelp_cpc_MAE = pd.Series(
#     [0.858582, 0.84991, 0.849614, 0.852794, 0.845739, 0.844346, 0.845175, 0.850605, 0.848854, 0.847123])
# yelp_cpc_RMSE = pd.Series(
#     [1.115507, 1.104035, 1.106813, 1.111985, 1.102323, 1.099561, 1.100729, 1.104909, 1.104872, 1.101328])
#
# yelp_ucu_MAE = (yelp_cpcUcu_MAE - 0.4 * yelp_cpc_MAE) / 0.6
# yelp_ucu_RMSE = (yelp_cpcUcu_RMSE - 0.4 * yelp_cpc_RMSE) / 0.6
#
#
# print '0.0*cpc+1.0*ucu'
# print 'MAE\t\t', ' '.join(str(e) for e in yelp_ucu_MAE.values)
# print 'RMSE\t', ' '.join(str(e) for e in yelp_ucu_RMSE.values)
#
# print '0.1*cpc+0.9*ucu'
# yelp_cpcUcu_MAE_1_9 = 0.1 * yelp_cpc_MAE + 0.9 * yelp_ucu_MAE
# yelp_cpcUcu_RMSE_1_9 = 0.1 * yelp_cpc_RMSE + 0.9 * yelp_ucu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in yelp_cpcUcu_MAE_1_9.values)
# print 'RMSE\t', ' '.join(str(e) for e in yelp_cpcUcu_RMSE_1_9.values)
# # douban_cpcUgu_MAE_1_9.plot(label='0.1*cpc+0.9*ugu')
# # douban_cpcUgu_RMSE_1_9.plot(label='0.1*cpc+0.9*ugu')
#
#
# print '0.2*cpc+0.8*ucu'
# yelp_cpcUcu_MAE_2_8 = 0.2 * yelp_cpc_MAE + 0.8 * yelp_ucu_MAE
# yelp_cpcUcu_RMSE_2_8 = 0.2 * yelp_cpc_RMSE + 0.8 * yelp_ucu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in yelp_cpcUcu_MAE_2_8.values)
# print 'RMSE\t',' '.join(str(e) for e in yelp_cpcUcu_RMSE_2_8.values)
# # douban_cpcUgu_MAE_2_8.plot(label='0.2*cpc+0.8*ugu')
# # douban_cpcUgu_RMSE_2_8.plot(label='0.2*cpc+0.8*ugu')
#
#
# print '0.3*cpc+0.7*ucu'
# yelp_cpcUcu_MAE_3_7 = 0.3 * yelp_cpc_MAE + 0.7 * yelp_ucu_MAE
# yelp_cpcUcu_RMSE_3_7 = 0.3 * yelp_cpc_RMSE + 0.7 * yelp_ucu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in yelp_cpcUcu_MAE_3_7.values)
# print 'RMSE\t',' '.join(str(e) for e in yelp_cpcUcu_RMSE_3_7.values)
# # douban_cpcUgu_MAE_3_7.plot(label='0.3*cpc+0.7*ugu')
# # douban_cpcUgu_RMSE_3_7.plot(label='0.3*cpc+0.7*ugu')
#
#
# print '0.4*cpc+0.6*ucu'
# yelp_cpcUcu_MAE_4_6 = 0.4 * yelp_cpc_MAE + 0.6 * yelp_ucu_MAE
# yelp_cpcUcu_RMSE_4_6 = 0.4 * yelp_cpc_RMSE + 0.6 * yelp_ucu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in yelp_cpcUcu_MAE_4_6.values)
# print 'RMSE\t',' '.join(str(e) for e in yelp_cpcUcu_RMSE_4_6.values)
# # douban_cpcUgu_MAE_4_6.plot(label='0.4*cpc+0.6*ugu')
# # douban_cpcUgu_RMSE_4_6.plot(label='0.4*cpc+0.6*ugu')
#
#
# print '0.5*cpc+0.5*ucu'
# yelp_cpcUcu_MAE_5_5 = 0.5 * yelp_cpc_MAE + 0.5 * yelp_ucu_MAE
# yelp_cpcUcu_RMSE_5_5 = 0.5 * yelp_cpc_RMSE + 0.5 * yelp_ucu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in yelp_cpcUcu_MAE_5_5.values)
# print 'RMSE\t',' '.join(str(e) for e in yelp_cpcUcu_RMSE_5_5.values)
# # douban_cpcUgu_MAE_5_5.plot(label='0.5*cpc+0.5*ugu')
# # douban_cpcUgu_RMSE_5_5.plot(label='0.5*cpc+0.5*ugu')
#
# print '0.6*cpc+0.4*ucu'
# yelp_cpcUcu_MAE_6_4 = 0.6 * yelp_cpc_MAE + 0.4 * yelp_ucu_MAE
# yelp_cpcUcu_RMSE_6_4 = 0.6 * yelp_cpc_RMSE + 0.4 * yelp_ucu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in yelp_cpcUcu_MAE_6_4.values)
# print 'RMSE\t',' '.join(str(e) for e in yelp_cpcUcu_RMSE_6_4.values)
# # douban_cpcUgu_MAE_6_4.plot(label='0.6*cpc+0.4*ugu')
# # douban_cpcUgu_RMSE_6_4.plot(label='0.6*cpc+0.4*ugu')
#
#
# print '0.7*cpc+0.3*ucu'
# yelp_cpcUcu_MAE_7_3 = 0.7 * yelp_cpc_MAE + 0.3 * yelp_ucu_MAE
# yelp_cpcUcu_RMSE_7_3 = 0.7 * yelp_cpc_RMSE + 0.3 * yelp_ucu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in yelp_cpcUcu_MAE_7_3.values)
# print 'RMSE\t',' '.join(str(e) for e in yelp_cpcUcu_RMSE_7_3.values)
# # douban_cpcUgu_MAE_7_3.plot(label='0.7*cpc+0.3*ugu')
# # douban_cpcUgu_RMSE_7_3.plot(label='0.7*cpc+0.3*ugu')
#
#
# print '0.8*cpc+0.2*ucu'
# yelp_cpcUcu_MAE_8_2 = 0.8 * yelp_cpc_MAE + 0.2 * yelp_ucu_MAE
# yelp_cpcUcu_RMSE_8_2 = 0.8 * yelp_cpc_RMSE + 0.2 * yelp_ucu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in yelp_cpcUcu_MAE_8_2.values)
# print 'RMSE\t',' '.join(str(e) for e in yelp_cpcUcu_RMSE_8_2.values)
# # douban_cpcUgu_MAE_8_2.plot(label='0.8*cpc+0.2*ugu')
# # douban_cpcUgu_RMSE_8_2.plot(label='0.8*cpc+0.2*ugu')
#
#
# print '0.9*cpc+0.1*ucu'
# yelp_cpcUcu_MAE_9_1 = 0.1 * yelp_cpc_MAE + 0.9 * yelp_ucu_MAE
# yelp_cpcUcu_RMSE_9_1 = 0.1 * yelp_cpc_RMSE + 0.9 * yelp_ucu_RMSE
# print 'MAE\t\t', ' '.join(str(e) for e in yelp_cpcUcu_MAE_9_1.values)
# print 'RMSE\t',' '.join(str(e) for e in yelp_cpcUcu_RMSE_9_1.values)
# # douban_cpcUgu_MAE_9_1.plot(label='0.9*cpc+0.1*ugu')
# # douban_cpcUgu_RMSE_9_1.plot(label='0.9*cpc+0.1*ugu')