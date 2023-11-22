"""Test cases for the review_evidence_central"""
"""
This test checks for text before '## ABSTRACT'
if it exists it will fail so that the text will
be removed and also checks for ![](/api/attachments/2107/download)
if it exist the test will fail but if it doesn't it will pass
"""
# flake8: noqa

import re


mark_text = """

## ABSTRACT

Like other known examples of metal documents, the book of Mormon contains blessings and curses, often in association with covenants.

---

##### EVIDENCE SUMMARY

One of the purposes of the Book of Mormon is to make known many of the “covenants of the Lord” ([Title Page of the Book of Mormon](https://www.churchofjesuschrist.org/study/scriptures/bofm/bofm-title?lang=eng)). As such, the text often describes the blessings that come from following its prophetic teachings and the consequences that result from their rejection. Like the Book of Mormon, metal plates in antiquity sometimes recorded curses and blessings.

**Ancient Near Eastern Plates**

Treaties in the ancient world were sometimes solemnized by inscribing them on metal plates. The text of these treaties often appealed to the deities worshipped by the respective parties to witness these significant agreements and enact the blessings or curses stated according to the integrity or treachery of those who accepted their conditions.

One such treaty between Pharaoh Rameses II and the Hittite king Hattusili was inscribed on a silver tablet (1280 BC.) After stipulating the terms of the peace agreement between the two kingdoms, it states, “as for these words, a thousand gods of the male gods and of the female gods of them of the land of Egypt, are with me as witnesses [*hearing*] these words.”[1](http://n1) Another Hittite Treaty between the Hittite kings Tudhaliya IV and Kurunta of Tarhuntassa (1235 BC) inscribed on a bronze plate reads, “the Thousand Gods have now been called to assembly for (attesting the contents of) this treaty tablet that I have just executed for you. Let them see, hear, and be witnesses thereto.”[2](#n2)

In addition to an appeal to divine witnesses, such treaties pronounced divine blessings or curses upon those who kept or failed to keep the conditions of the covenant. The treaty between Egypt and the Hittites states, “As for these words which are on the tablet of silver of the land of Hatti and of the land of Egypt—as for him who shall not keep them, a thousand gods of the land of Hatti, together with a thousand gods of the land of Egypt, shall destroy his house, his land, and his servants.”[3](#n3)

On the other hand for those “who shall keep these words which are on this tablet of silver, whether they are Hatti or whether they are Egyptians, and they are not neglectful of them, a thousand gods of the land of Hatti, together with a thousand gods of the land of Egypt, shall cause that he be well, shall cause that he live, together with his houses and his (land) and his servants.”[4](#n4)

The Hittite bronze tablet of Tudhaliya IV warns, “If you, Karunta, fail to comply with these treaty clauses, and do not remain loyal to My Majesty and subsequently the descendants of My Majesty as your rulers” and rebel, “then may these oath-deities destroy you together with your posterity.”[5](#n5) Loyalty, however, would cause the deities to “take good care of you, and may you grow old under the protection of My Majesty.”[6](#n6)

Several plates of gold, silver, and bronze were discovered in the foundations of a ruined Assyrian palace in Khorsabad in 1854. These recounted various deeds and donations bestowed by the king upon the temple of his gods. A part of the inscription, however, warns that whoever “brings to naught the law which I have established,—may Assur, Ningal, Adad, and the great gods, who dwell therein … set him in chains under (the heel) of his foe.”[7](#n7)

It also reads, “Let (some) future prince restore its ruins, let him inscribe his memorial stele and set it up alongside of mine. (Then) Assur will hear his prayers. Whoever destroys the work of my hands, who obliterates (the evidence of) my noble deeds, may Assur, the great lord, destroy his name and his seed from the land.”[8](#n8) These examples show an ancient pattern in which divine beings are invoked as witnesses and called upon to bless or curse.

**Greco-Roman Plates**

Later, in the Greco-Roman World, treaties between nations and even some laws passed by local assemblies were engraved upon bronze plates and invoked curses upon those who broke such agreements.[9](#n9) Many examples of lead plates recovered from Greece, Italy and Great Britain have been inscribed with curses to be invoked against evil doers or in the hopes of obtaining divine vengeance.[10](#n10)


Defixio tabella with an opisthographic curse in Greek against Kardelos. Lead, 4th century CE. From the Columbarium of the Villa Doria Pamphilj in Rome. Image and caption via Wikimedia commons.

**Indian Copper Plate Grants**

Copper plate inscriptions were an important class of legal document in ancient and medieval India and other parts of southern Asia which bestowed land and related rights and privileges upon brahmins by kings. Vedic law stipulated that when a king or ruler bestowed a grant, the record should be inscribed and include “an imprecation against him who should appropriate the donation to himself and should be signed with his own seal.”[11](#n11) Even the king was specifically warned that he must “not appropriate to himself landed property bestowed (upon Brahmanas) by other (rulers).”[12](#n12) Many examples of copper plate grants which have been rediscovered in the last two centuries record blessings to be bestowed upon the donors and curses upon those who might attempt to seize or take back the land granted.

A copper plate recovered from Bangladesh and dating to AD 478 states that “the giver of this land resides sixty thousand years in heaven; the one who challenges (a donation) as the one who approves (of the challenge) will reside as many [years] in hell. The one who would steal land given by himself or another becomes a worm in the excrement and is cooked with his ancestors.”[13](#n13) The Velvikudi grant, a set of ten copper plates from the 8th century AD, states, “Oh! Gladdener of your race! He that makes a gift on this earth blesses (his) ten generations past and future; and he that takes away (that which has been given) destroys ten generations past and future. To him that robs land given by himself or by others, there is no expiation anywhere except in dreadful hell.”[14](#n14)

The Baroda Copper Plate Inscription from Gujarit (AD 812) reads, “and anyone who, his mind being covered by a dark veil of ignorance, might revoke or allow someone else to revoke [this grant], would be guilty of the five great sins and five minor sins.” While the one who gifts this grant was to reside in heaven for sixty-thousand years, the one who “revokes it or allows [another to revoke it] dwells for the same period in hell.”[15](#n15) These examples show how such gifts of land were considered inviolable and not to be treated lightly.


The Velvikudi inscription is an 8th-century bilingual copper-plate grant from the Panday kingdom of southern India. Image via Wikimedia Commons. Caption via Wikipedia.

**Curses and Blessings in the Book of Mormon**

Book of Mormon prophets solemnly state the consequences of accepting or rejecting their testimony. Moroni explains in his abridgment of the book of Ether that he inscribed an account of the vision of the brother of Jared upon his father’s plates, but that this account was sealed to come forth at a later time to those who prove worthy ([Ether 4:4–7](https://www.churchofjesuschrist.org/study/scriptures/bofm/ether/4.4-7?lang=eng#p4)).

Moroni, declaring the words of Christ, then pronounces a curse upon those who fight against what he has written: “And **he that will contend against the word of the Lord**, let him be **accursed**; and **he that shall deny these things**, let him be **accursed**; for unto them will **I show no greater things**, saith Jesus Christ; for I am he who speaketh” ([Ether 4:8](https://www.churchofjesuschrist.org/study/scriptures/bofm/ether/4.8?lang=eng#p8)). A blessing is then pronounced upon those who do not resist Christ’s words: “But **he that believeth** these things which I have spoken, him will I **visit with the manifestations of my Spirit**, and **he shall know and bear record**. For because of my Spirit **he shall know that these things are true**; for it persuadeth men to do good ([Ether 4:11](https://www.churchofjesuschrist.org/study/scriptures/bofm/ether/4.11?lang=eng#p11)).[16](#n16)

Covenants mentioned in the Book of Mormon often provide warnings of condemnation if they are broken or if those who make them act in unworthiness. These include the blessings of the Gospel offered through the Church of Jesus Christ in the Latter-days ([3 Nephi 21:11–25](https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/21.11-25?lang=eng#p11)), the baptismal covenant ([2 Nephi 31:14](https://www.churchofjesuschrist.org/study/scriptures/bofm/2-ne/31.14?lang=eng#p14), [20](https://www.churchofjesuschrist.org/study/scriptures/bofm/2-ne/31.20?lang=eng#p20)), and the sacramental covenant ([3 Nephi 18:13](https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/18.13?lang=eng#p13), [29](https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/18.29?lang=eng#p29)).

**Curses and Blessings Associated with the Land of Promise**

Like copper plate grants, significant curses and blessings in the Book of Mormon are associated with the land which the Lord covenanted to his people in the Book of Mormon. Lehi taught his children that “if iniquity shall abound **cursed** shall be the land for their sakes, but unto the righteous it shall be **blessed** forever” ([2 Nephi 1:7](https://www.churchofjesuschrist.org/study/scriptures/bofm/2-ne/1.97?lang=eng#p7)). Alma taught his son Helaman, “Yea, and **cursed** be the land forever and ever unto those workers of darkness and secret combinations, even unto destruction, except they repent before they are fully ripe” ([Alma 37:31](https://www.churchofjesuschrist.org/study/scriptures/bofm/alma/37.31?lang=eng#p31)).

This applies not only to those of the past but those today and in the future. “Thus saith the Lord God—**Cursed** shall be the land, yea, this land unto every nation, kindred, tongue, and people, unto destruction, which do wickedly, when they are fully ripe; and as I have said so shall it be; for this is the **cursing** and the **blessing** of God upon the land” ([Alma 45:16](https://www.churchofjesuschrist.org/study/scriptures/bofm/alma/45.16?lang=eng#p16)).

**Conclusion**

Curses and blessings in relation to treaties, covenants, and other official documents can be found on a variety of metal documents, spanning from the Mediterranean to southern Asia and from the second millennium BC to the Middle Ages. As a covenant text filled with prophetic warnings and promised blessings, the Book of Mormon fits well among the known examples of metal records from ancient and Medieval history.


"""


def check_text_before_abstract(markdown_content):
    # result check variable boolean
    result_check = []

    # Search for the position of "abstract" (case insensitive)
    abstract_match = re.search(r"\b## ABSTRACT\b", markdown_content, re.IGNORECASE)

    if abstract_match:
        # Check content before the "abstract" text
        abstract_position = abstract_match.start()

        # Check if there is text before the "abstract" section
        if abstract_position > 0:
            result_check.append(True)
        else:
            result_check.append(False)

    else:
        result_check.append(False)

    img_match = re.search(r"!\[\]\(/api/attachments/\d+/download\)", markdown_content, re.IGNORECASE)

    if img_match:
        result_check.append(True)
    else:
        result_check.append(False)

    return result_check


def test_review_evidence_central() -> None:
    """It returns a valid Document for evidence central."""

    result = check_text_before_abstract(mark_text)
    assert len(result) == 2
    assert result[0] == False
    assert result[1] == False
