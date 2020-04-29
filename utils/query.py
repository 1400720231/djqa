from elasticsearch import Elasticsearch
import os

client = Elasticsearch(hosts='http://localhost:9200/')


# es搜索praisegoods的s算法
def search_from_es(sentence):

    """

    param sentente:询问的句子
    param kdt_id:有赞店铺id,praisestore保存为sid,prasiegoods保存为kdt_id
    param default_field:默认搜索的es中的字段为title
    param fuzziness:
    param order:匹配到的数据按照_score倒序排列
    """
    index = 'djqa'
    doc_type = 'modelresult'
   
    search_body = {
        "query": {
            "bool": {
                "must": [
                    {
                        "query_string": {
                            "default_field": '_all',
                            "query": sentence,
                        }
                    }
                ]
            }
        },
        "sort": [{"_score": "desc"}]
    }
    response = client.search(index=index, doc_type=doc_type, body=search_body)
    # print(response['hits']['total'])
    # print(response['hits']['hits'])
    if not response['hits']['total']:
        return None
    else:
        # print(response['hits']['hits'])
        
        results = [ hit for hit in response['hits']['hits']  ]# 最小分数设置在这里
        return results[0]['_source']['text']
if __name__ == '__main__':
	res = search_from_es("管理")
	print(res)

