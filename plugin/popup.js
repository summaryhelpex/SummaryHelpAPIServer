
$(function(){
    chrome.storage.sync.get(['total'],function(selectedText){
        $('#article').val(selectedText.total);
    });
    $('#submit').click(function () {
        //var art = {'article' : $('#article').val()};
        //var new_art = JSON.stringify(art, ['article']);
        //new_art = new_art.serialize();
        var queryString = $('#textForm').serialize();
        console.log('hi');
        $.ajax({
            url:'http://13.209.8.253/summary_ajax/',
            //data : new_art,
            data: queryString,
            dataType:'json',
            type:'POST',
            cache : false,
            processData: false,
            success: function (data) {
                var new_data = data['article'];
                alert(new_data);
                //$('#result').html(new_data);
                // 임시로 그냥 new_data를 summayText textarea에 넣어주었다.
                $('#summary').val(new_data);

                //평가 html을 추가하고, click 이벤트를 넣어서 평가를 서버에 보내는 함수이다.
                $('#evaluate').load('evaluate.html',function(){
                    $('#eval').click(function () {
                        var evalValue = $('#evalForm').serialize();
                        $.ajax({
                            url: 'http://13.209.8.253/summary_ajax/',
                            data: evalValue,
                            dataType: 'json',
                            type:'POST',
                            success: function (data) {
                                alert('success')
                            }
                            ,error: function (request) {
                                alert('error')
                            }
                        })
                    });
                });


                //$('#result').text(result['article']);
                }
                ,error:function(request,status,error){
                    alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);}
            })
            chrome.storage.sync.get(['total'],function(selectedText){
                var newTotal = "";
                var article = $('#article').val();
                if (article){
                    newTotal += article;
                }
                chrome.storage.sync.set({'total': newTotal}, function(){               
                });
            });
        });
            /*
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
        })
    });
    */
});
