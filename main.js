
(function (document) {
    'use strict';
    var LightTableFilter = (function (Arr) {

        var _input;
        var display;
        function _onInputEvent(e) {
            _input = e.target;
            var tables = document.getElementsByClassName(_input.getAttribute('data-table'));
            Arr.forEach.call(tables, function (table) {
                table.style.display = "table"
                console.log(table)
                display = 0
                Arr.forEach.call(table.tBodies, function (tbody) {
                    Arr.forEach.call(tbody.rows, _filter);
                    console.log(display)
                    if (display == 0) table.style.display = "none";
                });
            });
        }

        function _filter(row) {
            var text = row.textContent.toLowerCase(), val = _input.value.toLowerCase();
            if (text.indexOf(val) === -1) {
                row.style.display = 'none'
            } else {
                display += 1
                row.style.display = 'table-row';
            }

        }

        return {
            init: function () {
                var inputs = document.getElementsByClassName('light-table-filter');
                Arr.forEach.call(inputs, function (input) {
                    input.oninput = _onInputEvent;
                });
            }
        };
    })(Array.prototype);
    // function checkAwaited() {
    //     var checkbox = document.getElementById('await');

    //     if (checkbox.checked === true) {
    //         console.log("yes")
    //         var tables = document.getElementsByClassName('table');
    //         [].forEach.call(tables, function (table) {
    //             table.style.display = "table"
    //             console.log(table);
    //             [].forEach.call(table.tBodies, function (tbody) {
    //                 _input = "awaiting";
    //                 [].forEach.call(tbody.rows, _filter);
    //                 console.log(display)
    //                 if (display == 0) table.style.display = "none";
    //             });
    //         });
    //     }
    // }

    document.addEventListener('readystatechange', function () {
        if (document.readyState === 'complete') {
            LightTableFilter.init();
            // checkAwaited()
        }  
    });

})(document);
