```python
# For detailed script Please visit  https://github.com/sukantjain/Python/blob/main/NetCDF_to_CSV.ipynb
```


```python
import xarray
import pandas as pd
import numpy as np
```


```python
netcdf1 = xarray.open_dataset(r'D:\NIH\Training\Python for water\NWA\data\IMD\RF25_ind2020_rfp25.nc')

netcdf1
```




<div><svg style="position: absolute; width: 0; height: 0; overflow: hidden">
<defs>
<symbol id="icon-database" viewBox="0 0 32 32">
<path d="M16 0c-8.837 0-16 2.239-16 5v4c0 2.761 7.163 5 16 5s16-2.239 16-5v-4c0-2.761-7.163-5-16-5z"></path>
<path d="M16 17c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
<path d="M16 26c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
</symbol>
<symbol id="icon-file-text2" viewBox="0 0 32 32">
<path d="M28.681 7.159c-0.694-0.947-1.662-2.053-2.724-3.116s-2.169-2.030-3.116-2.724c-1.612-1.182-2.393-1.319-2.841-1.319h-15.5c-1.378 0-2.5 1.121-2.5 2.5v27c0 1.378 1.122 2.5 2.5 2.5h23c1.378 0 2.5-1.122 2.5-2.5v-19.5c0-0.448-0.137-1.23-1.319-2.841zM24.543 5.457c0.959 0.959 1.712 1.825 2.268 2.543h-4.811v-4.811c0.718 0.556 1.584 1.309 2.543 2.268zM28 29.5c0 0.271-0.229 0.5-0.5 0.5h-23c-0.271 0-0.5-0.229-0.5-0.5v-27c0-0.271 0.229-0.5 0.5-0.5 0 0 15.499-0 15.5 0v7c0 0.552 0.448 1 1 1h7v19.5z"></path>
<path d="M23 26h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 22h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 18h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
</symbol>
</defs>
</svg>
<style>/* CSS stylesheet for displaying xarray objects in jupyterlab.
 *
 */

:root {
  --xr-font-color0: var(--jp-content-font-color0, rgba(0, 0, 0, 1));
  --xr-font-color2: var(--jp-content-font-color2, rgba(0, 0, 0, 0.54));
  --xr-font-color3: var(--jp-content-font-color3, rgba(0, 0, 0, 0.38));
  --xr-border-color: var(--jp-border-color2, #e0e0e0);
  --xr-disabled-color: var(--jp-layout-color3, #bdbdbd);
  --xr-background-color: var(--jp-layout-color0, white);
  --xr-background-color-row-even: var(--jp-layout-color1, white);
  --xr-background-color-row-odd: var(--jp-layout-color2, #eeeeee);
}

html[theme=dark],
body[data-theme=dark],
body.vscode-dark {
  --xr-font-color0: rgba(255, 255, 255, 1);
  --xr-font-color2: rgba(255, 255, 255, 0.54);
  --xr-font-color3: rgba(255, 255, 255, 0.38);
  --xr-border-color: #1F1F1F;
  --xr-disabled-color: #515151;
  --xr-background-color: #111111;
  --xr-background-color-row-even: #111111;
  --xr-background-color-row-odd: #313131;
}

.xr-wrap {
  display: block !important;
  min-width: 300px;
  max-width: 700px;
}

.xr-text-repr-fallback {
  /* fallback to plain text repr when CSS is not injected (untrusted notebook) */
  display: none;
}

.xr-header {
  padding-top: 6px;
  padding-bottom: 6px;
  margin-bottom: 4px;
  border-bottom: solid 1px var(--xr-border-color);
}

.xr-header > div,
.xr-header > ul {
  display: inline;
  margin-top: 0;
  margin-bottom: 0;
}

.xr-obj-type,
.xr-array-name {
  margin-left: 2px;
  margin-right: 10px;
}

.xr-obj-type {
  color: var(--xr-font-color2);
}

.xr-sections {
  padding-left: 0 !important;
  display: grid;
  grid-template-columns: 150px auto auto 1fr 20px 20px;
}

.xr-section-item {
  display: contents;
}

.xr-section-item input {
  display: none;
}

.xr-section-item input + label {
  color: var(--xr-disabled-color);
}

.xr-section-item input:enabled + label {
  cursor: pointer;
  color: var(--xr-font-color2);
}

.xr-section-item input:enabled + label:hover {
  color: var(--xr-font-color0);
}

.xr-section-summary {
  grid-column: 1;
  color: var(--xr-font-color2);
  font-weight: 500;
}

.xr-section-summary > span {
  display: inline-block;
  padding-left: 0.5em;
}

.xr-section-summary-in:disabled + label {
  color: var(--xr-font-color2);
}

.xr-section-summary-in + label:before {
  display: inline-block;
  content: '►';
  font-size: 11px;
  width: 15px;
  text-align: center;
}

.xr-section-summary-in:disabled + label:before {
  color: var(--xr-disabled-color);
}

.xr-section-summary-in:checked + label:before {
  content: '▼';
}

.xr-section-summary-in:checked + label > span {
  display: none;
}

.xr-section-summary,
.xr-section-inline-details {
  padding-top: 4px;
  padding-bottom: 4px;
}

.xr-section-inline-details {
  grid-column: 2 / -1;
}

.xr-section-details {
  display: none;
  grid-column: 1 / -1;
  margin-bottom: 5px;
}

.xr-section-summary-in:checked ~ .xr-section-details {
  display: contents;
}

.xr-array-wrap {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: 20px auto;
}

.xr-array-wrap > label {
  grid-column: 1;
  vertical-align: top;
}

.xr-preview {
  color: var(--xr-font-color3);
}

.xr-array-preview,
.xr-array-data {
  padding: 0 5px !important;
  grid-column: 2;
}

.xr-array-data,
.xr-array-in:checked ~ .xr-array-preview {
  display: none;
}

.xr-array-in:checked ~ .xr-array-data,
.xr-array-preview {
  display: inline-block;
}

.xr-dim-list {
  display: inline-block !important;
  list-style: none;
  padding: 0 !important;
  margin: 0;
}

.xr-dim-list li {
  display: inline-block;
  padding: 0;
  margin: 0;
}

.xr-dim-list:before {
  content: '(';
}

.xr-dim-list:after {
  content: ')';
}

.xr-dim-list li:not(:last-child):after {
  content: ',';
  padding-right: 5px;
}

.xr-has-index {
  font-weight: bold;
}

.xr-var-list,
.xr-var-item {
  display: contents;
}

.xr-var-item > div,
.xr-var-item label,
.xr-var-item > .xr-var-name span {
  background-color: var(--xr-background-color-row-even);
  margin-bottom: 0;
}

.xr-var-item > .xr-var-name:hover span {
  padding-right: 5px;
}

.xr-var-list > li:nth-child(odd) > div,
.xr-var-list > li:nth-child(odd) > label,
.xr-var-list > li:nth-child(odd) > .xr-var-name span {
  background-color: var(--xr-background-color-row-odd);
}

.xr-var-name {
  grid-column: 1;
}

.xr-var-dims {
  grid-column: 2;
}

.xr-var-dtype {
  grid-column: 3;
  text-align: right;
  color: var(--xr-font-color2);
}

.xr-var-preview {
  grid-column: 4;
}

.xr-index-preview {
  grid-column: 2 / 5;
  color: var(--xr-font-color2);
}

.xr-var-name,
.xr-var-dims,
.xr-var-dtype,
.xr-preview,
.xr-attrs dt {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-right: 10px;
}

.xr-var-name:hover,
.xr-var-dims:hover,
.xr-var-dtype:hover,
.xr-attrs dt:hover {
  overflow: visible;
  width: auto;
  z-index: 1;
}

.xr-var-attrs,
.xr-var-data,
.xr-index-data {
  display: none;
  background-color: var(--xr-background-color) !important;
  padding-bottom: 5px !important;
}

.xr-var-attrs-in:checked ~ .xr-var-attrs,
.xr-var-data-in:checked ~ .xr-var-data,
.xr-index-data-in:checked ~ .xr-index-data {
  display: block;
}

.xr-var-data > table {
  float: right;
}

.xr-var-name span,
.xr-var-data,
.xr-index-name div,
.xr-index-data,
.xr-attrs {
  padding-left: 25px !important;
}

.xr-attrs,
.xr-var-attrs,
.xr-var-data,
.xr-index-data {
  grid-column: 1 / -1;
}

dl.xr-attrs {
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: 125px auto;
}

.xr-attrs dt,
.xr-attrs dd {
  padding: 0;
  margin: 0;
  float: left;
  padding-right: 10px;
  width: auto;
}

.xr-attrs dt {
  font-weight: normal;
  grid-column: 1;
}

.xr-attrs dt:hover span {
  display: inline-block;
  background: var(--xr-background-color);
  padding-right: 10px;
}

.xr-attrs dd {
  grid-column: 2;
  white-space: pre-wrap;
  word-break: break-all;
}

.xr-icon-database,
.xr-icon-file-text2,
.xr-no-icon {
  display: inline-block;
  vertical-align: middle;
  width: 1em;
  height: 1.5em !important;
  stroke-width: 0;
  stroke: currentColor;
  fill: currentColor;
}
</style><pre class='xr-text-repr-fallback'>&lt;xarray.Dataset&gt; Size: 51MB
Dimensions:    (LONGITUDE: 135, LATITUDE: 129, TIME: 366)
Coordinates:
  * LONGITUDE  (LONGITUDE) float64 1kB 66.5 66.75 67.0 ... 99.5 99.75 100.0
  * LATITUDE   (LATITUDE) float64 1kB 6.5 6.75 7.0 7.25 ... 38.0 38.25 38.5
  * TIME       (TIME) datetime64[ns] 3kB 2020-01-01 2020-01-02 ... 2020-12-31
Data variables:
    RAINFALL   (TIME, LATITUDE, LONGITUDE) float64 51MB ...
Attributes:
    history:      FERRET V7.5 (optimized) 20-Jan-23
    Conventions:  CF-1.6</pre><div class='xr-wrap' style='display:none'><div class='xr-header'><div class='xr-obj-type'>xarray.Dataset</div></div><ul class='xr-sections'><li class='xr-section-item'><input id='section-5ffd4d74-0f96-4cb2-b8b7-4750b19b3e40' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-5ffd4d74-0f96-4cb2-b8b7-4750b19b3e40' class='xr-section-summary'  title='Expand/collapse section'>Dimensions:</label><div class='xr-section-inline-details'><ul class='xr-dim-list'><li><span class='xr-has-index'>LONGITUDE</span>: 135</li><li><span class='xr-has-index'>LATITUDE</span>: 129</li><li><span class='xr-has-index'>TIME</span>: 366</li></ul></div><div class='xr-section-details'></div></li><li class='xr-section-item'><input id='section-b77cd05e-aa06-421f-89a1-9a2914718b65' class='xr-section-summary-in' type='checkbox'  checked><label for='section-b77cd05e-aa06-421f-89a1-9a2914718b65' class='xr-section-summary' >Coordinates: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>LONGITUDE</span></div><div class='xr-var-dims'>(LONGITUDE)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>66.5 66.75 67.0 ... 99.75 100.0</div><input id='attrs-9c8c7a5d-9f00-4fe6-842c-8540c590b05c' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-9c8c7a5d-9f00-4fe6-842c-8540c590b05c' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-86c4b65a-2ef0-4cad-b6dc-2c39be0e8d87' class='xr-var-data-in' type='checkbox'><label for='data-86c4b65a-2ef0-4cad-b6dc-2c39be0e8d87' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>units :</span></dt><dd>degrees_east</dd><dt><span>point_spacing :</span></dt><dd>even</dd><dt><span>axis :</span></dt><dd>X</dd><dt><span>modulo :</span></dt><dd>360.0</dd><dt><span>standard_name :</span></dt><dd>longitude</dd></dl></div><div class='xr-var-data'><pre>array([ 66.5 ,  66.75,  67.  ,  67.25,  67.5 ,  67.75,  68.  ,  68.25,  68.5 ,
        68.75,  69.  ,  69.25,  69.5 ,  69.75,  70.  ,  70.25,  70.5 ,  70.75,
        71.  ,  71.25,  71.5 ,  71.75,  72.  ,  72.25,  72.5 ,  72.75,  73.  ,
        73.25,  73.5 ,  73.75,  74.  ,  74.25,  74.5 ,  74.75,  75.  ,  75.25,
        75.5 ,  75.75,  76.  ,  76.25,  76.5 ,  76.75,  77.  ,  77.25,  77.5 ,
        77.75,  78.  ,  78.25,  78.5 ,  78.75,  79.  ,  79.25,  79.5 ,  79.75,
        80.  ,  80.25,  80.5 ,  80.75,  81.  ,  81.25,  81.5 ,  81.75,  82.  ,
        82.25,  82.5 ,  82.75,  83.  ,  83.25,  83.5 ,  83.75,  84.  ,  84.25,
        84.5 ,  84.75,  85.  ,  85.25,  85.5 ,  85.75,  86.  ,  86.25,  86.5 ,
        86.75,  87.  ,  87.25,  87.5 ,  87.75,  88.  ,  88.25,  88.5 ,  88.75,
        89.  ,  89.25,  89.5 ,  89.75,  90.  ,  90.25,  90.5 ,  90.75,  91.  ,
        91.25,  91.5 ,  91.75,  92.  ,  92.25,  92.5 ,  92.75,  93.  ,  93.25,
        93.5 ,  93.75,  94.  ,  94.25,  94.5 ,  94.75,  95.  ,  95.25,  95.5 ,
        95.75,  96.  ,  96.25,  96.5 ,  96.75,  97.  ,  97.25,  97.5 ,  97.75,
        98.  ,  98.25,  98.5 ,  98.75,  99.  ,  99.25,  99.5 ,  99.75, 100.  ])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>LATITUDE</span></div><div class='xr-var-dims'>(LATITUDE)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>6.5 6.75 7.0 ... 38.0 38.25 38.5</div><input id='attrs-17ee7630-35b7-480c-9479-09a4c51d269a' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-17ee7630-35b7-480c-9479-09a4c51d269a' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-6b1070b0-56e2-4674-a547-95109692b844' class='xr-var-data-in' type='checkbox'><label for='data-6b1070b0-56e2-4674-a547-95109692b844' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>units :</span></dt><dd>degrees_north</dd><dt><span>point_spacing :</span></dt><dd>even</dd><dt><span>axis :</span></dt><dd>Y</dd><dt><span>standard_name :</span></dt><dd>latitude</dd></dl></div><div class='xr-var-data'><pre>array([ 6.5 ,  6.75,  7.  ,  7.25,  7.5 ,  7.75,  8.  ,  8.25,  8.5 ,  8.75,
        9.  ,  9.25,  9.5 ,  9.75, 10.  , 10.25, 10.5 , 10.75, 11.  , 11.25,
       11.5 , 11.75, 12.  , 12.25, 12.5 , 12.75, 13.  , 13.25, 13.5 , 13.75,
       14.  , 14.25, 14.5 , 14.75, 15.  , 15.25, 15.5 , 15.75, 16.  , 16.25,
       16.5 , 16.75, 17.  , 17.25, 17.5 , 17.75, 18.  , 18.25, 18.5 , 18.75,
       19.  , 19.25, 19.5 , 19.75, 20.  , 20.25, 20.5 , 20.75, 21.  , 21.25,
       21.5 , 21.75, 22.  , 22.25, 22.5 , 22.75, 23.  , 23.25, 23.5 , 23.75,
       24.  , 24.25, 24.5 , 24.75, 25.  , 25.25, 25.5 , 25.75, 26.  , 26.25,
       26.5 , 26.75, 27.  , 27.25, 27.5 , 27.75, 28.  , 28.25, 28.5 , 28.75,
       29.  , 29.25, 29.5 , 29.75, 30.  , 30.25, 30.5 , 30.75, 31.  , 31.25,
       31.5 , 31.75, 32.  , 32.25, 32.5 , 32.75, 33.  , 33.25, 33.5 , 33.75,
       34.  , 34.25, 34.5 , 34.75, 35.  , 35.25, 35.5 , 35.75, 36.  , 36.25,
       36.5 , 36.75, 37.  , 37.25, 37.5 , 37.75, 38.  , 38.25, 38.5 ])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>TIME</span></div><div class='xr-var-dims'>(TIME)</div><div class='xr-var-dtype'>datetime64[ns]</div><div class='xr-var-preview xr-preview'>2020-01-01 ... 2020-12-31</div><input id='attrs-73216fcf-9b36-4693-bb27-9561ce1504b2' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-73216fcf-9b36-4693-bb27-9561ce1504b2' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-f5d583ac-2cfd-4904-ae33-c1f1495cd972' class='xr-var-data-in' type='checkbox'><label for='data-f5d583ac-2cfd-4904-ae33-c1f1495cd972' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>axis :</span></dt><dd>T</dd><dt><span>time_origin :</span></dt><dd>31-DEC-1900</dd><dt><span>standard_name :</span></dt><dd>time</dd></dl></div><div class='xr-var-data'><pre>array([&#x27;2020-01-01T00:00:00.000000000&#x27;, &#x27;2020-01-02T00:00:00.000000000&#x27;,
       &#x27;2020-01-03T00:00:00.000000000&#x27;, ..., &#x27;2020-12-29T00:00:00.000000000&#x27;,
       &#x27;2020-12-30T00:00:00.000000000&#x27;, &#x27;2020-12-31T00:00:00.000000000&#x27;],
      dtype=&#x27;datetime64[ns]&#x27;)</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-1c9176fb-91a6-4927-9e60-d7926646dfc4' class='xr-section-summary-in' type='checkbox'  checked><label for='section-1c9176fb-91a6-4927-9e60-d7926646dfc4' class='xr-section-summary' >Data variables: <span>(1)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span>RAINFALL</span></div><div class='xr-var-dims'>(TIME, LATITUDE, LONGITUDE)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-c9010c19-c582-43ed-aee1-1122739600d2' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-c9010c19-c582-43ed-aee1-1122739600d2' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-ef4754d0-d452-4df5-8bad-238c2e086ed4' class='xr-var-data-in' type='checkbox'><label for='data-ef4754d0-d452-4df5-8bad-238c2e086ed4' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Rainfall</dd><dt><span>units :</span></dt><dd>mm</dd><dt><span>history :</span></dt><dd>From ind2020_rfp25.grd</dd></dl></div><div class='xr-var-data'><pre>[6373890 values with dtype=float64]</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-3a0d25a7-676d-4abb-952a-80998eace1e0' class='xr-section-summary-in' type='checkbox'  ><label for='section-3a0d25a7-676d-4abb-952a-80998eace1e0' class='xr-section-summary' >Indexes: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-index-name'><div>LONGITUDE</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-e01bf2b4-761e-483a-a156-5fe57547bcc6' class='xr-index-data-in' type='checkbox'/><label for='index-e01bf2b4-761e-483a-a156-5fe57547bcc6' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(Index([ 66.5, 66.75,  67.0, 67.25,  67.5, 67.75,  68.0, 68.25,  68.5, 68.75,
       ...
       97.75,  98.0, 98.25,  98.5, 98.75,  99.0, 99.25,  99.5, 99.75, 100.0],
      dtype=&#x27;float64&#x27;, name=&#x27;LONGITUDE&#x27;, length=135))</pre></div></li><li class='xr-var-item'><div class='xr-index-name'><div>LATITUDE</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-8936da47-8562-433f-ba9c-d7da65f33376' class='xr-index-data-in' type='checkbox'/><label for='index-8936da47-8562-433f-ba9c-d7da65f33376' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(Index([  6.5,  6.75,   7.0,  7.25,   7.5,  7.75,   8.0,  8.25,   8.5,  8.75,
       ...
       36.25,  36.5, 36.75,  37.0, 37.25,  37.5, 37.75,  38.0, 38.25,  38.5],
      dtype=&#x27;float64&#x27;, name=&#x27;LATITUDE&#x27;, length=129))</pre></div></li><li class='xr-var-item'><div class='xr-index-name'><div>TIME</div></div><div class='xr-index-preview'>PandasIndex</div><div></div><input id='index-6e71abd0-4638-4ce1-a655-216229fb9876' class='xr-index-data-in' type='checkbox'/><label for='index-6e71abd0-4638-4ce1-a655-216229fb9876' title='Show/Hide index repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-index-data'><pre>PandasIndex(DatetimeIndex([&#x27;2020-01-01&#x27;, &#x27;2020-01-02&#x27;, &#x27;2020-01-03&#x27;, &#x27;2020-01-04&#x27;,
               &#x27;2020-01-05&#x27;, &#x27;2020-01-06&#x27;, &#x27;2020-01-07&#x27;, &#x27;2020-01-08&#x27;,
               &#x27;2020-01-09&#x27;, &#x27;2020-01-10&#x27;,
               ...
               &#x27;2020-12-22&#x27;, &#x27;2020-12-23&#x27;, &#x27;2020-12-24&#x27;, &#x27;2020-12-25&#x27;,
               &#x27;2020-12-26&#x27;, &#x27;2020-12-27&#x27;, &#x27;2020-12-28&#x27;, &#x27;2020-12-29&#x27;,
               &#x27;2020-12-30&#x27;, &#x27;2020-12-31&#x27;],
              dtype=&#x27;datetime64[ns]&#x27;, name=&#x27;TIME&#x27;, length=366, freq=None))</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-b02c51f5-68b2-4581-a093-02b4af4451cd' class='xr-section-summary-in' type='checkbox'  checked><label for='section-b02c51f5-68b2-4581-a093-02b4af4451cd' class='xr-section-summary' >Attributes: <span>(2)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'><dt><span>history :</span></dt><dd>FERRET V7.5 (optimized) 20-Jan-23</dd><dt><span>Conventions :</span></dt><dd>CF-1.6</dd></dl></div></li></ul></div></div>




```python
arr_lat = np.array(netcdf1['LATITUDE'])
arr_lon = np.array(netcdf1['LONGITUDE'])
arr_time = np.array(netcdf1['TIME'])

var_arr = netcdf1['RAINFALL']
var_arr[-1,:,:].plot()

```




    <matplotlib.collections.QuadMesh at 0x21ddc1deae0>




    
![png](11_Time_Series_Analysis_Part_II_files/11_Time_Series_Analysis_Part_II_3_1.png)
    



```python
user_lat = 23.21
user_lon = 77.40

closest_index_lat = np.argmin(np.abs(arr_lat-user_lat))
closest_index_lon = np.argmin(np.abs(arr_lon-user_lon))

closest_lat = arr_lat[closest_index_lat]
closest_lon = arr_lon[closest_index_lon]

name = str(closest_lat) + "_" + str(closest_lon)

arr_loc = var_arr[:,closest_index_lat,closest_index_lon]
df = pd.DataFrame({name:arr_loc}, index=arr_time)

df
```




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
      <th>23.25_77.5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-01-01</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2020-01-02</th>
      <td>1.103457</td>
    </tr>
    <tr>
      <th>2020-01-03</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2020-01-04</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2020-01-05</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>2020-12-27</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2020-12-28</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2020-12-29</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2020-12-30</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2020-12-31</th>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
<p>366 rows × 1 columns</p>
</div>




<iframe width="560" height="315" src="https://www.youtube.com/embed/-KF71FwBA1Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
