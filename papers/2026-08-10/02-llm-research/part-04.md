# 🧠 大模型相关研究 | 2026年08月10日

> 本类共 **152** 篇论文：已确认 **79** 篇，待复核 **73** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-152**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-152**

---

### 151. [CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG](https://arxiv.org/abs/2608.07458)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Gyuwan Kim, Cheoneum Park, Tao Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent optimization studies on Retrieval-Augmented Generation (RAG) have exploited chunk-level KV cache reuse to avoid processing long retrieved contexts for higher efficiency, while significant information redundancy and noise still remain in the coarse-grained chunks. This paper optimizes the Pareto frontier under low prefill latency constraints while maximizing accuracy by proposing CoinRAG (Contextualized Information Nugget KV Cache Reuse for Long-Context RAG). The name metaphorically reflects our core mechanism: much like assembling small tokens (or "coins") to accumulate a larger value, CoinRAG compositionally reuses offline-computed, fine-grained nugget caches to form a learned contextual representation efficiently in a more semantically relevant but compact manner. Specifically, instead of full-chunk encoding, CoinRAG identifies query-relevant semantic units within retrieved chunks through two-stage retrieval and seamlessly assembles their sliced KV representations with a chunk-level context. Extensive evaluations on LongBench multi-hop question answering tasks demonstrate that CoinRAG significantly reduces operational costs and outperforms the other baselines with a new Pareto frontier and an average 5.3% relative improvement in answer quality (F1) under a standard fast prefill latency budget.

---


### 152. [MirrorWorld: Taming Video Diffusion Models for Mirror Reflection Generation](https://arxiv.org/abs/2608.07463)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Youjun Zhao, Alex Warren, Gary K.L. Tam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video diffusion models (VDMs) have enabled high-fidelity video synthesis. However, generating mirror reflections remains challenging because the content within a mirror must remain consistent with the surrounding scene. Existing VDMs are not specifically designed to model scene-to-mirror relationships, which can lead to reflections with incorrect content or inconsistent spatial arrangements. We observe that mirror reflection generation involves two complementary challenges: determining what scene content should be reflected and how the reflected content should be spatially arranged within the mirror region. Motivated by this observation, we propose MirrorWorld, a reflection-aware video inpainting framework that models scene-to-mirror relationships during generation. Specifically, we introduce Semantic Relation Distillation (SRD), which transfers relational information from a frozen visual foundation model to encourage semantic associations between visible scene content and mirror regions. We further propose Geometric Transformation Alignment (GTA), which learns a transformation that guides the spatial arrangement of reflected content. The two components play complementary roles, with SRD modeling what should be reflected and GTA modeling how it should be arranged. To facilitate research on this problem, we construct a benchmark for video mirror reflection generation by repurposing four existing video mirror datasets into a unified reflection reconstruction task. Experimental results show that MirrorWorld achieves improved reflection reconstruction quality over representative image-based reflection generation methods and strong video inpainting baselines.

---


> [!TIP]
> 当前位于：**151-152**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-152**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
