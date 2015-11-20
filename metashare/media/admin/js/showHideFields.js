$(document).ready(function () {
    // show conditionsOfUse field only for specific licences
    var licences = ["openForReuseWithRestrictions", "non-standard/Other_Licence/Terms", "underNegotiation"];
    var licencesNoAttrAndFee = ['PSI-directive','CC-ZERO','PDDL','DL-DE-ZERO_Germany','non-standard/Other_Licence/Terms',
'underNegotiation'];
    var licenceAttrAndFee = ['OpenDataLicenceAtAFairCost_Belgium','OpenDataLicenceAtAFairCostForCommercialRe-use_Belgium'];

    $(".form-row.otherLicenceName input").each(function() {
            if($(this).val()!=""){
                var l = $(this).val();
                $(this).closest(".module.aligned").find(".otherLicence_TermsText label").text(l+" text:");
                $(this).closest(".module.aligned").find(".otherLicence_TermsURL label").text(l+" URL:");
            }
        });

        $("select option:selected").each(function () {
            if (jQuery.inArray($(this).val(), licencesNoAttrAndFee) != -1 || $(this).val() == ""){
                $(this).closest(".licence").siblings(".form-row.fee").hide();
                $(this).closest(".licence").siblings(".form-row.attributionText").hide();
            }
            else if(jQuery.inArray($(this).val(), licenceAttrAndFee) != -1){
                $(this).closest(".licence").siblings(".form-row.fee").show();
                $(this).closest(".licence").siblings(".form-row.attributionText").show();
            }
            else {
                $(this).closest(".licence").siblings(".form-row.fee").hide();
                $(this).closest(".licence").siblings(".form-row.attributionText").show();
            }
            if ($(this).val() != "non-standard/Other_Licence/Terms") {
                $(this).closest(".licence").siblings(".form-row.otherLicenceName").hide();
                $(this).closest(".licence").siblings(".form-row.otherLicence_TermsText").hide();
                $(this).closest(".licence").siblings(".form-row.otherLicence_TermsURL").hide();
            }
            if (jQuery.inArray($(this).val(), licences) != -1) {
                $(this).closest(".licence").siblings(".form-row.restrictionsOfUse").show();
            }
            else {
                $(this).closest(".licence").siblings(".form-row.restrictionsOfUse").hide();
            }

    })


    $(".form-row.otherLicenceName input").change(function() {
            if($(this).val()!=""){
                var l = $(this).val();
                $(this).closest(".module.aligned").find(".otherLicence_TermsText label").text(l+" text:");
                $(this).closest(".module.aligned").find(".otherLicence_TermsURL label").text(l+" URL:");
            }
    });

    $('select').change(function () {
        if (jQuery.inArray($(this).val(), licencesNoAttrAndFee) != -1 || $(this).val() == ""){
                $(this).closest(".licence").siblings(".form-row.fee").hide();
                $(this).closest(".licence").siblings(".form-row.attributionText").hide();
            }
            else if(jQuery.inArray($(this).val(), licenceAttrAndFee) != -1){
                $(this).closest(".licence").siblings(".form-row.fee").show();
                $(this).closest(".licence").siblings(".form-row.attributionText").show();
            }
            else {
                $(this).closest(".licence").siblings(".form-row.fee").hide();
                $(this).closest(".licence").siblings(".form-row.attributionText").show();
            }
        if (jQuery.inArray($(this).val(), licences) != -1) {
            $(this).parent().parent().siblings(".form-row.restrictionsOfUse").show();
        }
        else {
            $(this).parent().parent().siblings(".form-row.restrictionsOfUse").hide();
        }
        if ($(this).val() == 'non-standard/Other_Licence/Terms') {
            $(this).parent().parent().siblings(".form-row.otherLicenceName").show();
            $(this).parent().parent().siblings(".form-row.otherLicenceName").find("input").removeAttr('disabled');
            $(this).parent().parent().siblings(".form-row.otherLicence_TermsText").show();
            $(this).parent().parent().siblings(".form-row.otherLicence_TermsURL").show();
        }
        else {
            $(this).parent().parent().siblings(".form-row.otherLicenceName").hide();
            $(this).parent().parent().siblings(".form-row.otherLicenceName").find("input").attr('disabled', 'disabled');
            $(this).parent().parent().siblings(".form-row.otherLicence_TermsText").hide();
            $(this).parent().parent().siblings(".form-row.otherLicence_TermsURL").hide();
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

})(django.jQuery);