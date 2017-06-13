#coding:utf8
cityList  = {u'reason': u'\u6210\u529f', u'error_code': 0, u'result': [{u'cityId': u'2', u'cityName': u'\u5b89\u5fbd', u'provinceId': u'2'}, {u'cityId': u'45', u'cityName': u'\u9ec4\u5c71', u'provinceId': u'2'}, {u'cityId': u'42', u'cityName': u'\u5408\u80a5', u'provinceId': u'2'}, {u'cityId': u'51', u'cityName': u'\u5ba3\u57ce', u'provinceId': u'2'}, {u'cityId': u'50', u'cityName': u'\u829c\u6e56', u'provinceId': u'2'}, {u'cityId': u'36', u'cityName': u'\u5b89\u5e86', u'provinceId': u'2'}, {u'cityId': u'46', u'cityName': u'\u516d\u5b89', u'provinceId': u'2'}, {u'cityId': u'39', u'cityName': u'\u6c60\u5dde', u'provinceId': u'2'}, {u'cityId': u'38', u'cityName': u'\u5de2\u6e56', u'provinceId': u'2'}, {u'cityId': u'40', u'cityName': u'\u6ec1\u5dde', u'provinceId': u'2'}, {u'cityId': u'52', u'cityName': u'\u4eb3\u5dde', u'provinceId': u'2'}, {u'cityId': u'47', u'cityName': u'\u9a6c\u978d\u5c71', u'provinceId': u'2'}, {u'cityId': u'48', u'cityName': u'\u5bbf\u5dde', u'provinceId': u'2'}, {u'cityId': u'37', u'cityName': u'\u868c\u57e0', u'provinceId': u'2'}, {u'cityId': u'41', u'cityName': u'\u961c\u9633', u'provinceId': u'2'}, {u'cityId': u'44', u'cityName': u'\u6dee\u5357', u'provinceId': u'2'}, {u'cityId': u'49', u'cityName': u'\u94dc\u9675', u'provinceId': u'2'}, {u'cityId': u'4', u'cityName': u'\u798f\u5efa', u'provinceId': u'4'}, {u'cityId': u'61', u'cityName': u'\u53a6\u95e8', u'provinceId': u'4'}, {u'cityId': u'54', u'cityName': u'\u798f\u5dde', u'provinceId': u'4'}, {u'cityId': u'55', u'cityName': u'\u9f99\u5ca9', u'provinceId': u'4'}, {u'cityId': u'56', u'cityName': u'\u5357\u5e73', u'provinceId': u'4'}, {u'cityId': u'62', u'cityName': u'\u6f33\u5dde', u'provinceId': u'4'}, {u'cityId': u'57', u'cityName': u'\u5b81\u5fb7', u'provinceId': u'4'}, {u'cityId': u'60', u'cityName': u'\u4e09\u660e', u'provinceId': u'4'}, {u'cityId': u'59', u'cityName': u'\u6cc9\u5dde', u'provinceId': u'4'}, {u'cityId': u'58', u'cityName': u'\u8386\u7530', u'provinceId': u'4'}, {u'cityId': u'3', u'cityName': u'\u5317\u4eac', u'provinceId': u'3'}, {u'cityId': u'53', u'cityName': u'\u5317\u4eac', u'provinceId': u'3'}, {u'cityId': u'5', u'cityName': u'\u7518\u8083', u'provinceId': u'5'}, {u'cityId': u'69', u'cityName': u'\u5170\u5dde', u'provinceId': u'5'}, {u'cityId': u'68', u'cityName': u'\u9152\u6cc9', u'provinceId': u'5'}, {u'cityId': u'76', u'cityName': u'\u5f20\u6396', u'provinceId': u'5'}, {u'cityId': u'71', u'cityName': u'\u9647\u5357', u'provinceId': u'5'}, {u'cityId': u'72', u'cityName': u'\u5e73\u51c9', u'provinceId': u'5'}, {u'cityId': u'63', u'cityName': u'\u767d\u94f6', u'provinceId': u'5'}, {u'cityId': u'65', u'cityName': u'\u7518\u5357', u'provinceId': u'5'}, {u'cityId': u'65', u'cityName': u'\u7518\u5357\u85cf\u65cf\u81ea\u6cbb\u5dde', u'provinceId': u'5'}, {u'cityId': u'66', u'cityName': u'\u5609\u5cea\u5173', u'provinceId': u'5'}, {u'cityId': u'73', u'cityName': u'\u5e86\u9633', u'provinceId': u'5'}, {u'cityId': u'74', u'cityName': u'\u5929\u6c34', u'provinceId': u'5'}, {u'cityId': u'75', u'cityName': u'\u6b66\u5a01', u'provinceId': u'5'}, {u'cityId': u'64', u'cityName': u'\u5b9a\u897f', u'provinceId': u'5'}, {u'cityId': u'70', u'cityName': u'\u4e34\u590f', u'provinceId': u'5'}, {u'cityId': u'6', u'cityName': u'\u5e7f\u4e1c', u'provinceId': u'6'}, {u'cityId': u'80', u'cityName': u'\u5e7f\u5dde', u'provinceId': u'6'}, {u'cityId': u'91', u'cityName': u'\u6df1\u5733', u'provinceId': u'6'}, {u'cityId': u'87', u'cityName': u'\u6e05\u8fdc', u'provinceId': u'6'}, {u'cityId': u'82', u'cityName': u'\u60e0\u5dde', u'provinceId': u'6'}, {u'cityId': u'83', u'cityName': u'\u6c5f\u95e8', u'provinceId': u'6'}, {u'cityId': u'97', u'cityName': u'\u73e0\u6d77', u'provinceId': u'6'}, {u'cityId': u'90', u'cityName': u'\u97f6\u5173', u'provinceId': u'6'}, {u'cityId': u'81', u'cityName': u'\u6cb3\u6e90', u'provinceId': u'6'}, {u'cityId': u'78', u'cityName': u'\u4e1c\u839e', u'provinceId': u'6'}, {u'cityId': u'79', u'cityName': u'\u4f5b\u5c71', u'provinceId': u'6'}, {u'cityId': u'95', u'cityName': u'\u8087\u5e86', u'provinceId': u'6'}, {u'cityId': u'96', u'cityName': u'\u4e2d\u5c71', u'provinceId': u'6'}, {u'cityId': u'77', u'cityName': u'\u6f6e\u5dde', u'provinceId': u'6'}, {u'cityId': u'86', u'cityName': u'\u6885\u5dde', u'provinceId': u'6'}, {u'cityId': u'85', u'cityName': u'\u8302\u540d', u'provinceId': u'6'}, {u'cityId': u'88', u'cityName': u'\u6c55\u5934', u'provinceId': u'6'}, {u'cityId': u'84', u'cityName': u'\u63ed\u9633', u'provinceId': u'6'}, {u'cityId': u'94', u'cityName': u'\u6e5b\u6c5f', u'provinceId': u'6'}, {u'cityId': u'92', u'cityName': u'\u9633\u6c5f', u'provinceId': u'6'}, {u'cityId': u'93', u'cityName': u'\u4e91\u6d6e', u'provinceId': u'6'}, {u'cityId': u'89', u'cityName': u'\u6c55\u5c3e', u'provinceId': u'6'}, {u'cityId': u'7', u'cityName': u'\u5e7f\u897f', u'provinceId': u'7'}, {u'cityId': u'102', u'cityName': u'\u6842\u6797', u'provinceId': u'7'}, {u'cityId': u'108', u'cityName': u'\u5357\u5b81', u'provinceId': u'7'}, {u'cityId': u'98', u'cityName': u'\u767e\u8272', u'provinceId': u'7'}, {u'cityId': u'99', u'cityName': u'\u5317\u6d77', u'provinceId': u'7'}, {u'cityId': u'104', u'cityName': u'\u6cb3\u6c60', u'provinceId': u'7'}, {u'cityId': u'105', u'cityName': u'\u8d3a\u5dde', u'provinceId': u'7'}, {u'cityId': u'107', u'cityName': u'\u67f3\u5dde', u'provinceId': u'7'}, {u'cityId': u'100', u'cityName': u'\u5d07\u5de6', u'provinceId': u'7'}, {u'cityId': u'110', u'cityName': u'\u68a7\u5dde', u'provinceId': u'7'}, {u'cityId': u'111', u'cityName': u'\u7389\u6797', u'provinceId': u'7'}, {u'cityId': u'101', u'cityName': u'\u9632\u57ce\u6e2f', u'provinceId': u'7'}, {u'cityId': u'106', u'cityName': u'\u6765\u5bbe', u'provinceId': u'7'}, {u'cityId': u'103', u'cityName': u'\u8d35\u6e2f', u'provinceId': u'7'}, {u'cityId': u'109', u'cityName': u'\u94a6\u5dde', u'provinceId': u'7'}, {u'cityId': u'8', u'cityName': u'\u8d35\u5dde', u'provinceId': u'8'}, {u'cityId': u'114', u'cityName': u'\u8d35\u9633', u'provinceId': u'8'}, {u'cityId': u'117', u'cityName': u'\u9ed4\u5357', u'provinceId': u'8'}, {u'cityId': u'120', u'cityName': u'\u9075\u4e49', u'provinceId': u'8'}, {u'cityId': u'116', u'cityName': u'\u9ed4\u4e1c\u5357', u'provinceId': u'8'}, {u'cityId': u'119', u'cityName': u'\u94dc\u4ec1', u'provinceId': u'8'}, {u'cityId': u'112', u'cityName': u'\u5b89\u987a', u'provinceId': u'8'}, {u'cityId': u'113', u'cityName': u'\u6bd5\u8282', u'provinceId': u'8'}, {u'cityId': u'118', u'cityName': u'\u9ed4\u897f\u5357', u'provinceId': u'8'}, {u'cityId': u'9', u'cityName': u'\u6d77\u5357', u'provinceId': u'9'}, {u'cityId': u'133', u'cityName': u'\u4e09\u4e9a', u'provinceId': u'9'}, {u'cityId': u'135', u'cityName': u'\u4e07\u5b81', u'provinceId': u'9'}, {u'cityId': u'131', u'cityName': u'\u743c\u6d77', u'provinceId': u'9'}, {u'cityId': u'127', u'cityName': u'\u6d77\u53e3', u'provinceId': u'9'}, {u'cityId': u'122', u'cityName': u'\u4fdd\u4ead', u'provinceId': u'9'}, {u'cityId': u'130', u'cityName': u'\u9675\u6c34', u'provinceId': u'9'}, {u'cityId': u'125', u'cityName': u'\u5b9a\u5b89\u53bf', u'provinceId': u'9'}, {u'cityId': u'137', u'cityName': u'\u4e94\u6307\u5c71', u'provinceId': u'9'}, {u'cityId': u'124', u'cityName': u'\u6f84\u8fc8\u53bf', u'provinceId': u'9'}, {u'cityId': u'138', u'cityName': u'\u510b\u5dde', u'provinceId': u'9'}, {u'cityId': u'136', u'cityName': u'\u6587\u660c', u'provinceId': u'9'}, {u'cityId': u'10', u'cityName': u'\u6cb3\u5317', u'provinceId': u'10'}, {u'cityId': u'146', u'cityName': u'\u77f3\u5bb6\u5e84', u'provinceId': u'10'}, {u'cityId': u'139', u'cityName': u'\u4fdd\u5b9a', u'provinceId': u'10'}, {u'cityId': u'142', u'cityName': u'\u90af\u90f8', u'provinceId': u'10'}, {u'cityId': u'147', u'cityName': u'\u5510\u5c71', u'provinceId': u'10'}, {u'cityId': u'148', u'cityName': u'\u90a2\u53f0', u'provinceId': u'10'}, {u'cityId': u'141', u'cityName': u'\u627f\u5fb7', u'provinceId': u'10'}, {u'cityId': u'145', u'cityName': u'\u79e6\u7687\u5c9b', u'provinceId': u'10'}, {u'cityId': u'144', u'cityName': u'\u5eca\u574a', u'provinceId': u'10'}, {u'cityId': u'149', u'cityName': u'\u5f20\u5bb6\u53e3', u'provinceId': u'10'}, {u'cityId': u'140', u'cityName': u'\u6ca7\u5dde', u'provinceId': u'10'}, {u'cityId': u'143', u'cityName': u'\u8861\u6c34', u'provinceId': u'10'}, {u'cityId': u'11', u'cityName': u'\u6cb3\u5357', u'provinceId': u'11'}, {u'cityId': u'163', u'cityName': u'\u90d1\u5dde', u'provinceId': u'11'}, {u'cityId': u'155', u'cityName': u'\u6d1b\u9633', u'provinceId': u'11'}, {u'cityId': u'157', u'cityName': u'\u5e73\u9876\u5c71', u'provinceId': u'11'}, {u'cityId': u'156', u'cityName': u'\u5357\u9633', u'provinceId': u'11'}, {u'cityId': u'150', u'cityName': u'\u5b89\u9633', u'provinceId': u'11'}, {u'cityId': u'160', u'cityName': u'\u65b0\u4e61', u'provinceId': u'11'}, {u'cityId': u'153', u'cityName': u'\u7126\u4f5c', u'provinceId': u'11'}, {u'cityId': u'158', u'cityName': u'\u4e09\u95e8\u5ce1', u'provinceId': u'11'}, {u'cityId': u'161', u'cityName': u'\u4fe1\u9633', u'provinceId': u'11'}, {u'cityId': u'154', u'cityName': u'\u5f00\u5c01', u'provinceId': u'11'}, {u'cityId': u'152', u'cityName': u'\u6d4e\u6e90', u'provinceId': u'11'}, {u'cityId': u'162', u'cityName': u'\u8bb8\u660c', u'provinceId': u'11'}, {u'cityId': u'164', u'cityName': u'\u5468\u53e3', u'provinceId': u'11'}, {u'cityId': u'159', u'cityName': u'\u5546\u4e18', u'provinceId': u'11'}, {u'cityId': u'166', u'cityName': u'\u6f2f\u6cb3', u'provinceId': u'11'}, {u'cityId': u'151', u'cityName': u'\u9e64\u58c1', u'provinceId': u'11'}, {u'cityId': u'165', u'cityName': u'\u9a7b\u9a6c\u5e97', u'provinceId': u'11'}, {u'cityId': u'167', u'cityName': u'\u6fee\u9633', u'provinceId': u'11'}, {u'cityId': u'13', u'cityName': u'\u6e56\u5317', u'provinceId': u'13'}, {u'cityId': u'192', u'cityName': u'\u6b66\u6c49', u'provinceId': u'13'}, {u'cityId': u'197', u'cityName': u'\u5b9c\u660c', u'provinceId': u'13'}, {u'cityId': u'194', u'cityName': u'\u54b8\u5b81', u'provinceId': u'13'}, {u'cityId': u'195', u'cityName': u'\u8944\u9633', u'provinceId': u'13'}, {u'cityId': u'182', u'cityName': u'\u6069\u65bd', u'provinceId': u'13'}, {u'cityId': u'189', u'cityName': u'\u5341\u5830', u'provinceId': u'13'}, {u'cityId': u'183', u'cityName': u'\u9ec4\u5188', u'provinceId': u'13'}, {u'cityId': u'186', u'cityName': u'\u8346\u5dde', u'provinceId': u'13'}, {u'cityId': u'185', u'cityName': u'\u8346\u95e8', u'provinceId': u'13'}, {u'cityId': u'188', u'cityName': u'\u795e\u519c\u67b6\u6797\u533a', u'provinceId': u'13'}, {u'cityId': u'196', u'cityName': u'\u5b5d\u611f', u'provinceId': u'13'}, {u'cityId': u'184', u'cityName': u'\u9ec4\u77f3', u'provinceId': u'13'}, {u'cityId': u'190', u'cityName': u'\u968f\u5dde', u'provinceId': u'13'}, {u'cityId': u'181', u'cityName': u'\u9102\u5dde', u'provinceId': u'13'}, {u'cityId': u'193', u'cityName': u'\u4ed9\u6843', u'provinceId': u'13'}, {u'cityId': u'14', u'cityName': u'\u6e56\u5357', u'provinceId': u'14'}, {u'cityId': u'199', u'cityName': u'\u957f\u6c99', u'provinceId': u'14'}, {u'cityId': u'210', u'cityName': u'\u5f20\u5bb6\u754c', u'provinceId': u'14'}, {u'cityId': u'200', u'cityName': u'\u90f4\u5dde', u'provinceId': u'14'}, {u'cityId': u'211', u'cityName': u'\u682a\u6d32', u'provinceId': u'14'}, {u'cityId': u'206', u'cityName': u'\u6e58\u897f', u'provinceId': u'14'}, {u'cityId': u'202', u'cityName': u'\u6000\u5316', u'provinceId': u'14'}, {u'cityId': u'209', u'cityName': u'\u5cb3\u9633', u'provinceId': u'14'}, {u'cityId': u'208', u'cityName': u'\u6c38\u5dde', u'provinceId': u'14'}, {u'cityId': u'205', u'cityName': u'\u6e58\u6f6d', u'provinceId': u'14'}, {u'cityId': u'201', u'cityName': u'\u8861\u9633', u'provinceId': u'14'}, {u'cityId': u'203', u'cityName': u'\u5a04\u5e95', u'provinceId': u'14'}, {u'cityId': u'198', u'cityName': u'\u5e38\u5fb7', u'provinceId': u'14'}, {u'cityId': u'207', u'cityName': u'\u76ca\u9633', u'provinceId': u'14'}, {u'cityId': u'204', u'cityName': u'\u90b5\u9633', u'provinceId': u'14'}, {u'cityId': u'206', u'cityName': u'\u6e58\u897f\u571f\u5bb6\u65cf\u82d7\u65cf\u81ea\u6cbb\u5dde', u'provinceId': u'14'}, {u'cityId': u'15', u'cityName': u'\u5409\u6797', u'provinceId': u'15'}, {u'cityId': u'214', u'cityName': u'\u957f\u6625', u'provinceId': u'15'}, {u'cityId': u'215', u'cityName': u'\u5409\u6797', u'provinceId': u'15'}, {u'cityId': u'4569', u'cityName': u'\u957f\u767d\u5c71', u'provinceId': u'15'}, {u'cityId': u'213', u'cityName': u'\u767d\u5c71', u'provinceId': u'15'}, {u'cityId': u'220', u'cityName': u'\u5ef6\u8fb9', u'provinceId': u'15'}, {u'cityId': u'220', u'cityName': u'\u5ef6\u8fb9\u671d\u9c9c\u65cf\u81ea\u6cbb\u5dde', u'provinceId': u'15'}, {u'cityId': u'217', u'cityName': u'\u56db\u5e73', u'provinceId': u'15'}, {u'cityId': u'219', u'cityName': u'\u901a\u5316', u'provinceId': u'15'}, {u'cityId': u'16', u'cityName': u'\u6c5f\u82cf', u'provinceId': u'16'}, {u'cityId': u'226', u'cityName': u'\u82cf\u5dde', u'provinceId': u'16'}, {u'cityId': u'224', u'cityName': u'\u5357\u4eac', u'provinceId': u'16'}, {u'cityId': u'229', u'cityName': u'\u65e0\u9521', u'provinceId': u'16'}, {u'cityId': u'221', u'cityName': u'\u5e38\u5dde', u'provinceId': u'16'}, {u'cityId': u'232', u'cityName': u'\u626c\u5dde', u'provinceId': u'16'}, {u'cityId': u'233', u'cityName': u'\u9547\u6c5f', u'provinceId': u'16'}, {u'cityId': u'225', u'cityName': u'\u5357\u901a', u'provinceId': u'16'}, {u'cityId': u'230', u'cityName': u'\u5f90\u5dde', u'provinceId': u'16'}, {u'cityId': u'228', u'cityName': u'\u6cf0\u5dde', u'provinceId': u'16'}, {u'cityId': u'231', u'cityName': u'\u76d0\u57ce', u'provinceId': u'16'}, {u'cityId': u'227', u'cityName': u'\u5bbf\u8fc1', u'provinceId': u'16'}, {u'cityId': u'222', u'cityName': u'\u6dee\u5b89', u'provinceId': u'16'}, {u'cityId': u'223', u'cityName': u'\u8fde\u4e91\u6e2f', u'provinceId': u'16'}, {u'cityId': u'17', u'cityName': u'\u6c5f\u897f', u'provinceId': u'17'}, {u'cityId': u'238', u'cityName': u'\u4e5d\u6c5f', u'provinceId': u'17'}, {u'cityId': u'239', u'cityName': u'\u5357\u660c', u'provinceId': u'17'}, {u'cityId': u'241', u'cityName': u'\u4e0a\u9976', u'provinceId': u'17'}, {u'cityId': u'235', u'cityName': u'\u8d63\u5dde', u'provinceId': u'17'}, {u'cityId': u'243', u'cityName': u'\u5b9c\u6625', u'provinceId': u'17'}, {u'cityId': u'237', u'cityName': u'\u666f\u5fb7\u9547', u'provinceId': u'17'}, {u'cityId': u'236', u'cityName': u'\u5409\u5b89', u'provinceId': u'17'}, {u'cityId': u'240', u'cityName': u'\u840d\u4e61', u'provinceId': u'17'}, {u'cityId': u'234', u'cityName': u'\u629a\u5dde', u'provinceId': u'17'}, {u'cityId': u'242', u'cityName': u'\u65b0\u4f59', u'provinceId': u'17'}, {u'cityId': u'244', u'cityName': u'\u9e70\u6f6d', u'provinceId': u'17'}, {u'cityId': u'18', u'cityName': u'\u8fbd\u5b81', u'provinceId': u'18'}, {u'cityId': u'248', u'cityName': u'\u5927\u8fde', u'provinceId': u'18'}, {u'cityId': u'256', u'cityName': u'\u6c88\u9633', u'provinceId': u'18'}, {u'cityId': u'258', u'cityName': u'\u8425\u53e3', u'provinceId': u'18'}, {u'cityId': u'253', u'cityName': u'\u9526\u5dde', u'provinceId': u'18'}, {u'cityId': u'250', u'cityName': u'\u629a\u987a', u'provinceId': u'18'}, {u'cityId': u'249', u'cityName': u'\u4e39\u4e1c', u'provinceId': u'18'}, {u'cityId': u'245', u'cityName': u'\u978d\u5c71', u'provinceId': u'18'}, {u'cityId': u'246', u'cityName': u'\u672c\u6eaa', u'provinceId': u'18'}, {u'cityId': u'254', u'cityName': u'\u8fbd\u9633', u'provinceId': u'18'}, {u'cityId': u'255', u'cityName': u'\u76d8\u9526', u'provinceId': u'18'}, {u'cityId': u'247', u'cityName': u'\u671d\u9633', u'provinceId': u'18'}, {u'cityId': u'251', u'cityName': u'\u961c\u65b0', u'provinceId': u'18'}, {u'cityId': u'257', u'cityName': u'\u94c1\u5cad', u'provinceId': u'18'}, {u'cityId': u'252', u'cityName': u'\u846b\u82a6\u5c9b', u'provinceId': u'18'}, {u'cityId': u'20', u'cityName': u'\u5b81\u590f', u'provinceId': u'20'}, {u'cityId': u'274', u'cityName': u'\u94f6\u5ddd', u'provinceId': u'20'}, {u'cityId': u'3105', u'cityName': u'\u4e2d\u536b', u'provinceId': u'20'}, {u'cityId': u'271', u'cityName': u'\u56fa\u539f', u'provinceId': u'20'}, {u'cityId': u'272', u'cityName': u'\u77f3\u5634\u5c71', u'provinceId': u'20'}, {u'cityId': u'273', u'cityName': u'\u5434\u5fe0', u'provinceId': u'20'}, {u'cityId': u'21', u'cityName': u'\u9752\u6d77', u'provinceId': u'21'}, {u'cityId': u'281', u'cityName': u'\u897f\u5b81', u'provinceId': u'21'}, {u'cityId': u'276', u'cityName': u'\u6d77\u5317', u'provinceId': u'21'}, {u'cityId': u'278', u'cityName': u'\u6d77\u5357\u85cf\u65cf', u'provinceId': u'21'}, {u'cityId': u'22', u'cityName': u'\u5c71\u4e1c', u'provinceId': u'22'}, {u'cityId': u'292', u'cityName': u'\u9752\u5c9b', u'provinceId': u'22'}, {u'cityId': u'287', u'cityName': u'\u6d4e\u5357', u'provinceId': u'22'}, {u'cityId': u'297', u'cityName': u'\u70df\u53f0', u'provinceId': u'22'}, {u'cityId': u'291', u'cityName': u'\u4e34\u6c82', u'provinceId': u'22'}, {u'cityId': u'295', u'cityName': u'\u5a01\u6d77', u'provinceId': u'22'}, {u'cityId': u'294', u'cityName': u'\u6cf0\u5b89', u'provinceId': u'22'}, {u'cityId': u'299', u'cityName': u'\u6dc4\u535a', u'provinceId': u'22'}, {u'cityId': u'296', u'cityName': u'\u6f4d\u574a', u'provinceId': u'22'}, {u'cityId': u'288', u'cityName': u'\u6d4e\u5b81', u'provinceId': u'22'}, {u'cityId': u'293', u'cityName': u'\u65e5\u7167', u'provinceId': u'22'}, {u'cityId': u'298', u'cityName': u'\u67a3\u5e84', u'provinceId': u'22'}, {u'cityId': u'290', u'cityName': u'\u804a\u57ce', u'provinceId': u'22'}, {u'cityId': u'283', u'cityName': u'\u6ee8\u5dde', u'provinceId': u'22'}, {u'cityId': u'284', u'cityName': u'\u5fb7\u5dde', u'provinceId': u'22'}, {u'cityId': u'289', u'cityName': u'\u83b1\u829c', u'provinceId': u'22'}, {u'cityId': u'286', u'cityName': u'\u83cf\u6cfd', u'provinceId': u'22'}, {u'cityId': u'285', u'cityName': u'\u4e1c\u8425', u'provinceId': u'22'}, {u'cityId': u'23', u'cityName': u'\u5c71\u897f', u'provinceId': u'23'}, {u'cityId': u'310', u'cityName': u'\u8fd0\u57ce', u'provinceId': u'23'}, {u'cityId': u'303', u'cityName': u'\u664b\u4e2d', u'provinceId': u'23'}, {u'cityId': u'304', u'cityName': u'\u4e34\u6c7e', u'provinceId': u'23'}, {u'cityId': u'307', u'cityName': u'\u592a\u539f', u'provinceId': u'23'}, {u'cityId': u'302', u'cityName': u'\u664b\u57ce', u'provinceId': u'23'}, {u'cityId': u'301', u'cityName': u'\u5927\u540c', u'provinceId': u'23'}, {u'cityId': u'300', u'cityName': u'\u957f\u6cbb', u'provinceId': u'23'}, {u'cityId': u'308', u'cityName': u'\u5ffb\u5dde', u'provinceId': u'23'}, {u'cityId': u'309', u'cityName': u'\u9633\u6cc9', u'provinceId': u'23'}, {u'cityId': u'305', u'cityName': u'\u5415\u6881', u'provinceId': u'23'}, {u'cityId': u'306', u'cityName': u'\u6714\u5dde', u'provinceId': u'23'}, {u'cityId': u'24', u'cityName': u'\u9655\u897f', u'provinceId': u'24'}, {u'cityId': u'317', u'cityName': u'\u897f\u5b89', u'provinceId': u'24'}, {u'cityId': u'316', u'cityName': u'\u6e2d\u5357', u'provinceId': u'24'}, {u'cityId': u'312', u'cityName': u'\u5b9d\u9e21', u'provinceId': u'24'}, {u'cityId': u'314', u'cityName': u'\u5546\u6d1b', u'provinceId': u'24'}, {u'cityId': u'313', u'cityName': u'\u6c49\u4e2d', u'provinceId': u'24'}, {u'cityId': u'318', u'cityName': u'\u54b8\u9633', u'provinceId': u'24'}, {u'cityId': u'319', u'cityName': u'\u5ef6\u5b89', u'provinceId': u'24'}, {u'cityId': u'311', u'cityName': u'\u5b89\u5eb7', u'provinceId': u'24'}, {u'cityId': u'315', u'cityName': u'\u94dc\u5ddd', u'provinceId': u'24'}, {u'cityId': u'27', u'cityName': u'\u5929\u6d25', u'provinceId': u'27'}, {u'cityId': u'343', u'cityName': u'\u5929\u6d25', u'provinceId': u'27'}, {u'cityId': u'26', u'cityName': u'\u56db\u5ddd', u'provinceId': u'26'}, {u'cityId': u'324', u'cityName': u'\u6210\u90fd', u'provinceId': u'26'}, {u'cityId': u'333', u'cityName': u'\u7ef5\u9633', u'provinceId': u'26'}, {u'cityId': u'330', u'cityName': u'\u4e50\u5c71', u'provinceId': u'26'}, {u'cityId': u'329', u'cityName': u'\u5e7f\u5143', u'provinceId': u'26'}, {u'cityId': u'322', u'cityName': u'\u963f\u575d', u'provinceId': u'26'}, {u'cityId': u'331', u'cityName': u'\u51c9\u5c71', u'provinceId': u'26'}, {u'cityId': u'332', u'cityName': u'\u7709\u5c71', u'provinceId': u'26'}, {u'cityId': u'334', u'cityName': u'\u5357\u5145', u'provinceId': u'26'}, {u'cityId': u'323', u'cityName': u'\u5df4\u4e2d', u'provinceId': u'26'}, {u'cityId': u'327', u'cityName': u'\u7518\u5b5c', u'provinceId': u'26'}, {u'cityId': u'338', u'cityName': u'\u96c5\u5b89', u'provinceId': u'26'}, {u'cityId': u'339', u'cityName': u'\u5b9c\u5bbe', u'provinceId': u'26'}, {u'cityId': u'337', u'cityName': u'\u9042\u5b81', u'provinceId': u'26'}, {u'cityId': u'326', u'cityName': u'\u5fb7\u9633', u'provinceId': u'26'}, {u'cityId': u'328', u'cityName': u'\u5e7f\u5b89', u'provinceId': u'26'}, {u'cityId': u'341', u'cityName': u'\u81ea\u8d21', u'provinceId': u'26'}, {u'cityId': u'336', u'cityName': u'\u6500\u679d\u82b1', u'provinceId': u'26'}, {u'cityId': u'342', u'cityName': u'\u6cf8\u5dde', u'provinceId': u'26'}, {u'cityId': u'325', u'cityName': u'\u8fbe\u5dde', u'provinceId': u'26'}, {u'cityId': u'335', u'cityName': u'\u5185\u6c5f', u'provinceId': u'26'}, {u'cityId': u'331', u'cityName': u'\u51c9\u5c71\u5f5d\u65cf\u81ea\u6cbb\u5dde', u'provinceId': u'26'}, {u'cityId': u'322', u'cityName': u'\u963f\u575d\u85cf\u65cf\u7f8c\u65cf\u81ea\u6cbb\u5dde', u'provinceId': u'26'}, {u'cityId': u'327', u'cityName': u'\u7518\u5b5c\u85cf\u65cf\u81ea\u6cbb\u5dde', u'provinceId': u'26'}, {u'cityId': u'29', u'cityName': u'\u65b0\u7586', u'provinceId': u'29'}, {u'cityId': u'364', u'cityName': u'\u4e4c\u9c81\u6728\u9f50', u'provinceId': u'29'}, {u'cityId': u'366', u'cityName': u'\u4f0a\u7281', u'provinceId': u'29'}, {u'cityId': u'366', u'cityName': u'\u4f0a\u7281\u54c8\u8428\u514b\u81ea\u6cbb\u5dde', u'provinceId': u'29'}, {u'cityId': u'356', u'cityName': u'\u54c8\u5bc6', u'provinceId': u'29'}, {u'cityId': u'351', u'cityName': u'\u963f\u514b\u82cf', u'provinceId': u'29'}, {u'cityId': u'361', u'cityName': u'\u77f3\u6cb3\u5b50', u'provinceId': u'29'}, {u'cityId': u'355', u'cityName': u'\u660c\u5409', u'provinceId': u'29'}, {u'cityId': u'355', u'cityName': u'\u660c\u5409\u56de\u65cf\u81ea\u6cbb\u5dde', u'provinceId': u'29'}, {u'cityId': u'352', u'cityName': u'\u963f\u62c9\u5c14', u'provinceId': u'29'}, {u'cityId': u'353', u'cityName': u'\u5df4\u97f3\u90ed\u695e\u8499\u53e4\u81ea\u6cbb\u5dde', u'provinceId': u'29'}, {u'cityId': u'358', u'cityName': u'\u5580\u4ec0', u'provinceId': u'29'}, {u'cityId': u'359', u'cityName': u'\u514b\u62c9\u739b\u4f9d', u'provinceId': u'29'}, {u'cityId': u'28', u'cityName': u'\u897f\u85cf', u'provinceId': u'28'}, {u'cityId': u'346', u'cityName': u'\u62c9\u8428', u'provinceId': u'28'}, {u'cityId': u'25', u'cityName': u'\u4e0a\u6d77', u'provinceId': u'25'}, {u'cityId': u'321', u'cityName': u'\u4e0a\u6d77', u'provinceId': u'25'}, {u'cityId': u'30', u'cityName': u'\u4e91\u5357', u'provinceId': u'30'}, {u'cityId': u'373', u'cityName': u'\u6606\u660e', u'provinceId': u'30'}, {u'cityId': u'374', u'cityName': u'\u4e3d\u6c5f', u'provinceId': u'30'}, {u'cityId': u'369', u'cityName': u'\u5927\u7406', u'provinceId': u'30'}, {u'cityId': u'380', u'cityName': u'\u897f\u53cc\u7248\u7eb3', u'provinceId': u'30'}, {u'cityId': u'367', u'cityName': u'\u4fdd\u5c71', u'provinceId': u'30'}, {u'cityId': u'371', u'cityName': u'\u8fea\u5e86', u'provinceId': u'30'}, {u'cityId': u'372', u'cityName': u'\u7ea2\u6cb3', u'provinceId': u'30'}, {u'cityId': u'377', u'cityName': u'\u66f2\u9756', u'provinceId': u'30'}, {u'cityId': u'381', u'cityName': u'\u7389\u6eaa', u'provinceId': u'30'}, {u'cityId': u'382', u'cityName': u'\u662d\u901a', u'provinceId': u'30'}, {u'cityId': u'368', u'cityName': u'\u695a\u96c4', u'provinceId': u'30'}, {u'cityId': u'372', u'cityName': u'\u7ea2\u6cb3\u54c8\u5c3c\u65cf\u5f5d\u65cf\u81ea\u6cbb\u5dde', u'provinceId': u'30'}, {u'cityId': u'378', u'cityName': u'\u666e\u6d31', u'provinceId': u'30'}, {u'cityId': u'370', u'cityName': u'\u5fb7\u5b8f', u'provinceId': u'30'}, {u'cityId': u'370', u'cityName': u'\u5fb7\u5b8f\u50a3\u65cf\u666f\u9887\u65cf\u81ea\u6cbb\u5dde', u'provinceId': u'30'}, {u'cityId': u'368', u'cityName': u'\u695a\u96c4\u5f5d\u65cf\u81ea\u6cbb\u5dde', u'provinceId': u'30'}, {u'cityId': u'379', u'cityName': u'\u6587\u5c71', u'provinceId': u'30'}, {u'cityId': u'31', u'cityName': u'\u6d59\u6c5f', u'provinceId': u'31'}, {u'cityId': u'383', u'cityName': u'\u676d\u5dde', u'provinceId': u'31'}, {u'cityId': u'388', u'cityName': u'\u5b81\u6ce2', u'provinceId': u'31'}, {u'cityId': u'385', u'cityName': u'\u5609\u5174', u'provinceId': u'31'}, {u'cityId': u'386', u'cityName': u'\u91d1\u534e', u'provinceId': u'31'}, {u'cityId': u'384', u'cityName': u'\u6e56\u5dde', u'provinceId': u'31'}, {u'cityId': u'390', u'cityName': u'\u53f0\u5dde', u'provinceId': u'31'}, {u'cityId': u'389', u'cityName': u'\u7ecd\u5174', u'provinceId': u'31'}, {u'cityId': u'391', u'cityName': u'\u6e29\u5dde', u'provinceId': u'31'}, {u'cityId': u'387', u'cityName': u'\u4e3d\u6c34', u'provinceId': u'31'}, {u'cityId': u'392', u'cityName': u'\u821f\u5c71', u'provinceId': u'31'}, {u'cityId': u'393', u'cityName': u'\u8862\u5dde', u'provinceId': u'31'}, {u'cityId': u'33', u'cityName': u'\u9999\u6e2f', u'provinceId': u'33'}, {u'cityId': u'395', u'cityName': u'\u9999\u6e2f', u'provinceId': u'33'}, {u'cityId': u'0', u'cityName': u'', u'provinceId': u'33'}, {u'cityId': u'32', u'cityName': u'\u91cd\u5e86', u'provinceId': u'32'}, {u'cityId': u'394', u'cityName': u'\u91cd\u5e86', u'provinceId': u'32'}, {u'cityId': u'12', u'cityName': u'\u9ed1\u9f99\u6c5f', u'provinceId': u'12'}, {u'cityId': u'170', u'cityName': u'\u54c8\u5c14\u6ee8', u'provinceId': u'12'}, {u'cityId': u'168', u'cityName': u'\u5927\u5e86', u'provinceId': u'12'}, {u'cityId': u'180', u'cityName': u'\u4f0a\u6625', u'provinceId': u'12'}, {u'cityId': u'172', u'cityName': u'\u9ed1\u6cb3', u'provinceId': u'12'}, {u'cityId': u'177', u'cityName': u'\u9f50\u9f50\u54c8\u5c14', u'provinceId': u'12'}, {u'cityId': u'175', u'cityName': u'\u7261\u4e39\u6c5f', u'provinceId': u'12'}, {u'cityId': u'174', u'cityName': u'\u4f73\u6728\u65af', u'provinceId': u'12'}, {u'cityId': u'173', u'cityName': u'\u9e21\u897f', u'provinceId': u'12'}, {u'cityId': u'19', u'cityName': u'\u5185\u8499\u53e4', u'provinceId': u'19'}, {u'cityId': u'264', u'cityName': u'\u547c\u548c\u6d69\u7279', u'provinceId': u'19'}, {u'cityId': u'263', u'cityName': u'\u9102\u5c14\u591a\u65af', u'provinceId': u'19'}, {u'cityId': u'262', u'cityName': u'\u8d64\u5cf0', u'provinceId': u'19'}, {u'cityId': u'265', u'cityName': u'\u547c\u4f26\u8d1d\u5c14', u'provinceId': u'19'}, {u'cityId': u'270', u'cityName': u'\u5174\u5b89\u76df', u'provinceId': u'19'}, {u'cityId': u'261', u'cityName': u'\u5305\u5934', u'provinceId': u'19'}, {u'cityId': u'259', u'cityName': u'\u963f\u62c9\u5584\u76df', u'provinceId': u'19'}, {u'cityId': u'266', u'cityName': u'\u901a\u8fbd', u'provinceId': u'19'}, {u'cityId': u'268', u'cityName': u'\u4e4c\u5170\u5bdf\u5e03\u5e02', u'provinceId': u'19'}, {u'cityId': u'34', u'cityName': u'\u6fb3\u95e8', u'provinceId': u'34'}, {u'cityId': u'396', u'cityName': u'\u6fb3\u95e8', u'provinceId': u'34'}, {u'cityId': u'0', u'cityName': u'', u'provinceId': u'34'}, {u'cityId': u'35', u'cityName': u'\u53f0\u6e7e', u'provinceId': u'35'}, {u'cityId': u'401', u'cityName': u'\u53f0\u5317', u'provinceId': u'35'}, {u'cityId': u'5119', u'cityName': u'\u5357\u6295', u'provinceId': u'35'}, {u'cityId': u'398', u'cityName': u'\u82b1\u83b2', u'provinceId': u'35'}, {u'cityId': u'404', u'cityName': u'\u53f0\u4e2d', u'provinceId': u'35'}, {u'cityId': u'6571', u'cityName': u'\u65b0\u5317', u'provinceId': u'35'}, {u'cityId': u'397', u'cityName': u'\u9ad8\u96c4', u'provinceId': u'35'}, {u'cityId': u'402', u'cityName': u'\u53f0\u4e1c', u'provinceId': u'35'}, {u'cityId': u'5114', u'cityName': u'\u65b0\u7af9', u'provinceId': u'35'}, {u'cityId': u'5118', u'cityName': u'\u5f70\u5316', u'provinceId': u'35'}, {u'cityId': u'399', u'cityName': u'\u57fa\u9686', u'provinceId': u'35'}, {u'cityId': u'5117', u'cityName': u'\u82d7\u6817', u'provinceId': u'35'}, {u'cityId': u'5121', u'cityName': u'\u5c4f\u4e1c', u'provinceId': u'35'}]}
import requests
import json
from numpy import *
from Tkinter import *
import tkMessageBox

def cityName(city_name):
    for i in range(shape(cityList['result'])[0]):
        if  cityList['result'][i]['cityName'].encode("utf-8") == city_name:
            return cityList['result'][i]['cityId']


def tripRecom(city_name):
    cityId = cityName(city_name)
    url = "http://apis.haoservice.com/lifeservice/travel/scenery?pid=0&cid=%s&page=1&key=760f02c0930b4c9a9b45460c5ed453a6" % cityId
    response = requests.request("GET", url)
    viewpoint_name =  response.json()
    #viewpoint_name = tripName ={u'reason': u'\u6210\u529f', u'error_code': 0, u'result': [{u'cityId': u'133', u'title': u'\u4e9a\u9f99\u6e7e\u70ed\u5e26\u5929\u5802\u68ee\u6797\u516c\u56ed\uff08\u975e\u8bda\u52ff\u6270\u2161\u62cd\u6444\u5730\uff09', u'grade': u'AAAA', u'sid': u'26358', u'price_min': u'80', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_26358.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u4e9a\u9f99\u6e7e\u56fd\u5bb6\u65c5\u6e38\u5ea6\u5047\u533a\u5185', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/05/17/PxL6ZO_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u8708\u652f\u6d32\u5c9b', u'grade': u'AAAAA', u'sid': u'8078', u'price_min': u'60', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_8078.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u6797\u65fa\u9547\u6d77\u68e0\u6e7e\u8708\u652f\u6d32\u5c9b\u5ea6\u5047\u4e2d\u5fc3', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/07/18/dI7lpU_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u9e7f\u56de\u5934\u98ce\u666f\u533a', u'grade': u'AAA', u'sid': u'9724', u'price_min': u'32', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_9724.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u9e7f\u5cad\u8def\u9e7f\u56de\u5934\u516c\u56ed', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/08/17/ddXZ8m_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u5929\u6daf\u6d77\u89d2', u'grade': u'AAAA', u'sid': u'1370', u'price_min': u'60', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_1370.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u5929\u6daf\u9547\u9a6c\u5cad\u5c71\u9e93\u5929\u6daf\u6d77\u89d2\u6e38\u89c8\u533a\u5185', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/07/09/7hemXP_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u4e09\u4e9a\u5927\u5c0f\u6d1e\u5929', u'grade': u'AAAAA', u'sid': u'6651', u'price_min': u'116', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_6651.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u5d16\u57ce\u5927\u5c0f\u6d1e\u5929\u65c5\u6e38\u533a', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/08/19/HStAFU_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u73e0\u6c5f\u5357\u7530\u6e29\u6cc9', u'grade': u'', u'sid': u'9739', u'price_min': u'150', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_9739.html', u'address': u'\u6d77\u5357\u4e09\u4e9a\u6d77\u68e0\u6e7e\u5357\u7530\u65c5\u6e38\u57ce\u5185', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/11/02/16/1J0a9T_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u5357\u5c71\u5bfa', u'grade': u'AAAAA', u'sid': u'9738', u'price_min': u'138', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_9738.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u5d16\u57ce\u9547\u5357\u5c71\u6587\u5316\u65c5\u6e38\u533a\u5185', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/06/17/M2UcTE_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u4e09\u4e9a\u5947\u5e7b\u827a\u672f\u4f53\u9a8c\u9986', u'grade': u'', u'sid': u'28723', u'price_min': u'68', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_28723.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u91d1\u9e21\u5cad\u6021\u548c\u8c6a\u5ead1-2\u5c42\uff08\u65b0\u4e00\u4e2d\u5bf9\u9762\uff09', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/12/14/lzbWUf_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u5440\u8bfa\u8fbe\u96e8\u6797\uff08hold\u4f4f\u7231\u62cd\u6444\u5730\uff09', u'grade': u'AAAAA', u'sid': u'21294', u'price_min': u'138', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_21294.html', u'address': u'\u6d77\u5357\u7701\u4fdd\u4ead\u53bf\u56fd\u8425\u4e09\u9053\u519c\u573a\u5440\u8bfa\u8fbe\u96e8\u6797\u666f\u533a', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/05/19/qFmw1C_240x135_00.jpg'}, {u'cityId': u'133', u'title': u'\u897f\u5c9b\u6d77\u6d0b\u6587\u5316\u65c5\u6e38\u533a', u'grade': u'AAAA', u'sid': u'9750', u'price_min': u'118', u'comm_cnt': None, u'url': u'http://www.ly.com/scenery/BookSceneryTicket_9750.html', u'address': u'\u6d77\u5357\u7701\u4e09\u4e9a\u5e02\u4e09\u4e9a\u6e7e\u8def\u8096\u65d7\u6e2f\u7801\u5934', u'imgurl': u'http://pic4.40017.cn/scenery/destination/2016/09/12/11/FYDc4B_240x135_00.jpg'}]}


    print viewpoint_name
    for i in range(shape(viewpoint_name['result'])[0]):
        print viewpoint_name['result'][i]['title']
    return viewpoint_name

