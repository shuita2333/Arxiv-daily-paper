# 🧠 大模型相关研究 | 2026年09月11日

> 本类共 **148** 篇论文：已确认 **136** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-148](./part-03.md)

---

### 51. [Scaling E-Commerce Attribute Extraction with Parallel Decoding](https://arxiv.org/abs/2609.09716)

**<font color=#1a73e8>作者：</font>** Nikhita Vedula, Dushyanta Dhyani, Bryan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Customers rely on specific product attributes to compare products and make purchasing decisions, but e-commerce catalogs are messy and unstructured, making it difficult to identify which attributes matter most and extract them at scale. Standard Attribute Value Extraction (AVE) systems treat all attributes equally, producing large, inconsistent attribute sets that do not reflect the factors consumers use to differentiate products. We introduce a two-stage LLM pipeline that first discovers a compact, ranked schema of purchase-discriminative attributes for each product category, then extracts their values from catalog text using a fine-tuned compact LLM (Qwen3-4B) with Hyper-Parallel Decoding (HPD). This pipeline achieves 85% extraction accuracy, on par with the foundational LLM it was distilled from, while reducing inference costs by 92% over foundational LLMs, enabling production-scale use for product discovery and catalog enrichment. The resulting category-level structured representations effectively constitute automatically constructed product knowledge bases, providing consistent, comparable attributes across varied product categories that can ground downstream knowledge-intensive applications.

---


### 52. [StreamAlign: Streaming Text-Aligned Speech Tokenization](https://arxiv.org/abs/2609.09719)

**<font color=#1a73e8>作者：</font>** Kang-wook Kim, Jinyoung Park, Jinsoo Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-aligned speech tokenization methods have emerged to better align speech tokens with LLM token spaces, enabling more effective utilization of pretrained LLMs. However, they rely on offline automatic speech recognition (ASR), leading to two key limitations: (i) the need for complete utterances before tokenization, precluding real-time streaming, and (ii) vocabulary mismatch between ASR and LLMs, which reduces acoustic granularity from the subword to the word level. We introduce StreamAlign, a text-aligned speech tokenization framework that enables streaming tokenization for real-time speech-text joint modeling. StreamAlign performs online speech-text alignment by combining character-level RNN-Transducer alignment with word-level ASR guidance, mitigating ASR-LLM vocabulary mismatch while preserving recognition accuracy. A proactive word boundary classifier anticipates word completion at chunk boundaries, reducing tokenization latency from 560 ms to 270 ms. On LibriSpeech, StreamAlign achieves the lowest WER and highest UTMOS among evaluated tokenizers. Furthermore, StreamAlign-SLM, a spoken language model trained on StreamAlign units, outperforms other end-to-end spoken language models in speech continuation while achieving the strongest overall consistency on SALMon and spoken StoryCloze.

---


### 53. [EFQ-Softmax: Exp-Free Quantization for Softmax](https://arxiv.org/abs/2609.09721)

**<font color=#1a73e8>作者：</font>** Haohui Han, Yuming Wan, Hongni Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-bit attention accelerates Transformer inference by moving the $QK^\top$ and $PV$ matrix multiplications to FP8 or FP4 matrix engines. However, the softmax path often evaluates shifted-score exponentials in higher precision, forms a temporary probability block, and quantizes it before low-bit $PV$ multiplication. This exp-then-quantize path creates a mismatch between a high-precision probability producer and a low-bit matrix consumer. We propose EFQ-Softmax (Exp-Free Quantization for Softmax), a low-bit probability-generation method that directly maps shifted attention scores to block-scaled E2M1 operands. For each microscaling block, EFQ-Softmax selects an exponent-only scale from the local maximum, maps the shifted scores to a normalized residual domain, and generates nonnegative E2M1 probability codes using a single affine rule. The resulting operand is used consistently in both the $\widetilde{P}V$ numerator update and the $\widetilde{P}\mathbf{1}$ denominator update. The FlashAttention-style row-maximum update, historical rescaling, high-precision accumulation, and final normalization remain unchanged. We evaluate end-to-end quality on Qwen3-8B, Qwen3-VL-8B-Instruct, and WAN2.2-TI2V-5B, and separately measure kernel-level performance on the A5 vector unit. EFQ-Softmax improves the Qwen3-8B seven-task mean from 0.6749 with MXFP4 to 0.6773 and the Qwen3-VL nine-task mean from 0.7826 to 0.8000. On WAN2.2, it maintains temporal consistency and visual quality comparable to the FP16 and MXFP4 baselines under VBench. On the A5 vector unit, EFQ-Softmax reduces the vector-stage latency of the fused probability-generation kernel by 40.33% on average across sequence lengths from 16K to 128K. These results show that direct low-bit probability generation can replace the conventional exp-then-quantize path while preserving end-to-end model quality.

---


### 54. [LexAgentHallu: A Hierarchical Benchmark for Profiling Hallucinations in Legal Agents](https://arxiv.org/abs/2609.09754)

**<font color=#1a73e8>作者：</font>** Yujin Zhou, Mingxuan Zheng, Chuxue Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models are increasingly deployed as tool-augmented legal agents, they introduce agentic hallucinations where tool-call and reasoning errors cascade into fabricated holdings and miscited authority. However, existing legal benchmarks evaluate only single-turn QA with outcome-level metrics, while agentic hallucination benchmarks lack legal-specific diagnostic capability. Neither answers to what extent and how a legal agent hallucinates along its trajectory. To address these limitations, we introduce LexAgentHallu, a legal agentic hallucination benchmark designed to evaluate to what extent and how legal agents fail along multi-step trajectories. Built through a four-stage expert-in-the-loop pipeline, LexAgentHallu contains 3414 instances across 17 legal categories and 6 task types. Each instance is annotated under a dual-layer hallucination taxonomy of 7 high-level categories and 27 fine-grained subclasses, covering both substantive errors and agent-procedural failures. We further design fine-grained metrics that quantify to what extent and localize how each failure occurs along an agent's execution path. Our evaluation across 18 proprietary and open-source agents uncovers a Right-Answer-Wrong-Reason effect and reveals that hallucination subclasses cluster rather than scatter, forming distinct agentic framework, legal task, and category profiles. These findings, invisible to outcome-level evaluation, validate the diagnostic power of LexAgentHallu for evaluating agentic hallucination in law.

---


### 55. [SocialRL: Refining LLMs' Social Intelligence through Multi-turn Reinforcement Learning and Reward Design](https://arxiv.org/abs/2609.09764)

**<font color=#1a73e8>作者：</font>** Jianing Wang, Xintao Wang, Aili Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social intelligence enables agents to read social context, infer intent, and adapt over sustained dialogue. As language models become autonomous collaborators, it is central to building effective and trustworthy human-AI interaction. Existing reinforcement learning methods optimize single-turn utterances and sparse outcome rewards, producing short-sighted policies that struggle to manage goal-relationship tensions across multi-turn interactions. We propose SocialRL, a multi-turn reinforcement learning framework addressing both challenges. First, we apply multi-turn reinforcement learning using PPO that propagates delayed outcome rewards back to each turn, enabling long-horizon planning. Second, we design six process reward dimensions capturing the goal-relationship trade-off, including goal advancement, relational attunement, contextual coherence, etc. A reward model dynamically generates fine-grained scoring criteria for each dimension, while a stage-aware weight schedule prioritizes relationship-building in early turns, goal advancement mid-way, and balanced closure late. Across multiple social-dialogue benchmarks, SocialRL improves Goal Achievement by an average of 9.2 percentage points over the corresponding Base models. These results demonstrate the effectiveness of SocialRL across synthetic and real social scenes, as well as standard and challenging social scenarios.

---


### 56. [CARRE: Counterfactual Action Retrieval and Reason Evaluation for Explainable Churn Prescription](https://arxiv.org/abs/2609.09766)

**<font color=#1a73e8>作者：</font>** MinJoo Kim, SanJin Park, SeungHwan Cho  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Churn models typically identify high-risk customers but do not specify which feasible retention action should be considered or why that action is appropriate. We present CARRE (Counterfactual Action Retrieval and Reason Evaluation), a three-stage framework that combines retrieval-augmented candidate generation, cost-aware counterfactual scoring, and large language model (LLM) reasoning. CARRE retrieves a predefined catalog of retention actions, estimates model-predicted churn-risk changes under explicit feature transformations, and generates a structured churn reason and a profile-grounded explanation for the selected action. On the IBM Telco Customer Churn dataset, CARRE achieves 79.8% greater mean model-predicted risk reduction than the plain SHAP baseline and 80.4% greater reduction than the cost-controlled SHAP+Cost baseline across 313 high-risk test cases; its cost-normalized efficiency is 10.5% higher than that of plain SHAP. On a 136-case reason-stratified evaluation sample, diagnosis-driven prompt refinement increases weak-label agreement from 79.4% to 90.4%, with no auxiliary-plan constraint violations; because the same sample was used for error diagnosis and re-evaluation, the post-refinement result is not an independent estimate of generalization. For 135 explanations generated using the pre-refinement v2 reason outputs, two cross-vendor LLM judges assign mean scores ranging from 4.02 to 5.00 out of 5, although one judge saturates on actionability, and a deterministic audit finds no contradictions among 66 verifiable profile claims. Retrieval ablations show that k=5 provides the best evaluated compromise between high candidate coverage and downstream reasoning agreement in this dataset. These results illustrate how retrieval, model-based counterfactual scoring, and language generation can be separated and jointly evaluated in a prototype churn-prescription pipeline.

---


### 57. [Fine-Tuning a KV Cache Concatenation-Aware Model or Recomputing KV Caches? Why Not Both?](https://arxiv.org/abs/2609.09768)

**<font color=#1a73e8>作者：</font>** Fumihiko Tachibana, Daisuke Miyashita, Jun Deguchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In Retrieval-Augmented Generation (RAG) systems, a large number of retrieved chunks are concatenated to form the input context so that users can receive high-quality responses based on external knowledge. As a result, the input context length increases substantially, leading to a larger prefill workload and, in turn, a longer time to first token (TTFT). While previous works that reuse precomputed key-value (KV) caches effectively reduce TTFT for long-context inputs, it remains unclear whether response quality is preserved when the input context becomes very long. In this paper, we propose a combined approach that (i) fine-tunes the model while taking KV cache concatenation into account and (ii) selectively recomputes a subset of the KV caches. By applying both techniques, we demonstrate improved accuracy for long-context inputs. Experiments on the RULER benchmark show that, for a 124k-token input, our method improves the RULER score by 9.7 point over the baseline that recomputes KV caches only. Moreover, TTFT is reduced by 80% compared with full attention.

---


### 58. [Procedural Memory Under Change: Reuse and Interference in Controlled Web Tasks](https://arxiv.org/abs/2609.09774)

**<font color=#1a73e8>作者：</font>** Yanze Cao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Procedural memory lets language agents reuse successful routines, but reuse presumes that a stored routine remains applicable. We study what happens when that presumption is deliberately violated. The study combines a retrospective, human-assisted interface-adaptation case from BrowserGym TimeWarp with controlled frozen-memory comparisons on synthetic shopping decisions. During the documented WebShop V1-V6 development path, interface-specific code was adapted while the separately stored high-level procedure was not reported to change; this phase does not constitute an autonomous memory-agent evaluation. In the controlled phase, an early pilot produced one task on which two memory conditions selected a more expensive item while the no-memory condition selected the reference minimum. Follow-up probes did not establish a recurring row-order or identity-binding pattern. We then tested four forms of mismatch: changed quantities, a different evidence representation, a conflict between local and global optimization, and distributed promotion evidence, across 32 formal cells. Each cell used one temperature-0 generation with the same local qwen3:8b configuration and no adaptive retry. Across these pairs, none of the predefined diagnostic interference signatures appeared on the tasks for which they were defined when current-task evidence was explicit and sufficient. The result identifies a tested region of non-interference: a procedural memory can be mismatched without becoming behaviorally disruptive. It does not establish general safety or a mechanism. The remaining question is which additional conditions turn applicability mismatch into observable, memory-caused error.

---


### 59. [Proof-Carrying Cognition: Closing the Verification Gap with Reality-Settled Reward](https://arxiv.org/abs/2609.09776)

**<font color=#1a73e8>作者：</font>** Eshwar Reddy M, Sourav Karmakar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier gains in language-model reasoning come from reinforcement learning on reasoning traces and are concentrated in domains with a cheap, sound verifier. We argue the field's binding constraint is the verification gap: no scalable, incorruptible reward for reasoning outside formal domains. We make four contributions. (1) Theory: in a joint-Gaussian model of best-of-N selection, verifier-gold correlation rho is the exact exchange rate between test-time compute and capability, and an unsound verifier pays a polynomial penalty N^(1/rho^2); a margin-free copula form predicts realized soundness of real LLM judges to 4% median error. (2) Demonstration: in program-synthesis testbeds with executable ground truth, including a pre-registered scaled replication, unsound verifiers lose Soundness-under-Pressure as optimization grows (0.94 to 0.32 at N=4096) while a sound verifier improves monotonically; reality-anchored settlement beats a frozen verifier under i.i.d. and adversarial pressure, driving the hacking gap from ~0.27 to ~0; soundness scales log-linearly with settled labels, with on-policy settlement ~10x more label-efficient than random labeling. With real LLM judges and unit-test execution as gold, a weak judge loses soundness under best-of-N (p<0.001), a stronger judge is more robust, and selection alone manufactures +0.53 hacking gaps from honest samples. Under real GRPO training, a frozen reward model traces the full overoptimization curve (executed reward collapses 90%) while the same model refit on a 10% settlement stream preserves 6x the executed reward. (3) Paradigm: proof-carrying cognition, where reasoning steps are typed probabilistic claims priced by a self-built world model trained only on held-out reality and settled by proper scoring rules. (4) Benchmark: we specify Soundness-under-Pressure as the headline metric for a reality-settled reasoning benchmark.

---


### 60. [ROAM: Robust Organization of Atomic Memories for Agents through Semantic Relations](https://arxiv.org/abs/2609.09778)

**<font color=#1a73e8>作者：</font>** Jianjie Zheng, Peng Lai, Sijie Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term language-model agents rely on external memory across interactions. Atomic memories are particularly useful: their fine-grained semantic boundaries enable precise retrieval and direct comparison between observations. Yet accumulating atoms inevitably become redundant, overlapping, or conflicting. Existing methods often ask an LLM manager to add, update, delete, or rewrite memories directly, coupling semantic interpretation, storage decisions, and content generation in one error-prone operation. We introduce ROAM, a relation-guided framework that uses atomicity for management while allowing richer answer-time representations. ROAM classifies incoming--stored atom pairs as independent, equivalent, directionally subsuming, or conflicting, then organizes observations into active Primary and supporting Evidence roles. Fusion subsequently combines complementary details and temporal changes into compact, potentially non-atomic views. Only Primary views are retrieved for answering, preventing redundant or outdated atoms from competing independently. Across models and evaluation settings, ROAM improves answer accuracy by up to 29.8 percentage points. Ablations show complementary benefits from different relations and consistent gains from fusion beyond role organization. Mechanism analysis further finds 15.6-point higher answer-critical source recall and an 11.5-point lower confounder-token share. ROAM remains robust across manager scales.

---


### 61. [BRACE: Anchored Bellman-Residual Correction for Stale Critics in Asynchronous RL](https://arxiv.org/abs/2609.09783)

**<font color=#1a73e8>作者：</font>** Guanqun Zhao, Zijun Xie, Binbin Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Asynchronous reinforcement learning has become the standard way to scale training for language models, but the resulting policy lag biases the critic toward the stale behavior policy. Existing work on asynchronous LLM training corrects the actor and leaves this bias unaddressed, while the off-policy value correction of classical RL does not carry over to long-horizon agentic tasks, since a short correction horizon leaves the regression target free of the reward and a long one lets the product of importance ratios drift exponentially with the trajectory length. We propose BRACE, an anchored Bellman-residual correction for stale value models. BRACE bounds the correction horizon to a prefix of policy tokens and anchors a constant-weight Monte-Carlo tail beyond it, which separates policy correction from reward propagation. BRACE improves mean@1 on BrowseComp-Plus by $2.4\%$ over the strongest baseline, runs $2.46\times$ faster per step than synchronous training, and remains stable $50$ updates off-policy.

---


### 62. [LogiScope-VQA: Benchmarking Vision-Language Models for Logistics Hazard Identification in Industrial Scenarios](https://arxiv.org/abs/2609.09790)

**<font color=#1a73e8>作者：</font>** Hanjing Zhou, Mingze Yin, Ying Lian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Multimodal Models (LMMs) large-scale deployment in industrial warehouse settings specifically necessitates that models exhibit human-expert-level hazard-oriented perception, understanding, and reasoning capabilities. However, the scarcity of real industrial data, tightly coupled to commercial terms, significantly hampers further advancement. To bridge this gap, we curate LogiScope-VQA to investigate the practical applicability of mainstream LMMs in real-world logistics operations. LogiScope-VQA comprises 2,476 images and 2,918 videos primarily sourced from real-world logistics parks, along with 10,274 VQAs meticulously curated and validated by human annotators. Grounded in 18 core objects and 20 risk types, we devise 39 subtasks aligned with three principal themes: industrial element perception, warehouse knowledge understanding, and potential risk reasoning. Furthermore, we incorporate dynamic thinking-budget configurations and dual-dimensional risk bias analyses to elucidate the properties of LMMs. Extensive experiments unveil that even powerful proprietary models, including GPT-5.5, Gemini-3.1-Pro, and Claude-Opus-4.7, exhibit a significant gap relative to human performance. The unique challenge of jointly integrating perception, understanding, and reasoning for hazard identification poses substantial headroom for further improvement on LogiScope-VQA. We additionally reveal the pervasive security bias issue that impedes LLMs' practical deployment in real-world settings. The industrial dataset is publicly available under the CC BY-NC-SA 4.0 license.

---


### 63. [MUCnoHARM@GermEval Shared Task 2026: Retrieval-based In-Context Learning for Defamatory Offences, and Where It Falls Short](https://arxiv.org/abs/2609.09791)

**<font color=#1a73e8>作者：</font>** Kristin Gnadt, Maximilian Meidinger, Matthias Aßenmacher  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With hate speech being ubiquitous online, automatic detection is crucial, in particular when it comes to criminally relevant social media posts. We study a variety of retrieval-based in-context learning (RetICL) strategies for detecting defamatory offences under §§ 185-187 StGB (the subject of GermEval 2026 Subtask 4). Few-shot prompting beats zero-shot, but retrieval-based approaches offer only marginal gains over random demonstrations, and even fall behind an optimised static set of demonstrations. Providing concrete legal knowledge helps, yet model choice outweighs every other system choice. Models over-predict criminal relevance while still missing 26-57% of criminally relevant posts, suiting them for triage rather than autonomous moderation.

---


### 64. [Privacy-Preserving Split Learning for Federated LLM Fine-Tuning](https://arxiv.org/abs/2609.09794)

**<font color=#1a73e8>作者：</font>** Heng Jin, Chaoyu Zhang, Hexuan Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models (LLMs) on domain-specific data is essential for downstream adaptation. In many deployments, a participant cannot hold the complete model locally. This happens because the model owner keeps the full model proprietary, or because the participant lacks sufficient compute resources. Split Learning (SL) addresses this by partitioning the model between the participant and a server so that only a small portion runs locally. When the underlying data is additionally distributed across multiple institutions with privacy requirements, Federated Learning (FL) further enables collaborative training across participants by sharing only model updates instead of raw data. In this combined setting, each client transmits intermediate activations to the server, and for LLM fine-tuning, this exchange poses an inherent privacy paradox. The autoregressive nature of LLMs causes the transmitted activations to leak the input, and existing perturbation-based defenses are fundamentally ineffective in this setting. We address this leakage through a learned obfuscate-and-recover scheme that protects participants' private datasets while still allowing an independently deployable model to be trained on the server side. Experiments demonstrate that our approach achieves strong privacy protection with modest utility loss and system overhead, making split-based federated LLM fine-tuning practically viable.

---


### 65. [UnitBoost: Managing Compound LLM Systems with a Merge Operator, Not a Model](https://arxiv.org/abs/2609.09815)

**<font color=#1a73e8>作者：</font>** Xing Zhang, Guanghui Wang, Yanwei Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Compound LLM systems often solve a coordination problem by adding a higher-level LLM. The resulting meta-agent reads workers' outputs, writes the final answer, allocates later calls, and decides when to stop. It is expressive, but it also concentrates three control decisions in an opaque, order-sensitive model call. We ask whether the manager needs to be generative at all. UnitBoost replaces that model with a defined meta-level operator: a task-given unit map turns worker outputs into slot-value proposals, a constrained argmax assembles the output, and the slots left unfilled or unsupported become an explicit residual for the next round. The operator is order-free, records unit provenance, and gives a simple guarantee: without coupling constraints, unit-wise maximization under the same admission score dominates selection of any complete candidate. On three held-out benchmarks, it exceeds the best single candidate chosen with gold labels by 0.060-0.195 absolute task-score points and input-matched generative managers by 0.048-0.076. Replacing only the management step improves six compound-system configurations by 0.013-0.182. Residual-directed rounds raise FanOutQA cell F1 from 0.4778 to 0.5524; matched controls show that the true residual outperforms random targets and ordinary rereading, while a label-free supply signal flags exhaustion after one unproductive round. The same analysis measures three conditions in which no such gain is available (one indivisible unit, unavailable unit identity, and an endpoint that charges for every emitted unit) and quantifies cross-unit coupling as a repair cost. The manager gives up semantic freedom and gains order invariance, unit provenance, and testable failure conditions.

---


### 66. [HyperTrace: Hypothesis-Based Preference Tracing for Online LLM Personalization](https://arxiv.org/abs/2609.09835)

**<font color=#1a73e8>作者：</font>** Jianzhi Shen, Keyu Mao, Minghao Shao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalized language models aim to adapt responses to individual users, whose preferences are often latent and revealed gradually through interaction. Existing training-free methods rely on stored histories or retrieved memories, but they often struggle to reconcile long- term preferences with short-term topic-specific needs. To address this issue, we propose HyperTrace, a training-free framework that formulates online personalization as latent preference tracing. HyperTrace maintains interpretable natural-language hypotheses over short-term intent and long-term preferences, and updates them through an SMC-style reweight process using an LLM-based surrogate choice model. By updating these hypotheses across turns and sessions, HyperTrace enables personalization without parameter updates. Experiments on PRISM and PersonaMem-v2 show that HyperTrace improves response alignment, preference prediction, and profile consistency over strong online baselines, demonstrating the effectiveness of tracing latent user preferences for robust personalization. Code and scripts are available in the repository: this https URL.

---


### 67. [$S^3$-Bench: Evaluating Speech Interaction Models as Scientific Voice Assistants](https://arxiv.org/abs/2609.09852)

**<font color=#1a73e8>作者：</font>** Heyang Liu, Jiayi Huang, Wenyang Xiao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The advance of multimodal large language models (MLLMs) has fundamentally reshaped the paradigm of human-computer interaction, especially speech interaction models capable of seamless conversations. Despite remarkable performance as general voice assistants, their performance in specialized domains remains underexplored, particularly in scientific areas. Scientific interactions introduce formidable challenges, involving rare technical terminology, spoken norms of abbreviations, and the natural verbalization of symbolic special expressions. In this paper, we introduce S$^3$-Bench, a systematic evaluation framework covering 10 major disciplines, consisting of a Knowledge set for speech question-answering and a Dialogue set for multi-turn progressive interactions with simulated user agents. By decomposing a complete atomic turn into stages of speech recognition, perception, knowledge utilization with reasoning, and response pronunciation, we systematically characterize the common challenges and performance tradeoffs of existing approaches. Furthermore, experiments on multi-turn interactions reveal persistent limitations in user adaptation and the generation of accurate, comprehensive, and efficient responses.

---


### 68. [The Era by Eon Benchmark: A Generated Enterprise Estate with Exact Ground Truth for Benchmarking LLM Agents](https://arxiv.org/abs/2609.09853)

**<font color=#1a73e8>作者：</font>** Benjamin Gruenbaum, Doron Porat, Assaf Natanzon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents for enterprise systems of record cannot be evaluated on customer production data, and no existing substitute provides ground truth. We present the Era by Eon Benchmark for evaluating LLM agents that use enterprise tools. The benchmark is built around a complete fictional company. It includes product simulators, company-specific internal databases, benchmark questions, and computed answer keys. Industry, company size, business model, application portfolio, and a seed define each company. One seeded entity graph supplies shared company data to simulators of Salesforce, Zendesk, Slack, Gong, and other products. A questionconditioned generator creates the schemas and records for internal databases. It takes shared entities, keys, and values from the same graph before generating database-specific facts. Both mechanisms therefore describe one consistent enterprise estate. Every expected answer is computed from the final records, so grading is exact. Design and answer-key checks validate the internal databases. A realism scorecard and adversarial detector validate the entity graph. Across 23 generated companies, the mean realism score rose from 61.8 to 97.0, with zero records flagged as synthetic. In the reported simulator-track comparison, nine models answered the same 33 questions three times each. Accuracy estimates ranged from 42.4% to 76.8%, and three of 36 pairwise differences remained supported after correction.

---


### 69. [Exact Degeneracy Under Balanced k-Shot Sampling:Consequences for Small-Sample Discriminant Analysis on LLM Embeddings](https://arxiv.org/abs/2609.09860)

**<font color=#1a73e8>作者：</font>** Lingxiao Qu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Balanced k-shot sampling draws exactly k labeled examples per class. We show that it induces an exact, provable degeneracy in a family of small-sample discriminant estimators. Under balanced sampling, the within-class scatter operator of Kernelized Linear Principal Component Discriminant Analysis (KLPCDA) is not merely rank-deficient but exactly a scaled orthogonal projector. We derive the consequences in closed form: two of KLPCDA's seven variants have every signal eigenvalue exactly equal, so their eigenvector selection criterion is provably indifferent rather than ill-conditioned, and a third has a provably void objective. This follows from the estimators' construction, not any dataset; we confirm it on frozen sentence embeddings and, separately, on residual-stream activations from a decoder-only generative model. An in-formula tie-break repairs the two repairable variants, with recovery gated by class count: the residual subspace constraint costs 5x more on few-class than many-class datasets (p=0.000001).
We then evaluate the repaired framework on few-shot text classification on frozen LLM embeddings (n much smaller than d, up to 4096), across four datasets, three embedding sizes, and three trained baselines (SetFit, LoRA, in-context learning). A properly cross-validated logistic-regression probe still beats every KLPCDA variant on three of four datasets, at every embedding size; guidance carried from pixel, vibration-signal, and gene-expression data does not directly generalize to this feature space. Three independent geometric separability metrics fail to explain why one high-dimensional decoder-based embedding model underperforms smaller bidirectional encoders, ruling out anisotropy; the gap is substantially an estimation-efficiency effect, not a permanent ceiling, closing by more than 80% when the support set grows from k<=10 to k=30-50 (p=0.00195, both many-class datasets).

---


### 70. [AgentAudit: An Open, Extensible Framework for Full-Lifecycle Trust Evaluation of AI Agents](https://arxiv.org/abs/2609.09875)

**<font color=#1a73e8>作者：</font>** Shrey Nag, Sachita, Abhishek Kumar Singh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing evaluation frameworks mostly assess only one part of AI agents, such as task completion (AgentBench) or security robustness (AgentDojo, ASB), rather than the complete pipeline of planning, tool selection, tool execution, memory and reasoning. Failures can occur at any stage, yet existing benchmarks rarely identify their precise source. AgentAudit evaluates the entire execution trace across ten capability, grounding, security and behavioural dimensions, namely instruction integrity, planner, memory, tool selection, tool invocation, tool correctness, alignment, tool faithfulness, security and execution integrity, combined with behavioural classification and failure attribution to pinpoint the exact stage responsible for an observed failure. AgentAudit can evaluate any LLM-based AI agent, since it attaches to the agent instead of replacing it. It reads only the recorded execution trace and does not interfere with how the agent runs, so it places no constraint on the agent's internal implementation. We evaluate five language models (OpenAI GPT-5, Claude Sonnet 5, Sarvam 105B, Llama 3.3 70B and Gemini 2.5 Flash) across nine capability and adversarial tasks. Claude Sonnet 5 and GPT-5 obtain the highest mean Composite Trust Scores (95.1 and 80.6 out of 100, respectively), while Sarvam 105B, Llama 3.3 70B and Gemini 2.5 Flash trail substantially (57.6, 45.7 and 22.6). All traces were scored by a single fixed judge model, which was itself one of the evaluated models, a limitation discussed in Section VII.E. More importantly, models with similar task-completion behaviour can diverge sharply in trustworthiness, as several non-frontier models are repeatedly classified Unsafe_Compliance on adversarial tasks rather than merely failing them, a distinction that pass/fail benchmarks cannot surface.

---


### 71. [From Pixels to Hierarchical Sequences: Quadtree Mask Encoding for Vision-Language Binary Change Detection](https://arxiv.org/abs/2609.09876)

**<font color=#1a73e8>作者：</font>** Xiao An, Ruikang Zhang, Chen Zhong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense change detection in remote sensing requires vision-language models (VLMs) to compare bi-temporal images and generate accurate pixel-level masks. Existing VLMs are largely confined to change captioning outputs, and the few that produce pixel-level masks still rely on external decoders or flat text-as-mask serialization, which are less effective for small and fragmented changes. We introduce QUAKE-CD, a framework that recasts dense change prediction as syntax-verifiable structured generation. QUAKE-CD represents binary change masks as grammar-constrained quadtree token sequences, making the masks compact, syntactically checkable, and deterministically decodable within an autoregressive generation space. We further construct QUAKE-CoT, which pairs these sequences with chain-of-thought traces grounded in visual evidence, and jointly optimizes textual reasoning and spatial dense prediction through a progressive curriculum followed by grammar-gated dual-reward RL. On QUAKE-CoT, QUAKE-CD achieves 78.31% accumulated F1, outperforming decoder-based and flat text-as-mask VLMs while producing more faithful bi-temporal reasoning.

---


### 72. [Scored vs. Generated Readouts in Behavioral Language Models: An Empirical Study of Elicitation Format](https://arxiv.org/abs/2609.09882)

**<font color=#1a73e8>作者：</font>** Touchapon Kraisingkorn, Krittin Pachtrachai, Wachiravit Modecrua  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models fine-tuned on customer behavior can predict outcomes and generate explanations, but these readouts are often treated as interchangeable. Holding model checkpoint and prompt content fixed, we compare probabilities obtained by scoring answer tokens with predictions generated after a written rationale. Across 13 model-domain cells covering four retail tasks in three markets, including two using fully public data and checkpoints, the scored readout ranks outcomes more accurately in 12 of 13 cells (two-sided sign test, p approximately 0.003), by 1.5 to 14.5 points in area under the receiver operating characteristic curve (AUC). Paired bootstrap confidence intervals exclude zero in every newly measured cell. The gap varies with task-specific supervision and mismatch between training and serving formats, ranging from -2.2 points for an untuned base model to +13.7 for rationale-format supervision. Analysis of approximately 9,000 rationales identifies two correlates: reduced reliance on the dominant predictive feature and convergence on stock formulations. Probability saturation does not track the gap. A third readout, eliciting a probability before any verdict, improves calibration (Brier score from 0.47 to 0.15) while ranking within noise of scoring, but only for outcome rates represented in training; it is worse than scoring when the scored head is already calibrated. We interpret these differences through the objectives matched by each readout, identify training choices that narrow the gap, and propose retaining generated rationales while sourcing ranking from the scored head.

---


### 73. [Forward-Free LLM Depth Pruning via Weight Redundancy](https://arxiv.org/abs/2609.09883)

**<font color=#1a73e8>作者：</font>** Vincent-Daniel Yun, Woosang Lim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Depth pruning reduces large language model (LLM) inference cost by removing complete Transformer blocks. Activation-based methods collect hidden states through forward passes on calibration data, while existing forward-free methods score each Transformer block separately without measuring similarity between blocks. We propose Weight-Redundancy Pruning (WRP), a forward-free depth-pruning method that estimates inter-layer redundancy from checkpoint weights to select blocks without calibration data or model forward passes. WRP compares attention output and MLP down-projection weights across layers and combines their pairwise similarities with relative projection-scale information. The resulting all-pairs similarity matrix guides layer grouping and block selection. Across multiple pruning settings, model families, and downstream tasks, WRP consistently outperforms existing forward-free magnitude pruning and approaches the performance of activation-based methods.

---


### 74. [When Does Defendant Statement Matter? A Study of Bias and Persuasion in LLM-Simulated Jurors](https://arxiv.org/abs/2609.09887)

**<font color=#1a73e8>作者：</font>** Cho-Ying Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs have been used to simulate human decision-making in professional settings, yet their behaviors in common-law jury trials remain unexplored. We study when and how a defendant's courtroom statement affects LLM-simulated jurors, focusing on persuasion, ideological bias, and background-based affinity. To support the analysis, we introduce JuryBench, a benchmark containing controversial criminal cases in U.S. criminal law. In each case, a defendant can claim various plausible justifications to support acquittal or reduced liability. We fix the base case and design defendants of different backgrounds, who give courtroom statements with varying emotional appeal or rebuttal. Jurors with diverse ideological profiles across the spectrum are simulated. We examine 20 frontier LLMs, resulting in a total of 432K decisions and rationales, and quantify changes in verdict severity. Our findings show that LLM-jury simulation echoes many human-jury findings. First, emotional persuasion can be detrimental, since jurors may perceive it as evidence of guilt or inconsistency. Next, we show that background fit between jurors and defendants is a stronger and significant factor than other isolated factors, and that jurors are in general harsher toward opposite-background defendants and lenient toward same-background ones. Finally, we find that juror ideology also strongly shapes severity judgments. These findings highlight both the promise and risks of using LLMs to model jury reasoning and call for careful evaluation. The data and code are available at this https URL

---


### 75. [Leveraging Fine-grained Error Correction in Korean Speech Recognition for Consultation Services](https://arxiv.org/abs/2609.09889)

**<font color=#1a73e8>作者：</font>** Yonghyun Jun, Jimin Lee, Hwan Chang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Speech Recognition (ASR) technology is fundamental to customer service automation and large-scale transcription. However, even advanced ASR models exhibit inevitable errors in complex real-world environments such as call center conversations. When privacy restrictions preclude audio access, error correction must rely on text-based post-editing. Existing text-only approaches face significant challenges in low-resource languages, mainly due to a critical scarcity of annotated corpora and tailored correction methodologies. For Korean, this resource gap is particularly pronounced, as existing resources are predominantly designed for ASR training rather than text-based error correction. To address this, we introduce DasanCallDial, the first large-scale Korean benchmark dataset specifically curated for dialogue-level ASR error correction. Derived from genuine call center interactions, it comprises 1,974 dialogues with 115,460 utterances. Leveraging this resource, we propose Detector-Gated Contextual Span Correction (DCSC), a text-only post-editing framework for error-sparse Korean speech recognition transcripts. DCSC combines an encoder-based detector that first performs token-level error detection, followed by a language model-based corrector trained to rectify fine-grained span-level errors. Additionally, we employ dialogue-level context augmentation to enable the model to leverage discourse history for disambiguation. By employing multi-level granularity, our method achieves state-of-the-art performance, effectively overcoming the limitations of general LLMs in low-resource settings.

---


### 76. [Can We Trust Video Hallucination Detectors? VidHalLoc for Evaluating the Evaluators](https://arxiv.org/abs/2609.09895)

**<font color=#1a73e8>作者：</font>** Xinyu Chen, Adnan Mahmood, Mark Dras  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-language models and video agents can produce hallucinations that conflict with spatiotemporal evidence. Existing benchmarks mainly evaluate model hallucinations, and heterogeneous mechanisms make detector reliability difficult to compare. We introduce VidHalLoc, a benchmark that evaluates hallucination detection methods under a unified diagnostic evaluation protocol using 2,000 adversarial hallucination samples across Video Question Answering and Video Captioning tasks, spanning Ontology and Dynamic hallucination categories. To construct VidHalLoc efficiently, we introduce VideoHALO, a Harness Engineering-informed multi-agent workflow that decomposes data construction into four executable stages supported by a memory system and a communication protocol. Evaluation of fifteen methods reveals that the four dedicated detectors peak at an Overall accuracy of only 34.63%, indicating limited reliability across video hallucination types [Dataset Repository: this https URL].

---


### 77. [Grounded Evaluation and Repair for NL-to-PDDL Problem Generation](https://arxiv.org/abs/2609.09898)

**<font color=#1a73e8>作者：</font>** Joana Rosa, Pedro Santos, Valdemar Oliveira 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown promise for translating Natural Language (NL) planning descriptions into PDDL problem instances. However, standard evaluation criteria such as syntactic validity or planner success can substantially overestimate faithfulness to the described task: a generated problem may be parseable and solvable while misrepresenting the intended initial state, goal, object structure, or optimization target. This paper studies an end-to-end NL-to-PDDL pipeline that combines LLM generation, checks in terms of PDDL parsing, planning and validation, a domain-conformance checker, an LLM critic, and iterative repair. Fine-grained repair feedback is constructed from the domain description, the generated problem, the natural language problem description, and operational diagnostics. Reference-based comparisons against curated benchmark PDDL problem descriptions are used for post-hoc benchmark analysis, and these offline checks include renaming-invariant structural matching and semantic equivalence, where domain support is available. Across Planetarium, AutoPlanBench, and curated PDDL~2.1 problems, results show that operational success and benchmark-reference reconstruction can diverge substantially. Results also show that structured repair can be useful, and that PDDL~2.1 remains challenging for reference reconstruction, even when operational success improves.

---


### 78. [Strangers to Themselves: What Language Models Say About Themselves Is Generic](https://arxiv.org/abs/2609.09899)

**<font color=#1a73e8>作者：</font>** Phil Blandfort, Urja Pawar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models can fluently describe how they would behave: whether they would cave to pushback, misuse a tool, or lie under pressure. Is that description actually about the model speaking? We turn self-knowledge into a prediction test. Across nine behavioral evaluations, we measure how a model behaves under different conditions, ask it to predict those rates, and compare its predictions with controls that remove the self from the question. We find that: (i) Direct self-report is weak (r = +0.04), and even showing the model the exact items only raises prediction to +0.24. Crucially, the same item-informed question about "capable AI agents in general" does just as well (+0.28), while other models' answers about themselves predict the target model at least as well as its own. (ii) Frontier scale does not detectably change this pattern: any gains in prediction are not self-specific, and are consistent with a better theory of how AI assistants behave rather than better self-knowledge. (iii) First-person framing does have one robust effect: it shifts reports in the flattering direction, understating harmful behavior relative to the same question about a generic agent. (iv) Finetuning on a model's own behavioral record can teach narrow self-predictions, but it also changes the behavior being predicted and the gains do not transfer broadly. The practical implication is simple: asking a model what it would do mostly reveals a theory of AI assistants in general, plus a favorable bias, rather than privileged knowledge of that model.

---


### 79. [Deep and shallow biases in language models](https://arxiv.org/abs/2609.09901)

**<font color=#1a73e8>作者：</font>** An Vo, Vy Tuong Dang, Khai-Nguyen Nguyen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often repeatedly select the same answer even when many alternatives are plausible. Prior work treats this concentration as bias, but it does not distinguish stable model preferences from responses that depend on a particular prompt wording. We introduce a bias depth score that measures both how strongly a model prefers its top answer under direct prompting and whether that answer survives scenario reframing. Across 4,442 opinion prompts and four large language models, only about a quarter of the concentrated preferences survive reframing. We call these persistent cases Deep biases, and the remaining prompt-dependent cases Shallow biases. Our results show that Deep biases are more often inherited from pretraining and preserved through SFT. Under both continued fine-tuning and prompt-based debiasing for diversity, Deep biases are consistently harder to remove than Shallow biases. Bias depth therefore separates stable learned biases from prompt-wording artifacts that single-prompt metrics conflate. Code, models, and data are available at this http URL.

---


### 80. [Time-Frequency Geometric Cross-Attention for Chunked Vision-Language-Action Models](https://arxiv.org/abs/2609.09925)

**<font color=#1a73e8>作者：</font>** Shengye Dong, Haochen Niu, Hao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern vision-language-action (VLA) policies predict a whole chunk of actions: one to two seconds of coordinated motion emitted in a single forward pass. Yet an action chunk is essentially a short multivariate trajectory, but inside these models it is a sequence of generic per-timestep hidden tokens decoded by a linear head. This under-serves two motion structures. First, frequency: a chunk superimposes a smooth global trend and fine corrective motion across time scales, and a single token entangles them. Second, cross-phase geometry: motions of different phases (reach, contact, grasp adjustment, settling) unfold along very different, near-orthogonal directions in representation space, yet are tightly related for the task and arise across the time axis. Dot-product attention scores alignment by an inner product, so it favors aligned tokens and is least sensitive near orthogonality, leaving such relationships for the network to recover through a detour.
We introduce Time-Frequency Geometric Cross-Attention (TFGCA), a drop-in module repairing both blind spots. TFGCA uses a per-dimension learnable stationary wavelet transform to decompose the action chunk into time-frequency tokens, and each time token retrieves information from them via a cross-attention that fuses the dot product (similarity) with the wedge-product magnitude (sensitive to near-orthogonality) through a learnable weight. A zero-initialized residual reproduces the base behavior at initialization, so it can be dropped onto a pretrained VLA and fine-tuned jointly. Relative to the same-source base, TFGCA improves in-distribution LIBERO by +1.5 on average, the OOD LIBERO-Plus by +6.3, the randomized average under RoboTwin domain randomization by +28.5, and the overall success rate on three real-robot AgiBot A2 tasks by +11.67 points, with larger gains out of distribution.

---


### 81. [Structural Process Supervision for Latent Chain-of-Thought Reasoning](https://arxiv.org/abs/2609.09928)

**<font color=#1a73e8>作者：</font>** Yiqi Li, Xu Chen, Chen Ju 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent reasoning approaches enhance token-level efficiency and robustness by replacing verbose, explicit chain-of-thought (CoT) tokens with compact continuous-space embeddings. However, existing methods lack direct process supervision over these latent embeddings, which often leads to representation collapse and uneven information distribution. To address this, we propose Prototype-Mediated Process Supervision (PMPS), which introduces learnable reasoning prototypes as semantic anchors to provide structural process-level supervision for latent reasoning. PMPS projects latent embeddings and explicit CoT embeddings into a shared prototype space, achieving many-to-many soft alignment between unequal-length representations through prototype assignment. Meanwhile, we introduce a Progressive Sequential Alignment (PSA) module to further guide training: positional priors initially encourage sequential alignment structure, then gradually relax to permit adaptive matching. Experimental results show that PMPS compresses output token length to under 50% of explicit CoT on GSM8K-Aug. Compared to leading baseline SIM-CoT, our method achieves average accuracy gains of 2.08% across different model families. On GPT-2, PMPS even surpasses CoT-SFT. On larger models and a more challenging task, PMPS consistently attains the highest accuracy among all latent reasoning methods with comparable output length.

---


### 82. [Vague2Detect: Handling Ambiguous Prompts in Knowledge-Based Open-World Detection](https://arxiv.org/abs/2609.09949)

**<font color=#1a73e8>作者：</font>** Ibrohimjon Muminov, Jihie Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world detectors must often interpret functional or ambiguous prompts, yet conventional models such as YOLO remain restricted to fixed class lists. Even open-vocabulary models like YOLO-World frequently misalign vague language with the intended objects. Building on our prior work Commonsense-Guided Open-World Object Detection Using LLMs and Visual-Semantic Matching, we address YOLO-World's limitations in grounding task-driven queries. We propose Vague2Detect, a hybrid pipeline in which a fine-tuned Sentence-BERT retrieves candidates from a structured household Knowledge Base (KB), and YOLO-World verifies their presence in the image. For prompts outside the KB, a large language model (GPT-3.5-turbo) generates candidate descriptions, dynamically expanding the KB to cover novel concepts. On a benchmark of household scenes using custom images and an Open Images V7 subset, YOLO-World alone achieves only 32% Vague Prompt Success Rate (VPSR), the ability to map ambiguous queries to correct detections. In contrast, Vague2Detect improves performance to 61% VPSR with high precision, and up to 85% when augmented with GPT fallback.

---


### 83. [5-Dialects-BN: Unmasking the Impact of Transliteration on Bangla Dialectal LLMs](https://arxiv.org/abs/2609.09964)

**<font color=#1a73e8>作者：</font>** Md Mahir Jawad, Galib Mahmud Jim, Rafid Ahmed 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved remarkable progress across natural language processing (NLP) tasks, yet their capabilities degrade sharply for low-resource languages and dialectally diverse settings. Bangla, the world's sixth most spoken language, exemplifies this gap: existing resources overwhelmingly target Standard Bangla, leaving its regional dialects without the benchmarks needed to develop or evaluate dialect-aware systems. We address this gap with 5-Dialects-BN, the first multi-annotation Bangla dialect benchmark to align Romanized transliteration with dialectal text, Standard Bangla, English, and subjectivity labels across five regional varieties. The dataset comprises 6,000 manually annotated entries spanning five major dialects: Chittagong, Barisal, Noakhali, Sylhet, and Rangpur (Chittagong 1,900; Noakhali 1,500; Sylhet 1,200; Barisal 700; Rangpur 700), reflecting natural online availability. Each entry is enriched with five aligned annotations: the original dialectal text, a Romanized transliteration, an English translation, a Standard Bangla translation, and a subjectivity label (subjective vs. objective). Annotations were produced and cross-validated by native speakers and undergraduate linguistics students to ensure dialectal authenticity and semantic fidelity. The resulting resource supports a diverse suite of tasks, including dialect identification, dialect-to-standard normalization, machine translation, subjectivity classification, and parameter-efficient fine-tuning (e.g., LoRA) of multilingual LLMs. By providing a standardized, multi-annotation benchmark, 5-Dialects-BN enables principled evaluation of LLMs on dialectally diverse Bangla and lays a foundation for further research in low-resource, dialect-aware NLP.

---


### 84. [Putting Captions to the Test: Evaluating Video Caption Quality through Multiple-Choice Question Answering](https://arxiv.org/abs/2609.09973)

**<font color=#1a73e8>作者：</font>** Zizhen Wang, Bo Feng, Zhengfeng Lai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating video captioning remains a critical challenge for Visual Large Language Models (VLLMs). Existing metrics primarily rely on matching generated text against ground-truth references. This paradigm suffers from the ``one-to-many'' nature of video description, where high-quality captions are often penalized for lexical mismatches or valid shifts in visual focus. Furthermore, such assessments are typically one-dimensional, failing to provide a fine-grained analysis of caption quality. To address this, we redefine caption quality through the lens of information fidelity: A caption must maximize the coverage of salient visual information while ensuring strict factuality. We introduce CapQuiz, a novel reference-free benchmark that assesses captions based on their utility in answering human-verified, fine-grained, multiple-choice questions derived from the video. CapQuiz features a hierarchical taxonomy of 10 question types (spanning Descriptive and Inferential categories) across 24 diverse video domains. Extensive experiments demonstrate that CapQuiz correlates significantly better with human judgments than existing metrics and offers interpretable insights into model performance.

---


### 85. [Towards Stress-Aware Sentence-Level Filipino G2P With Weakly-Supervised ByT5 Fine-Tuning](https://arxiv.org/abs/2609.09974)

**<font color=#1a73e8>作者：</font>** Lorenz Bernard Marqueses, Paulo Grane Gabriel Silva, Chastine Cabatay 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grapheme-to-phoneme conversion (G2P) refers to the task of converting a sequence of graphemes to a corresponding sequence of phonemes. While Filipino G2P is fairly straightforward due to its shallow orthography, the inclusion of prosodic features such as stress adds a layer of complexity that requires sentence-level context instead of single-word inputs. However, sentence-level data for Filipino typically do not include phoneme transcriptions, posing a challenge for training G2P models. As such, we investigate how to obtain sentence-level phoneme data for Filipino using available data and compare the resulting models with multilingual word-level G2P as well as measure how accurately they predict stress marker position for Filipino. We propose fine-tuning a ByT5-based model, pre-trained on multilingual word-level G2P data, on three sentence-level G2P datasets annotated with an LLM-assisted pipeline guided by data from Wiktionary. This approach produces models that perform well on the G2P task, achieving at best around 0.54% PER and 2.50% CER, a significant decrease compared to base model PER at around 19.74%, on a manually-corrected test set. The model is able to correctly classify most of the main stress classes in Filipino, but struggles particularly with malumi words. We show that a ByT5-based model performs well at sentence-level Filipino G2P and offers strong potential for Filipino homograph disambiguation.

---


### 86. [Multi-Functional Embedding Models for Funder Name Disambiguation in Scientific Publication Records](https://arxiv.org/abs/2609.09984)

**<font color=#1a73e8>作者：</font>** Kanyao Han, Zhiwen You, Jinseok Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding the historical allocation and distribution of research funding advances our knowledge of how scientific research is supported across fields, institutions, and regions. However, large-scale analyses are hindered by the lack of comprehensive funder name disambiguation solutions, as funder names often exhibit spelling variations, translations, abbreviations, and inconsistent levels of granularity. In this paper, we present a framework for developing multilingual, multi-functional funder name disambiguation models and demonstrate its application to research publications in biodiversity conservation. To construct a training dataset, we integrated the Research Organization Registry (ROR), which provides unique identifiers for research organizations, with two publication datasets: the Web of Science (WoS) and the Crossref Open Funder Registry (OFR). We used multi-task learning with Contrastive Loss and Multiple Negatives Ranking Loss to fine-tune three open-weight embedding models from the Sentence Transformer, Gemma, and Qwen3 families. The best-performing models achieved accuracy above 0.90 when matching WoS funder names to ROR identifiers, outperforming general-purpose LLMs, including GPT-5.2, Claude-Sonnet-4.6, and Gemini-2.5-Flash, by more than 0.1. For funder names not indexed in ROR, we constructed a similarity network among funder names and identified clusters within it. Finally, we analyzed the disambiguation results and highlighted challenges arising from limited knowledge of smaller funders and funders from non-English-speaking countries. This work provides a reusable framework for funder name disambiguation with potential applicability across different model architectures and datasets, featuring cost-effective training data creation and multi-task learning and disambiguation.

---


### 87. [VLX-VR: An Agentic-Aware Video Reasoning Model](https://arxiv.org/abs/2609.09985)

**<font color=#1a73e8>作者：</font>** Sheng Li, Peng Liu, Qianqian Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-world video understanding requires integrating visual, audio, textual, and temporal evidence distributed across a video. Yet many pipelines use a fixed video context and single-pass inference, limiting adaptive evidence acquisition when observations are incomplete, ambiguous, or conflicting. We present VLX-VR, an agentic-aware video reasoning model trained within a video reasoning framework defined by a Think--Memory--Observation loop. At each step, VLX-VR determines the needed evidence, invokes read_memory or write_memory, incorporates the returned Observation, and decides whether to continue or produce the task output. We train VLX-VR with multimodal data, including videos and agent trajectories, using reinforcement learning to learn evidence acquisition, memory use, and termination. On MINERVA, VLX-VR achieves state-of-the-art performance among the models included in our comparison, with 78.79% accuracy. Under the original three duration groups, its accuracies are 76.70%, 78.73%, and 80.92%, with a cross-duration accuracy variance of 2.97~$\mathrm{pp}^2$. On correctly answered samples, 96.20% of VLX-VR's reasoning traces are consistent with the MINERVA reference reasoning traces and the evidence described by them, while approximately 75.80% of all evaluated samples satisfy both answer correctness and this evidence-grounded trace criterion. These results show strong performance and broadly stable behavior across durations, while counting, state changes, causal reasoning, and spatial perception remain challenging.

---


### 88. [Beyond Similarity: Foundation Models as an Efficient Backbone for Training-Free Composed Video Retrieval](https://arxiv.org/abs/2609.10008)

**<font color=#1a73e8>作者：</font>** Dmitry Demidov, Muhammad Zaigham Zaheer, Omkar Thawakar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed video retrieval (CoVR) searches a gallery for the target video that realizes a natural-language modification of a source clip. However, at gallery scale, this creates a fundamental tension: compact embeddings enable efficient, reusable search but can miss the transient actions, state changes, and subtle constraints that demand fine-grained video reasoning, whereas applying large multimodal models uniformly sacrifices scalability. To address these limitations, we propose that frozen foundation models should instead occupy complementary roles, with inference depth adapted to query difficulty. Based on this premise, we introduce \methodname{}, a framework for training-free \methodexpansion{}. Specifically, a composed-query embedding first searches reusable video-only gallery representations; uncertain queries undergo bounded reranking and candidate expansion; ambiguous edits trigger target-description generation; and only close leading candidates reach multimodal verification. To support these roles, frame selection, spatial resolution, and time cues are adapted to each stage. Across complete target-gallery evaluations, our method reaches state-of-the-art performance among training-free approaches, with 89.55 and 93.43 R@1 on Dense-WebVid-CoVR and CoVR-R, respectively (with more than +35\% and +25\% absolute margins to the closest counterpart). These results show that adaptively orchestrating foundation-model capabilities can combine scalable retrieval with fine-grained reasoning without task-specific training. The source code and all relevant guidelines are available on this https URL.

---


### 89. [MetroLLM-Bench: Evaluating Language Models as Transit Kiosk Runtimes](https://arxiv.org/abs/2609.10016)

**<font color=#1a73e8>作者：</font>** Remco Hendriks  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce MetroLLM-Bench, a 955-case benchmark for testing language models as the policy layer of a transit kiosk. It covers six real metro systems, ranging from 37 to 414 stations, and eleven categories that include routing, fare calculation, disruptions, accessibility, and adversarial input. In each case, the model must call structured tools and submit a machine-renderable terminal state containing an outcome, a per-ticket fare quote when applicable, and a kiosk action. Fourteen deterministic scoring components form Tier 1; eight semantic-quality components form Tier 2, six of which use a language-model judge. We report Tier 1 and the combined score of both tiers. A stratified 75/25 split reserves 717 cases for training-data generation and 238 for held-out evaluation.
We evaluate twenty-six models from six vendors, of which twenty-three are ranked. On the held-out partition, a 4B Qwen 3.5 student trained through parameter-efficient fine-tuning (PEFT) exceeds both GPT-5.6 tiers on Tier 1 (91.3 against 90.6 and 90.0) and matches GPT-5.4 full at maximum reasoning effort (91.4), with a 2.6 GB Q4_K_M footprint. Larger 9B and 27B students provide no further Tier 1 improvement over the 4B student at this training scale. Across the four Qwen sizes, the PEFT gain over the corresponding base model decreases from +7.03 points at 2B (three training seeds) to -0.91 at 27B; every seed shows the same direction at every size. A deterministic rule-based baseline reaches 84.6 on Tier 1, with the remaining language-model advantage concentrated in policy adaptation, compound scenarios, accessibility, and temporal reasoning. Muse Glimmer 30B leads the composite ranking, and serving configuration alone moves the Qwen 3.5-to-3.8 comparison by 2.7 Tier 1 points. The benchmark, harness, reproduction guide, and fine-tuned students are released at this https URL.

---


### 90. [Belief-State Engine: Augmenting LLMs for Principled Planning Under Partial Observability](https://arxiv.org/abs/2609.10036)

**<font color=#1a73e8>作者：</font>** Arnab Chattopadhayay, Debdipta Halder  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents produce fluent action sequences across a wide range of tasks, yet they fail in characteristic ways once the environment becomes partially observable. Ambiguous feedback pushes them into premature commitments. A single informative observation can collapse their uncertainty onto the wrong hypothesis. Policies drift as the history grows. We trace these symptoms to a common structural cause. An LLM agent, as commonly deployed, is a history-conditioned policy with no explicit belief over hidden state.
We propose an architectural fix. The Belief-State Engine (BSE) is an inference module placed outside the LLM. It maintains a Bayesian posterior over the latent states of a given POMDP (Partially Observable Markov Decision Process) model, and at each decision step it exposes only that posterior to the LLM. The raw action-observation log is not shown. We set out a minimal four-axiom specification of what a belief-consistent internal state must satisfy, and prove that the LLM paired with the BSE is a sound Markov policy on the belief MDP induced by the underlying POMDP. It therefore inherits the Bellman optimality guarantees of classical POMDP theory, provided the LLM is never exposed to the raw history.
We evaluate the architecture on the Tiger POMDP and a red-team attack-graph task, against six baselines: a reactive LLM, Chain-of-Thought, ReAct, a natural-language belief tracker, QMDP, and POMCP. Across both domains, the BSE-augmented agent improves task return, belief calibration, and decision consistency. Ten targeted ablations isolate the contribution of each architectural choice confirms that the effect is not specific to any one model. Code, environment specifications, prompt templates, and seed logs accompany this paper.

---


### 91. [Streaming P300 Acquisition and Statistical Signal Validation Across Five EEG Platforms: A Hardware-Agnostic BrainFlow/LSL Pipeline](https://arxiv.org/abs/2609.10047)

**<font color=#1a73e8>作者：</font>** Isabella Guan, Rui Liu, Fusheng Wang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> P300 spellers offer people with severe motor impairment, such as ALS, an effective communication channel and remain one of the most established surgery-free alternatives to intracortical interfaces. Advanced language models have made spellers faster and more robust, yet the hardware beneath them is under-studied. We present a hardware-agnostic, real-time P300 acquisition pipeline built on BrainFlow and Lab Streaming Layer (LSL) that runs unchanged across consumer- and research-grade EEG headsets, with permutation tests of signal separability. Using a standard 6 x 6 row/column paradigm, we piloted five configurations: a custom dry system, a custom wet/gel system, Emotiv Flex, Emotiv EPOC X, and Muse 2. The custom systems and EPOC X showed weak or inconsistent signal separability, Muse 2 had the highest acquisition reliability despite limited centro-parietal coverage, and Flex showed the most promising signal. In 20 further Flex sessions varying subject, timing, and phrase length (131 target characters), a peak-amplitude permutation test and a cross-validated xDAWN decoder both detected a significant target response under two channel-exclusion policies, with decoder AUC reaching about 0.72 after 15 repetitions. Character accuracy depended heavily on evaluation methodology: in-sample majority voting reached 94.7%, whereas character-held-out accuracy was 31.3% with evidence accumulated across repetitions, about three times that of held-out majority voting. These analyses indicate that Flex captured a detectable, if still weak, P300 under the studied conditions, while broader participant-level validation and improved decoding remain necessary.

---


### 92. [Direct Diversity Optimization for Diverse Successful Trajectories in Preference Post-Training](https://arxiv.org/abs/2609.10052)

**<font color=#1a73e8>作者：</font>** Junwon Ko, Dong-Jae Lee, Minchan Kwon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents for sequential decision tasks are often post-trained with trajectory-level outcome labels, but such labels provide little supervision for preserving multiple successful branches from the same decision state. We study this problem as successful strategy coverage: how broadly a model realizes distinct successful strategies under a fixed rollout budget. We present Direct Diversity Optimization (DDO), an offline post-training method that combines Divergence-Tree Collection (DTC) with the Reference-Relative Target-Odds Objective (RTO). DTC constructs state-aligned branch sets rooted at shared decision states, and RTO trains the model to match reference-relative targets over successful alternatives. DDO achieves the strongest task success and successful strategy coverage among the compared post-training methods across BabyAI, BabaIsAI, and WebShop. It also achieves the highest recovery rate after local action replacement and higher task success and coverage than successful-only imitation and decoding-time diversification controls.

---


### 93. [OntologyAligner: Ontology-Aligned Retrieval and Hierarchy-Guided Large Language Model Reranking for Biomedical Ontology Normalization](https://arxiv.org/abs/2609.10055)

**<font color=#1a73e8>作者：</font>** Jie Song, Zhichuan Xu, Ziyu Lu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biomedical ontology normalization maps free-text expressions to standardized concepts, enabling consistent integration and analysis of biomedical data. This task remains challenging because lexical variation and subtle distinctions among hierarchically related concepts can obscure concept boundaries. We present OntologyAligner, a three-stage framework that combines ontology-aligned retrieval, large language model candidate reranking, and selective hierarchy-guided refinement. We also construct PhenoNormBench, a unified benchmark comprising 13,390 samples from seven Human Phenotype Ontology datasets. OntologyAligner achieved state-of-the-art performance on HPO normalization, with 88.78% Macro Top-1 Accuracy and 86.75% Micro Top-1 Accuracy, exceeding the strongest baseline by 4.85 and 5.07 percentage points, respectively. Ablation analyses showed complementary contributions from all three stages, and sensitivity analyses demonstrated stability across candidate-set sizes and model backbones. Applications to MONDO, MEDIC, and NCBITaxon further established portability to other ontologies. OntologyAligner offers a generalizable framework for accurate mapping of biomedical text to structured ontology concepts. PhenoNormBench and the code are publicly available at this https URL.

---


### 94. [AutoTrans: AI-Assisted Automatic Translation of Security Assertions for RISC-V Processors](https://arxiv.org/abs/2609.10057)

**<font color=#1a73e8>作者：</font>** Sharjeel Imtiaz, Uljana Reinsalu, Tara Ghasempouri  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reusing a set of verified security assertions across RISC-V processor targets remains one of the most expensive bottlenecks in hardware security verification. Manual translation takes hours per assertion. Raw LLM translation is fast but unreliable, introducing signal hallucination, where the model invents port names absent from the target RTL and produces outputs that may vary across model updates or even within the same model version. This paper presents AutoTrans, an automated framework that addresses the above shortcomings. First, a new lightweight Regular Expression-based System Verilog signal extractor is proposed to identify the signals for generating security assertions. This step is necessary to prevent signal hallucination. Second, a template is introduced to create prompt and pinned inference parameters that guarantee a byte-identical prompt assembly on every run, making the pipeline output resilient to model updates. Moreover, the introduced template for LLM prompting is capable of generating security assertions from English-only security descriptions of RISC-V processors, with no manual authoring. Third, a formal verification process (JasperGold FPV) is integrated, which guarantees that the generated security assertions verify the security of the RISC-V processor rather than silently entering the result set. The workflow is applied on Deepseek V4 to translate security assertions from one RISC-V to another (e.g., for IBEX from NS31A RISC-V). The experiment shows that AutoTrans achieves 78\% Auto Translation Acceptance Rate (TAR) automatically and without human intervention and 100\% Final TAR after refinement by humans.

---


### 95. [Reference-Based Bias Detection in LLMs via Relative Representations of Hidden States](https://arxiv.org/abs/2609.10060)

**<font color=#1a73e8>作者：</font>** Marek Jeliński, Jan Dubiński, Maciej Chrabaszcz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing bias auditing methods typically rely on model outputs, requiring costly benchmarks or judge models and potentially missing internal shifts that never appear in generated text. We propose a reference-based method that audits bias in hidden-state representations across related model variants, for example before and after fine-tuning. Because fine-tuning reshapes representation geometry, absolute hidden states are not directly comparable, so we encode each sentence by its similarities to a fixed set of anchor sentences, yielding relative representations in a shared comparison space. There we measure how target groups shift in their association with positive and negative attributes, a quantity we call the Representational Bias Shift $\Delta B$. Across three model families and the WildGuardMix, DecodingTrust and ToxiGen benchmarks, $\Delta B$ correlates with output-level bias change in 15 of the 18 settings we test, reaching $|r| = 0.84$ ($p < 0.001$) under full fine-tuning and becoming more model-dependent under parameter-efficient adaptation. Thresholding $\Delta B$ detects checkpoints whose bias increased with ROC AUC between $0.65$ and $0.99$, and on WildGuardMix and DecodingTrust it separates them better than a SEAT-based baseline for all three families. $\Delta B$ is also stable under changes to the anchor set, attribute sets and target templates. Our method requires no task-specific evaluation data and audits a model in about three minutes, using $3$-$50\times$ less compute than the output-level benchmarks considered here. We view it as complementary to output-based auditing rather than a replacement for it.

---


### 96. [RAP: Research Attention Prediction Reveals Target-Conditioned Evidence Acquisition Biases](https://arxiv.org/abs/2609.10092)

**<font color=#1a73e8>作者：</font>** Yingqian Wu, Jingcong Liang, Siyuan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly act as research agents, yet their ability to track shifts in research attention is difficult to evaluate because reviews and research ideas lack uniquely verifiable outcomes. We introduce Research Attention Prediction (RAP), a rolling benchmark covering 278 AI/ML fields and 1,390 episodes. At each cut-off, an LLM agent searches a temporally restricted arXiv corpus and predicts the next six months' paper shares across eight frozen research directions. Search generally helps, but all four diagnostic models perform worse than an exact-count exponentially weighted moving average (EWMA) baseline in compositional accuracy. We identify two linked bottlenecks. Under cumulative-history access, State carry-forward outperforms direct Forecast for all four diagnostic models; frozen-evidence replay links a shared component of this reversal to Forecast-oriented policies retrieving a smaller share of recent evidence. Even with exact historical activity, future-specific updating remains limited, with only GPT-5.5 plus reopened Search slightly surpassing EWMA. Fine-tuning on realised outcomes improves Qwen3-4B's forecast Spearman correlation by 0.105 on held-out fields at later origins, with gains also on change-rich episodes.

---


### 97. [Data-Centric Post-Training for Financial Reasoning: Mining, Distillation, and Verifiable Learning](https://arxiv.org/abs/2609.10113)

**<font color=#1a73e8>作者：</font>** Zhirayr Hayrapetyan, Andrei Kalmykov, Denis Kokosinskii 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial text, textbooks, and question-answer pairs are abundant, but only a small fraction is directly usable for reasoning-focused post-training. Existing QA pairs often lack explicit reasoning, sufficient context, or reliably verifiable answers, while textbooks must first be transformed into synthetic training examples. We present a data-centric pipeline that constructs complementary corpora by mining open-source reasoning traces, distilling financial instruction data, and generating knowledge-graph-guided question-answer pairs from financial educational material. After semantic deduplication, three lightweight sequence classifiers select finance-relevant examples, reject under-specified questions, and identify tasks suitable for reinforcement learning with compact rule-based verifiers. For model adaptation, we study supervised fine-tuning and reinforcement learning, while self-distilled fine-tuning and post-training model merging are used to prevent the loss of financial capabilities already present in the starting model. We evaluate the adapted language models using FINESSE-Bench, reporting aggregate performance and changes relative to their starting checkpoints. Across the selected comparisons, ordinary SFT reduces FINESSE-Bench accuracy by 3.2-4.0 percentage points, whereas self-distilled SFT improves over the corresponding starting models by 1.0-2.8 points. Equal-weight merging recovers 3.0 points over its SFT parent and finishes 0.9 points above the original model; GRPO on hard tasks adds 0.4 points after self-distilled SFT or 3.0 points when applied directly to verifiable tasks. These results show that retention-aware adaptation can improve financial reasoning without the regressions observed after ordinary SFT.

---


### 98. [Understanding the Security Boundary of Obfuscation-based On-Device LLM Protection](https://arxiv.org/abs/2609.10117)

**<font color=#1a73e8>作者：</font>** Hanyi Zhou, Chenyang Li, Yuanzhe Pang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted Execution Environments (TEEs) offer a promising mechanism for safeguarding the intellectual property of on-device Large Language Models (LLMs). To overcome the inherent computational bottlenecks of TEEs, existing TEE-Shielded LLM Partition (TSLP) methods apply efficient obfuscation schemes to computationally intensive layers, offloading them to external GPUs while retaining only lightweight operations within the TEE. Although a growing body of TSLP-based approaches has emerged, these defense mechanisms remain largely heuristic. Consequently, some methods are proven vulnerable to certain specialized adversarial attacks designed to exploit their specific architectural implementations. To overcome the limitations of these heuristic designs, this paper addresses a fundamental research question: can we establish common primitives to unify representative prior methodologies, characterize the security boundary of their compositions, and systematically extend them? To this end, we formalize a set of obfuscation primitives, defined as dual-tuples of linear computations satisfying specific algebraic properties. We demonstrate that the matrix-level weight transformations of the representative efficient TSLP frameworks studied in this paper can be expressed as compositions of these primitives; consequently, the canonical form of these primitive compositions, denoted as O_prior, characterizes the structural boundary of this primitive family. We then expose the vulnerabilities of O_prior through a novel primitive-guided attack methodology, Collapse, demonstrating a shared vulnerability in several prominent TSLP methods published in top-tier venues, such as ArrowCloak (Security'25), TSQP (S&P'25), and LoRO (NeurIPS'25). Finally, we introduce two novel obfuscation primitives and integrate them with existing constructs to formulate O_ext, extending this security boundary.

---


### 99. [ProbPlug: A Plugin Uncertainty Network for Reliable Confidence in LLM Binary Classification](https://arxiv.org/abs/2609.10122)

**<font color=#1a73e8>作者：</font>** Jianzong Wang, Chuhang Liu, Botao Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved strong performance across a broad range of classification settings, yet the reliability of their predictions remains a major obstacle to deployment in high-stakes scenarios. Although confidence estimation for LLMs has been widely studied, confidence calibration for LLM-based classification remains underexplored. We introduce ProbPlug, a lightweight confidence estimation framework for LLM-based binary classification, which predicts whether an output is correct using internal token features extracted from a frozen LLM. ProbPlug employs a self-attention module to aggregate hidden representations and can be integrated into the original inference pipeline without modifying the base model. Experiments across multiple tasks involving both text-based and multimodal large models show that ProbPlug provides more reliable confidence estimates, improves classification performance with negligible additional overhead, and exhibits strong generalization across tasks. These results indicate that ProbPlug serves as a practical solution for confidence estimation in LLM-based classification. Our code is publicly available at Github.

---


### 100. [Agent-Based ML-LLM Fusion with Self-Optimizing Prompts for Plateau Weather Alerts](https://arxiv.org/abs/2609.10135)

**<font color=#1a73e8>作者：</font>** Shuai Yan, Yang Xu, Shan He  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To address insufficient contextualization, weak generalization, and poor scenario adaptation in tourism meteorological services, we propose SmartWeatherAgent--a unified three-stage architecture integrating intent recognition, hazard prediction, and reasoning-enhanced generation. The system fuses rule-based methods with large language models to parse queries at multiple granularities and employs a LightGBM model enriched with highland-specific features (e.g., wind speed abruptness rate), achieving an F1-Macro score of 0.605 with 1.60 ms latency on high-wind, precipitation, and low-temperature events. A 12-round micro-step prompt self-optimization loop boosts the composite warning quality score S_final from 4.2 (B01) to 8.9 (B12, +112%). Key improvements include a sharp rise in B08 from data source citation (6.5 -> 8.5), sustained high performance in B10 via physical mechanism explanation, and a peak scientific rigor score of 9.2 in B12 through explicit uncertainty statements. The system autonomously generates structured warnings that integrate causal mechanisms, spatiotemporal evolution, quantitative evidence, regulatory references, and confidence statements--enhancing professional depth, logical rigor, and scientific soundness, and advancing meteorological services toward proactive perception, explainable decision-making, and intelligent agency.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-148](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
