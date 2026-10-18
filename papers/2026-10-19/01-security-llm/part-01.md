# 🔐 大模型安全相关研究 | 2026年10月19日

> 本类共 **4** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems](https://arxiv.org/abs/2610.20776)

**<font color=#1a73e8>作者：</font>** Thuy Dung Nguyen, Jingyi Guo, Rana Seda Dubauskas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based agents increasingly execute long-horizon, end-to-end workflows involving shell commands, code modification, dependency installation, and interaction with remote services. This growing autonomy expands their exposure to indirect prompt injection (IPI), where adversarial instructions embedded in external content are interpreted as legitimate task directives. Existing evaluations, however, often focus on isolated malicious strings, single-step tool calls, or narrowly scoped agent configurations. We introduce INFUSE, an end-to-end benchmark for evaluating IPI throughout the lifecycle of long-horizon agent workflows. INFUSE comprises 40 realistic tasks and a structured taxonomy of 56 attack scenarios spanning five threat categories. Attacks are injected through realistic interaction surfaces encountered during task execution, extending evaluation beyond attacks placed only in initial prompts or isolated tool interactions. We evaluate 19 LLMs from the GPT, Claude, Gemini, Llama, Gemma, and Qwen families, producing 41,824 adversarial trajectories (26,220 without defenses) and 720 benign reference runs. Across the benchmark, mean attack success reaches 19.6% under LLM-based evaluation and 15.4% under heuristic verification, with per-model ASR-L ranging from 3.2% to 41.9%. Existing guard models provide limited protection, while prompt-level instructional hardening reduces mean attack success from 58.2% to 14.3%, revealing substantial but model-dependent security-utility trade-offs. Our code is available at this https URL.

---


### 2. [Poisoning the Neighborhood: A Topology-Aware Topic-Level Attack on Large-Scale HNSW-based RAG Systems](https://arxiv.org/abs/2610.21464)

**<font color=#1a73e8>作者：</font>** Yufei Chen, Yao Wang, Haibin Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) mitigates hallucinations and knowledge staleness in large language models using external knowledge. However, ingestion from public and third-party sources exposes RAG systems to poisoning attacks. Existing attacks are designed and evaluated under exact retrieval, where poisoned documents participate in global ranking. Deployment-scale systems instead rely on approximate nearest-neighbor (ANN) indexes such as hierarchical navigable small world (HNSW), where limited search budgets, graph-search reachability, and local benign-document competition invalidate this assumption and degrade existing attacks. We present a topology-aware topic-level poisoning attack against large-scale HNSW-RAG that generalizes to unseen topic queries. We organize poisoned documents into a Hub-Satellite structure: Satellites provide competitive entry points across semantic regions, while Hubs strengthen local cohesion and facilitate cascading retrieval. For generation, we propose an entity-claim promotion attack combining evidence anchoring and entity-claim coupling to promote the target entity via a target claim across different query regions. On 2M-document Wikipedia, our attack maintains over 72% retrieval success and reaches 31.29% attack success, substantially outperforming baselines; domain-specific experiments further support its effectiveness. Structural analyses show that the Hub-Satellite topology forms in HNSW, indicating that graph structure contributes to improved poisoned-document retrieval. Existing poisoning defenses cannot mitigate the attack, exposing graph-structural risks in HNSW-RAG systems.

---


### 3. [In the Guise of Correction: How Framing and Cultural Adaptation Erode LLM Safety on Real-World Criminal Cases](https://arxiv.org/abs/2610.21789)

**<font color=#1a73e8>作者：</font>** Mohsinul Kabir, Md. Tariquzzaman, Karam S. R. Elradie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing safety benchmarks rely largely on synthetic prompts with loosely grounded taxonomies and offer little focused analysis of severe crime categories. We introduce GUISE, a benchmark of criminal-assistance scenarios sourced from real-world cases and organised under a taxonomy from the UNODC International Classification of Crime for Statistical Purposes (ICCS). Each scenario is rendered under three linguistic framings and evaluated across five distinct cultures. Using our proposed two-tier evaluation framework, which judges both harmfulness and operational uplift, we find that: (i) framing alone drives unsafe compliance, with the mean unsafe compliance rate rising from 28.9% under direct requests to 66.4% under correction seeking (peaking at 97.3%; p < 0.05), as models correcting deliberately distorted details supply executable criminal steps; (ii) culturally adapted prompts elicit significantly more unsafe compliance than literal translations of the same requests in all four non-English languages (+7 to +18 points), a risk that translation-based benchmarks miss; and (iii) unsafe responses from the least-safe models carry strong Anglocentric registers, and the extent of this leakage increases monotonically with response harmfulness ($\rho$ = 0.46 to 0.63 across languages, all p < 0.001). GUISE offers a grounded resource and fine-grained diagnostics for strengthening refusal alignment across languages and cultures. We publish our code and data to facilitate future research.

---


### 4. [Behavioral Forgetting Is Not Privacy in Machine Unlearning](https://arxiv.org/abs/2610.21799)

**<font color=#1a73e8>作者：</font>** Tyler Lizzo, Larry Heck  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove targeted information from large language models, but existing evaluations often measure forgetting only on a designated benchmark distribution. We argue that such behavioral forgetting is an insufficient standard for privacy-oriented unlearning, and that evaluation should instead test whether forgetting persists across the access paths through which the same information may be recovered. We demonstrate this with a controlled case study of cross-lingual querying: across multiple multilingual model families, forgetting varies substantially when semantically equivalent information is queried in different languages and scripts. A single access path is therefore enough to expose a real gap between behavioral forgetting and information inaccessibility, motivating broader evaluation of access-path generalization and adversarial recoverability alongside in-distribution forgetting.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
