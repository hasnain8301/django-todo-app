function checkBoxClicked() {
    // Get the checkbox
    var checkBox = document.getElementById("checkBox-1");
    // Get the output text
    var text = document.getElementById("text-1");
  
    // If the checkbox is checked, display the output text
    if (checkBox.checked == true){
        // $.ajax({url: "demo_test.txt", success: function(result){
        //     $("#div1").html(result);
        //   }});
        location.reload();
    } else {
      text.style.display = "none";
    }
  }
  