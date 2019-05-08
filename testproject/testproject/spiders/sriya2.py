# -*- coding: utf-8 -*-
import scrapy
from loginform import fill_login_form
import logging

logging.basicConfig(level=logging.DEBUG, filename='sriya2.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
class QuotesSpider(scrapy.Spider):
    name = 'sriya2'
    allowed_domains = ['119.46.164.56']
    start_urls = ['http://119.46.164.56:8082/WebFront/Home/Login.aspx']
    login_url= 'http://119.46.164.56:8082/WebFront/Home/Login.aspx'
    login_user='hx001'
    login_password='12345'

    def parse(self,response):
        return scrapy.Request(
            url=self.login_url,
            callback=self.login,
            )

    def login(self,response):
        logindata={
            "__VIEWSTATEGENERATOR":response.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value').extract_first(),
            "__VIEWSTATE":response.xpath('//*[@id="__VIEWSTATE"]/@value').extract_first(),
            "__EVENTTARGET":"cBtnLogin",
            "__EVENTVALIDATION":response.xpath('//*[@id="__EVENTVALIDATION"]/@value').extract_first(),
            "cTxUserName":"hx001",
            "cTxPassword":"12345",
            "__EVENTARGUMENT":"",
            "cHdComputerName":"",
            "cHdComputerIP":"124.120.89.132",
            "cHdIsUpdateComDetComplete":"false"
}

        return scrapy.FormRequest.from_response(
                                response,
                                formdata=logindata,
                                callback=self.after_login)

    def after_login(self, response):
        # check login succeed before going on
        if b"authentication failed" in response.body:
            self.logger.error("Login failed")
            logging.error(f'login failed URL response is {response.url}')
            return
        else:
            logging.debug(f'logged in responded with {response.url}')
        return scrapy.Request(
            url="http://119.46.164.56:8082/WebFront/Stocks/StockProduct_Man.aspx",
            callback=self.fillinventoryform)
    def fillinventoryform(self, response):
        logging.debug(f'filling inventory form at {response.url}')
        with open('sriya2_before_filling_form.html','w') as f:
            f.write(response.text)
            logging.debug('sriya2_before_filling_form.html is written')
        logindata={
            "__VIEWSTATEGENERATOR":response.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value').extract_first(),
            "__VIEWSTATE":response.xpath('//*[@id="__VIEWSTATE"]/@value').extract_first(),
            "__EVENTTARGET":"",
            "__EVENTVALIDATION":response.xpath('//*[@id="__EVENTVALIDATION"]/@value').extract_first(),
            "__EVENTARGUMENT":"",
            "ctl00$Page_Header1$cHdCompany_Title1": "บริษัท ศิริยาฟาร์มา (2) จำกัด",
            "ctl00$Page_Header1$cHdCompany_Title2": "หน้าร้าน",
            "ctl00$Page_Header1$cHdLogin_FullName": "Health Express",
            "ctl00$MainContent$cChkProductAdd": "on",
            "ctl00$MainContent$cChkProductSearch": "on",
            "ctl00$MainContent$cRdFindType": "1",
            "ctl00$MainContent$cHdPickList_ProductGroup": "1",
            "ctl00$MainContent$cHdPickList_ProductType": "2",
            "ctl00$MainContent$cHdPickList_ProductGenericName": "5",
            "ctl00$MainContent$cDdItemPerPage": "5000",
            "ctl00$MainContent$cBtnFind": "ค้นหา",
            "ctl00$MainContent$cChkProductList": "on",
            "ctl00$MainContent$cHdUser_Id": "74",
            "ctl00$MainContent$cHdGridColumns": "VF_RowNumber,Product_Code,VF_ProductNameUnit,Product_Qty,Product_Location,Product_OrderComment,VF_Product_SellerMainCode",
            "ctl00$MainContent$cHdProduct_Id": "-1",
            "ctl00$MainContent$cHdIsCopyToInsert": "false",
            "ctl00$MainContent$cHdIsBranchRunning": "False",
                }
        return scrapy.FormRequest.from_response(
                response,
                formdata=logindata,
                callback=self.parsefirstpage
                )
    def parsefirstpage(self,response):
        with open("sriya_firstpage.html",'w') as f:
            f.write(response.text)
            logging.debug(f'first page is returned at {response.url}')
        secondpage_data={
            "__VIEWSTATEGENERATOR":response.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value').extract_first(),
            "__VIEWSTATE":response.xpath('//*[@id="__VIEWSTATE"]/@value').extract_first(),
            "__EVENTTARGET":"ctl00$MainContent$cGrvProduct",
            "__EVENTVALIDATION":response.xpath('//*[@id="__EVENTVALIDATION"]/@value').extract_first(),
            "__EVENTARGUMENT":"Page$2",
            "ctl00$Page_Header1$cHdCompany_Title1": "บริษัท ศิริยาฟาร์มา (2) จำกัด",
            "ctl00$Page_Header1$cHdCompany_Title2": "หน้าร้าน",
            "ctl00$Page_Header1$cHdLogin_FullName": "Health Express",
            "ctl00$MainContent$cChkProductAdd": "on",
            "ctl00$MainContent$cChkProductSearch": "on",
            "ctl00$MainContent$cRdFindType": "1",
            "ctl00$MainContent$cHdPickList_ProductGroup": "1",
            "ctl00$MainContent$cHdPickList_ProductType": "2",
            "ctl00$MainContent$cHdPickList_ProductGenericName": "5",
            "ctl00$MainContent$cDdItemPerPage": "10000",
            "ctl00$MainContent$cChkProductList": "on",
            "ctl00$MainContent$cHdUser_Id": "74",
            "ctl00$MainContent$cHdGridColumns": "VF_RowNumber,Product_Code,VF_ProductNameUnit,Product_Qty,Product_Location,Product_OrderComment,VF_Product_SellerMainCode",
            "ctl00$MainContent$cHdProduct_Id": "-1",
            "ctl00$MainContent$cHdIsCopyToInsert": "false",
            "ctl00$MainContent$cHdIsBranchRunning": "False",
               }
        return scrapy.FormRequest.from_response(
                response,
                formdata=secondpage_data,
                callback=self.parse_secondpage
                )
    def parse_secondpage(self,response):
        with open("sriya_secondpage.html",'w') as f:
            f.write(response.text)
            logging.debug(f'second page is returned at {response.url}')
