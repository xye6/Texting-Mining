import json

form = '''
{
    "Family Info":{
        "Ethnicity":{"HL":"Hispanic or Latino origin",
                     "non":"Non-Hispanic or Non-Latino origin",
                     "n":"Do not wish to provide"},
        "Race":{"aian":"American Indian or Alaskan Native",
                "cw":"Caucasian/White",
                "nhop":"Native Hawaiian or Other Pacific",
                "a":"Asian",
                "ac":"Aboriginal Canadian Islander",
                "b":"Black or African American",
                "bc":"Black Canadian",
                "n":"Do not wish to provide"},
        "Marital status":{"m":"Married",
                          "d":"divorced",
                          "s":"separated",
                          "u":"unmarried",
                          "w":"widowed"}
        },           
    "Developmental and Medical History":[
        {"Pregnancy History":
            {"PH1":{
                "description": "Is the pregnancy history of the biological mother available?(If 'no' skip to next section)",
                "value":{"1":"Yes",
                         "-1":"No"}
                },
            "PH2":{
                "description":"How many times has the biological mother been pregnant:",
                "value":"number of times"
                },
            "PH3":{
                "description":"How many children does the biological mother have now?",
                "value":"number of children"
                },
            "PH4":{
                "description":"Did the biological mother lose any pregnancies?",
                "value":"number of loss"
                },
            "PH5":{
                "description":"Biological birth order of this child.",
                "value":{"number":"order number",
                         "0":"Unsure"}
                }
            }
        },
        {"Pregnancy and Perinatal History":
            {"PPH1":{
                "description":"Did the mother receive assisted reproductive technology?",
                "value":{"1":"Yes",
                         "-1":"No",
                         "0":"Unsure"}
                },
             "PPH2":{
                "description":"Biological mothers age at birth of child",
                "value":"age"
                },
             "PPH3":{
                "description":"Biological fathers age at birth of child",
                "value":"age"
                },
             "PPH4":{
                "description":"Did the mother have fever over 101F (excluding those occurring during labor & delivery) during the pregnancy with this child?",
                "value":{"1":"Yes",
                         "-1":"No",
                         "0":"Unsure"}
                },
             "PPH5":{
                "description":"Did the mother have any infection during the pregnancy with this child?",
                "value":{"infection names":"infection names",
                         "1":"yes but no infection name",
                         "-1":"No",
                         "0":"Unsure"}
                }
            }
        },
        {"Medications During Pregnancy":{
            "MDP1":{
                "description":"Check the one that best describes alcenol use during pregnancy.",
                "value":{"0":"Unsure",
                         "1":"No alcohol use",
                         "2":"1 drink or lss per week",
                         "3":"1 drink per day",
                         "4":"2 or more drinks per day"} 
                },
            "MDP2":{
                "description":"Check the one that best describes tobacco use during pregnancy.",
                "value":{"0":"Unsure",
                         "1":"None",
                         "2":"less than 10 cigarettes a day",
                         "3":"pack or more per day"} 
                }
            }
        },
        {"Labor and Delivery":{
            "LD1":{
                "description":"Was this child:",
                "value":{"1":"Singleton",
                         "2":"One of twins, unsure type",
                         "3":"One of triplets",
                         "4":"One of multiple",
                         "i":"identical twins",
                         "f":"fraternal twins"} 
                },
            "LD2":{
                "description":"Was this child born by:",
                "value":{"1":"vaginal delivery",
                         "2":"cesarean section"} 
                },
            "LD3":{
                "description":"Were there any labor or delivery complications?",
                "value":{"description":"If yes, describe",
                         "1":"no word or can't distinguish",
                         "-1":"No",
                         "0":"Unsure"}
                },
            "LD4":{
                "description":"What was the length of the pregnancy",
                "value":{"...m":"number of months",
                         "...w":"number of weeks"}
                }
            }
        },
        {"Developmental History":{
            "description":"Please tell us if your child has learned any of the following skills,even if he or she later stopped doing that skill. If 'Yes' please provide your best estimate of the age first learned.",
            "value":{"age":"Age first achieved",
                      "-1":"no",
                      "1":"achieved unsure age"},
            "skills":{"s1":"Walk (without holding on)",
                      "s2":"First words (other than mama/dada)",
                      "s3":"First phrases (2-3 words)",
                      "s4":"Toilet trained"}
            }
        },
    
    {"Health and Mental Health History":{
        "description":"Are any of these health concerns a problem for the child currently or were they a concern in the past?",
        "Health Concerns":{
            "B1-B27":{
                "B1":"Headaches",
                "B2":"Vision problems",
                "B3":"Ear, nose and throat problems",
                "B4":"Dental problems",
                "B5":"Heart conditions",
                "B6":"Asthma or other lung problem",
                "B7":"Nausea/Vomiting",
                "B8":"Reflux",
                "B9":"Diarrhea",
                "B1O":"Constipation",
                "B11":"Stomach/abdominal pain",
                "B12":"Feeding problem",
                "B13":"Kidney/ bladder/genital problems",
                "B14":"Bone or joint problems",
                "B15":"Blood or anemia problems",
                "B16":"Skin conditions",
                "B17":"Endocrine or hormone problems",
                "B18":"Seizures",
                "B19":"Tics",
                "B20":"Allergies (food, medication environmental)",
                "B21":"Genetic Disorder",
                "B22":"Loss of skills/regression",
                "B23":"Depression",
                "B24":"Bipolar mood disorder",
                "B25":"Anxiety disorder",
                "B26":"Obsessive compulsive disorder (OCD)",
                "B27":"Attention Deficit Hyperactivity Disorder (ADHD)"},
            "value":{"1":"Never a problem",
                 "2":"Currently a problem",
                 "3":"Was a problem in the past",
                 "4":"Unsure"}
        },
        "Physical Disability":{
            "description":"Does your child have a physical disability such as cerebral palsy or spina bifida that makes it difficult for him or her to walk or get from place to place?",
            "value":{"0":"no",
                     "1":"wear braces or AFO",
                     "2":"use a walker or wheelchair",
                     "3":"require other medical devices such as oxygen, tracheostomy, or feeding tube"}
        },
        "HMHH1":{
            "description":"Has your child been admitted to the hospital overnight or had surgery?",
            "value":{"1":"yes",
                     "-1":"no"}
            },
        "HMHH2":{
            "description":"Has your child had blood drawn to test lead level?",
            "value":{"1":"Yes",
                         "-1":"No",
                         "0":"Unsure"}
            },
        "HMHH3":{
            "description":"Has your child had a hearing test? If yes, at what age?",
            "value":{"-1":"No",
                     "0":"Unsure",
                     "age":"age of hearing test"}
            },
        "HMHH4":{
            "description":"Is your child up to data on immunizations?",
            "value":{"1":"Yes",
                     "-1":"No",
                     "0":"Unsure"}
            },
        "HMHH5":{
            "description":"Does your child take any medicines regularly? If yes, please list:",
            "value":{"-1":"No",
                     "0":"Unsure",
                     "1":"yes but no medicine name",
                     "medicines":"dose, name, reason"}
            }
        }
    }
    ],
    "Family History":{
        "description":"The questions below ask about the family history of the child. Please let us know if there is someone in the child's family who has each disorder listed. If Yes, indicate which family member(s). Include only biological (blood) relatives",
        "disorder":{
            "d1":"Autism Spectrum Disorder(including Aspergers disorder and PDD-NOS)",
            "d2":"learning disability",
            "d3":"intellectual disability (mental retardation)",
            "d4":"Speech Delay or disorder, received speech therapy",
            "d5":"ADHD",
            "d6":"Anxiety, Depression,Obsessive CompulsiveDisorder (OCD)",
            "d7":"Manic Depression or Bipolar Disorder",
            "d8":"Schizophrenia",
            "d9":"Tics or Tourette's Syndrome",
            "d10":"Seizures",
            "d11":"Fragile X",
            "d12":"Tuberous Sclerosis or Neurofibromatosis",
            "d13":"Auto-immune disorders (e.g.. Lupus, RheumatoidArthritis, Multiple Sclerosis)",
            "d14":"Gastrointestinal diseases(Crohn's or Ulcertative Colitis, Celiac, Irritable Bowerl, etc.)"},
        "value":{"-1":"No",
                 "0":"Unsure",
                 "1":"Grandmother",
                 "2":"Grandfather",
                 "3":"Cousin",
                 "4":"Mother",
                 "5":"Father",
                 "6":"Other",
                 "7":"Aunt/Uncle",
                 "8":"Sister/Brother"}
                 
    },
    "Sleep Behavior":{
        "description":{
            "C1": "During the week what time does your child usually go to sleep?",
            "C2": "During the week what time does your child usually wake up?",
            "C3":"On the weekend what time does your child usually go to sleep?",
            "C4":"On the weekend what time does your child usually wake up?",
            "C5":"Child goes to bed at the same time at night",
            "C6":"Child falls asleep within 20 minutes after going to bed",
            "C7":"Child falls asleep alone in own bed",
            "C8":"Child falls asleep in parent's or siblings bed",
            "C9":"Child needs parent in the room to fall asleep",
            "C10":"Child struggles at bedtime (cries, refuses to stay in bed, etc.)",
            "C11":"Child is afraid of seeping in the dark",
            "C12":"Child is afraid of sleeping alone",
            "C13":"Child's usual amount of sleep each day(combining night time sleep and naps)",
            "C14":"Child sleeps too little",
            "C15":"Child sleeps the right amount",
            "C16":"Child sleeps about the same amount each day",
            "C17":"Child wets the bed at night",
            "C18":"Child talks during sleep",
            "C19":"Child is restless and moves a lot during sleep",
            "C20":"Child sleepwalks during the night",
            "C21":"Child moves to someone else's bed during the night (parent, brother, sister, etc.)",
            "C22":"Child grinds teeth during sleep (vour dentist may have told you this)",
            "C23":"Child snores loudly",
            "C24":"Child seems to stop breathing during sleep",
            "C25":"Child snorts and/or gasps during sleep",
            "C26":"Child has trouble sleeping away from home (visiting relatives, vacation, etc.)",
            "C27":"Child awakens during the night screaming,sweating, and inconsolable",
            "C28": "Child awakens alarmed by a frightening dream",
            "C29":"Child awakes once during the night",
            "C30":"Child awakes more than once during the night",
            "C31":"Write the number of minutes a night waking usually lasts (If they do not wake during the night, please record 0 min.)",
            "C32":"Child wakes up by him/herself",
            "C33":"Child wakes up in negative mood",
            "C34":"Adults or siblings wake up child",
            "C35":"Child has difficulty getting out of bed in the morning",
            "C36":"Child takes a long time to become alert in the morning",
            "C37":"Child seems tired",
            "C38":"Child has appeared very sleepy or fallen asleep watching TV",
            "C39":"Child has appeared very sleepy or fallen asleep riding in car"},
        
        "C1-C4 value":"Time",
        "C5-C30 & C32-C37 value":{"-1":"Not a problem",
                                  "0":"It's a problem but don't known how often",
                                  "1":"rarely(0-1)",
                                  "2":"sometimes(2-4)",
                                  "3":"usually(5-7)"},
        "C13 & C31 value":"time",
        "C38,C39 value":{"1":"Not Sleepy",
                         "2":"Very Sleepy",
                         "3":"Falls Asleep",
                         "4":"Not Applicable"}
    }
           
}    
    

'''
data = json.loads(form)
print(data)
