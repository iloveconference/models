"""Test cases for the review_load_dc_people"""
"""
This test checks for text after '=========='
if it exists it will fail so that the text will
be removed or pass if it has already been removed
"""
# flake8: noqa

import re
from typing import Any

from models.load_dc_people import clean_text


mark_text = """

In the fall of 1836, at age twenty-three Amos became a resident of Commerce, Illinois. He served the small community as a postmaster and a tavern keeper. Amos welcomed Latter-day Saints to Commerce in 1839 and offered employment to a few good men. “My husband had been in the employ of Amos Davis, a merchant in Nauvoo, for one year,” wrote Nancy Tracy. “At this time, my husband was one who was chosen to go and preach the Gospel. My husband went to Mr. Davis and got his wages, and besides, Mr. Davis made him a present of a nice suit of clothes, a hat, and fine boots and gave to me a dress pattern.”[1](#f1)

In April 1840 Amos entered baptismal waters. Two months after his baptism, he left Nauvoo to share the message of the Restoration with relatives in the east. On January 19, 1841 the Prophet Joseph Smith received a revelation directing Amos to “pay stock into the hands of those whom I have appointed to build a house for boarding, even the Nauvoo House”—

This let him do if he will have an interest: and let him hearken unto the counsel of my servant Joseph, and labor with his own hands that he may obtain the confidence of men.

And when he shall prove himself faithful in all things that shall be entrusted unto his care, yea, even a few things, he shall be made ruler over many;

Let him therefore abase himself that he may be exalted. Even so, Amen (D&C 124:111-14).

In 1842 misunderstandings between Amos Davis and the Prophet Joseph Smith became public. On March 10, 1842 the court case, “The City of Nauvoo versus Amos Davis” was held in Nauvoo. Amos was charged for—

>
> indecent and abusive language about [Joseph Smith] while at Mr. Davis’ the day previous. The charges were clearly substantiated by the testimony of Dr. Foster, Mr. and Mrs. Hibbard, and others. Mr. Davis was found guilty by the jury, and by the municipal court, bound over to keep the peace six months, under $100 bond.[2](#f2)
>
>
>

On November 30, 1842 Joseph had “Amos Davis brought before the municipal court for slander, but, in consequence of the informality of the writ drawn by Squire Daniel H. Wells, [he] was non-suited.”[3](#f3) Two days later, Joseph attended the trial of “Amos Davis, who was fined in the sum of $25 for breach of city ordinance for selling spirits by the small quantity.”[4](#f4) Joseph also attended the “Municipal Court on ‘habeas corpus, John M. Finch at suit of Amos Davis.’” The verdict was that Amos “pay costs, it being a vexatious and malicious suit.”[5](#f5)

In each of the court cases, Amos revealed his apostate sentiments. These sentiments were confirmed in a June 20, 1844 Robert D. Foster letter written in Carthage, Illinois: “Tell Amos Davis to keep his eyes open, as we learn that consecration law will soon commence on him. This we know, and he had better look out sharp.”[6](#f6)

Amos did not join the Latter-day Saint exodus from Nauvoo to the Territory of Iowa. In 1847 he sued Church trustees for debts owed him. In the late 1840s, Amos journeyed to the west. Nancy Tracy wrote, “In the early part of winter, my husband’s old employer, Amos Davis, came along through our settlement with a load of goods from his store in Nauvoo. He stopped with us for a day. When he left, he gave us some tea, sugar, and coffee, which was highly appreciated and was a luxury in those hard times.”[7](#f7)

By 1850 Amos was residing in Northern California. By 1853 he was living in Michigan. Five years later, he had returned to Illinois. Amos died on March 22, 1872 near Nauvoo at age fifty-eight.

[1](#t1). Nancy Tracy Autobiography, typescript, p. 27. L. Tom Perry Special Collections, Harold B. Lee Library, Brigham Young University, Provo, UT.

[2](#t2). Journal, December 1841–December 1842, p. 89. Joseph Smith Papers.

[3](#t3). Docket Entry, 30 November 1842 [*City of Nauvoo v. Davis for Slander of JS–B*], p. 10. Joseph Smith Papers.

[4](#t4). Smith, *History of the Church*, 5:198.

[5](#t5). Docket Entry, between circa 23 and circa 24 November 1843 [*State of Illinois v. Finch*], p. 89. Joseph Smith Papers.

[6](#t6). History, 1838–1856, volume F-1 [1 May 1844–8 August 1844], p. 130. Joseph Smith Papers.

[7](#t7). Nancy Tracy Autobiography, p. 35.

"""


def check_text(markdown_content: str) -> Any:
    # result check variable boolean
    result_check = []

    # Search for the position of "abstract" (case insensitive)
    text_match = re.search(r"\b[\d+](#t\d+).\b", markdown_content, re.IGNORECASE)

    if text_match:
        # Check content after the "text" text
        text_position = text_match.start()

        # Check if there is text after the "text" section
        if text_position > 0:
            result_check.append("True")
        else:
            result_check.append("False")

    return result_check


def test_review_load_dc_people() -> None:
    """It returns a valid Document for load dc people."""

    result = clean_text(mark_text)
    assert len(result) == 0
    assert "True" not in result
