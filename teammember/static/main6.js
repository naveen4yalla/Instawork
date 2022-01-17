function phone_formatting(ele,restore) {
    var new_number,
        selection_start = ele.selectionStart,
        selection_end = ele.selectionEnd,
        number = ele.value.replace(/\D/g,'');
    
    
    if (number.length > 2) {
      
      new_number = number.substring(0,3) + '-';
      if (number.length === 4 || number.length === 5) {
        
        new_number += number.substr(3);
      }
      else if (number.length > 5) {
        new_number += number.substring(3,6) + '-';
      }
      if (number.length > 6) {
        new_number += number.substring(6);
      }
    }
    else {
      new_number = number;
    }
    
    ele.value =  (new_number.length > 12) ? new_number.substring(12,0) : new_number;
    
    
    
    if (new_number.slice(-1) === '-' && restore === false
        && (new_number.length === 8 && selection_end === 7)
            || (new_number.length === 4 && selection_end === 3)) {
        selection_start = new_number.length;
        selection_end = new_number.length;
    }
    else if (restore === 'revert') {
      selection_start--;
      selection_end--;
    }
    ele.setSelectionRange(selection_start, selection_end);
  
  }
    
  function phone_number_check(field,e) {
    var key_code = e.keyCode,
        key_string = String.fromCharCode(key_code),
        press_delete = false,
        dash_key = 189,
        delete_key = [8,46],
        direction_key = [33,34,35,36,37,38,39,40],
        selection_end = field.selectionEnd;
    if (delete_key.indexOf(key_code) > -1) {
      press_delete = true;
    }
    
    
    if (key_string.match(/^\d+$/) || press_delete) {
      phone_formatting(field,press_delete);
    }
  
    else if(direction_key.indexOf(key_code) > -1) {
     
    }
    else if(dash_key === key_code) {
      if (selection_end === field.value.length) {
        field.value = field.value.slice(0,-1)
      }
      else {
        field.value = field.value.substring(0,(selection_end - 1)) + field.value.substr(selection_end)
        field.selectionEnd = selection_end - 1;
      }
    }
    else {
      e.preventDefault();
      phone_formatting(field,'revert');
    }
  
  }
  var toggleMenuClick = function() {
    $('[for="id_choice_1"]').css("opacity", "0.5");
    $('[for="id_choice_0"]').css("opacity", "1");
    $('#id_choice_0').prop("checked", true);
    $('#id_choice_1').prop("checked", false);
  
} 
var toggleMenuClick1 = function() {
  $('[for="id_choice_0"]').css("opacity", "0.5");
        $('[for="id_choice_1"]').css("opacity", "1");
        $('#id_choice_0').prop("checked", false);
        $('#id_choice_1').prop("checked", true);
}

var phone_slicing = function(){
  if (document.getElementById("delete_id")){
    var value = document.getElementById("id_phone").value
    value = value.slice(0,3)+"-"+value.slice(3,6)+"-"+value.slice(6,10)
    document.getElementById("id_phone").value = value
   
     document.getElementsByClassName("headings")[0].innerHTML ="Edit Page"
     document.getElementsByClassName("headings")[1].innerHTML = "Edit team member"
     document.getElementsByClassName("headings")[2].innerHTML = "Edit contact info and location"
 }
}
  
  