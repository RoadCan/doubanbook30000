# -*- coding:utf-8 -*-
import catch
# 抓取各标签列表页
"""
	输入参数为:
	requireip 是否使用代理，默认否
	v 是否限制爬虫速度，默认否，时间为1秒仿人工
	lockprefix 文件加锁后缀
"""
catch.catchbooklist(0,2,'html')
