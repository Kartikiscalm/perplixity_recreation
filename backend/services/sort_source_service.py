from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer


class SortSourceService:
    def __init__(self):
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

    def sort_sources(self, query:str, search_results: List[dict]):
        try:
            relevent_docs = []
            query_embedding = self.embedding_model.encode(query)

            for res in search_results:
                res_embeddings = self.embedding_model.encode(res['content'] or "")
                # np.linalg.norm cal the magnitude of the query_emd and the res_emd
                similarity = float(np.dot(query_embedding, res_embeddings)/(np.linalg.norm(query_embedding) * np.linalg.norm(res_embeddings)))

                res['relevence_score'] = similarity

                if similarity > 0.3:
                    relevent_docs.append(res)

            return sorted(relevent_docs, key= lambda x: x['relevence_score'], reverse = True)
        except Exception as e:
            print(e)