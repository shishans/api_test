import os
import sys
import pytest
import urllib3
import allure
urllib3.disable_warnings()
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from case.func.classificationDelete import ClassificationDelete
from case.func.classificationAdd import ClassificationAdd,db_classificationDelete
from common.read_yaml import readyml
from common.mylogger import logger
from common.connect_mysql import execute_sql,select_sql

curPath = os.path.dirname(os.path.dirname(__file__))+'/data'
yamlFilePath = os.path.join(curPath, 'classificationAdd.yml')
base_data = readyml(yamlFilePath)

@allure.feature('web-分类-添加分类')
class TestClassificationAdd():

    @pytest.fixture(scope='module')
    def start_up(self,getSession,getImagePath,getHostAndProxies,file_path,dbinfo):
        s = getSession
        host,proxies = getHostAndProxies
        add = ClassificationAdd(s, host)
        image_path = getImagePath
        dele = ClassificationDelete(s,host)
        db = dbinfo
        sql = '''
                DELETE from classification_add where classification_name='{name}'
                '''
        return s,add,image_path,dele,proxies,db,sql


    # @pytest.fixture(scope='function')
    # def start_up(self,getSession,getImagePath,getHostAndProxies,file_path,dbinfo):
    #     s = getSession
    #     host,proxies = getHostAndProxies
    #     add = ClassificationAdd(s, host)
    #     image_path = getImagePath
    #     dele = ClassificationDelete(s,host)
    #     yield s,add,image_path,dele,proxies
    #     db = dbinfo
    #     db_classificationDelete(db, base_data['case1']['name'][0])
    #     logger.info('删除添加的数据')

    # @pytest.fixture(scope='function')
    # def delet(self,dbinfo,request):
    #     db = dbinfo
    #     db_classificationDelete(db,base_data['case1']['name'][0])
    #     logger.info('删除添加的数据')

    data = base_data['case1']
    @allure.story('只传必填项，添加成功')
    @pytest.mark.classificationAdd
    @pytest.mark.parametrize('source',data['source'])
    @pytest.mark.parametrize('status',data['status'])
    @pytest.mark.parametrize('name',data['name'])
    @pytest.mark.parametrize('parentId',data['parentId'])
    def test_classificationAdd_1(self,start_up,name,parentId,status,source):
        '''只传必填项，添加成功'''
        try:
            s,add,image_path,dele,proxies,db,sql = start_up
            data = {
                'name':name,
                'parentId':parentId,
                'status':status,
                'source':source,
                'proxies': proxies
            }
            r = add.classificationAdd(**data)
            assert r['code'] == '000000'
            assert r['data'] != None
            classificationId = r['data']
            r = dele.classificationDelete(classificationId,proxies=proxies)
            assert r['code'] == '000000'
        finally:
            pass
            # sql = sql.format(name=name)
            # logger.info('数据库删除新增的分类，sql:%s'%sql)
            # execute_sql(db,sql)
            # print('执行了删除操作')



    # data = base_data['case1']
    # @allure.story('只传必填项，添加成功')
    # @pytest.mark.classificationAdd
    # @pytest.mark.parametrize('source',data['source'])
    # @pytest.mark.parametrize('status',data['status'])
    # @pytest.mark.parametrize('name',data['name'])
    # @pytest.mark.parametrize('parentId',data['parentId'])
    # def test_classificationAdd_1(self,start_up,name,parentId,status,source,delet):
    #     '''只传必填项，添加成功'''
    #     s,add,image_path,dele,proxies = start_up
    #     data = {
    #         'name':name,
    #         'parentId':parentId,
    #         'status':status,
    #         'source':source,
    #         'proxies': proxies
    #     }
    #     r = add.classificationAdd(**data)
    #     assert r['code'] == '000000'
    #     assert r['data'] != None
    #     classificationId = r['data']
    #     r = dele.classificationDelete(classificationId,proxies=proxies)
    #     assert r['code'] == '000000'
    #     delet

    data = base_data['case2']

    @allure.story('添加分类，上传图片')
    @pytest.mark.classificationAdd
    @pytest.mark.parametrize('source',data['source'])
    @pytest.mark.parametrize('status',data['status'])
    @pytest.mark.parametrize('name',data['name'])
    @pytest.mark.parametrize('parentId',data['parentId'])
    def test_classificationAdd_uploadImage_2(self,start_up,name,parentId,status,source):
        '''添加分类，上传图片'''
        try:
            s,add,image_path,dele,proxies,db,sql = start_up
            data = {
                'name':name,
                'parentId':parentId,
                'status':status,
                'source':source,
                'proxies': proxies,
                'logo':image_path
            }
            r = add.classificationAdd(**data)
            assert r['code'] == '000000'
            assert r['data'] != None
            classificationId = r['data']
            r = dele.classificationDelete(classificationId,proxies=proxies)
            assert r['code'] == '000000'
        finally:
            pass
            # sql = sql.format(name=name)
            # logger.info('数据库删除新增的分类，sql:%s'%sql)
            # execute_sql(db,sql)
            # print('执行了删除操作')






