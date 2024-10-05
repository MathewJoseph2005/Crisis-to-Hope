define l = Character("Lucas Alvarez", color="#ffcc00")
define a = Character("Amara Singh", color="#ff6666")
define e = Character("Dr. Elena Greene", color="#66ccff")
define y = Character("Yusuf Patel", color="#66ff66")

# Backgrounds
image bg_summit = "images/bg_summit.png"
image bg_water = "images/bg_water.png"
image bg_ecosystem = "images/bg_ecosystem.png"
image bg_emergency = "images/bg_emergency.png"

# Music
define bgm_dramatic = "audio/bgm_dramatic.ogg"
define bgm_tense = "audio/bgm_tense.ogg"
define bgm_hopeful = "audio/bgm_hopeful.ogg"

# Additional Images and Sound Effects can be added similarly.
label start:
    scene bg_summit
    play music bgm_tense
    
    l "Welcome, everyone. As we gather here today, the reports are clear: the situation is dire. Climate change is accelerating, and we must act swiftly."
    l "However, we need to consider our options carefully. We push too hard, and economies could collapse. We don’t push hard enough, and our future goes up in smoke. The question is: where’s the balance?"
    
    a "Balance? We’re long past the point of balance, Lucas. Climate justice isn’t about protecting the interests of big polluters. People are dying—droughts, floods, famine! We don’t have time for compromise."
    
    e "The data doesn’t lie. Every year we delay, emissions rise, and the 2°C target becomes harder to achieve. We need to implement serious reductions now, or we’re looking at 3°C or more by the end of the century."
    
    y "But technology can solve this, right? We don’t have to pull the emergency brake and crash the economy. We could invest in clean tech, use carbon capture, transition gradually. Isn’t that more realistic?"
    
    # Player choices appear here.
    menu:
        "Commit to Aggressive Emissions Targets":
            $ choice = "aggressive"
            l "That’s a bold move! It will show our commitment, but we need to prepare for backlash from some member countries."
            e "This could inspire others to follow suit. If we stand united, we can create a global movement."
            a "It’s time to be bold. People need to see real change!"
            
            # Continue the narrative for this choice...
            jump outcome_aggressive

        "Implement Carbon Trading":
            $ choice = "carbon_trading"
            l "A more flexible approach could encourage countries to participate, but we need to ensure it doesn’t become a loophole for big polluters."
            e "We must set strict guidelines to prevent exploitation of this system. If we do it right, it can be a valuable tool."
            
            # Continue for carbon trading choice...
            jump outcome_carbon_trading

        "Compromise on Economic Growth":
            $ choice = "compromise"
            l "This could help us avoid immediate backlash, but it might not be enough to meet our long-term goals."
            e "This will send the wrong message. Compromising now may cost us dearly in the future."
            
            # Continue for compromise...
            jump outcome_compromise

label outcome_aggressive:
    e "The agreement sets strict targets, and nations unite to work on reducing emissions. Initial backlash from industry groups occurs, but public support grows as the data is shared."
    a "The world starts to stabilize, leading to further collaborative efforts."
    
    # Continue the story to the next section...
    jump hydrosphere_protocols

label outcome_carbon_trading:
    e "The carbon trading system provides some emissions reductions, but industries exploit loopholes."
    a "Future missions will involve dealing with the consequences of insufficient action."
    
    # Continue the story...
    jump hydrosphere_protocols

label outcome_compromise:
    e "Emissions continue to rise, and the player faces a future mission with communities suffering from increased climate impacts."
    a "This leads to social unrest and demands for immediate action."
    
    # Continue the story...
    jump hydrosphere_protocols

label hydrosphere_protocols:
    scene bg_water
    y "We’ve developed several innovative techniques to conserve water and improve water quality."
    y "But the real challenge isn’t the technology; it’s getting industries and governments to adopt these solutions."
    
    a "And why aren’t they adopting them? Is it because it costs too much? Or because they don’t want to change their profit-driven models? We need to hold these corporations accountable."
    
    # More dialogue, followed by player choices.
    
    menu:
        "Launch a Global Water Conservation Fund":
            # Good outcome...
            jump outcome_water_good

        "Focus on Awareness Campaigns":
            # Moderate outcome...
            jump outcome_water_moderate

        "Delay Action for Economic Stability":
            # Bad outcome...
            jump outcome_water_bad

label outcome_water_good:
    e "The Global Water Conservation Fund successfully drives innovation and adoption of sustainable practices. Water security improves in vulnerable regions."
    a "This approach gains international support, leading to long-term positive effects."
    
    # Continue the story...
    jump final_stand

label outcome_water_moderate:
    e "Awareness campaigns raise public consciousness, but without significant policy changes, water security remains a challenge."
    a "While it's a step in the right direction, the delay in aggressive action may come with future costs."
    
    # Continue the story...
    jump final_stand

label outcome_water_bad:
    e "By delaying action for economic stability, we avoided immediate disruptions. However, as water scarcity worsens, the impacts become increasingly severe."
    a "Communities are suffering, and the delayed response has cost us precious time. It's a grim outlook moving forward."
    
    # Continue the story or proceed to the next section.
    jump final_stand

label final_stand:
    scene bg_emergency
    l "We’ve hit the tipping point. Heatwaves are becoming deadly, food supplies are dwindling, and entire nations are at risk of disappearing under rising seas."
    l "We have one last chance to get this right."
    
    e "Our models show we can still stabilize the climate if we reach net-zero by 2050, but every year we delay, the window narrows. We need immediate, unprecedented action."

    a "The people are ready to act. We’ve seen the protests, the grassroots movements. They’re demanding change now. But are we ready to give them what they need?"

    menu:
        "Implement an Emergency Global Climate Fund (Good Choice)":
            $ final_choice = "fund"
            l "We’ll establish an emergency global climate fund to address both mitigation and adaptation on an unprecedented scale. Every nation must contribute, and every vulnerable region must benefit."
            l "This could work, but we’ll need every major economy on board. If even one country pulls out, the whole plan could fall apart."
            e "It’s risky, but it’s the best option we have. We can’t afford to go slow anymore."
            jump ending_new_dawn

        "Call for Immediate National Emergency Actions (Moderate Choice)":
            $ final_choice = "emergency_actions"
            l "Let’s call for immediate national emergency actions to address current crises, but without a formal funding structure yet."
            e "Immediate actions are necessary, but without funding, the impact will be limited. How do we ensure sustainability?"
            jump ending_age_of_struggle

        "Delay Action for Political Stability (Bad Choice)":
            $ final_choice = "delay"
            l "Let’s postpone radical changes for a few years to maintain political stability. We’ll focus on gradual adaptation."
            e "This may keep some governments in power, but at what cost? We might miss the crucial opportunity to act."
            jump ending_collapse

label ending_new_dawn:
    e "The emergency fund is established, allowing for immediate large-scale climate action. Countries begin deploying green technology and adaptation measures on a massive scale."
    a "This is the best possible outcome. The world begins to recover."
    
    scene bg_summit
    show flourish_citydefine l = Character("Lucas Alvarez", color="#ffcc00")
define a = Character("Amara Singh", color="#ff6666")
define e = Character("Dr. Elena Greene", color="#66ccff")
define y = Character("Yusuf Patel", color="#66ff66")

# Backgrounds
image bg_summit = "images/bg_summit.png"
image bg_water = "images/bg_water.png"
image bg_ecosystem = "images/bg_ecosystem.png"
image bg_emergency = "images/bg_emergency.png"

# Music
define bgm_dramatic = "audio/bgm_dramatic.ogg"
define bgm_tense = "audio/bgm_tense.ogg"
define bgm_hopeful = "audio/bgm_hopeful.ogg"

# Additional Images and Sound Effects can be added similarly.
label start:
    scene bg_summit
    play music bgm_tense
    
    l "Welcome, everyone. As we gather here today, the reports are clear: the situation is dire. Climate change is accelerating, and we must act swiftly."
    l "However, we need to consider our options carefully. We push too hard, and economies could collapse. We don’t push hard enough, and our future goes up in smoke. The question is: where’s the balance?"
    
    a "Balance? We’re long past the point of balance, Lucas. Climate justice isn’t about protecting the interests of big polluters. People are dying—droughts, floods, famine! We don’t have time for compromise."
    
    e "The data doesn’t lie. Every year we delay, emissions rise, and the 2°C target becomes harder to achieve. We need to implement serious reductions now, or we’re looking at 3°C or more by the end of the century."
    
    y "But technology can solve this, right? We don’t have to pull the emergency brake and crash the economy. We could invest in clean tech, use carbon capture, transition gradually. Isn’t that more realistic?"
    
    # Player choices appear here.
    menu:
        "Commit to Aggressive Emissions Targets":
            $ choice = "aggressive"
            l "That’s a bold move! It will show our commitment, but we need to prepare for backlash from some member countries."
            e "This could inspire others to follow suit. If we stand united, we can create a global movement."
            a "It’s time to be bold. People need to see real change!"
            
            # Continue the narrative for this choice...
            jump outcome_aggressive

        "Implement Carbon Trading":
            $ choice = "carbon_trading"
            l "A more flexible approach could encourage countries to participate, but we need to ensure it doesn’t become a loophole for big polluters."
            e "We must set strict guidelines to prevent exploitation of this system. If we do it right, it can be a valuable tool."
            
            # Continue for carbon trading choice...
            jump outcome_carbon_trading

        "Compromise on Economic Growth":
            $ choice = "compromise"
            l "This could help us avoid immediate backlash, but it might not be enough to meet our long-term goals."
            e "This will send the wrong message. Compromising now may cost us dearly in the future."
            
            # Continue for compromise...
            jump outcome_compromise

label outcome_aggressive:
    e "The agreement sets strict targets, and nations unite to work on reducing emissions. Initial backlash from industry groups occurs, but public support grows as the data is shared."
    a "The world starts to stabilize, leading to further collaborative efforts."
    
    # Continue the story to the next section...
    jump hydrosphere_protocols

label outcome_carbon_trading:
    e "The carbon trading system provides some emissions reductions, but industries exploit loopholes."
    a "Future missions will involve dealing with the consequences of insufficient action."
    
    # Continue the story...
    jump hydrosphere_protocols

label outcome_compromise:
    e "Emissions continue to rise, and the player faces a future mission with communities suffering from increased climate impacts."
    a "This leads to social unrest and demands for immediate action."
    
    # Continue the story...
    jump hydrosphere_protocols

label hydrosphere_protocols:
    scene bg_water
    y "We’ve developed several innovative techniques to conserve water and improve water quality."
    y "But the real challenge isn’t the technology; it’s getting industries and governments to adopt these solutions."
    
    a "And why aren’t they adopting them? Is it because it costs too much? Or because they don’t want to change their profit-driven models? We need to hold these corporations accountable."
    
    # More dialogue, followed by player choices.
    
    menu:
        "Launch a Global Water Conservation Fund":
            # Good outcome...
            jump outcome_water_good

        "Focus on Awareness Campaigns":
            # Moderate outcome...
            jump outcome_water_moderate

        "Delay Action for Economic Stability":
            # Bad outcome...
            jump outcome_water_bad

label outcome_water_good:
    e "The Global Water Conservation Fund successfully drives innovation and adoption of sustainable practices. Water security improves in vulnerable regions."
    a "This approach gains international support, leading to long-term positive effects."
    
    # Continue the story...
    jump final_stand

label outcome_water_moderate:
    e "Awareness campaigns raise public consciousness, but without significant policy changes, water security remains a challenge."
    a "While it's a step in the right direction, the delay in aggressive action may come with future costs."
    
    # Continue the story...
    jump final_stand

label outcome_water_bad:
    e "By delaying action for economic stability, we avoided immediate disruptions. However, as water scarcity worsens, the impacts become increasingly severe."
    a "Communities are suffering, and the delayed response has cost us precious time. It's a grim outlook moving forward."
    
    # Continue the story or proceed to the next section.
    jump final_stand

label final_stand:
    scene bg_emergency
    l "We’ve hit the tipping point. Heatwaves are becoming deadly, food supplies are dwindling, and entire nations are at risk of disappearing under rising seas."
    l "We have one last chance to get this right."
    
    e "Our models show we can still stabilize the climate if we reach net-zero by 2050, but every year we delay, the window narrows. We need immediate, unprecedented action."
    
    # Player makes the final choice...

    "The world rapidly transitions to renewable energy, with adaptation efforts saving millions of lives. Global warming stabilizes, and ecosystems begin to recover. The final scenes show flourishing cities powered by clean energy and communities thriving in harmony with the planet."
    
    return

label ending_age_of_struggle:
    e "Emergency actions save lives in the short term, but the lack of funding leads to sustainability issues."
    a "It’s a step in the right direction, but we’ll have to keep pushing in future missions."
    
    scene bg_ecosystem
    show recover_world
    "The world avoids total collapse, but progress is slow. Some nations adapt, while others struggle under climate pressures. Emissions are reduced, but the damage from previous delays means more frequent climate crises. The ending shows a world in recovery, but with ongoing challenges and inequalities."
    
    return

label collapse_ending:
    # Scene background
    scene bg_emergency

    # Stop any previous music or sound
    stop music fadeout 1.0

    # Play the collapse video in full-screen mode
    play movie "world_collapse.mp4"

    # Wait for the movie to finish
    # queue movie
    show black

    # Continue the narration after the video
    "The final scene shows a world in chaos, with a few survivors struggling to adapt to a harsh, damaged environment."
    "Rising seas swallow cities, heatwaves scorch the land, and food shortages lead to unrest."
    
    stop movie

    # Transition to the next part or end
    return
