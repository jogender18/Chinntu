//! MemoryBackend trait for all storage backends.

use chinntu_core::{ChinntuError, RetrievalResult};
use serde_json::Value;

pub trait MemoryBackend: Send + Sync {
    fn backend_id(&self) -> &str;
    fn store(
        &self,
        content: &str,
        source: &str,
        metadata: Option<&Value>,
    ) -> Result<String, ChinntuError>;
    fn retrieve(
        &self,
        query: &str,
        top_k: usize,
    ) -> Result<Vec<RetrievalResult>, ChinntuError>;
    fn delete(&self, doc_id: &str) -> Result<bool, ChinntuError>;
    fn clear(&self) -> Result<(), ChinntuError>;
    fn count(&self) -> Result<usize, ChinntuError>;
}
