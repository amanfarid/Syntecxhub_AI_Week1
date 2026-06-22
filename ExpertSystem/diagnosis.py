def run_inference(
    facts,
    rules
):

    logs = []

    changed = True

    while changed:

        changed = False

        for conditions, result in rules:

            if conditions.issubset(
                facts
            ):

                if result not in facts:

                    facts.add(result)

                    logs.append(
                        f"{conditions} -> {result}"
                    )

                    changed = True

    return facts, logs