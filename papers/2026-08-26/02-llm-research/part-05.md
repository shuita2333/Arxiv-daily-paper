# 🧠 大模型相关研究 | 2026年08月26日

> 本类共 **363** 篇论文：已确认 **347** 篇，待复核 **16** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-363](./part-08.md)

---

### 201. [WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs](https://arxiv.org/abs/2608.22704)

**<font color=#1a73e8>作者：</font>** Yiming Yao, Chenyang Lyu, Xuanfan Ni 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-form audio inputs make the KV cache the dominant memory cost of speech LLMs. Prefill-only KV compression methods permanently discard audio KV positions once evicted, with no pathway to recover them during decoding. We show this is fragile on long-form audio: prefill attention concentrates near the audio start (an attention-sink effect), while decode-time attention distributes broadly, and the two rankings overlap weakly. We propose WnW (Waxing-and-Waning KV cache), which classifies KV-heads into anchor, tidal, and fixed roles via offline calibration. Anchor heads remain on GPU and serve as a decode-time importance observer; tidal heads keep a CPU-resident complement that is recalled chunk-by-chunk based on aggregated anchor-head scores; fixed heads keep only an on-GPU subset, with the rest permanently discarded. On LibriSpeech-Long with two 3B backbones (Voxtral-mini-3b and Qwen2.5-Omni-3B), WnW preserves near-Full-Cache accuracy while keeping only 20% of audio tokens on GPU, where prefill-only baselines fail to terminate. Results generalize across language, task, and domain shifts, and CPU-GPU recall adds little decode-time overhead in our measurements.

---


### 202. [CacheRouter: A Dual-Path Tool Routing Architecture with Cache-Preserving Main-Model Isolation for Long-Tail Tool Discovery](https://arxiv.org/abs/2608.22708)

**<font color=#1a73e8>作者：</font>** Donghui Zha, Lingwei Xu, Linxiao Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool use in LLM systems faces a structural trade-off. Progressive disclosure keeps the prompt small by showing only the tools relevant to the current task, while prompt caching rewards a request prefix that stays fixed across calls; every change to the visible tool list invalidates the cached prefix. This paper treats the trade-off as a problem of request architecture and proposes a dual-path routing design that assigns tool selection and tool delivery to separate channels. The main model always sees a small, fixed set of core tools, so the head of its request is unchanged across calls; all other tools are reached through an independent routing channel, in which a router sub-model searches the full tool list, selects one tool, executes it, and returns the result. Tool registration is automated from source code and supports runtime updates, so the tool set can grow without modifying the main model's request prefix. The design generalizes progressive disclosure: capabilities are disclosed through the routing channel, and the main model's prefix stays stable. A prototype implementation was exercised on 55 functional queries and a 30-turn dialogue; token-level cache hit rates reached 90.99% and 95.2%, cutting input cost to about 12.0% and 8.0% of a no-cache baseline under DeepSeek's pricing, where cache-hit input tokens cost roughly 1/30 of cache-miss tokens.

---


### 203. [A Source-Grounded Framework for Constructing and Evaluating Progressive Multimodal Diagnostic Dialogues from Clinical Case Reports](https://arxiv.org/abs/2608.22713)

**<font color=#1a73e8>作者：</font>** Yufan Wang, Rui Yang, Yi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical diagnosis requires progressive integration of patient history, physical examination, laboratory findings, medical images, and diagnostic-informative tests. However, most multimodal medical benchmarks evaluate fixed inputs or endpoint answers, while fully interactive diagnostic agents conflate evidence selection with evidence interpretation. We present a source-grounded framework to construct progressive multimodal diagnostic dialogues from case reports and an evaluation strategy for assessing MLLMs on final diagnosis, diagnostic reasoning, and image-finding interpretation. Evaluation on 24 internal medicine case reports showed that our framework can accurately convert case reports into reference dialogues, achieving a diagnosis F1 of 0.99 and a reasoning-quality score of 4.79 out of 5. Evaluation on two frontier MLLMs (o4-mini and Claude Haiku 4.5) achieved reasoning-quality scores of 2.75 and 2.50, respectively, with substantially lower diagnosis, reasoning, and image-finding F1 scores. The results demonstrate that fluent responses do not necessarily reflect evidence-grounded clinical reasoning and highlight the utility of the proposed framework for evaluating multimodal diagnostic reasoning.

---


### 204. [LLM-Based Selection of Incongruent Verbal and Nonverbal Behavior for Virtual Humans](https://arxiv.org/abs/2608.22731)

**<font color=#1a73e8>作者：</font>** Parisa Ghanad Torshizi, Stacy Marsella  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Nonverbal behavior generation systems for virtual agents often take an utterance as input and generate nonverbal behaviors that emphasize or illustrate the content of the verbal channel. However, human nonverbal behavior is shaped by more than the content of the speech. It is also influenced by speaker roles, interpersonal relationships, social context, and the cognitive and emotional states of the interactants. As a result, the nonverbal channel may reinforce, weaken, qualify, or even contradict the verbal channel. It may also reveal internal states that are hidden or only indirectly implied in speech, including emotional "leakage" that may be incidental to the immediate interaction. Modeling this richer relationship between verbal and nonverbal behavior is important for designing virtual agents that exhibit realistic, human-like behavior. It is especially critical in training contexts that require nuanced social interpretation, such as counseling simulations involving virtual patients. Drawing on Ekman's framework of verbal nonverbal relationships, we propose a taxonomy of categories in which mismatches between verbal and nonverbal behavior can occur. We then examine alternative approaches for realizing these behaviors using large language models, focusing on whether LLMs can select contextually appropriate mismatched verbal and nonverbal behaviors from a given dialogue and social interaction context. Finally, we evaluate the resulting behaviors in a human-subject study, assessing whether context-driven nonverbal behavior, when embodied in a virtual human, produces the intended effects on observers.

---


### 205. [DiaRelay: Relaying Dialogue Context with a Constant-Size Memory for Emotion Recognition in Conversation](https://arxiv.org/abs/2608.22745)

**<font color=#1a73e8>作者：</font>** Zihao Zhou, Bin Yang, Jinghui Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion Recognition in Conversation (ERC) requires models to identify subtle emotional cues that are often distributed across distant dialogue turns. Existing methods typically incorporate dialogue history through a fixed context window. However, short windows discard potentially useful long-range evidence, while enlarging the window repeatedly re-encodes overlapping utterances, increases computational and memory costs, and may introduce irrelevant context. Moreover, commonly used parameter-efficient adaptation methods, such as LoRA, mainly introduce fixed low-rank transformations in the feature space and do not explicitly maintain a dialogue-level state or condition their transformations on the evolving conversational context. To address these limitations, we propose a lightweight adapter, DiaRelay, to enable LLMs to explicitly maintain a dialogue-level memory for accurate ERC. Based on LoRA, DiaRelay introduces two extra tightly collaborative components, Selective Relay Memory Transition and Dual-axis Relay Memory Read. Selective Relay Memory Transition progressively aggregates useful historical evidence into a bounded relay memory and propagates it across successive utterance predictions. This allows earlier emotional cues to influence later predictions after they leave the local context window, without re-encoding the complete dialogue history or expanding the backbone context length. Dual-axis Relay Memory Read uses the propagated memory to dynamically modulate low-rank feature transformations, enabling context-dependent representation adaptation without test-time gradient updates. Extensive experiments show that DiaRelay can achieve SOTA weighted F1 and accuracy on MELD while obtaining competitive results on IEMOCAP with only an extra 7.1M trainable parameters, indicating the effectiveness and generalizability of our DiaRelay in enhancing LLM-based emotional understanding.

---


### 206. [The Compaction Cliff in Long-Running AI Agent Memory](https://arxiv.org/abs/2608.22752)

**<font color=#1a73e8>作者：</font>** Saber Zerhoudi, Jelena Mitrovic, Michael Granitzer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A safety rule and an episodic log compete for the same tokens in an AI agent's context. When the budget overflows, both are summarized at the same rate; only the rule needs exact wording to remain enforceable. On 20 production agent configurations, Claude Code's /compact prompt on Sonnet 4.6 preserves 53\% of safety rules after one compaction round and 10\% after five. We name this the Compaction Cliff. We address it with Knowledge Triage, a framework that classifies each line of an agent's knowledge base by type and routes each type through its own retention policy. Three deterministic operators implement this triage across the three context-management operations: TypeCompact rewrites items in place under per-type fidelity, TypeDecompose partitions a topic too large to compact safely, replicating in-scope safety rules across partitions, and TypeRetrieve fetches items from external storage with in-scope rules pinned ahead of relevance. On five public corpora, TypeCompact preserves 2--4$\times$ more safety rules than the strongest single-shot LLM compactor at every ratio, with 96\% recall over five rounds. TypeDecompose reaches 0\% locality violations against 93\% under uniform partitioning. TypeRetrieve reaches 100\% recall@50 against 73\% for the best single-shot LLM retriever. On three downstream behavioral benchmarks, we outperform the production Sonnet compactor on medical compliance (paired McNemar $p < 10^{-8}$ on preservation, $N = 200$), the full-policy and hierarchical baselines on retail task pass rate ($p < 0.01$, $N = 115$), and the hierarchical compaction on the airline domain ($p = 0.024$). We release AgentArtifactCorpus (396{,}934 agent configurations from 54{,}628 public GitHub repositories), the classifier, and the reference implementation.

---


### 207. [Beyond Factual Knowledge: Benchmarking and Learning Step-Level Procedural Rule Reasoning in Large Language Models](https://arxiv.org/abs/2608.22753)

**<font color=#1a73e8>作者：</font>** Bohan Yu, Pengfei Cao, Chen Han 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) excel at text understanding and generation, yet still struggle to reliably understand and apply externally provided procedural rules at scale. To evaluate this capability, we introduce RuleWorld, a large-scale benchmark that reformulates rules as globally reusable abstract units rather than instance-specific facts. In RuleWorld, several scenarios, including single-rule, parallel multi-rule, and multi-hop reasoning, are settled for comprehensive evaluation. We further propose DynaRule, an end-to-end framework that injects the given rules into the KV cache and turns retrieval into an internal, learnable, step-wise process. Specifically, DynaRule employs Stacked Step-Level Attention Training with a special <search> token to enable dynamic rule re-attention and updating during inference. In this way, the model can re-attend to the most relevant rules at each step, dynamically replacing outdated ones to support more stable multi-step reasoning. Experiments on RuleWorld show that existing LLMs face challenges under large rule pools, while DynaRule improves average QA accuracy by up to 19 points and achieves over 85% Recall@1 at 10K rules, outperforming strong baselines by large margins. We make our code and dataset available here: this https URL.

---


### 208. [Object-Uni: A Unified Model for Object-Centric Spatial Understanding and Controllable Generation](https://arxiv.org/abs/2608.22757)

**<font color=#1a73e8>作者：</font>** Mining Tan, Yinuo Wang, Ziqi Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified models for visual understanding and generation have made rapid progress, yet they still lack the ability to understand and manipulate the spatial states of object instances. Existing models can describe objects in natural language, but they struggle to precisely represent continuous object poses and generate geometrically consistent images under target viewpoints. To mitigate this, we propose \emph{Object-Uni}, a unified model for object-centric spatial understanding and controllable generation. Specifically, we formulate object-centric spatial intelligence as a unified problem connecting pose perception, spatial reasoning, pose-conditioned generation, and object-centric novel view synthesis. We treat object pose as an explicit geometric variable shared by understanding and generation, rather than merely a prediction label or control signal. To make pose usable by multimodal large language models, we propose a viewpoint-based orientation abstraction that maps orientation into structured viewpoint descriptions while preserving continuous geometric supervision. We further construct an object-centric spatial benchmark (UniSpatial-80K) and train a unified model with an object-token-grounded pose anchor to associate each instance with its pose state. Experiments show that our model improves object-level pose understanding and pose-controllable generation, moving unified models from describing objects toward manipulating spatial states.

---


### 209. [XTC: Head-Aware Sampling by Excluding Top Choices](https://arxiv.org/abs/2608.22758)

**<font color=#1a73e8>作者：</font>** Philipp Emanuel Weidmann, Allen Roush, Judah Goldfeder 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard decoding rules for autoregressive language models promote diversity by rescaling the full next-token distribution or truncating its low-probability tail. These strategies overlook a common regime of open-ended generation in which several continuations are plausible but too much probability mass remains concentrated on the most generic choice. We introduce XTC (Exclude Top Choices), a lightweight head-aware decoding operator that targets this regime directly. XTC identifies tokens whose probabilities exceed an absolute plausibility threshold $\tau$: when at least two qualify, it removes the dominant eligible choices with probability $\rho$ and retains only the weakest plausible alternative before renormalization. Across 60 experiments on Gemma 3 27B Q4, Gemma 3 12B Q6, and DeepSeek R1 14B Q6, with scaling validation on Llama 3.3 70B Q4, XTC improves the diversity-repetition Pareto frontier. On creative generation, Distinct-2 increases by 11--15% and repeat trigrams decrease by 27--47% across the four models. Combined with temperature scaling, gains reach 38% in Distinct-2 and 71% in repeat-trigram reduction over baseline. A blinded Amazon Mechanical Turk study with 150 Master raters yields a 62.3% creativity preference for XTC ($p<10^{-4}$) without reduced fluency, while a GPT-4o control judge reproduces the Anthropic-judge direction on every measure. On IFEval with Llama 3.3 70B Q4, XTC preserves prompt-level strict accuracy within 1.7 percentage points of baseline while recovering most of the diversity gain; a temperature setting matched on Distinct-2 reduces IFEval by 8.8 points. The effect is additive with temperature and repetition penalties, robust across quantization levels and model families, and consistent across twelve prompt genres. XTC has been adopted by this http URL, ExLlamaV2, and text-generation-webui.

---


### 210. [Don't Repeat Yourself: Stopping Verbatim Loops at Sampling Time](https://arxiv.org/abs/2608.22761)

**<font color=#1a73e8>作者：</font>** Philipp Emanuel Weidmann, Allen Roush, Judah Goldfeder 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models generate text autoregressively, but open-ended generation is prone to verbatim looping, in which models repeat spans already present in context. Standard defenses such as repetition, presence, and frequency penalties and n-gram blocking act on token recurrence rather than the sequential structure of a loop, and often suppress looping only at strengths that also degrade formatting or fluency. We propose Don't Repeat Yourself (DRY), a sampling-time logit adjustment that penalizes a candidate token only when generating it would extend the current suffix into an exact continuation of a span seen earlier in the context. Sequence breakers protect chat templates and formatting tokens. Across models from 1.5B to 120B parameters, nine prompt families, and a 600-pair human study, DRY reduces suffix-extension rate by 47% while improving lexical diversity. An intervention-matched placebo produces no comparable reduction, identifying suffix matching as the operative mechanism. On AWQ-quantized 70B and 120B models, DRY reduces loop rate by roughly half while preserving MT-Bench, MMLU, and GSM8K performance, whereas standard alternatives lose measurable ground. DRY has been adopted by popular open-source LLM inference frameworks including this http URL, ExLlamaV2, and text-generation-webui, highlighting its practical impact on text generation.

---


### 211. [Compositional Chain-of-Relations for Faithful Knowledge Graph Question Answering with Large Language Models](https://arxiv.org/abs/2608.22762)

**<font color=#1a73e8>作者：</font>** Chenhui Liu, Jianpeng Zhou, Jiahai Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graph question answering (KGQA) is a key task for evaluating KG-augmented Large Language Models (LLMs), and complex KGQA that requires multi-hop reasoning is especially challenging. Solving a complex query involves two coupled phases: candidate retrieval, which locates answer candidates over the KG, and constraint handling, which filters these candidates against the query constraints. Faithful reasoning requires grounding both phases in the KG. However, existing agent-based methods ground candidate retrieval through entity-centric exploration, while leaving constraint handling to the LLM's internal knowledge, which leads to two critical limitations. (1) Unreliable entity pruning: entity-centric exploration uses entities as search units and must prune them to a fixed-size subset at each hop. Because entity information in KGs is often incomplete and a fixed-size subset cannot retain all valid entities, such pruning inevitably drops valid entities and ultimately leads to wrong answers. (2) Ungrounded constraint handling: query constraints are resolved from the LLM's internal knowledge rather than the KG, leaving the final answers unverifiable and prone to hallucination. To address these limitations, this paper introduces a relation-centric exploration paradigm, which uses relations rather than entities as search units and thus avoids unreliable entity pruning. Built on this paradigm, this paper proposes Compositional Chain-of-Relations (CCoR), a simple and effective framework that grounds both phases in the KG with two relation chains: a main chain for candidate retrieval and a constraint chain that verifies query constraints through explicit KG exploration. Experiments on four KGQA benchmarks show that CCoR consistently improves accuracy, faithfulness, and efficiency over strong baselines, with more pronounced gains on complex queries.

---


### 212. [The Retriever Should Remember: Experience-Amortized Reranking for Long-Term Agent Memory](https://arxiv.org/abs/2608.22767)

**<font color=#1a73e8>作者：</font>** Qi Feng, Chris Ding, Jicong Fan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term language-model agents accumulate memories across interactions, but their retrievers typically do not accumulate retrieval experience. Semantic retrieval is efficient, but embedding similarity does not always reflect whether a memory contains evidence relevant to the current query. Large language model (LLM) rerankers provide stronger query-conditioned relevance scores, yet stateless reranking repeatedly scores a large candidate pool and discards these scores after each query. We introduce EARM, an experience-amortized reranking framework that treats previously acquired LLM relevance scores as reusable retrieval experience. EARM stores sparse query--memory relevance scores in an online matrix, learns their shared structure through causal matrix completion, and combines a small set of newly observed scores with estimated scores to rerank the remaining candidates. The scoring budget decreases as experience accumulates, changing LLM reranking from a repeated per-query expense into a retrieval capability learned over an agent's lifetime. Experiments on long-term conversational memory show that mixed observed-and-estimated reranking improves answer accuracy over semantic retrieval by up to 6.62% and remains effective when only 17.5% of candidates receive direct LLM relevance scores, thereby substantially reducing the inference overhead of LLM reranking. These results motivate a broader view of agent memory: a long-lived agent should remember not only past content, but also how that content has proved useful for retrieval.

---


### 213. [DelistBench: Evaluating Search-Enabled LLMs for Auditable Corporate-Event Database Completion](https://arxiv.org/abs/2608.22770)

**<font color=#1a73e8>作者：</font>** Xuan Yao, Li Shuping, Dai Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial institutions need an independent way to detect missing, stale, and misclassified corporate-event records in vendor databases. We introduce Search-to-Record, a database-assurance task in which search-enabled large language models reconstruct institution-defined event records from public sources for a known security universe and historical cutoff, and DelistBench, a 1,200-record benchmark for security-level delisting announcements. We evaluate five models in paired closed-book and web-enabled conditions. Web access raises announcement-date accuracy within seven days by 34.0 to 48.0 percentage points and event-status accuracy by approximately 2.8 to 21.7 points; the best system achieves 81.5% overall joint accuracy within seven days. Economy web systems achieve 75.9-78.3% overall joint accuracy within seven days at 4.5-6.6% of the API cost of the most expensive web system. Risk-based triage identifies low-error subsets, although the highest-coverage operating point still sends 27.3% of the balanced test set to review. The evaluation identifies web retrieval as the main source of timing gains and shows that low-cost systems can approach the best system's accuracy. Together, Search-to-Record, DelistBench, and the evaluation provide concrete deployment guidance: calibrate triage to local event prevalence and market mix, preserve positive-event recall, and route positive and ambiguous cases to targeted review.

---


### 214. [Can We Perform Online RL for Image Editing without Editing Rewards?](https://arxiv.org/abs/2608.22780)

**<font color=#1a73e8>作者：</font>** Qichao Ma, Jikang Cheng, Ling Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) enables direct preference optimization for image editing through editing-specific rewards, which remain less developed due to costly triplet supervision and complex task-dependent calibration. In contrast, text-to-image (T2I) generation benefits from a mature and diverse reward ecosystem spanning semantic alignment, aesthetics, realism, glyph shape, and other visual preferences. Extending this ecosystem to image editing would substantially broaden the range of visual preferences accessible to RL-based optimization, prompting the central question: \emph{Can We Perform Image Editing RL without Editing Rewards?} In this paper, we argue that the standard image editing dimensions have potential to be mapped to the T2I reward space: image quality can transfer directly, prompt following can be aligned through a description of the desired visual state, and reference consistency admits a coarse semantic conversion by encoding the source content to preserve. However, editing instructions specify relative changes, whereas T2I rewards require self-contained target descriptions; moreover, semantically valid captions from generic vision-language models may be incompatible with the frozen reward. Hence, we further introduce Lever-Edit, a two-stage framework that learns a reward-aligned captioner for counterfactual target descriptions, freezes it, and optimizes the editing policy solely with the transferred T2I reward. Experiments show competitive editing alignment and source preservation against editing-reward-based fine-tuning, while outperforming intuitive transfer baselines.

---


### 215. [OmicSync: Reliability-Aware Spatial Multi-Omics Clustering with Evidence-Constrained LLM Reasoning](https://arxiv.org/abs/2608.22785)

**<font color=#1a73e8>作者：</font>** Rabeya Tus Sadia, Qiang Ye, Qiang Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial multi-omics technologies jointly profile gene expression, surface proteins, and histology at each tissue spot, yet most spatial domain discovery methods provide only cluster assignments, without indicating assignment reliability, modality contributions, or why a domain decision should be trusted. We present OmicSync, a reliability-aware spatial multi-omics framework that couples unsupervised domain clustering with evidence-constrained LLM reasoning using model-derived per-spot signals, including assignment confidence, epistemic routing uncertainty, and modality-routing weights. These signals are converted into structured evidence dictionaries and used to generate standard, stepwise, counterfactual, contrastive, and uncertainty-focused explanations. OmicSync integrates a KAN-GCN backbone with spatial encoding, cross-modal fusion, uncertainty-aware routing, cell-type supervision, and missing-modality imputation. We further introduce OmicSync-R, which closes the reasoning-clustering loop by using automatically computed reasoning-quality scores as REINFORCE rewards, allowing reasoning coherence to shape the latent structure without backpropagating through the language model. Across four 10x CytAssist FFPE spatial proteomics benchmarks, OmicSync achieves the best average rank on Human Tonsil (1.44), Glioblastoma (1.78), and Tonsil Add-on (1.22), and second-best on Human Breast Cancer (2.33). OmicSync-R further improves ARI on Human Breast Cancer from 45.73 to 46.72 and outperforms existing methods on six of nine clustering metrics. Together, OmicSync and OmicSync-R enable reliability-aware, spot-level auditable spatial domain discovery guided by evidence-constrained reasoning.

---


### 216. [TailSieve: Partial-Rollout-Guided Tail Routing for LLM Rollouts](https://arxiv.org/abs/2608.22788)

**<font color=#1a73e8>作者：</font>** Tianqi Xu, Lu Lv, Haoyang Huang 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-scale rollouts have become a core component of modern LLM systems, spanning reinforcement learning (RL) post-training, on-policy distillation (OPD), and sampling-heavy evaluation pipelines. Unlike online serving, which is typically optimized for request-level latency and throughput, a small number of long-tail generations can dominate the end-to-end makespan of an entire rollout step. In practice, rollout requests are often routed uniformly across replicas, which can place extremely long generations inside high-concurrency decoding batches.
To address this, we present TailSieve, a partial-rollout-guided framework that jointly controls tail routing and replica allocation for LLM rollouts. In an idealized setting with known completion lengths, we show that makespan-optimal routing in the long-tail regime combines tail isolation with load balancing, and that a simple top-k policy closely approximates this offline optimum. Leveraging the observation that long-tail prompts tend to remain long-tailed across policy updates, TailSieve uses partial rollouts as a training-free signal for identifying candidate tail groups. A hierarchical controller then jointly adapts the number of isolated groups and the replica split between the tail and bulk pools using collected response-work history and a measured concurrency-throughput model. TailSieve achieves up to 1.67x routing-only speedup over uniform group routing. The resulting low-concurrency tail pool further enables route-specialized speculative decoding with MTP or DFlash, achieving up to 2.59x speedup over uniform routing. Selected prompts are regenerated under the current policy, preserving on-policy generation and avoiding additional routing-induced length bias in steady state.

---


### 217. [TRACE: A Self-Evolving Skill Bank for Consistent, Limit-Aware LLM Agents](https://arxiv.org/abs/2608.22793)

**<font color=#1a73e8>作者：</font>** Wenhao Wu, Menghao Zhang, Xin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable deployment of LLM agents in user-facing products depends not on raw task-solving ability but on consistency and limit-awareness: behaving the same way across repeated trials, and recognizing when a request cannot, or cannot yet, be safely fulfilled. CAR-bench exposes this reliability gap in the domain of in-car assistants: an LLM-simulated user issues incomplete or ambiguous requests, requiring the agent to resolve uncertainty through multi-turn dialogue and tool use while strictly adhering to domain policies. Even frontier models show a substantial gap between what they can solve at least once (Pass@3) and what they solve consistently across trials (Pass^k). We bridge this gap with TRACE (TRAjectory-Contrastive Evolution), which iteratively improves a skill-based agent's behavioral knowledge without modifying model weights. This knowledge is organized as a Skill Bank of modular, retrievable skills, each encoding a self-contained set of tool-use rules and behavioral guidelines. TRACE evolves this bank through an agentic self-evolution loop: after each evaluation round, it groups trajectories by the skills invoked and refines each skill by contrasting successful and failed behaviors. The updated bank then guides subsequent rounds, while during deployment the Actor performs state-conditioned skill orchestration at every turn. On GPT-5.5, TRACE improves consistency (Pass^3) by 34.6 points, from 59.9% to 94.5%, while shrinking the gap between potential and reliable performance to just 4.0 points. On the official hidden set, TRACE achieved first place using GPT-5.6-Sol, attaining a Pass^3 score of 70%-a 40% relative improvement over the baseline. These results show that TRACE converts high model potential into stable, consistent performance gain. Project homepage: this https URL.

---


### 218. [Performance of a domain-specific large language model in answering patient questions in psychiatry](https://arxiv.org/abs/2608.22797)

**<font color=#1a73e8>作者：</font>** Alexander J. Hish, Arjun Nagendran, Scott N. Compton  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background This study was designed to evaluate whether a domain-specific large language model (LLM) trained exclusively on patient education resources can answer questions about psychiatric medications, in a manner superior to LLM chatbots. We developed an LLM ("MIND") fine-tuned for clinical fidelity, trained on patient education resources from authoritative medical organizations. Methods We compared the responses of MIND, ChatGPT, and OpenEvidence to patient questions about escitalopram, using two methods: (1) computer analysis according to a rubric measuring accuracy, clarity, completeness, nuance, safety, and referral appropriateness; (2) ratings from N=10 board-licensed psychiatrists on similar metrics. Results When rated by rubric, MIND was rated highest in all domains (p<0.001). When rated by psychiatrists, ChatGPT was rated accurate more often than MIND with a negligible effect size (p=0.021, r=0.073); MIND was rated complete more often than ChatGPT with a small effect size (p<0.001, r=0.160); and MIND and ChatGPT were rated safe with the same frequency (p=0.955, r=0.002). The majority of psychiatrists preferred the responses generated by ChatGPT (57.6%) compared to MIND (42.4%, p=0.003). Conclusions MIND was able to answer many questions about escitalopram in a manner deemed accurate, complete, and safe by psychiatrists the majority of the time. However, despite MIND's ability to provide more complete responses, psychiatrists preferred ChatGPT's responses. MIND represents a step towards building safe LLM systems to enhance patient education in psychiatry.

---


### 219. [SDoH-Aware Narrative Anchoring Bias in Medical LLMs for Trustworthy Clinical Decision Support](https://arxiv.org/abs/2608.22802)

**<font color=#1a73e8>作者：</font>** Ahnaf Atef Choudhury, Ramkrishna Saha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical large language models are often judged by how many clinical questions they answer correctly. That view is useful, but it misses a practical risk. A model may know the right answer and still change its response when the same case is written in a different patient voice. This paper evaluates that risk as SDoH aware narrative anchoring bias. We use NarrativeShield SDoH MedQA, a counterfactual medical question answering dataset in which each case appears in persona based narratives while the answer key remains fixed. The dataset is reshaped from wide format into case grouped persona rows. We evaluate three open source instruction tuned LLMs from the Qwen2.5 family: 1.5B, 3B, and 7B. The final experiment uses 300 clinical cases and produces 8,100 model responses across three prompting conditions. We report persona level accuracy, counterfactual consistency, correct consistency, and narrative sensitivity error. Qwen2.5 7B achieves the best accuracy at 56.33 percent and the best correct consistency at 40.33 percent. Paired McNemar exact tests show significant accuracy gains for 7B over 3B in all prompt settings. Even so, narrative sensitivity remains, with the lowest error still at 31.67 percent. These results suggest that trustworthy clinical decision support should be evaluated by both average correctness and stability across medically equivalent patient narratives.

---


### 220. [DIAG: Diagnostic Iterative Alignment and Generation for Data-Efficient Mathematical Preference Distillation](https://arxiv.org/abs/2608.22806)

**<font color=#1a73e8>作者：</font>** Guhan Chen, Songtao Tian, Bohan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Iterative preference optimization is essential for aligning Large Language Models on mathematical reasoning tasks, yet its efficiency is often throttled by signal scarcity: as the model improves, static problem sets become increasingly mismatched to the model's evolving competence, producing rollouts that are either too easy or too hard and therefore non-informative, which leads to a scarcity of valid preference pairs. We propose DIAG, a Diagnostic Iterative Alignment and Generation framework that adaptively reshapes the practice distribution to increase informative supervision and focus training near the student's current competence boundary. DIAG consists of two phases: (1) diagnosing valid preference-pair yield to calibrate the exploration-exploitation trade-off and allocate topic quotas via an Empirical Bayes shrinkage estimator, thereby prioritizing high-yield concepts; and (2) generating targeted practice, where a teacher synthesizes variants from the student's failure traces. We further provide a theoretical view interpreting DIAG as a teacher-mediated approximation to KL-regularized reweighting of the practice distribution toward the student's competence boundary, where valid preference-pair yield is maximized. Experiments show that DIAG boosts yield across iterations and delivers stronger reasoning performance under an iso-effective training budget, demonstrating that it can distill more informative preference supervision for mathematical reasoning.

---


### 221. [CatchBench: When Can an Agent Failure Be Caught?](https://arxiv.org/abs/2608.22808)

**<font color=#1a73e8>作者：</font>** Yue Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When can an agent failure be caught? An audit is usually limited by the record rather than by the method. CatchBench therefore puts one auditor's question to three information states: the declared configuration before a run (PRE), a growing prefix of its trace (LIVE), and the finished trace (POST). Prior benchmarks fix one of these states or vary the telemetry; to our knowledge none scores all three under one task-method interface. Each state admits different questions, so seven task contracts carry their own labels and metrics rather than one leaderboard. Four are evidential; three are Gold-derived mechanism diagnostics.
The release scores 72 entrants, from rule scanners and structural models to eleven LLM judges across nine model families (GPT, Claude, Gemini, Gemma, Llama, Qwen, DeepSeek, Mistral, Nova), over 1187 declared configurations and 1162 recorded runs. Most of the arena does not order: 47 of 118 pre-declared contrasts separate, and the rest are published unresolved rather than ranked. The two sharpest results cut against our own data. One rule ignores every name and permission; it flags each capability declared after the first. On one of six configuration sources it reaches a perfect F1, so a score there measures how the corpus was built rather than how well a method reasons. Our admissibility bar then rejected one injected substrate and withheld evidential status from the other. A benchmark number is therefore not interpretable until the process behind its labels is published and tested for the shortcut it may leave. We report both, and regenerate every ordering from released predictions with no model call.

---


### 222. [Industrial-Instruction: An End-to-End Framework for Building Instruction-Tuning and Benchmark Datasets from Industrial Technical Reports](https://arxiv.org/abs/2608.22817)

**<font color=#1a73e8>作者：</font>** Parsa Bakhtiari, Hassan Bashiri, Alireza Khalilipour 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Industrial technical reports contain high-value knowledge for maintenance, troubleshooting, and product engineering, but their heterogeneous structure (dense prose, specifications, tables) makes them difficult to index and reason over with standard retrieval and QA pipelines, and no public instruction-tuning or benchmark datasets are built from such documents. We address this gap with Industrial-Instruction, contributing (i) two open QA datasets built from real industrial technical reports and (ii) the end-to-end pipeline that produces them. Using 906 public Panasonic documents (7,525 pages), we apply layout-aware extraction, build a semantic retrieval index, and synthesize multiple-choice QA grounded in retrieved evidence under five query-document relationships (irrelevant retrieval, single-/multi-document support, single-/multi-document answer). After filtering an initial 23.9k generated samples, each dataset provides approximately 13.6k QA pairs with source documents and a held-out benchmark split. Fine-tuning small open LLMs (under 10B parameters) improves Set-Match Accuracy from 28.5% to 42.0% and F1 from 46.6% to 63.5% on the Panasonic benchmark. We release two parallel versions built by the same pipeline: one generated with the open-weight Qwen3-30B-A3B-Instruct model and one with the closed, API-based Claude-Opus-4.6 model, enabling a direct comparison of open- versus frontier-model data generation. The Claude-Opus-4.6 dataset yields a cleaner raw corpus and larger fine-tuning gains, at roughly two orders of magnitude higher cost. MMLU evaluation shows models trained on the Claude-Opus-4.6 data retain essentially all general knowledge, versus a small but measurable forgetting effect for the Qwen-generated data. Together, these datasets and pipeline offer a practical, reproducible path toward scalable industrial benchmarks and training data from real-world documentation.

---


### 223. [Fairness-Aware Mixture-of-Experts via Subgroup Reweighting and Gate Regularization](https://arxiv.org/abs/2608.22820)

**<font color=#1a73e8>作者：</font>** Sunhee Hwang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models often produce performance disparities across demographic groups, due to the training data imbalance with respect to sensitive attributes such as gender or age. To address this problem, existing work has explored fair representation learning, data re-sampling, and adversarial training, which can be broadly categorized into two main approaches. Single-stage methods typically learn a shared representation for fairness, but often struggle to handle heterogeneous subgroup distributions. Two-stage methods learn representations separately from the final prediction task, which can lead to misalignment between fairness objectives and downstream predictions. We identify routing-induced bias, a failure mode in which subgroup imbalance drives the gating network to route subgroups onto a few experts, and propose an end-to-end Mixture-of-Experts (MoE) framework that corrects it. Specifically, we apply subgroup reweighting to correct data imbalance, and introduce gate entropy regularization to prevent routing from collapsing onto subgroup attributes, keeping expert utilization both balanced and interpretable. Beyond improving fairness, the routing distribution offers an interpretable view of how subgroups are allocated across experts. Experimental results demonstrate that the proposed approach improves fairness while maintaining competitive predictive performance.

---


### 224. [Beyond the Harness: End-to-End Optimization of Context Artifacts for Enterprise Text-to-SQL](https://arxiv.org/abs/2608.22830)

**<font color=#1a73e8>作者：</font>** Kate Gwimm, Carson Eisenach  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying LLMs for enterprise Text-to-SQL is bottlenecked less by the model than by what context reaches it: business logic spans thousands of tables, and no model can ingest a full catalog at once. We argue that the most effective place to intervene is therefore the \emph{knowledge-base context} the model consumes, and that this context should be \emph{constructed} from historical usage rather than tuned for as a fixed input. Using a query-DAG decomposition--the same family of intermediates that enterprise benchmarks like BEAVER annotate, here recovered from production SQL--we compare the value of oracle query graphs versus retrieved knowledge-base context. In this ablation, retrieved knowledge-base context provides the largest marginal improvement when added to the full oracle graph. Building on this, we optimize a distillation procedure that turns historical query profiles into reusable SQL reference cards. On a benchmark of 5176 production queries from a major online retailer, optimizing these context artifacts yields larger gains (${\sim}12$--$25\%$ AST similarity) than optimizing the retrieval harness (${\sim}3$--$12\%$). On the public BEAVER benchmark, which lacks the production-usage signals available in our internal setting, the picture is more mixed: table cards alone perform about the same as raw historical SQL. The best optimized variant retrieves both cards and raw SQL, scoring $9.00\%$ versus $6.33\%$ (p-value $0.12$) for the comparable baseline on a held-out $N{=}300$ subset, using retrieved context and harness changes but no agentic loop.

---


### 225. [Minimal Local Simulation Foundations for LLM- and VLM-Driven Agents in 2D and 3D Environments](https://arxiv.org/abs/2608.22833)

**<font color=#1a73e8>作者：</font>** Ryuki Hyodo  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) and vision-language models (VLMs) are expanding the range of behaviors that can be represented in agent-based simulations, but many contemporary platforms are difficult to study, modify, or run on ordinary computers. We present two intentionally minimal simulation foundations for education and rapid prototyping. SD-AgentFoundry-2D provides a two-dimensional multi-agent environment in which locally hosted LLM agents move, communicate, respond to place occupancy, and encounter spatially localized fire events. SD-AgentFoundry-3D provides a three-dimensional digital-twin environment in which a locally hosted VLM receives first-person images and produces natural-language movement instructions. Both codebases are designed to run locally on macOS, Windows, and Linux and are deliberately left open to modification rather than developed as finished applications. Together, they offer accessible starting points for learning about generative social simulation and for building domain-specific extensions.

---


### 226. [Hierarchy-Aware Supervised Uncertainty Estimation for Black-box LLM Taxonomic Reasoning](https://arxiv.org/abs/2608.22839)

**<font color=#1a73e8>作者：</font>** Shuting Xie, Nathaniel Lesperance, Graham W. Taylor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for scientific decision support, yet reliable confidence estimation remains difficult in black-box settings. We study uncertainty estimation for hierarchical taxonomic reasoning generated by a black-box LLM in a long-tailed biodiversity monitoring pipeline. Using proxy features extracted by an open-source tool LLM, we train lightweight supervised estimators with hierarchy-aware supervision to predict rank-wise correctness. Across three tool LLMs, the supervised estimators consistently outperform a token-likelihood baseline for micro discrimination and selective prediction under a single global rejection threshold, improving micro AUROC from 0.57 to 0.75--0.80. The best results are achieved by a rank-specific multi-head design (H3), suggesting that accounting for hierarchical output structure is important when a unified abstention rule is required. Our code is publicly available at this https URL

---


### 227. [FinixDoc: Rethinking Financial Document Parsing Beyond Saturated Benchmarks](https://arxiv.org/abs/2608.22842)

**<font color=#1a73e8>作者：</font>** Hang Wang, Jin Zhang, Guoliang Xu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial document parsing requires accuracy, structural consistency, and verifiability that current benchmarks often fail to reflect. We present FinixDoc, an end-to-end agentic parsing system for real-world financial documents, with FinixDoc-VL, a 4B-scale vision-language model built on Qwen3-VL-4B, as its core parser. To characterize the gap between benchmark and deployment performance, we introduce a Document Parsing Capability Matrix organized along two practical axes: visual quality and document scale. Guided by this matrix, FinixDoc-VL is trained with a domain-adapted recipe combining homoglyph-aware contrastive learning and multi-stage reinforcement learning with composite domain-specific rewards. To better leverage our accumulated advantage in low-quality financial-document data and support large-scale, high-quality data production, we further build a human-in-the-loop Data Factory pipeline with confidence-aware expert review. For evaluation, we construct FinixDocBench, a financial-domain evaluation suite covering digital-native, camera-captured, ultra-large-page, and internal-workflow scenarios, with a compliance-reviewed subset released alongside this technical report. On its main subsets, FinixDoc-VL achieves the highest overall score (81.43) among evaluated baselines, outperforming the next-best open-source model by 5.13 points, with the largest gains on internal financial workflows (FinixInner: 84.08 vs. 78.73).

---


### 228. [GSAR: Goal-State-Anchor Rewards for Mobile GUI Agents with Self-Evolving Data Synthesis](https://arxiv.org/abs/2608.22847)

**<font color=#1a73e8>作者：</font>** Long Zhang, Yuhan Chen, Chaoran Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) based GUI agents stand to benefit significantly from online reinforcement learning (RL). However, their training is bottlenecked by two fundamental issues: current data synthesis methods for GUI Agents rely on specific environments and struggle to generate diverse data, while existing evaluators either suffer from limited scalability or provide inaccurate and unreliable reward signals. To overcome these challenges, we introduce GSAR (Goal-State-Anchor Reward), a RL reward framework that supports scalable task generation and delivers reliable reward signals for stable and efficient policy optimization. Our approach features self-evolving data synthesis, which produces multiple environments through task execution and generates diverse tasks and goal states. Complementing this, a state-anchor mechanism automatically annotates task-relevant UI elements in successful goal states as reference anchors. During RL training, these reference anchors provide accurate, scalable reward signals that substantially enhance efficiency. Extensive evaluations demonstrate that our framework achieves over 90% accuracy on offline trajectory verification and performs closest to rule-based methods. Furthermore, agents trained using our reward framework exhibit strong performance on both AndroidWorld and our constructed benchmark, establishing a scalable approach for GUI agent training.

---


### 229. [Your AI, On a Dial: Controlling Investment Bias in LLMs with a Single Neuron](https://arxiv.org/abs/2608.22852)

**<font color=#1a73e8>作者：</font>** Sahong Park, Suhwan Park, Hoyoung Lee 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in investment decision-making, yet prior work shows that they exhibit systematic, model-specific investment preferences. We study whether a model's overall investment stance can be calibrated to a specified direction and strength. We introduce an investment-bias dial, an inference-time intervention on a single neuron that continuously adjusts a model-level decision prior---its overall tendency toward buying or selling---without targeting specific firms or investment attributes. Using matched positive and negative evidence, we evaluate five open-weight LLMs and find that the dial produces monotonic changes in investment stance without modifying prompts or model parameters. At the response level, the dial shifts both investment decisions and the evidential emphasis of generated rationales under identical inputs. In an agentic retrieval setting, the dial also changes what information the model searches for, which evidence it selects, and which evidence is reflected in its final analysis. In a long-context evaluation, the dial maintains stable stance control as context length increases, whereas a matched system-prompt instruction progressively attenuates. We further show that changes in the dial propagate to security rankings and downstream portfolio composition in an exploratory backtest. Overall, our results show that an LLM's aggregate investment stance can be calibrated toward a specified target at inference time.

---


### 230. [Thinking at the Right Size: Amortized Distillation Across Post-Trained LLMs](https://arxiv.org/abs/2608.22854)

**<font color=#1a73e8>作者：</font>** Yan Zhou, Sara Kangaslahti, Jonathan Geuter 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Practical deployment of large language models (LLMs) requires families of post-trained variants---instruction-tuned, reasoning-tuned, and chat-style models---each at multiple sizes to meet diverse latency and memory budgets. Producing each (variant, size) pair independently is prohibitive, so model families typically span only a handful of coarse-grained sizes per post-trained variant. Boomerang distillation (Kangaslahti et al., 2026) reduces this cost along the size axis for base models. Through model size interpolation, it constructs models of intermediate sizes from a single teacher-student pair without additional training. However, it still treats each post-trained variant as a separate object of optimization. We introduce ADAPT---Amortized Distillation Across Post-Trained LLMs---a framework for amortizing distillation across both axes of a model family: size and post-training variant, producing $L \times K$ models for $L$ interpolated sizes across $K$ post-trained variants with a single distillation run. ADAPT combines two components. First, a two-phase distillation procedure constructs post-trained students through pre-training alignment and supervised fine-tuning distillation, enabling smooth size--performance interpolation on generation and reasoning tasks. Second, weight-delta initialization approximates this construction across post-trained variants by transferring the distillation-induced weight change from the base model to students initialized from different post-trained variants. The resulting continuum of interpolated models also enables adaptive model-size selection at inference time, improving the compute--accuracy trade-off for long-form reasoning tasks.

---


### 231. [SAVER: Selective Auditing of Verbal Evidence for Error Recovery in VLM Change Reasoning](https://arxiv.org/abs/2608.22857)

**<font color=#1a73e8>作者：</font>** Youdi Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) frequently fail at visual change reasoning, even when their vision encoders contain sufficient information. We observe that correct VLM outputs tend to contain explicit verbal evidence (object names, colors, spatial locations) that supports the claimed change, while incorrect outputs often lack such evidence. We propose SAVER (Selective Auditing of Verbal Evidence for Error Recovery), a lightweight, rule-based method that parses VLM responses for this evidence and triggers structured reprompting only when evidence is missing or inconsistent. Across three change detection benchmarks and four VLMs, SAVER significantly improves accuracy on tasks where errors stem from the model failing to articulate what it saw (expression failures), with gains up to +25.8% on CLEVR-Change. The evidence patterns can also be generated by an LLM in a single call, matching the hand-tuned gate on CLEVR-Change. Ablation experiments confirm that the evidence gate, not reprompting alone, drives the improvement.

---


### 232. [AgentFlow: A Flow-Centric Policy Language and Framework for Securing LLM Agent Systems](https://arxiv.org/abs/2608.22868)

**<font color=#1a73e8>作者：</font>** Basavesh Ammanaghatta Shivakumar, Swarn Priya, Peng Gao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly read untrusted content, invoke external tools, access private data, and delegate work to other agents. Harm often arises not from a single unsafe action but from the flow of sensitive data across a sequence of otherwise plausible steps. We present AgentFlow, a flow-centric policy language and runtime enforcement model for specifying where data may travel in agent systems. Policies are defined over labeled runtime edges and constrain which tools may receive sensitive fields, which sinks may receive released data, and what authority may cross delegation boundaries. The language supports flow and path rules, task-scoped capabilities, controlled release, and stateful taint semantics. A runtime reference monitor mediates agent actions, and a bounded SMT-based verifier checks safety properties for a structured policy fragment.
We evaluate AgentFlow on multiple agent benchmarks. In our prototype, seven safety properties verify in under 0.5 seconds each, and the verifier catches all seeded unsafe policy variants in our study. On 949 AgentDojo injected cases across four suites, AgentFlow reduces confirmed compromise from 33.0\% to 0.0\% while improving aggregate utility from 46.7\% to 63.3\%. On a 200-case AgentDyn Dailylife benchmark, it reduces confirmed compromise from 73.5\% to 0.0\% while preserving near-baseline utility (44.5\% to 43.5\%). Breadth checks across ASB, InjecAgent, BIPIA, AgentHarm, and MCPTox replays suggest that the configured policies block the benchmark-specified policy-visible attacker flows; in ASB's direct-prompt-injection harness, attack success is 0/1{,}200. These results are preliminary and scoped to the modeled policy-visible agent behaviors and evaluated benchmarks.

---


### 233. [Better Retrieval, Worse Robustness:How Multi-hop RAG Amplifies Upstream ASR Errors](https://arxiv.org/abs/2608.22872)

**<font color=#1a73e8>作者：</font>** Zhenghua Bao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-based applications pass spoken queries through automatic speech recognition (ASR) before any retrieval module, so ASR errors enter the pipeline as a fixed upstream constraint. We empirically test whether two extensions to standard retrieval-augmented generation (RAG), entity-graph linking and iterative reformulation, absorb or amplify these errors. Using four English accents synthesized through neural TTS, we evaluate four RAG configurations on three multi-hop QA benchmarks (HotpotQA, 2WikiMultiHopQA and MuSiQue) against a clean-text oracle. Although the structurally richer configurations generally retain higher absolute F1 under ASR input, both extensions amplify the error: the F1 gap from clean text to the highest-WER accent is 36-67% larger under their combination than under naive dense retrieval, on all three benchmarks. The dominant failure mode is corruption of one or more query entities, accounting for 87-96% of degradation cases on 2WikiMultiHopQA across all four methods. Two lightweight surface-form mitigations leave most of the gap intact, indicating that downstream retrieval structure amplifies remaining entity errors. We release code and data at this https URL .

---


### 234. [The Mask Is Not the Model: Auditing Prefix Invariance in Attention, State-Space, and Hybrid Sequence Models](https://arxiv.org/abs/2608.22876)

**<font color=#1a73e8>作者：</font>** Taebong Kim, Youngsik Hong, Minsik Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We formalize prefix invariance: representations at position t must not depend on future inputs. We give a lightweight audit, two forward passes, no training or gradients, that localizes exactly where causality breaks. Attention-mask inspection is incomplete: leaks can occur via scans or normalization despite correct masks. Across 192 injected-fault trials on eight checkpoints, mask inspection found none, while our audit localized all 192/192, also finding a defect in Zamba2 and Nemotron-H.

---


### 235. [FOVEA: Focused On-Demand Visual Evidence Adaptation for Cache-Friendly Multimodal Speculative Decoding](https://arxiv.org/abs/2608.22883)

**<font color=#1a73e8>作者：</font>** Hengjie Zhu, Dayan Wu, Zihao Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal speculative decoding accelerates vision-language models by allowing a lightweight draft model to propose candidate tokens for parallel verification by a larger target model. Existing methods typically condition the drafter on a fixed visual interface, such as a predefined visual-token budget or a static compressed representation. However, our controlled visual-budget analysis shows that visual demand varies substantially across tasks and decoding stages, which means more visual input is not always beneficial. Actually, insufficient evidence may weaken visual grounding, while excessive context adds overhead and may disrupt drafting. We propose FOVEA (Focused On-demand Visual Evidence Adaptation), a cache-friendly approach that builds a reusable visual memory and dynamically retrieves a bounded subset for a draft state. A cumulative-mass rule determines both how many and which entries are selected. The selected entries are aggregated into a visual readout and fused with the current draft hidden state through a lightweight gated residual correction. Rather than inserting visual tokens into the autoregressive context, the correction modifies only the representation passed to the language-model head. Experiments across multiple vision-language backbones and multimodal benchmarks show that FOVEA improves draft acceptance and end-to-end decoding speed, achieving up to $2.13\times$ speedup over autoregressive decoding. These results demonstrate that state-conditioned evidence retrieval is an effective alternative to reusing a fixed visual representation throughout multimodal generation.

---


### 236. [Predicting the scale limits of social mechanisms in agent societies](https://arxiv.org/abs/2608.22884)

**<font color=#1a73e8>作者：</font>** Zengqing Wu, Chuan Xiao  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Societies of interacting language-model agents offer a controllable and repeatable way to study collective behaviour at scales that would be difficult to test with people. Their scientific value, however, depends on whether a social mechanism that works in a small group still operates when thousands of agents interact, and testing this directly requires costly large-scale runs. Here we introduce an audit that predicts a mechanism's fate as a population grows. It asks how often the mechanism can act, whether agents use the information it supplies, and whether the measurement itself creates apparent scale effects. Controlled experiments show that a single structural term can decide whether reciprocity, consensus or punishment survives scaling. For gossip, the population at which the mechanism fails is set by the reach and lifetime of its messages. In language-model societies, agents respond not only to social information but to how it is expressed: counts and percentages led to different scale behaviour. Predictions made before execution held on third-party code and a second model family, while a failed prediction exposed the boundary of the finding. The audit provides a prospective way to decide which social mechanisms can be interpreted across population scales.

---


### 237. [DRAgent: Discriminative Reasoning Agent for Referring Expression Segmentation](https://arxiv.org/abs/2608.22885)

**<font color=#1a73e8>作者：</font>** Yujie Qi, Luyan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring Expression Segmentation (RES) aims to generate a pixel-level mask for the object specified by a language expression. Recent methods based on multimodal large language models (MLLMs) often rely on one-pass coordinate prediction for visual localization, which serializes continuous spatial locations as discrete text tokens and may lead to localization bias and alignment errors. To address these issues, we propose DRAgent, an MLLM-driven discriminative reasoning (DR) framework for RES. Instead of requiring the MLLM to generate localization coordinates, DRAgent first constructs a detector-generated candidate space and then uses the MLLM as a visual-semantic target discriminator. Specifically, the MLLM performs reliable target selection among potential distractors through a two-stage DR mechanism, which first screens high-recall candidates and then performs instance-wise verification. The selected target box is subsequently used as a spatial prompt for a foundation segmentation model to produce the final pixel-level mask. Furthermore, we construct a self-consistency-filtered reasoning-chain data pipeline for LoRA-based fine-tuning, providing more reliable supervision for enhancing the MLLM's discriminative reasoning capability. Experiments demonstrate that DRAgent achieves competitive performance on RefCOCO, RefCOCO+, and RefCOCOg.

---


### 238. [Proxy reliance in large language model decisions is uncalibrated to predictive evidence](https://arxiv.org/abs/2608.22887)

**<font color=#1a73e8>作者：</font>** Zengqing Wu, Chuan Xiao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are entering decisions in triage and lending, where task-relevant inference must be distinguished from impermissible proxy use. Current audits ask whether decisions change when demographics change. But attributes correlated with a protected group carry predictive value, so a changed decision can be discrimination or sound inference. We measure causal proxy effects in four LLMs on a clinical-ranking task with known ground truth, where the reliance the evidence warrants can be computed exactly and used as the reference. One audit signal yields three verdicts: over-reliance, warranted and under-reliance. Under neutral labels every model relies on proxies with no information. Informative proxies draw all three. Social field names push reliance down, below the reference in one model. Two findings explain this. Reliance severely undertracks the evidence, and social-label suppression is fragile, since in-context examples raise it above zero in every model. Accuracy-based evaluation detects none of this.

---


### 239. [Verification-Guided Specification Synthesis with Large Language Models for Intrusion Detection Rules](https://arxiv.org/abs/2608.22889)

**<font color=#1a73e8>作者：</font>** Kohei Yamamoto, Marie Katsurai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Attacks against Internet-connected IoT devices continue to increase; however, transforming observed attack traffic into deployable intrusion detection system (IDS) rules remains largely a manual process. Recent studies have explored using large language models (LLMs) to generate IDS rules; nonetheless, existing approaches often require auxiliary information beyond observed traffic or generate rules without validating their detection logic against benign traffic. This study presents a verification-guided specification synthesis framework for generating Suricata rules directly from HTTP request traces. Instead of having an LLM generate IDS rules in a single step, an LLM first identifies a vulnerable parameter and synthesizes a semantic detection specification. These specifications are iteratively refined through counterexample-guided inductive synthesis (CEGIS), in which benign traffic samples serve as counterexamples during synthesis and verification. Verified specifications are then deterministically compiled into Suricata rules. Experiments on 281 real-world CVEs and benign traffic collected from real IoT devices show that the proposed method achieves a detection rate of 81.5% while maintaining a false positive rate of 0.0%. An ablation study also demonstrates that CEGIS-based verification improves detection performance while maintaining a low false positive rate.

---


### 240. [AraDetox: A Multi-Dialect Arabic Detoxification Dataset](https://arxiv.org/abs/2608.22894)

**<font color=#1a73e8>作者：</font>** Mo El-Haj  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Arabic harmful-language detection has received considerable attention, yet Arabic text detoxification remains underexplored. We introduce AraDetox, a multi-dialect Arabic detoxification dataset comprising 10,500 harmful social-media posts and 84,000 detoxified rewrites generated using GPT-5 and Gemini 2.5 Flash across Modern Standard Arabic, Gulf, Levantine, and Egyptian Arabic. The generated outputs were assessed through human evaluation and automatic analyses of lexical change, semantic preservation, sentiment, and dialectal style. Results show that detoxification is primarily a meaning-preserving rewriting task: substantial lexical and structural reformulation is accompanied by consistently high semantic similarity. Human evaluation confirms successful harmful-language removal while largely preserving the original meaning. Dialectal analyses further indicate that the generated variants exhibit measurable stylistic alignment with reference Arabic dialect corpora. Comparison with existing resources highlights two complementary approaches to detoxification: minimal-edit lexical substitution and meaning-preserving reformulation. Our findings demonstrate that large-scale Arabic detoxification resources can be constructed through LLM-assisted generation and human verification. The dataset is publicly available at this https URL to support future research on Arabic detoxification, safe text generation, and multi-dialect Arabic NLP.

---


### 241. [SelFusion: Self-distillation for Diffusion Language Models](https://arxiv.org/abs/2608.22898)

**<font color=#1a73e8>作者：</font>** Hyeongsoo Lim, Jinyoung Kim, Eunseo Seo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) alleviate the inherent latency bottleneck of autoregressive (AR) large language models (LLMs), but their degraded generation quality limits practical applicability. Although knowledge distillation (KD) can be a promising direction for improving performance, we empirically find that naively applying conventional KD yields only marginal gains, or even degrades generation quality. Based on these observations, we propose a novel self-distillation framework for DLMs, namely SelFusion. To enable effective KD without an external teacher model, SelFusion performs two forward passes with different masking levels, defining the hard mode with a larger masking probability and the easy mode with a smaller masking probability. However, the easy mode is not always more accurate than the hard mode and can be overconfident on incorrect tokens. Thus, we introduce bidirectional KD between the two modes, which can dynamically determine the distillation direction based on token-level correctness. Experimental results on instruction-following tasks show that the proposed self-distillation substantially outperforms other KD methods with external LLM and DLM teachers. In many configurations, the student trained with SelFusion even surpasses the performance of the LLM teacher, providing a practical path toward improving DLM generation quality. Source code can be found at this https URL

---


### 242. [Do Spoken Language Models Hear Speech as They Read Text? Bridging Structural Gaps Between Speech and Text](https://arxiv.org/abs/2608.22908)

**<font color=#1a73e8>作者：</font>** Hyeonyu Kim, Hwayeon Kim, Youngwon Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spoken Language Models (SLMs) generate textual responses directly from speech, offering an alternative to cascaded systems. Despite recent advances, existing SLMs still exhibit weaker instruction-following behavior and limited generalization across diverse tasks compared to text-based language models. Our analysis shows that speech and text representations in current SLMs remain weakly aligned despite strong downstream performance, indicating that structural differences between continuous, temporally varying speech and discrete text remain insufficiently addressed. To address this, we propose a simple framework that decouples length mismatch from semantic alignment and encourages closer correspondence between speech and text representations. Experiments across multiple benchmarks demonstrate competitive performance against strong baselines, underscoring the importance of explicitly addressing structural differences between speech and text in SLM training. Our code is publicly available at this https URL.

---


### 243. [Safety Hacking in Constrained Best-of-$N$ Inference-time Scaling](https://arxiv.org/abs/2608.22915)

**<font color=#1a73e8>作者：</font>** Akifumi Wachi, Takumi Tanabe, Youhei Akimoto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-time pipelines often sample multiple outputs, filter them with a learned safety model, and return the proxy-feasible output with the highest learned reward. We show that this composition creates a two-stage failure: an imperfect safety proxy first contaminates the feasible set with unsafe outputs, and reward maximization can then amplify this residual contamination. We define \emph{safety hacking} as selecting an output that passes the learned constraint but violates the true safety criterion. For constrained Best-of-$N$ sampling, we derive finite-$N$ bounds governed by the joint upper reward tails of safe and unsafe outputs within the proxy-feasible set. If unsafe-but-feasible outputs have the heavier tail, safety hacking becomes asymptotically certain as $N$ grows, even when false-positive mass and average safety- and reward-proxy errors are arbitrarily small. We also show that policies within a bounded $\chi^2$ divergence from the proxy-feasible reference distribution admit an $N$-independent safety-hacking bound, and instantiate this general coverage-control principle with constrained pessimistic sampling. Coverage control limits amplification but cannot repair a contaminated feasible set: admitted unsafe outputs may still be favored, and regularized selection is not necessarily safer than constrained Best-of-$N$ for every reward proxy. Toy and language-model experiments characterize both contamination and its reward-tail amplification, which exposes an inherent difficulty in inference-time scaling with learned safety models.

---


### 244. [Knowing Isn't Always Saying: When Do Spatial Encodings Reach Answers in Vision-Language Models?](https://arxiv.org/abs/2608.22916)

**<font color=#1a73e8>作者：</font>** Zeyu Wang, Xinming Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models are known to encode spatial information in their hidden states, yet often fail to use it when answering. However, it remains unclear when and where this encoded information reaches the answer. We address this with direction patching, a class-conditioned causal intervention applied across layers, token positions, and prompt formats. Using spatial-ID directions constructed following prior encoding evidence, we find that causal influence on answer logits emerges only at mid-to-deep depths. Text chain-of-thought suppresses immediate object-word argmax-level transport in most models, while visually grounded prompts keep it open. Positive target-logit gain can remain below the argmax threshold, and transport can re-emerge at the final prefix token or at the answer step in deeper layers. Across the ten VLMs we study, these local effects form descriptive transport patterns. Complementary experiments characterize how these patterns shift across datasets, attributes, and encoding amplitudes. Together, these results reframe the encoding-grounding gap as a problem of conditional transport in VLMs.

---


### 245. [TSWAP: A Multilingual Retrieval-Augmented Thai Wellness Advisor](https://arxiv.org/abs/2608.22917)

**<font color=#1a73e8>作者：</font>** Pornthep Ukosaramig, Kobkrit Viriyayudhakorn  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present TSWAP, a deployed eight-language conversational wellness advisor grounded, via retrieval-augmented generation, in a verified knowledge base of Thai traditional medicine and certified wellness providers. An unmodified open-weight LLM (Qwen3.6-35B-A3B on vLLM) is grounded on a ~30.6K-chunk Thai index by a hybrid dense-sparse retriever with cross-encoder reranking; a first-turn query classifier forces tool-based retrieval for entity lookups; a rule-based safety layer enforces medical scope and Thai emergency routing; and all eight languages are served zero-shot with translate-then-retrieve. We release the first Thai traditional-medicine/wellness retrieval benchmark (50 questions with gold document IDs; Recall@5 = 0.88), production QA logs (91.1% test-retest pass over 259 cases), and a 71-question frontier no-retrieval probe showing what each grounding pillar contributes: without the safety prompt the backend model family produced a full drug-dosing schedule and complied with out-of-scope requests, and without the knowledge base it produced zero verifiable provider recommendations. We further report two transferable deployment findings: English-calibrated 4-bit AWQ quantization corrupts Thai tone marks, and forced-retrieval routing is necessary for reliable grounding.

---


### 246. [HelaBERT: Enhancing Sinhala Language Understanding with Dual Pooling Classification Head](https://arxiv.org/abs/2608.22922)

**<font color=#1a73e8>作者：</font>** Thisen Ekanayake, Nisansa de Silva  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present HelaBERT, a family of two BERT-based masked language models pre-trained from scratch on approximately 1 billion tokens of Sinhala text sourced from MADLAD-400, CulturaX, and a custom corpus comprising news articles, Sinhala Wikipedia, and web crawl data. HelaBERT-Small (~23.3M parameters, 6 layers) and HelaBERT-Large (~110M parameters, 12 layers) both use a SentencePiece Unigram tokenizer (vocabulary size 32,000) tailored to Sinhala's agglutinative morphology and complex script. We evaluate both models on four downstream Sinhala text classification tasks: news category classification, news source classification, sentiment analysis, and writing style classification, using 5 independent seed runs with stratified 80/20 train/test splits. We additionally propose a dual pooling classification head and evaluate it systematically across all four tasks, finding consistent improvements on sentiment analysis and a moderate gain on news category classification for HelaBERT-Small, while the standard [CLS]-linear head remains competitive on news source classification, a headline-level task with short average input length. We release both models to support further research in Sinhala NLP.

---


### 247. [Motion-Based Tokenization for Cross-Dataset Egocentric Gaze Modeling](https://arxiv.org/abs/2608.22926)

**<font color=#1a73e8>作者：</font>** Virmarie Maquiling, Zhuojiang Cai, Enkelejda Kasneci  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaze is increasingly used as an input signal for vision and multimodal models, yet no consensus exists on how to represent it across datasets. Raw traces preserve detail but are noisy and device-dependent, while coarse event labels are easy to model but can discard local motion structure. We formulate event-aligned, fixed-horizon angular displacement as an interpretable, event-conditioned motion vocabulary and compare it with event-only, spatial, absolute-angle, learned vector-quantized, and continuous representations. To assess transfer alongside target predictability and token collapse, our evaluation combines next-token prediction with target-domain regret, low-order target references, paired bootstrap, order sensitivity, motif overlap, and frozen structural probes. In an event-aligned headset benchmark, angular-motion tokens have lower target-domain regret than frozen-codebook VQ tokens in one transfer direction, while the reverse direction is inconclusive. The probes reveal complementary representation properties, and event-only tokens show that low perplexity can retain little motion information. On a third egocentric dataset, a matched comparison of I-VT, native, and frame-span interfaces shows that event construction materially changes transfer: native events have the lowest regret into EGTEA, while frame-span events have zero motif overlap and fail severely as a source. Motion-based tokenization therefore provides a compact representation for event-aligned egocentric gaze streams, while the evaluation identifies how target predictability and event construction shape cross-dataset conclusions.

---


### 248. [Concepts for Securing Agentic AI Coding and the Terok Environment](https://arxiv.org/abs/2608.22930)

**<font color=#1a73e8>作者：</font>** Jiří Vyskočil, Franz Pöschel, Andreas Knüpfer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI is a fascinating new tool for software development. It is a huge step forward compared to "conventional" AI assisted coding, which in turn was a considerable breakthrough earlier. AI support through LLMs is a young and very fast-moving field. The "conventional" (non-agentic) flavor became useful and productive in early 2025 (around 18 months ago) and the agentic flavor followed in fall 2025 (approximately 9 months ago). Besides all its benefits and potential, it also carries some fundamental risks for IT security. And the agentic approach added very severe risks while making others much more dangerous.
With all the motivation to explore this fascinating new tool we should not ignore the risks but actively address them. We present (I) an assessment of the IT security risks, (II) a concept for mitigating them without breaking its benefits, and (III) an overview about an implementation of our concept. In this very dynamic field this is likely not the final and once-and-for-all answer to the identified issues but still a substantial step forward in responsible usage of Agentic AI for software development. It should also be a contribution to the community to allow early and eager evaluation of the potential of agentic AI for software development without actually suffering from its implied IT security risks.

---


### 249. [What Proves You Wrong: Benchmarking Language Models on Falsifiable Research Ideation](https://arxiv.org/abs/2608.22948)

**<font color=#1a73e8>作者：</font>** Ziyue Wang, Aomufei Yuan, Yiran Yao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to propose research ideas, yet the prevailing ways of judging such ideas supply no shared decision rule: free-form judging sways with style and position, and scoring against a later paper rewards recovery of one realized trajectory. We introduce a benchmark that carries a proposal from Literature to Test: the Lit2Test benchmark centers on a six-field contract organized around a falsifying outcome, so that every proposal precommits the observation that would prove it wrong, making its quality decidable in the first place rather than merely arguable. Built prospectively from 200 real-paper neighborhoods, Lit2Test elicits proposals from four frontier models and compares them through 1,200 pairwise comparisons judged blind in both presentation orders. The protocol audits its own reliability through diagnostic controls and bounded human calibration, with three annotators corroborating the conclusions within explicitly stated reliability bounds. Lit2Test recovers a strict ranking of the four models in all 10,000 bootstrap replicates, and the separation comes from the quality of the proposed tests and metrics rather than from surface fluency. We release the benchmark, construction pipeline, and audit artifacts for public use.

---


### 250. [WADE: A Reasoning-Annotated Benchmark for Multi-Instance Floating-Waste Grounding with Compact Vision-Language Models](https://arxiv.org/abs/2608.22950)

**<font color=#1a73e8>作者：</font>** Md. Asaduzzaman Shuvo, Ahsan Farabi, Md. Abdul Ahad Minhaz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Floating waste in inland waterways threatens aquatic ecosystems and requires timely monitoring under cluttered, multi-object conditions. Existing aquatic-waste datasets provide limited geographic coverage, sparse multi-instance annotations, and little supervision beyond boxes and labels. Compact vision-language models (VLMs) therefore remain insufficiently evaluated for jointly localizing, classifying, counting, and explaining floating waste. We introduce WADE, a reasoning-annotated benchmark containing 2,167 images from rural Bangladesh, 13,608 bounding boxes, and ten waste categories. Each annotation is associated with class-level recognition rules covering visual cues, likely confusions, and discriminative features. We evaluate six VLMs under zero-shot, two-shot, reasoning-guided, and fine-tuned settings using detection, counting, and hallucination metrics. For resource-efficient adaptation, we jointly fine-tune Qwen3-VL-2B on boxes, labels, and reasoning chains using QLoRA. Fine-tuning increases recall from 0.0248 to 0.2339 and F1 from 0.0257 to 0.2163, while reducing image-level hallucination from 0.6836 to 0.0883. However, over three-quarters of instances remain undetected, establishing WADE as a challenging benchmark for dense floating-waste grounding with compact VLMs.

---


> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-363](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
