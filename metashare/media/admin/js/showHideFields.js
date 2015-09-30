$(document).ready(function () {
    // show restrictionsOfUse field only for specific licences
    var licences = ["openForReuseWithRestrictions", "termsOfUse", "proprietary", "underNegotiation", "other"];
    $("select option:selected").each(function () {
        if (jQuery.inArray($(this).val(), licences) != -1) {
            $(this).parent().parent().parent().siblings(".form-row.restrictionsOfUse").show();
        }
        else {
            $(this).parent().parent().parent().siblings(".form-row.restrictionsOfUse").hide();
        }
    });

    $('select').on('change', function () {
        if (jQuery.inArray($(this).val(), licences) != -1) {
            $(this).parent().parent().siblings(".form-row.restrictionsOfUse").show();
        }
        else {
            $(this).parent().parent().siblings(".form-row.restrictionsOfUse").hide();
        }
    })

    //show additional information if respective boolean field is checked
    $("input[id*='personalDataIncluded']").each(function () {
        $(this).parent().parent().next().find("textarea").attr({
            "rows": "2",
            "cols": "10"
        });
        if (!this.checked) {
            $(this).parent().parent().next().hide();
        }
    })

    $("input[id*='sensitiveDataIncluded']").each(function () {
        $(this).parent().parent().next().find("textarea").attr({
            "rows": "2",
            "cols": "10"
        });
        if (!this.checked) {
            $(this).parent().parent().next().hide();
        }
    })

    $("input[id*='personalDataIncluded']").change(function () {
        if (!this.checked) {
            $(this).parent().parent().next().hide();
            $(this).parent().parent().next().find("textarea").attr('disabled', 'disabled');
            //$(this).parent().parent().next().find( "textarea" ).val("");
        } else {
            $(this).parent().parent().next().show();
            $(this).parent().parent().next().find("textarea").removeAttr('disabled');
        }
    });

    $("input[id*='sensitiveDataIncluded']").change(function () {
        if (!this.checked) {
            $(this).parent().parent().next().hide();
            $(this).parent().parent().next().find("textarea").val("");
        } else {
            $(this).parent().parent().next().show();
            $(this).parent().parent().next().removeAttr('disabled');
        }
    })

});