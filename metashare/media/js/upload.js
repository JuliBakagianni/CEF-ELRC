var donotclose = function () {
    $('.overlay').show();
    $('.uploadWin').show();
}

var disable_input = function (container) {
    container.find("input").prop('disabled', true);
    container.hide();
}

var enable_input = function (container) {
    container.find("input").prop('disabled', false);
    container.show();
}

$(document).ready(function () {
        var mode = $("#contributionmode input[type='radio']:checked").val();
        if (mode == "uploadzip") {
            disable_input($("#resourceurl"));
            enable_input($("#fileupload"));
        } else if (mode == "url") {
            disable_input($("#fileupload"));
            enable_input($("#resourceurl"));
        }
    }
);

$(function () {
        $("#contributionmode input[type='radio']").change(function () {
            mode = $(this).val();
            if (mode == "uploadzip") {
                disable_input($("#resourceurl"));
                enable_input($("#fileupload"));
            } else if (mode == "url") {
                disable_input($("#fileupload"));
                enable_input($("#resourceurl"));
            }
        })
    }
)

$(function () {
    $('form').submit(function (event) {
        if ($('#filebutton')[0].files[0].size > 52428800) {
            alert("The file you are trying to upload is larger " +
                "than the maximum upload file size (50mb).\n" +
                "Please contact elrc-share@ilsp.gr");
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

        beforeSend: function (xhr, opts) {
        var fileName = $('input[type=file]').val().split('/').pop().split('\\').pop();
            if (!fileName.endsWith(".zip")){
                xhr.abort();
                alert("The file you are trying to upload does not have a .zip extension.\n" +
                    "Please make sure that you properly compress your data into a valid .zip file before uploading.");
                return false
            }
            status.removeClass("success");
            status.html("Uploading file: \"" + fileName + "\".\nPlease wait...");
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
            alert("There was an error uploading this file.\n" +
                "Please make sure that you are trying to upload a valid '.zip' file.\n" +
                "If the problem persists please try again later.");
        },
        complete: function (response) {
            var json_response = JSON.parse(response.responseText);
            if(json_response.status == 'failed'){
                status.addClass("failure")
                bar.hide();
                percent.hide();
                $(".progress").hide();
            } else {
                status.removeClass("failure");
                status.addClass("success");
                $('form').clearForm();
            }
            status.html(json_response.message);
            ok.show();
            //location.reload();
        }
    });
});
