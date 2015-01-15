#!/usr/bin/env python
"""
WordAPI.py
Copyright 2014 Wordnik, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

from .models import *


class TradeApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    

    def get(self, **kwargs):
        """Get Trades.

        Args:
            symbol, str: Instrument symbol. Send a series (e.g. XBT) to get data for the nearest contract in that series. (optional)

            filter, object: Generic table filter. Send JSON key/value pairs, such as {&quot;key&quot;: &quot;value&quot;}. (optional)

            columns, list[str]: Array of column names to fetch. If omitted, will return all columns. Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect. (optional)

            start, float: Starting point for results. (optional)

            reverse, bool: If true, will sort results newest first. (optional)

            startTime, datetime: Starting date filter for results. (optional)

            endTime, datetime: Ending date filter for results. (optional)

            count, float: Number of results to fetch. (optional)

            

        Returns: Array[Trade]
        """

        allParams = ['symbol', 'filter', 'columns', 'start', 'reverse', 'startTime', 'endTime', 'count']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/trade'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('symbol' in params):
            queryParams['symbol'] = self.apiClient.toPathValue(params['symbol'])
        if ('filter' in params):
            queryParams['filter'] = self.apiClient.toPathValue(params['filter'])
        if ('columns' in params):
            queryParams['columns'] = self.apiClient.toPathValue(params['columns'])
        if ('count' in params):
            queryParams['count'] = self.apiClient.toPathValue(params['count'])
        if ('start' in params):
            queryParams['start'] = self.apiClient.toPathValue(params['start'])
        if ('reverse' in params):
            queryParams['reverse'] = self.apiClient.toPathValue(params['reverse'])
        if ('startTime' in params):
            queryParams['startTime'] = self.apiClient.toPathValue(params['startTime'])
        if ('endTime' in params):
            queryParams['endTime'] = self.apiClient.toPathValue(params['endTime'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Array[Trade]')
        return responseObject
        

        

    def getBucketed(self, **kwargs):
        """Get previous trades in time buckets.

        Args:
            symbol, str: Instrument symbol. Send a series (e.g. XBT) to get data for the nearest contract in that series. (optional)

            filter, object: Generic table filter. Send JSON key/value pairs, such as {&quot;key&quot;: &quot;value&quot;}. (optional)

            columns, list[str]: Array of column names to fetch. If omitted, will return all columns. Note that this method will always return item keys, even when not specified, so you may receive more columns that you expect. (optional)

            start, float: Starting point for results. (optional)

            reverse, bool: If true, will sort results newest first. (optional)

            startTime, datetime: Starting date filter for results. (optional)

            endTime, datetime: Ending date filter for results. (optional)

            binSize, str: Time interval to bucket by. Available options: ['30s', '1m', '5m', '1h', '1d']. (optional)

            count, float: Number of results to fetch. (optional)

            

        Returns: Array[TradeBin]
        """

        allParams = ['symbol', 'filter', 'columns', 'start', 'reverse', 'startTime', 'endTime', 'binSize', 'count']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getBucketed" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/trade/bucketed'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('binSize' in params):
            queryParams['binSize'] = self.apiClient.toPathValue(params['binSize'])
        if ('symbol' in params):
            queryParams['symbol'] = self.apiClient.toPathValue(params['symbol'])
        if ('filter' in params):
            queryParams['filter'] = self.apiClient.toPathValue(params['filter'])
        if ('columns' in params):
            queryParams['columns'] = self.apiClient.toPathValue(params['columns'])
        if ('count' in params):
            queryParams['count'] = self.apiClient.toPathValue(params['count'])
        if ('start' in params):
            queryParams['start'] = self.apiClient.toPathValue(params['start'])
        if ('reverse' in params):
            queryParams['reverse'] = self.apiClient.toPathValue(params['reverse'])
        if ('startTime' in params):
            queryParams['startTime'] = self.apiClient.toPathValue(params['startTime'])
        if ('endTime' in params):
            queryParams['endTime'] = self.apiClient.toPathValue(params['endTime'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Array[TradeBin]')
        return responseObject
        

        

    def getByDate(self, startTime, **kwargs):
        """Get trades between two dates. [Deprecated, use GET /trades]

        Args:
            symbol, str: Instrument symbol. Send a series (e.g. XBT) to get data for the nearest contract in that series. (optional)

            startTime, datetime: Start date. (required)

            endTime, datetime: End Date. (optional)

            

        Returns: Array[Trade]
        """

        allParams = ['symbol', 'startTime', 'endTime']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getByDate" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/trade/byDate'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('symbol' in params):
            queryParams['symbol'] = self.apiClient.toPathValue(params['symbol'])
        if ('startTime' in params):
            queryParams['startTime'] = self.apiClient.toPathValue(params['startTime'])
        if ('endTime' in params):
            queryParams['endTime'] = self.apiClient.toPathValue(params['endTime'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Array[Trade]')
        return responseObject
        

        

    def getRecent(self, count= None, **kwargs):
        """Get recent trades. [Deprecated, use GET /trades]

        Args:
            symbol, str: Instrument symbol. Send a series (e.g. XBT) to get data for the nearest contract in that series. (optional)

            count, float: Number of trades to fetch. (required)

            

        Returns: Array[Trade]
        """

        allParams = ['symbol', 'count']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getRecent" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/trade/recent'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('symbol' in params):
            queryParams['symbol'] = self.apiClient.toPathValue(params['symbol'])
        if ('count' in params):
            queryParams['count'] = self.apiClient.toPathValue(params['count'])
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Array[Trade]')
        return responseObject
        

        

    




