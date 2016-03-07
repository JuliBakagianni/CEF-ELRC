var donotclose = function () {
    $('.overlay').show();
    $('.uploadWin').show();
}

$(function () {
    $('form').submit(function (event) {
        if ($('#filebutton')[0].files[0].size > 52428800) {
            alert("The file you are trying to upload is larger " +
            "than the maximum upload file size (50mb)");
            return false;
        }
        return true;
    })
});


$(function () {
    var bar = $('.bar');
    var percent = $('.percent');
    var status = $('#status');
    var ok = $('#ok');
    $('form').ajaxForm({

        beforeSend: function () {
        var fileName = $('input[type=file]').val().split('/').pop().split('\\').pop();
            status.removeClass("success");
            status.html("Uploading file: \""+fileName+"\".\nPlease wait...");
            ok.hide();
            donotclose();
            var percentVal = '0%';
            bar.width(percentVal);
            percent.html(percentVal);

        },
        uploadProgress: function (event, position, total, percentComplete) {
            var percentVal = percentComplete + '%';
            bar.width(percentVal);
            percent.html(percentVal);
        },
        error: function () {
            $('.uploadWin').hide();
            $('.overlay').hide();
            alert("There was an error uploading this file. " +
            "Please try again later.");
        },
        complete: function () {
            status.addClass("success");
            status.html("Your data has been successfully submitted. " +
            "You can continue uploading more resources if you want.");
            ok.show();
            $('form').clearForm();
            //location.reload();
        }
    });
});
