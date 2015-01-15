package com.wordnik.client.api;

import com.wordnik.client.ApiException;
import com.wordnik.client.ApiInvoker;
import com.wordnik.client.model.Trade;
import com.wordnik.client.model.TradeBin;
import java.util.*;
import java.io.File;

public class TradeApi {
  String basePath = "https://www.bitmex.com/api/v1";
  ApiInvoker apiInvoker = ApiInvoker.getInstance();

  public void addHeader(String key, String value) {
    getInvoker().addDefaultHeader(key, value);
  }

  public ApiInvoker getInvoker() {
    return apiInvoker;
  }

  public void setBasePath(String basePath) {
    this.basePath = basePath;
  }

  public String getBasePath() {
    return basePath;
  }

  //error info- code: 200 reason: "Request was successful" model: <none>
  //error info- code: 400 reason: "Parameter Error" model: <none>
  //error info- code: 401 reason: "Unauthorized" model: <none>
  //error info- code: 404 reason: "Not Found" model: <none>
  public List<Trade> get (String symbol, Object filter, List<String> columns, Double start, Boolean reverse, Date startTime, Date endTime, Double count) throws ApiException {
    // create path and map variables
    String path = "/trade".replaceAll("\\{format\\}","json");

    // query params
    Map<String, String> queryParams = new HashMap<String, String>();
    Map<String, String> headerParams = new HashMap<String, String>();

    if(!"null".equals(String.valueOf(symbol)))
      queryParams.put("symbol", String.valueOf(symbol));
    if(!"null".equals(String.valueOf(filter)))
      queryParams.put("filter", String.valueOf(filter));
    if(!"null".equals(String.valueOf(columns)))
      queryParams.put("columns", String.valueOf(columns));
    if(!"null".equals(String.valueOf(count)))
      queryParams.put("count", String.valueOf(count));
    if(!"null".equals(String.valueOf(start)))
      queryParams.put("start", String.valueOf(start));
    if(!"null".equals(String.valueOf(reverse)))
      queryParams.put("reverse", String.valueOf(reverse));
    if(!"null".equals(String.valueOf(startTime)))
      queryParams.put("startTime", String.valueOf(startTime));
    if(!"null".equals(String.valueOf(endTime)))
      queryParams.put("endTime", String.valueOf(endTime));
    String contentType = "application/json";

    try {
      String response = apiInvoker.invokeAPI(basePath, path, "GET", queryParams, null, headerParams, contentType);
      if(response != null){
        return (List<Trade>) ApiInvoker.deserialize(response, "List", Trade.class);
      }
      else {
        return null;
      }
    } catch (ApiException ex) {
      if(ex.getCode() == 404) {
        return null;
      }
      else {
        throw ex;
      }
    }
  }
  //error info- code: 200 reason: "Request was successful" model: <none>
  //error info- code: 400 reason: "Parameter Error" model: <none>
  //error info- code: 401 reason: "Unauthorized" model: <none>
  //error info- code: 404 reason: "Not Found" model: <none>
  public List<TradeBin> getBucketed (String symbol, Object filter, List<String> columns, Double start, Boolean reverse, Date startTime, Date endTime, String binSize, Double count) throws ApiException {
    // create path and map variables
    String path = "/trade/bucketed".replaceAll("\\{format\\}","json");

    // query params
    Map<String, String> queryParams = new HashMap<String, String>();
    Map<String, String> headerParams = new HashMap<String, String>();

    if(!"null".equals(String.valueOf(binSize)))
      queryParams.put("binSize", String.valueOf(binSize));
    if(!"null".equals(String.valueOf(symbol)))
      queryParams.put("symbol", String.valueOf(symbol));
    if(!"null".equals(String.valueOf(filter)))
      queryParams.put("filter", String.valueOf(filter));
    if(!"null".equals(String.valueOf(columns)))
      queryParams.put("columns", String.valueOf(columns));
    if(!"null".equals(String.valueOf(count)))
      queryParams.put("count", String.valueOf(count));
    if(!"null".equals(String.valueOf(start)))
      queryParams.put("start", String.valueOf(start));
    if(!"null".equals(String.valueOf(reverse)))
      queryParams.put("reverse", String.valueOf(reverse));
    if(!"null".equals(String.valueOf(startTime)))
      queryParams.put("startTime", String.valueOf(startTime));
    if(!"null".equals(String.valueOf(endTime)))
      queryParams.put("endTime", String.valueOf(endTime));
    String contentType = "application/json";

    try {
      String response = apiInvoker.invokeAPI(basePath, path, "GET", queryParams, null, headerParams, contentType);
      if(response != null){
        return (List<TradeBin>) ApiInvoker.deserialize(response, "List", TradeBin.class);
      }
      else {
        return null;
      }
    } catch (ApiException ex) {
      if(ex.getCode() == 404) {
        return null;
      }
      else {
        throw ex;
      }
    }
  }
  //error info- code: 200 reason: "Request was successful" model: <none>
  //error info- code: 400 reason: "Parameter Error" model: <none>
  //error info- code: 401 reason: "Unauthorized" model: <none>
  //error info- code: 404 reason: "Not Found" model: <none>
  public List<Trade> getByDate (String symbol, Date startTime, Date endTime) throws ApiException {
    // verify required params are set
    if(startTime == null ) {
       throw new ApiException(400, "missing required params");
    }
    // create path and map variables
    String path = "/trade/byDate".replaceAll("\\{format\\}","json");

    // query params
    Map<String, String> queryParams = new HashMap<String, String>();
    Map<String, String> headerParams = new HashMap<String, String>();

    if(!"null".equals(String.valueOf(symbol)))
      queryParams.put("symbol", String.valueOf(symbol));
    if(!"null".equals(String.valueOf(startTime)))
      queryParams.put("startTime", String.valueOf(startTime));
    if(!"null".equals(String.valueOf(endTime)))
      queryParams.put("endTime", String.valueOf(endTime));
    String contentType = "application/json";

    try {
      String response = apiInvoker.invokeAPI(basePath, path, "GET", queryParams, null, headerParams, contentType);
      if(response != null){
        return (List<Trade>) ApiInvoker.deserialize(response, "List", Trade.class);
      }
      else {
        return null;
      }
    } catch (ApiException ex) {
      if(ex.getCode() == 404) {
        return null;
      }
      else {
        throw ex;
      }
    }
  }
  //error info- code: 200 reason: "Request was successful" model: <none>
  //error info- code: 400 reason: "Parameter Error" model: <none>
  //error info- code: 401 reason: "Unauthorized" model: <none>
  //error info- code: 404 reason: "Not Found" model: <none>
  public List<Trade> getRecent (String symbol, Double count) throws ApiException {
    // verify required params are set
    if(count == null ) {
       throw new ApiException(400, "missing required params");
    }
    // create path and map variables
    String path = "/trade/recent".replaceAll("\\{format\\}","json");

    // query params
    Map<String, String> queryParams = new HashMap<String, String>();
    Map<String, String> headerParams = new HashMap<String, String>();

    if(!"null".equals(String.valueOf(symbol)))
      queryParams.put("symbol", String.valueOf(symbol));
    if(!"null".equals(String.valueOf(count)))
      queryParams.put("count", String.valueOf(count));
    String contentType = "application/json";

    try {
      String response = apiInvoker.invokeAPI(basePath, path, "GET", queryParams, null, headerParams, contentType);
      if(response != null){
        return (List<Trade>) ApiInvoker.deserialize(response, "List", Trade.class);
      }
      else {
        return null;
      }
    } catch (ApiException ex) {
      if(ex.getCode() == 404) {
        return null;
      }
      else {
        throw ex;
      }
    }
  }
  }

