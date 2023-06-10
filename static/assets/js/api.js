$(document).ready(function() {
    // Collapse/expand sections as at when clicked
    $('.endpoint h2').click(function() {
      $(this).next().slideToggle();
    });

    // Makess the API requests
    $('#get-resources').click(function() {
      $.ajax({
        url: '/resources',
        method: 'GET',
        success: function(response) {
          // Handles the response data
          console.log(response);
        }
      });
    });

    $('#get-resource').click(function() {
      var resourceId = 1; 
      $.ajax({
        url: '/resources/' + resourceId,
        method: 'GET',
        success: function(response) {
          console.log(response);
        }
      });
    });

    $('#create-resource').click(function() {
      var resourceData = {
        title: 'New Resource',
        description: 'Resource Description',
        link: 'https://eudaimonia.onrender.com/resources'
      };
      $.ajax({
        url: '/resources',
        method: 'POST',
        data: JSON.stringify(resourceData),
        contentType: 'application/json',
        success: function(response) {
          // Handle the response data
          console.log(response);
        }
      });
    });

    $('#update-resource').click(function() {
      var resourceId = 1;
      var updatedResourceData = {
        title: 'Updated Resource',
        description: 'Updated Description',
        link: 'https://eudaimonia.onrender.com/resources/updated'
      };
      $.ajax({
        url: '/resources/' + resourceId,
        method: 'PUT',
        data: JSON.stringify(updatedResourceData),
        contentType: 'application/json',
        success: function(response) {
          console.log(response);
        }
      });
    });

    $('#delete-resource').click(function() {
      var resourceId = 1; 
      $.ajax({
        url: '/resources/' + resourceId,
        method: 'DELETE',
        success: function(response) {
          console.log(response);
        }
      });
    });
  });
