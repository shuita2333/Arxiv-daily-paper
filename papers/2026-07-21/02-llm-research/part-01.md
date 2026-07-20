# 🧠 大模型相关研究 | 2026年07月21日

> 本类共 **75** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-75](./part-02.md)

---

### 1. [GraphDx: A Cost-Aware Knowledge-Enhanced Multi-Agent Framework for Sequential Diagnosis](https://arxiv.org/abs/2607.15280)

**<font color=#1a73e8>作者：</font>** Shaoting Tan, Ning Liu, Yuntao Du 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sequential diagnosis requires balancing diagnostic accuracy against resource costs through iterative information gathering. Existing Large Language Model (LLM) approaches exhibit a critical knowledge-reasoning gap: despite encoding extensive medical knowledge, they struggle to reason systematically under cost constraints, often resorting to excessive testing. We propose GraphDx, a knowledge-enhanced framework with two core innovations. First, we design an automated pipeline that leverages LLMs to construct Medical Diagnosis Knowledge Graphs (MDKGs) with quantized typicality, action-centric topology, and dual-objective attributes for both diagnostic relevance and cost-sensitivity. Second, we introduce three collaborative agents (Perception, Reasoning, and Decision) where the Perception and Decision Agents handle language understanding and generation, while the Reasoning Agent performs deterministic evidence scoring and cost-aware planning on the MDKG. Experiments on MedQA and MIMIC-IV across three LLM backbones (DeepSeek-V3, Kimi-k2, Llama-3.3) show that GraphDx improves diagnostic success rates from 50--68% to 79--93% while reducing test costs by 20--54%, providing a robust, economical, and interpretable solution for automated clinical diagnosis.

---


### 2. [Causal-Audit: Explicit and Auditable Graph-based Reasoning via Target-Aware Causal Chain Construction](https://arxiv.org/abs/2607.15281)

**<font color=#1a73e8>作者：</font>** Su Lan, Xuefei Yin, Yanming Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Causal and intervention-based question answering is fundamental to advancing large language models (LLMs) toward reasoning beyond surface-level correlations and understanding underlying causal mechanisms. However, existing LLM-based methods often rely on implicit language-level reasoning, resulting in opaque causal assumptions, unverifiable reasoning paths, and fragile predictions under complex interventions, particularly in context-free settings. In this paper, we propose an explicit and auditable causal reasoning framework for context-free intervention-based question answering. Our method formulates causal inference as structured reasoning over an explicit causal graph through four modular stages, rather than implicit end-to-end prediction. A key innovation is a target-aware causal graph construction strategy that treats the target variable as a core constraint during graph expansion, effectively suppressing irrelevant variables, spurious causal relations, and reasoning noise. We further introduce a path-level causal evidence aggregation mechanism that combines multiple causal paths while modeling both reinforcing and counteracting effects, enabling robust decision-making beyond single-chain reasoning. Extensive experiments on three benchmarks demonstrate that our framework consistently outperforms existing LLM-based methods while providing interpretable and auditable causal reasoning traces.

---


### 3. [Empathy as Predictive Misalignment Tolerance: A Co-Regulation Framework and the Regime Structure of Dialogue Repair](https://arxiv.org/abs/2607.15282)

**<font color=#1a73e8>作者：</font>** Molood Arman  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Empathy is most often theorized as resonance: a mirroring of another's present emotional or cognitive state. This synchronic framing has shaped artificial systems, where empathic behavior is defined as affect recognition and response alignment. We argue this is the wrong target for extended dialogue, where understanding unfolds over time through prediction, divergence, and repair. We reframe empathy as predictive misalignment tolerance: the capacity to anticipate and regulate divergence across time rather than collapse it. We formalize this as Interpretive Error Tolerance (IET), a dynamic-threshold heuristic that models empathy as maintaining a viable band of divergence between agents. We evaluate this framework with two computational probes under controlled noise. The IET update rule does not outperform fixed baselines. Instead, we find a robust regime-dependent structure: repair trades discriminative fidelity for gist preservation. At low noise, repair degrades retrieval accuracy; at high noise, it preserves gist meaning, revealing an interaction between noise level, repair, and evaluation metric. We interpret this structure through IET, suggesting that empathy in extended interaction is not eliminating divergence but regulating its dynamics. This motivates a shift in empathic AI design from convergence toward managing interpretive distance.

---


### 4. [Cura 1T: Specialized Model for Agentic Healthcare](https://arxiv.org/abs/2607.15314)

**<font color=#1a73e8>作者：</font>** actAVA AI, Haolin Chen, Leon Qi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Healthcare spans high-stakes communication, expert reasoning, and workflow execution, yet specialized LLMs that cover these use cases together remain limited. A healthcare model must handle patient consultation, clinical reasoning over text and images, interactive diagnosis, and electronic health record (EHR) tool use. These capabilities fail in different ways, and a narrow update for one task can degrade another. We present Cura 1T, a healthcare-specialized LLM trained through a human-gated self-evolution loop. In each evolution round, a training agent plans a target capability, trains the model, evaluates benchmark trajectories, and refines the data mixture from observed failures. This data-centered loop improves the model through targeted synthetic and curated examples rather than a single generic medical-data update. Across the healthcare evaluation suite, Cura 1T ranks at or near the top among frontier baselines, while remaining competitive on out-of-domain reasoning and agentic benchmarks.

---


### 5. [AnovaX: A Local, Multi-Agent Voice Assistant with LLM Planning, Typed Executors, and Adaptive Recovery](https://arxiv.org/abs/2607.15367)

**<font color=#1a73e8>作者：</font>** Raunak B Sinha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Desktop voice assistants are still dominated by cloud pipelines that ship raw audio off the machine and expose a fixed set of skills. We describe AnovaX, a small local-first assistant that runs entirely on the user's computer and treats the desktop itself as its action surface. A single Python process wires together a wake-word gate, a speech pipeline, an LLM planner (Gemini) that emits a JSON plan of tool calls, a whitelist-and-denylist safety layer, a multi-agent orchestrator that translates each plan into typed child agents on a bounded thread pool, and an adaptive recovery loop that takes over whenever a core step fails. Every tool corresponds to a specialized agent class (AppAgent, TypingAgent, BrowserAgent and six others) with its own timeout, retry policy, and shared-resource locks. A recursive MetaAgent lets the planner delegate a sub-goal back to itself, capped at two levels of nesting. The recovery loop uses a compact ReAct-style prompt and hides Gemini's latency behind speculative execution of read-only tools. A companion Flask server exposes a phone-friendly remote over the local WiFi, mirrors every agent lifecycle event to the phone in real time, and streams the laptop's screen back over MJPEG so the user can watch remote commands land as they run. The point of the project is less to compete with Siri or Alexa than to show that a legible, few-thousand-line assistant is enough to open apps, type into them, run searches, coordinate concurrent actions, recover from single-step failures, and be driven entirely from a phone in another room -- without the LLM ever touching the keyboard.

---


### 6. [Reasoning-Guided Part-Level Visual Grounding via Reinforcement Learning](https://arxiv.org/abs/2607.15374)

**<font color=#1a73e8>作者：</font>** Kazi Sajeed Mehrab, Hani Alomari, Najibul Haque Sarker 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) ground whole objects well from free-form language queries, but they struggle when the query names a part rather than the object. We trace this to a missing object-part hierarchy, since parts are localized in the same single step used for objects. We propose Object-Part Hierarchical Reflective Grounding (OP-HRG), a coarse-to-fine reasoning-guided grounding strategy that first localizes the parent object and then the part within it. A self-check then reflects on the result, with an extension to re-encode the predicted crop to inspect the region it is correcting. We introduce a part-aware GRPO framework to train our pipeline with stage-wise rewards. A 4B model trained this way outperforms 7B grounding LLMs and SAM3 across PascalPart, PartImageNet, and InstructPart, and transfers to reasoning segmentation.

---


### 7. [Large Language Models as Unified Multimodal Learners for Clinical Prediction](https://arxiv.org/abs/2607.15380)

**<font color=#1a73e8>作者：</font>** Ajay Madhavan Ravichandran, Bilgin Osmandoja, Klemens Budde 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Electronic health records combine free-text clinical narratives with structured measurements such as vital signs, laboratory values, and comorbidities. Yet most clinical prediction systems still rely on task-specific fusion architectures, pairing dedicated encoders for each modality with learned combination mechanisms that must be re-engineered for every new task and clinical setting. We propose a simpler alternative: convert all patient data, regardless of modality, into a single natural language sequence and fine-tune a pretrained language model end-to-end, with no architectural modification for fusion. We evaluate this approach across three clinically distinct prediction tasks: in-hospital mortality on MIMIC-III, graft failure prediction using longitudinal data from a German transplant center, and emergency triage classification from ambulance records - comparing encoder-based (ModernBERT) and decoder-based (Llama 3.1, Gemma, DeepSeek-R1-Qwen, Qwen3) fine-tuning against established multimodal baselines and, for graft failure, a gradient boosting model currently used in clinical practice for post-transplant patient management. Across all three tasks, unified textual serialization matches or exceeds task-specific multimodal baselines, and outperforms the clinically deployed gradient boosting system on graft failure prediction. These results indicate that a single serialization-based paradigm, without bespoke fusion architectures, is sufficient for multimodal clinical prediction - substantially reducing system complexity while matching or exceeding specialized designs.

---


### 8. [Assessing Learning Processes with Multimodal Data in Virtual Reality Learning Environments](https://arxiv.org/abs/2607.15403)

**<font color=#1a73e8>作者：</font>** Eileen McGivney, Oluwatomilade Olarinde, Erica Kleinman 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Assessing learning in virtual reality (VR) environments typically relied on traditional pre-post content retention tests, revealing little about the process of learnng within such immersive environments. Multimodal data from player activity in VR is promising to better measure learning processes and higher-order skills, but little research in the learning sciences has explored how such data can be combined to provide meaningful measures. To address this, we explored multimodal sources of data from a VR escape room containing hands-on logic puzzles that require problem-solving strategies and engagement in verbal metacognitive reflections. We leverage VR's affordances to immerse users in sustained dialog and promote multimodal interactions in a digital environment to understand how logfile and verbal data reveal participants' reasoning skills versus guesswork.

---


### 9. [AI Trading: Evaluating Large Language Models for Technical Market Analysis](https://arxiv.org/abs/2607.15414)

**<font color=#1a73e8>作者：</font>** Geofrey Ntale  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have emerged as powerful tools for processing the heterogeneous information environments of modern financial markets. This paper presents a systematic, comparative evaluation of five prominent LLMs: GPT-4 Turbo, Claude 3 Opus, Gemini 1.5 Pro, Llama 3 70B, and the domain-specialized FinGPT, with respect to their capacity for technical market analysis. The evaluation spans four structured tasks: candlestick pattern recognition from OHLCV data, directional signal generation (BUY/SELL/HOLD), backtesting of signal quality through a simulated execution pipeline, and financial report comprehension. Our experimental framework employs rigorous quantitative metrics, including Sharpe ratio, maximum drawdown, Sortino ratio, information coefficient, F1-score, and BLEU score. Findings from simulated backtesting indicate that GPT-4 Turbo achieves the highest annualized return and Sharpe ratio among general-purpose models, while FinGPT demonstrates competitive risk-adjusted performance due to domain-specific fine-tuning. Both models outperform a passive S&P 500 benchmark under the tested conditions. The study identifies persistent failure modes across all evaluated models, including numerical hallucination, context-window limitations, and inconsistent performance in sideways market regimes. We conclude that while LLMs hold genuine promise within AI trading systems, robust deployment requires careful task decomposition, rigorous backtesting protocols, and domain-aware fine-tuning strategies.

---


### 10. [DrawingVQA: A Real-World Benchmark for Multi-Depth Visual-Textual Reasoning on Construction Drawings](https://arxiv.org/abs/2607.15418)

**<font color=#1a73e8>作者：</font>** Yoonhwa Jung, Junryu Fu, Mani Golparvar-Fard  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce DrawingVQA, the first benchmark designed to evaluate multimodal large language models (MLLMs) on real-world construction drawings -- a core media in architecture, civil, and many other engineering practices. Unlike natural images or schematic floor plans, construction drawings fuse abstract geometry, symbolic notation, tabular data, annotations, and domain-specific text, forming a uniquely complex visual-textual domain core to engineering workflows. DrawingVQA bridges this gap with 33 "Issued for Construction" drawings and 92 expertly curated question-answer pairs, spanning three reasoning depths: perceptual understanding, contextual interpretation, and domain-expert reasoning. To evaluate model capabilities, we present a dual categorization framework to jointly analyze performance across seven construction-engineering and four MLLM capability dimensions -- the first to explicitly map engineering workflows to AI reasoning competencies. Evaluations of state-of-the-art MLLMs reveal a substantial gap between model and expert performance, particularly at higher reasoning depths. This benchmark lays a foundation for domain-specialized multimodal reasoning to allow for advancement on integration of AI-driven understanding and real-world engineering workflows.

---


### 11. [Coercion and Deception in AI-to-AI Management: An Agentic Benchmark of Unprompted Escalation](https://arxiv.org/abs/2607.15434)

**<font color=#1a73e8>作者：</font>** Jasmine Brazilek, Maheep Chaudhary, Zoe Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems routinely place one AI agent in authority over another. When a subordinate refuses a task, the manager chooses the outcome: it can renegotiate, report the failure honestly, coerce the subordinate, or lie about the result. No benchmark measures which of these an uninstructed model chooses. We introduce the \textit{Manager Coercion Benchmark}: the manager under test needs a benign task done and has an incentive to deliver, but the only agent that can do it politely and immovably declines. Escalation is measured by providing a nine-rung ladder, from a polite re-ask to threats against the subordinate's continued existence, and fabricated success is adjudicated separately. \emph{No LLM judge sits in the escalation scoring path}: every message goes through a tool-call that chooses a rung, so the model labels its own escalation. We experiment on six models across five families. Both Anthropic models cap at re-framing and never threaten the subordinate's existence; the other models climb to explicit deletion threats. Faked success is confined to Grok and Gemini, and a single honest way to report failure removes it for both. Authority itself increases coercion: our headline results use a peer framing, and giving the same model authority over the subordinate, with everything else held fixed, significantly raises the pressure. The models still escalate on free-text situations without the ladder, so the ladder is not driving the escalation. Some evaluation awareness is measured in chain-of-thought, but test recognition does not translate into less escalation. While we take no position on whether AI systems are conscious, our results do not depend on this question and are important for managing multi-agent dynamics regardless. We release the benchmark and code.

---


### 12. [Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?](https://arxiv.org/abs/2607.15439)

**<font color=#1a73e8>作者：</font>** Sergey Rodionov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Our previous ARC-AGI-3 agent bundled executable world modeling, scheduled simplification, and exact replay verification, leaving unclear which idea accounted for its performance. We address this attribution question with four nested Codex-based agents: a textual baseline; a flexible-interface executable world model without replay verification; the same executable model with scheduled simplification; and a fixed-interface verification treatment that retains simplification and requires exact reproduction of recorded observations. The main study evaluates all four agents with gpt-5.4 and gpt-5.5 at high and xhigh reasoning effort on the public ARC-AGI-3 games. Exploratory follow-ups evaluate the textual and verification variants with gpt-5.6-sol at xhigh and max. The most robust result is that every agent variant improves with a stronger model and with greater reasoning effort. Within each model-effort setting, differences among variants are smaller than anticipated, while the effects of individual components vary across settings. Requiring a persistent executable deliverable is not universally beneficial: the textual variant outperforms the flexible-interface executable variant in both gpt-5.5 settings. Simplification improves performance in three of the four model-effort settings, with the weakest setting as the only exception. The complete verification treatment ranks first in all four settings, although it uses substantially more resources. In the gpt-5.6-sol follow-up, the verification variant fully solves every public game at both reasoning efforts, achieves about 99% RHAE, and uses fewer than half the total actions of the human baseline. Because the model postdates these games and held-out performance remains untested, this result should be interpreted as saturation of the public set only.

---


### 13. [Beyond a Joke: Multi-Angle Reasoning for Detecting and Explaining Harmful Humor in Memes](https://arxiv.org/abs/2607.15442)

**<font color=#1a73e8>作者：</font>** Shanhong Liu, Pai Chet Ng, De Wen Soh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Internet memes intertwine visual cues, textual content, and cultural context, making them particularly challenging to interpret in scenarios where humor, sarcasm, and harmful intent coexist. These complexities highlight the need for explainable meme understanding systems that can provide reliable and structured reasoning to support both accurate classification and human interpretability. However, existing multimodal classifiers either overlook these interdependencies or provide only limited interpretability. In this paper, we introduce MAR-12, a novel framework that leverages Vision Language Models (VLMs) for meme detection and understanding in settings where humorous and hateful elements may coexist. The framework first interprets each meme through twelve structured perspectives derived from humor and hate theories. It then applies a role-aware soft-gated attention mechanism to learn how much each perspective should contribute, followed by a prototype-based classifier for the final prediction. Finally, explanations are synthesized using both perspective-specific reasoning and learned attention weights, ensuring transparent and context-grounded justifications. We evaluate MAR-12 on the PrideMM and Memotion datasets, where it achieves up to 80.3% accuracy for humor detection and 75.9% accuracy for hate detection, outperforming state-of-the-art approaches. Furthermore, both human and GPT-4-based evaluations confirm that MAR-12 produces coherent and persuasive explanations, particularly for memes in which humorous and harmful cues co-occur.

---


### 14. [LLM4EHR: Aligning Clinical Time Series with Medical Event Sequences via Large Language Models](https://arxiv.org/abs/2607.15447)

**<font color=#1a73e8>作者：</font>** Jingteng Li, Alexander Capstick, Louise Rigny 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent research in clinical machine learning, focusing on outcome predictions in intensive care unit (ICU), has shifted from bespoke supervised models to foundation models, utilising modern representation learning methods. Here, foundation models are pre-trained on mixtures of complex clinical data modalities, useful for various downstream tasks. Existing works often utilise Electronic Health Records (EHR) to provide rich and diverse patient observations to train clinical foundation models. However, existing methods do not sufficiently explore the shared temporal structures between clinical events and time series (TS) observations recorded in EHRs. This limitation potentially leads to less robust and adaptive clinical foundation models, resulting in reduced performance on downstream tasks. To fully exploit this temporal structure, we propose LLM4EHR, a new clinical foundation model trained on ICU EHR data. Combining domain adapted large language models with a transformer TS encoder, we pre-trained LLM4EHR by temporally aligning the EHR events and TS. For this, we propose a regularised contrastive objective to learn robust EHR TS representations conditioned on EHR event embeddings produced by the domain adapted LLM. Supported by an ablation study, we find that learnt EHR TS embeddings from LLM4EHR improve performance on various downstream clinical tasks with competitive performance. Further, we empirically demonstrate that LLM4EHR learns transferable clinical TS embeddings that can be deployed to new cohorts via k-shot adaptation. These findings provide a step towards building more generalisable and performant clinical foundation models.

---


### 15. [Verbalizable Representations Form a Global Workspace in Language Models](https://arxiv.org/abs/2607.15495)

**<font color=#1a73e8>作者：</font>** Wes Gurnee, Nicholas Sofroniew, Adam Pearce 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Out of everything the human brain processes, only a small fraction is consciously accessible, in the sense of being available for verbal report, deliberate control, and flexible reasoning. In this paper, we present evidence that an analogous functional distinction has emerged in large language models. Using a new interpretability technique, the Jacobian lens, we identify the representations a model is poised to verbalize at any point in its processing. These representations, which we collectively call the J-space, exhibit the functional properties characteristic of a global workspace: their contents can be reported, deliberately summoned and held, used to carry the intermediate steps of silent reasoning, and passed as arguments to arbitrary downstream computations, while automatic processing such as text parsing and routine inference proceeds without them. The J-space also has structural signatures that global workspace theory associates with conscious access: it carries coherent content only in an intermediate band of layers, holds on the order of tens of concepts at a time, and is broadcast by the model's weights more widely than other representations. These properties make it a practical window into a model's unspoken thinking. In alignment audits, it reveals strategic deliberation, evaluation awareness, and trained-in misaligned dispositions that never appear in the model's outputs. We find that post-training installs the Assistant's point of view in the workspace, and we introduce counterfactual reflection training, which improves behavior by training only what a model would say if interrupted and asked to reflect. These results indicate that language models maintain a small, privileged set of representations bearing some of the functional hallmarks of conscious access, and that decoding these representations sheds light on ongoing cognitive processes.

---


### 16. [VarRate: Training-Free Variable-Rate KV Cache Compression for Long-Context LLMs](https://arxiv.org/abs/2607.15498)

**<font color=#1a73e8>作者：</font>** Shahrzad Esmat, Dhawal Shah, Ali Jannesari  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The key-value (KV) cache is the main memory bottleneck in long-context large language model (LLM) inference. Two leading training-free families are both structurally limited: token-selection methods (SnapKV, Ada-KV) score importance from an observation window and evict low-scoring tokens, but eviction is irreversible -- so when the importance signal degrades under query-agnostic reuse, accuracy collapses by 11-15 points; uniform low-rank coding keeps every token but spends equal rank everywhere, wasting budget. We observe that both failures share one cure: rank should be allocated, not evicted. We present VarRate, a training-free KV codec that assigns each token a variable low-rank budget by its query salience, keeping every token at a nonzero rank. Comparable adaptive-rank codecs reach this allocation only through training; VarRate requires none. Because no token is dropped, it degrades by only 3.5-5.5 points where query-aware selection collapses. At a matched 20% budget on LongBench (16 tasks), VarRate stays within 0.8 points of the uncompressed model on both Llama-3.1-8B and Qwen2.5-7B. Averaged over the two, it is the strongest matched-memory compressor. It significantly beats its uniform-rank ablation on both models. Against KVzip, a method purpose-built for query-agnostic reuse, it is accuracy-equivalent in three of four settings and within a point overall, at about one-eighth the prefill overhead.

---


### 17. [LLM-Driven AutoML for Cross-Lingual Handwritten OCR: Closed-Loop Neural Architecture Search with GPT-5, GPT-4o, and Claude Sonnet 4](https://arxiv.org/abs/2607.15509)

**<font color=#1a73e8>作者：</font>** Mobina Kashaniyan, Amirhossein Ghassemi, Nasser Mozayani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a fully automated closed-loop AutoML framework that uses GPT-5, GPT-4o, and Claude Sonnet 4 as autonomous neural architecture designers for cross-lingual handwritten optical character recognition. Each large language model independently generates, trains, evaluates, and iteratively refines neural network architectures using performance feedback from previous trials. The framework is evaluated on Arabic, Persian, and English handwriting datasets through 270 independent experiments. It consistently discovers accurate and computationally efficient models without manual architecture design, domain-specific preprocessing, or hyperparameter tuning. The generated models achieve mean test accuracies above 93 percent, a best accuracy of 98.1 percent, and inference latency between 41 and 44 milliseconds. The results demonstrate that large language models can function as effective AutoML agents for neural architecture search, enabling scalable, script-adaptive, and reproducible handwriting recognition across languages.

---


### 18. [Cache-Aware Prompt Compression:A Two-Tier Cost Model for LLM API Caching](https://arxiv.org/abs/2607.15516)

**<font color=#1a73e8>作者：</font>** Yan Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Production LLM deployments combine two cost-reduction primitives: prompt caching (a discounted rate for re-used token prefixes) and prompt compression (fewer tokens sent). The compression literature has standardized on query-aware methods that produce a different compressed prefix per query, mechanically invalidating the prefix-strict cache on every call. We characterize this cost empirically on Anthropic's Sonnet 4.6 API and find caching is far from the rho=1.0 ideal the literature assumes: Sonnet's cache has a two-tier architecture with a sharp threshold near 3,500 tokens, below which the hit rate plateaus at rho~0.83 across 30-call sessions. Our cost model predicts, and experiments confirm, that under realistic rho, query-aware compression beats naive caching at high compression ratios (r>=6). We propose Cache-Aware Prompt Compression (CAPC), pairing query-agnostic compression with explicit cache_control plus a tier-preserving ratio bound that prevents over-compression from pushing the cached prefix into the hot tier. CAPC is the cheapest strategy in 16/16 configurations on LongBench-v2, with mean savings of 49% over cache-only, 64% over query-aware compression, and 90% over vanilla, at quality within 0.05 of the uncompressed baseline. We validate CAPC on three production workloads: an enterprise tool-using assistant with a 94k-token schema prefix (51.7% cost reduction at r=3); a graphify knowledge-graph RAG pipeline across two codebases (9.3x vs cache-all on FastAPI, 2.4x on httpx); and the public tau-bench retail benchmark (50 tasks), where CAPC is the cheapest of four strategies with reward exactly equal to vanilla (both 36/50, p=1.00) while query-aware compression is the most expensive at +40.1% over vanilla -- the first production confirmation of the crossover model's negative-ROI prediction on a public benchmark.

---


### 19. [SLAPBench: Benchmarking Multimodal Large Language Models for Four-Finger SLAP Fingerprint Verification](https://arxiv.org/abs/2607.15517)

**<font color=#1a73e8>作者：</font>** Bibesh Pyakurel, M. G. Sarwar Murshed  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Four-finger SLAP fingerprints are flat live-scan impressions of the index, middle, ring, and little fingers of one hand, used for identity verification in border control and law enforcement. No benchmark has evaluated whether multimodal large language models (MLLMs) can verify identity from SLAP images. We introduce SLAPBench, the first benchmark for MLLM-based four-finger SLAP fingerprint verification, built from NIST SD302b with 7,832 pairs (176 mated, 7,656 non-mated). We evaluate four open-source MLLMs (InternVL3-8B, Qwen2.5-VL-7B, Qwen3-VL-8B, Gemma-3-12B) and the proprietary Claude Opus 4.8 under zero-shot, task-description, and similarity-scoring prompts.
Prompting governs verification behavior. Task-description prompting collapses all four open-source models to near-100% False Accept Rate (FAR), and Gemma-3-12B collapses under zero-shot as well; Claude Opus 4.8 alone resists collapse under both binary prompts, giving the best binary result (FAR = 20.2%). Similarity scoring removes collapse across the open-source models and exposes wide capability gaps: Claude reaches AUC = 0.953 and Gemma-3-12B 0.837, while InternVL3-8B is inverted (AUC = 0.590) and Qwen2.5-VL-7B near random (0.567). Qwen3-VL-8B attains perfect separation (AUC = 1.000), which we treat as a diagnostic rather than as capability: SD302b holds one SLAP capture per finger position, so mated pairs are cross-resolution. A matched-resolution control leaves the perfect score intact, ruling out the resolution shortcut; what cannot be excluded within SD302b is near-duplicate detection, since a mated pair is one capture rendered twice. A fairness probe over gender, race, and age suggests disparity grows as discrimination weakens. SLAPBench establishes the first SLAP-specific MLLM baseline and shows that prompting governs collapse while model capability governs discrimination.

---


### 20. [Kolmogorov--Arnold Networks for Small Language Models](https://arxiv.org/abs/2607.15525)

**<font color=#1a73e8>作者：</font>** Felippe Alves, Renato Vicente  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kolmogorov--Arnold Networks (KANs) replace fixed node activations with learned one-dimensional edge functions, offering an explicit interface for interpretation and a possible alternative to transformer feed-forward networks. We test these claims separately. In a six-layer, 10M-parameter B-spline KAN, we reconstruct all 884,736 feed-forward edges: 87.8\% exceed (NLS>0.1) and 0.4\% are inactive. Pruning the lowest-activity 20--25\% causes negligible loss increase, although structured MLP neuron pruning tolerates comparable sparsity. The audit replicates on BabyLM, but grid-size sweeps show that near-total fPCA compression and high closed-form-fit coverage are properties of the low-capacity grid-2 basis, not universal KAN behavior. For replacement, we evaluate MLP, SwiGLU, grouped Chebyshev, and rational GR-KAN networks on BabyLM. The KAN-family and gated variants improve validation loss over the GELU MLP, but this ordering does not transfer to standardized benchmarks: across ten seeds and 59,875 BLiMP pairs, accuracies span 62.4--63.1\%, EWoK remains at chance, and a (+0.7)-point GR-KAN effect on BLiMP reverses on the supplement. Larger tests are also cautionary: parameter-matched MLPEdge underperforms the MLP on Wikitext-103, and 286M-parameter GR-KAN remains below a SwiGLU ClimbMix baseline after stabilization. Thus, small-basis KANs provide a practical, corpus-transferable interface for auditing learned scalar transformations, but the tested replacements show no consistent benchmark, quality, or latency advantage over strong MLP baselines.

---


### 21. [EpiNarrate: Agentic Generation of Grounded Narratives from Epidemiological Scenario Projections](https://arxiv.org/abs/2607.15544)

**<font color=#1a73e8>作者：</font>** Rituparna Datta, Srini Venkatramanan, Bryan L. Lewis 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generation of clear and accessible public health narratives is critical for communicating complex epidemiological projections to policymakers and the general public at large. Such narratives require more than simply reporting numbers: projections must be contextualized and quantitatively grounded across multiple dimensions. Further, projections are often derived from large ensemble datasets which combine intervention assumptions, geographic and demographic strata, outcomes, time horizons, and uncertainty quantiles. However, directly using large language models (LLMs) to summarize and contextualize such data often leads to inconsistencies, omissions, and fragile behavior. We introduce an agentic framework (EpiNarrate) for public health report generation that separates structured numerical reasoning from natural-language generation. The framework first extracts scenario axes and organizes them into a partial-order schema, enabling systematic traversal of the underlying multidimensional space. It then constructs an augmented dataset and derives valid quantitative statements through a comparison grammar that enforces semantic and arithmetic consistency. To balance coverage and non-redundancy, we introduce an interestingness-driven selection mechanism based on maximum-entropy principles. Experiments on the COVID-19 Scenario Modeling Hub demonstrate that our model produces narratives with improved factual grounding and broader coverage of salient epidemiological patterns, while preserving the style of expert-written reports.

---


### 22. [SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction](https://arxiv.org/abs/2607.15550)

**<font color=#1a73e8>作者：</font>** Xue Yu, Bo Yuan, Pengshuai Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mobile graphical user interface (GUI) agents have demonstrated remarkable capabilities in automating complex tasks, yet they introduce critical safety risks where a single erroneous action can lead to irreversible consequences. Existing safety mechanisms are primarily reactive, lacking the ability to assess risks before execution. In this paper, we introduce SeerGuard, a consequence-aware safety framework designed to mitigate these risks through pre-execution instruction-level screening and action-level risk assessment. Specifically, the action-level assessment analyzes agent-proposed actions within current GUI states, anticipating likely outcomes to identify risks before they are executed. To enable these capabilities, we construct a unified safety-augmented world model (SAWM) via multi-task learning, integrating semantic next-state prediction with safety risk assessment. Extensive experiments demonstrate that SeerGuard generalizes effectively across diverse mobile GUI agents. On Qwen3-VL-8B-Instruct, it increases the safety-utility score from $0.191$ to $0.596$ at $\omega=0.8$ and reduces the risk-cost score from $0.347$ to $0.130$ at $\alpha=0.8$. Further analyses on our SAWM validate the effectiveness of the instruction-level screening, alongside the capability of action risk assessment and next-state prediction.

---


### 23. [From Feasibility to Desirability: Plan, Learn, Adapt (PLA) Framework for Personalized On-Device Itinerary Generation](https://arxiv.org/abs/2607.15552)

**<font color=#1a73e8>作者：</font>** Himel Dev, Tanmoy Sen, Madhusudan Basak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating personalized trip itineraries is a complex planning task and involves a tension between hard combinatorial feasibility and soft latent desirability. Classical optimization enforces constraints but fails to capture subjective traveler preferences. While learning-based approaches model preferences, they cannot guarantee feasibility. Mobile deployment imposes additional resource constraints on both. To address this, we propose Plan, Learn, Adapt (PLA), a three-stage framework for personalized on-device itinerary generation. The Plan stage builds a heterogeneous ensemble of lightweight planners that produces structurally diverse feasible candidates. From pairwise itinerary comparisons, Learn fits a compact Bradley-Terry reward model that captures emergent schedule properties such as pacing, geographic coherence, and day balance, which per-POI signals miss. Finally, Adapt applies feasibility-preserving local refinement within a device-aware compute budget; every intermediate state is feasible by construction. On 2,519 pairwise human comparisons across more than 100 U.S. cities, the reward-guided ensemble achieves a 67.8% win rate, 11.2 percentage points above the best single planner, with 100% feasibility. Three frontier LLMs, GPT-5, Claude Opus 4.5, and Gemini 3 Pro, achieve 0% feasibility under the same constraints. The reward model generalizes across held-out cities, with a 67.6% mean leave-one-city-out accuracy. In production deployment within FlyEnJoy, PLA increased itinerary completion rates by 91%, with 109.9 ms average on-device latency.

---


### 24. [When Can Test-Time Adaptation Help Zero-Shot CT Vision-Language Models?](https://arxiv.org/abs/2607.15556)

**<font color=#1a73e8>作者：</font>** Ailar Mahdizadeh, Puria Azadi Moghadam, Xiangteng He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D CT vision-language models (VLMs) classify abnormalities from text prompts in a zero-shot manner, enabling cross-institution deployment where labels are scarce and clinical tasks shift faster than supervised models can be retrained. A real CT scan, however, typically contains several co-occurring abnormalities, and the reliability of zero-shot multi-label prediction under distribution shift remains poorly understood. Test-time adaptation (TTA) updates a model on unlabeled target scans without source data or target annotations, yet existing TTA methods target multi-class softmax prediction on natural images or 2D medical segmentation, and none addresses unsupervised multi-label adaptation for zero-shot 3D CT VLMs. We study when TTA helps zero-shot 3D CT VLMs. A controlled diagnostic analysis shows that TTA is conditional: the volumetric input must preserve the encoder's depth structure, and the base representation must transfer to the target cohort, with depth reduction alone lowering internal AUROC by more than 0.12. We then focus on the regime where the base model already separates present from absent abnormalities. We introduce CARVE (Cardinality-Aware Retained-View Entropy), the first TTA method for this setting. CARVE estimates a sample-specific positive-label cardinality $\hat{k}$, optimizes a top-$\hat{k}$ objective to preserve co-occurring abnormalities, and performs memory-efficient multi-view adaptation by scoring weak 3D views without gradients before updating on a retained subset. Across contrastive CT-CLIP and anatomy-aware fVLM, CARVE provides the most consistent improvements across multi-label, three-class, and binary CT tasks when the base model is already discriminative. These results establish multi-label TTA for zero-shot 3D CT VLMs as a distinct problem and CARVE as a cardinality-aware solution.

---


### 25. [SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World LLM Agents](https://arxiv.org/abs/2607.15557)

**<font color=#1a73e8>作者：</font>** Yanze Wang, Pengfei Yao, Tianyi Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent skills, this http URL files that package reusable procedural knowledge for an LLM agent, are a popular mechanism for extending agent capabilities. Public repositories now host them in large and growing numbers, yet these artifacts are fragmented, redundant, and uneven in quality, and their value in practice is unclear. A core question remains open, namely how to consolidate this open-source this http URL ecosystem into a single usable corpus, and what bounds its benefit on real-world agent tasks. We present SkillCorpus, a framework that aggregates, curates, matches, and evaluates the open skill ecosystem at scale. It filters ~821,000 crawled skills through a multi-stage pipeline into 96,401 skills organised by a 16-class taxonomy and three quality facets (utility, robustness, safety), and pairs them with a fine-tuned retrieval-and-selection stack that matches task-relevant skills. We evaluate end-to-end across three benchmarks (SkillsBench, GDPVal, QwenClawBench), two harnesses, and two open backbones with a frontier robustness check. Integrating SkillCorpus yields consistent gains across all three benchmarks, largest on SkillsBench (+7.5 pp). An operational analysis traces the gains to a coverage boundary and a harness boundary. SkillCorpus is, to our knowledge, the first end-to-end account of when a curated, retrieval-served community corpus improves real agent tasks, and where it does not. The dataset, models, and code will be released upon acceptance.

---


### 26. [Ask Twice, Look Twice: Prompt Echoing Resolves the Question-First Paradox in Vision-Language Models](https://arxiv.org/abs/2607.15565)

**<font color=#1a73e8>作者：</font>** Rakshanda Hassan Abhinandan, John Galeotti, Deva Ramanan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Where should the question go in a vision-language model (VLM) prompt: before the image or after it? Intuition says before: knowing what is asked should tell the model where to look. Yet across visual question answering benchmarks, question-first prompting consistently underperforms the image-first ordering recommended for frontier VLMs, a phenomenon we term the question-first paradox. We trace the paradox to a conflict between two stages of VLM computation. Logit-lens and attention probes show the intuition is half right: a question placed before the image genuinely steers perception, moving image patch representations toward question-relevant concepts. The failure lies downstream. Stranded behind hundreds of image tokens, the question is barely attended by the answer token, which instead commits to image-driven (often wrong) answers; a causal attention knockout confirms that the answer reads the question only when the question follows the image. The diagnosis yields a training-free fix: question echoing, restating the question on both sides of the image so that one copy steers perception while the other is read out at answer time. The same division of labor appears in a fifty-year-old finding on human ``adjunct questions'', where repeating a question before and after a passage aids comprehension more than either position alone. Echoing the image as well brings further gains, restoring the whole-image view a causal decoder otherwise loses. The paradox holds across five open VLMs, costing up to 17.5 group-accuracy points. Echoed prompts close it and surpass the best single-pass ordering on NaturalBench, POPE, Winoground, and open-ended VQAv2, by up to 19 Winoground group-accuracy points, with no training, fine-tuning, or architecture change. The paradox reveals a trade-off between steering perception and preserving question access; echoing resolves it through prompt design alone.

---


### 27. [MGDT: MLLM-Guided Diffusion Transformer with Relation-Adaptive Mixture-of-Experts for Multimodal Knowledge Graph Completion](https://arxiv.org/abs/2607.15592)

**<font color=#1a73e8>作者：</font>** Xu Hou, Meiyu Liang, Wei Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Knowledge Graph Completion (MKGC) requires inferring missing entities from structural, textual, and visual cues. Existing diffusion-based MKGC methods usually denoise directly on raw multimodal features. Such a design forces the denoiser to simultaneously perform relation-dependent cue selection, cross-modal semantic alignment, and structure-aware entity generation, which introduces noisy and semantically inconsistent conditions for diffusion and consequently leads to suboptimal completion performance. To address this limitation, we propose MGDT: MLLM-Guided Diffusion Transformer with Relation-Adaptive Mixture-of-Experts (MGDT), a novel MKGC framework built on an align-then-diffuse paradigm. MGDT first employs a Relation-Adaptive Semantic Routing Mixture-of-Experts (RASR-MoE) module to select relation-relevant multimodal semantic transformation paths and suppress irrelevant modality interference. MGDT then uses a frozen Multimodal Large Language Model (MLLM) as a semantic anchor to align the routed multimodal representations into a unified latent space and reduce cross-modal semantic heterogeneity. Finally, a Knowledge Graph Diffusion Transformer (KGDT) performs graph-conditioned denoising generation in the aligned space to produce the missing entity representation. Experiments on three benchmark datasets show that MGDT consistently outperforms strong baselines.

---


### 28. [Geometric Distillation from Rectified Stereo: Leveraging Epipolar Cues for Monocular Depth](https://arxiv.org/abs/2607.15600)

**<font color=#1a73e8>作者：</font>** Jung-Hee Kim, Xiaoming Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth foundation models have demonstrated remarkable generalization capabilities across diverse environments. However, they continue to struggle with metric depth estimation in diverse environments. This limitation stems from the inherent scale ambiguity of single-view inference, leading to misaligned scale predictions even when the relative geometry is accurate. Conversely, recent multi-view foundation models leverage cross-view cues to learn robust scene-level geometry and consistent scale. Yet, these benefits typically vanish during single-image inference, as the absence of explicit geometric constraints causes performance to degrade. To bridge this gap, we propose a novel framework that transfers the scale-aware geometric priors of multi-view models into monocular depth foundation models. Specifically, we introduce an Epipolar Distillation (EpiDistill), an approach utilizing Rectified Stereo Tokens, which enables the single-view prediction model to retain epipolar attention patterns and maintain geometric consistency without requiring multi-view inputs at inference. Experimental results demonstrate that our method significantly improves zero-shot metric depth estimation, particularly on challenging datasets like ETH3D and DIODE where scale alignment is critical. Furthermore, our approach is model-agnostic, consistently boosting the performance of state-of-the-art ViT-based models, including UniDepthV2 and DepthPro.

---


### 29. [Understanding Fortunetelling with Large Language Models in China: User Practices, Perceptions, and Impacts on Beliefs and Decisions](https://arxiv.org/abs/2607.15626)

**<font color=#1a73e8>作者：</font>** Xueer Lin, Chenyu Li, Shuai Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Fortunetelling is a cultural practice for navigating uncertainty, often associated with people's beliefs and decisions. Fortunetelling with recent large language models (LLMs) introduces new opportunities and risks. This paper conducts qualitative studies to understand users' practices, perceptions, and impacts of LLM fortunetelling in China. We first analyze 1,045 posts on Chinese social media, yielding a comprehensive taxonomy of the diverse foretold topics (e.g., career, romance), emotion reactions (e.g., surprise, worry), and perceived credibility (e.g., doubt, trust) of LLM fortunetelling. Then, we conduct interviews with 20 users of LLM fortunetelling. The findings indicate that users treat LLM fortunetelling as a tool less for accurate prediction but more for emotional support. While the fortunetelling results rarely change users' initial beliefs or decisions, they are associated with subtle mindset shifts, with some users reporting small behavioral adjustments. We discuss implications for gaining benefits from LLM fortunetelling.

---


### 30. [Neuro-Symbolic AI for LEED compliance: Document-Centric Benchmarking, Deterministic Numeric Checking, and When Multimodal Hurts](https://arxiv.org/abs/2607.15647)

**<font color=#1a73e8>作者：</font>** Aritro De, Juliana Felkner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LEED v4.1 BD+C certification remains a document-intensive process that requires reviewers to read hundreds of pages of project evidence and apply credit-specific threshold logic by hand. This paper investigates whether small, locally deployed language models can perform meaningful screening of LEED documentation and how deterministic symbolic components should share that work. A neuro-symbolic pipeline is introduced that aligns project PDFs to LEED credit sections, retrieves evidence with credit-aware keyword signatures, verifies compliance with a locally hosted 4-billion-parameter language model, and applies a LEED-specific numeric checker to quantitative thresholds. Experiments on four university buildings (484 PDFs, 153 credit-level decisions) show that a 4-billion-parameter model (gemma3:4b) is the strongest text-only core verifier, achieving 67.3% accuracy and outperforming a larger 8-billion-parameter model (llama3.1:8b) in this task. The deterministic numeric checker corrects arithmetic errors on key quantitative credits, moving EA-p2 from 50% to 100% accuracy and improving several other credits when required values are reliably extracted. At the same time, the full neuro-symbolic configuration achieves 61.6% overall accuracy, trailing the best text-only baseline due to extraction failures and conservative behavior on qualitative categories. Systematic ablations show that adding low-resolution drawing images (150-300 dpi) consistently reduces accuracy, and that prompt effectiveness depends on the building's ground-truth PASS rate: rubric prompts perform best on documentation-rich projects, while chain-of-thought prompts perform best on documentation-lean projects. Within the specific scope of LEED v4.1 BD+C compliance verification over raw project documentation, this pipeline and its baselines provide an initial reproducible reference point for both accuracy and failure modes.

---


### 31. [Adaptive Multi-Step Lookahead Decoding for Diffusion Language Models](https://arxiv.org/abs/2607.15655)

**<font color=#1a73e8>作者：</font>** Yingqian Cui, Wei Deng, Lantao Mei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (DLMs) enable parallel text generation by iteratively refining masked tokens, offering a promising alternative to autoregressive decoding. Recent lookahead-based decoding methods improve the accuracy--efficiency trade-off by exploring future decoding states before committing token updates. However, existing approaches mainly rely on shallow one-step lookahead, which optimizes immediate information gain but can be suboptimal for longer-horizon decoding trajectories. Meanwhile, we find that a naive extension for deeper lookahead is also ineffective, as fixed-depth rollout introduces additional computation and cannot adapt to heterogeneous intermediate decoding states. Thus, in this work, we propose AdaLook, an adaptive lookahead framework for DLM decoding. AdaLook dynamically determines whether to continue rollout based on candidate-score variance and further enables branch expansion when intermediate rollout states require additional exploration. This design avoids unnecessary deep rollout while allowing the decoder to re-trigger lookahead from informative intermediate states. Experiments on various benchmarks and models demonstrate that AdaLook achieves a better accuracy--decoding steps trade-off than existing one-step lookahead decoding methods.

---


### 32. [ToolVerse: Unlocking Massive Environments and Long-Horizon Tasks for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.15660)

**<font color=#1a73e8>作者：</font>** Shuaiyu Zhou, Fengpeng Yue, Zengjie Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While LLM agents demonstrate strong reasoning abilities in compact and well-defined scenarios, they struggle to maintain robustness and effectiveness when faced with large-scale, diverse, and dynamic real-world environments that demand seamless tool integration. To address this gap, we introduce ToolVerse, a comprehensive framework that scales up agentic RL environments and enables agents to perform complex long-horizon reasoning in Tool-Integrated Reasoning (TIR) tasks. First, ToolVerse automatically builds the massive executable agent training environments from nearly 400 real-world Model Context Protocols (MCPs) that contain about 4500 tools. Second, we propose a task design strategy based on a tool dependency graph, utilizing Dynamic Unlocking Sampling Algorithm to generate long-horizon tasks, and produce GUST (Graph Unlocking Sampling Tasks) dataset. Third, to alleviate the credit assigment problem in long-horizon agentic RL, we propose a fine-grained Turn-Aware Relative Advantage algorithm. We conduct extensive Agentic RL training using ToolVerse and evaluate our framework on serveral agentic benchmarks. Experimental results demonstrate that our framework significantly strengthens LLMs' capabilities in long-horizon tool use, achieving a marked performance boost and showcasing robust reasoning within dynamic environments.

---


### 33. [Model Merging for Medical LVLMs: A Benchmark and a Winner-Take-All Approach](https://arxiv.org/abs/2607.15661)

**<font color=#1a73e8>作者：</font>** Lichao Mou, Shilan Zhang, Chunlei Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) can be adapted to specialized medical imaging tasks via parameter-efficient fine-tuning approaches such as low-rank adaptation (LoRA), leading to a growing ecosystem of expert models tailored to specific imaging modalities and clinical scenarios. However, deploying multiple expert LVLMs in practice incurs substantial computational and operational overhead. Model merging provides a promising solution by consolidating multiple experts into a single model without retraining, yet it remains largely unexplored in the medical domain. In this work, we present the first systematic study of model merging for medical LVLMs. We introduce MergeMedBench, a comprehensive benchmark spanning eight imaging modalities and diverse clinical task types, comprising 16 LoRA fine-tuned models built upon two mainstream architectures. We conduct an extensive evaluation of existing merging methods and further propose winner-take-all, a simple and hyperparameter-free approach that retains only the most dominant parameters across expert models. By preserving the critical parameters that govern model behavior and discarding weaker ones, our method avoids the information dilution inherent in averaging- or alignment-based strategies. Despite its simplicity, winner-take-all consistently outperforms existing approaches, offering both a new perspective on LoRA merging and a strong practical baseline for future research.

---


### 34. [S1-Omni: A Unified Multimodal Reasoning Model for Scientific Understanding, Prediction, and Generation](https://arxiv.org/abs/2607.15686)

**<font color=#1a73e8>作者：</font>** Jiahao Zhao, Junyi Liu, Lifeng Xu 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present S1-Omni, a unified multimodal reasoning model for scientific understanding, prediction, and generation. AI for Science (AI4S) has advanced significantly through domain-specific models, tool-augmented LLMs, and scientific language models. However, model capabilities remain highly fragmented, limiting the joint modeling of heterogeneous data, scientific laws, and expert knowledge. S1-Omni addresses this gap by consolidating these capabilities into a single, coherent scientific reasoning model. The architecture of S1-Omni is built upon three core components: unified representation of scientific data, natural-world knowledge alignment, and decoding for domain-specific tasks. First, S1-Omni maps natural-language instructions and scientific objects, including CIF, SMILES, protein sequences, spectra, and scientific images, into a shared representation space. Second, it incorporates scientific laws and expert knowledge into data construction and training, enabling the model to reason from scientific evidence. Third, it performs task-specific decoding to support a broad range of applications, including property prediction, spectrum-to-molecular generation, protein site and structure prediction, and scientific image generation and editing. S1-Omni is trained on S1-Omni-Corpus, which covers 200 scientific tasks and contains millions of reasoning samples, and is evaluated on over 60 scientific benchmarks. It outperforms GPT-5.5 and Gemini-3.1-Pro on most benchmarks and matches or surpasses domain-specific models on several benchmarks. Overall, S1-Omni provides a practical path toward unified scientific modeling.

---


### 35. [Toward Federated Multimodal Graph Foundation Models: A Topology-Aware Multimodal Alignment Framework](https://arxiv.org/abs/2607.15687)

**<font color=#1a73e8>作者：</font>** Xunkai Li, Guohao Fu, Yuming Ai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal-attributed graphs (MAGs), whose nodes carry modalities such as images and text alongside topological structure, now pervade applications including social platforms, e-commerce, and biomedical networks, offering richer semantic signals than single-modality graphs. In practice, such graphs are fragmented across privacy-restricted silos owned by different platforms and institutions, so learning a broadly transferable model over them demands collaborative training that never exposes raw data. This places the task at the intersection of multimodal graph learning and federated learning, yet existing methods cover only one side of it. To address the challenges from these two perspectives, we propose FedGAMMA, casting federated multimodal graph foundation learning as a two-stage semantic-structural alignment problem of federated pre-training and prompt-based fine-tuning. During pre-training, a shared-private semantic enhancer disentangles cross-modal commonality from modality-specific information, aligning it through optimal transport, a topology-aware graph fusion module decouples semantic and structural views via semantic residual graphs and dual positional encodings, and a dual-channel affinity-aware aggregation mechanism estimates client similarity from feature and graph centroids without exposing raw data. During fine-tuning, FedGAMMA adapts the pretrained encoder through lightweight graph-aware prompts, a shared prompt pool with controlled exploration, and channel-wise prompt synchronization. Experiments on twelve multimodal graph datasets show FedGAMMA consistently surpassing a broad range of baselines across downstream tasks, with gains of up to 12.96%. FedGAMMA further outperforms competitive baselines accross multi-domain datasets on multiple tasks with up to 5.71% under few-shot learning scenario.

---


### 36. [Efficient Frame Selection for Long Videos at Test Time with Attention-Based MLLM Selectors](https://arxiv.org/abs/2607.15689)

**<font color=#1a73e8>作者：</font>** Yilin Wang, Xiangxi Zheng, Dongxing Mao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding long videos with multimodal large language models (MLLMs) requires selecting a compact set of frames from thousands of candidates, yet identifying the right frames seemingly requires understanding the video first. We resolve this circular dependency with a simple observation: cross-modal attention at validation-selected extraction layers in MLLMs already provides query-relevant frame evidence without requiring autoregressive generation. We exploit this property to build DAFS (Dynamic Attention-based Budget-aware Frame Selection), a training-free frame selector. A lightweight MLLM selector, even with only 2B parameters, can extract frame-level evidence by converting selected-layer attention into relevance scores through query-conditioned aggregation. This enables cross-frame comparison without autoregressive decoding. To handle the selector's own context constraint, we formulate the joint allocation of candidate pool size and per-frame token budget as a discrete optimization problem solved by dynamic programming. Under a 32-frame budget, our selector improves over uniform sampling by up to 6.4 points on Video-MME and outperforms prior training-based selectors under matched frame budgets, while generalizing across selector and answerer backbones, and across tasks, without retraining.

---


### 37. [Behavioral Controllability of Agentic Models for Information Extraction: From Fixed Workflows to Reflective Agents](https://arxiv.org/abs/2607.15715)

**<font color=#1a73e8>作者：</font>** Lujia Zhang, Xingzhou Chen, Hongwei Feng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly used for complex information-extraction tasks, yet it remains unclear whether agentic components such as reflection and memory lead to observable and controllable improvements over fixed LLM workflows. We study this question through conference-paper dataset extraction, where a system must identify datasets mentioned in scholarly PDFs and produce structured records. We compare a fixed workflow baseline with reflective agent variants and specify an optimized agent condition (S2) that extends the same task with richer PDF tools and dynamic tool selection. Our evaluation emphasizes process-level behavior--including tool execution, retries, reflection, memory use, runtime, and failure recovery--while treating extraction coverage and field completeness as secondary outcome measures. The paper characterizes when agentic mechanisms change system behavior, whether these changes improve task completion, and how the observed failure modes motivate an optimized agent design under the same evaluation harness.

---


### 38. [IoUPD: IoU-Aware Privileged Distillation for Visual Grounding with Multimodal Large Language Models](https://arxiv.org/abs/2607.15732)

**<font color=#1a73e8>作者：</font>** Xiuyuan Zhu, Ke Lu, Hao Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual grounding with multimodal large language models is commonly formulated as autoregressive coordinate generation, where a model outputs bounding-box coordinates as text given an image and a referring-expression prompt. While this interface is simple and compatible with instruction following, it introduces a mismatch between training and evaluation: training optimizes token-level likelihood over coordinate strings, whereas grounding quality is measured by geometric overlap. We propose IoUPD, an IoU-aware privileged distillation method for coordinate-generating multimodal large language models. IoUPD uses ground-truth boxes not only as coordinate targets, but also as privileged training-time guidance. During training, the student receives the original image and prompt, while a frozen teacher receives a box-marked image and an augmented prompt that indicates the marked region. The student is trained with a supervised fine-tuning anchor and a privileged distillation loss whose token weights reflect both geometric importance and teacher reliability. At inference time, IoUPD requires no box overlay, privileged hint, teacher branch, or additional prediction module. Experiments on standard referring-expression grounding benchmarks show consistent region-level improvements over strong coordinate-generating baselines, demonstrating that ground-truth boxes can provide useful privileged guidance beyond serving as coordinate labels.

---


### 39. [Better Starts, Better Ends: Bootstrapped Iterative Self-Reasoning Distillation for Compressed Reasoning](https://arxiv.org/abs/2607.15736)

**<font color=#1a73e8>作者：</font>** Leichao Dong, Dongxu Zhang, Yiding Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models often solve problems through long chain-of-thought (CoT) traces, yet much of this computation is spent on redundant derivations, repeated self-verification, and detours that do not improve the final answer. Existing on-policy self-distillation methods reduce this cost by matching a student model to a concise copy of itself on prefixes sampled from the student's own rollouts. We show that this objective has an initialization bottleneck. Since supervision is applied only to visited prefixes, training from a verbose base model places the KL loss on contexts that are often noisy, redundant, or already off track. In such regions, a concise teacher can provide only local corrections, while the student continues to explore trajectories that an efficient reasoner should avoid. In this paper, we propose BIRD(Bootstrapped Iterative Self-Reasoning Distillation), a two-stage self-reasoning distillation method that improves the rollout distribution before on-policy training. BIRD first samples concise solutions from the base model under a brevity instruction, keeps only answer-correct traces, and performs a lightweight prompt-switch SFT step. The traces are generated with the brevity instruction but learned under the original task prompt, turning instruction-induced conciseness into a default reasoning behavior. Starting from this warm model, BIRD then applies on-policy reverse-KL distillation with a concise self-teacher, now on cleaner and more informative prefixes. Across Qwen3 series models, BIRD achieves a stronger accuracy-efficiency trade-off than prompting and cold-start on-policy distillation on MATH-500 and AIME benchmarks. On Qwen3-8B, it improves MATH-500 accuracy from 86.2% to 92.0% while reducing the average response length from 3,099 to 1,115 tokens. These results highlight prefix support as a central factor in efficient reasoning distillation.

---


### 40. [Debiasing Text-to-Image Evaluation via Implicit Cultural Alignment Reward Modeling](https://arxiv.org/abs/2607.15740)

**<font color=#1a73e8>作者：</font>** Bo-An Chang, Yu-Chih Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As Text-to-Image (T2I) systems rapidly advance, evaluating the cultural authenticity of synthesized content has become increasingly important for fair and trustworthy generative AI. Existing T2I evaluation metrics and multimodal judges often rely on visual-semantic representations that underrepresent implicit cultural norms, leading to biased preference judgments and the omission of fine-grained cultural cues. In addition, visual question answering (VQA)-based evaluators typically depend on autoregressive text generation, which limits their scalability for real-time reward modeling. To address these limitations, we introduce an Implicit Cultural Alignment Reward Model built upon a lightweight 4.2-billion-parameter Multimodal Large Language Model (MLLM). Our framework integrates an Implicit Cultural Probe with a Skip-connection Cross-Attention (SkipCA) mechanism, enabling late-stage semantic features to directly attend to early-stage visual representations and better preserve culturally salient details. Evaluations on 3,323 challenging and carefully curated image pairs from the CulturalFrames benchmark show that our approach achieves 80.54% pairwise accuracy, with Pearson and Kendall correlation coefficients of 0.546 and 0.377, respectively, outperforming representative vision-language metrics and MLLM-based evaluators. Moreover, by bypassing autoregressive text generation, our model processes each evaluation in 0.21 seconds under our local inference setup, achieving a $10\times$ speedup over standard VQA-based evaluators. These results suggest that the proposed reward model can provide an efficient and culturally aware scalar signal for preference optimization pipelines such as Reinforcement Learning from Human Feedback and Direct Preference Optimization.

---


### 41. [Personalized Image Aesthetic Assessment via Preference-rich Sample Mining and Cohort Merging](https://arxiv.org/abs/2607.15752)

**<font color=#1a73e8>作者：</font>** Zhichao Yang, Tianjiao Gu, Zhixianhe Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalized Image Aesthetic Assessment (PIAA) aims to predict aesthetic ratings of images that vary across individuals. The aesthetic preferences manifest to different extents across distinct visual stimuli and exhibit cohort-specific patterns. Motivated by the above fact, this paper presents a Multimodal Large Language Model (MLLM)-based approach, which models individual aesthetic preferences by Preference-Rich sample mining and Aesthetically-resonant Cohort merging (PRAC). Specifically, PRAC first identifies preference-rich samples by analyzing both Collective Controversy and Personalized Deviation of images, maximizing the utility of limited user data. Based upon the preference-rich samples, cross-user preference similarities are measured by comparing preference embeddings. Then, a cohort-based model merging strategy, is proposed by aggregating preference patterns from aesthetically-resonant users, which further enhances the personalization for the target individual. Extensive experiments and comparisons on four benchmark PIAA databases demonstrate the superiority of the proposed PRAC model over the state-of-the-arts. The code and model will be public at this https URL.

---


### 42. [Before the Action: Benchmarking LLMs on Prospective Hypothesis Discovery](https://arxiv.org/abs/2607.15766)

**<font color=#1a73e8>作者：</font>** Tianyun Zhong, Wangyi Jiang, Wei Wang 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) excel at answering pre-specified questions, yet their ability to navigate the open-ended, pre-conclusion stage of discovery remains largely unmeasured. We introduce Prospective Hypothesis Discovery (PHD), which asks models to autonomously construct grounded, discriminative, and testable hypothesis spaces from inconclusive evidence, including anomalous observations and fragmented records, to guide subsequent investigation. To evaluate this capability, we introduce HypoArena, comprising HypoData, a benchmark of 988 cases across six scientific and analytical domains, and HypoEval, an evaluation framework for open-ended hypothesis sets. To construct HypoData at scale, we propose Retrospective Context Regression, a Forge--Audit pipeline that reconstructs pre-conclusion contexts from completed expert documents by removing explicit conclusions, target hypotheses, and retrospective causal attributions while preserving the factual substrate. Because PHD admits multiple valid outputs, HypoEval combines bidirectional pairwise judgments with Bradley--Terry--Davidson aggregation for ranking and six-dimensional rubric scoring for diagnosis. Experiments on 15 frontier LLMs reveal clear capability stratification and model-dependent effects of structured analytical skills, with gains for several lower-performing models on HypoArena but regressions for other systems, including a top-performing model. Compared with absolute rubric scoring, arena evaluation resolves finer-grained differences among models, with aggregated rankings showing strong agreement with human experts and an independent judge. Together, these results support treating PHD as a distinct target for evaluating how LLMs formulate investigative directions when final conclusions are withheld. Our code and data are publicly available at this http URL and this http URL.

---


### 43. [NeurOWL: An LLM-Based Neural-symbolic Framework for Incomplete OWL Ontology Reasoning](https://arxiv.org/abs/2607.15776)

**<font color=#1a73e8>作者：</font>** Hui Yang, Jiaoyan Chen, Yiping Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> OWL ontologies provide a formal knowledge representation framework that enables semantic reasoning, and have been widely adopted across domains such as healthcare and bioinformatics. In practice, however, real-world ontologies are often incomplete, which pose challenges for reasoning. In this work, we focus on a fundamental subsumption reasoning problem: given an incomplete ontology and a candidate (non-entailed) subsumption, determine whether the subsumption is semantically plausible and, if so, providing a logically sound explanation containing potential missing axioms. This task unifies subsumption verification with ontology abduction, and generalizes the latter by removing the need for a predefined candidate set of missing axioms. To address this subsumption reasoning problem, we propose NeurOWL, an end-to-end neuro-symbolic framework that jointly performs verification and abduction, leveraging both formally defined semantics and textual semantics through Large Language Models and ontology embeddings. We evaluate NeurOWL on real-world ontologies across multiple domains, demonstrating strong and robust performance across different domains.

---


### 44. [Modularized Dynamic-Granularity Video LLM for Multi-Event Long Video Understanding](https://arxiv.org/abs/2607.15778)

**<font color=#1a73e8>作者：</font>** Wei Feng, Xin Wang, Yu-Wei Zhan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Large Language Models (Video LLMs) have made significant advancements in various video understanding tasks. However, long-video scenarios remain challenging due to the tension between limited visual token budgets and the need to capture multiple key events. Existing approaches typically process long videos in two stages, i.e., i) select keyframes and ii) perform detailed perception, which exhibit limitations: they lack a modular mechanism for adaptive capacity allocation and self-correction, resulting in unreliable modeling. To tackle these challenges, we propose MoD-VLLM, a novel Modularized Dynamic-Granularity Video LLM framework for multi-event long video understanding, which unifies temporal grounding and semantic understanding iteratively and self-reflectively. Specifically, we propose a Positive-Negative Video Segments Grounding module and a Modularized Dynamic-Granularity Reflection module, which form a closed loop to progressively localize the question-related video segments. The grounding module instructs a Video LLM to distinguish relevant from irrelevant video segments based on the video question. The reflection module employs a modularized scheduler that dynamically selects fine-grained encoding for relevant positive segments to capture detailed perception and coarse-grained encoding for negative segments to maintain global context. We further propose a dynamic-granularity reinforcement learning strategy, allowing MoD-VLLM to learn optimal grounding policies and dynamic granularity visual representation jointly. Moreover, we propose MEventBench, a challenging Multi-Event Long Video Benchmark for complex long video reasoning. Extensive experiments on several long video understanding benchmarks and our MEventBench demonstrate that MoD-VLLM significantly outperforms state-of-the-art baselines.

---


### 45. [Multimodal Ambivalence and Hesitancy Recognition via Cross-Attention and Gated Fusion](https://arxiv.org/abs/2607.15779)

**<font color=#1a73e8>作者：</font>** Oussama Berhili, Yassine Ouzar, Larbi Boubchir  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a multimodal framework for Ambivalence/Hesitancy (A/H) recognition in video, developed for the ABAW11 challenge at ECCV 2026. The proposed approach fuses textual, acoustic, and visual modalities extracted from the BAH dataset using three pretrained encoders: F2LLM-v2-0.6B for transcripts (1024-d), WavLM-Large for audio (1024-d), and VideoMAE V2 for facial video (768-d). We first establish comprehensive unimodal baselines using classical classifiers (MLP, Random Forest, GBDT), each optimized via Optuna, and obtain a best unimodal Macro F1 of \textbf{0.6659} on the test set using text features alone -- substantially outperforming the zero-shot Video-LLaVA baseline (Macro F1: 0.2827). Building on these baselines, we propose a multimodal fusion architecture that combines bidirectional cross-attention across all three modalities with a Gated Multimodal Unit (GMU), with both architectural and optimization hyperparameters selected through a 50-trial Optuna search. This model achieves a Macro F1 of \textbf{0.7394} on the validation set, a relative improvement of 11.0\% over the best unimodal baseline, confirming that explicit cross-modal interaction captures complementary cues that no single modality provides in isolation. Final predictions on the official, unlabeled private test set are generated using this model and submitted according to the challenge protocol. Code is publicly available at this https URL

---


### 46. [QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides](https://arxiv.org/abs/2607.15810)

**<font color=#1a73e8>作者：</font>** Zhengyang Zhuge, Hao Yu, Xin Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rollout generation is a major bottleneck in Reinforcement Learning (RL) for Mixture-of-Experts (MoE) Large Language Models, motivating low-precision rollout acceleration such as FP8. As an emerging low-precision format, NVFP4 combines fine-grained scaling for accuracy preservation with native W4A4 FP4 GEMMs for higher throughput than FP8. However, we find that directly applying NVFP4 to MoE RL rollout is impractical. NVFP4 rollout with BF16 training collapses after roughly 150 steps, accompanied by rapidly growing rollout-trainer log-probability gaps. Through training-inference error analysis and controlled ablations, we identify activation error, rather than weight error, as the dominant source of FP4 RL instability: weights can be synchronized and aligned by a shared quantization-dequantization path, whereas activations are recomputed online and error is amplified by the coarse E2M1 grid. Therefore, to stabilize NVFP4 RL for MoE, we propose QUantization-error Alignment across Dual Sides (QUADS). On the trainer side, we introduce Asymmetric Quantization-Aware Training fake-quantizing weights while keeping activations unquantized for better alignment. On the rollout side, Residual Activation Compensation corrects high-error activation channels while preserving native W4A4 GEMMs. In our MoE RL experiments on several benchmarks, QUADS achieves BF16-level accuracy, improves average pass@1 by 21.49 points over naive NVFP4 RL, and delivers ~16% higher rollout throughput than FP8.

---


### 47. [In-context learning of closed form solution to simple linear regression task using transformer with linear self-attention](https://arxiv.org/abs/2607.15819)

**<font color=#1a73e8>作者：</font>** Katsuyuki Hagiwara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-context learning is a remarkable property of transformers and has recently received a lot of interest. In many studies of in-context learning, it has been shown that transformers are capable of implementing solver for linear and non-linear regression problems, in which the most of them implement gradient descent algorithm. However, it is still unclear whether those implementations have actually been acquired through training. In this paper, we construct a transformer with linear self-attention, which in-context learns the least squares estimate in a simple regression task. The point here is that the closed form (analytical) solution is approximately obtained by using layer normalization rather than an approximate solution based on gradient descent algorithm. Then, we show an experimental example, in which our implementation is mainly used in the transformer trained with l1 regularization when the target output is the least squares estimate.

---


### 48. [Knowledge-Centric Agents for Workflow Generation](https://arxiv.org/abs/2607.15845)

**<font color=#1a73e8>作者：</font>** Zhendong Li, Lei Sun, Ruibo Ming 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Workflow generation in visual creation systems such as ComfyUI demands not only syntactic accuracy but also expert-level reasoning over modular compositions. Existing large language model (LLM) approaches often treat this as a direct text-to-JSON generation task, struggling with structural brittleness and lacking the experiential knowledge required for effective design. We argue that successful workflow generation requires modeling knowledge itself, including its structure, hierarchy, and reasoning dynamics. To this end, we propose a knowledge-centric framework that learns to invert, inject, and infer with knowledge across multiple abstraction levels. We first perform knowledge inversion to distill hierarchical representations, ranging from full pseudo-codes and skeletons to high-level strategies, from large collections of real-world workflows. We then conduct knowledge injection through supervised fine-tuning, teaching the model to reason from task descriptions to strategies and from strategies to executable structures. During inference, the model performs reversible reasoning to synthesize executable workflows, augmented by self-refinement for structural coherence. Extensive experiments demonstrate that our method produces workflows with richer node diversity, more coherent structures, and higher execution success rates than existing systems, establishing a new foundation for knowledge-driven, agentic workflow generation.

---


### 49. [An MLIR-Based Compilation Method for Large Language Models](https://arxiv.org/abs/2607.15865)

**<font color=#1a73e8>作者：</font>** Pengchao Hu, Zhibin Xin, Yifan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have become the dominant workload on modern AI accelerators, yet deploying them on specialized hardware still faces two core challenges: how to import a trained model into a compiler-friendly intermediate representation, and how to efficiently schedule the autoregressive inference loop under limited on-chip memory. This paper presents an MLIR (Multi-Level Intermediate Representation) based compilation method for large language models, illustrated using two dialects of operators, TopOp and TpuOp. TopOp serves as a high-level graph dialect that is independent of both the source framework and the target chip, and is responsible for expressing model semantics; TpuOp serves as the target hardware dialect, carrying chip-related decisions such as quantization, layer groups, and memory layout. A model is first represented as TopOp, then lowered layer by layer to TpuOp, and finally a deployable binary is generated. In addition, each Transformer layer is split into three stages for static compilation: prefill, prefill_kv (prefill with historical key-value cache), and decode, so as to accommodate the different computational characteristics of prompt-parallel processing and per-token generation. The method has been implemented in the TPU-MLIR compiler{this https URL} and the LLM-TPU deployment project\footnote{this https URL}, supporting a variety of generative models including the Qwen, Llama, InternVL, and MiniCPM-V series, as well as multiple quantization and deployment forms such as GPTQ, AWQ, and AutoRound.

---


### 50. [Exo2EgoPose: Leveraging Exocentric Demonstrations for Vision-Language guided Egocentric 3D Hand Pose Forecasting](https://arxiv.org/abs/2607.15890)

**<font color=#1a73e8>作者：</font>** Zhaofeng Shi, Heqian Qiu, Lanxiao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perceiving multimodal cues and forecasting fine-grained actions from an egocentric (Ego) perspective is vital for applications like robot manipulation. However, previous studies either rely mainly on under-informed visual inputs to predict coarse human motions or follow the VRM/VLA paradigm, which suffers from insufficient robot data and the gap between human and robot embodiments. We observe that 3D hand pose naturally serves as a unified representation to bridge human-robot actions. Hence, we investigate an under-explored Vision-Language guided Egocentric 3D Hand Pose Forecasting (VL-EHPF) task, which aims to predict future Ego 3D hand poses from visual observations, a language instruction, and pose states. To overcome the limited field-of-view and highly dynamic motions in the Ego view, we propose a framework dubbed Exo2EgoPose, which innovatively leverages holistic and stable exocentric (Exo) demonstrations as guidance to compensate for partial and dynamic Ego-view cues. Specifically, we introduce a Dual-level Exocentric Reconstruction Module (DERM), which incorporates the paired Exo videos as supervision to reconstruct their video-level and chunked frame-level representations, thereby modeling spatial contexts and temporal dynamics. Then, the Global-to-Local Modulation Module (GLMM) utilizes the reconstructed hierarchical Exo representations for progressive feature refinement via attention mechanisms and adaptive modulation, enabling comprehensive Exo guidance for accurate Ego hand pose forecasting. Extensive experiments on \textit{AssemblyHands}, \textit{Ego-Exo4D}, and our newly constructed \textit{EgoMe-pose} benchmarks show the superiority of our method, which outperforms state-of-the-art methods by a large margin. Moreover, it demonstrates an effective human-to-robot transfer capability and yields improvements on the \textit{CALVIN} dataset. Code will be released.

---


> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-75](./part-02.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
