/**
 * @author Pavel Miroshnichenko
 * @email pavel@miroshnichen.co
 **/

function runWithString(argument)
{
    if (argument.length == 0){
        LaunchBar.debugLog("EMPTY");
        //return [{ title : "No arguments passed" }]
    } else {
        //creates 2 requests, getting labels and abbreviations
        //bad code
        var list_by_abbreviation = LaunchBar.executeAppleScriptFile('te_get_abbr.scpt', argument);
        var list_by_label = LaunchBar.executeAppleScriptFile('te_get_label.scpt', argument);
        LaunchBar.debugLog(list_by_abbreviation);
        LaunchBar.debugLog(list_by_label);

        //create array
        var list_by_abbreviation = list_by_abbreviation.split(' ');
        var list_by_label = list_by_label.split(' ');
        LaunchBar.debugLog(list_by_abbreviation);
        LaunchBar.debugLog(list_by_label);

        try {
                var launchbar_preview = [];
                var i = 0;
                for (i = 0; i < list_by_abbreviation.length; i++) {
                    var the_abbreviation = list_by_abbreviation[i];
                    var the_label = list_by_label[i];

                    //remove ',' from the end of item
                    if (the_abbreviation.substr(the_abbreviation.length - 1) === ','){
                        the_abbreviation = the_abbreviation.slice(0,-1);
                    }
                    LaunchBar.debugLog(the_abbreviation);
                    LaunchBar.debugLog(the_label);

                    launchbar_preview.push({
                                     'title' : the_abbreviation,
                                     'subtitle' : the_label,
                                     'icon' : 'com.smileonmymac.textexpander'
                                     });
                }
                return launchbar_preview;
        } catch (exception) {
            LaunchBar.log('Exception while parsing result: ' + exception);
            return [];
        }
    }
}
