import json

form = '''
{
    "Personal Info":{
        "pi1":{
            "description":"has this student ever repeated a grade?",
            "value":{"0":"No",
                      "1":"Yes but no grade written",
                      "grade":"grade"}
        },
        "pi2":{
            "description":"his this student been reviewed by the Committee on Special Education(CSE)?",
            "value":{"0":"No",
                     "1":"Yes"}
        },
        "pi3":{
            "description":"when was he/she classified",
            "value":{"0":"not classified",
                      "time":"the time classified"}
        },
        "pi4":{
            "description":"what classification",
            "value":{"0":"no classification",
                     "classification":"classification description"}
        },
        "pi5":{
            "description":"Does this student currently have an IEP?",
            "value":{"0":"No",
                    "1":"Yes"}
        },
        "pi6":{
            "description":"Does this student currently have a 504 Accommodation/Support Plan?",
            "value":{"0":"No",
                      "1":"Yes"}
        },
        "pi7":{
            "description":"Does this student receive AIS or other instructional remediation/support?",
            "value":{"0":"No",
                     "1":"yes"},
            "services":{
                "services description": {
                    "a1":"Reading Decoding",
                    "a2":"Reading Comprehension",
                    "a3":"Math Computation",
                    "a4":"Math Application",
                    "a5":"Written Language",
                    "a6":"other"},
                "value":"frequency/length of service per week/cycle, remedial instruction, supplemental instruction, push-in or pull-out(if other, add description"
                }
        },
        "pi8":{
            "description":"Does this student receive services from a special education teacher (inclusion classroom/blended classroom/consultant teacher/resource room/self-contained classroom)?",
            "value":{"0":"No",
                     "1":"Yes but no description",
                     "description":"if yes and described"}
        },
        "pi9":{
            "description":"Does this student receive instruction outside of a general education classroom?",
            "value":{"0":"No",
                     "1":"Yes but no description",
                     "description":"if yes and described"}
        },
        "pi10":{
            "description":"Does this student receive related services (e.g. speech/language therapy/occupational therapy, physical therapy/counseling/adaptive physical education)",
            "value":{"0":"No",
                      "1":"yes"},
            "services":{
                "services description": {
                    "b1":"Adaptive Physical Education",
                    "b2":"Counseling",
                    "b3":"Occupational Therapy",
                    "b4":"Physical Therapy",
                    "b5":"Speech/Language Therapy",
                    "b6":"Physical Therapy",
                    "b7":"Aide/Note-taker",
                    "b8":"Other"},
                "value":"type of service:direct, indirect, and/or consult individual and/or group, frequency/length of service per week/cycle/month, push-in or pull-out(if other, add description)"
            }
        },
        "pi11":{
            "description":"Does this student have a modified curriculum?",
            "value":{"0":"No",
                      "explanation":"If yes, explain"}
            },
        "pi12":{
            "description":"Does this student have a 12-month program or receive services during the summer?",
            "value":{"0":"No",
                      "explanation":"If yes, explain"}
            },
        "pi13":{
            "description":"Does this student have an instructional team with an assugned case manager?",
            "value":{"0":"No",
                      "explanation":"If yes, explain"}
            }
    },
    "Previous Evaluations":{
        "pe1d":{
            "description":"Psychological date",
            "value":"date"
        },
        "pe1r":{
            "description":"Psychological result",
            "value":"result"
        },
        "pe2d":{
            "description":"Educational date",
            "value":"date"
        },
        "pe2r":{
            "description":"Educational result",
            "value":"result"
        },
        "pe3d":{
            "description":"Speech/Language date",
            "value":"date"
        },
        "pe3r":{
            "description":"Speech/Language result",
            "value":"result"
        },
        "pe4d":{
            "description":"Occupation Therapy date",
            "value":"date"
        },
        "pe4r":{
            "description":"Occupation Therapy result",
            "value":"result"
        },
        "pe5d":{
            "description":"Physical Therapy date",
            "value":"date"
        },
        "pe5r":{
            "description":"Physical Therapy result",
            "value":"result"
        },
        "pe6d":{
            "description":"Other evaluations data",
            "value":"date"
        },
        "pe6r":{
            "description":"Other evaluations result",
            "value":"result"
        }
    },
    "Academic Achievement":{
        "reading":{
            "r1":{
                "description":"current reading level: Decoding",
                "value":"description"
                },
            "r2":{
                "description":"current reading level: comprehension",
                "value":"description"
                },
            "r3":{
                "description":"tests used",
                "value":"description"
                },
            "r4":{
                "description":"current reading program",
                "value":"description"
                },
            "r5":{
                "description":"classroom setting for reading instruction",
                "value":"description"
                },
            "r6":{
                "description":"reading strengths",
                "value":"description"
                },
            "r7":{
                "description":"reading weakness",
                "value":"description"
                }
            },
        "mathematics":{
            "m1":{
                "description":"current math level: Decoding",
                "value":"description"
                },
            "m2":{
                "description":"current math level: applied math skills",
                "value":"description"
                },
            "m3":{
                "description":"tests used",
                "value":"description"
                },
            "m4":{
                "description":"current math program",
                "value":"description"
                },
            "m5":{
                "description":"classroom setting for math instruction",
                "value":"description"
                },
            "m6":{
                "description":"math strengths",
                "value":"description"
                },
            "m7":{
                "description":"math weakness",
                "value":"description"
                }
            },
        "Written Language":{
            "w1":{
                "description":"current level of written language skills",
                "value":"description"
                },
            "w2":{
                "description":"tests used",
                "value":"description"
                },
            "w3":{
                "description":"current written language program",
                "value":"description"
                },
            "w4":{
                "description":"written language strengths",
                "value":"description"
                },
            "w5":{
                "description":"written language weaknesses",
                "value":"description"
                }
            }
    }


}'''

data = json.loads(form)
print(data)
