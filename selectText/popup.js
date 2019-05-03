$(function(){

    chrome.storage.sync.get(['total'],function(selectedText){
        $('#total').text(selectedText.total);
    });

    $('#spendAmount').click(function(){
        chrome.storage.sync.get(['total'],function(selectedText){
            var newTotal = "";
            var amount = $('#amount').val();
            if (amount){
                newTotal += amount;
            }
            chrome.storage.sync.set({'total': newTotal}, function(){               
            });
            $('#total').text(newTotal);
            $('#amount').val('');
        });
    });
});