# google-translate-collector
Allows you to take a bunch of phrases in your native language and turn them into an mp3 recording in your target language. Meant for people who learn languages better from hearing.  

It also helps you revise for your language class hands-free, which is huge for your productivity and cognitive comfort. Not to mention your neck will thank you for this.

__v1__  ===============  DONE  
Given I have a source language phrase saved in a text file  
And I don't have a translation file with that phrase yet

When I run the program  
And the phrase is read  
And a translation API is contacted  

Then I receive a translation  
And the translation is saved to a text file

__v1.1__  ===============  
Given I have more than 1 source language phrase saved in a text file  
And I don't have a translation file with that phrase yet  

When I run the program  

Then the phrases are read in bulk  
And a translation API is contacted only once  


__v2__  ===============  
Given I have a target language phrase saved in a text file  
And I don't have an mp3 file with that phrase yet  

When I run the program  
And the phrase is read  
And a text-to-speech API is contacted  

Then I receive a stream of audio data  
And the audio data is saved to an mp3 file

__v3__  ===============  
Given I have a couple of mp3 files with target language phrases  
And I have a couple of mp3 files with the corresponding source language phrases  

When I run the program  
And I specify which phrase __pairs__ (!) are to be concatenated  
And I specify the length of pause between phrases in the pair  
And I specify the length of pause between pairs  

Then I receive a stream of audio data  
And the audio data is saved to an mp3 file  
And the source phrase always comes first in the pair  
