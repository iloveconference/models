"""Test cases for the review_evidence_central"""
"""
This test checks for text before '## ABSTRACT'
if it exists it will fail so that the text will
be removed and also checks for ![](/api/attachments/2107/download)
if it exist the test will fail but if it doesn't it will pass
"""
# flake8: noqa

import re
from typing import Any

from models.load_evidence_central import clean_data


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

mark_text = """

[\n\n![Christ delivering the Sermon on the Mount. Image via churchofjesuschrist.org.](/api/attachments/1959/thumbnail/w760)\nChrist delivering the Sermon on the Mount. Image via churchofjesuschrist.org.\n\n---\n\n## ABSTRACT\n\nThe omission of the phrase \u201cwithout a cause\u201d in Christ\u2019s Sermon at the Temple in 3 Nephi finds support in early New Testament manuscripts and modern biblical scholarship.\n\n---\n\n##### EVIDENCE SUMMARY\n\nWhen the resurrected Jesus visited the people of Nephi at the temple in Bountiful, he gave them a version of the Sermon on the Mount which he taught during his mortal ministry ([Matthew 5\u20137](https://abn.churchofjesuschrist.org/study/scriptures/nt/matt/5.1?lang=eng#p1); [3 Nephi 12\u201314](https://abn.churchofjesuschrist.org/study/scriptures/bofm/3-ne/12.1?lang=eng#p1)). While the wording is very similar in both texts, they also contain some differences, as noted in an important study by John W. Welch.[1](#n1) One discrepancy is especially noteworthy.\n\nIn the King James Version of the Gospel of Matthew, Jesus taught: \u201cBut I say unto you, That whosoever is angry with his brother **without a cause** (*eike\u0304i* ) shall be in danger of the judgment\u201d ([Matthew 5:21\u201322](https://abn.churchofjesuschrist.org/study/scriptures/nt/matt/5.21-22?lang=eng#p21)). In contrast, the record of Jesus\u2019 words to the Nephites omits the phrase \u201cwithout a cause\u201d ([3 Nephi 12:22](https://abn.churchofjesuschrist.org/study/scriptures/bofm/3-ne/12.22?lang=eng#p22)).[2](#n2)\n\n**Evidence from New Testament Manuscripts**\n\nInterestingly, this same omission can be found in some early New Testament manuscripts. Welch observes:\n\nWhile lacking unanimous consensus in the early manuscripts of the Sermon on the Mount (which is not unusual), the absence of the phrase \u201cwithout a cause\u201d is evidenced by the following manuscripts: *p*64, *p*67, Sinaiticus (original hand), Vaticanus, some minuscules, the Latin Vulgate (Jerome mentions that it was not found in the oldest manuscripts known to him), the Ethiopic texts, the Gospel of the Nazarenes, Justin, Tertullian, Origen, and others.[3](#n3)\n\nThus, this passage may not have originally implied that anger is justifiable in some circumstances, as the phrase \u201cwithout a cause\u201d would suggest.\n\n![](/api/attachments/1960/download)\nEarly mauscript fragment of the Gospel of Matthew (Papyrus 104). Image via Wikimedia Commons.\n\n**A Misunderstood Idiom**\n\nIn his study on this topic, P. Wernberg-Moller argues that \u201cwithout a cause\u201d (*eike\u0304i*) was original to the Greek text, but that it reflects a misunderstanding of an Aramaic idiom, from which it was derived. As described by Wernberg-Moller, \u201cThe Greek translator, then, followed the Aramaic ground text word for word, without being aware, however, that by a slavish rendering of the Aramaic idiom as *eike\u0304i*, the original categorical saying was turned into a conditional one which made allowance for anger in some circumstances.\u201d[4](#n4)\n\n![](/api/attachments/1961/download)\nThe front side of Papyrus 37, a New Testament manuscript of the Gospel of Matthew. Image and caption info via Wikimedia Commons.\n\nThe omission of the phrase in many New Testament manuscripts can be accounted for by assuming that a later scribe \u201crecognized the Semitic idiom behind the saying in its Greek form, or because he felt that the Greek text with the reading *eike\u0304i* unsuitably weakened the categorical denunciation of anger originally intended by our Lord.\u201d[5](#n5)\n\n**Conclusion**\n\nThe above evidence supports the version of Christ\u2019s statements found in the Book of Mormon, which omits the phrase \u201cwithout a cause.\u201d Unlike many variations in New Testament manuscripts, this one isn\u2019t trivial.[6](#n6) As Welch concluded,\n\nIn my estimation, this textual variant in favor of the Sermon at the Temple is very meaningful. The removal of without a cause has important moral, behavioral, psychological, and religious ramifications, as it is the main place where a significant textual change from the KJV was in fact needed and delivered.[7](#n7)\n\nThis is now the predominate reading of Matthew 5:22, as rendered in most modern versions of the Bible.[8](#n8) It is unlikely, however, given Joseph Smith\u2019s limited educational opportunities, that he would have known anything about the relevant variants in New Testament manuscripts of the Sermon on the Mount.[9](#n9) Moreover, Wernberg-Moller\u2019s groundbreaking article explaining this issue was not published until 1956, more than 100 years after the Book of Mormon\u2019s publication.\n\n---\n\n##### FURTHER READING\n\nJohn W. Welch, [*Illuminating the Sermon at the Temple and the Sermon on the Mount*](https://archive.bookofmormoncentral.org/content/sermon-temple-and-greek-new-testament-manuscripts) (Provo, UT: Foundation for Ancient Research and Mormon Studies, 1999), 199\u2013210.\n\nDaniel K Judd and Allen W. Stoddard, \u201c[Adding and Taking Away \u2018Without a Cause\u2019 in Matthew 5:22](https://rsc.byu.edu/how-new-testament-came-be/adding-taking-away-without-cause-matthew-522)\u201d in *How the New Testament Came to Be: The Thirty-fifth Annual Sidney B. Sperry Symposium*, ed. Kent P. Jackson and Frank F. Judd Jr. (Provo and Salt Lake City, UT: BYU Religious Studies Center and Deseret Book, 2006), 157\u2013174.\n\n#####  RELEVANT SCRIPTURES\n\nBible\n\n[Matthew 5:22](https://abn.churchofjesuschrist.org/study/scriptures/nt/matt/5.22?lang=eng#p22)\n\nBook of Mormon\n\n[3 Nephi 12:22](https://abn.churchofjesuschrist.org/study/scriptures/bofm/3-ne/12.22?lang=eng#p22)\n\n#####\n\n---\n\n##### END NOTES\n\n[1](#p1) John W. Welch, [*Illuminating the Sermon at the Temple and the Sermon on the Mount*](https://archive.bookofmormoncentral.org/content/sermon-temple-and-greek-new-testament-manuscripts) (Provo, UT: Foundation for Ancient Research and Mormon Studies, 1999), 125\u2013210.\n\n[2](#p2) See Royal Skousen, [*Analysis of Textual Variants of the Book of Mormon: Part Five, Alma 56\u20133 Nephi 18*](https://bookofmormoncentral.org/content/analysis-of-textual-variants-of-the-book-of-mormon), 6 vols. (Provo, UT: FARMS and Brigham Young University, 2014), 5:3368\u20133369. After drawing attention to this change, Skousen further notes that \u201cin general, other textual differences between the Book of Mormon text and the King James version of the Sermon on the Mount are not supported by textual variants in the Greek New Testament text\u201d (p. 3369).\n\n[3](#p3) Welch, [*Illuminating the Sermon at the Temple and the Sermon on the Mount*](https://archive.bookofmormoncentral.org/content/sermon-temple-and-greek-new-testament-manuscripts), 200. For a much more comprehensive list, see Daniel K. Judd and Allen W. Stoddard, \u201c[Adding and Taking Away \u2018Without a Cause\u2019 in Matthew 5:22](https://rsc.byu.edu/how-new-testament-came-be/adding-taking-away-without-cause-matthew-522)\u201d in *How the New Testament Came to Be: The Thirty-fifth Annual Sidney B. Sperry Symposium*, ed. Kent P. Jackson and Frank F. Judd Jr. (Provo and Salt Lake City, UT: BYU Religious Studies Center and Deseret Book, 2006), 160\u2013165.\n\n[4](#p4) P. Wernberg-Moller, \u201cA Semitic Idiom in Matt. V.22,\u201d *New Testament Studies* 3, no. 1 (November 1956): 71\u201372.\n\n[5](#p5) Wernberg-Moller, \u201cA Semitic Idiom in Matt. V.22,\u201d 72.\n\n[6](#p6) As the prominent New Testament scholar, Bart Ehrman, stated, \u201cMost of the hundreds of thousands of variations are of very little importance for anything, as most people\u2014even specialists\u2014would admit. Only a minority really matter.\u201d See <https://ehrmanblog.org/fundamentalists-and-the-variants-in-our-manuscripts/>. Thus, we shouldn\u2019t necessarily expect Christ\u2019s statements in the Book of Mormon to adhere to every early manuscript variant. For the most part, the King James version can be assumed to substantively reflect the original meaning and intent of its authors. This is the very type of occasion\u2014when a variant changes the fundamental meaning of both a passage and a doctrine concerning human behavior\u2014that we might expect such an inspired change. For further discussion on this topic, see Bart D. Ehrman, *Lost Christianities: The Battles for Scripture and the Faiths We Never Knew* (New York, NY: Oxford University Press, 2003), 217\u2013227. See also, Carol F. Ellertson, \u201c[New Testament Manuscripts, Textual Families, and Variants](https://rsc.byu.edu/how-new-testament-came-be/new-testament-manuscripts-textual-families-variants)\u201d in *How the New Testament Came to Be: The Thirty-fifth Annual Sidney B. Sperry Symposium*, ed. Kent P. Jackson and Frank F. Judd Jr. (Provo, UT: Religious Studies Center, Brigham Young University; Salt Lake City: Deseret Book, 2006), 93\u2013108.\n\n[7](#p7) Welch, [*Illuminating the Sermon at the Temple and the Sermon on the Mount*](https://archive.bookofmormoncentral.org/content/sermon-temple-and-greek-new-testament-manuscripts), 201.\n\n[8](#p8) See <https://biblehub.com/matthew/5-22.htm>. See also, udd and Stoddard, \u201c[Adding and Taking Away \u2018Without a Cause\u2019 in Matthew 5:22](https://rsc.byu.edu/how-new-testament-came-be/adding-taking-away-without-cause-matthew-522),\u201d 157\u2013174.\n\n[9](#p9) See Evidence Central, \u201c[Book of Mormon Evidence: Joseph Smith\u2019s Limited Education](https://evidencecentral.org/social-media/public/evidence_form/__parms__/te/117/class/evidence),\u201d Evidence# 0001, September 19, 2020, online at evidencecentral.org.\n\n]

"""


def check_text_before_abstract(markdown_content: str) -> Any:
    # result check variable boolean
    result_check = []

    markdown_content = clean_data(markdown_content)

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
