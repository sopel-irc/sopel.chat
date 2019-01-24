---
title: Module commands
order: 10
---

| Commands | Purpose | Example | Module |
| -------- | ------- | ------- | ------ |
| .afraid | *No documentation found.* | .afraid | emoticons |
| .rage<br>.anger | *No documentation found.* | .anger | emoticons |
| .announce | <br>    Send an announcement to all channels the bot is in<br>     | .announce Some important message here | announce |
| .at | <br>    Gives you a reminder at the given time. Takes hh:mm:ssTimezone<br>    message. Timezone is any timezone Sopel takes elsewhere; the best choices<br>    are those from the tzdb; a list of valid options is available at<br>    https://sopel.chat/tz . The seconds and timezone are optional.<br>     | .at 13:47 Do your homework! | remind |
| .ban | <br>    This give admins the ability to ban a user.<br>    The bot must be a Channel Operator for this command to work.<br>     |  | adminchannel |
| .bing | Queries Bing for the specified input. | .bing sopel irc bot | search |
| .btc<br>.bitcoin | *No documentation found.* | .btc 20 EUR | currency |
| .blocks | Manage Sopel's blocking features.<br><br>    https://github.com/sopel-irc/sopel/wiki/Making-Sopel-ignore-people<br><br>     |  | coretasks |
| .c<br>.calc | Evaluate some calculation. | .c 5 / 2 | calc |
| .chairs | <br>    Set the meeting chairs.<br>    https://github.com/sopel-irc/sopel/wiki/Using-the-meetbot-module<br>     | .chairs Tyrope Jason elad | meetbot |
| .choose<br>.ch<br>.choice | <br>    .choice option1|option2|option3 - Makes a difficult choice easy.<br>     |  | dice |
| .u | *No documentation found.* | .u 203D | unicode_info |
| .crazy | *No documentation found.* | .crazy | emoticons |
| .cry | *No documentation found.* | .cry | emoticons |
| .length<br>.distance | <br>    Convert distances<br>     | .length 3 parsec | units |
| .duck<br>.ddg<br>.g | Queries Duck Duck Go for the specified input. | .duck sopel irc bot | search |
| .useserviceauth | *No documentation found.* |  | coretasks |
| .endmeeting | <br>    End a meeting.<br>    https://github.com/sopel-irc/sopel/wiki/Using-the-meetbot-module<br>     | .endmeeting | meetbot |
| .cur<br>.currency<br>.exchange | Show the exchange rate between two currencies | .cur 20 EUR in USD | currency |
| .ety | Look up the etymology of a word | .ety word | etymology |
| .tell<br>.ask | Give someone a message the next time they're seen | Sopel, tell Embolalia he broke something again. | tell |
| .t<br>.time | Returns the current time. | .t America/New_York | clock |
| .countdown | <br>    .countdown <year> <month> <day> - displays a countdown to a given date.<br>     |  | countdown |
| .getchanneltimeformat<br>.getctf | <br>    Gets the channel's preferred time format, will return current channel's if<br>    no channel name is given<br>     | .getctf [channel] | clock |
| .getsafeforwork<br>.getsfw | <br>    Gets the preferred channel's Safe for Work status, or the current<br>    channel's status if no channel given.<br>     | .getsfw [channel] | reddit |
| .getchanneltz<br>.getctz | <br>    Gets the preferred channel timezone, or the current channel timezone if no<br>    channel given.<br>     | .getctz [channel] | clock |
| .gettimeformat<br>.gettf | <br>    Gets a user's preferred time format, will show yours if no user specified<br>     | .gettf [nick] | clock |
| .gettz<br>.gettimezone | <br>    Gets a user's preferred time zone, will show yours if no user specified<br>     | .gettz [nick] | clock |
| .tld | Show information about the given Top Level Domain. | .tld ru | tld |
| .lmgtfy<br>.lmgify<br>.gify<br>.gtfy | Let me just... google that for you. | .lmgtfy | lmgtfy |
| .happy | *No documentation found.* | .happy | emoticons |
| .help<br>.commands | Shows a command's documentation, and possibly an example. | .help tell | help |
| .hungry | *No documentation found.* | .hungry | emoticons |
| .console | <br>    Starts an interactive IPython console<br>     |  | ipython |
| .iplookup<br>.ip | IP Lookup tool | .ip 8.8.8.8 | ip |
| .isup<br>.isupinsecure | isup.me website status checker |  | isup |
| .join | Join the specified channel. This is an admin-only command. | .join #example or .join #example key | admin |
| .kick | <br>    Kick a user from the channel.<br>     |  | adminchannel |
| .kickban<br>.kb | <br>    This gives admins the ability to kickban a user.<br>    The bot must be a Channel Operator for this command to work.<br>    .kickban [#chan] user1 user!*@* get out of here<br>     |  | adminchannel |
| .lenny | *No documentation found.* | .lenny | emoticons |
| .listactions | *No documentation found.* | .listactions | meetbot |
| .love | *No documentation found.* | .love | emoticons |
| .mangle<br>.mangle2 | Repeatedly translate the input until it makes absolutely no sense. |  | translate |
| .weight<br>.mass | <br>    Convert mass<br>     |  | units |
| .me | <br>    Send an ACTION (/me) to a given channel or nick. Can only be done in privmsg<br>    by an admin.<br>     |  | admin |
| .action | <br>    Log an action in the meeting log<br>    https://github.com/sopel-irc/sopel/wiki/Using-the-meetbot-module<br>     | .action elad will develop a meetbot | meetbot |
| .agreed | <br>    Log an agreement in the meeting log.<br>    https://github.com/sopel-irc/sopel/wiki/Using-the-meetbot-module<br>     | .agreed Bowties are cool | meetbot |
| .info | <br>    Log an informational item in the meeting log<br>    https://github.com/sopel-irc/sopel/wiki/Using-the-meetbot-module<br>     | .info all board members present | meetbot |
| .link | <br>    Log a link in the meeing log.<br>    https://github.com/sopel-irc/sopel/wiki/Using-the-meetbot-module<br>     | .link http://example.com | meetbot |
| .subject | <br>    Change the meeting subject.<br>    https://github.com/sopel-irc/sopel/wiki/Using-the-meetbot-module<br>     | .subject roll call | meetbot |
| .mode | Set a user mode on Sopel. Can only be done in privmsg by an admin. |  | admin |
| .msg | <br>    Send a message to a given channel or nick. Can only be done in privmsg by an<br>    admin.<br>     | .msg #YourPants Does anyone else smell neurotoxin? | admin |
| .part | Part the specified channel. This is an admin-only command. | .part #example | admin |
| .load | Wrapper for allowing delivery of .load command via PM |  | reload |
| .reload | Wrapper for allowing delivery of .reload command via PM |  | reload |
| .update | Wrapper for allowing delivery of .update command via PM |  | reload |
| .pronouns | *No documentation found.* | .pronouns Embolalia | pronouns |
| .py | Evaluate a Python expression. | .py len([1,2,3]) | calc |
| .quiet | <br>    This gives admins the ability to quiet a user.<br>    The bot must be a Channel Operator for this command to work.<br>     |  | adminchannel |
| .quit | Quit from the server. This is an owner-only command. |  | admin |
| .rand | Replies with a random number between first and second argument. | .rand 10 99 | rand |
| .redditor | Show information about the given Redditor | .redditor poem_for_your_sprog | reddit |
| .in | Gives you a reminder in the given amount of time. | .in 3h45m Go to class | remind |
| .d<br>.dice<br>.roll | .dice XdY[vZ][+N], rolls dice and reports the result.<br><br>    X is the number of dice. Y is the number of faces in the dice. Z is the<br>    number of lowest dice to be dropped from the result. N is the constant to<br>    be applied to the end result.<br>     | .roll 1d1+1d1 | dice |
| .save | Save state of sopels config object to the configuration file. | .save | admin |
| .search | Searches Bing and Duck Duck Go. | .search sopel irc bot | search |
| .seen | Reports when and where the user was last seen. |  | seen |
| .set | See and modify values of sopels config object.<br><br>    Trigger args:<br>        arg1 - section and option, in the form "section.option"<br>        arg2 - value<br><br>    If there is no section, section will default to "core".<br>    If value is None, the option will be deleted.<br>     | .set core.owner Me | admin |
| .tmask | <br>    Set the mask to use for .topic in the current channel. {} is used to allow<br>    substituting in chunks of text.<br>     |  | adminchannel |
| .setpronouns | *No documentation found.* | .setpronouns they/them/their/theirs/themselves | pronouns |
| .comments | <br>    Show the comments that have been logged for this meeting with .comment.<br>    https://github.com/sopel-irc/sopel/wiki/Using-the-meetbot-module<br>     |  | meetbot |
| .showmask | Show the topic mask for the current channel. |  | adminchannel |
| .shrug | *No documentation found.* | .shrug | emoticons |
| .sick | *No documentation found.* | .sick | emoticons |
| .spellcheck<br>.spell | <br>    Says whether the given word is spelled correctly, and gives suggestions if<br>    it's not.<br>     | .spellcheck stuff | spellcheck |
| .startmeeting | <br>    Start a meeting.<br>    https://github.com/sopel-irc/sopel/wiki/Using-the-meetbot-module<br>     | .startmeeting title or .startmeeting | meetbot |
| .success<br>.winner | *No documentation found.* | .winner | emoticons |
| .suggest | Suggest terms starting with given input | .suggest lkashdfiauwgeaef | search |
| .surprised | *No documentation found.* | .surprised | emoticons |
| .tableflip<br>.tflip | *No documentation found.* | .tflip | emoticons |
| .comment | <br>    Log a comment, to be shown with other comments when a chair uses .comments.<br>    Intended to allow commentary from those outside the primary group of people<br>    in the meeting.<br><br>    Used in private message only, as `.comment <#channel> <comment to add>`<br>    https://github.com/sopel-irc/sopel/wiki/Using-the-meetbot-module<br>     |  | meetbot |
| .temp | <br>    Convert temperatures<br>     | .temp 100K | units |
| .title | <br>    Show the title or URL information for the given URL, or the last URL seen<br>    in this channel.<br>     | .title http://google.com | url |
| .safety |  Set safety setting for channel  |  | safety |
| .topic | <br>    This gives ops the ability to change the topic.<br>    The bot must be a Channel Operator for this command to work.<br>     |  | adminchannel |
| .translate<br>.tr | Translates a phrase, with an optional language hint. | .tr mon chien | translate |
| .unban | <br>    This give admins the ability to unban a user.<br>    The bot must be a Channel Operator for this command to work.<br>     |  | adminchannel |
| .unflip | *No documentation found.* | .unflip | emoticons |
| .unquiet | <br>    This gives admins the ability to unquiet a user.<br>    The bot must be a Channel Operator for this command to work.<br>     |  | adminchannel |
| .setchanneltz<br>.setctz | <br>    Set the preferred time zone for the channel.<br>     | .setctz America/New_York | clock |
| .setsafeforwork<br>.setsfw | <br>    Sets the Safe for Work status (true or false) for the current<br>    channel. Defaults to false.<br>     | .setsfw false | reddit |
| .setchanneltimeformat<br>.setctf | <br>    Sets your preferred format for time. Uses the standard strftime format. You<br>    can use http://strftime.net or your favorite search engine to learn more.<br>     | .setctf %Y-%m-%dT%T%z | clock |
| .settz<br>.settimezone | <br>    Set your preferred time zone. Most timezones will work, but it's best to<br>    use one from https://sopel.chat/tz<br>     | .settz America/New_York | clock |
| .settimeformat<br>.settf | <br>    Sets your preferred format for time. Uses the standard strftime format. You<br>    can use http://strftime.net or your favorite search engine to learn more.<br>     | .settf %Y-%m-%dT%T%z | clock |
| .uptime | .uptime - Returns the uptime of Sopel. |  | uptime |
| .version | Display the latest commit version, if Sopel is running in a git repo. |  | version |
| .confused<br>.wat | *No documentation found.* | .wat | emoticons |
| .w<br>.wiki<br>.wik | *No documentation found.* | .w San Francisco | wikipedia |
| .wt<br>.define<br>.dict | Look up a word on Wiktionary. | .wt bailiwick | wiktionary |
| .worried | *No documentation found.* | .worried | emoticons |
| .xkcd | <br>    .xkcd - Finds an xkcd comic strip. Takes one of 3 inputs:<br>    If no input is provided it will return a random comic<br>    If numeric input is provided it will return that comic, or the nth-latest<br>    comic if the number is non-positive<br>    If non-numeric input is provided it will return the first google result for those keywords on the xkcd.com site<br>     |  | xkcd |
