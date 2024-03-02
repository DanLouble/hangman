import random

Graphics = [r'''
___    ___   _____     _     _        ____        _    ______    _____
| |    | |  / ____ \  | |   | |      | ___ \     | |  |  ____|  |  __ \   
 \ \  / /  | |    | | | |   | |      | |  \ \    | |  | |       | |  \ \ 
  \ \/ /   | |    | | | |   | |      | |   \ \   | |  | |___    | |   \ \   
   |  |    | |    | | | |   | |      | |    | |  | |  |  ___|   | |    | |  
   |  |    | |____| | | |___| |      | |____| |  | |  | |____   | |____| |  
   |__|     \______/   \_____/       |________|  |_|  |______|  |________|  ''',r'''
------------
|         |
|           
|         
|          
|          
|         O ''',r'''
------------
|         |
|          O 
|         
|          
|          
|           ''',r'''
------------
|         |
|          O 
|         / 
|          
|          
|          ''',r'''
------------
|         |
|          O 
|         / |
|          
|          
|          ''',r'''
------------
|         |
|          O 
|         / |
|          |
|          
|          ''',r'''
------------
|         |
|          O 
|         / |
|          |
|         / 
|          ''',r'''
------------
|         |
|          O 
|         / |
|          |
|         / | 
|               ''']

#list of words 
wordlist = ['Ability', 'Backing', 'Cabinet', 'Absence', 'Balance', 'Calibre', 'Academy', 'Banking', 'Calling', 'Account', 'Barrier', 'Capable', 'Accused', 'Battery', 'Capital', 'Achieve', 'Bearing', 'Captain', 'Acquire', 'Beating', 'Caption', 'Address', 'Because', 'Capture', 'Advance', 'Bedroom', 'Careful', 'Adverse', 'Believe', 'Carrier', 'Advised', 'Beneath', 'Caution', 'Adviser', 'Benefit', 'Ceiling', 'Against', 'Besides', 'Central', 'Airline', 'Between', 'Centric', 'Airport', 'Billion', 'Century', 'Alcohol', 'Binding', 'Certain', 'Alleged', 'Brother', 'Chamber', 'Already', 'Brought', 'Channel', 'Analyst', 'Burning', 'Chapter', 'Ancient', 'Dealing', 'Charity', 'Another', 'Decided', 'Charlie', 'Anxiety', 'Decline', 'Charter', 'Anxious', 'Default', 'Checked', 'Anybody', 'Defence', 'Chicken', 'Applied', 'Deficit', 'Chronic', 'Arrange', 'Deliver', 'Circuit', 'Arrival', 'Density', 'Classes', 'Article', 'Deposit', 'Classic', 'Assault', 'Desktop', 'Climate', 'Assumed', 'Despite', 'Closing', 'Assured', 'Destroy', 'Closure', 'Attempt', 'Develop', 'Clothes', 'Attract', 'Devoted', 'Collect', 'Auction', 'Diamond', 'College', 'Average', 'Digital', 'Combine', 'Eastern', 'Discuss', 'Comfort', 'Economy', 'Disease', 'Command', 'Edition', 'Display', 'Comment', 'Elderly', 'Dispute', 'Compact', 'Element', 'Distant', 'Company', 'Engaged', 'Diverse', 'Compare', 'Enhance', 'Divided', 'Compete', 'Essence', 'Drawing', 'Complex', 'Evening', 'Driving', 'Concept', 'Evident', 'Dynamic', 'Concern', 'Exactly', 'Factory', 'Concert', 'Examine', 'Faculty', 'Conduct', 'Example', 'Failing', 'Confirm', 'Excited', 'Failure', 'Connect', 'Exclude', 'Fashion', 'Consent', 'Exhibit', 'Feature', 'Consist', 'Expense', 'Federal', 'Contact', 'Explain', 'Feeling', 'Contain', 'Explore', 'Fiction', 'Content', 'Express', 'Fifteen', 'Contest', 'Extreme', 'Filling', 'Context', 'Gallery', 'Finance', 'Control', 'Gateway', 'Finding', 'Convert', 'General', 'Fishing', 'Correct', 'Genetic', 'Fitness', 'Council', 'Genuine', 'Foreign', 'Counsel', 'Gigabit', 'Forever', 'Counter', 'Greater', 'Formula', 'Country', 'Hanging', 'Fortune', 'Crucial', 'Heading', 'Forward', 'Crystal', 'Healthy', 'Founder', 'Culture', 'Hearing', 'Freedom', 'Current', 'Heavily', 'Further', 'Cutting', 'Helpful', 'Illegal', 'Jointly', 'Helping', 'Illness', 'Journal', 'Herself', 'Imagine', 'Journey', 'Highway', 'Imaging', 'Justice', 'Himself', 'Improve', 'Justify', 'History', 'Include', 'Keeping', 'Holding', 'Initial', 'Killing', 'Holiday', 'Inquiry', 'Kingdom', 'Housing', 'Insight', 'Kitchen', 'However', 'Install', 'Knowing', 'Hundred', 'Instant', 'Machine', 'Husband', 'Instead', 'Manager', 'Landing', 'Intense', 'Married', 'Largely', 'Interim', 'Massive', 'Lasting', 'Involve', 'Maximum', 'Leading', 'Natural', 'Meaning', 'Learned', 'Neither', 'Measure', 'Leisure', 'Nervous', 'Medical', 'Liberal', 'Network', 'Meeting', 'Liberty', 'Neutral', 'Mention', 'Library', 'Notable', 'Message', 'License', 'Nothing', 'Million', 'Limited', 'Nowhere', 'Mineral', 'Listing', 'Nuclear', 'Minimal', 'Logical', 'Nursing', 'Minimum', 'Loyalty', 'Pacific', 'Missing', 'Obvious', 'Package', 'Mission', 'Offence', 'Painted', 'Mistake', 'Officer', 'Parking', 'Mixture', 'Ongoing', 'Partial', 'Monitor', 'Opening', 'Partner', 'Monthly', 'Operate', 'Passage', 'Morning', 'Opinion', 'Passing', 'Musical', 'Optical', 'Passion', 'Mystery', 'Organic', 'Passive', 'Portion', 'Outcome', 'Patient', 'Poverty', 'Outdoor', 'Pattern', 'Precise', 'Outlook', 'Payable', 'Predict', 'Outside', 'Payment', 'Premier', 'Overall', 'Penalty', 'Premium', 'Proudly', 'Pending', 'Prepare', 'Project', 'Pension', 'Present', 'Promise', 'Pealing', 'Prevent', 'Promote', 'Perfect', 'Primary', 'Protect', 'Perform', 'Printer', 'Protein', 'Perhaps', 'Privacy', 'Protest', 'Phoenix', 'Private', 'Provide', 'Picking', 'Problem', 'Publish', 'Picture', 'Proceed', 'Purpose', 'Pioneer', 'Process', 'Pushing', 'Plastic', 'Produce', 'Qualify', 'Pointed', 'Product', 'Quality', 'Popular', 'Profile', 'Quarter', 'Section', 'Success', 'Radical', 'Segment', 'Suggest', 'Railway', 'Serious', 'Summary', 'Readily', 'Service', 'Support', 'Reading', 'Serving', 'Suppose', 'Reality', 'Session', 'Supreme', 'Realise', 'Setting', 'Surface', 'Receipt', 'Seventh', 'Surgery', 'Receive', 'Several', 'Surplus', 'Recover', 'Shortly', 'Survive', 'Reflect', 'Showing', 'Suspect', 'Regular', 'Silence', 'Sustain', 'Related', 'Silicon', 'Teacher', 'Release', 'Similar', 'Telecom', 'Remains', 'Sitting', 'Telling', 'Removal', 'Sixteen', 'Tension', 'Removed', 'Skilled', 'Theatre', 'Replace', 'Smoking', 'Therapy', 'Request', 'Society', 'Thereby', 'Require', 'Somehow', 'Thought', 'Reserve', 'Someone', 'Through', 'Resolve', 'Speaker', 'Tonight', 'Respect', 'Special', 'Totally', 'Respond', 'Species', 'Touched', 'Restore', 'Sponsor', 'Towards', 'Retired', 'Station', 'Traffic', 'Revenue', 'Storage', 'Trouble', 'Reverse', 'Strange', 'Turning', 'Rollout', 'Stretch', 'Typical', 'Routine', 'Student', 'Uniform', 'Running', 'Studied', 'Unknown', 'Satisfy', 'Subject', 'Unusual', 'Science', 'Succeed', 'Upgrade', 'Walking', 'Whether', 'Upscale', 'Wanting', 'Willing', 'Utility', 'Warning', 'Winning', 'Variety', 'Warrant', 'Without', 'Various', 'Wearing', 'Witness', 'Vehicle', 'Weather', 'Working', 'Venture', 'Webcast', 'Writing', 'Version', 'Website', 'Written', 'Veteran', 'Wedding', 'Western', 'Victory', 'Weekend', 'Whereas', 'Viewing', 'Welcome', 'Whereby', 'Village', 'Welfare', 'Virtual', 'Violent', 'Visible', 'Waiting']

enteredletterlist = []

word = (random.choice(wordlist)).lower()

guesslen = len(word)

totallives = len(word)

print("you have",totallives,"lives or you die")

hiddenword = ["_"]*len(word)

while guesslen > 0 and totallives > 0:

    guess = (input("guess a letter of the word ")).lower()


    while guess in enteredletterlist or guess.isalpha() == False or len(guess) > 1:
        if guess in enteredletterlist:
            print("you've already entered that letter")
            guess = input("guess another letter ")
        elif guess.isalpha() == False:
            guess = input("error, give me a letter this time ")
        elif len(guess) > 1:
            guess = input("only one letter ")
    
    count = word.count(guess)

    for eachletter in word:
        if guess == eachletter:
            i = word.index(eachletter)
            hiddenword[i] = guess
        else:
            for position, letter in enumerate(word):
                if letter == guess:
                    hiddenword[position] = guess

    enteredletterlist.append(guess)
    
    if count > 0 and guesslen > 0:
        guesslen -= count 
        print("correct!",totallives,"lives left")    
    else:
        totallives -= 1
        print("wrong, you have",totallives,"lives left")    
    
    print(Graphics[totallives])
    print(*hiddenword) 
    

    
  
if guesslen == 0:
    print("congratulations, hangman survives! The word is",word)       
if totallives == 0:
    print(" ")
    print("you died. The word was",word)
    print(" ")