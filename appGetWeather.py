#coding=gbk
# JarvisChu  
#Blog: zhujiangtao.com,blog.csdn.net/jarvischu  
 
import sys,urllib2,appGetWeather_help  




#Locate the city  
city_info = urllib2.urlopen( 'http://pv.sohu.com/cityjson').read()    
city = city_info.split('=')[1].split(';')[0]  #split out the city name'''
city=eval(city)['cname']#str into dict 

print u"���ĳ���:",city
#----------------------------------------------------------------------------  

#convert city name to short
cityName=appGetWeather_help.convertName(city)  

#convert city name to cityID  
cityID=appGetWeather_help.getCityCodeFromName(cityName)  
#print "cityId:",cityID  
#---------------------------------------------------  
 
#get the weather  
msg = appGetWeather_help.getCityWeather_RealTime(cityID)  
print u'����:    ',msg['city']  
print u'����   ',msg['wind']  
print u'ʪ�ȣ�   ',msg['sd']  
print u'����ʱ��:',msg['time']
