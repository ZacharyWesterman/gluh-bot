REPLIES = (
    (10, "gluh"),
    (10, "Gluh."),
    (5, "...gluh?"),
    (5, "g l u h"),
    (5, "gluh..."),
    (4, "gluh!"),
    (4, "gluh?"),
    (3, "GLUH!!"),
    (3, "gluh gluh"),
    (3, "\\*gluh noises\\*"),
    (3, "g-gluh...?"),
    (3, "gluh :3"),
    (3, "gluh 😀"),
    (3, "gluh ☹️"),
    (3, "gluh 🫤"),
    (3, "gluh™"),
    (3, "gluh moment 🤯"),
    (3, "gluh 👍"),
    (3, "gluh 👎"),
    (2, "gluhn't"),
    (2, "many such cases."),
    (2, "source: gluh"),
    (1, '> Guhhhh, gluh.\n\\- gluh'),
    (1, "ERROR: gluh overflow"),
    (1, "1. gluh\n2. gluh\n3. ???\n4. gluh"),
    (1, "gluh quota exceeded"),
    (0.5, "gluh has reviewed your message and chosen violence"),
    (0.5, "gluh has been advised by legal counsel not to comment"),
    (0.5, "gluh? in this economy?"),
    (0.5, "gluh jumpscare (real)"),
    (0.5, "you have alerted the gluh"),
    (0.5, "gluh detected. activating neurotoxin."),
    (0.5, "I am in incredible pain. Uh, I mean... gluh"),
    (0.5, "gluh: command not found"),
    (0.5, "gluh returned exit code 137"),
    (0.5, "core dumped (gluh)"),
    (0.2, "gluh service unavailable due to gluh"),
    (0.2, "known issue: gluh"),
    (0.1, "One day you will answer for your crimes. And God will not be as merciful as I am."),
    (0.1, "srry busy overthrowing lithuania. be bac l8r."),
    (0.1, "every copy of gluh is personalized"),
    (0.1, "> No, go ahead, I've got this covered.\n> Yeah they still think it's a bot.\n> Of course I turned audio transcription off, why?\n> What?\n> Oh for fu-\n\n[END OF AUDIO LOG]"),
)


def messages() -> list[float]:
    return [i[1] for i in REPLIES]


def weights() -> list[str]:
    return [i[0] for i in REPLIES]
