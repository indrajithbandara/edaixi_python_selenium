#-*-coding:utf-8-*- 
#coding=utf-8
from appobjectutils import SingleWebDriver
#class appobjectops:
# class appObjectUtils(self):
#     
class appobjectops:
    
    #operation system testcase01 perminssion manage module appobject
    permloginClickButton="div#container.container h3.text-center.text-primary a.btn.btn-success.text-center"
    clickPermissionLink="div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li.dropdown a.dropdown-toggle"
    clickPermissionButton="div#container.container div.panel.panel-primary div.panle-body table.table.table-striped tbody tr:first-child td:last-child div.btn-toolbar a.btn.btn-sm.btn-success"
    
    clickPositionLink="div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li.dropdown a.dropdown-toggle"
    clickPositionNewButton="div#container.container div#content-container a.btn.btn-info.col-md-1"
    clickPositionEditButton="div#container.container div#content div.panel.panel-primary div.panle-body table.table.table-striped tbody tr:last-child td:last-child a.btn.btn-sm.btn-info"
    clickPositionDeleteButton="div#container.container div#content div.panel.panel-primary div.panle-body table.table.table-striped tbody tr:last-child td:last-child a.btn.btn-sm.btn-danger"
    
    
    
    #operation sysytem testcase08 RechargeReturncrash module app object
    loginClickButton = "div#container.container h3.text-center.text-primary a.btn.btn-success.text-center"
    clickRechargeReturncrashLink= "div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(8)+") a"
    
    clickNewButtonRechargeReturncrash="div#container.container div a.btn.btn-info.btn-info"
    addchizhifanxianResult="div#container.container div.alert.fade.in.alert-success"
    
    clickEditButtonRechargeReturncrash="div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:first-child"
    editchizhifanxianresult="div#container.container div.alert.fade.in.alert-success"
    
    clickDeleteButtonRechargeReturncrash="div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:last-child"
    deletechizhifanxianresult="div#container.container div.alert.fade.in.alert-success"
    
    
    
    #operation sysytem testcase03
    
    #operation sysytem testcase04
    
    #operation sysytem testcase05
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def getWebElementOpsRechargereturncrash(self):
        #SingleWebDriver.getWebDriverInstance().find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(8)+") a").click()
        return SingleWebDriver.getWebDriverInstance(self).find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(8)+") a")