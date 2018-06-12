# Quandl-Python-API-Wrapper
A simple API wrapper for parsing requests from Quandl. 
Quandl is a marketplace for financial, economic and alternative data delivered in modern formats for today's analysts.

### The full documentation for Quandl's API can be found here: (https://docs.quandl.com/docs/in-depth-usage)

## How to use:
- The parse() function will take in the following parameters:
  - data_type: either "datatables" for table data or "datasets" for time series data
  - data_name and data_code is explained in the full API documentation. These are used to identify the data to be retrieved, and can be found in their repective web pages on Quandl.com
  - outout_format: the output can be in json, xml, or csv
  - options: additional data slicing tools to refine your data parse. Refer to the API documentation for the full list of commands
  
## Examples:
To retrieve a time series:
```
out = req.query("datasets","FRED","GDP","csv",{"collapse":"annual","rows":6,"order":"asc","column_index":1}) 
```
```
DATE,VALUE
1947-12-31,260.3
1948-12-31,280.7
1949-12-31,271
1950-12-31,320.3
1951-12-31,356.6
1952-12-31,381.2
```

To retrive a data table:
```
out = req.query("datatables","MER","F1","xml",{"mapcode":-5370,"compnumber":39102,"reporttype":"A","qopts.columns":"reportdate,amount"}) 
```
```
<quandl-response>
<datatable>
<data type="array">
<datum type="array">
<datum type="date">2005-12-31</datum>
<datum type="float">7.832008</datum>
</datum>
<datum type="array">
<datum type="date">2006-12-31</datum>
<datum type="float">10.121263</datum>
</datum>
<datum type="array">
<datum type="date">2007-12-31</datum>
<datum type="float">13.140962</datum>
</datum>
<datum type="array">
<datum type="date">2008-12-31</datum>
<datum type="float">13.508695</datum>
</datum>
<datum type="array">
<datum type="date">2009-12-31</datum>
<datum type="float">11.061462</datum>
</datum>
<datum type="array">
<datum type="date">2010-12-31</datum>
<datum type="float">11.444623</datum>
</datum>
<datum type="array">
<datum type="date">2011-12-31</datum>
<datum type="float">10.420364</datum>
</datum>
<datum type="array">
<datum type="date">2012-12-31</datum>
<datum type="float">8.109622</datum>
</datum>
<datum type="array">
<datum type="date">2013-12-31</datum>
<datum type="float">3.423688</datum>
</datum>
<datum type="array">
<datum type="date">2014-12-31</datum>
<datum type="float">3.442269</datum>
</datum>
<datum type="array">
<datum type="date">2015-12-31</datum>
<datum type="float">3.404856</datum>
</datum>
</data>
<columns type="array">
<column>
<name>reportdate</name>
<type>Date</type>
</column>
<column>
<name>amount</name>
<type>BigDecimal(36,14)</type>
</column>
</columns>
</datatable>
<meta>
<next-cursor-id nil="true"/>
</meta>
</quandl-response>
```




