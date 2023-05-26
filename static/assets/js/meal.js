document.getElementById('grocery').addEventListener('click', function() {
    var table = document.getElementById('gtable');
    if (table.style.display === 'none') {
      // The table is hidden, so show it
      var xhr = new XMLHttpRequest();
      xhr.open('GET', '/grocery', true);
      xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
      xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
          var data = JSON.parse(xhr.responseText);
          // Clear the table body
          var tbody = table.getElementsByTagName('tbody')[0];
          tbody.innerHTML = '';
          // Add the data to the table
          for (var i = 0; i < data.length; i++) {
            var row = tbody.insertRow();
            var DateCell = row.insertCell();
            var ItemCell = row.insertCell();
            DateCell.appendChild(document.createTextNode(data[i].Date));
            ItemCell.appendChild(document.createTextNode(data[i].Item));
          }
          // Show the table
          table.style.display = 'block';
        }
      };
      xhr.send();
    } else {
      // The table is visible, so hide it
      table.style.display = 'none';
    }
  });
  
  
  
    function update(food) {
        var Date = food.cells[0].textContent;
        var BreakFast = food.cells[1].textContent;
        var Lunch = food.cells[2].textContent;
        var Dinner = food.cells[3].textContent;
  
      // Send the updated data to the server
      var xhr = new XMLHttpRequest();
        xhr.open('POST', '/update', true);
        xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
        xhr.send(JSON.stringify({
          'Date': Date,
          'BreakFast': BreakFast,
          'Lunch': Lunch,
          'Dinner': Dinner
        }));
    }
  
    document.addEventListener('blur', function(e) {
      if (e.target.matches('td[contenteditable]')) {
        update(e.target.parentElement);
      }
    }, true);


    function show() {
      var table = document.getElementById("gtabe");
      if (table.style.display === "none") {
        table.style.display = "table";
      } else {
        table.style.display = "none";
      }
    }
    