from pinecone import Pinecone
from app.core.config import PINECONE_KEY


class PineconeRepo:
    def __init__(self):
        if PINECONE_KEY:
            try:
                self.pc = Pinecone(api_key=PINECONE_KEY)
            except Exception as e:
                print(f"Error conectando a Pinecone: {e}")
                self.pc = None
        else:
            self.pc = None

    def get_episodic_memory(self, index_name="mep", limit=100):
        """Obtiene memoria episódica de Pinecone"""
        if not self.pc:
            return []

        try:
            index = self.pc.Index(index_name)

            # Consulta con vector dummy para obtener resultados
            dummy_vector = [0.0] * 768
            results = index.query(
                vector=dummy_vector,
                top_k=limit,
                include_metadata=True
            )

            memories = []
            for match in results.get('matches', []):
                memories.append({
                    'id': match.get('id'),
                    'score': match.get('score', 0),
                    'metadata': match.get('metadata', {}),
                    'text': match.get('metadata', {}).get('text', 'N/A')
                })

            return memories
        except Exception as e:
            print(f"Error obteniendo memoria episódica: {e}")
            return []

    def get_semantic_memory(self, index_name="mese", limit=100):
        """Obtiene memoria semántica de Pinecone"""
        if not self.pc:
            return []

        try:
            index = self.pc.Index(index_name)

            dummy_vector = [0.0] * 768
            results = index.query(
                vector=dummy_vector,
                top_k=limit,
                include_metadata=True
            )

            memories = []
            for match in results.get('matches', []):
                memories.append({
                    'id': match.get('id'),
                    'score': match.get('score', 0),
                    'metadata': match.get('metadata', {}),
                    'text': match.get('metadata', {}).get('text', 'N/A')
                })

            return memories
        except Exception as e:
            print(f"Error obteniendo memoria semántica: {e}")
            return []
