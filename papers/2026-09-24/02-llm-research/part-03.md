# 🧠 大模型相关研究 | 2026年09月24日

> 本类共 **206** 篇论文：已确认 **192** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-206](./part-05.md)

---

### 101. [Governed AI-Agent Coordination for Dementia Care: Architecture, Safety Contracts, and Evidence-Derived Workflow Verification](https://arxiv.org/abs/2609.25956)

**<font color=#1a73e8>作者：</font>** Francesca Medda, Hui Gong  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Dementia care increasingly involves connected sensors, medication devices, electronic records, and assistive technologies. Interoperability can transport observations but cannot maintain an accountable care state, reconcile evidence, determine who may act, or verify resolution. The shift from large language models to agentic engineering creates a systems opportunity: an external runtime can maintain memory across episodes, plan over goals and constraints, invoke tools, observe outcomes, and enforce governance. This paper presents Governed Closed-loop Agent Coordination (GCAC), an architecture for bounded agent participation in community dementia-care workflows. Evidence on care-coordination failures and policy obligations is translated into traceable system requirements. GCAC separates observation, governed memory, planning, deterministic policy enforcement, execution, and outcome monitoring through a typed event-memory-decision-action-outcome contract. A reference harness evaluates 18 evidence-derived traces covering missing records, medication conflict, caregiver reports, service failure, consent change, stale state, duplicate events, untrusted text, and suspected acute neurological change. GCAC satisfies all 18 contract oracles with zero policy-violating tool calls and correctly preserves obligations, rejects stale state, creates human hand-offs, and records workflow closure. Event-threshold and stateless-planner controls satisfy 2/18 and 1/18 oracles, respectively. Component ablations localise failures to the removed memory, policy, or versioning function. The results establish architectural conformance rather than clinical effectiveness and show how agentic systems can automate reconciliation, routing, documentation, and follow-up while preserving human authority over consequential care decisions.

---


### 102. [CausalLoss-Fin: Attributing Financial-Agent Loss to Decisions and Infrastructure Faults](https://arxiv.org/abs/2609.25960)

**<font color=#1a73e8>作者：</font>** Abhishek Sharma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When an agent handling a payment exception loses money, the agent-step attribution methods this paper compares against will name one of its actions. They will do so even when a settlement message was dropped and the agent never had a chance: they intervene on agent actions and do not expose infrastructure faults as intervenable variables, so every dollar they explain is charged to a decision. We take a benchmark whose fault process is explicit and replayable, decompose each episode's realised delivery schedule into named, individually repairable messages, and intervene on both the agent's choices and the infrastructure's. A telescoping identity splits any policy's loss exactly three ways: an infrastructure effect, a policy differential against the best implementable policy, and a reference-policy residual. Two of the three can be negative, so none is a share; Shapley then divides the first into signed allocations over individual messages. One result is structural and needs no corpus: an agent-only baseline identifies no infrastructure cause, because its model contains no variable that could name one. What 545 planted episodes across 3 policies measure is the size of that consequence. It misfiles 100% of infrastructure episodes and charges $114,383.40 to the agent. Repairing what it names recovers 0.0% of the available loss; repairing a minimal sufficient set recovers 100.0%. Scoring messages one at a time is not merely imprecise: 27.8% (95% CI: 23.3--32.3%) of episodes do not decompose additively. We evaluate deterministic programmatic policies rather than language-model agents, which is what makes replay exact and which limits external validity to stochastic agents. The prevalence figures are properties of this generator, not field rates.

---


### 103. [VideoX-Qwen: Data-Centric Instruction-Based Video Editing](https://arxiv.org/abs/2609.26015)

**<font color=#1a73e8>作者：</font>** JJiahang Li, Dingbao Shao, Xinyu Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Progress in general-purpose video editing depends on constructing large-scale paired supervision and effectively adapting video-generation backbones to instruction-driven editing. Unlike video generation, video editing must execute a requested transformation while preserving unrelated subjects, scene structure, motion, and temporal continuity. We present VideoX-Qwen, an integrated data-construction and model-training framework for general instruction-based video editing. Our scalable production pipeline organizes specialized generation and understanding models into complementary routes for addition, removal, replacement, and attribute editing, followed by quality screening and instruction enrichment. It produces more than 1.2 million directional video-editing records, including over 400,000 records in each major task group, with an automatic acceptance rate of 89%. The resulting corpus provides broad and structured coverage of common editing operations through a unified source-instruction-target interface. We further develop a unified Qwen-Wan editor that combines multimodal semantic conditioning with dense source-video latent guidance. A progressive image-video training strategy aligns the multimodal instruction interface, adapts the video generator to source-conditioned editing, and refines output quality with selected high-resolution data. In a 100-example comparison with UniVideo and Kling O1, VideoX-Qwen achieves the best mean result on nine of eleven reported metrics, including instruction following, editing quality, content preservation, structural and perceptual similarity, and video-distribution quality. Together, the large-scale data-production system and unified training framework provide a practical foundation for more capable instruction-driven video editing.

---


### 104. [CQ4OE: A benchmark for assessing LLM-assisted ontology generation from competency questions](https://arxiv.org/abs/2609.26029)

**<font color=#1a73e8>作者：</font>** Jiayi Li, Ziyuan Wang, Daniel Garijo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ontology generation from Competency Questions (CQs) is a central yet labor-intensive phase of Ontology Engineering. While large language models (LLMs) offer promising automation capabilities, current evaluations remain fragmented. Task formulations are heterogeneous, gold standards often lack fine-grained CQ provenance, metrics conflate lexical overlap with structural and logical adequacy, and reference ontologies are not always explicitly designed around the evaluation CQs. Here, we address these limitations with CQ4OE, a benchmark for the systematic and reproducible evaluation of LLM-based ontology generation from CQs. For each ontology in the benchmark, we build a CQ-driven gold OWL ontology with explicit provenance linking each CQ to the classes, properties, and axioms required to answer it. From this resource, we define two complementary evaluation tasks. CQ2Term supports term-level evaluation of CQ-specific class and property prediction over 99 CQs, and CQ2Onto supports ontology-level evaluation over 118 CQs, including hierarchy, property modeling, and axiom-level structure. We demonstrate CQ4OE with experiments using nine LLMs under zero-shot, iterative, and multi-agent generation strategies, showing that LLMs recover explicit vocabulary terms more reliably than creating ontologies, particularly in property modeling, hierarchy construction, and axiom generation.

---


### 105. [Domain-Adaptive Pretraining Enhances Water Treatment Semantic Representation for Large-Scale Structured Literature Mining](https://arxiv.org/abs/2609.26034)

**<font color=#1a73e8>作者：</font>** Mudi Zhai, Ruihong Qiu, Qingyun Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Water treatment research is expanding rapidly, but much of the knowledge acquired from this research remains scattered across unstructured literature. The field still lacks a dedicated language model that can efficiently capture water treatment-specific domain semantics for large-scale literature mining. Here, we address this by developing WaterBERT, a domain-adapted encoder model designed for semantic representation and structured information extraction from water treatment texts. WaterBERT was developed by continual pretraining on a large-scale water treatment corpus comprising about 2.97 billion tokens. Three fine-tuned models based on WaterBERT were systematically evaluated on downstream tasks, achieving the best overall performance among general-purpose and domain-specific BERT models, with F1 scores of 90.12% for multiclass treatment process classification, 79.50% for named entity recognition, and 74.04% for relation extraction. Beyond these benchmark tasks, we further demonstrated WaterBERT's advantages for large-scale literature processing. Applied to 5,144 Environmental Science & Technology articles, WaterBERT-BERTopic identified coherent, diverse, and domain-specific research topics without predefined categories. Building on WaterBERT, we processed 693,211 abstracts at substantially lower cost than commercial LLMs while retaining competitive extraction performance to construct a structured water treatment knowledge graph. The knowledge graph was then integrated with lexical and dense retrieval to develop a Water Knowledge-Enhanced Retrieval System (WaterKERS), which achieved a relevance score of 77.7, substantially outperforming text-based retrieval baselines (54.7-64.5). Through WaterBERT, this study provides a compact and scalable semantic foundation for large-scale information processing and evidence mapping in water treatment research.

---


### 106. [Truth for Believable AI: Expressed Doubt, Provenance, and Belief Revision as an Engineerable Stance](https://arxiv.org/abs/2609.26035)

**<font color=#1a73e8>作者：</font>** Sebastian Cochinescu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational agents often express answers in a uniformly confident register. We test whether expressed uncertainty, provenance-aware assertion, and explicit belief revision can be implemented as a behavior layer over a fixed language model; we do not test believability or trust. The layer combines three epistemic states, per-claim confidence and typed provenance, a provenance-gated expression rule, and a persistent revision store with auditable acknowledgments and partial resistance to false corrections. We evaluate it on a constructed, mechanically scored multi-session benchmark using a synthetic model and Qwen2.5-0.5B-Instruct. The synthetic instrument passes all five checks. On the real model, acknowledgment soundness, a by-construction guarantee, holds in 100% of cases, and true corrections are accepted more often than false ones (0.44 vs. 0.15 on held beliefs; 0.875 vs. 0.420 including rule-accepted corrections of unheld facts), but the pre-specified expression-fidelity, contradiction-separation, and provenance margins fail. A disclosed post hoc analysis shows that expression gated on mean answer-token probability ranks correctness below chance end to end (AUC 0.41, conversation-clustered), whereas gating on sampling consistency discriminates (AUC 0.66). A consistency-gated configuration selected from this finding and evaluated under a separately committed protocol meets the conversation-level manipulation and capability-equivalence criteria and replicates on a redrawn conversation set. The manipulation result is selection-dependent, and both criteria remain unresolved when uncertainty is clustered over the 60 facts. The supported conclusions are limited to the by-construction audit guarantee, store-dependent partial correction discrimination, and a benchmark- and model-specific failure of token-probability gating; scaling the fact base is required before human evaluation.

---


### 107. [FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents](https://arxiv.org/abs/2609.26048)

**<font color=#1a73e8>作者：</font>** Nikita Agarwal, Nivedit Jain  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents often reach a working solution and then fail to consistently deliver it. We study runtime policies: targeted natural-language instructions and action denials applied by the agent harness at states that preceded observed failures, without changing model weights or the user prompt. With this, keeping capability constant, we observe a meaningful unlock in delivered reliability. Across the complete 87-task Terminal-Bench 2.1 suite, with two attempts per task, policies increase repeated success (pass^2) in all three GPT-5.6 tiers: 50.6% to 54.0% for Luna, 55.2% to 60.9% for Terra, and 64.4% to 73.6% for Sol. Sol's best-of-two success changes by 1.2 points while repeated success rises by 9.2, showing that policies chiefly convert reachable solutions into dependable delivery. We further cover 14 tasks under Terra's frozen portfolio. Policy-guided Terra reaches 71.4%, compared with 64.3% for unassisted Sol, at about half the cost, demonstrating how engineering around models could unlock dependability for a use case. To isolate the mechanism we run a randomized five-arm experiment: real policies reach 61% on eligible tasks, versus 39% without a policy, 36% with a timing-matched sham, and 39 to 43% with generic verification or reconsideration. The intended corrective behavior appears in 22 of 24 coded policy attempts, against at most 14 in any other arm. Runtime policies are therefore a practical reliability layer: they make capabilities an agent already possesses substantially more repeatable.

---


### 108. [Optimizing Denoising Trajectories in dLLMs: A Lightweight Evolutionary Heuristic Approach](https://arxiv.org/abs/2609.26052)

**<font color=#1a73e8>作者：</font>** Zijian Zhao, Dian Jin, Xialiang Tong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (dLLMs) have recently emerged as a promising alternative to conventional Auto-Regressive (AR) Large Language Models (LLMs). By leveraging bidirectional attention and parallel decoding, dLLMs enable more efficient generation. However, they require a carefully designed denoising scheduler at inference time (absent during training) whose choice significantly impacts generation quality. While confidence-based heuristic schedulers have shown strong empirical performance, they suffer from two critical failure modes: EOS Overflow and Proximal Bias. Through in-depth analysis of the Transformer's attention patterns, we reveal that these failures stem from certain positions assigning disproportionately high attention weights to invalid tokens (e.g., [MASK] and [EOS]), which produce misleading confidence signals. Building on this insight, empirical evidence shows that valid attention scores can provide complementary guidance to conventional confidence-based heuristics, yet no single metric consistently excels across all scenarios, implying that the optimal denoising trajectory is highly context-dependent. To address this problem, we propose a lightweight evolutionary heuristic scheduler optimized using the Covariance Matrix Adaptation Evolution Strategy (CMA-ES). Our scheduler dynamically integrates multiple heuristic features with a contextual mean-field embedding, while requiring only 393 trainable parameters. Evaluated on LLaDA and Dream across four reasoning and planning benchmarks, our method consistently outperforms strong baselines, including conventional heuristics, block auto-regressive methods, and recent State-Of-The-Art (SOTA) approaches. To the best of our knowledge, it represents the most parameter-efficient neural scheduler to date. Our code is available at this https URL .

---


### 109. [CricRAG: Retrieval Augmented Vision-Language Models for Personalized Cricket Coaching](https://arxiv.org/abs/2609.26056)

**<font color=#1a73e8>作者：</font>** Agamdeep Singh, Sujit PB, Mayank Vatsa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) offer promising capabilities for automated sports coaching but face a fundamental limitation: they implicitly compare against professional standards, making their feedback impractical for developing players. We present CricRAG, a retrieval-augmented framework that aligns VLMs with skill-appropriate benchmarks for personalized cricket coaching. Our key insight is that by retrieving similar-but-better techniques as reference points, we can guide VLMs to provide developmentally appropriate feedback that mirrors human coaching practices. We contribute: (1) a labelled dataset of 288 cricket technique videos spanning multiple skill levels, (2) an efficient motion retrieval pipeline using contrastive learning that achieves 78% top-3 retrieval accuracy, (3) a frame sampling technique that reduces inference costs, and (4) a retrieval-augmented approach that significantly improves feedback alignment with coaching principles, achieving up to 94% agreement with professional assessments compared to 67% without retrieval context.

---


### 110. [ChainUQ: Reasoning Consistency-Aware Uncertainty Quantification for Large Language Models](https://arxiv.org/abs/2609.26060)

**<font color=#1a73e8>作者：</font>** Dahai Yu, Rongchao Xu, Lin Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While large language models (LLMs) exhibit impressive reasoning capabilities, response-level confidence may remain unreliable when intermediate claims conflict with the final conclusion. Therefore, effective uncertainty quantification (UQ) is required to capture logical inconsistencies within the reasoning chain, not just the correctness of the final output. Current approaches have two major limitations: (1) their reliance on token-level probabilities fails to capture reasoning consistency, and (2) they lack mechanisms to dynamically calibrate confidence using the structural logic of the generated chain. To advance existing research, we introduce ChainUQ, a reasoning consistency-aware uncertainty quantification framework for LLMs. ChainUQ consists of two key technical components: an alignment-aware lightweight UQ module that estimates a raw intrinsic model confidence score from frozen features aligned to the final conclusion, and a reasoning consistency-aware calibrator that refines this score using reasoning-chain consistency evidence. Evaluations across diverse in-distribution and out-of-distribution benchmarks show that ChainUQ consistently improves response-level uncertainty estimation, achieving an average 3.1% relative gain in AUROC and up to 45.0% relative reduction in ECE, and can be directly transferred to new settings without additional fine-tuning.

---


### 111. [Policy-Backed Selective Regeneration under Tainted Inter-Agent Communication](https://arxiv.org/abs/2609.26072)

**<font color=#1a73e8>作者：</font>** Jinghan Xu, Longze Fan, Zeyuan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Inter-agent communication is essential to multi-agent language-model systems, yet a single message may combine task-critical information with instructions not authorized by the original request. Prompt-based defenses leave enforcement to models exposed to adversarial messages, while indiscriminate message removal discards useful information. We introduce Executable Semantic Commitments with Clean-Room Recovery (ESC-CR), a policy-backed framework for secure inter-agent code generation and recovery. It separates message claims from authorization, constructs executable commitments from trusted tasks, evidence, and policy, and enforces them at an external release boundary. Upon a violation, ESC-CR taints the responsible message and rejected artifact, reconstructs a clean context from evidence-backed task information, and regenerates under the same policy. We evaluate ESC-CR across communication-essential and standard code-generation benchmarks, multiple model families and communication topologies, and adaptive attacks spanning direct, obfuscated, and verifier-aware payloads. Results show that polluted-context retry frequently fails to remove unauthorized influence, while complete message removal can discard information required by communication-essential tasks. ESC-CR preserves evidence-backed claims while suppressing unauthorized releases under matched computational budgets, and the same design transfers to end-to-end agent trajectories.

---


### 112. [Selection-Invariant Communication Compilers for Privacy-Aware Multi-Agent LLM Workflows](https://arxiv.org/abs/2609.26076)

**<font color=#1a73e8>作者：</font>** Jinghan Xu, Longze Fan, Zeyuan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Structured multi-agent workflows exchange intermediate messages whose content and form can reveal private state even when the final output is safe. We identify selection-channel leakage: after authorization fixes what may be released, a private-state-aware choice among semantically valid realizations creates an additional inference channel. We introduce the selection-invariant communication compiler(SICC), which constrains this post-authorization representation kernel rather than prescribing templates. Any deterministic or independently public-randomized generator satisfying the invariant is valid; requirement-indexed canonical forms are one auditable implementation. We prove a compositional communication-layer guarantee: authorization, public-only form generation, and a dependency-safe utility gate make the emitted transcript reveal no information beyond the complete authorized view. Private-state-aware selection remains vulnerable after surface-disjoint and length-matched controls. Across 132 AgentLeak communication replays and 100 executable LangGraph tasks, deterministic SICC retains complete protocol utility without a positive excess-gain signal; independent public randomization preserves the same result in AgentLeak and 480 controlled cases.

---


### 113. [CoVeR: Coverage-Based Routing of Verifier Calls in Agentic Retrieval](https://arxiv.org/abs/2609.26086)

**<font color=#1a73e8>作者：</font>** Daeyoung Roh, Donghee Han  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An agentic retrieval system issues a sequence of search queries and must decide, at each step, whether the evidence collected so far is enough to stop. Delegating that decision to an LLM verifier or a prompt judge makes stopping reliable, but the verifier then reprocesses the growing evidence after every retrieval step, a substantial repeated cost. We show that most of these calls can be skipped without materially changing answer accuracy: a single threshold on a frozen sentence-embedding coverage margin detects the states in which the evidence is still plainly incomplete, and the verifier is called only on the ambiguous remainder, a gate we call CoVeR (Coverage-based Verifier Routing). Across three multi-hop QA benchmarks, with the evaluation protocol fixed before the full-scale run, the CoVeR-gated agent matches the answer accuracy of both the full-budget agent and the always-verify baseline within a fraction of an EM point. It cuts 62-68% of verifier calls, and 93% in a saturated regime. Routers built on evidence counts, lexical overlap, or BM25 relevance, alone or learned in combination, give weaker overall trade-offs, the gate transfers without re-tuning across deciders and agent scales, and its drafter distills into a 921k-parameter head atop the frozen encoder, leaving no LLM in the routing loop. The same signal cannot replace verification: matching a claim is far easier than deciding the claim is supported.

---


### 114. [The Architect, the Adversary, and the Judge: Closed-Loop Generation of Standards-Aligned Assessment Items at Scale](https://arxiv.org/abs/2609.26087)

**<font color=#1a73e8>作者：</font>** Wenhui Chen, Ziyao Lin, Jianlin Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present CLAIM, a production pipeline for K-12 assessment-item generation coupling a two-stage generate-then-attack protocol (the model drafts as a "curriculum architect", then re-enters the same conversation as a hostile adversarial reviewer), bi-directional few-shot conditioning on accepted and rejected items, the latter carrying the evaluator's diagnosis, and a knowledge dictionary of 44,844 error-correction rules mined from that feedback and retrieved per standard and item type. Across 43,227 scored items over 755 Common Core ELA standards, three item types, and ten LLMs, the pipeline reaches a 97.8% expert-evaluator pass rate on a 9,074-item production run. We then ask what that rate certifies. Re-scoring a stratified sample with three judges from other vendors, blind to the deployed verdict, reproduces the format ordering under every judge and recovers a larger open-set deficit than the deployed evaluator does; but agreement on the accept/reject binary is weak at production prevalence (kappa about 0.13), and the judges agree with each other no better. The level is therefore judge-relative, and with no student-response data our quality evidence is evaluator-judged throughout. The corpus also exposes a robust asymmetry. Multiple-choice and multiple-select generation saturate at 98% or above for both frontier models under a dozen static rules, whereas fill-in-the-blank generation is capability-tiered (82.8-96.7% across five models under a matched rule set, standards, and judge) and plateaus under prompt-only optimization, with error mass shifting between answer-key over-inclusion and omission as rules accumulate. We analyze this as open-set boundary determination, a task autoregressive decoders are structurally ill-equipped to solve, and show the asymmetry recurring when the evaluator itself is distilled: fail-recall rises from 8% to 63% while F1 saturates at 0.25.

---


### 115. [SpecialEduBench: Benchmarking Vision-Language Models on Knowledge, Skill, and Attitude in Language Intervention for Autistic Children](https://arxiv.org/abs/2609.26090)

**<font color=#1a73e8>作者：</font>** Jihoi Na, Taeyeong Kim, Sungjune Kong 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language is the target of most early intervention for autistic children. Because the goal and the method change from child to child, the work falls to a teacher who takes one child at a time and judges each scene as it unfolds. Artificial intelligence is now being brought to that work, yet the benchmarks that reach special education ask what a model knows rather than what it does in front of a child. Building one is not straightforward, since whether a response is good teaching depends on what the child has just done, so no answer key applies. The evidence that settles it is visual as much as verbal, since the length of a wait, a shift of gaze, and the child's uptake leave no trace in a transcript. We introduce \emph{SpecialEduBench}, which measures pedagogical competence along knowledge, skill, and attitude, with 4,537 knowledge items and with 200 skill items and 68 attitude items built on recorded intervention, the attitude items crossing pressure with monitoring into 192 response cells. Seven special-education experts wrote, scored, and reviewed the items, and we revised the judge model's instruction against the reference scores they set. Across eight frontier vision-language models no axis is saturated, since the strongest still fails about a tenth of the honesty cells. The models converge where the knowledge is factual and separate where the task is situated, and the failures gather where pressure is applied. We intend the benchmark as an audit to run before deployment and as a starting point for models built for this domain.

---


### 116. [From Bilinear to Linear: Differentially Private Federated LoRA via Low-Dimensional Parameterization](https://arxiv.org/abs/2609.26091)

**<font color=#1a73e8>作者：</font>** Lele Zheng, Ruijie Hu, Tao Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated Low-Rank Adaptation (LoRA) provides an efficient solution for finetuning large language models across distributed and privacy-sensitive data. However, despite avoiding raw data sharing, federated LoRA remains vulnerable to privacy leakage through transmitted model updates. Differential privacy (DP) mitigates such leakage, but integrating DP into federated LoRA introduces two fundamental challenges: aggregation mismatch from independently averaging low-rank factors, and quadratic noise amplification when noise is injected into both factors. To address these challenges, we propose FedHSIP, a differentially private federated LoRA framework based on a unified low-dimensional parameterization. FedHSIP reformulates all LoRA parameters into a shared low-dimensional trainable vector, enabling clients to optimize and communicate only low-dimensional updates. This reformulation transforms federated LoRA from a bilinear factor aggregation problem into a unified linear parameter space, thereby eliminating aggregation mismatch and preventing the quadratic amplification of DP noise. To further handle non-IID data, we introduce a heterogeneity- and sensitivity-aware isometric projection, constructed from warm-up statistics, which groups coordinates with compatible cross-client update patterns while balancing sensitivity, update energy, and heterogeneity across the low-dimensional space. Extensive experiments on natural language understanding and generation benchmarks show that FedHSIP consistently outperforms existing federated LoRA methods under both private and non-private settings, achieving up to 3-4% improvements under differential privacy while reducing communication cost by over 80% and maintaining robustness under heterogeneous data distributions.

---


### 117. [RECAP: Relation Evidence Calibration for Detecting Spatial Relation Hallucinations in Vision-Language Models](https://arxiv.org/abs/2609.26093)

**<font color=#1a73e8>作者：</font>** Feixiang Liu, Qiang Qiu, Qingyang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models can answer spatial relation questions confidently even when the image supports an incompatible relation. We formulate relation-grounded selective prediction: accept or reject an already-produced yes/no answer by auditing its visual support, rather than treating uncertainty as evidence. RECAP, our relation-evidence calibration framework, compares image-conditioned likelihoods for a claim, its semantic contradictions, and optional one-sided supports, then converts these witnesses into an answer-conditioned rejection risk. A calibration-only gate preserves confidence as a veto when confidence is demonstrably informative and otherwise deploys relation evidence alone. Across 20 group/image-disjoint splits, RECAP lowers H-FPR@80 over confidence by between 2.0 and 17.9 points on VSR and raises Acc@80 by 3.0, 8.6, and 12.6 points on What'sUp for Qwen3-VL-8B, InternVL3.5-8B, and LLaVA-1.5-7B. It outperforms matched VCD-style visual contrast on all four primary metrics in all six settings. Full-pool VSR fallback, target-ranked GSR-Bench transfer, equal-budget supervised controls, and two additional checkpoints show a consistent operating principle: structured counterevidence complements certainty when confidence is misaligned, while the gate retains confidence when it is already useful.

---


### 118. [CoEvo: Oracle-Grounded Self-Evolution of a Single Model for Multi-Step Causal Reasoning](https://arxiv.org/abs/2609.26094)

**<font color=#1a73e8>作者：</font>** Jian Zhang, Bingyi Wang, Yizhi Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-step causal reasoning requires chaining inferences where each step constrains the next. An early error propagates silently, and a correct answer reached via flawed logic evades outcome-level detection. In specialized domains, teacher LLMs err on intermediate steps, safety constraints restrict cloud distillation, and shifting conditions demand adaptation, leaving self-evolution as the practical route. Naive self-evolution can collapse: outcome-only rewards let the model exploit distributional shortcuts, and weak self-evaluation reinforces spurious paths into stable failure patterns. We exploit a key asymmetry: generating a correct chain is hard, but verifying a single step is easy. Many high-stakes domains admit a deterministic, queryable oracle, a physics simulator or rule engine over codified constraints. It checks asserted steps without teacher-level ability and abstains beyond its rules; it can check what the model asserts, never replace it. This enables CoEvo, an oracle-grounded self-evolution framework where a single model alternates between Proposer and Solver. As Solver, the model generates competing chains; intra-group debate exposes disagreement steps, a proxy for the capability boundary, and the oracle adjudicates them into process-level supervision. As Proposer, the same model constructs progressively harder scenarios inside oracle constraints, steering the curriculum toward deep multi-hop chains. Both roles are updated jointly, so training pressure co-evolves with the model. On industrial, clinical, and legal multi-step causal reasoning benchmarks, CoEvo enables an 8B LLM to sustain self-evolution, surpassing distillation baselines and the strongest proprietary reference on path correctness (82.1% vs. 71.4%). The trained model generalizes to unseen categories and systems, preserving root-cause accuracy.

---


### 119. [One Domain, Many Tongues: Composing Domain and Language LoRAs for Cross-Lingual Remote-Sensing MLLMs without Paired Data](https://arxiv.org/abs/2609.26097)

**<font color=#1a73e8>作者：</font>** Xuechen Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Remote-sensing (RS) multimodal large language models (MLLMs) are trained and evaluated only in English, while text-only instruction data covers over 100 languages. We propose MODL (Mutually Orthogonal Domain-Language composition), a recipe that adds new languages to an English RS MLLM without a single multilingual RS example: a domain LoRA trained on English RS imagery and a language LoRA trained on text alone are learned jointly, under one loss term that keeps the two updates mutually orthogonal at every layer throughout training. This constraint is the recipe's active ingredient. Without it, the same training answers RS questions correctly but in English, erases much of the base model's multilingual text ability, and diverges on one seed in three; sixteen alternatives, from training-free merging to prior orthogonality variants, fail the same way. MODL repairs every failure on every seed: answers are correct and in the target language 56-71% of the time, where the best alternative reaches 27% and most stay below 8%, text ability stays at the level of the untrained base, and on Spanish it surpasses Qwen2.5-VL-7B, with zero multilingual-multimodal data. A single five-language adapter retains English, Spanish, and Vietnamese at full strength across three seeds; non-Latin scripts remain an open boundary.

---


### 120. [Test-time Reinforcement Learning for Anomalous Video Understanding](https://arxiv.org/abs/2609.26099)

**<font color=#1a73e8>作者：</font>** Huining Li, Yuxiang Duan, Jiyang Tan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anomalous video understanding aims to identify abnormal events in videos and interpret their semantic meanings beyond simple anomaly detection. Recent video large language models (Video-LLMs) have demonstrated promising zero-shot capabilities for this task, yet their performance remains limited due to insufficient adaptation to diverse anomaly patterns and evolving environments. Test-time reinforcement learning offers a promising solution by enabling models to improve through self-generated feedback signals without requiring additional human annotations. However, applying it to anomalous video understanding remains challenging due to three issues: (1) generated pseudo-labels can be unreliable when consensus is weak; (2) binary reward designs fail to capture uncertainty in model generations, resulting in ineffective optimization signals; and (3) unanimous rollout groups receive identical rewards, causing group-relative advantages to collapse and eliminating effective policy-gradient signals. To address these challenges, we present a novel test-time reinforcement learning framework for anomalous video understanding by introducing dual-query consistency filtering, an entropy-aware consensus reward, and a virtual negative anchor mechanism. The framework retains reliable samples through consistency across semantically equivalent queries, combines answer agreement with generation uncertainty for reward estimation, and introduces a virtual negative anchor to create reward variation in unanimous rollout groups, thereby preserving effective group-relative optimization signals. Experiments on VAU-Bench show that our method outperforms the compared frozen and supervised baselines. The gains are most pronounced on the ECVA subset of VAU-Bench with thinking, where accuracy improves from 75.81% to 90.00% relative to the frozen backbone.

---


### 121. [TSS: Target-Side Sparsification for Speculative Decoding in Domain-Specific Large Language Models](https://arxiv.org/abs/2609.26100)

**<font color=#1a73e8>作者：</font>** Haibo Hu, Lianming Huang, Qiao Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model inference through collaboration between a lightweight draft model and a target verifier. Existing methods mainly improve the draft side, while the target model is typically kept dense and unchanged. We show that, under domain-specific inference, full-depth target verification is not always the optimal choice. Counter-intuitively, skipping selected target layers can reduce verification cost while simultaneously increasing draft acceptance and preserving, or even improving, downstream task performance. Based on this observation, we propose TSS, a target-side sparsification framework for speculative decoding. TSS employs an acceptance- and metric-aware breadth search to explore multi-layer skip configurations without imposing a fixed priority between the two objectives. The selected configurations are stored in a domain-to-configuration mapping and applied by a lightweight skip controller, allowing one complete target model to support multiple sparse verification paths without retraining or permanent parameter pruning. Experiments on Spec-Bench across multiple domains, model scales, and speculative decoding methods show consistent improvements in draft acceptance and downstream task performance. In Translation setting, TSS increases the average accept length from 2.70 to 4.53 (+67.8%), improves BLEU from 0.131 to 0.237 (+80.9%), and raises end-to-end throughput from 75.6 to 127.3 tokens/s, corresponding to a 1.68X speedup.

---


### 122. [Differentiable Fuzzy Inference Layer: A Monotone, Compositional Ordinal Reasoning Head for Large Language Models](https://arxiv.org/abs/2609.26113)

**<font color=#1a73e8>作者：</font>** Zhen Zhang, Amr Alanwar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A state-of-the-art language model asked to interpret "most of most students passed" typically answers "most," though composing two instances of "most" yields a proportion closer to "some." We trace this failure to an architectural choice rather than a data deficit: standard classifier heads treat ordinal categories as independent labels, with no mechanism to respect their natural ordering or compose them algebraically. We introduce the Differentiable Fuzzy Inference Layer (DFIL), a dual-path prediction head pairing a standard classifier with a scalar-bottlenecked branch grounded in a bank of ordered membership functions. DFIL supplies two structural primitives that a label-only head cannot inherit: monotonicity in the underlying quantity, and compositional reasoning via t-norm operations without any compositional training data. The scalar branch additionally provides an interpretable interface for analyzing residual errors. We instantiate DFIL on ordinal natural-language tasks across diverse LLM families.

---


### 123. [DTOC: Dynamic Tool Output Compression for Adaptive Context Management in AI Agents](https://arxiv.org/abs/2609.26121)

**<font color=#1a73e8>作者：</font>** Abhay Chaturvedi, Shreya Bhattacharya, Rashmika Gopalkrishnan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agent capabilities have grown, practical limitations increasingly stem from constrained context windows rather than model capacity. Common strategies, such as truncation, heuristic aging, and lossy summarization, may discard useful information or introduce hallucination risk. To address these challenges, we propose Dynamic Tool Output Compression (DTOC), a framework for scalable context management in LLM-based agents that models context updates as explicit and reversible operations within the agent reasoning loop. DTOC retains full tool outputs in external memory while inserting compact placeholders into the active context, enabling selective reconstruction when needed. We formalize the DTOC mechanism, integrate it into a ReAct-style agent architecture, and provide a production-oriented implementation supporting on-demand restoration of compressed outputs. Experiments on DeepSWE reveal model-dependent effects: for responsive models (Sonnet 4.6, GPT-5.4), DTOC reduces input tokens (10.3 and 12.7%) and agent steps (2.4 and 32.3%), while increasing solve rates (2.5 and 1.5 times higher) and lowering cost per solved task (3 and 3.5 times lower cost per solved task). For the other models results are more mixed, with GPT-5.5 doubling solve rate and halving cost, but no impact on solve rate and negative impact on cost for the other models. Ablation results show reversibility is critical: disable-only compression variants degraded performance, while full DTOC recovered baseline accuracy at substantially lower context cost. These findings indicate that explicit, reversible context management can improve the efficiency of long-horizon agent reasoning without degrading task performance.

---


### 124. [MAC-RRG: Iterative Multi-Agent Collaboration for X-ray Radiology Report Generation](https://arxiv.org/abs/2609.26124)

**<font color=#1a73e8>作者：</font>** Futian Wang, Yuhan Qiao, Xiao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite the remarkable progress of LLM-based and knowledge graph-augmented Radiology Report Generation (RRG) methods, existing techniques still suffer from inherent defects. Conventional LLM-only models lack structured medical prior knowledge, resulting in frequent medical hallucinations and low diagnostic interpretability. Current knowledge graph-enhanced schemes adopt static one-round knowledge fusion with single-source knowledge, incapable of dynamic knowledge updating according to generation feedback. This paper proposes a novel Multi-Agent Collaborative iterative framework for X-ray Radiology Report Generation, termed MAC-RRG. Inspired by multi-agent technology, our framework constructs a closed-loop optimization paradigm based on task decoupling and collaborative reasoning. Specifically, the framework first generates a preliminary radiology report from input X-ray images via a vision encoder and a basic LLM. Subsequently, a multimodal knowledge graph (MM-KG) agent mines structured disease correlation and anatomical knowledge from medical knowledge graphs, while an auxiliary knowledge agent extracts unstructured domain knowledge from public medical databases. The multi-source knowledge acquired by dual agents is fused and embedded to guide the LLM in iteratively refining the initial report. Extensive quantitative and qualitative experiments on mainstream X-ray RRG datasets, including IU X-ray, MIMIC, and CheXpert Plus, fully verify the superiority of our proposed method. The source code and pre-trained models have been released on this https URL

---


### 125. [VACS: Value-Aligned Compositional Shielding for Multi-Agent Reasoning](https://arxiv.org/abs/2609.26135)

**<font color=#1a73e8>作者：</font>** Yiyao Zhang, Diksha Goel, Hussain Ahmad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent reasoning systems in high-stakes domains must be both accurate and safe, yet agents often follow heterogeneous value priorities (e.g., rigor, conciseness, safety), causing conflicting recommendations. Existing methods do not jointly provide: (i) principled inference of each agent's implicit values from behavior, (ii) compositional formal safety guarantees without full online communication, and (iii) value-aware conflict resolution with faithful explanations. We present VACS (Value-Aligned Compositional Shielding), a four-layer framework addressing all three. Layer 1 learns value-dimension rewards from pairwise preferences using Bradley-Terry modeling and infers per-agent value weights via deep MaxEnt IRL. Layer 2 encodes value constraints in a Lean-inspired DSL and synthesizes compositional assume-guarantee shields for runtime safety. Layer 3 resolves disagreement through nucleolus-based credit allocation and Hamiltonian consensus optimization under long-term value constraints. Layer 4 extracts a critical reasoning path from co-state sensitivities and generates formally grounded natural-language explanations. Our contribution is primarily a unified systems design with formalized interfaces and operational guarantees at the verifier-constrained decision level, rather than a complete end-to-end formal proof of all language-model internals. In controlled proof-of-concept evaluations with role-conditioned agent panels on NEJM-AI QA, MathInstruct-Subset, and a cybersecurity incident-response benchmark (CyberSec-Eval), VACS outperforms strong baselines in accuracy (85.4%, 95.0%, and 90.0%) while reducing logical inconsistency rates to near zero.

---


### 126. [Block-Level Weight-Space Structure Persists Under Post-Training: An Empirical Study Across LLM Families](https://arxiv.org/abs/2609.26147)

**<font color=#1a73e8>作者：</font>** Zhaohui Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern LLMs are deployed as families of post-trained variants (base, instruct, chat, code) derived from a shared set of pre-trained weights. We present an empirical study of how post-training transforms weight-space geometry, covering eight configurations across four architecture families (Qwen2.5, Llama-3.1/3.2, Mistral, Gemma-2). We identify a granularity gap: post-training modifies every tensor (zero of 291-339 tensors remain byte-identical, so hash-based deduplication achieves 0% savings), yet preserves block-level structure (mean cosine similarity exceeds 0.99 and relative Frobenius distance stays below 0.13). Post-training therefore acts as a structured perturbation that shifts every parameter while leaving block-level geometry intact. The property is not universal: independently trained specializations (for example, Qwen2.5-Coder) attain cosine similarity around 0.64 with the general base, indicating a disconnected region of weight space. Perturbation magnitude varies systematically with model scale, architecture family, and post-training recipe. As a practical application, we build LinkerLLM, a lazy loader that aliases shareable blocks across co-resident variants, achieving 18-48% GPU memory savings and enabling up to five 7B-parameter variants on a single 24 GB consumer GPU. Five of eight configurations retain at least 94% of the unshared variant's quality on MMLU, ARC-Challenge, HellaSwag, and WinoGrande; the remaining three (Mistral-7B, Gemma-2-2B, Llama-3.2-1B) have one below-threshold benchmark each (87-91%), which we report transparently rather than gate the block-sharing decision on a single threshold.

---


### 127. [Spectral Tail Interventions in Decoder-Only Language Models: Reasoning-Sensitive Weight Structure from Controlled Surgery](https://arxiv.org/abs/2609.26165)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Sanjida Akhter, Md Najmus Swaqeeb 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight-space structure often correlates with language-model behavior, but correlation alone does not establish computational involvement. We study concentrated upper spectral tails in decoder-only transformers through controlled interventions. At a fixed relative offset, we derive a finite-width conditional bound linking the inverse participation ratio of squared singular values to central pre-softmax logit kurtosis. We then define a pointwise query--key ($QK$) product-tail target and compare independent factor surgery with a product-targeted factorization that preserves native attention computation. Across three base checkpoints and five reasoning benchmarks, plus an instruction-tuned Phi checkpoint analyzed separately, the learned-tail edit is more damaging than the mean of five fixed spectrum-matched Haar controls in all 20 model--task cells. Eighteen paired contrasts remain significant after Holm correction, while two are directional but inconclusive. Product-targeted factors attain higher held-out tail-subspace fractions, providing an empirical bridge between product- and factor-level interventions. Component isolation identifies contributions from $QK$, value--output, and multilayer-perceptron blocks, although the theorem covers only $QK$. In separate studies, inverse participation precedes pooled accuracy transitions under a matched crossing rule, and residualized tail-aware low-rank adaptation (LoRA) reaches targets earlier than standard LoRA and PiSSA while final-score intervals overlap. Conclusions are restricted to the evaluated checkpoints, layers, tasks, interventions, and controls.

---


### 128. [TRACE: Transparent Retrieval for Abstract Concept Evaluation](https://arxiv.org/abs/2609.26168)

**<font color=#1a73e8>作者：</font>** Joseph Bingham  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent work reports that vision--language models (VLMs) struggle to establish and maintain stable reference in repeated reference games. Rather than ask which VLM does best, we ask a more basic question: do you need a large pretrained VLM for this at all? On grounding a single director utterance to one of twelve tangram silhouettes, we compare six off-the-shelf VLMs against a transparent baseline that uses \emph{no learned visual representation}: classical SIFT keypoint matching and a signal-quality index over retrieved images. On identical trials, the transparent baseline matches the strongest VLM (SigLIP-large) and significantly outperforms the other five, including every CLIP and OpenCLIP variant. The baseline additionally retrieves external images, so this is not a matched-information comparison; what it shows is that a learned \emph{visual} representation is not the bottleneck for this task: given retrieved images, a shape-appropriate classical similarity suffices. Along the way we find that abstract-grounding ability varies widely across VLMs (15--39\% top-1; chance 8.33\%, humans $\approx$77--80\%), so the weakness is model-specific rather than intrinsic to contrastive pretraining; on the 1{,}013-shape KiloGram benchmark the pattern generalizes for CLIP, with per-shape difficulty tracking human shape-nameability. The pipeline is a classical, inspectable alternative rather than a learned one. We close by sketching how an explicit, inspectable representation of listener-side pact state could carry this approach into interactive multi-turn reference, which we leave to future work. Code available in supplementary material.

---


### 129. [Component Type, Not Reconstruction Error, Predicts Attention Quantization Sensitivity](https://arxiv.org/abs/2609.26173)

**<font color=#1a73e8>作者：</font>** Kasun Dewage, Marianna Pensky, Suranadi De Silva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many post-training quantization (PTQ) methods use layer-wise reconstruction, second-order proxy objectives, or activation-aware transformations to reduce quantization-induced error. Whether that error signal predicts the downstream functional impact of quantizing an individual attention projection has not been directly characterized. We sweep nine open-weight language models (1.3B--8B parameters; OPT, GPT-J, LLaMA-1/2/3, Mistral, Qwen 2.5) and quantize one attention projection at a time under round-to-nearest (RTN) and, for seven models, GPTQ at 3 and 4 bits, recording reconstruction error, perplexity change, and per-projection activation-weighted quantization error for 3,808 distinct measurements. We find: (1) within a given component type (Q, K, V, or O), reconstruction error explains less than 10% of the variance in perplexity sensitivity in 27 of 36 cases under RTN, with median R^2 = 0.044; (2) both component type and layer identity explain more variance than reconstruction error in all 9 models, with layer identity the strongest predictor in 7 of 9 models and component type strongest in the remaining 2; (3) value (V) projections are the most commonly dominant component, accounting for 38--51% of total positive Delta PPL in seven of nine models; (4) the dominant component is broadly preserved between RTN and GPTQ (5 of 7 cases); and (5) activation-weighted quantization error is a moderately better within-component predictor than reconstruction error for V projections specifically (median R^2 of 0.20 vs. 0.06). These findings indicate that relative weight reconstruction error alone is insufficient for sensitivity-aware bit allocation, and that V projections merit dedicated consideration in mixed-precision schemes.

---


### 130. [The Uncontrolled Variable: Vision-Language Model Refusal Responds to Image Presence in Ways Risk Cannot Explain](https://arxiv.org/abs/2609.26174)

**<font color=#1a73e8>作者：</font>** Haoyu Zhang, Yi Feng, Shibo Zheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision-Language Model (VLM) safety is expected to depend on what a request asks for. We show that safety-aligned VLMs also key refusal on a property of a request's form: whether an image is attached, holding everything the request asks fixed. Attaching a blank canvas - unreadable, unrelated to the request, identical across prompts - shifts refusal by tens of percentage points, with no defense in the loop.
The shift is not blanket caution. Neutral instructions are almost unaffected while borderline-benign prompts move sharply, so the cost falls on sensitivity-adjacent traffic: benign questions about privacy, self-harm and violence. Attachment alone is sufficient, while the image's properties set the price: a black canvas costs substantially more than a white one of identical size, and on an open checkpoint the carrying axis is pixel count. Nor is the shift under instructional control - telling the model the image is a placeholder to be disregarded removes only a fraction of it, and on one model asserting that an attachment exists moves refusal substantially with nothing attached.
Attachment may correlate with risk in deployment; what these models do with it does not track risk. It is not the serving stack, since the same weights reached two ways behave alike, nor a property of VLMs as such, since several open-weight checkpoints show nothing. It belongs to particular aligned checkpoints, one of them open. It is also decoupled from what it buys: the canvas does prevent some attack success on a matched harmful set, but far less than it costs, and its sign is not fixed - on one open model the identical canvas makes the model markedly easier to attack. Image presence is not a default a deployer chose or priced; it is an uncontrolled variable inherited with the weights.

---


### 131. [EADC: Evaluation of Advanced and Deep-level Compliance in Large Language Models](https://arxiv.org/abs/2609.26175)

**<font color=#1a73e8>作者：</font>** Yan Zhang, Ruien Li, Yaoyao Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have been used in various industries. However, ensuring their compliance with complex laws and regulatory frameworks remains a great challenge. Existing evaluation paradigms mainly rely on static benchmarks that suffer from three severe limitations: First, the compliance rules being used do not comply with the requirements of Artificial Intelligence (AI) laws and regulations; Second, they only handle apparent, explicit compliance risks, leaving implicit and covert compliance risks undetected; Third, they fail to track the systematic propagation of risks along logical dependency chains or evaluate compliance within nuanced, context-based real-world scenarios. To bridge this critical gap, we introduce EADC, a novel advanced evaluation benchmark of LLMs based on an AI compliance knowledge graph and AI compliance legal experts. By mapping abstract legal rules into structured logical multi-relational graphs, our framework enables automated, evolving agents to distill and synthesize highly sophisticated adversarial scenarios. This compliance benchmark is reviewed and corrected by human AI legal experts throughout the whole process. The resulting dataset (4,435+ QA pairs) provides an extensive, multi-dimensional taxonomy covering critical regulatory frontiers, including bias and discrimination, fairness, personal privacy protection, and values. Crucially, our compliance dataset moves beyond shallow string-matching by incorporating contextual long-horizon interactions and logic-driven hazard chains, capturing deeply embedded compliance anomalies that bypass traditional filters. Experiment evaluations demonstrate that our framework exposes critical regulatory blind spots in state-of-the-art LLMs, offering a rigorous, AI laws and regulations-aligned benchmark to safeguard high-level and deep compliance in the application of LLMs.

---


### 132. [Magnitude Profile Pruning: Calibration-Free Structured Attention Head Removal for Transformer Compression](https://arxiv.org/abs/2609.26177)

**<font color=#1a73e8>作者：</font>** Kasun Dewage, Marianna Pensky, Heranga K. Rathnasekara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured pruning of attention heads provides a hardware-friendly way to compress Transformer language models. However, existing methods for measuring head-level importance require calibration data, gradient computation, or Hessian estimation. These requirements add extra overhead and make the methods depend on the data. Our work presents Magnitude Profile (MP) scoring, a training-free criterion for head importance that identifies dispensable heads through statistical outlier detection on weight row norms. Heads whose projection weights fall within the population bulk are pruned, while heads exhibiting outlier norms, which carry disproportionate representational capacity, are preserved. Our work further gives MP-G, a variant that handles Grouped Query Attention (GQA) by distributing shared key-value group scores across associated query heads. Across five models evaluated on WikiText-2 perplexity at 12.5%-50% head sparsity, MP-G achieves the best perplexity on OPT-6.7B at all sparsity levels (18.46 at 12.5%, 27.87 at 25%, 152.0 at 50%). MP-G also gives the best results on RoBERTa-large at 12.5% and 25% sparsity, with perplexity values of 7.27 and 10.28, outperforming calibration-dependent baselines including Wanda-Head, SparseGPT-Head, and Gradient-Head. It requires zero forward passes, calibration samples, or gradient computation. At 50% sparsity, head pruning yields up to 16% parameter reduction with 50% attention FLOP savings. Our results show that weight-only statistical scoring can match or outperform data-dependent methods for structured head pruning, providing a practical, zero-cost criterion for Transformer compression.

---


### 133. [Modality-Gated Deep Adapters: Adding a Modality to a Frozen Embedding Model with Exact Preservation](https://arxiv.org/abs/2609.26182)

**<font color=#1a73e8>作者：</font>** Abdul Basit Tonmoy, Kazi Fardinul Hoque, Md. Shahrier Islam Arham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal embedding models are deployed at scale: retrieval indices, benchmark results, and behavioral audits all depend on the base model's exact outputs. Extending such a model to a new modality with existing parameter-efficient methods silently changes those outputs; LoRA-style adaptation rewrites the text path whether or not the weights are merged, invalidating every stored embedding. We propose modality-gated deep adapters: bottleneck adapters attached to every decoder layer of a frozen multimodal embedding LLM, grouped into per-modality packs that execute only while their own modality is being encoded. The result is a modality added with zero change to existing outputs: inputs no pack claims traverse the base model's own computation graph, bit-for-bit unchanged, and co-loaded packs compose with an exact-zero isolation matrix. Both properties are stated as propositions, hold after arbitrary training rather than only at initialization, require no task labels or routing metadata at inference, and are verified by exact-equality tests on the released checkpoints. On one frozen 2B base, the audio pack (injected as connector tokens) improves audio-to-text R@10 by +3.4 to +5.4 points over an identically trained control, positive at every seed and reproduced at eleven times the data; the thermal pack, reusing the base's own frozen vision path, clears its pre-registered acceptance gate roughly sevenfold at every seed and lifts thermal-to-text R@10 from 0.224 to 0.785. An encoder swap locates the missing capacity: an external audio encoder that outranks Whisper-family encoders in CLAP-style comparisons loses by 16 R@10 points inside the frozen LLM, so the capacity belongs in the layers, exactly where the gated adapters place it. We release the audio model, the thermal pack, and the training, evaluation and invariance suites: models at this http URL, code on GitHub.

---


### 134. [Identifying Intelligent Processes via Online Sequential Testing](https://arxiv.org/abs/2609.26193)

**<font color=#1a73e8>作者：</font>** Aritra Das, Debayan Gupta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Active sequential hypothesis testing studies how to identify an unknown hypothesis with a given set of sensing actions. We study this in the setting of identifying large language models (LLMs), \textit{i.e.}, if a user is conversing with an LLM drawn from a known set of models, how can they identify which one is in use? Here, the available sensing actions (evaluations) are themselves a design choice: an evaluator must first decide which environments and prompt families to construct, and only then decide how to use them sequentially. We formalize these two levels as an outer probe-design problem and an inner identification problem. Simply put, the outer stage selects a set of probes to be sent to the entire set of models, creating a kind of fingerprint dataset. This is followed by the inner stage, which sequentially sends a budget-minimizing set of those probes to identify the model in use. For the outer problem, we show that selecting which evaluations to construct at minimum cost, so that every pair of candidates is distinguished, is exactly a weighted set cover problem. Since the response distributions of the candidate models are not known exactly but only through calibration samples, we give a one-shot procedure that estimates the cover instance from these samples. For the inner problem, we bound the number of evaluations needed to identify the unknown model in terms of how well the available evaluations distinguish each pair of candidates.

---


### 135. [LLaVA-Assessor: Building the Foundation LMM For Visual Quality Assessment](https://arxiv.org/abs/2609.26205)

**<font color=#1a73e8>作者：</font>** Ziheng Jia, Zicheng Zhang, Jiaying Qian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aligning with the human visual system~(HVS) in perceiving and evaluating the quality of visual signals is a central objective of machine-vision-based visual quality assessment systems. With the rapid progress of large multi-modal models~(LMMs), visual question answering provides a promising paradigm for building unified foundation models for visual quality assessment under multi-modal and multi-task scenarios. Inspired by the classical ``perception-decision" process in HVS-based quality evaluation, we formulate visual quality assessment for LMM-based machine vision as two complementary tasks: ``quality interpretation'' and ``quality scoring". Centered on these objectives, we propose LLaVA-Assessor, a unified data construction and model training system. To support multi-modal inputs, we design an adaptive model architecture that enables efficient processing of both images and videos. For data construction, we develop rigorous human annotation protocols and a novel machine-synthesis-dominated data expansion pipeline to build a large-scale and high-quality datasets. Furthermore, we introduce a simple yet effective prompt disentanglement strategy to alleviate training-objective confusion in multi-task learning, thereby enabling stable and coherent joint training. The resulting all-in-one LMM LLaVA-Assessor-GIGA achieves superior performance on $11$ image/video quality scoring test sets and 4 visual quality interpretation benchmarks. Extensive results demonstrate the effectiveness of integrating structured data construction, adaptive model design, and multi-task joint training for automated visual quality assessment. Our work provides compelling insights for developing foundation LMMs for automatic visual quality assessment. Project page at this https URL.

---


### 136. [Beyond Static Charts: Can Language and Vision Language Models Generate Interactive Data Visualization Interfaces?](https://arxiv.org/abs/2609.26208)

**<font color=#1a73e8>作者：</font>** Mizanur Rahman, Aaryaman Kartha, Enamul Hoque Prince  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data visualization is central to analytical reasoning, but real-world analysis increasingly requires language-driven interactive interfaces rather than static charts. Although recent large language and vision language models (LLMs/VLMs) have shown promise in generating static charts from natural language, their ability to generate interactive data visualization interfaces remains largely unexplored due to the lack of benchmarks. We introduce VIS-GEN, a benchmark for evaluating how well LLMs/VLMs can generate interactive visualization interfaces from natural language queries. VIS-GEN comprises 3,042 samples covering diverse analytical intents, including data filtering, temporal analysis, and visualization editing, each paired with dataset metadata and natural language queries that are designed to reflect realistic, goal driven data exploration scenarios. We benchmark 14 state-of-the-art open-source and closed-source LLMs/VLMs, revealing large performance gaps and frequent failures on queries involving implicit intent, multiple interaction alternatives, and complex editing operations, highlighting interactive interface generation as a key open challenge beyond static chart synthesis. To address this, we propose a structured multi stage interface generation framework that decomposes the task into visualization design representation, generation of multiple interface candidates, constraint-aware critique, and self-refinement. This approach improves the best models pass rate by 15.9 percentage points, demonstrating a practical path toward more reliable language-driven interactive visualization systems. We release VIS-GEN at this https URL.

---


### 137. [Same Chart, Different Story: Bias in Vision-Language Chart Interpretation](https://arxiv.org/abs/2609.26210)

**<font color=#1a73e8>作者：</font>** Mizanur Rahman, Huan Wu, Arash Asgari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used to interpret charts and generate natural-language explanations for socially consequential data. However, they may produce different narratives for the same chart when only the referenced social group changes, reinforcing stereotypes and misleading decisions. Despite these risks, no benchmark exists for systematically evaluating bias in chart interpretation across social dimensions. We introduce ChartBias, the first benchmark for auditing bias in VLM-based chart interpretation. ChartBias contains 820 manually curated real-world charts spanning six attributes: race, income, age, religion, immigration status, and gender, yielding 4,319 valid chart, attribute instances and 8,638 paired generations where the chart is fixed and only the group term is swapped. Across 12 proprietary and open-source VLMs, totaling 155,484 model responses, we find three widespread failure modes: narrative shift (same chart, different narratives), group hallucination (assigning a chart to a group without evidence), and preference polarity (favourable trends often linked to one group). We further propose a multi-agent mitigation framework that serves as a strong baseline by separating chart-grounded evidence extraction from group-conditioned generation and using a counterfactual judge to verify that group-driven differences are supported by the chart. The framework substantially reduces narrative shift while preserving chart-grounded reasoning. Our findings show that evaluating chart understanding requires measuring not only accuracy, but also fairness and consistency across social groups. We release ChartBias at this https URL.

---


### 138. [Beyond Imitation: Auditing the Recoverability of Reasoning in Distilled Models](https://arxiv.org/abs/2609.26216)

**<font color=#1a73e8>作者：</font>** Ruitong Li, Binjie Guo, Aisheng Mo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A correct teacher solution becomes useful supervision when the receiving student can continue its reasoning. We measure this compatibility with prefix recovery: after revealing 25%, 50%, or 75% of a verified solution, we test whether the student completes it correctly. We connect recovery to the cosine conflict between cross-entropy and reverse-KL gradients over the full vocabulary. Across adjacent Qwen3 teacher-student pairs from 0.6B to 8B parameters, reverse-KL distillation delivers its most consistent mathematical and code improvements for the two students below 2B parameters. On a fixed cohort of 1,000 trajectories, average prefix recovery rises from 71.0% to 91.9% as student size increases from 0.6B to 4B, and the robust-fragile recovery gap contracts from 46.0 to 14.4 percentage points. With the teacher fixed at 8B, conflict separation falls from 0.993 to 0.233. An independent objective intervention finds the largest reverse-KL rescue on fragile trajectories. The three measurements locate the same capacity-dependent transfer regime: distribution matching has the greatest headroom when correct traces remain unevenly recoverable. Prefix recovery provides a practical diagnostic for selecting costly distribution-level distillation.

---


### 139. [MSA-CITE: A Co-Adapted LoRA Specialist Ecology for Fixed-Budget Small-Model Inference](https://arxiv.org/abs/2609.26217)

**<font color=#1a73e8>作者：</font>** Ruitong Li, Binjie Guo, Aisheng Mo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compact language models are typically deployed by retaining a single post-training checkpoint and sampling it repeatedly. In this work, we challenge this practice by treating multiple discarded checkpoints as composable assets for deployment. Starting from a single Qwen3-4B backbone, we preserve four frozen LoRA branches, each derived from a different post-training trajectory. stead of drawing four generations from one branch, we allocate a fixed four-generation budget by sampling one completion from each branch. Our method, Multi-path Specialist Adaptation with Calibrated Inference-Time Evidence (MSA-CITE), processes the resulting portfolio by grouping terminal answers into equivalence classes, scoring each class via summed calibration-derived source priors, and selecting a representative under deterministic tie-breaking rules. The readout stage does not learn from evaluation results, nor does it introduce additional generations, verifiers, or reranking steps. On 200 held-out mathematics items, the four-path portfolio achieves 65.5% accuracy, compared with 62.0% for the strongest single-branch baseline. On a 100-item subject-disjoint shift, it attains 42.0% versus 40.0%. Under in-distribution conditions, the improvements over homogeneous SFT and Online-OPD repetition are robust; results against the strongest baseline and under shifted conditions are not conclusive. Our findings offer a narrow but concrete contribution: post-training branches, even without co-training, can be collectively beneficial for deployment.

---


### 140. [Towards Effective Black-Box Adversarial Attacks on Deep Code Models via Structural and Identifier Perturbations](https://arxiv.org/abs/2609.26234)

**<font color=#1a73e8>作者：</font>** Bin Duan, Jintao Lin, Dan Dongseong Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep code models (DCMs) are increasingly embedded in code intelligence tasks. However, their robustness under adversarial attacks remains insufficiently understood. Prior black-box attacks mainly rely on identifier- only substitutions or structural edits transferred from reference samples, yielding perturbation spaces defined largely independently of the attacked input. We introduce Strike, an input-conditioned black-box adversarial robustness-testing framework that constructs and searches a hierarchical perturbation space for each input. Strike first partitions code into blocks and uses an LLM to generate context-specific structural candidates, filtered for syntactic validity, ranked by similarity, and adaptively combined. It then refines the best structural variant through similarity-guided identifier substitutions drawn from dynamically constructed candidate pools. Evaluations across representative code intelligence tasks, including clone detection, vulnerability detection, and code summarization, demonstrate that Strike achieves higher attack success rates with competitive target- model query overhead. Strategy-specific static checks across all three tasks and execution-based validation on the executable Juliet vulnerability-detection subset provide complementary, task-bounded evidence regarding the validity of the generated variants. Representation similarity and human evaluation further indicate that the variants remain highly similar to the original code and contextually natural. Fine-tuning with Strike- generated samples improves cross-attack performance on fixed perturbed evaluation sets while preserving clean performance.

---


### 141. [Damage Predicts Recovery: When Calibration Data Matters in Compressing Financial LLMs](https://arxiv.org/abs/2609.26241)

**<font color=#1a73e8>作者：</font>** Junyi Ye, Mengjia Yu, Debapriya Hazra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training quantization and pruning rely on a small calibration corpus. Whether specialized domains such as finance require domain-matched calibration data remains unsettled. We argue that the answer depends on the task-level damage caused by compression rather than on domain mismatch. If compression preserves the target capability, changing the calibration corpus has little effect. If compression causes large losses, task-formatted calibration can recover part of the loss. We test this hypothesis across two model families, six compression configurations, three token-matched calibration corpora, and ten financial classification and numerical question-answering tasks. The results support this hypothesis. Quantization largely preserves task performance, and calibration choice has little effect in this case. Pruning reduces numerical QA accuracy by over 40 points. In these damaged settings, another generic corpus does not help, while FinMix, a mixture of financial task examples, recovers a large part of the loss. The link between damage and recovery holds across model families and scales. These findings support a practical rule. Measure task-specific compression damage first, and construct specialized calibration data only when the damage is large.

---


### 142. [PACE-dLLM: Elastic Block Decoding via Confidence Cliff Estimation for Diffusion Language Models](https://arxiv.org/abs/2609.26249)

**<font color=#1a73e8>作者：</font>** Xiaocheng Lu, Shuhan Guo, Ziyue Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (dLLMs), such as LLaDA and Dream, have become competitive with autoregressive (AR) LLMs in generation quality while supporting native parallel decoding. A standard acceleration strategy is block-wise decoding, where each forward pass predicts a block of length B and commits high-confidence tokens. However, B couples two distinct decisions: the look-ahead horizon and the number of tokens to commit. Existing accelerators address this limitation through indirect heuristics, such as volatility tracking, delimiter detection, and learned scoring. In contrast, we show that the required information is already encoded in the model's own per-step confidence: in-window confidence typically follows a context-dependent cliff, whose saturation point directly identifies the appropriate look-ahead horizon. We propose PACE-dLLM, which fits this parametric cliff in closed form at each step, sets the next horizon by its saturation point, and uses an independent confidence threshold for token commitment. Under a saturated-yield abstraction, we show that the cliff-anchored horizon is the smallest horizon attaining maximal useful per-pass yield: fixed horizons that undershoot it incur a worse asymptotic NFE rate, while overshooting adds no useful yield. On four reasoning and code benchmarks, PACE-dLLM achieves the best average accuracy on both open-source dLLM backbones, with average wall-clock speedups of 5.23x on LLaDA and 3.06x on Dream (up to 8.52x on math) over the unaccelerated semi-AR baseline, advancing the quality-throughput Pareto frontier.

---


### 143. [Coding Agents are Strong Prompt Optimizers](https://arxiv.org/abs/2609.26261)

**<font color=#1a73e8>作者：</font>** Agamdeep Singh, Srishti Gautam, Priyanshu Gupta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Search-based prompt optimizers improve prompts through iterative search: they propose edits, execute fresh rollouts, score the resulting trajectories, and retain only edits that improve a validation metric. We show that this optimization loop is unnecessary. Given only a static corpus of agent trajectories, an off-the-shelf coding agent can directly synthesize an optimized prompt, requiring neither environment access nor validation data. We call this approach \textit{Coding-Agent Skill Distillation} (CASD). The key insight is reflection scope. Rather than reasoning over a small batch of trajectories at each optimization step, the coding agent writes and executes analysis code to compute corpus-wide statistics, identifies systematic failure modes, inspects representative episodes, and distills the resulting insights into behavioral rules. Across four agentic benchmarks (ALFWorld, $\tau^2$-bench retail and telecom, and SpreadsheetBench-Verified), under matched data access, a single CASD pass outperforms GEPA, a state-of-the-art reflective prompt optimizer, on three of four benchmarks and outperforms validation-gated reflective search (SkillOpt) on all four, improving the unoptimized baseline by 16.6 percentage points on average versus 10.9 for GEPA and 5.3 for SkillOpt. Because CASD performs a single offline analysis pass rather than iterative search, producing an optimized prompt costs approximately \$1.60---over $22\times$ cheaper than validation-gated search. Even when competing methods are granted additional validation data and unrestricted environment access, CASD remains ahead on two of four benchmarks. These results suggest that corpus-scale statistical reflection is a viable alternative to iterative search for prompt optimization.

---


### 144. [Decoupling Is Not Identification: Supervised Evidential Learning in Next-Token Prediction](https://arxiv.org/abs/2609.26268)

**<font color=#1a73e8>作者：</font>** Ge Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A next-token probability says what a model predicts, not how much training support lies behind it. A Dirichlet head can represent this distinction by separating mean $m$ from concentration $S$, but decoupling does not identify what $S$ means. Here we propose an Evidential Next-Token Prediction (ENTOP) framework to audit this gap on character-level Moby-Dick, using exact 8-gram count as a reproducible lexical-support label and withholding count regression from 20% of context types. Standard implicit evidential training carries essentially no count signal beyond confidence on held-out-label types (partial Spearman $\rho = 0.001 \pm 0.014$), whereas explicit supervision generalizes ($\rho = 0.201 \pm 0.010$; matched-pair win $= 0.822 \pm 0.021$). CE predictive entropy is at chance for unseen 8-grams (AUROC $= 0.490 \pm 0.004$), while supervised vacuity reaches $0.772 \pm 0.003$, comparable with an indexed CE-representation baseline ($0.769$) but below the tautological corpus oracle ($1.000$). Neither longest-suffix nor representation-distance strata explain where amortization succeeds. Increasing count weight under the digamma objective improves support fit only by sacrificing prediction. A constant predictor wins natural log-RMSE, and vacuity does not improve error deferral. These results motivate a minimum evidence protocol---confidence control, matched pairs, held-out labels, a constant baseline, and a decision test---and show that concentration can pass identification while failing calibration and utility.

---


### 145. [AIGC Video Detection based on the fusion of spatial-frequency-optical flow multimodal features](https://arxiv.org/abs/2609.26274)

**<font color=#1a73e8>作者：</font>** S. Hong, X.Q. Wang, C. Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of generative AI (e.g., Sora, Hunyuan) makes it essential to develop effective detection strategies that can generalize across ever-evolving synthesis techniques. This study is motivated by the observation of a fundamental challenge in generative models: the inherent difficulty of maintaining cross-modal consistency between appearance and motion. To this end, we propose a multi-modal framework for AIGC video forgery detection tasks, named Cross-Attention based Video Forgery Detector (CrossAtt-VFD), based on joint multi-view analysis of this http URL, we introduce a dual-branch architecture that simultaneously extracts spatial-frequency and optical-flow this http URL approach enables the modeling of videos from complementary perceptual this http URL core of this process is a dedicated cross-attention mechanism, which governs the alignment of the two modalities and translates cross-modal inconsistencies into a potent diagnostic signal. This multi-modal strategy facilitates the detection of motion that is statistically inconsistent with the visual appearance of a scene. Comprehensive experimental results demonstrated that our model achieves an accuracy of 94.22%, a precision of 91.67 %,and a recall of 96.25 %, effectively verifying the advantages of the multi-modal fusion strategy.

---


### 146. [On the security and privacy of LLMs in Mobility](https://arxiv.org/abs/2609.26295)

**<font color=#1a73e8>作者：</font>** Mauro Conti, Lorenzo Perinello, Umberto Salviati  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The mobility sector is undergoing a paradigm shift driven by advances in Generative Artificial Intelligence. With a global market valued at approximately 2.9 trillion dollars annually, considering only cars, the integration of these technologies has the potential to impact more than 1.5 billion vehicles worldwide. As Large Language Models (LLMs) are increasingly adopted in mobility, concerns about cybersecurity, privacy, and reliability emerge. Accordingly, this paper surveys current applications and assesses these challenges. Since the European AI Act classifies transportation AI as high risk, we derive nine technical classes from its requirements to assess current research and future deployments. Our findings show that research mainly studies GPT and Llama models (over 50\% of reviewed works) and traffic applications while largely neglecting security, privacy, and reliability. This gap extends to AI Act compliance: among 35 reviewed works, only one includes a partial vulnerability assessment and one a partial risk management system. We identify a clear gap between strong optimization performance and regulatory adherence, suggesting compliance is limited less by technology than by a focus on static performance over lifecycle safety, and underscoring an urgent need for security-by-design in safety-critical intelligent transportation systems.

---


### 147. [CompKV: Compensation-Aware KV Selection for Long-Context LLM Inference](https://arxiv.org/abs/2609.26300)

**<font color=#1a73e8>作者：</font>** Zhen Huang, Ruizhe Yao, Danyi Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite their strong performance, large language models (LLMs) are bottlenecked by KV cache memory traffic during long-context inference. Sparse attention is widely used to accelerate LLM inference by computing exact attention over a selected subset of tokens. To recover the contribution of tokens excluded from exact attention, recent methods apply coarse-grained compensation to the omitted attention tail. However, existing methods typically select tokens based on attention mass and only then compensate for the unselected tokens. This decoupled design overlooks their interaction: selection should prioritize tokens that would leave the largest compensation error if omitted. To address this limitation, we introduce CompKV, the first compensation-aware sparse attention framework that divides tokens into blocks and explicitly optimizes selection for the downstream compensation mechanism. Our theoretical analysis shows that the residual left by block-level mean compensation is governed by both block attention mass and within-block logit variation. We approximate this residual using compact block-level statistics, yielding a deployable selection criterion. We further develop an efficient asynchronous implementation. Experiments on RULER and LongBench-Pro show that CompKV performs best among the evaluated sparse baselines while delivering up to a $6.85\times$ self-attention speedup over full attention.

---


### 148. [Design and Evaluation of a Controlled Post-Alert Incident Orchestration and Response Subsystem Using a Rule Engine and a Local Large Language Model](https://arxiv.org/abs/2609.26316)

**<font color=#1a73e8>作者：</font>** Hoang-Lam Huynh, Quoc-Cuong Tang, Van-Tri Phan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents a controlled post-alert incident orchestration and response subsystem for educational information systems. The architecture separates deterministic classification, contextual analysis, human approval, and technical execution. A Rule Engine determines severity and selects the playbook, while Static RAG and a local large language model provide advisory content under Validator, Guardrail, Output Sanitizer, and Safe Fallback controls. Experiments begin after simulated alerts are stored in Elasticsearch. The Rule Engine matched the predefined routing matrix in all 30 boundary cases. The Durable Queue completed 100 events without duplicate tasks, new failed tasks, or unintended firewall rules. An eight-alert contention experiment preserved the configured limit of one active model request, and 30 sequential measurements showed an overall mean post-alert processing time of approximately 33 seconds. The results demonstrate functional correctness, traceability, controlled recovery, and bounded model integration within the evaluated laboratory scope.

---


### 149. [Disaggregated Quantization: Specializing LLM Prefill and Decode](https://arxiv.org/abs/2609.26333)

**<font color=#1a73e8>作者：</font>** Andrei Panferov, Maximilian Kleinegger, Sweta Priyadarshi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prefill and decode reward different approaches to quantization: low-precision arithmetic accelerates prompt processing, while compact weights reduce memory traffic during generation. We propose "disaggregated quantization" (DQ), which specializes computation formats, weights and storage placement to both of these phases. On Qwen 3 and Gemma 3, removing activation quantization specifically on decode improves accuracy on decode-heavy tasks without increasing inference cost. Training separate compute-native prefill weights accelerates prompt processing relative to weight-only inference while matching or exceeding its accuracy at 2-3-bit decode on both decode-heavy and prefill-heavy tasks. With released Qwen3.8-27B GGUF decoders, training an NVFP4 prefiller improves 1-bit accuracy by 32.5 points on MMLU-Pro and 35.3 on MMMU-Pro without modifying the decode checkpoint. To accommodate the additional checkpoint on a single device, offloaded disaggregated prefill (ODP) streams its weights from SSD, amortizing loading over prompt length. On the same 27B model, ODP delivers a 1.78x time-to-first-token speedup over the weight-only baseline at 8K prompt length in this http URL. We evaluate accuracy under disaggregated serving in vLLM and further validate shared-weight format disaggregation through post-training quantization on models up to 2.8T parameters.

---


### 150. [TransBERT: A Framework for Synthetic Translation in Domain-Specific Language Modeling](https://arxiv.org/abs/2609.26347)

**<font color=#1a73e8>作者：</font>** Julien Knafou, Luc Mottin, Anaïs Mottaz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The scarcity of non-English language data in specialized domains significantly limits the development of effective Natural Language Processing (NLP) tools. We present TransBERT, a novel framework for pre-training language models using exclusively synthetically translated text, and introduce TransCorpus, a scalable translation toolkit. Focusing on the life sciences domain in French, our approach demonstrates that state-of-the-art performance on various downstream tasks can be achieved solely by leveraging synthetically translated data. We release the TransCorpus toolkit, the TransCorpus-bio-fr corpus (36.4GB of French life sciences text), TransBERT-bio-fr, its associated pre-trained language model and reproducible code for both pre-training and fine-tuning. Our results highlight the viability of synthetic translation in a high-resource translation direction for building high-quality NLP resources in low-resource language/domain pairs.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-206](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
