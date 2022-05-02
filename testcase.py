import unittest
import check_data

class DataTestCase(unittest.TestCase):
    def test_data(self):
        #測試空資料
        empty_data = {}
        self.assertEqual(check_data.validation(empty_data), 0)
        #測試缺漏值
        less_data = {"date": "2019-06-05"}
        self.assertEqual(check_data.validation(less_data), 0)
        #測試key不在預設
        wrong_key = {"ad_network": "FOO", "datetime": "2019-06-05", "app_name": "LINETV", "unit_id": "55665201314","request": "100", "revenue": "0.00365325", "imp": "23"}
        self.assertEqual(check_data.validation(wrong_key), 0)
        #測試ad值格式
        ad_type = {"ad_network": 123, "date": "2019-06-05", "app_name": "LINETV", "unit_id": "55665201314","request": "100", "revenue": "0.00365325", "imp": "23"}
        self.assertEqual(check_data.validation(ad_type), 0)
        #測試date值格式
        date_type = {"ad_network": "FOO", "date": "2019_06_05", "app_name": "LINETV", "unit_id": "55665201314","request": "100", "revenue": "0.00365325", "imp": "23"}
        self.assertEqual(check_data.validation(date_type), 0)
        #測試app值格式
        app_type = {"ad_network": "FOO", "date": "2019-06-05", "app_name": 123, "unit_id": "55665201314","request": "100", "revenue": "0.00365325", "imp": "23"}
        self.assertEqual(check_data.validation(app_type), 0)
        #測試id值格式
        id_type = {"ad_network": "FOO", "date": "2019-06-05", "app_name": "LINETV", "unit_id": 123,"request": "100", "revenue": "0.00365325", "imp": "23"}
        self.assertEqual(check_data.validation(id_type), 0)
        #測試request值格式
        request_type = {"ad_network": "FOO", "date": "2019-06-05", "app_name": "LINETV", "unit_id": "55665201314","request": 123, "revenue": "0.00365325", "imp": "23"}
        self.assertEqual(check_data.validation(request_type), 0)
        #測試revenue值格式
        revenue_type = {"ad_network": "FOO", "date": "2019-06-05", "app_name": "LINETV", "unit_id": "55665201314","request": "100", "revenue": 123, "imp": "23"}
        self.assertEqual(check_data.validation(revenue_type), 0)
        #測試imp值格式
        imp_type = {"ad_network": "FOO", "date": "2019-06-05", "app_name": "LINETV", "unit_id": "55665201314","request": "100", "revenue": "0.00365325", "imp": 123}
        self.assertEqual(check_data.validation(imp_type), 0)
        #測試資料空值
        miss_data = {"ad_network": "FOO", "date": "2019-06-05", "app_name": "LINETV", "unit_id": "55665201314","request": "100", "revenue": "0.00365325", "imp": ""}
        self.assertEqual(check_data.validation(miss_data), 0)
        #測試資料空值
        none_data = {"ad_network": None, "date": "2019-06-05", "app_name": "LINETV", "unit_id": "55665201314","request": "100", "revenue": "0.00365325", "imp": "23"}
        self.assertEqual(check_data.validation(none_data), 0)
        #測試id整數
        id_int = {"ad_network": "FOO", "date": "2019-06-05", "app_name": "LINETV", "unit_id": "LINETV","request": "100", "revenue": "0.00365325", "imp": "23"}
        self.assertEqual(check_data.validation(id_int), 0)
        #測試request整數
        request_int = {"ad_network": "FOO", "date": "2019-06-05", "app_name": "LINETV", "unit_id": "55665201314","request": "LINETV", "revenue": "0.00365325", "imp": "23"}
        self.assertEqual(check_data.validation(request_int), 0)
        #測試imp整數
        imp_int = {"ad_network": "FOO", "date": "2019-06-05", "app_name": "LINETV", "unit_id": "55665201314","request": "100", "revenue": "0.00365325", "imp": "LINETV"}
        self.assertEqual(check_data.validation(imp_int), 0)
        #測試revenue浮點數
        revenue_float = {"ad_network": "FOO", "date": "2019-06-05", "app_name": "LINETV", "unit_id": "55665201314","request": "100", "revenue": "LINETV", "imp": "23"}
        self.assertEqual(check_data.validation(revenue_float), 0)
        #測試revenue浮點數
        revenue_float2 = {"ad_network": "FOO", "date": "2019-06-05", "app_name": "LINETV", "unit_id": "55665201314","request": "100", "revenue": "0.00.365325", "imp": "23"}
        self.assertEqual(check_data.validation(revenue_float2), 0)
        #測試正確資料
        checked_data = {"ad_network": "FOO", "date": "2019-06-05", "app_name": "LINETV", "unit_id": "55665201314","request": "100", "revenue": "0.00365325", "imp": "23"}
        self.assertEqual(check_data.validation(checked_data), 1)
        
if __name__ == '__main__':
    unittest.main()