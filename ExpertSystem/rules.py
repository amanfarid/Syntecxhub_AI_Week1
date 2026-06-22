rules = [

    (
        {"fever", "cough"},
        "flu"
    ),

    (
        {"flu", "body_pain"},
        "viral_infection"
    ),

    (
        {"rash", "fever"},
        "measles"
    ),

    (
        {"headache", "fever"},
        "dengue"
    ),

    (
        {"dengue"},
        "visit_hospital"
    ),

    (
        {"viral_infection"},
        "consult_doctor"
    )

]