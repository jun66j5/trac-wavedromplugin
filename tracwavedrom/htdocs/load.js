jQuery(document).ready(function($) {
    WaveDrom.ProcessAll();
    $(document).ajaxComplete(function(event, xhr, settings) {
        if ($('script[type=WaveDrom]').length !== 0) {
            WaveDrom.ProcessAll();
        }
    });
});
