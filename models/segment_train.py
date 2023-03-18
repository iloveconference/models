"""Functions to train segmentation models."""
from typing import Any


def get_paragraph_ngram_pairs(
    paragraph_segments: list[dict[str, Any]], ngram_size: int = 5
) -> list[dict[str, Any]]:
    """Generate ngram pairs from paragraph segments."""
    ngram_pairs = []
    for i_start in range(0, len(paragraph_segments)):
        for i_end in range(1, ngram_size):
            if (
                i_start + i_end > len(paragraph_segments)
                or paragraph_segments[i_start]["segment"]
                != paragraph_segments[i_start + i_end - 1]["segment"]
            ):
                continue
            i_text = "\n\n".join(
                paragraph_segment["text"]
                for paragraph_segment in paragraph_segments[i_start : i_start + i_end]
            )
            j_start = i_start + i_end
            for j_end in range(1, ngram_size):
                if (
                    j_start + j_end > len(paragraph_segments)
                    or paragraph_segments[j_start]["segment"]
                    != paragraph_segments[j_start + j_end - 1]["segment"]
                ):
                    continue
                j_text = "\n\n".join(
                    paragraph_segment["text"]
                    for paragraph_segment in paragraph_segments[
                        j_start : j_start + j_end
                    ]
                )
                ngram_pairs.append(
                    {
                        "ngrams_left": i_end,
                        "ngrams_right": j_end,
                        "text_left": i_text,
                        "text_right": j_text,
                        "label": 1
                        if paragraph_segments[i_start]["segment"]
                        == paragraph_segments[j_start]["segment"]
                        else 0,
                    }
                )
    return ngram_pairs
