Data Structures
~~~~~~~~~~~~~~~

Justcoin API
============

The justcoin API returns the following JSON format. For **markets**::

    [
       {
          "id":"BTCEUR",
          "last":"679.000",
          "high":"680.000",
          "low":"527.000",
          "bid":"610.000",
          "ask":"679.000",
          "volume":"27.86606",
          "scale":3
       },
       {
          "id":"BTCLTC",
          "last":"69.789",
          "high":"81.909",
          "low":"40.000",
          "bid":"69.243",
          "ask":"77.000",
          "volume":"9.39458",
          "scale":3
       },
       {
          "id":"BTCNOK",
          "last":"4864.000",
          "high":"4898.000",
          "low":"4348.206",
          "bid":"4600.001",
          "ask":"4898.000",
          "volume":"51.35807",
          "scale":3
       },
       {
          "id":"BTCUSD",
          "last":"890.000",
          "high":"890.000",
          "low":"680.000",
          "bid":"780.700",
          "ask":"890.000",
          "volume":"5.75107",
          "scale":3
       },
       {
          "id":"BTCXRP",
          "last":"61151.000",
          "high":"79000.000",
          "low":"60155.000",
          "bid":"61151.000",
          "ask":"89000.000",
          "volume":"4.75641",
          "scale":3
       }
    ]

The data is stored in the database in the exact same format, except every entry add a **date** field, which contains an ISO formatted timestamp (UTC) of the moment at which the data was retrieved.