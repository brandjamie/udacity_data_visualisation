# Data Visualisation project for Udacity (Project 6)

## Summary
Students in the PISA 2012 survey answered a questionaire investigating, among
other things, their attitude towards school and were graded on their
abilities in maths, science and reading. An additional questionaire
was filled out by the senior administrator in each school. This visualisation examines the relationships between UK students attitude and their grade as well as allowing the viewer investigate the effects different schools can have on their students.

## Design

### Version 1 - index1.html
My first attempt used a scatterplot to show each students score (on a chosen subject), compared to their schools average score.

The colour of each point was assigned to their answer to the chosen attitude question (e.g. How much do you agree with the following statement? - School has been a waste of time.)

I was hoping to see banding of the colours, with the students who strongly agreed that school was a waste of time, getting lower marks than those who disagreed.

In practice it was difficult to see any patterns in the data due to some answers being much more prevailent than others. In addition, the sheer number of answers made the animation slow.

Note: The 'y' axis is incorrectly labeled on this version and should be labled after the student score as selected in the top left.

### Version 2 - index2.html

Similarly to the previous plot, this showed the average score for each answer to the attitudes questions, grouped by school. Schools were placed on the y axis according to the average score of the school. Schools could also be placed according to other variables from the school questionaire although this was not very effective. 

While this showed the relationships between scores and attitudes a little better, and alleviated the problems of processing times from the previous plot, it was still confusing. In particular, I felt having each school represented by four points (one for each answer) was very unclear. 


### Version 3 - index4.html (index3 was a dead end!)

In an effort to make the data clearer to the viewer, I opted for a collection of charts to be compared to one another. Each chart was a variation on the bar chart, with the width of each bar representing the percentage of students who gave each answer, and the height representing their average score.

A second chart showed the break down of schools, either according to the their average score (in 25% quantile blocks) or the schools' responses to questions about the availability of resources in the school.

Four smaller charts showed the data from the first chart broken into four groups by school, according to the catagorisation method chosen in the second chart.

### Version 4 - index5.html

Having multiple charts seemed to confuse people, particularly using the percentile groupings. This version took the same basic idea for a chart but instead had only one chart with the option to filter the number of schools included in the data according to the schools answer to certain question and/or the average score of the school.

The text was reduced and tooltips and other information (the number of students and schools in the chart) were added to help clarity. 

An option was given to add a second copy of the graph if the user wanted to make comparisons between different groups. 
A text resizing function was added to resize the chart's title according to it's length. 


### Version 5 - index6.html

A new colour pallete was suggested in the feedback. The suggestion was to use green and red for agree disagree. While this has positive and negative connotations, a number of the statements are worded negatively so that 'disagree' acctually shows a positive attitude towards school. I also wished to use a colorblind friendly pallete so I selected a diverging pallete from colorbrewer2.org

Bugs were fixed where text resizing not working on second chart and the y axis not being renamed on update.

The legend was adjusted to avoid overlaps when the 'strongly agree' group had very high scores. 

From the feedback it was found that the filter section was still unclear. Tooltips were added to explain each option. In addition, a low opacity was added to unselected filters to  make it easier to see what was having an effect on the current chart as well as clarify the effect of the toggles.

To further clarify things, the default filters were changed. Previously they showed all the schools by default, this meant that toggling the filters had no immediate effect which could have been confusing to viewers trying to understand what the filters did.

A final small change was added to make the second chart have the same parameters on creation as the first chart. This was just to make it easier for the viewer to compare specific things.


black outline for bars and legend?
copy added to show explicit relationship

code commented and refactored where neccesary




## Feedback:
Initial feedback was conducted with workmates with additional final feedback being requested from the Udacity forums. 

### Version 1:
#### Steven O. - Spoken, face to face. 

> I can't see what it's trying to show. I can't see any patterns in the colours. The scores get higher as they go to the right but I'm not sure what it's supposed to represent.

### Version 3: 

#### Adam J. - Through online chat. 

> small grammar - last paragraph 'devided' - divided
> i'd say the text is too small and difficult to read

> seems strange that the percentage of strongly agrees is nearly the same across all achievement categories - or am i reading it wrong?

> i think the areas to adjust parameters needs a bit of explanation - i was about to try it but realised i'm relyig on trial and error
> Just a sentence or two there would help to clarify
> Once you click it's obvious, but knowing beforehand is better
> or am i being nickpicky?

> the differences are miniscule it seems

> Visually it doesn't convey much, although of course the stats are what they are - maybe a line of dialogue could explain when they are clicked - differences between reading maths and science scores

> And wow, there are lots of permutations

> Which is great - though that strikes me as endlessly time consuming.

> Could that be narrowed down - or at least have some guidance on ones to focus on

> Overall the presentation seems goodbtw

> And what about having the numbers displayed inside the coloured areas - or as a seperate list next to the graphs as they change
> That would make the figures clearer - but then again it could be a lot of work
> Actually inside the colours won't work because some are so small, so as a list maybe
> Just an idea - maybe it's not necessary

me - I was thinking I may add mouseover's with the numbers (so you hover over a 'bar' and it shows you the actual figures).

> yes, that sounds good - and tell them that

> Slightly space out the adjustment boxes too - so the text describing it is more clearly associated

> definitely increase text size




Ray P. ***********************************************
Via Email

    What do you notice in the visualization?

The 'across the board' commonality and consistency of the percentile breakdown.

    What questions do you have about the data?

None, it's clear and easy to interpret, though each should, initially presented with its own comments, and then the percentile charts collected to demonstrate the commonality.

    What relationships do you notice?

Fig 1, to 3, 4, 5, and 6. Fig 2, in my opinion did not need to be expressed as a chart (but that's just me :)

    What do you think is the main takeaway from this visualization?

Clarity.

    Is there something you don’t understand in the graphic?

No.


Steven O. ****************************************************
Via Email. 

First off I notice of course that the poorer you do in school the more you agree with it being a waste of time and I can 
understand them feeling that way.
2nd I cant think of one but maybe later after some thought.
3rd- I think i answered that above.
4th- main takeaway is again students who dont do well in school just dont see the value in it.
5th- I dont understand how they differ. I mean on the side and the horizontal it seems like the same title
but you have different numbers and different size graphs. Need to speak in person.


Robert S. *****************************************************
Via Email.

I don't understand the percentiles.



Malcolm V. ****************************************************
Spoken, face to face.

It's very clean. The first two graphs were quite clear but I wasn't sure what the others were supposed to represent. There's certainly a lot of options but I was confused as to what was changing. If I changed one of the parameters, all the graphs changed and I wasn't quite sure what was happening.


Version 5:


Ray P. ***********************************************
Via Email


    What do you notice in the visualization? It's very clear and easy to determine the responses.
    What questions do you have about the data? That the positive responses are prevalent.
    What relationships do you notice? None.
    What do you think is the main takeaway from this visualization? Its ease of interpretation.
    Is there something you don’t understand in the graphic? Box two. When I clicked the filters in/out, there was no change.



wilfried_29181078645 *********************************
Via Udacity Forums


Thanks for sharing this visualization. You found an interesting way to explore the PISA study and its various aspects.

There are a few thinks I would like to mention:

It took me some time to understand the bar representation. It is a mixture of bar (vertical) and stacked bar (horizontal). I would suggest changing it to something else but I don't have a clever idea what to chose instead.

I think, the colors of the bars don't serve their meaning very well. I would have understood green for agree and red for disagree. I would recommend a different color palette.

It also took me some time to understand the filters on the right. This is especially true for the school filter. The lower part of filter is based on the response of a senior administrator, correct?

I found some visualization problems:
- y axis is not changing with scoring selection
- the right bars could overlap the legend if only schools with high scores are selected

Great start. I'm looking forward to seeing your next version of this.






# Resources


http://bl.ocks.org/weiglemc/6185069

http://bost.ocks.org/mike/bar/

http://egorkhmelev.github.io/jslider/

http://designbump.com/css3-toggle-switches-tutorial/

http://zeroviscosity.com/d3-js-step-by-step/step-5-adding-tooltips

http://stackoverflow.com/questions/14569415/read-width-of-d3-text-element

http://api.jquery.com/slideup/

http://api.jquery.com/slidedown/

http://api.jquery.com/mouseover/

http://colorbrewer2.org