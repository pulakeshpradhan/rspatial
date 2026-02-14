[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pulakeshpradhan/geopython/blob/main/Web_Scraping_web_Table.ipynb)

# Web Scraping Web Table using Python
---
This Jupyter Notebook demonstrates how to extract tabular data from a **Web page** using Python libraries `requests`, `BeautifulSoup` and `pandas`.




```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

```


### Imports three core Python libraries:

requests: for fetching web pages using HTTP.

BeautifulSoup: for parsing and navigating HTML/XML content.

pandas: for reading structured tables and storing them as DataFrames.


These libraries together form a complete workflow — fetch → parse → extract → analyze.

### Set the target URL
We specify the web page we want to scrape data from.


Defines the target webpage URL (the page listing large dams in India).

This URL acts as the source from which your script will collect the data.


```python
# URL of the dams page
url = "https://indiawris.gov.in/wiki/doku.php?id=large_dams_in_india"

```

### Send the HTTP request to fetch page content
We use `requests.get()` to retrieve the HTML of the web page.


```python
# Fetch the web page using requests
response = requests.get(url)
print(response)

#response.status_code
```

    <Response [200]>
    

Sends an HTTP GET request to the given URL and prints the response object.


The response object tells you whether your request was successful.

A status code like 200 means success; others (e.g., 404) indicate errors.

### Converts the HTML content of the response into a structured parse tree using BeautifulSoup.

You can now search for tags like < table >, < div >, or < p >  easily — ideal for extracting data.



```python
soup = BeautifulSoup(response.text, "html.parser")
print(soup)

```

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    
    <html dir="ltr" lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
    <title>large_dams_in_india - INDIA WRIS WIKI</title>
    <meta content="DokuWiki" name="generator"/>
    <meta content="index,follow" name="robots"/>
    <meta content="large_dams_in_india" name="keywords"/>
    <link href="/wiki/lib/exe/opensearch.php" rel="search" title="INDIA WRIS WIKI" type="application/opensearchdescription+xml"/>
    <link href="/wiki/" rel="start"/>
    <link href="/wiki/doku.php?id=large_dams_in_india&amp;do=index" rel="contents" title="Sitemap"/>
    <link href="/wiki/lib/exe/manifest.php" rel="manifest"/>
    <link href="/wiki/feed.php" rel="alternate" title="Recent Changes" type="application/rss+xml"/>
    <link href="/wiki/feed.php?mode=list&amp;ns=" rel="alternate" title="Current namespace" type="application/rss+xml"/>
    <link href="/wiki/doku.php?do=export_xhtml&amp;id=large_dams_in_india" rel="alternate" title="Plain HTML" type="text/html"/>
    <link href="/wiki/doku.php?do=export_raw&amp;id=large_dams_in_india" rel="alternate" title="Wiki Markup" type="text/plain"/>
    <link href="http://10.247.136.5/wiki/doku.php?id=large_dams_in_india" rel="canonical"/>
    <link href="/wiki/lib/exe/css.php?t=vector&amp;tseed=c1598faef04a5955bd72b1dabab273ea" rel="stylesheet" type="text/css"/>
    <!--[if gte IE 9]><!-->
    <script type="text/javascript">/*<![CDATA[*/var NS='';var JSINFO = {"confirm_delete":"Are you sure you want to delete this page?","doku_base":"\/wiki\/","cg_rev":"","dw_version":50.2,"chrome_version":0,"hide_captcha_error":"none","ckg_dbl_click":"","ckg_canonical":0,"doku_url":"http:\/\/10.247.136.5\/wiki\/","has_wrap":"Wrap","wrapDiv":"WRAP","wrapSpan":"wrap","ckgEdPaste":"off","rel_links":0,"ckg_template":"vector","htmlok":1,"id":"large_dams_in_india","namespace":"","ACT":"show","useHeadingNavigation":0,"useHeadingContent":0};
    /*!]]>*/</script>
    <script charset="utf-8" src="/wiki/lib/exe/jquery.php?tseed=23f888679b4f1dc26eef34902aca964f" type="text/javascript"></script>
    <script charset="utf-8" src="/wiki/lib/exe/js.php?t=vector&amp;tseed=c1598faef04a5955bd72b1dabab273ea" type="text/javascript"></script>
    <script charset="utf-8" defer="defer" src="/wiki/lib/plugins/ckgedit/scripts/mediamgr.js" type="text/javascript"></script>
    <!--<![endif]-->
    <script type="text/javascript">
        //<![CDATA[ 
        function LoadScript( url )
        {
         document.write( '<scr' + 'ipt type="text/javascript" src="' + url + '"><\/scr' + 'ipt>' ) ;        
    
        }
       function LoadScriptDefer( url )
        {
         document.write( '<scr' + 'ipt type="text/javascript" src="' + url + '" defer><\/scr' + 'ipt>' ) ;        
    
        }
    //]]> 
    
     </script>
    <meta content="width=device-width,initial-scale=1" name="viewport"/>
    <link href="/wiki/lib/tpl/vector/user/favicon.ico" rel="shortcut icon"/>
    <link href="/wiki/lib/tpl/vector/static/3rd/dokuwiki/apple-touch-icon.png" rel="apple-touch-icon"/>
    <!--[if lte IE 8]><link rel="stylesheet" media="all" type="text/css" href="/wiki/lib/tpl/vector/static/css/screen_iehacks.css" /><![endif]-->
    <!--[if lt IE 7]><style type="text/css">body{behavior:url("/wiki/lib/tpl/vector/static/3rd/vector/csshover.htc")}</style><![endif]-->
    </head>
    <body class="skin-vector">
    <div id="page-container">
    <div class="noprint" id="page-base"></div>
    <div class="noprint" id="head-base"></div>
    <!-- start div id=content -->
    <div id="content">
    <a id="top" name="top"></a>
    <a id="dokuwiki__top" name="dokuwiki__top"></a>
    <!-- start main content area -->
    <!-- start div id bodyContent -->
    <div class="dokuwiki" id="bodyContent">
    <!-- start rendered wiki content -->
    <h1 class="sectionedit1" id="large_dams_in_india">Large Dams in India</h1>
    <div class="level1">
    <p>
    <strong>DEFINITION OF LARGE DAMS FOR INCLUSION UNDER NRLD</strong> <br/>
    
    As per International Commission on Large Dams (ICOLD) Specification
    </p>
    <ul>
    <li class="level1"><div class="li"> A large dam is classified as one with a maximum height of more than 15 metres from its deepest foundation to the crest.</div>
    </li>
    <li class="level1"><div class="li"> A dam between 10 and 15 metres in height from its deepest foundation is also included in the classification of a large dam provided it complies with one of the following conditions :</div>
    </li>
    </ul>
    <p>
    a) length of crest of the dam is not less than 500 metres or
    </p>
    <p>
    b) capacity of the reservoir formed by the dam is not less than one million cubic metres or
    </p>
    <p>
    c) the maximum flood discharge dealt with by the dam is not less than 2000 cubic metres per second or
    </p>
    <p>
    d) the dam has specially difficult foundation problems, or
    </p>
    <p>
    e) the dam is of unusual design
    </p>
    <p>
    On review on consideration of “height” for arriving at whether dam is in category of Large dam or not the above definition has been retained for dams other than Earthen and Rock fill dams. For Earthen and Rock fill dams following definition of large dams has been adopted from “IS 12169-1987- criteria for design of small embankment dams” for inclusion under NRLD.
    </p>
    <p>
    <strong>Large Dam</strong>
    </p>
    <p>
    A dam exceeding 15m in height above deepest river bed level and a dam between 10 and 15 m height provided volume of earthwork exceeds 0.75 million m<sup>3</sup>   and storage exceeds 1 million m<sup>3</sup>   or the maximum flood discharge exceeds 2000 cumecs.“
    </p>
    <div class="table sectionedit2"><table class="inline">
    <thead>
    <tr class="row0">
    <th class="col0">#</th><th class="col1">Name</th><th class="col2">Purpose</th><th class="col3">River</th><th class="col4">Nearest City</th><th class="col5">District</th><th class="col6">State</th><th class="col7">Basin</th><th class="col8">Status</th><th class="col9">Completion Year</th><th class="col10">Type</th><th class="col11">Length (m)</th><th class="col12">Max Height above Foundation (m)</th><th class="col13">Design Gross Storage Capacity (MCM)</th>
    </tr>
    </thead>
    <tr class="row1">
    <th class="col0">1</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00742&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Tehri_Dam_D00742" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00742&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Tehri_Dam_D00742">Tehri Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Bhagirathi</td><td class="col4">Pratapnagar</td><td class="col5">Tehri Garhwal</td><td class="col6">Uttarakhand</td><td class="col7">Ganga</td><td class="col8">Completed</td><td class="col9">2005</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">575</td><td class="col12">260.5</td><td class="col13">3540</td>
    </tr>
    <tr class="row2">
    <th class="col0">2</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00723&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lakhwar_Dam_D00723" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00723&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lakhwar_Dam_D00723">Lakhwar Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Yamuna</td><td class="col4">Dehradun</td><td class="col5">Dehradun</td><td class="col6">Uttarakhand</td><td class="col7">Ganga</td><td class="col8">Proposed</td><td class="col9"> </td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">451</td><td class="col12">204</td><td class="col13">587.84</td>
    </tr>
    <tr class="row3">
    <th class="col0">3</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03331&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Idukki_(Eb)/Idukki_Arch_Dam_D03331" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03331&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Idukki_(Eb)/Idukki_Arch_Dam_D03331">Idukki (Eb)/Idukki Arch Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Periyar</td><td class="col4">Todupulai</td><td class="col5">Idukki</td><td class="col6">Kerala</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1974</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">366</td><td class="col12">169</td><td class="col13">1998.57</td>
    </tr>
    <tr class="row4">
    <th class="col0">4</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00993&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Bhakra_Dam_D00993" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00993&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Bhakra_Dam_D00993">Bhakra Dam</a></td><td class="col2">Hydroelectric,Irrigation,Recreation</td><td class="col3">Satluj</td><td class="col4">Bilaspur</td><td class="col5">Bilaspur</td><td class="col6">Himachal Pradesh</td><td class="col7">Indus up to International Border</td><td class="col8">Completed</td><td class="col9">1963</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">518.16</td><td class="col12">167.64</td><td class="col13">9867.84</td>
    </tr>
    <tr class="row5">
    <th class="col0">5</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D02983&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Pakal_Dul_Dam_D02983" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D02983&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Pakal_Dul_Dam_D02983">Pakal Dul Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Marusudar</td><td class="col4">Kishtwar</td><td class="col5">Kishtwar</td><td class="col6">Jammu &amp; Kashmir</td><td class="col7">Indus up to International Border</td><td class="col8">Proposed</td><td class="col9"> </td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">305</td><td class="col12">167</td><td class="col13">.1254</td>
    </tr>
    <tr class="row6">
    <th class="col0">6</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03023&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Sardar_Sarover_Gujarat_Dam_D03023" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03023&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Sardar_Sarover_Gujarat_Dam_D03023">Sardar Sarover Gujarat Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Narmada</td><td class="col4">Rajpipla</td><td class="col5">Narmada</td><td class="col6">Gujarat</td><td class="col7">Narmada</td><td class="col8">Completed</td><td class="col9"> </td><td class="col10">Gravity &amp; Masonry</td><td class="col11">1210</td><td class="col12">163</td><td class="col13">9500</td>
    </tr>
    <tr class="row7">
    <th class="col0">7</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00557&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Srisailam_(N.S.R.S.P)_Dam_D00557" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00557&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Srisailam_(N.S.R.S.P)_Dam_D00557">Srisailam (N.S.R.S.P) Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Krishna</td><td class="col4">Nandikotkur</td><td class="col5">Kurnool</td><td class="col6">Telangana</td><td class="col7">Krishna</td><td class="col8">Completed</td><td class="col9">1984</td><td class="col10">Earthen</td><td class="col11">512</td><td class="col12">145</td><td class="col13">8724.88</td>
    </tr>
    <tr class="row8">
    <th class="col0">8</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03535&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Ranjit_Sagar_Dam_D03535" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03535&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Ranjit_Sagar_Dam_D03535">Ranjit Sagar Dam</a></td><td class="col2">Flood Control,Hydroelectric,Irrigation</td><td class="col3">Ravi</td><td class="col4">Pathankot</td><td class="col5">Kathua</td><td class="col6">Punjab</td><td class="col7">Indus up to International Border</td><td class="col8">Completed</td><td class="col9">1999</td><td class="col10">Earthen</td><td class="col11">617</td><td class="col12">145</td><td class="col13">3280</td>
    </tr>
    <tr class="row9">
    <th class="col0">9</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03079&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Baglihar_Dam_D03079" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03079&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Baglihar_Dam_D03079">Baglihar Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">CHENAB</td><td class="col4">Ramban</td><td class="col5">Ramban</td><td class="col6">Jammu &amp; Kashmir</td><td class="col7">Indus up to International Border</td><td class="col8">Completed</td><td class="col9">2009</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">364.362</td><td class="col12">143</td><td class="col13">475</td>
    </tr>
    <tr class="row10">
    <th class="col0">10</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00589&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Chamera_I_Dam_D00589" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00589&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Chamera_I_Dam_D00589">Chamera I Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Ravi</td><td class="col4">Bhattiyat</td><td class="col5">Chamba</td><td class="col6">Himachal Pradesh</td><td class="col7">Indus up to International Border</td><td class="col8">Completed</td><td class="col9">1994</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">295</td><td class="col12">140</td><td class="col13">242.3</td>
    </tr>
    <tr class="row11">
    <th class="col0">11</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03326&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Cheruthoni_(Eb)_Dam_D03326" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03326&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Cheruthoni_(Eb)_Dam_D03326">Cheruthoni (Eb) Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Cheruthoni</td><td class="col4">Todupulai</td><td class="col5">Idukki</td><td class="col6">Kerala</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1976</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">651</td><td class="col12">138.38</td><td class="col13">1998.57</td>
    </tr>
    <tr class="row12">
    <th class="col0">12</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00579&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Pong_Dam_D00579" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00579&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Pong_Dam_D00579">Pong Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Beas</td><td class="col4">Dera Gopipur</td><td class="col5">Kangra</td><td class="col6">Himachal Pradesh</td><td class="col7">Indus up to International Border</td><td class="col8">Completed</td><td class="col9">1974</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">1950.7</td><td class="col12">132.59</td><td class="col13">8570</td>
    </tr>
    <tr class="row13">
    <th class="col0">13</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01161&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Jamrani_Dam_D01161" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01161&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Jamrani_Dam_D01161">Jamrani Dam</a></td><td class="col2">Irrigation</td><td class="col3">Gola</td><td class="col4">Naini Tal</td><td class="col5">Nainital</td><td class="col6">Uttarakhand</td><td class="col7">Ganga</td><td class="col8">Proposed</td><td class="col9">1990</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">465</td><td class="col12">130.6</td><td class="col13"> </td>
    </tr>
    <tr class="row14">
    <th class="col0">14</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00004&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Subansiri_Lower_HE_(Nhpc)_Dam_D00004" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00004&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Subansiri_Lower_HE_(Nhpc)_Dam_D00004">Subansiri Lower HE (Nhpc) Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Subansiri</td><td class="col4">Lower Subansiri</td><td class="col5">Lower Subansiri</td><td class="col6">Arunanchal Pradesh</td><td class="col7">Brahmaputra</td><td class="col8">Under Construction</td><td class="col9">2014</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">284</td><td class="col12">130</td><td class="col13">1643</td>
    </tr>
    <tr class="row15">
    <th class="col0">15</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01125&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Ramganga_Dam_D01125" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01125&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Ramganga_Dam_D01125">Ramganga Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Ramganga</td><td class="col4">Lansdowne</td><td class="col5">Garhwal</td><td class="col6">Uttarakhand</td><td class="col7">Ganga</td><td class="col8">Completed</td><td class="col9">1974</td><td class="col10">Earthen</td><td class="col11">630</td><td class="col12">127.5</td><td class="col13">2448</td>
    </tr>
    <tr class="row16">
    <th class="col0">16</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00690&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Nagarjuna_Sagar_Dam_D00690" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00690&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Nagarjuna_Sagar_Dam_D00690">Nagarjuna Sagar Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Krishna</td><td class="col4">Guruzala</td><td class="col5">Guntur</td><td class="col6">Telangana</td><td class="col7">Krishna</td><td class="col8">Completed</td><td class="col9">1974</td><td class="col10">Earthen</td><td class="col11">4865</td><td class="col12">124.66</td><td class="col13">11553</td>
    </tr>
    <tr class="row17">
    <th class="col0">17</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03369&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Kakki_(Eb)_Dam_D03369" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03369&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Kakki_(Eb)_Dam_D03369">Kakki (Eb) Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Kakki</td><td class="col4">Rani</td><td class="col5">Pathanamthitta</td><td class="col6">Kerala</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1966</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">336.19</td><td class="col12">116.13</td><td class="col13">454.07</td>
    </tr>
    <tr class="row18">
    <th class="col0">18</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01205&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Nagi_Dam_D01205" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01205&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Nagi_Dam_D01205">Nagi Dam</a></td><td class="col2">Irrigation</td><td class="col3">Nagi</td><td class="col4">Jamui</td><td class="col5">Jamui</td><td class="col6">Bihar</td><td class="col7">Ganga</td><td class="col8">Completed</td><td class="col9">1958</td><td class="col10">Earthen</td><td class="col11">1884</td><td class="col12">113.5</td><td class="col13">108</td>
    </tr>
    <tr class="row19">
    <th class="col0">19</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03068&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Salal_(Rockfill_And_Concrete_)_Dam_D03068" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03068&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Salal_(Rockfill_And_Concrete_)_Dam_D03068">Salal (Rockfill And Concrete ) Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Chenab</td><td class="col4">Gool Gulab Garh</td><td class="col5">Reasi</td><td class="col6">Jammu &amp; Kashmir</td><td class="col7">Indus up to International Border</td><td class="col8">Completed</td><td class="col9">1986</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">487</td><td class="col12">113</td><td class="col13">28.5</td>
    </tr>
    <tr class="row20">
    <th class="col0">20</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D05812&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lakhya_Dam_D05812" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D05812&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lakhya_Dam_D05812">Lakhya Dam</a></td><td class="col2">Drinking / Water Supply</td><td class="col3">Lakhya hole</td><td class="col4">Mudigere</td><td class="col5">Chikmagalur</td><td class="col6">Karnataka</td><td class="col7">Krishna</td><td class="col8">Completed</td><td class="col9">1994</td><td class="col10">Earthen</td><td class="col11">1048</td><td class="col12">108</td><td class="col13">273.79</td>
    </tr>
    <tr class="row21">
    <th class="col0">21</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00314&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Sholayar_Dam_D00314" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00314&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Sholayar_Dam_D00314">Sholayar Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Sholayar</td><td class="col4">Pollachi</td><td class="col5">Coimbatore</td><td class="col6">Tamil Nadu</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1971</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">1244.18</td><td class="col12">105.16</td><td class="col13">152.48</td>
    </tr>
    <tr class="row22">
    <th class="col0">22</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D05104&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Koyna_Dam_D05104" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D05104&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Koyna_Dam_D05104">Koyna Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Koyna</td><td class="col4">Patan</td><td class="col5">Satara</td><td class="col6">Maharashtra</td><td class="col7">Krishna</td><td class="col8">Completed</td><td class="col9">1964</td><td class="col10">Earthen</td><td class="col11">807.72</td><td class="col12">103.02</td><td class="col13">2980.69</td>
    </tr>
    <tr class="row23">
    <th class="col0">23</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03183&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Idamalayar_(Eb)_Dam_D03183" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03183&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Idamalayar_(Eb)_Dam_D03183">Idamalayar (Eb) Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Idamalayar</td><td class="col4">Devikolam</td><td class="col5">Idukki</td><td class="col6">Kerala</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1985</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">373</td><td class="col12">102</td><td class="col13">1208.23</td>
    </tr>
    <tr class="row24">
    <th class="col0">24</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D04595&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Supa_Dam_D04595" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D04595&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Supa_Dam_D04595">Supa Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Kali Nadi</td><td class="col4">Supa</td><td class="col5">Uttara Kannada</td><td class="col6">Karnataka</td><td class="col7">West flowing rivers from Tapi to Tadri</td><td class="col8">Completed</td><td class="col9">1987</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">331.29</td><td class="col12">101</td><td class="col13">4178</td>
    </tr>
    <tr class="row25">
    <th class="col0">25</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01195&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Karjan_Dam_D01195" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01195&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Karjan_Dam_D01195">Karjan Dam</a></td><td class="col2">Irrigation</td><td class="col3">Karjan</td><td class="col4">Rajpipla</td><td class="col5">Narmada</td><td class="col6">Gujarat</td><td class="col7">Narmada</td><td class="col8">Completed</td><td class="col9">1987</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">903</td><td class="col12">100</td><td class="col13">630</td>
    </tr>
    <tr class="row26">
    <th class="col0">26</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03334&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Kulamavu_(Eb)_Dam_D03334" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03334&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Kulamavu_(Eb)_Dam_D03334">Kulamavu (Eb) Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Kilivillithode</td><td class="col4">Todupulai</td><td class="col5">Idukki</td><td class="col6">Kerala</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1977</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">385</td><td class="col12">100</td><td class="col13">1998.57</td>
    </tr>
    <tr class="row27">
    <th class="col0">27</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00823&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Koteshwar_Dam_D00823" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00823&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Koteshwar_Dam_D00823">Koteshwar Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Bhagirathi</td><td class="col4">Pratapnagar</td><td class="col5">Tehri Garhwal</td><td class="col6">Uttarakhand</td><td class="col7">Ganga</td><td class="col8">Completed</td><td class="col9"> </td><td class="col10">Gravity &amp; Masonry</td><td class="col11">300.5</td><td class="col12">97.5</td><td class="col13">88.9</td>
    </tr>
    <tr class="row28">
    <th class="col0">28</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00654&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lower_:_PPSP_Dam_D00654" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00654&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lower_:_PPSP_Dam_D00654">Lower : PPSP Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Kistobazar nalla</td><td class="col4">Puruliya</td><td class="col5">Puruliya</td><td class="col6">West Bengal</td><td class="col7">Subarnarekha</td><td class="col8">Completed</td><td class="col9"> </td><td class="col10">Rockfill</td><td class="col11">310</td><td class="col12">95</td><td class="col13">16</td>
    </tr>
    <tr class="row29">
    <th class="col0">29</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01456&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Doyang_Hep_Dam_D01456" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01456&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Doyang_Hep_Dam_D01456">Doyang Hep Dam</a></td><td class="col2">Hydroelectric,Drinking / Water Supply</td><td class="col3">Doyang</td><td class="col4">Wokha</td><td class="col5">Wokha</td><td class="col6">Nagaland</td><td class="col7">Brahmaputra</td><td class="col8">Completed</td><td class="col9"> </td><td class="col10">Earthen</td><td class="col11">462</td><td class="col12">92</td><td class="col13">565</td>
    </tr>
    <tr class="row30">
    <th class="col0">30</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00726&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Rihand_Dam_D00726" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00726&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Rihand_Dam_D00726">Rihand Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Rihand</td><td class="col4">Dudhi</td><td class="col5">Sonbhadra</td><td class="col6">Uttar Pradesh</td><td class="col7">Ganga</td><td class="col8">Completed</td><td class="col9">1962</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">932</td><td class="col12">91.46</td><td class="col13">10608.32</td>
    </tr>
    <tr class="row31">
    <th class="col0">31</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D02080&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Indira_Sagar_(NHDC)_Dam_D02080" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D02080&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Indira_Sagar_(NHDC)_Dam_D02080">Indira Sagar (NHDC) Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Narmada</td><td class="col4">Khandwa</td><td class="col5">East Nimar</td><td class="col6">Madhya Pradesh</td><td class="col7">Narmada</td><td class="col8">Completed</td><td class="col9">2006</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">654</td><td class="col12">91.4</td><td class="col13">12220</td>
    </tr>
    <tr class="row32">
    <th class="col0">32</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D02976&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Warna_Dam_D02976" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D02976&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Warna_Dam_D02976">Warna Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Varna</td><td class="col4">Shahuwadi</td><td class="col5">Kolhapur</td><td class="col6">Maharashtra</td><td class="col7">Krishna</td><td class="col8">Completed</td><td class="col9">2000</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">1580</td><td class="col12">88.8</td><td class="col13">974.188</td>
    </tr>
    <tr class="row33">
    <th class="col0">33</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D02993&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Bhatsa_Dam_D02993" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D02993&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Bhatsa_Dam_D02993">Bhatsa Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Bhatsa and chorna</td><td class="col4">Shahapur</td><td class="col5">Thane</td><td class="col6">Maharashtra</td><td class="col7">West flowing rivers from Tapi to Tadri</td><td class="col8">Completed</td><td class="col9">1983</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">959</td><td class="col12">88.5</td><td class="col13">976.1</td>
    </tr>
    <tr class="row34">
    <th class="col0">34</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00755&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Pillur_Dam_D00755" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00755&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Pillur_Dam_D00755">Pillur Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Bhavani</td><td class="col4">Mettuppalaiyam</td><td class="col5">Coimbatore</td><td class="col6">Tamil Nadu</td><td class="col7">Cauvery</td><td class="col8">Completed</td><td class="col9">1967</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">357</td><td class="col12">88</td><td class="col13">44.4</td>
    </tr>
    <tr class="row35">
    <th class="col0">35</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00785&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Upper_Kodayar_Dam_D00785" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00785&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Upper_Kodayar_Dam_D00785">Upper Kodayar Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Kodayar</td><td class="col4">Kalkulam</td><td class="col5">Kanniyakumari</td><td class="col6">Tamil Nadu</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1972</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">166</td><td class="col12">88</td><td class="col13">98.51</td>
    </tr>
    <tr class="row36">
    <th class="col0">36</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01063&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=_Hasdeo_Bango_(Minimata)_Dam_D01063" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01063&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=_Hasdeo_Bango_(Minimata)_Dam_D01063">Hasdeo Bango (Minimata) Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Hasdeo</td><td class="col4">Katghora</td><td class="col5">Korba</td><td class="col6">Chhattisgarh</td><td class="col7">Mahanadi</td><td class="col8">Completed</td><td class="col9">1990</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">554.5</td><td class="col12">87</td><td class="col13">3417</td>
    </tr>
    <tr class="row37">
    <th class="col0">37</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00426&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Jakham_Main_Dam_D00426" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00426&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Jakham_Main_Dam_D00426">Jakham Main Dam</a></td><td class="col2">Irrigation</td><td class="col3">Jakham (mahi)</td><td class="col4">Pratapgarh</td><td class="col5">Pratapgarh</td><td class="col6">Rajasthan</td><td class="col7">Mahi</td><td class="col8">Completed</td><td class="col9">1986</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">253</td><td class="col12">87</td><td class="col13">142.02</td>
    </tr>
    <tr class="row38">
    <th class="col0">38</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01535&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Teesta_-V_(NHPC)_Dam_D01535" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01535&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Teesta_-V_(NHPC)_Dam_D01535">Teesta -V (NHPC) Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Teesta</td><td class="col4">North</td><td class="col5">North</td><td class="col6">Sikkim</td><td class="col7">Brahmaputra</td><td class="col8">Completed</td><td class="col9">2007</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">176.5</td><td class="col12">86.8</td><td class="col13">13.5</td>
    </tr>
    <tr class="row39">
    <th class="col0">39</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D05100&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lower_Ghatghar_Dam_D05100" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D05100&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lower_Ghatghar_Dam_D05100">Lower Ghatghar Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Shahi Nalla</td><td class="col4">Shahapur</td><td class="col5">Thane</td><td class="col6">Maharashtra</td><td class="col7">West flowing rivers from Tapi to Tadri</td><td class="col8">Completed</td><td class="col9">2007</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">449</td><td class="col12">86.14</td><td class="col13">3.21</td>
    </tr>
    <tr class="row40">
    <th class="col0">40</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03104&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Kallada_(Parappar)_(Id)_Dam_D03104" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03104&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Kallada_(Parappar)_(Id)_Dam_D03104">Kallada (Parappar) (Id) Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Kallada</td><td class="col4">Pattanapuram</td><td class="col5">Kollam</td><td class="col6">Kerala</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1986</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">335</td><td class="col12">85.35</td><td class="col13">524</td>
    </tr>
    <tr class="row41">
    <th class="col0">41</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03460&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Madupetty_(Eb)_Dam_D03460" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03460&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Madupetty_(Eb)_Dam_D03460">Madupetty (Eb) Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Palar</td><td class="col4">Devikolam</td><td class="col5">Idukki</td><td class="col6">Kerala</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1957</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">237.74</td><td class="col12">85.34</td><td class="col13">55.4</td>
    </tr>
    <tr class="row42">
    <th class="col0">42</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01007&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Parbati_II_Dam_D01007" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01007&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Parbati_II_Dam_D01007">Parbati II Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Parbati</td><td class="col4">Kullu</td><td class="col5">Kullu</td><td class="col6">Himachal Pradesh</td><td class="col7">Indus up to International Border</td><td class="col8">Under Construction</td><td class="col9"> </td><td class="col10">Gravity &amp; Masonry</td><td class="col11">101.5</td><td class="col12">85</td><td class="col13">6.55</td>
    </tr>
    <tr class="row43">
    <th class="col0">43</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D05615&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Chakra_Dam_D05615" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D05615&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Chakra_Dam_D05615">Chakra Dam</a></td><td class="col2">Irrigation</td><td class="col3">Chakra</td><td class="col4">Hosanagara</td><td class="col5">Shimoga</td><td class="col6">Karnataka</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1985</td><td class="col10">Rockfill</td><td class="col11">570</td><td class="col12">84</td><td class="col13">222.6</td>
    </tr>
    <tr class="row44">
    <th class="col0">44</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03191&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Bandardhara_Dam_D03191" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03191&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Bandardhara_Dam_D03191">Bandardhara Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Paravara</td><td class="col4">Akola</td><td class="col5">Ahmadnagar</td><td class="col6">Maharashtra</td><td class="col7">Godavari</td><td class="col8">Completed</td><td class="col9">1926</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">2717</td><td class="col12">82.35</td><td class="col13">312.6</td>
    </tr>
    <tr class="row45">
    <th class="col0">45</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D05130&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lower_Vaitarna_Dam_D05130" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D05130&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lower_Vaitarna_Dam_D05130">Lower Vaitarna Dam</a></td><td class="col2">Drinking / Water Supply</td><td class="col3">Vaitarna</td><td class="col4">Shahapur</td><td class="col5">Thane</td><td class="col6">Maharashtra</td><td class="col7">West flowing rivers from Tapi to Tadri</td><td class="col8">Completed</td><td class="col9">1954</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">567.07</td><td class="col12">82</td><td class="col13">204.98</td>
    </tr>
    <tr class="row46">
    <th class="col0">46</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01004&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Ukai_Dam_D01004" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01004&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Ukai_Dam_D01004">Ukai Dam</a></td><td class="col2">Flood Control,Hydroelectric,Irrigation</td><td class="col3">Tapi</td><td class="col4">Songadh</td><td class="col5">Tapi</td><td class="col6">Gujarat</td><td class="col7">Tapi</td><td class="col8">Completed</td><td class="col9">1972</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">4927</td><td class="col12">81</td><td class="col13">8510</td>
    </tr>
    <tr class="row47">
    <th class="col0">47</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00771&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Upper_Aliyar_Dam_D00771" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00771&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Upper_Aliyar_Dam_D00771">Upper Aliyar Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Aliyar</td><td class="col4">Pollachi</td><td class="col5">Coimbatore</td><td class="col6">Tamil Nadu</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1971</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">315</td><td class="col12">81</td><td class="col13">26.57</td>
    </tr>
    <tr class="row48">
    <th class="col0">48</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03202&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Aruna_Dam_D03202" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03202&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Aruna_Dam_D03202">Aruna Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Aruna</td><td class="col4">Vaibhavwadi</td><td class="col5">Sindhudurg</td><td class="col6">Maharashtra</td><td class="col7">West flowing rivers from Tapi to Tadri</td><td class="col8"> </td><td class="col9"> </td><td class="col10">Earthen</td><td class="col11">1240</td><td class="col12">80.41</td><td class="col13">93.378</td>
    </tr>
    <tr class="row49">
    <th class="col0">49</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00756&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Upper_Bhavani_Dam_D00756" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00756&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Upper_Bhavani_Dam_D00756">Upper Bhavani Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Bhavani</td><td class="col4">Udagamandalam</td><td class="col5">The Nilgiris</td><td class="col6">Tamil Nadu</td><td class="col7">Cauvery</td><td class="col8">Completed</td><td class="col9">1965</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">419</td><td class="col12">80</td><td class="col13">101.2</td>
    </tr>
    <tr class="row50">
    <th class="col0">50</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D06416&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Pare_Dam_(Pare_HE_project)_D06416" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D06416&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Pare_Dam_(Pare_HE_project)_D06416">Pare Dam (Pare HE project)</a></td><td class="col2"> </td><td class="col3">Dikrong</td><td class="col4"> </td><td class="col5"> </td><td class="col6"> </td><td class="col7"> </td><td class="col8">Completed</td><td class="col9"> </td><td class="col10">Gravity &amp; Masonry</td><td class="col11">152.2</td><td class="col12">78</td><td class="col13">19.63</td>
    </tr>
    </table></div>
    <p>
    <strong>(Source: <a class="urlextern" href="http://59.179.19.250/" rel="nofollow" title="http://59.179.19.250/">India-WRIS WebGIS</a>)</strong>
    </p>
    </div>
    <h2 class="sectionedit3" id="other_links">Other links</h2>
    <div class="level2">
    <ol>
    <li class="level1"><div class="li"> National register of large dams <a class="wikilink2" href="/wiki/doku.php?id=http:www.cwc.nic.in_main_downloads_new_nrld.pdf" rel="nofollow" title="http:www.cwc.nic.in_main_downloads_new_nrld.pdf">Link]</a></div>
    </li>
    <li class="level1"><div class="li"> India-WRIS: Water Resources Projects sub-information system <a class="wikilink2" href="/wiki/doku.php?id=http:59.179.19.250_wrpapp.html" rel="nofollow" title="http:59.179.19.250_wrpapp.html">Link]</a></div>
    </li>
    </ol>
    </div>
    <script type="text/javascript">
        //<![CDATA[ 
    
        function createRequestValue() {
            try{
            var inputNode=document.createElement('input');
            inputNode.setAttribute('type','hidden');
            inputNode.setAttribute('value','yes');
            inputNode.setAttribute('name','dwedit_preview');
            inputNode.setAttribute('id','dwedit_preview');
            var dwform = GetE("dw__editform");
            dwform.appendChild(inputNode);
            }catch(e) { alert(e); }
        }
    //]]> 
     </script>
    <!-- end rendered wiki content -->
    <div class="clearer"></div>
    </div>
    <!-- end div id bodyContent -->
    </div>
    <!-- end div id=content -->
    <!-- start div id=head -->
    <div class="noprint" id="head">
    <div id="p-personal">
    <ul>
    <li id="pt-login"><a href="/wiki/doku.php?id=large_dams_in_india&amp;do=login" rel="nofollow">Log In</a></li>
    </ul>
    </div>
    <!-- start div id=left-navigation -->
    <div id="left-navigation">
    <div class="vectorTabs" id="p-namespaces">
    <ul>
    <li class="selected" id="ca-nstab-main"><a href="/wiki/doku.php?id=large_dams_in_india"><span>Article</span></a></li>
    <li id="ca-talk"><a href="/wiki/doku.php?id=talk:large_dams_in_india"><span>Discussion</span></a></li>
    </ul>
    </div>
    </div>
    <!-- end div id=left-navigation -->
    <!-- start div id=right-navigation -->
    <div id="right-navigation">
    <div class="vectorTabs" id="p-views">
    <ul>
    <li class="selected" id="ca-view"><a href="/wiki/doku.php?id=large_dams_in_india"><span>Read</span></a></li>
    <li id="ca-edit"><a accesskey="E" href="/wiki/doku.php?id=large_dams_in_india&amp;do=edit&amp;rev=1629789147" title="[ALT+E]"><span>Show pagesource</span></a></li>
    <li id="ca-history"><a accesskey="O" href="/wiki/doku.php?id=large_dams_in_india&amp;do=revisions" title="[ALT+O]"><span>Old revisions</span></a></li>
    </ul>
    </div>
    <div id="p-search">
    <h5>
    <label for="qsearch__in">Search</label>
    </h5>
    <form accept-charset="utf-8" action="/wiki/doku.php?id=start" id="dw__search" name="dw__search">
    <input name="do" type="hidden" value="search"/>
    <div id="simpleSearch">
    <input accesskey="f" id="qsearch__in" name="id" type="text" value=""/>
    <button id="searchButton" name="button" title="Search for this text" type="submit"> </button>
    </div>
    <div class="ajax_qsearch JSpopup" id="qsearch__out"></div>
    </form>
    </div>
    </div>
    <!-- end div id=right-navigation -->
    </div>
    <!-- end div id=head -->
    <!-- start panel/sidebar -->
    <div class="noprint" id="panel">
    <!-- start logo -->
    <div id="p-logo">
    <a accesskey="h" href="/wiki/doku.php?id=start" style="background-image:url(/wiki/lib/tpl/vector/user/logo.png);" title="[ALT+H]"></a>
    </div>
    <!-- end logo -->
    <div class="portal" id="p-navigation">
    <h5>Navigation</h5>
    <div class="body">
    <div class="dokuwiki">
    <p>
    <span class="curid"><a class="wikilink1" href="/wiki/doku.php?id=wris_publications" title="wris_publications">WRIS publications</a></span>
    </p>
    <p>
    <a class="wikilink1" href="/wiki/doku.php?id=recent_updates" title="recent_updates">Recent updates</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=help" title="help">Help</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=sitemap" title="sitemap">Sitemap</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=related_links" title="related_links">Related Links</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=feedback" title="feedback">Feedback</a>
    </p>
    <hr/>
    <p>
    <a class="wikilink1" href="/wiki/doku.php?id=india_s_water_wealth" title="india_s_water_wealth">India's Water Wealth</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=river_basins" title="river_basins">River Basins</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=state" title="state">State</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=river_info" title="river_info">Rivers in India</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=major_medium_irrigation_projects" title="major_medium_irrigation_projects">Major &amp; Medium Irrigation Projects</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=headworks_dam_barrage_weir_anicut_lift" title="headworks_dam_barrage_weir_anicut_lift">Headworks</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=hydro_electric_projects" title="hydro_electric_projects">Hydro Electric Projects</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=multi_purpose_projects" title="multi_purpose_projects">Multi PurposeProjects</a>
    </p>
    <p>
    <a class="wikilink1" href="/wiki/doku.php?id=inter_state_projects" title="inter_state_projects">Inter State Projects</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=irrigation_and_power_complexes" title="irrigation_and_power_complexes">Irrigation and Power Complexes</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=accelerated_irrigation_benefit_programme" title="accelerated_irrigation_benefit_programme">AIBP</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=command_area_development_programme" title="command_area_development_programme">CADWM</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=evaluation_studies_for_irrigation_projects_done_by_cwc" title="evaluation_studies_for_irrigation_projects_done_by_cwc">Evaluation Studies for Irrigation Projects</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=cwc_hydro-meteorological_sites" title="cwc_hydro-meteorological_sites">River Monitoring Sites</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=flood_management" title="flood_management">Flood Management</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=cwc_national_flood_forecasting_network" title="cwc_national_flood_forecasting_network">CWC National Flood Forecasting Network</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=river_water_quality_monitoring" title="river_water_quality_monitoring">River Water Quality Monitoring</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=cgwb_ground_water_resources" title="cgwb_ground_water_resources">CGWB Ground Water Resources</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=inland_waterways" title="inland_waterways">Inland Waterways</a>
    </p>
    <p>
    <a class="wikilink1" href="/wiki/doku.php?id=inter_basin_water_transfer_links" title="inter_basin_water_transfer_links">Inter Basin Water Transfer Links</a>
    </p>
    <p>
    <a class="wikilink1" href="/wiki/doku.php?id=legal_instruments" title="legal_instruments">Legal Instruments on River in India</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=inter_state_disputes" title="inter_state_disputes">Inter StateDisputes</a>
    </p>
    <p>
    <a class="wikilink1" href="/wiki/doku.php?id=large_dams_in_india" title="large_dams_in_india">Large Dams in India</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=water_tourism" title="water_tourism">Water Tourism</a><br/>
    <a class="wikilink1" href="/wiki/doku.php?id=glossary_of_terms" title="glossary_of_terms">Glossary</a>
    </p>
    </div>
    </div>
    </div>
    <div class="portal" id="p-coll-print_export">
    <h5>Print/export</h5>
    <div class="body">
    <div class="dokuwiki">
    <ul>
    <li id="t-print"><a href="/wiki/doku.php?id=large_dams_in_india&amp;rev=1629789147&amp;vecdo=print" rel="nofollow">Printable version</a></li>
    </ul>
    </div>
    </div>
    </div>
    <div class="portal" id="p-tb">
    <h5>Tools</h5>
    <div class="body">
    <div class="dokuwiki">
    <ul>
    <li id="t-whatlinkshere"><a href="/wiki/doku.php?id=large_dams_in_india&amp;do=backlink">What links here</a></li>
    <li id="t-recentchanges"><a href="/wiki/doku.php?id=start&amp;do=recent" rel="nofollow">Recent Changes</a></li>
    <li id="t-upload"><a href="/wiki/doku.php?id=start&amp;do=media" rel="nofollow">Media Manager</a></li>
    <li id="t-special"><a href="/wiki/doku.php?id=start&amp;do=index" rel="nofollow">Sitemap</a></li>
    <li id="t-permanent"><a href="/wiki/doku.php?id=large_dams_in_india&amp;rev=1629789147" rel="nofollow">Permanent link</a></li>
    <li id="t-cite"><a href="/wiki/doku.php?id=large_dams_in_india&amp;rev=1629789147&amp;vecdo=cite" rel="nofollow">Cite this page</a></li>
    </ul>
    </div>
    </div>
    </div>
    <div class="portal" id="p-qrcode">
    <h5>QR Code</h5>
    <div class="body">
    <div class="dokuwiki">
    <span id="t-qrcode"><img alt="QR Code large_dams_in_india (generated for current page)" src="http://api.qrserver.com/v1/create-qr-code/?data=http%3A%2F%2F10.247.136.5%2Fwiki%2Fdoku.php%3Fid%3Dlarge_dams_in_india&amp;size=130x130&amp;margin=0&amp;bgcolor=f3f3f3" title="Current page as QR Code (scan for easy mobile access)"/></span>
    </div>
    </div>
    </div>
    </div>
    <!-- end panel/sidebar -->
    </div>
    <!-- end page-container -->
    <!-- start footer -->
    <div class="noprint" id="footer">
    <ul id="footer-info">
    <li id="footer-info-lastmod">
    <bdi>large_dams_in_india.txt</bdi> · Last modified: 2021/08/24 12:42 (external edit)<br/>
    </li>
    <li id="footer-info-copyright">
    <div class="dokuwiki"><div class="license">Except where otherwise noted, content on this wiki is licensed under the following license: <bdi><a class="urlextern" href="http://creativecommons.org/licenses/by-sa/4.0/" rel="license">CC Attribution-Share Alike 4.0 International</a></bdi></div></div>
    </li>
    </ul>
    <ul id="footer-places">
    <li>
    <a href="/wiki/feed.php" rel="nofollow" target="_blank" title="Recent changes"><img alt="Recent changes" border="0" height="15" src="/wiki/lib/tpl/vector/static/img/button-rss.png" title="Recent changes" width="80"/></a>
    <a href="https://www.dokuwiki.org/template:vector" rel="nofollow" target="_blank" title="vector template for DokuWiki"><img alt="vector template for DokuWiki" border="0" height="15" src="/wiki/lib/tpl/vector/static/img/button-vector.png" title="vector template for DokuWiki" width="80"/></a>
    <a href="https://www.dokuwiki.org/" rel="nofollow" target="_blank" title="DokuWiki"><img alt="DokuWiki" border="0" height="15" src="/wiki/lib/tpl/vector/static/img/button-dw.png" title="DokuWiki" width="80"/></a>
    <a href="http://validator.w3.org/check/referer" rel="nofollow" target="_blank" title="Valid XHTML"><img alt="Valid XHTML" border="0" height="15" src="/wiki/lib/tpl/vector/static/img/button-xhtml.png" title="Valid XHTML" width="80"/></a>
    </li>
    </ul>
    <div style="clearer"></div>
    </div>
    <!-- end footer -->
    <img alt="" height="1" src="/wiki/lib/exe/indexer.php?id=large_dams_in_india&amp;1760505460" width="2"/>
    </body>
    </html>
    
    


```python
table = soup.find("table")
print (table)
```

    <table class="inline">
    <thead>
    <tr class="row0">
    <th class="col0">#</th><th class="col1">Name</th><th class="col2">Purpose</th><th class="col3">River</th><th class="col4">Nearest City</th><th class="col5">District</th><th class="col6">State</th><th class="col7">Basin</th><th class="col8">Status</th><th class="col9">Completion Year</th><th class="col10">Type</th><th class="col11">Length (m)</th><th class="col12">Max Height above Foundation (m)</th><th class="col13">Design Gross Storage Capacity (MCM)</th>
    </tr>
    </thead>
    <tr class="row1">
    <th class="col0">1</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00742&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Tehri_Dam_D00742" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00742&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Tehri_Dam_D00742">Tehri Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Bhagirathi</td><td class="col4">Pratapnagar</td><td class="col5">Tehri Garhwal</td><td class="col6">Uttarakhand</td><td class="col7">Ganga</td><td class="col8">Completed</td><td class="col9">2005</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">575</td><td class="col12">260.5</td><td class="col13">3540</td>
    </tr>
    <tr class="row2">
    <th class="col0">2</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00723&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lakhwar_Dam_D00723" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00723&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lakhwar_Dam_D00723">Lakhwar Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Yamuna</td><td class="col4">Dehradun</td><td class="col5">Dehradun</td><td class="col6">Uttarakhand</td><td class="col7">Ganga</td><td class="col8">Proposed</td><td class="col9"> </td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">451</td><td class="col12">204</td><td class="col13">587.84</td>
    </tr>
    <tr class="row3">
    <th class="col0">3</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03331&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Idukki_(Eb)/Idukki_Arch_Dam_D03331" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03331&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Idukki_(Eb)/Idukki_Arch_Dam_D03331">Idukki (Eb)/Idukki Arch Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Periyar</td><td class="col4">Todupulai</td><td class="col5">Idukki</td><td class="col6">Kerala</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1974</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">366</td><td class="col12">169</td><td class="col13">1998.57</td>
    </tr>
    <tr class="row4">
    <th class="col0">4</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00993&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Bhakra_Dam_D00993" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00993&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Bhakra_Dam_D00993">Bhakra Dam</a></td><td class="col2">Hydroelectric,Irrigation,Recreation</td><td class="col3">Satluj</td><td class="col4">Bilaspur</td><td class="col5">Bilaspur</td><td class="col6">Himachal Pradesh</td><td class="col7">Indus up to International Border</td><td class="col8">Completed</td><td class="col9">1963</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">518.16</td><td class="col12">167.64</td><td class="col13">9867.84</td>
    </tr>
    <tr class="row5">
    <th class="col0">5</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D02983&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Pakal_Dul_Dam_D02983" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D02983&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Pakal_Dul_Dam_D02983">Pakal Dul Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Marusudar</td><td class="col4">Kishtwar</td><td class="col5">Kishtwar</td><td class="col6">Jammu &amp; Kashmir</td><td class="col7">Indus up to International Border</td><td class="col8">Proposed</td><td class="col9"> </td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">305</td><td class="col12">167</td><td class="col13">.1254</td>
    </tr>
    <tr class="row6">
    <th class="col0">6</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03023&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Sardar_Sarover_Gujarat_Dam_D03023" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03023&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Sardar_Sarover_Gujarat_Dam_D03023">Sardar Sarover Gujarat Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Narmada</td><td class="col4">Rajpipla</td><td class="col5">Narmada</td><td class="col6">Gujarat</td><td class="col7">Narmada</td><td class="col8">Completed</td><td class="col9"> </td><td class="col10">Gravity &amp; Masonry</td><td class="col11">1210</td><td class="col12">163</td><td class="col13">9500</td>
    </tr>
    <tr class="row7">
    <th class="col0">7</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00557&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Srisailam_(N.S.R.S.P)_Dam_D00557" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00557&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Srisailam_(N.S.R.S.P)_Dam_D00557">Srisailam (N.S.R.S.P) Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Krishna</td><td class="col4">Nandikotkur</td><td class="col5">Kurnool</td><td class="col6">Telangana</td><td class="col7">Krishna</td><td class="col8">Completed</td><td class="col9">1984</td><td class="col10">Earthen</td><td class="col11">512</td><td class="col12">145</td><td class="col13">8724.88</td>
    </tr>
    <tr class="row8">
    <th class="col0">8</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03535&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Ranjit_Sagar_Dam_D03535" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03535&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Ranjit_Sagar_Dam_D03535">Ranjit Sagar Dam</a></td><td class="col2">Flood Control,Hydroelectric,Irrigation</td><td class="col3">Ravi</td><td class="col4">Pathankot</td><td class="col5">Kathua</td><td class="col6">Punjab</td><td class="col7">Indus up to International Border</td><td class="col8">Completed</td><td class="col9">1999</td><td class="col10">Earthen</td><td class="col11">617</td><td class="col12">145</td><td class="col13">3280</td>
    </tr>
    <tr class="row9">
    <th class="col0">9</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03079&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Baglihar_Dam_D03079" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03079&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Baglihar_Dam_D03079">Baglihar Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">CHENAB</td><td class="col4">Ramban</td><td class="col5">Ramban</td><td class="col6">Jammu &amp; Kashmir</td><td class="col7">Indus up to International Border</td><td class="col8">Completed</td><td class="col9">2009</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">364.362</td><td class="col12">143</td><td class="col13">475</td>
    </tr>
    <tr class="row10">
    <th class="col0">10</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00589&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Chamera_I_Dam_D00589" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00589&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Chamera_I_Dam_D00589">Chamera I Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Ravi</td><td class="col4">Bhattiyat</td><td class="col5">Chamba</td><td class="col6">Himachal Pradesh</td><td class="col7">Indus up to International Border</td><td class="col8">Completed</td><td class="col9">1994</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">295</td><td class="col12">140</td><td class="col13">242.3</td>
    </tr>
    <tr class="row11">
    <th class="col0">11</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03326&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Cheruthoni_(Eb)_Dam_D03326" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03326&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Cheruthoni_(Eb)_Dam_D03326">Cheruthoni (Eb) Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Cheruthoni</td><td class="col4">Todupulai</td><td class="col5">Idukki</td><td class="col6">Kerala</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1976</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">651</td><td class="col12">138.38</td><td class="col13">1998.57</td>
    </tr>
    <tr class="row12">
    <th class="col0">12</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00579&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Pong_Dam_D00579" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00579&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Pong_Dam_D00579">Pong Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Beas</td><td class="col4">Dera Gopipur</td><td class="col5">Kangra</td><td class="col6">Himachal Pradesh</td><td class="col7">Indus up to International Border</td><td class="col8">Completed</td><td class="col9">1974</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">1950.7</td><td class="col12">132.59</td><td class="col13">8570</td>
    </tr>
    <tr class="row13">
    <th class="col0">13</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01161&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Jamrani_Dam_D01161" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01161&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Jamrani_Dam_D01161">Jamrani Dam</a></td><td class="col2">Irrigation</td><td class="col3">Gola</td><td class="col4">Naini Tal</td><td class="col5">Nainital</td><td class="col6">Uttarakhand</td><td class="col7">Ganga</td><td class="col8">Proposed</td><td class="col9">1990</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">465</td><td class="col12">130.6</td><td class="col13"> </td>
    </tr>
    <tr class="row14">
    <th class="col0">14</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00004&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Subansiri_Lower_HE_(Nhpc)_Dam_D00004" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00004&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Subansiri_Lower_HE_(Nhpc)_Dam_D00004">Subansiri Lower HE (Nhpc) Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Subansiri</td><td class="col4">Lower Subansiri</td><td class="col5">Lower Subansiri</td><td class="col6">Arunanchal Pradesh</td><td class="col7">Brahmaputra</td><td class="col8">Under Construction</td><td class="col9">2014</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">284</td><td class="col12">130</td><td class="col13">1643</td>
    </tr>
    <tr class="row15">
    <th class="col0">15</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01125&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Ramganga_Dam_D01125" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01125&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Ramganga_Dam_D01125">Ramganga Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Ramganga</td><td class="col4">Lansdowne</td><td class="col5">Garhwal</td><td class="col6">Uttarakhand</td><td class="col7">Ganga</td><td class="col8">Completed</td><td class="col9">1974</td><td class="col10">Earthen</td><td class="col11">630</td><td class="col12">127.5</td><td class="col13">2448</td>
    </tr>
    <tr class="row16">
    <th class="col0">16</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00690&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Nagarjuna_Sagar_Dam_D00690" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00690&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Nagarjuna_Sagar_Dam_D00690">Nagarjuna Sagar Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Krishna</td><td class="col4">Guruzala</td><td class="col5">Guntur</td><td class="col6">Telangana</td><td class="col7">Krishna</td><td class="col8">Completed</td><td class="col9">1974</td><td class="col10">Earthen</td><td class="col11">4865</td><td class="col12">124.66</td><td class="col13">11553</td>
    </tr>
    <tr class="row17">
    <th class="col0">17</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03369&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Kakki_(Eb)_Dam_D03369" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03369&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Kakki_(Eb)_Dam_D03369">Kakki (Eb) Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Kakki</td><td class="col4">Rani</td><td class="col5">Pathanamthitta</td><td class="col6">Kerala</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1966</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">336.19</td><td class="col12">116.13</td><td class="col13">454.07</td>
    </tr>
    <tr class="row18">
    <th class="col0">18</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01205&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Nagi_Dam_D01205" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01205&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Nagi_Dam_D01205">Nagi Dam</a></td><td class="col2">Irrigation</td><td class="col3">Nagi</td><td class="col4">Jamui</td><td class="col5">Jamui</td><td class="col6">Bihar</td><td class="col7">Ganga</td><td class="col8">Completed</td><td class="col9">1958</td><td class="col10">Earthen</td><td class="col11">1884</td><td class="col12">113.5</td><td class="col13">108</td>
    </tr>
    <tr class="row19">
    <th class="col0">19</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03068&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Salal_(Rockfill_And_Concrete_)_Dam_D03068" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03068&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Salal_(Rockfill_And_Concrete_)_Dam_D03068">Salal (Rockfill And Concrete ) Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Chenab</td><td class="col4">Gool Gulab Garh</td><td class="col5">Reasi</td><td class="col6">Jammu &amp; Kashmir</td><td class="col7">Indus up to International Border</td><td class="col8">Completed</td><td class="col9">1986</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">487</td><td class="col12">113</td><td class="col13">28.5</td>
    </tr>
    <tr class="row20">
    <th class="col0">20</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D05812&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lakhya_Dam_D05812" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D05812&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lakhya_Dam_D05812">Lakhya Dam</a></td><td class="col2">Drinking / Water Supply</td><td class="col3">Lakhya hole</td><td class="col4">Mudigere</td><td class="col5">Chikmagalur</td><td class="col6">Karnataka</td><td class="col7">Krishna</td><td class="col8">Completed</td><td class="col9">1994</td><td class="col10">Earthen</td><td class="col11">1048</td><td class="col12">108</td><td class="col13">273.79</td>
    </tr>
    <tr class="row21">
    <th class="col0">21</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00314&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Sholayar_Dam_D00314" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00314&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Sholayar_Dam_D00314">Sholayar Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Sholayar</td><td class="col4">Pollachi</td><td class="col5">Coimbatore</td><td class="col6">Tamil Nadu</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1971</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">1244.18</td><td class="col12">105.16</td><td class="col13">152.48</td>
    </tr>
    <tr class="row22">
    <th class="col0">22</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D05104&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Koyna_Dam_D05104" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D05104&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Koyna_Dam_D05104">Koyna Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Koyna</td><td class="col4">Patan</td><td class="col5">Satara</td><td class="col6">Maharashtra</td><td class="col7">Krishna</td><td class="col8">Completed</td><td class="col9">1964</td><td class="col10">Earthen</td><td class="col11">807.72</td><td class="col12">103.02</td><td class="col13">2980.69</td>
    </tr>
    <tr class="row23">
    <th class="col0">23</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03183&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Idamalayar_(Eb)_Dam_D03183" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03183&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Idamalayar_(Eb)_Dam_D03183">Idamalayar (Eb) Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Idamalayar</td><td class="col4">Devikolam</td><td class="col5">Idukki</td><td class="col6">Kerala</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1985</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">373</td><td class="col12">102</td><td class="col13">1208.23</td>
    </tr>
    <tr class="row24">
    <th class="col0">24</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D04595&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Supa_Dam_D04595" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D04595&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Supa_Dam_D04595">Supa Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Kali Nadi</td><td class="col4">Supa</td><td class="col5">Uttara Kannada</td><td class="col6">Karnataka</td><td class="col7">West flowing rivers from Tapi to Tadri</td><td class="col8">Completed</td><td class="col9">1987</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">331.29</td><td class="col12">101</td><td class="col13">4178</td>
    </tr>
    <tr class="row25">
    <th class="col0">25</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01195&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Karjan_Dam_D01195" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01195&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Karjan_Dam_D01195">Karjan Dam</a></td><td class="col2">Irrigation</td><td class="col3">Karjan</td><td class="col4">Rajpipla</td><td class="col5">Narmada</td><td class="col6">Gujarat</td><td class="col7">Narmada</td><td class="col8">Completed</td><td class="col9">1987</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">903</td><td class="col12">100</td><td class="col13">630</td>
    </tr>
    <tr class="row26">
    <th class="col0">26</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03334&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Kulamavu_(Eb)_Dam_D03334" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03334&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Kulamavu_(Eb)_Dam_D03334">Kulamavu (Eb) Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Kilivillithode</td><td class="col4">Todupulai</td><td class="col5">Idukki</td><td class="col6">Kerala</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1977</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">385</td><td class="col12">100</td><td class="col13">1998.57</td>
    </tr>
    <tr class="row27">
    <th class="col0">27</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00823&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Koteshwar_Dam_D00823" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00823&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Koteshwar_Dam_D00823">Koteshwar Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Bhagirathi</td><td class="col4">Pratapnagar</td><td class="col5">Tehri Garhwal</td><td class="col6">Uttarakhand</td><td class="col7">Ganga</td><td class="col8">Completed</td><td class="col9"> </td><td class="col10">Gravity &amp; Masonry</td><td class="col11">300.5</td><td class="col12">97.5</td><td class="col13">88.9</td>
    </tr>
    <tr class="row28">
    <th class="col0">28</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00654&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lower_:_PPSP_Dam_D00654" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00654&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lower_:_PPSP_Dam_D00654">Lower : PPSP Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Kistobazar nalla</td><td class="col4">Puruliya</td><td class="col5">Puruliya</td><td class="col6">West Bengal</td><td class="col7">Subarnarekha</td><td class="col8">Completed</td><td class="col9"> </td><td class="col10">Rockfill</td><td class="col11">310</td><td class="col12">95</td><td class="col13">16</td>
    </tr>
    <tr class="row29">
    <th class="col0">29</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01456&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Doyang_Hep_Dam_D01456" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01456&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Doyang_Hep_Dam_D01456">Doyang Hep Dam</a></td><td class="col2">Hydroelectric,Drinking / Water Supply</td><td class="col3">Doyang</td><td class="col4">Wokha</td><td class="col5">Wokha</td><td class="col6">Nagaland</td><td class="col7">Brahmaputra</td><td class="col8">Completed</td><td class="col9"> </td><td class="col10">Earthen</td><td class="col11">462</td><td class="col12">92</td><td class="col13">565</td>
    </tr>
    <tr class="row30">
    <th class="col0">30</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00726&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Rihand_Dam_D00726" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00726&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Rihand_Dam_D00726">Rihand Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Rihand</td><td class="col4">Dudhi</td><td class="col5">Sonbhadra</td><td class="col6">Uttar Pradesh</td><td class="col7">Ganga</td><td class="col8">Completed</td><td class="col9">1962</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">932</td><td class="col12">91.46</td><td class="col13">10608.32</td>
    </tr>
    <tr class="row31">
    <th class="col0">31</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D02080&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Indira_Sagar_(NHDC)_Dam_D02080" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D02080&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Indira_Sagar_(NHDC)_Dam_D02080">Indira Sagar (NHDC) Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Narmada</td><td class="col4">Khandwa</td><td class="col5">East Nimar</td><td class="col6">Madhya Pradesh</td><td class="col7">Narmada</td><td class="col8">Completed</td><td class="col9">2006</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">654</td><td class="col12">91.4</td><td class="col13">12220</td>
    </tr>
    <tr class="row32">
    <th class="col0">32</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D02976&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Warna_Dam_D02976" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D02976&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Warna_Dam_D02976">Warna Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Varna</td><td class="col4">Shahuwadi</td><td class="col5">Kolhapur</td><td class="col6">Maharashtra</td><td class="col7">Krishna</td><td class="col8">Completed</td><td class="col9">2000</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">1580</td><td class="col12">88.8</td><td class="col13">974.188</td>
    </tr>
    <tr class="row33">
    <th class="col0">33</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D02993&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Bhatsa_Dam_D02993" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D02993&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Bhatsa_Dam_D02993">Bhatsa Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Bhatsa and chorna</td><td class="col4">Shahapur</td><td class="col5">Thane</td><td class="col6">Maharashtra</td><td class="col7">West flowing rivers from Tapi to Tadri</td><td class="col8">Completed</td><td class="col9">1983</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">959</td><td class="col12">88.5</td><td class="col13">976.1</td>
    </tr>
    <tr class="row34">
    <th class="col0">34</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00755&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Pillur_Dam_D00755" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00755&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Pillur_Dam_D00755">Pillur Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Bhavani</td><td class="col4">Mettuppalaiyam</td><td class="col5">Coimbatore</td><td class="col6">Tamil Nadu</td><td class="col7">Cauvery</td><td class="col8">Completed</td><td class="col9">1967</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">357</td><td class="col12">88</td><td class="col13">44.4</td>
    </tr>
    <tr class="row35">
    <th class="col0">35</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00785&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Upper_Kodayar_Dam_D00785" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00785&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Upper_Kodayar_Dam_D00785">Upper Kodayar Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Kodayar</td><td class="col4">Kalkulam</td><td class="col5">Kanniyakumari</td><td class="col6">Tamil Nadu</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1972</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">166</td><td class="col12">88</td><td class="col13">98.51</td>
    </tr>
    <tr class="row36">
    <th class="col0">36</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01063&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=_Hasdeo_Bango_(Minimata)_Dam_D01063" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01063&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=_Hasdeo_Bango_(Minimata)_Dam_D01063">Hasdeo Bango (Minimata) Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Hasdeo</td><td class="col4">Katghora</td><td class="col5">Korba</td><td class="col6">Chhattisgarh</td><td class="col7">Mahanadi</td><td class="col8">Completed</td><td class="col9">1990</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">554.5</td><td class="col12">87</td><td class="col13">3417</td>
    </tr>
    <tr class="row37">
    <th class="col0">37</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00426&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Jakham_Main_Dam_D00426" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00426&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Jakham_Main_Dam_D00426">Jakham Main Dam</a></td><td class="col2">Irrigation</td><td class="col3">Jakham (mahi)</td><td class="col4">Pratapgarh</td><td class="col5">Pratapgarh</td><td class="col6">Rajasthan</td><td class="col7">Mahi</td><td class="col8">Completed</td><td class="col9">1986</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">253</td><td class="col12">87</td><td class="col13">142.02</td>
    </tr>
    <tr class="row38">
    <th class="col0">38</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01535&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Teesta_-V_(NHPC)_Dam_D01535" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01535&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Teesta_-V_(NHPC)_Dam_D01535">Teesta -V (NHPC) Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Teesta</td><td class="col4">North</td><td class="col5">North</td><td class="col6">Sikkim</td><td class="col7">Brahmaputra</td><td class="col8">Completed</td><td class="col9">2007</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">176.5</td><td class="col12">86.8</td><td class="col13">13.5</td>
    </tr>
    <tr class="row39">
    <th class="col0">39</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D05100&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lower_Ghatghar_Dam_D05100" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D05100&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lower_Ghatghar_Dam_D05100">Lower Ghatghar Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Shahi Nalla</td><td class="col4">Shahapur</td><td class="col5">Thane</td><td class="col6">Maharashtra</td><td class="col7">West flowing rivers from Tapi to Tadri</td><td class="col8">Completed</td><td class="col9">2007</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">449</td><td class="col12">86.14</td><td class="col13">3.21</td>
    </tr>
    <tr class="row40">
    <th class="col0">40</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03104&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Kallada_(Parappar)_(Id)_Dam_D03104" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03104&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Kallada_(Parappar)_(Id)_Dam_D03104">Kallada (Parappar) (Id) Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Kallada</td><td class="col4">Pattanapuram</td><td class="col5">Kollam</td><td class="col6">Kerala</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1986</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">335</td><td class="col12">85.35</td><td class="col13">524</td>
    </tr>
    <tr class="row41">
    <th class="col0">41</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03460&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Madupetty_(Eb)_Dam_D03460" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03460&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Madupetty_(Eb)_Dam_D03460">Madupetty (Eb) Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Palar</td><td class="col4">Devikolam</td><td class="col5">Idukki</td><td class="col6">Kerala</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1957</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">237.74</td><td class="col12">85.34</td><td class="col13">55.4</td>
    </tr>
    <tr class="row42">
    <th class="col0">42</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01007&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Parbati_II_Dam_D01007" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01007&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Parbati_II_Dam_D01007">Parbati II Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Parbati</td><td class="col4">Kullu</td><td class="col5">Kullu</td><td class="col6">Himachal Pradesh</td><td class="col7">Indus up to International Border</td><td class="col8">Under Construction</td><td class="col9"> </td><td class="col10">Gravity &amp; Masonry</td><td class="col11">101.5</td><td class="col12">85</td><td class="col13">6.55</td>
    </tr>
    <tr class="row43">
    <th class="col0">43</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D05615&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Chakra_Dam_D05615" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D05615&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Chakra_Dam_D05615">Chakra Dam</a></td><td class="col2">Irrigation</td><td class="col3">Chakra</td><td class="col4">Hosanagara</td><td class="col5">Shimoga</td><td class="col6">Karnataka</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1985</td><td class="col10">Rockfill</td><td class="col11">570</td><td class="col12">84</td><td class="col13">222.6</td>
    </tr>
    <tr class="row44">
    <th class="col0">44</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03191&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Bandardhara_Dam_D03191" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03191&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Bandardhara_Dam_D03191">Bandardhara Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Paravara</td><td class="col4">Akola</td><td class="col5">Ahmadnagar</td><td class="col6">Maharashtra</td><td class="col7">Godavari</td><td class="col8">Completed</td><td class="col9">1926</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">2717</td><td class="col12">82.35</td><td class="col13">312.6</td>
    </tr>
    <tr class="row45">
    <th class="col0">45</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D05130&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lower_Vaitarna_Dam_D05130" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D05130&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Lower_Vaitarna_Dam_D05130">Lower Vaitarna Dam</a></td><td class="col2">Drinking / Water Supply</td><td class="col3">Vaitarna</td><td class="col4">Shahapur</td><td class="col5">Thane</td><td class="col6">Maharashtra</td><td class="col7">West flowing rivers from Tapi to Tadri</td><td class="col8">Completed</td><td class="col9">1954</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">567.07</td><td class="col12">82</td><td class="col13">204.98</td>
    </tr>
    <tr class="row46">
    <th class="col0">46</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D01004&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Ukai_Dam_D01004" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D01004&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Ukai_Dam_D01004">Ukai Dam</a></td><td class="col2">Flood Control,Hydroelectric,Irrigation</td><td class="col3">Tapi</td><td class="col4">Songadh</td><td class="col5">Tapi</td><td class="col6">Gujarat</td><td class="col7">Tapi</td><td class="col8">Completed</td><td class="col9">1972</td><td class="col10">Earthen / Gravity &amp; Masonry</td><td class="col11">4927</td><td class="col12">81</td><td class="col13">8510</td>
    </tr>
    <tr class="row47">
    <th class="col0">47</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00771&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Upper_Aliyar_Dam_D00771" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00771&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Upper_Aliyar_Dam_D00771">Upper Aliyar Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Aliyar</td><td class="col4">Pollachi</td><td class="col5">Coimbatore</td><td class="col6">Tamil Nadu</td><td class="col7">West flowing rivers from Tadri to Kanyakumari</td><td class="col8">Completed</td><td class="col9">1971</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">315</td><td class="col12">81</td><td class="col13">26.57</td>
    </tr>
    <tr class="row48">
    <th class="col0">48</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D03202&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Aruna_Dam_D03202" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D03202&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Aruna_Dam_D03202">Aruna Dam</a></td><td class="col2">Hydroelectric,Irrigation</td><td class="col3">Aruna</td><td class="col4">Vaibhavwadi</td><td class="col5">Sindhudurg</td><td class="col6">Maharashtra</td><td class="col7">West flowing rivers from Tapi to Tadri</td><td class="col8"> </td><td class="col9"> </td><td class="col10">Earthen</td><td class="col11">1240</td><td class="col12">80.41</td><td class="col13">93.378</td>
    </tr>
    <tr class="row49">
    <th class="col0">49</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D00756&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Upper_Bhavani_Dam_D00756" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D00756&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Upper_Bhavani_Dam_D00756">Upper Bhavani Dam</a></td><td class="col2">Hydroelectric</td><td class="col3">Bhavani</td><td class="col4">Udagamandalam</td><td class="col5">The Nilgiris</td><td class="col6">Tamil Nadu</td><td class="col7">Cauvery</td><td class="col8">Completed</td><td class="col9">1965</td><td class="col10">Gravity &amp; Masonry</td><td class="col11">419</td><td class="col12">80</td><td class="col13">101.2</td>
    </tr>
    <tr class="row50">
    <th class="col0">50</th><td class="col1"><a class="urlextern" href="http://59.179.19.250/wrpinfo/wiki1.php?show=D06416&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Pare_Dam_(Pare_HE_project)_D06416" rel="nofollow" title="http://59.179.19.250/wrpinfo/wiki1.php?show=D06416&amp;str2=http://59.179.19.250/wrpinfo/index.php?title=Pare_Dam_(Pare_HE_project)_D06416">Pare Dam (Pare HE project)</a></td><td class="col2"> </td><td class="col3">Dikrong</td><td class="col4"> </td><td class="col5"> </td><td class="col6"> </td><td class="col7"> </td><td class="col8">Completed</td><td class="col9"> </td><td class="col10">Gravity &amp; Masonry</td><td class="col11">152.2</td><td class="col12">78</td><td class="col13">19.63</td>
    </tr>
    </table>
    


```python
# Read the HTML table into a pandas DataFrame
df = pd.read_html(str(table))
df

```

    C:\Users\sukan\AppData\Local\Temp\ipykernel_26364\1219735312.py:2: FutureWarning: Passing literal html to 'read_html' is deprecated and will be removed in a future version. To read from a literal string, wrap it in a 'StringIO' object.
      df = pd.read_html(str(table))
    




    [     #                                Name  \
     0    1                           Tehri Dam   
     1    2                         Lakhwar Dam   
     2    3         Idukki (Eb)/Idukki Arch Dam   
     3    4                          Bhakra Dam   
     4    5                       Pakal Dul Dam   
     5    6          Sardar Sarover Gujarat Dam   
     6    7           Srisailam (N.S.R.S.P) Dam   
     7    8                    Ranjit Sagar Dam   
     8    9                        Baglihar Dam   
     9   10                       Chamera I Dam   
     10  11                 Cheruthoni (Eb) Dam   
     11  12                            Pong Dam   
     12  13                         Jamrani Dam   
     13  14       Subansiri Lower HE (Nhpc) Dam   
     14  15                        Ramganga Dam   
     15  16                 Nagarjuna Sagar Dam   
     16  17                      Kakki (Eb) Dam   
     17  18                            Nagi Dam   
     18  19  Salal (Rockfill And Concrete ) Dam   
     19  20                          Lakhya Dam   
     20  21                        Sholayar Dam   
     21  22                           Koyna Dam   
     22  23                 Idamalayar (Eb) Dam   
     23  24                            Supa Dam   
     24  25                          Karjan Dam   
     25  26                   Kulamavu (Eb) Dam   
     26  27                       Koteshwar Dam   
     27  28                    Lower : PPSP Dam   
     28  29                      Doyang Hep Dam   
     29  30                          Rihand Dam   
     30  31             Indira Sagar (NHDC) Dam   
     31  32                           Warna Dam   
     32  33                          Bhatsa Dam   
     33  34                          Pillur Dam   
     34  35                   Upper Kodayar Dam   
     35  36         Hasdeo Bango (Minimata) Dam   
     36  37                     Jakham Main Dam   
     37  38                Teesta -V (NHPC) Dam   
     38  39                  Lower Ghatghar Dam   
     39  40         Kallada (Parappar) (Id) Dam   
     40  41                  Madupetty (Eb) Dam   
     41  42                      Parbati II Dam   
     42  43                          Chakra Dam   
     43  44                     Bandardhara Dam   
     44  45                  Lower Vaitarna Dam   
     45  46                            Ukai Dam   
     46  47                    Upper Aliyar Dam   
     47  48                           Aruna Dam   
     48  49                   Upper Bhavani Dam   
     49  50          Pare Dam (Pare HE project)   
     
                                        Purpose              River  \
     0                 Hydroelectric,Irrigation         Bhagirathi   
     1                 Hydroelectric,Irrigation             Yamuna   
     2                            Hydroelectric            Periyar   
     3      Hydroelectric,Irrigation,Recreation             Satluj   
     4                            Hydroelectric          Marusudar   
     5                 Hydroelectric,Irrigation            Narmada   
     6                 Hydroelectric,Irrigation            Krishna   
     7   Flood Control,Hydroelectric,Irrigation               Ravi   
     8                            Hydroelectric             CHENAB   
     9                            Hydroelectric               Ravi   
     10                           Hydroelectric         Cheruthoni   
     11                Hydroelectric,Irrigation               Beas   
     12                              Irrigation               Gola   
     13                           Hydroelectric          Subansiri   
     14                Hydroelectric,Irrigation           Ramganga   
     15                Hydroelectric,Irrigation            Krishna   
     16                           Hydroelectric              Kakki   
     17                              Irrigation               Nagi   
     18                           Hydroelectric             Chenab   
     19                 Drinking / Water Supply        Lakhya hole   
     20                Hydroelectric,Irrigation           Sholayar   
     21                           Hydroelectric              Koyna   
     22                           Hydroelectric         Idamalayar   
     23                           Hydroelectric          Kali Nadi   
     24                              Irrigation             Karjan   
     25                           Hydroelectric     Kilivillithode   
     26                           Hydroelectric         Bhagirathi   
     27                Hydroelectric,Irrigation   Kistobazar nalla   
     28   Hydroelectric,Drinking / Water Supply             Doyang   
     29                Hydroelectric,Irrigation             Rihand   
     30                Hydroelectric,Irrigation            Narmada   
     31                Hydroelectric,Irrigation              Varna   
     32                Hydroelectric,Irrigation  Bhatsa and chorna   
     33                           Hydroelectric            Bhavani   
     34                           Hydroelectric            Kodayar   
     35                Hydroelectric,Irrigation             Hasdeo   
     36                              Irrigation      Jakham (mahi)   
     37                           Hydroelectric             Teesta   
     38                           Hydroelectric        Shahi Nalla   
     39                Hydroelectric,Irrigation            Kallada   
     40                           Hydroelectric              Palar   
     41                           Hydroelectric            Parbati   
     42                              Irrigation             Chakra   
     43                Hydroelectric,Irrigation           Paravara   
     44                 Drinking / Water Supply           Vaitarna   
     45  Flood Control,Hydroelectric,Irrigation               Tapi   
     46                           Hydroelectric             Aliyar   
     47                Hydroelectric,Irrigation              Aruna   
     48                           Hydroelectric            Bhavani   
     49                                     NaN            Dikrong   
     
            Nearest City         District               State  \
     0       Pratapnagar    Tehri Garhwal         Uttarakhand   
     1          Dehradun         Dehradun         Uttarakhand   
     2         Todupulai           Idukki              Kerala   
     3          Bilaspur         Bilaspur    Himachal Pradesh   
     4          Kishtwar         Kishtwar     Jammu & Kashmir   
     5          Rajpipla          Narmada             Gujarat   
     6       Nandikotkur          Kurnool           Telangana   
     7         Pathankot           Kathua              Punjab   
     8            Ramban           Ramban     Jammu & Kashmir   
     9         Bhattiyat           Chamba    Himachal Pradesh   
     10        Todupulai           Idukki              Kerala   
     11     Dera Gopipur           Kangra    Himachal Pradesh   
     12        Naini Tal         Nainital         Uttarakhand   
     13  Lower Subansiri  Lower Subansiri  Arunanchal Pradesh   
     14        Lansdowne          Garhwal         Uttarakhand   
     15         Guruzala           Guntur           Telangana   
     16             Rani   Pathanamthitta              Kerala   
     17            Jamui            Jamui               Bihar   
     18  Gool Gulab Garh            Reasi     Jammu & Kashmir   
     19         Mudigere      Chikmagalur           Karnataka   
     20         Pollachi       Coimbatore          Tamil Nadu   
     21            Patan           Satara         Maharashtra   
     22        Devikolam           Idukki              Kerala   
     23             Supa   Uttara Kannada           Karnataka   
     24         Rajpipla          Narmada             Gujarat   
     25        Todupulai           Idukki              Kerala   
     26      Pratapnagar    Tehri Garhwal         Uttarakhand   
     27         Puruliya         Puruliya         West Bengal   
     28            Wokha            Wokha            Nagaland   
     29            Dudhi        Sonbhadra       Uttar Pradesh   
     30          Khandwa       East Nimar      Madhya Pradesh   
     31        Shahuwadi         Kolhapur         Maharashtra   
     32         Shahapur            Thane         Maharashtra   
     33   Mettuppalaiyam       Coimbatore          Tamil Nadu   
     34         Kalkulam    Kanniyakumari          Tamil Nadu   
     35         Katghora            Korba        Chhattisgarh   
     36       Pratapgarh       Pratapgarh           Rajasthan   
     37            North            North              Sikkim   
     38         Shahapur            Thane         Maharashtra   
     39     Pattanapuram           Kollam              Kerala   
     40        Devikolam           Idukki              Kerala   
     41            Kullu            Kullu    Himachal Pradesh   
     42       Hosanagara          Shimoga           Karnataka   
     43            Akola       Ahmadnagar         Maharashtra   
     44         Shahapur            Thane         Maharashtra   
     45          Songadh             Tapi             Gujarat   
     46         Pollachi       Coimbatore          Tamil Nadu   
     47      Vaibhavwadi       Sindhudurg         Maharashtra   
     48    Udagamandalam     The Nilgiris          Tamil Nadu   
     49              NaN              NaN                 NaN   
     
                                                 Basin              Status  \
     0                                           Ganga           Completed   
     1                                           Ganga            Proposed   
     2   West flowing rivers from Tadri to Kanyakumari           Completed   
     3                Indus up to International Border           Completed   
     4                Indus up to International Border            Proposed   
     5                                         Narmada           Completed   
     6                                         Krishna           Completed   
     7                Indus up to International Border           Completed   
     8                Indus up to International Border           Completed   
     9                Indus up to International Border           Completed   
     10  West flowing rivers from Tadri to Kanyakumari           Completed   
     11               Indus up to International Border           Completed   
     12                                          Ganga            Proposed   
     13                                    Brahmaputra  Under Construction   
     14                                          Ganga           Completed   
     15                                        Krishna           Completed   
     16  West flowing rivers from Tadri to Kanyakumari           Completed   
     17                                          Ganga           Completed   
     18               Indus up to International Border           Completed   
     19                                        Krishna           Completed   
     20  West flowing rivers from Tadri to Kanyakumari           Completed   
     21                                        Krishna           Completed   
     22  West flowing rivers from Tadri to Kanyakumari           Completed   
     23         West flowing rivers from Tapi to Tadri           Completed   
     24                                        Narmada           Completed   
     25  West flowing rivers from Tadri to Kanyakumari           Completed   
     26                                          Ganga           Completed   
     27                                   Subarnarekha           Completed   
     28                                    Brahmaputra           Completed   
     29                                          Ganga           Completed   
     30                                        Narmada           Completed   
     31                                        Krishna           Completed   
     32         West flowing rivers from Tapi to Tadri           Completed   
     33                                        Cauvery           Completed   
     34  West flowing rivers from Tadri to Kanyakumari           Completed   
     35                                       Mahanadi           Completed   
     36                                           Mahi           Completed   
     37                                    Brahmaputra           Completed   
     38         West flowing rivers from Tapi to Tadri           Completed   
     39  West flowing rivers from Tadri to Kanyakumari           Completed   
     40  West flowing rivers from Tadri to Kanyakumari           Completed   
     41               Indus up to International Border  Under Construction   
     42  West flowing rivers from Tadri to Kanyakumari           Completed   
     43                                       Godavari           Completed   
     44         West flowing rivers from Tapi to Tadri           Completed   
     45                                           Tapi           Completed   
     46  West flowing rivers from Tadri to Kanyakumari           Completed   
     47         West flowing rivers from Tapi to Tadri                 NaN   
     48                                        Cauvery           Completed   
     49                                            NaN           Completed   
     
         Completion Year                         Type  Length (m)  \
     0            2005.0  Earthen / Gravity & Masonry     575.000   
     1               NaN  Earthen / Gravity & Masonry     451.000   
     2            1974.0            Gravity & Masonry     366.000   
     3            1963.0  Earthen / Gravity & Masonry     518.160   
     4               NaN  Earthen / Gravity & Masonry     305.000   
     5               NaN            Gravity & Masonry    1210.000   
     6            1984.0                      Earthen     512.000   
     7            1999.0                      Earthen     617.000   
     8            2009.0            Gravity & Masonry     364.362   
     9            1994.0  Earthen / Gravity & Masonry     295.000   
     10           1976.0  Earthen / Gravity & Masonry     651.000   
     11           1974.0  Earthen / Gravity & Masonry    1950.700   
     12           1990.0            Gravity & Masonry     465.000   
     13           2014.0            Gravity & Masonry     284.000   
     14           1974.0                      Earthen     630.000   
     15           1974.0                      Earthen    4865.000   
     16           1966.0  Earthen / Gravity & Masonry     336.190   
     17           1958.0                      Earthen    1884.000   
     18           1986.0  Earthen / Gravity & Masonry     487.000   
     19           1994.0                      Earthen    1048.000   
     20           1971.0  Earthen / Gravity & Masonry    1244.180   
     21           1964.0                      Earthen     807.720   
     22           1985.0  Earthen / Gravity & Masonry     373.000   
     23           1987.0            Gravity & Masonry     331.290   
     24           1987.0  Earthen / Gravity & Masonry     903.000   
     25           1977.0            Gravity & Masonry     385.000   
     26              NaN            Gravity & Masonry     300.500   
     27              NaN                     Rockfill     310.000   
     28              NaN                      Earthen     462.000   
     29           1962.0            Gravity & Masonry     932.000   
     30           2006.0  Earthen / Gravity & Masonry     654.000   
     31           2000.0  Earthen / Gravity & Masonry    1580.000   
     32           1983.0  Earthen / Gravity & Masonry     959.000   
     33           1967.0            Gravity & Masonry     357.000   
     34           1972.0            Gravity & Masonry     166.000   
     35           1990.0  Earthen / Gravity & Masonry     554.500   
     36           1986.0            Gravity & Masonry     253.000   
     37           2007.0            Gravity & Masonry     176.500   
     38           2007.0            Gravity & Masonry     449.000   
     39           1986.0            Gravity & Masonry     335.000   
     40           1957.0  Earthen / Gravity & Masonry     237.740   
     41              NaN            Gravity & Masonry     101.500   
     42           1985.0                     Rockfill     570.000   
     43           1926.0            Gravity & Masonry    2717.000   
     44           1954.0            Gravity & Masonry     567.070   
     45           1972.0  Earthen / Gravity & Masonry    4927.000   
     46           1971.0            Gravity & Masonry     315.000   
     47              NaN                      Earthen    1240.000   
     48           1965.0            Gravity & Masonry     419.000   
     49              NaN            Gravity & Masonry     152.200   
     
         Max Height above Foundation (m)  Design Gross Storage Capacity (MCM)  
     0                            260.50                            3540.0000  
     1                            204.00                             587.8400  
     2                            169.00                            1998.5700  
     3                            167.64                            9867.8400  
     4                            167.00                               0.1254  
     5                            163.00                            9500.0000  
     6                            145.00                            8724.8800  
     7                            145.00                            3280.0000  
     8                            143.00                             475.0000  
     9                            140.00                             242.3000  
     10                           138.38                            1998.5700  
     11                           132.59                            8570.0000  
     12                           130.60                                  NaN  
     13                           130.00                            1643.0000  
     14                           127.50                            2448.0000  
     15                           124.66                           11553.0000  
     16                           116.13                             454.0700  
     17                           113.50                             108.0000  
     18                           113.00                              28.5000  
     19                           108.00                             273.7900  
     20                           105.16                             152.4800  
     21                           103.02                            2980.6900  
     22                           102.00                            1208.2300  
     23                           101.00                            4178.0000  
     24                           100.00                             630.0000  
     25                           100.00                            1998.5700  
     26                            97.50                              88.9000  
     27                            95.00                              16.0000  
     28                            92.00                             565.0000  
     29                            91.46                           10608.3200  
     30                            91.40                           12220.0000  
     31                            88.80                             974.1880  
     32                            88.50                             976.1000  
     33                            88.00                              44.4000  
     34                            88.00                              98.5100  
     35                            87.00                            3417.0000  
     36                            87.00                             142.0200  
     37                            86.80                              13.5000  
     38                            86.14                               3.2100  
     39                            85.35                             524.0000  
     40                            85.34                              55.4000  
     41                            85.00                               6.5500  
     42                            84.00                             222.6000  
     43                            82.35                             312.6000  
     44                            82.00                             204.9800  
     45                            81.00                            8510.0000  
     46                            81.00                              26.5700  
     47                            80.41                              93.3780  
     48                            80.00                             101.2000  
     49                            78.00                              19.6300  ]




```python
df2 = pd.read_html(str(table))[0]
df2

```

    C:\Users\sukan\AppData\Local\Temp\ipykernel_26364\2094832078.py:1: FutureWarning: Passing literal html to 'read_html' is deprecated and will be removed in a future version. To read from a literal string, wrap it in a 'StringIO' object.
      df2 = pd.read_html(str(table))[0]
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Purpose</th>
      <th>River</th>
      <th>Nearest City</th>
      <th>District</th>
      <th>State</th>
      <th>Basin</th>
      <th>Status</th>
      <th>Completion Year</th>
      <th>Type</th>
      <th>Length (m)</th>
      <th>Max Height above Foundation (m)</th>
      <th>Design Gross Storage Capacity (MCM)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Tehri Dam</td>
      <td>Hydroelectric,Irrigation</td>
      <td>Bhagirathi</td>
      <td>Pratapnagar</td>
      <td>Tehri Garhwal</td>
      <td>Uttarakhand</td>
      <td>Ganga</td>
      <td>Completed</td>
      <td>2005.0</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>575.000</td>
      <td>260.50</td>
      <td>3540.0000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Lakhwar Dam</td>
      <td>Hydroelectric,Irrigation</td>
      <td>Yamuna</td>
      <td>Dehradun</td>
      <td>Dehradun</td>
      <td>Uttarakhand</td>
      <td>Ganga</td>
      <td>Proposed</td>
      <td>NaN</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>451.000</td>
      <td>204.00</td>
      <td>587.8400</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Idukki (Eb)/Idukki Arch Dam</td>
      <td>Hydroelectric</td>
      <td>Periyar</td>
      <td>Todupulai</td>
      <td>Idukki</td>
      <td>Kerala</td>
      <td>West flowing rivers from Tadri to Kanyakumari</td>
      <td>Completed</td>
      <td>1974.0</td>
      <td>Gravity &amp; Masonry</td>
      <td>366.000</td>
      <td>169.00</td>
      <td>1998.5700</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Bhakra Dam</td>
      <td>Hydroelectric,Irrigation,Recreation</td>
      <td>Satluj</td>
      <td>Bilaspur</td>
      <td>Bilaspur</td>
      <td>Himachal Pradesh</td>
      <td>Indus up to International Border</td>
      <td>Completed</td>
      <td>1963.0</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>518.160</td>
      <td>167.64</td>
      <td>9867.8400</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Pakal Dul Dam</td>
      <td>Hydroelectric</td>
      <td>Marusudar</td>
      <td>Kishtwar</td>
      <td>Kishtwar</td>
      <td>Jammu &amp; Kashmir</td>
      <td>Indus up to International Border</td>
      <td>Proposed</td>
      <td>NaN</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>305.000</td>
      <td>167.00</td>
      <td>0.1254</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Sardar Sarover Gujarat Dam</td>
      <td>Hydroelectric,Irrigation</td>
      <td>Narmada</td>
      <td>Rajpipla</td>
      <td>Narmada</td>
      <td>Gujarat</td>
      <td>Narmada</td>
      <td>Completed</td>
      <td>NaN</td>
      <td>Gravity &amp; Masonry</td>
      <td>1210.000</td>
      <td>163.00</td>
      <td>9500.0000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Srisailam (N.S.R.S.P) Dam</td>
      <td>Hydroelectric,Irrigation</td>
      <td>Krishna</td>
      <td>Nandikotkur</td>
      <td>Kurnool</td>
      <td>Telangana</td>
      <td>Krishna</td>
      <td>Completed</td>
      <td>1984.0</td>
      <td>Earthen</td>
      <td>512.000</td>
      <td>145.00</td>
      <td>8724.8800</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Ranjit Sagar Dam</td>
      <td>Flood Control,Hydroelectric,Irrigation</td>
      <td>Ravi</td>
      <td>Pathankot</td>
      <td>Kathua</td>
      <td>Punjab</td>
      <td>Indus up to International Border</td>
      <td>Completed</td>
      <td>1999.0</td>
      <td>Earthen</td>
      <td>617.000</td>
      <td>145.00</td>
      <td>3280.0000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Baglihar Dam</td>
      <td>Hydroelectric</td>
      <td>CHENAB</td>
      <td>Ramban</td>
      <td>Ramban</td>
      <td>Jammu &amp; Kashmir</td>
      <td>Indus up to International Border</td>
      <td>Completed</td>
      <td>2009.0</td>
      <td>Gravity &amp; Masonry</td>
      <td>364.362</td>
      <td>143.00</td>
      <td>475.0000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>Chamera I Dam</td>
      <td>Hydroelectric</td>
      <td>Ravi</td>
      <td>Bhattiyat</td>
      <td>Chamba</td>
      <td>Himachal Pradesh</td>
      <td>Indus up to International Border</td>
      <td>Completed</td>
      <td>1994.0</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>295.000</td>
      <td>140.00</td>
      <td>242.3000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>Cheruthoni (Eb) Dam</td>
      <td>Hydroelectric</td>
      <td>Cheruthoni</td>
      <td>Todupulai</td>
      <td>Idukki</td>
      <td>Kerala</td>
      <td>West flowing rivers from Tadri to Kanyakumari</td>
      <td>Completed</td>
      <td>1976.0</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>651.000</td>
      <td>138.38</td>
      <td>1998.5700</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>Pong Dam</td>
      <td>Hydroelectric,Irrigation</td>
      <td>Beas</td>
      <td>Dera Gopipur</td>
      <td>Kangra</td>
      <td>Himachal Pradesh</td>
      <td>Indus up to International Border</td>
      <td>Completed</td>
      <td>1974.0</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>1950.700</td>
      <td>132.59</td>
      <td>8570.0000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>Jamrani Dam</td>
      <td>Irrigation</td>
      <td>Gola</td>
      <td>Naini Tal</td>
      <td>Nainital</td>
      <td>Uttarakhand</td>
      <td>Ganga</td>
      <td>Proposed</td>
      <td>1990.0</td>
      <td>Gravity &amp; Masonry</td>
      <td>465.000</td>
      <td>130.60</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>Subansiri Lower HE (Nhpc) Dam</td>
      <td>Hydroelectric</td>
      <td>Subansiri</td>
      <td>Lower Subansiri</td>
      <td>Lower Subansiri</td>
      <td>Arunanchal Pradesh</td>
      <td>Brahmaputra</td>
      <td>Under Construction</td>
      <td>2014.0</td>
      <td>Gravity &amp; Masonry</td>
      <td>284.000</td>
      <td>130.00</td>
      <td>1643.0000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>Ramganga Dam</td>
      <td>Hydroelectric,Irrigation</td>
      <td>Ramganga</td>
      <td>Lansdowne</td>
      <td>Garhwal</td>
      <td>Uttarakhand</td>
      <td>Ganga</td>
      <td>Completed</td>
      <td>1974.0</td>
      <td>Earthen</td>
      <td>630.000</td>
      <td>127.50</td>
      <td>2448.0000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>Nagarjuna Sagar Dam</td>
      <td>Hydroelectric,Irrigation</td>
      <td>Krishna</td>
      <td>Guruzala</td>
      <td>Guntur</td>
      <td>Telangana</td>
      <td>Krishna</td>
      <td>Completed</td>
      <td>1974.0</td>
      <td>Earthen</td>
      <td>4865.000</td>
      <td>124.66</td>
      <td>11553.0000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>Kakki (Eb) Dam</td>
      <td>Hydroelectric</td>
      <td>Kakki</td>
      <td>Rani</td>
      <td>Pathanamthitta</td>
      <td>Kerala</td>
      <td>West flowing rivers from Tadri to Kanyakumari</td>
      <td>Completed</td>
      <td>1966.0</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>336.190</td>
      <td>116.13</td>
      <td>454.0700</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>Nagi Dam</td>
      <td>Irrigation</td>
      <td>Nagi</td>
      <td>Jamui</td>
      <td>Jamui</td>
      <td>Bihar</td>
      <td>Ganga</td>
      <td>Completed</td>
      <td>1958.0</td>
      <td>Earthen</td>
      <td>1884.000</td>
      <td>113.50</td>
      <td>108.0000</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>Salal (Rockfill And Concrete ) Dam</td>
      <td>Hydroelectric</td>
      <td>Chenab</td>
      <td>Gool Gulab Garh</td>
      <td>Reasi</td>
      <td>Jammu &amp; Kashmir</td>
      <td>Indus up to International Border</td>
      <td>Completed</td>
      <td>1986.0</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>487.000</td>
      <td>113.00</td>
      <td>28.5000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>Lakhya Dam</td>
      <td>Drinking / Water Supply</td>
      <td>Lakhya hole</td>
      <td>Mudigere</td>
      <td>Chikmagalur</td>
      <td>Karnataka</td>
      <td>Krishna</td>
      <td>Completed</td>
      <td>1994.0</td>
      <td>Earthen</td>
      <td>1048.000</td>
      <td>108.00</td>
      <td>273.7900</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>Sholayar Dam</td>
      <td>Hydroelectric,Irrigation</td>
      <td>Sholayar</td>
      <td>Pollachi</td>
      <td>Coimbatore</td>
      <td>Tamil Nadu</td>
      <td>West flowing rivers from Tadri to Kanyakumari</td>
      <td>Completed</td>
      <td>1971.0</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>1244.180</td>
      <td>105.16</td>
      <td>152.4800</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>Koyna Dam</td>
      <td>Hydroelectric</td>
      <td>Koyna</td>
      <td>Patan</td>
      <td>Satara</td>
      <td>Maharashtra</td>
      <td>Krishna</td>
      <td>Completed</td>
      <td>1964.0</td>
      <td>Earthen</td>
      <td>807.720</td>
      <td>103.02</td>
      <td>2980.6900</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>Idamalayar (Eb) Dam</td>
      <td>Hydroelectric</td>
      <td>Idamalayar</td>
      <td>Devikolam</td>
      <td>Idukki</td>
      <td>Kerala</td>
      <td>West flowing rivers from Tadri to Kanyakumari</td>
      <td>Completed</td>
      <td>1985.0</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>373.000</td>
      <td>102.00</td>
      <td>1208.2300</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
      <td>Supa Dam</td>
      <td>Hydroelectric</td>
      <td>Kali Nadi</td>
      <td>Supa</td>
      <td>Uttara Kannada</td>
      <td>Karnataka</td>
      <td>West flowing rivers from Tapi to Tadri</td>
      <td>Completed</td>
      <td>1987.0</td>
      <td>Gravity &amp; Masonry</td>
      <td>331.290</td>
      <td>101.00</td>
      <td>4178.0000</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>Karjan Dam</td>
      <td>Irrigation</td>
      <td>Karjan</td>
      <td>Rajpipla</td>
      <td>Narmada</td>
      <td>Gujarat</td>
      <td>Narmada</td>
      <td>Completed</td>
      <td>1987.0</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>903.000</td>
      <td>100.00</td>
      <td>630.0000</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26</td>
      <td>Kulamavu (Eb) Dam</td>
      <td>Hydroelectric</td>
      <td>Kilivillithode</td>
      <td>Todupulai</td>
      <td>Idukki</td>
      <td>Kerala</td>
      <td>West flowing rivers from Tadri to Kanyakumari</td>
      <td>Completed</td>
      <td>1977.0</td>
      <td>Gravity &amp; Masonry</td>
      <td>385.000</td>
      <td>100.00</td>
      <td>1998.5700</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
      <td>Koteshwar Dam</td>
      <td>Hydroelectric</td>
      <td>Bhagirathi</td>
      <td>Pratapnagar</td>
      <td>Tehri Garhwal</td>
      <td>Uttarakhand</td>
      <td>Ganga</td>
      <td>Completed</td>
      <td>NaN</td>
      <td>Gravity &amp; Masonry</td>
      <td>300.500</td>
      <td>97.50</td>
      <td>88.9000</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>Lower : PPSP Dam</td>
      <td>Hydroelectric,Irrigation</td>
      <td>Kistobazar nalla</td>
      <td>Puruliya</td>
      <td>Puruliya</td>
      <td>West Bengal</td>
      <td>Subarnarekha</td>
      <td>Completed</td>
      <td>NaN</td>
      <td>Rockfill</td>
      <td>310.000</td>
      <td>95.00</td>
      <td>16.0000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29</td>
      <td>Doyang Hep Dam</td>
      <td>Hydroelectric,Drinking / Water Supply</td>
      <td>Doyang</td>
      <td>Wokha</td>
      <td>Wokha</td>
      <td>Nagaland</td>
      <td>Brahmaputra</td>
      <td>Completed</td>
      <td>NaN</td>
      <td>Earthen</td>
      <td>462.000</td>
      <td>92.00</td>
      <td>565.0000</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>Rihand Dam</td>
      <td>Hydroelectric,Irrigation</td>
      <td>Rihand</td>
      <td>Dudhi</td>
      <td>Sonbhadra</td>
      <td>Uttar Pradesh</td>
      <td>Ganga</td>
      <td>Completed</td>
      <td>1962.0</td>
      <td>Gravity &amp; Masonry</td>
      <td>932.000</td>
      <td>91.46</td>
      <td>10608.3200</td>
    </tr>
    <tr>
      <th>30</th>
      <td>31</td>
      <td>Indira Sagar (NHDC) Dam</td>
      <td>Hydroelectric,Irrigation</td>
      <td>Narmada</td>
      <td>Khandwa</td>
      <td>East Nimar</td>
      <td>Madhya Pradesh</td>
      <td>Narmada</td>
      <td>Completed</td>
      <td>2006.0</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>654.000</td>
      <td>91.40</td>
      <td>12220.0000</td>
    </tr>
    <tr>
      <th>31</th>
      <td>32</td>
      <td>Warna Dam</td>
      <td>Hydroelectric,Irrigation</td>
      <td>Varna</td>
      <td>Shahuwadi</td>
      <td>Kolhapur</td>
      <td>Maharashtra</td>
      <td>Krishna</td>
      <td>Completed</td>
      <td>2000.0</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>1580.000</td>
      <td>88.80</td>
      <td>974.1880</td>
    </tr>
    <tr>
      <th>32</th>
      <td>33</td>
      <td>Bhatsa Dam</td>
      <td>Hydroelectric,Irrigation</td>
      <td>Bhatsa and chorna</td>
      <td>Shahapur</td>
      <td>Thane</td>
      <td>Maharashtra</td>
      <td>West flowing rivers from Tapi to Tadri</td>
      <td>Completed</td>
      <td>1983.0</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>959.000</td>
      <td>88.50</td>
      <td>976.1000</td>
    </tr>
    <tr>
      <th>33</th>
      <td>34</td>
      <td>Pillur Dam</td>
      <td>Hydroelectric</td>
      <td>Bhavani</td>
      <td>Mettuppalaiyam</td>
      <td>Coimbatore</td>
      <td>Tamil Nadu</td>
      <td>Cauvery</td>
      <td>Completed</td>
      <td>1967.0</td>
      <td>Gravity &amp; Masonry</td>
      <td>357.000</td>
      <td>88.00</td>
      <td>44.4000</td>
    </tr>
    <tr>
      <th>34</th>
      <td>35</td>
      <td>Upper Kodayar Dam</td>
      <td>Hydroelectric</td>
      <td>Kodayar</td>
      <td>Kalkulam</td>
      <td>Kanniyakumari</td>
      <td>Tamil Nadu</td>
      <td>West flowing rivers from Tadri to Kanyakumari</td>
      <td>Completed</td>
      <td>1972.0</td>
      <td>Gravity &amp; Masonry</td>
      <td>166.000</td>
      <td>88.00</td>
      <td>98.5100</td>
    </tr>
    <tr>
      <th>35</th>
      <td>36</td>
      <td>Hasdeo Bango (Minimata) Dam</td>
      <td>Hydroelectric,Irrigation</td>
      <td>Hasdeo</td>
      <td>Katghora</td>
      <td>Korba</td>
      <td>Chhattisgarh</td>
      <td>Mahanadi</td>
      <td>Completed</td>
      <td>1990.0</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>554.500</td>
      <td>87.00</td>
      <td>3417.0000</td>
    </tr>
    <tr>
      <th>36</th>
      <td>37</td>
      <td>Jakham Main Dam</td>
      <td>Irrigation</td>
      <td>Jakham (mahi)</td>
      <td>Pratapgarh</td>
      <td>Pratapgarh</td>
      <td>Rajasthan</td>
      <td>Mahi</td>
      <td>Completed</td>
      <td>1986.0</td>
      <td>Gravity &amp; Masonry</td>
      <td>253.000</td>
      <td>87.00</td>
      <td>142.0200</td>
    </tr>
    <tr>
      <th>37</th>
      <td>38</td>
      <td>Teesta -V (NHPC) Dam</td>
      <td>Hydroelectric</td>
      <td>Teesta</td>
      <td>North</td>
      <td>North</td>
      <td>Sikkim</td>
      <td>Brahmaputra</td>
      <td>Completed</td>
      <td>2007.0</td>
      <td>Gravity &amp; Masonry</td>
      <td>176.500</td>
      <td>86.80</td>
      <td>13.5000</td>
    </tr>
    <tr>
      <th>38</th>
      <td>39</td>
      <td>Lower Ghatghar Dam</td>
      <td>Hydroelectric</td>
      <td>Shahi Nalla</td>
      <td>Shahapur</td>
      <td>Thane</td>
      <td>Maharashtra</td>
      <td>West flowing rivers from Tapi to Tadri</td>
      <td>Completed</td>
      <td>2007.0</td>
      <td>Gravity &amp; Masonry</td>
      <td>449.000</td>
      <td>86.14</td>
      <td>3.2100</td>
    </tr>
    <tr>
      <th>39</th>
      <td>40</td>
      <td>Kallada (Parappar) (Id) Dam</td>
      <td>Hydroelectric,Irrigation</td>
      <td>Kallada</td>
      <td>Pattanapuram</td>
      <td>Kollam</td>
      <td>Kerala</td>
      <td>West flowing rivers from Tadri to Kanyakumari</td>
      <td>Completed</td>
      <td>1986.0</td>
      <td>Gravity &amp; Masonry</td>
      <td>335.000</td>
      <td>85.35</td>
      <td>524.0000</td>
    </tr>
    <tr>
      <th>40</th>
      <td>41</td>
      <td>Madupetty (Eb) Dam</td>
      <td>Hydroelectric</td>
      <td>Palar</td>
      <td>Devikolam</td>
      <td>Idukki</td>
      <td>Kerala</td>
      <td>West flowing rivers from Tadri to Kanyakumari</td>
      <td>Completed</td>
      <td>1957.0</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>237.740</td>
      <td>85.34</td>
      <td>55.4000</td>
    </tr>
    <tr>
      <th>41</th>
      <td>42</td>
      <td>Parbati II Dam</td>
      <td>Hydroelectric</td>
      <td>Parbati</td>
      <td>Kullu</td>
      <td>Kullu</td>
      <td>Himachal Pradesh</td>
      <td>Indus up to International Border</td>
      <td>Under Construction</td>
      <td>NaN</td>
      <td>Gravity &amp; Masonry</td>
      <td>101.500</td>
      <td>85.00</td>
      <td>6.5500</td>
    </tr>
    <tr>
      <th>42</th>
      <td>43</td>
      <td>Chakra Dam</td>
      <td>Irrigation</td>
      <td>Chakra</td>
      <td>Hosanagara</td>
      <td>Shimoga</td>
      <td>Karnataka</td>
      <td>West flowing rivers from Tadri to Kanyakumari</td>
      <td>Completed</td>
      <td>1985.0</td>
      <td>Rockfill</td>
      <td>570.000</td>
      <td>84.00</td>
      <td>222.6000</td>
    </tr>
    <tr>
      <th>43</th>
      <td>44</td>
      <td>Bandardhara Dam</td>
      <td>Hydroelectric,Irrigation</td>
      <td>Paravara</td>
      <td>Akola</td>
      <td>Ahmadnagar</td>
      <td>Maharashtra</td>
      <td>Godavari</td>
      <td>Completed</td>
      <td>1926.0</td>
      <td>Gravity &amp; Masonry</td>
      <td>2717.000</td>
      <td>82.35</td>
      <td>312.6000</td>
    </tr>
    <tr>
      <th>44</th>
      <td>45</td>
      <td>Lower Vaitarna Dam</td>
      <td>Drinking / Water Supply</td>
      <td>Vaitarna</td>
      <td>Shahapur</td>
      <td>Thane</td>
      <td>Maharashtra</td>
      <td>West flowing rivers from Tapi to Tadri</td>
      <td>Completed</td>
      <td>1954.0</td>
      <td>Gravity &amp; Masonry</td>
      <td>567.070</td>
      <td>82.00</td>
      <td>204.9800</td>
    </tr>
    <tr>
      <th>45</th>
      <td>46</td>
      <td>Ukai Dam</td>
      <td>Flood Control,Hydroelectric,Irrigation</td>
      <td>Tapi</td>
      <td>Songadh</td>
      <td>Tapi</td>
      <td>Gujarat</td>
      <td>Tapi</td>
      <td>Completed</td>
      <td>1972.0</td>
      <td>Earthen / Gravity &amp; Masonry</td>
      <td>4927.000</td>
      <td>81.00</td>
      <td>8510.0000</td>
    </tr>
    <tr>
      <th>46</th>
      <td>47</td>
      <td>Upper Aliyar Dam</td>
      <td>Hydroelectric</td>
      <td>Aliyar</td>
      <td>Pollachi</td>
      <td>Coimbatore</td>
      <td>Tamil Nadu</td>
      <td>West flowing rivers from Tadri to Kanyakumari</td>
      <td>Completed</td>
      <td>1971.0</td>
      <td>Gravity &amp; Masonry</td>
      <td>315.000</td>
      <td>81.00</td>
      <td>26.5700</td>
    </tr>
    <tr>
      <th>47</th>
      <td>48</td>
      <td>Aruna Dam</td>
      <td>Hydroelectric,Irrigation</td>
      <td>Aruna</td>
      <td>Vaibhavwadi</td>
      <td>Sindhudurg</td>
      <td>Maharashtra</td>
      <td>West flowing rivers from Tapi to Tadri</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Earthen</td>
      <td>1240.000</td>
      <td>80.41</td>
      <td>93.3780</td>
    </tr>
    <tr>
      <th>48</th>
      <td>49</td>
      <td>Upper Bhavani Dam</td>
      <td>Hydroelectric</td>
      <td>Bhavani</td>
      <td>Udagamandalam</td>
      <td>The Nilgiris</td>
      <td>Tamil Nadu</td>
      <td>Cauvery</td>
      <td>Completed</td>
      <td>1965.0</td>
      <td>Gravity &amp; Masonry</td>
      <td>419.000</td>
      <td>80.00</td>
      <td>101.2000</td>
    </tr>
    <tr>
      <th>49</th>
      <td>50</td>
      <td>Pare Dam (Pare HE project)</td>
      <td>NaN</td>
      <td>Dikrong</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Completed</td>
      <td>NaN</td>
      <td>Gravity &amp; Masonry</td>
      <td>152.200</td>
      <td>78.00</td>
      <td>19.6300</td>
    </tr>
  </tbody>
</table>
</div>



### In summary, the process:

#### Fetches a webpage (requests)

#### Parses HTML (BeautifulSoup)

#### Extracts tables (pandas)

#### Converts them into an analytical DataFrame


```python

```
