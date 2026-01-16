import json
import pandas as pd
from typing import List, Dict
from working_code_1_generate_synthetci_profiles import generate_context_packets

# ✅ 1️⃣ Core function: generate context for a list of posts
def generate_dataset_with_context(posts: List[Dict]) -> List[Dict]:
    """
    Given a list of post objects, generate synthetic contextual packets
    (WHO, WHEN, WHERE, HOW) for each post.

    Returns a list of enriched post objects.
    Input Structure:
    posts = [
        {
            "post_id": "p001",
            "text": "Feeling frustrated about the quota situation... students deserve fairness. #protest",
            "image_captions": ["A crowd of people holding signs in a street"],
            "video_captions": [],
            "timestamp": "2025-12-20T18:10:00",
            "platform": "Facebook",
            "surface": "Group",
            "group_topic": "University Students"
        }
    ]
    Output Structure:
    {
        "post": {
            "post_id": "p001",
            "text": "...",
            "timestamp": "...",
            "platform": "Facebook",
            "surface": "Group",
            "group_topic": "University Students"
        },
        "context": {
            "who": {...},
            "when": {...},
            "where": {...},
            "how": {...}
        }
    }
    """
    enriched_posts = []

    for idx, post in enumerate(posts):
        user_id = post.get("user_id", f"user_{idx:05d}")

        context_packets = generate_context_packets(
            post=post,
            user_id=user_id
        )

        enriched_posts.append({
            "post": post,
            "context": context_packets
        })

    return enriched_posts



# ✅ 3️⃣ JSONL writer (recommended for ICWSM experiments)
def write_dataset_jsonl(posts: List[Dict], output_path: str):
    """
    Generate synthetic context for posts and write to JSONL.
    """
    with open(output_path, "w", encoding="utf-8") as f:
        for idx, post in enumerate(posts):
            user_id = post.get("user_id", f"user_{idx:05d}")

            context_packets = generate_context_packets(
                post=post,
                user_id=user_id
            )

            record = {
                "post": post,
                "context": context_packets
            }

            f.write(json.dumps(record) + "\n")

def generate_dataset_with_ground_truth(posts: List[Dict]) -> List[Dict]:
    enriched = []

    for idx, post in enumerate(posts):
        user_id = post.get("user_id", f"user_{idx:05d}")
        context = generate_context_packets(post, user_id)

        enriched.append({
            "post": post,
            "context": context,
            "ground_truth": {
                "persona": context["who"]["persona"],
                "dominant_topics": sorted(
                    context["who"]["post_history"],
                    key=context["who"]["post_history"].get,
                    reverse=True
                )[:3],
                "surface": context["where"]["surface"],
                "group_topic": context["where"]["group_topic"]
            }
        })

    return enriched


def main():
    # ✅ 3️⃣ JSONL writer (recommended for ICWSM experiments)

    
    # read posts from csv file 
    df = pd.read_csv(
        "/home/malam10/projects/agentic-contextual-understanding/posts.csv",
        encoding="utf-8",
        quotechar='"',
        skipinitialspace=True
    )

    print(df.head())

    # ✅ Step 4 (Recommended): Convert CSV → JSONL (ICWSM-ready)
    with open("posts.jsonl", "w", encoding="utf-8") as f:
        for _, row in df.iterrows():
            obj = row.to_dict()
            json.dump(obj, f, ensure_ascii=False)
            f.write("\n")


    enriched_posts = generate_dataset_with_ground_truth([row.to_dict() for _, row in df.iterrows()])
    with open("posts_with_context_ground_truth.json", "w", encoding="utf-8") as f:
        json.dump(enriched_posts, f, ensure_ascii=False, indent=2)
