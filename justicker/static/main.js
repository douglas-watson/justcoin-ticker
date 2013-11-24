/*
 * main.js
 * ~~~~~~~
 *
 * Main front-end code for the Justcoin ticker app.
 *
 * :copyright: 2013, Douglas C. Watson
 * :license: MIT license.
 */

 $(function() {
    console.log("Fetching JSON");
    $.getJSON('/api/markets/BTCEUR', function(data) {

        // create the chart
        $('#container').highcharts('StockChart', {
            

            rangeSelector : {
                selected : 1
            },

            title : {
                text : 'Justcoin BTC to EUR rates'
            },

            series : [{
                type : 'candlestick',
                name : 'BTCEUR',
                data : data,
                dataGrouping : {
                    units : [
                        ['week', // unit name
                        [1] // allowed multiples
                    ], [
                        'month', 
                        [1, 2, 3, 4, 6]]
                    ]
                }
            }]
        });
    });
});