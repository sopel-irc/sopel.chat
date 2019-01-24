---
title: Module commands
order: 10
---

This page contains a list of all commands from modules within Sopel's
main modules directory. If you have added modules without rebuilding
the documentation, or are using a secondary modules directory, those
modules will not be shown here.

| Command(s) | Purpose | Example | Module |
| ---------- | ------- | ------- | ------ |
| .join | Join the specified channel. This is an admin-only command. | .join #example or .join #example key | admin |
| .me | Send an ACTION (/me) to a given channel or nick. Can only be done in privmsg<br>by an admin. |  | admin |
| .mode | Set a user mode on Sopel. Can only be done in privmsg by an admin. |  | admin |
| .msg | Send a message to a given channel or nick. Can only be done in privmsg by an<br>admin. | .msg #YourPants Does anyone else smell neurotoxin? | admin |
| .part | Part the specified channel. This is an admin-only command. | .part #example | admin |
| .quit | Quit from the server. This is an owner-only command. |  | admin |
| .save | Save state of sopels config object to the configuration file. | .save | admin |
| .set | See and modify values of sopels config object.<br><br>Trigger args:<br>    arg1 - section and option, in the form "section.option"<br>    arg2 - value<br><br>If there is no section, section will default to "core".<br>If value is None, the option will be deleted. | .set core.owner Me | admin |
| .ban | This give admins the ability to ban a user.<br>The bot must be a Channel Operator for this command to work. |  | adminchannel |
| .kick | Kick a user from the channel. |  | adminchannel |
| .kickban<br>.kb | This gives admins the ability to kickban a user.<br>The bot must be a Channel Operator for this command to work.<br>.kickban [#chan] user1 user!*@* get out of here |  | adminchannel |
| .quiet | This gives admins the ability to quiet a user.<br>The bot must be a Channel Operator for this command to work. |  | adminchannel |
| .tmask | Set the mask to use for .topic in the current channel. {} is used to allow<br>substituting in chunks of text. |  | adminchannel |
| .showmask | Show the topic mask for the current channel. |  | adminchannel |
| .topic | This gives ops the ability to change the topic.<br>The bot must be a Channel Operator for this command to work. |  | adminchannel |
| .unban | This give admins the ability to unban a user.<br>The bot must be a Channel Operator for this command to work. |  | adminchannel |
| .unquiet | This gives admins the ability to unquiet a user.<br>The bot must be a Channel Operator for this command to work. |  | adminchannel |
| .announce | Send an announcement to all channels the bot is in | .announce Some important message here | announce |
| .c<br>.calc | Evaluate some calculation. | .c 5 / 2 | calc |
| .py | Evaluate a Python expression. | .py len([1,2,3]) | calc |
| .t<br>.time | Returns the current time. | .t America/New_York | clock |
| .getchanneltimeformat<br>.getctf | Gets the channel's preferred time format; will return current channel's if<br>no channel name is given | .getctf [channel] | clock |
| .getchanneltz<br>.getctz | Gets the channel's preferred timezone; returns the current channel's<br>if no channel given. | .getctz [channel] | clock |
| .gettimeformat<br>.gettf | Gets a user's preferred time format; will show yours if no user specified. | .gettf [nick] | clock |
| .gettz<br>.gettimezone | Gets a user's preferred time zone; will show yours if no user specified | .gettz [nick] | clock |
| .setchanneltz<br>.setctz | Set the preferred timezone for the channel. | .setctz America/New_York | clock |
| .setchanneltimeformat<br>.setctf | Sets your preferred format for time. Uses the standard strftime format. You<br>can use <http://strftime.net> or your favorite search engine to learn more. | .setctf %Y-%m-%dT%T%z | clock |
| .settz<br>.settimezone | Set your preferred time zone. Most timezones will work, but it's best to<br>use one from <https://sopel.chat/tz> | .settz America/New_York | clock |
| .settimeformat<br>.settf | Sets your preferred format for time. Uses the standard strftime format. You<br>can use <http://strftime.net> or your favorite search engine to learn more. | .settf %Y-%m-%dT%T%z | clock |
| .countdown | .countdown <year> <month> <day> - displays a countdown to a given date. |  | countdown |
| .btc<br>.bitcoin | *No documentation found.* | .btc 20 EUR | currency |
| .cur<br>.currency<br>.exchange | Show the exchange rate between two currencies | .cur 20 EUR in USD | currency |
| .choose<br>.ch<br>.choice | .choice option1|option2|option3 - Makes a difficult choice easy. |  | dice |
| .d<br>.dice<br>.roll | .dice XdY[vZ][+N], rolls dice and reports the result.<br><br>X is the number of dice. Y is the number of faces in the dice. Z is the<br>number of lowest dice to be dropped from the result. N is the constant to<br>be applied to the end result. | .roll 1d1+1d1 | dice |
| .afraid | *No documentation found.* | .afraid | emoticons |
| .rage<br>.anger | *No documentation found.* | .anger | emoticons |
| .crazy | *No documentation found.* | .crazy | emoticons |
| .cry | *No documentation found.* | .cry | emoticons |
| .happy | *No documentation found.* | .happy | emoticons |
| .hungry | *No documentation found.* | .hungry | emoticons |
| .lenny | *No documentation found.* | .lenny | emoticons |
| .love | *No documentation found.* | .love | emoticons |
| .shrug | *No documentation found.* | .shrug | emoticons |
| .sick | *No documentation found.* | .sick | emoticons |
| .success<br>.winner | *No documentation found.* | .winner | emoticons |
| .surprised | *No documentation found.* | .surprised | emoticons |
| .tableflip<br>.tflip | *No documentation found.* | .tflip | emoticons |
| .unflip | *No documentation found.* | .unflip | emoticons |
| .confused<br>.wat | *No documentation found.* | .wat | emoticons |
| .worried | *No documentation found.* | .worried | emoticons |
| .ety | Look up the etymology of a word | .ety word | etymology |
| .help<br>.commands | Shows a command's documentation, and possibly an example. | .help tell | help |
| .iplookup<br>.ip | IP Lookup tool | .ip 8.8.8.8 | ip |
| .console | Starts an interactive IPython console |  | ipython |
| .isup<br>.isupinsecure | isup.me website status checker |  | isup |
| .lmgtfy<br>.lmgify<br>.gify<br>.gtfy | Let me just... google that for you. | .lmgtfy | lmgtfy |
| .chairs | Set the meeting chairs.    See [meetbot module usage]({% link _usage/meetbot-module.md %}) | .chairs Tyrope Jason elad | meetbot |
| .endmeeting | End a meeting.    See [meetbot module usage]({% link _usage/meetbot-module.md %}) | .endmeeting | meetbot |
| .listactions | *No documentation found.* | .listactions | meetbot |
| .action | Log an action in the meeting log.    See [meetbot module usage]({% link _usage/meetbot-module.md %}) | .action elad will develop a meetbot | meetbot |
| .agreed | Log an agreement in the meeting log.    See [meetbot module usage]({% link _usage/meetbot-module.md %}) | .agreed Bowties are cool | meetbot |
| .info | Log an informational item in the meeting log.    See [meetbot module usage]({% link _usage/meetbot-module.md %}) | .info all board members present | meetbot |
| .link | Log a link in the meeing log.    See [meetbot module usage]({% link _usage/meetbot-module.md %}) | .link http://example.com | meetbot |
| .subject | Change the meeting subject.    See [meetbot module usage]({% link _usage/meetbot-module.md %}) | .subject roll call | meetbot |
| .comments | Show the comments that have been logged for this meeting with .comment.<br><br>See [meetbot module usage]({% link _usage/meetbot-module.md %}) |  | meetbot |
| .startmeeting | Start a meeting.    See [meetbot module usage]({% link _usage/meetbot-module.md %}) | .startmeeting title or .startmeeting | meetbot |
| .comment | Log a comment, to be shown with other comments when a chair uses .comments.<br>Intended to allow commentary from those outside the primary group of people<br>in the meeting.<br><br>Used in private message only, as `.comment <#channel> <comment to add>`<br><br>See [meetbot module usage]({% link _usage/meetbot-module.md %}) |  | meetbot |
| .pronouns | *No documentation found.* | .pronouns Embolalia | pronouns |
| .setpronouns | *No documentation found.* | .setpronouns they/them/their/theirs/themselves | pronouns |
| .rand | Replies with a random number between first and second argument. | .rand 10 99 | rand |
| .getsafeforwork<br>.getsfw | Gets the preferred channel's Safe for Work status, or the current<br>channel's status if no channel given. | .getsfw [channel] | reddit |
| .redditor | Show information about the given Redditor | .redditor poem_for_your_sprog | reddit |
| .setsafeforwork<br>.setsfw | Sets the Safe for Work status (true or false) for the current<br>channel. Defaults to false. | .setsfw false | reddit |
| .load | Wrapper for allowing delivery of .load command via PM |  | reload |
| .reload | Wrapper for allowing delivery of .reload command via PM |  | reload |
| .update | Wrapper for allowing delivery of .update command via PM |  | reload |
| .at | Gives you a reminder at the given time. Takes `hh:mm:ssTimezone message`.<br>Timezone is any timezone Sopel takes elsewhere; the best choices are those<br>from the tzdb; a list of valid options is available at<br><https://sopel.chat/tz>. The seconds and timezone are optional. | .at 13:47 Do your homework! | remind |
| .in | Gives you a reminder in the given amount of time. | .in 3h45m Go to class | remind |
| .safety | Set safety setting for channel |  | safety |
| .bing | Queries Bing for the specified input. | .bing sopel irc bot | search |
| .duck<br>.ddg<br>.g | Queries Duck Duck Go for the specified input. | .duck sopel irc bot | search |
| .search | Searches Bing and Duck Duck Go. | .search sopel irc bot | search |
| .suggest | Suggest terms starting with given input | .suggest lkashdfiauwgeaef | search |
| .seen | Reports when and where the user was last seen. |  | seen |
| .spellcheck<br>.spell | Says whether the given word is spelled correctly, and gives suggestions if<br>it's not. | .spellcheck stuff | spellcheck |
| .tell<br>.ask | Give someone a message the next time they're seen | Sopel, tell Embolalia he broke something again. | tell |
| .tld | Show information about the given Top Level Domain. | .tld ru | tld |
| .mangle<br>.mangle2 | Repeatedly translate the input until it makes absolutely no sense. |  | translate |
| .translate<br>.tr | Translates a phrase, with an optional language hint. | .tr mon chien | translate |
| .u | *No documentation found.* | .u 203D | unicode_info |
| .length<br>.distance | Convert distances | .length 3 parsec | units |
| .weight<br>.mass | Convert mass |  | units |
| .temp | Convert temperatures | .temp 100K | units |
| .uptime | .uptime - Returns the uptime of Sopel. |  | uptime |
| .title | Show the title or URL information for the given URL, or the last URL seen<br>in this channel. | .title http://google.com | url |
| .version | Display the latest commit version, if Sopel is running in a git repo. |  | version |
| .w<br>.wiki<br>.wik | *No documentation found.* | .w San Francisco | wikipedia |
| .wt<br>.define<br>.dict | Look up a word on Wiktionary. | .wt bailiwick | wiktionary |
| .xkcd | .xkcd - Finds an xkcd comic strip. Takes one of 3 inputs:<br>If no input is provided it will return a random comic<br>If numeric input is provided it will return that comic, or the nth-latest<br>comic if the number is non-positive<br>If non-numeric input is provided it will return the first google result for those keywords on the xkcd.com site |  | xkcd |
| .blocks | Manage Sopel's blocking features.    See [ignore system documentation]({% link _usage/ignoring-people.md %}). |  | coretasks |
| .useserviceauth | *No documentation found.* |  | coretasks |
