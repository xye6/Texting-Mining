import json


form_string = """
{
    "A. Language and Communication": [
         {"A1":{
            "subtitle" : "Overall Level of Non-Echoed Spoken Language",
            "description": "The rating for this item should reflect the majority of the participant's utterances, not merely the best ones. For the purposes of the ADOS-2, a complex sentence is defined as an utterance with two or more clauses. Examples include \\"I didn't go to the zoo because it, rained\\" or \\"l think wasps are really scary.\\" In contrast, \\"I have two sisters and one brother\\" would not be considered a complex sentence.",
            "value": {"0": "Uses sentences in a largely correct fashion (must use some complex,speech).",
                      "1": "Some relatively complex speech (occasional utterances with two or more clauses), but with recurrent grammatical errors not associated with use of dialect.",
                      "2": "Non-echoed speech is mostly utterances of at least three words, but without complex language as described above.",
                      "3": "Non-echoed language is mostly simple phrases."}
            }
         },
         {"A2":{
            "subtitle" : "Speech Abnormalities Associated With Autism(Intonation/Volume/Rhythm/Rate)",
            "description": "The focus of this item is on speech abnormalities that are characteristic of autism. Because of the variability within the autism spectrum, speech patterns in intonation, volume, rhythm, or rate (not articulation) that are unusual, but not obviously characteristic of autism, should receive a rating of 1. Code this item relative to the participant's expressive language level.", 
            "value": {"0": "Appropriately varying intonation, reasonable volume, and normal rate of speech, with regular rhythm coordinated with breathing.",
                      "1": "Little variation in pitch and tone; rather flat or exaggerated intonation, but not obviously peculiar, OR slightly unusual volume, AND/OR speech that tends to be somewhat unusually slow, fast, or jerky.",
                      "2": "Speech that is clearly abnormal for ANY of the following reasons: slow and halting; inappropriately rapid; jerky and irregular in rhythm (other than ordinary stutter/stammer), such that there is some interference with intelligibility; odd intonation or inappropriate pitch and stress; markedly flat and toneless (\\"mechanical\\"); consistently abnormal volume.",
                      "7": "Stutter or stammer or other fluency disorder (if odd intonation is also present, code 1 or 2 accordingly)."}
            }
         },
         {"A3":{
            "subtitle" : "Immediate Echolalia",
            "description": "This item pertains to the participant's immediate repetition of the last statement or series of statements made by the examiner or another person. When coding, do not include repetitions that are a lead-in to a response to the examiner or that are used as a memory device in specific tasks.",
            "value": {"0": "Does not repeat others' speech.",
                      "1": "Occasional echoing.",
                      "2": "Echoing words and phrases regularly. but some spontaneous language, which can be stereotyped",
                      "3": "Speech largely consists of immediate echolalia."}
            }
         },
         {"A4":{
            "subtitle" : "Stereotyped/Idiosyncratic Use of Words or Phrases",
            "description": "Coding for this item includes delayed echolalia or other highly repetitive utterances with consistent intonation patterns. These words or phrases can be intended meaningfully and can be appropriate to conversation at some level. The focus of the item is on the stereotyped or idiosyncratic quality of the phrasing, unusual use of words or formation of utterances, and/or their arbitrary association with a particular meaning. Neologisms and referring to oneself by name should be coded here, as well as clear evidence of a pronoun error across person (e.g. you or he or she to mean 1). Code relative to the participant's expressive language level.", 
            "value": {"0": "Rarely or never uses stereotyped or idiosyncratic words or phrases.",
                      "1": "Use of words or phrases tends to be more repetitive or formal than that of most individuals at the same level of expressive language, but not obviously odd, OR occasional stereotyped utterances or odd use of words or phrases, with substantial spontaneous, flexible language as well.",
                      "2": "Often uses stereotyped utterances or odd words or phrases, with some other language.",
                      "3": "Frequently uses odd or stereotyped speech, and rarely uses non-stereotyped spontaneous speech."}
            }
         },
         {"A5":{
            "subtitle" : "Offers Information",
            "description": "The focus of this item is on the participants spontaneous, appropriate offering of personal information, new to the examiner. It does not have to occur in context or be part of a sustained interaction. Ít can occur as the elaboration of responses to questions, but must include new information, not specified by the question. It can be related to the participants interests, but should not be related solely to preoccupations. Comments about facts (e.g., \\"Did you know that whales are mammals?\\") are not coded here, but can be considered in assigning a rating under \\"Conversation\\" later in this section. Comments about relationships or possessions (e.g.,\\"I have two brothers\\" or \\"Our family has a boat\\") can be coded here if they refer to an activity rather than a list of characteristics or objects. Lists of multiple characteristics (e.g., \\"I like to hike, sail, and fish\\")should be counted as one instance of offering information unless they are part of compulsive listing behavior, which does not receive credit here.", 
            "value": {"0": "Spontaneously offers information about his or her own thoughts, feelings, or experiences on several occasions.",
                      "1": "Occasionally offers information spontaneously about his or her own thoughts, feelings, or experiences.",
                      "2": "Rarely or never offers information spontaneously, except about circumscribed interests or preoccupations, OR offers information about facts or general knowledge including preoccupations or circumscribed interests."}
            }
         },
         {"A6":{
            "subtitle" : "Asks for Information",
            "description": "The focus of this item is on the participant's spontaneous expression of interest in the examiners ideas, experiences, or reactions. This should not be part of a preoccupation. When assigning a rating, exclude asking for information that is not related to the examiner, or about the ADOS-2 materials, or about particular facts not specific to the examiner; instead, include these when assigning a rating under \\"Conversation.\\" For this item, questions do not necessarily have to lead to a sustained conversation. Questions about relationships or possessions may be coded here if they refer to the examiner's experiences rather than filling in a list.", 
            "value": {"0": "Asks the examiner about his or her thoughts, feelings, or experiences on several occasions.",
                      "1": "Occasionally (at least one clear example) asks the examiner about his or her thoughts, feelings, or experiences.",
                      "2": "Responds appropriately to examiner's comments about his or her thoughts, feelings, or experiences, but does not spontaneously inquire about them.",
                      "3": "Rarely or never expresses interest in the examiner's thoughts, feelings, or experiences."}
            }
         },
         {"A7":{
            "subtitle" : "Reporting of Events",
            "description": "The focus of this item is on the participant's ability to select an event spontaneously or in response to the examiner's general questioning and to describe it in a comprehensible fashion without requiring specific probes. This should involve a sequential description of an event outside the immediate environment. Code the \\"best\\" example, given the rating constraints described below with regard to preoccupations and probes.",
            "value": {"0": "Reports a specific nonroutine event (e.g., a holiday, a vacation, a shopping trip) that is not part of any preoccupations or intense interests and seems likely to be real. Gives a reasonable account without specific probes, but may need to be asked a general question to get started.",
                      "1": "Gives a reasonable account of a routine event (e.g., playing a favorite game. usual routine when he or she arrives home from school) that is not part of a preoccupation or intense interest and seems likely to be real. Gives the account without specific probes. but initially may need to be asked to describe the event. Include accounts from the \\"Demonstration Task\\" here.",
                      "2": "Provides an account of routine or nonroutine events, but dependent on specific probes. OR only describes an event that seems unlikely to have been real.",
                      "3": "Inconsistent or insufficient responses. even to specific probes."}
            }
         },
         {"A8":{
            "subtitle" : "Conversation",
            "description": "This is a summary item that focuses on the to-and-fro use of words and phrases in social conversation. Code this item relative to the participant's expressive language level. Code evidence of (or lack of) nonverbal reciprocity under \\"Amount of Reciprocal Social Communication\\" in section B of this protocol. This rating should consider all opportunities for conversation, not merely the best.", 
            "value": {"0": "Conversation flows, building on the examiner's dialogue. This rating requires that much of the participant's speech provide both a response to the examiner's speech and some additional talking (not necessarily a question) that builds on what has just been said and allows a response from the examiner(i.e., sequences of at least four elements:examiner opens, participant comments, examiner responds, participant responds to response).",
                      "1": "Speech includes some spontaneous elaboration of the participant's own responses for the examiner's benefit OR provides leads for the examiner to follow, but either this is less in amount than would be expected for the participant's expressive language level or it is limited in flexibility.",
                      "2": "Little reciprocal conversation sustained by the participant; may follow his or her own train of thought rather than participate in an interchange; may have some spontaneous offering of information or comments, but little sense of reciprocity.",
                      "3": "Little spontaneous communicative speech (although there may be much echoed or noncommunicative speech). This rating can be used to describe participants who make some limited, but very few, responses to conversational initiations by the examiner."}
            }
         },
         {"A9":{
            "subtitle" : "Descriptive, Conventional, Instrumental, or Informational Gestures",
            "description": "The focus of this item is on descriptive gestures that enact or represent an object or event(such as acting out rinsing a toothbrush or showing how a roller coaster curves through the air). Gestures that are conventional(e.g., clapping for \\"well done\\"), informational, or instrumental (e.g., pointing, shrugging, head nodding, or head shaking) receive partial credit. When coding, exclude emphatic gestures (e.g., \\"beats\\" accompanying speech); include behaviors that occur during the \\"Demonstration Task\\" and throughout the ADOS-2 evaluation. The emphasis is on how the participant uses gestures before he or she is prompted or asked todo so, or gestures that the participant adds as he or she responds to a requested description (e.g., pretending to spit after demonstrating how to use a toothbrush, as requested). Pointing is included here as an instrumental gesture, as it is not coded separately in Module 3. Grabbing and reaching are not coded here.", 
            "value": {"0": "Spontaneous use of several descriptive gestures. These gestures may be typical or idiosyncratic but must be communicative. May also use conventional or instrumental gestures.",
                      "1": "Some spontaneous use of descriptive gestures but exaggerated or limited in range and/or contexts (e.g., occur only during \\"Demonstration Task\\"), OR frequent use of conventional or instrumental gestures, but rare or no use of descriptive gestures.",
                      "2": "Some spontaneous use of informational, conventional, or instrumental gestures, but rare or no use of descriptive gestures.",
                      "3": "No or very limited spontaneous use of conventional, instrumental, informational, or descriptive gestures.",
                      "8": "N/A (e.g., limited by physical disability)."}
            }
         }
    ],
    "B. Reciprocal Social Interaction": [
         {"B1":{
            "subtitle" : "Unusual Eye Contact",
            "description": "Coding for this item requires that clear, flexible, socially modulated, and appropriate gaze that is used for a variety of purposes be distinguished from gaze that is limited in flexibility, appropriateness, or contexts. If the participant is shy initially, and his or her gaze changes markedly and consistently as he or she becomes more comfortable, do not base the code on earlier impressions. However, if eye contact never improves, coding must be based on what is observed, even if the participant seems shy. Do not code eye contact that occurs between the participant and individuals other than the examiner who may be in the ADOS-2 assessment room.", 
            "value": {"0": "Appropriate gaze with subtle changes meshed with other communication.",
                      "2": "Uses poorly modulated eye contact to initiate, terminate, or regulate social interaction."}
            }
         },
         {"B2":{
            "subtitle" : "Facial Expressions Directed to Examiner",
            "description": "The rating for this item should indicate whether the participant's facial expressions are directed to the examiner for the purpose of communicating affective (e.g., enjoyment, frustration) or cognitive (e.g., puzzlement, skepticism) states. Facial expressions that are directed to objects or other people in the room, or that are undirected, are not rated here. Appropriate or slightly exaggerated facial expressions should be coded even if there are also odd expressions.", 
            "value": {"0": "Directs a range of appropriate facial expressions to the examiner in order to communicate affective or cognitive states.",
                      "1": "Some direction of facial expressions to the examiner (e.g., directs only expressions indicating emotional extreme(s), or occasionally directs wider range of expressions). A participant who has a limited range of facial expressions, but who directs almost all of his or her facial expressions to the examiner, may be rated here.",
                      "2": "Does not direct appropriate facial expressions to the examiner."}
            }
         },
         {"B3":{
            "subtitle" : "Language Production and Linked Nonverbal Communication",
            "description": "The purpose of this item is to code the degree to which, when the participant vocalizes, the vocalization is accompanied by subtle changes in gaze, facial expression, and gesture. This item should be coded on the basis of the vocalizations used, regardless of their frequency. Code the most typical occurrences, not merely the best ones. When assigning a rating, include vocalizations used to maintain interaction or to respond to the examiner, as well as initiations. A rating of 8 (uncodable) should be assigned by default if one or more of the following behaviors coded earlier in this protocol received a rating of 2: \\"Unusual Eye Contact\\", \\"Facial Expressions Directed to Examiner\\", or \\"Descriptive,d  Conventional, Instrumental, or InformationalGestures.", 
            "value": {"0": "Vocalization usually accompanied by subtle and socially appropriate changes in gesture, gaze, and facial expression.",
                      "1": "Vocalization accompanied by abnormal, limited, or less than usual frequency and/or range of gesture, gaze. and facial expression, OR use of one modality almost exclusively(e.g., frequent use of gaze, but limited use of gesture and facial expression).",
                      "2": "Little or no nonverbal communication linked with vocalization.",
                      "7": "Some avoidance of direct eye gaze, particularly at the beginning of the session, perhaps because of shyness. but shows some modulation and coordination of language and nonverbal behavior.",
                      "8": "N/A; no vocalization OR no or minimal use of gesture, facial expression, or socially directed gaze. This code should be assigned automatically if the absence of linking can be accounted for by the limited frequency of unusual eye contact, facial expressions, and/or gestures."}
            }
         },
         {"B4":{
            "subtitle" : "Shared Enjoyment in Interaction",
            "description": "Rate the participant's directed pleasure during any of the tasks or conversation. This item should not be used to indicate his or her general emotional state during the ADOS-2 evaluation. The rating applies to the participant's ability to indicate pleasure to the examiner, not just to interact or respond.", 
            "value": {"0": "Shows definite pleasure appropriate to context during interactive participation or conversation with the examiner in more than one task or conversational topic.",
                      "1": "Shows some pleasure appropriate to context during interactions with the examiner, OR shows definite pleasure during one interaction.",
                      "2": "Shows litte or no expressed pleasure during interaction with the examiner, but shows pleasure in his or her own speech or actions, or in noninteractive components of the ADOS-2 materials or activities.",
                      "3": "Little or no expressed pleasure during the ADOS-2 evaluation."}
            }
         },
         {"B5":{
            "subtitle" : "Comments on others' Emotions/Epathy",
            "description": "The focus of this item is on the participant's communication of his or her recognition, understanding, and/or response to the feelings of other people or characters, real or conveyed in stories or other tasks. Exclude shared enjoyment with the examiner, which is rated in the preceding item.", 
            "value": {"0": "Spontaneously communicates clear understanding or labeling of and/or appropriate response to several different emotions in other people/characters. Labeling several emotions in others is sufficient but not necessary if there are other clear indications of understanding and/or appropriate response.",
                      "1": "Communicates some understanding, labeling, or response to an emotion in others(e.g., spontaneously and correctly identifies at least one emotion in another person/character).",
                      "2": "No or minimal identification/communication of understanding of emotion in others."}
            }
         },
         {"B6":{
            "subtitle" : "Insight into Typical Social Situations and Relationships",
            "description": "The focus of this item is on the participant's ability to provide spontaneous examples of insight into the nature of social relationships. These can include ongoing relationships, such as friendships or marriage, or interactive situations, such as getting along with other students at school, that may be discussed in conversation or in response to the socioemotional questions. Two separate aspects of relationships are coded: (a) the nature of specific relationships (e.g., what is friendship), and (b) the participant's role in these relationships.", 
            "value": {"0": "Shows examples of insight into the nature of several typical social relationships (without evidence of lack of insight into these same relationships), including his or her own role in at least one. May show no more than one example of inaccurate understanding of other social relationships.",
                      "1": "Shows examples of insight into several typical social relationships, but not into his or her own role, OR into only one relationship including his or her own role.",
                      "2": "Shows some insight into one typical social relationship, though not necessarily about his or her own role in it.",
                      "3": "Shows no or limited insight into typical social relationships."}
            }
         },
         {"B7":{
            "subtitle" : "Quality of Social Overtures",
            "description": "This is a summary item that focuses on the quality of the participant's attempts to initiate social interaction with the examiner, not on the frequency of such attempts. Special attention should be given to the form of the overture and its appropriateness to thË social context. The rating should reflect the majority of social overtures to the examiner, not merely the best ones.", 
            "value": {"0": "Effectively uses nonverbal and verbal means to make clear social overtures to the examiner. The overtures must be appropriate to immediate contexts.",
                      "1": "Slightly unusual quality of some social overtures. Overtures may be restricted to personal demands or related to the participant's own interests, but with some attempt to involve the examiner in those interests.",
                      "2": "Inappropriate overtures; many overtures lack integration into context AND/OR social quality. This includes the participant's bringing up preoccupations with little attempt to involve the examiner in them.",
                      "3": "No social overtures of any kind."}
            }
         },
         {"B8":{
            "subtitle" : "Amount of Social Overtures/Maintenance of Attention",
            "description": "The focus of this item is on the number of the participant's attempts to get, maintain, or direct the examiner's attention, AND/OR to direct the examiner's attention to objects, actions, or topics of interest to the participant. The rating for this item may include verbal or nonverbal behaviors if they are neither related to preoccupations nor aimed at getting objects, but seem to function primarily as a method of social contact. Do not include requests when rating this item except for a code of 3.", 
            "value": {"0": "Frequent attempts to get or maintain the examiner's attention AND/OR to direct the examiner's attention to objects, actions, or topics of interest to the participant.",
                      "1": "Some attempts at getting, maintaining, or directing the examiner's attention as described above for a rating of 0, but reduced in frequency or the number of different activities in which they are used.",
                      "2": "Makes occasional attempts to get, maintain, or direct the examiner's attention, including overtures solely related to preoccupations.",
                      "3": "Shows relatively little concern as to whether the examiner is paying attention to him or her unless he or she needs help (e.g., initiates social contact only when requesting).",
                      "7": "Unusually frequent, intense, or excessive demands for attention."}
            }
         },
         {"B9":{
            "subtitle" : "Quailty of Social Response",
            "description": "This is a summary item that focuses on the participant's social responses throughout the ADOS-2 evaluation.", 
            "value": {"0": "Shows a range of appropriate responses that are varied according to immediate social situations and presses.",
                      "1": "Shows responsiveness to most social contexts, but somewhat limited, socially awkward, inappropriate, inconsistent, or consistently negative.",
                      "2": "Odd, stereotyped responses, or responses that are restricted in range or inappropriate to the context.",
                      "3": "Minimal or no response to the examiner's attempts to engage the participant."}
            }
         },
         {"B10":{
            "subtitle" : "Amount of Reciprocal Social Communication",
            "description": "The focus of this item is on the frequency with which reciprocal interchanges occur during the course of the ADOS-2 evaluation, using any mode of communication. Frequency here is defined both by absolute number of occurrences and distribution across a range of contexts.The rating for this summary item should describe aspects of nonverbal and verbal/vocal behavior that need not be coordinated but must result in at least brief reciprocal interchanges with the examiner (not others who may be present in the ADOS-2 assessment room).",
            "value": {"0": "Extensive use of verbal or nonverbal behaviors (at whatever level attained) for social interchange (i.e., chat, comments, remarks, or nonverbal behaviors that appear to have reciprocal intent).",
                      "1": "Some reciprocal social communication (as described above for a rating of 0), but reduced in frequency or amount, or in the number of contexts in which such behaviors occur (regardless of the amount of nonsocial talk).",
                      "2": "Most communication is either object-oriented (i.e., to ask for things), OR response to questions, OR echolalic, OR concerned with particular preoccupations; little or no social chat or give-and-take.",
                      "3": "Little or no communication with the examiner."}
            }
         },
         {"B11":{
            "subtitle" : "Overall Quality of Rapport",
            "description": "The code for this item is a summary rating that reflects the examiner's overall judgment of the rapport established with the participant during the ADOS-2 evaluation. The rating should particularly take into account the degree to which the examiner had to modify his or her own behavior to maintain the interaction successfully.", 
            "value": {"0": "Comfortable interaction between the participant and examiner that is appropriate to the context of the ADOS-2 assessment.",
                      "1": "Interaction sometimes comfortable, but not sustained (e.g., sometimes feels awkward or stilted, or the participant's behavior seems mechanical or slightly inappropriate).",
                      "2": "One-sided or unusual interaction resulting in a consistently mildly uncomfortable session or a session that would have been difficult if the examiner had not continuously modified the structure of the situation beyond the standard activities in the ADOS-2 evaluation.",
                      "3": "The participant shows minimal regard for the examiner, OR the session is markedly uncomfortable for a significant proportion of the time."}
            }
         }
    ],
    "C. Imagination": [
         {"C1":{
            "subtitle" : "Imagination/Creativity",
            "description": "This item should be assigned a rating that reflects the degree to which any of several forms of creativity/inventiveness are exhibited by the participant throughout the ADOS-2 evaluation, either in his or her use of objects or through verbal descriptions.", 
            "value": {"0": "Several different spontaneous, inventive, creative activities or comments in conversation.",
                      "1": "Some creative or make-believe actions, but limited in range or occurring only in response to one structured situation (e.g., creating a story).",
                      "2": "Little spontaneous creative or make-believe actions, OR only actions that are repetitive OR stereotyped in quality.",
                      "3": "No creative or inventive actions (not even stereotyped or repetitive)."}
            }
         }
    ],
    "D. Stereotyped Behavior and Restricted Interests": [
         {"D1":{
            "subtitle" : "Unusual Sensory Interest in Play Material/Person",
            "description": "Rate the participant's interest in or unusual behaviors associated with sensory aspects of toys or surroundings (e.g., sniffing, repetitive feeling of texture, licking, mouthing, or biting, unusually strong interest in the  repetition of certain sounds, unusual or prolonged visual examination). If the participant has a preoccupation that is based on a sensory interest, this may be coded here as one unusual sensory interest. For example, if he or she shows an interest in radiators or plumbing, that is coded later in this section of the protocol under \\"D4. Excessive Interest in or References to Unusual or Highly Specific Topics or Objects or Repetitive Behaviors.\\" If the participant is interested in the radiator in the room because he or she likes to look at it, as shown by peering at it while tilting his or her head, rocking from side to side, and jiggling his or her hands, this should be coded under \\"D2. Hand and Finger and Other Complex Mannerisms,\\" but it may also be coded here because of the sensory component involved. If the participant likes to look out of the corner of his or her eye at the radiator, the corners of the room, the doors on the cabinets, and the slats of the window blinds, but does not become overly preoccupied with any of these objects and does not move in unusual ways as he or she does so, he or she should be coded here for unusual sensory interests but not under \\"Hand and Finger and Other Complex Mannerisms\\" or under item \\"D4. Excessive Interest...\\" If the ADOS-2 assessment occurs in a room with a one-way mirror, looking into the mirror is not coded as an unusual sensory interest. Do not code here for touching the pin art. Sensory aversions are also not coded here.", 
            "value": {"0": "No unusual sensory interests or sensory-seeking behaviors.",
                      "1": "Several possible sensory interests not as clear as specified below for a rating of 2 AND/OR only one clear occurrence of an unusual sensory interest or a sensory-seeking behavior. One \\"possible\\" sensory interest should be coded 0.",
                      "2": "Definite interest in sensory elements of objects or of play materials, OR sensory examination of himself or herself or others; two or more clear occurrences must be observed. May be observed during the same activity.",
                      "3": "Definite unusual sensory-seeking behaviors occur frequently, during at least two different tasks or activities, and may interfere with the ADOS-2 assessment."}
            }
         },
         {"D2":{
            "subtitle" : "Hand and Finger and Other Complex Mannerisms",
            "description": "Rate unusual and/or repetitive movements or posturing of the hands and fingers, arms. or body. Repetitive clapping may be coded here. Do not include body rocking unless it involves more than the torso. Finger tapping, nail biting, hair twisting, and thumb sucking are also not coded here. The participant does not have to watch the movements of his or her fingers or hands for the movements to be coded here.", 
            "value": {"0": "None.",
                      "1": "Unusual and/or repetitive hand and finger mannerisms or complex mannerisms not as clear as specified below for a rating of 2.",
                      "2": "Definite finger flicking or twisting, AND/OR hand or finger or complex mannerisms, stereotypies or posturing. May be brief and/or rare if clear.",
                      "3": "Mannerisms, as described above, occur frequently, during at least two different tasks or activities, and/or may interfere with the ADOS-2 assessment."}
            }
         },
         {"D3":{
            "subtitle" : "Self-injurious Behavior",
            "description": "Rate behaviors that involve any kind of aggressive act to self, even if not clearly harmful.", 
            "value": {"0": "No attempts to harm self.",
                      "1": "Dubious or possible self-injury, and/or rare but clear self- injury (e.g., one clear example of biting at own hand or arm, pulling own hair, slapping own face, or banging own head).",
                      "2": "More than one clear example of self-injury, such as head banging, face slapping. hair pulling, or self-biting."}
            }
         },
         {"D4":{
            "subtitle" : "Excessive Interet in or Reference to Unusual or Highly Specific Topics or Objects or Repetitive Behaviors",
            "description": "Because circumscribed interests, preoccupations, or unusual behaviors are often difficult to judge during a brief observation, the focus of this item is on any references that (a) are unexpectedJy high in frequency, (b) pertain to an unusual or odd topic, (c) are not well integrated into the conversation, or any behaviors that (d) pertain to use of an object in a manner highly specific to the participant, or (e) pertain to use of the participant's own body in a highly specific manner not clearly associated with behaviors coded under items D1 (SensoryInterests) or D2 (Hand/Finger Mannerisms); for example, putting his or her hands over and/or fingers in his or her ears should be considered here. Persistent aversive reactions that are unusual in form and/or intensity to sensory stimuli (e.g., the feel of the laminated picture, the sound of the examiner clearing his or her throat) can be coded here as 1, 2, or 3, as appropriate. Topics that are developmentally or age appropriate should not be coded here (e.g., an 8-year-old who repeatedly talks about a recent vacation in general terms would not be coded here; if he or she repeatedly talks about staying in hotel room 465, that behavior would be considered here). The focus of this item is on the topic of references and/or unusual forms of behavior. Use of unusual terms (e.g., stereotyped phrases) and/or lack of conversational flexibility are coded elsewhere. Behaviors may be coded in two ways if they represent separate instances of each domain. For instance, if the participant repeatedly says \\"Do they need room service in room 465?\\", uses the same phrase in several other contexts (\\"No more room service!.\\" \\"Room service now!\\"), and makes other statements about hotel room numbers, this would be coded both here and under \\"A4. Stereotyped/Idiosyncratic Use of Words or Phrases\\" earlier in this protocol. Repetitive behaviors involving objects that have a clear sequence (e.g., touching objects in a particular order) should be coded under the following item, \\"Compulsions or Rituals.\\"", 
            "value": {"0": "No excessive interest in or references to unusual or highly specific or restricted topics or objects or repetitive behaviors.",
                      "1": "Occasional references to unusual or highly specific topics or patterns of interest, occurring to an unusual degree, or occasional repetitive behaviors.",
                      "2": "Definite, stereotyped, or unusual patterns of interest that may or may not intrude and/or interfere with social communication and/or definite repetitive behaviors.",
                      "3": "Definite preoccupation(s) and/or repetitive behaviors to a degree that interferes with the ADOS-2 assessment."}
            }
         },
         {"D5":{
            "subtitle" : "Compulsions or Rituals",
            "description": "The emphasis for compulsions or rituals in this context is on the participants determination to carry out an activity that involves a predictable sequence, endpoint, or manner that is not required as part of an ADOS-2 task (e.g., checking if a wallet is in a purse; insistence on completing the book used for the storytelling task; careful placement of materials as they were initially presented; reciting a list of classmates as friends). Provision of lists should be rated here.", 
            "value": {"0": "No obvious activities or verbal routines that must be completed in full or according to a sequence that is not part of the task.",
                      "1": "Unusually routinized in speech or activities (includes insistence on finishing the book or providing a list that is not relevant to the conversation), but no behavior that appears clearly compulsive in quality.",
                      "2": "One or more activities or verbal routines that the participant has to perform or say in a special way. The participant appears under pressure or becomes anxious if an activity is disrupted (i.e., compulsive quality is present). Include the recitation of lists that must be completed or that the examiner is asked to record (e.g., friends, favorite foods) or insistence that the examiner respond in a specific way."}
            }
         }
    ],
    "E. Other Abnormal Behaviors": [
         {"E1":{
            "subtitle" : "Overactivity/Agitation",
            "description": "This item describes excessive movement or physical agitation. Code this item relative to the participant's nonverbal mental age.", 
            "value": {"0": "Sits still appropriately throughout the ADOS-2 assessment.",
                      "1": "Sits, but often fidgets or moves about in the chair. Difficulties in the ADOS-2 assessment are not principally due to overactivity or agitation.",
                      "2": "Difficulty sitting; moves either in or out of the a chair or handles or manipulates objects in a way that is mildly disruptive.",
                      "3": "Overactive behaviors are difficult to interrupt. The level of activity disrupts the ADOS-2 assessment.",
                      "7": "Underactive."}
            }
         },
         {"E2":{
            "subtitle" : "Tantrum, Aggression, Negative or Disruptive Behavior",
            "description": "This item includes any form of anger or disruption beyond communication of mild frustration or whining.", 
            "value": {"0": "Not disruptive, destructive, negative, or aggressive during the ADOS-2 assessment.",
                      "1": "Displays an example of mild disruption, anger, or aggression or negative behavior to the examiner (includes verbal threats, swearing, or a deliberately loud voice).",
                      "2": "More than one intentionally disruptive or negative incident. Loud talking or repeated swearing is coded here.",
                      "3": "Shows marked or repeated temper tantrums or significant aggression (e.g., throwing things, hitting or biting others). Screaming  or yelling is included here."}
            }
         },
         {"E3":{
            "subtitle" : "Anxiety",
            "description": "Anxiety includes initial wariness or self-consciousness, as well as more obvious signs of worry, upset, or concern.", 
            "value": {"0": "No obvious anxiety (eg., trembling or jumpiness).",
                      "1": "Mild signs of anxiety or self-consciousness, especially at the beginning of the ADOS-2 session or in response to specific activities.",
                      "2": "Marked anxiety throughout the ADOS-2 assessment (may be intermittent or continuous)."}
            }
         }
    ],
    "Social Affect(SA)": "A7+A8+A9+B1+B2+B4+B7+B9+B10+B11",
    "Restricted and Repetitive Behavior(RRB)": "A4+D1+D2+D4",
    "Overall Total": "SA + RRB",
    "ADOS-2 Comparison Score":{
        "description": "Level of autism spectrum-related symptoms",
        "value":{
                "10": "high",
                "9": "high",
                "8": "moderate",
                "7": "moderate",
                "6": "moderate",
                "5": "low",
                "4": "low",
                "3": "low",
                "2": "minimal-to-no evidence",
                "1": "minimal-to-no evidence"
                }
        },
    "Classification": {
        "description": "Compare the Overall Total to the cutoff for Module3",
        "value":{
                "10": "autism",
                "9": "autism",
                "8": "autism spectrum",
                "7": "autism spectrum",
                "6": "non-spectrum",
                "5": "non-spectrum",
                "4": "non-spectrum",
                "3": "non-spectrum",
                "2": "non-spectrum",
                "1": "non-spectrum"
                }
    },
    "Comparison Score Conversion": {
        "description": "Convert Overall Total to Comparison Score",
        "matrix age range": "[[2,5], [6,9], [10,16]]",
        "Conversion Matrix": {"10":[[18,28],[18,28],[18,28]],
                              "9":[[16,17],[15,17],[15,17]],
                              "8":[[13,15],[13,14],[13,14]],
                              "7":[[12],[11,12],[11,12]],
                              "6":[[9,11],[9,10],[9,10]],
                              "5":[[8],[8],[8]],
                              "4":[[7],[7],[7]],
                              "3":[[5,6],[5,6],[5,6]],
                              "2":[[4],[3,4],[4]],
                              "1":[[0,3],[0,2],[0,3]]}
    }
}        
"""

data = json.loads(form_string)
print(data)
