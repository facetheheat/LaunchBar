/**
 * @author Pavel Miroshnichenko
 * @email pavel@miroshnichen.co
 **/

function run()
{
    LaunchBar.openCommandURL('x-launchbar:hide');
}

function runWithString(argument)
{
    LaunchBar.debugLog(argument);
    LaunchBar.openCommandURL('x-launchbar:hide');
    LaunchBar.executeAppleScriptFile('te_put.scpt', argument);
}