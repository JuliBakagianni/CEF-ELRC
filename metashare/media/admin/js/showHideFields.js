$(document).ready(function () {
    // show conditionsOfUse field only for specific licences
    var licences = ["openForReuseWithRestrictions", "non-standard/Other_Licence/Terms", "underNegotiation"];

        $("select option:selected").each(function () {
            if ($(this).val() != "non-standard/Other_Licence/Terms") {
                $(this).parent().parent().parent().siblings(".form-row.otherLicenceName").hide();
                $(this).parent().parent().parent().siblings(".form-row.termsOfUseText").hide();
                $(this).parent().parent().parent().siblings(".form-row.termsOfUseURL").hide();
            }
            if (jQuery.inArray($(this).val(), licences) != -1) {
                $(this).parent().parent().parent().siblings(".form-row.restrictionsOfUse").show();
            }
            else {
                $(this).parent().parent().parent().siblings(".form-row.restrictionsOfUse").hide();
            }

    })


    $('select').change(function () {
        if (jQuery.inArray($(this).val(), licences) != -1) {
            $(this).parent().parent().siblings(".form-row.restrictionsOfUse").show();
        }
        else {
            $(this).parent().parent().siblings(".form-row.restrictionsOfUse").hide();
        }
        if ($(this).val() == 'non-standard/Other_Licence/Terms') {
            $(this).parent().parent().siblings(".form-row.otherLicenceName").show();
            $(this).parent().parent().siblings(".form-row.otherLicenceName").find("input").removeAttr('disabled');
            $(this).parent().parent().siblings(".form-row.termsOfUseText").show();
            $(this).parent().parent().siblings(".form-row.termsOfUseURL").show();
        }
        else {
            $(this).parent().parent().siblings(".form-row.otherLicenceName").hide();
            $(this).parent().parent().siblings(".form-row.otherLicenceName").find("input").attr('disabled', 'disabled');
            $(this).parent().parent().siblings(".form-row.termsOfUseText").hide();
            $(this).parent().parent().siblings(".form-row.termsOfUseURL").hide();
        }
    });

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