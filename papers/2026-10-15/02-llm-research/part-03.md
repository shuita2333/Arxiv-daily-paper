# 🧠 大模型相关研究 | 2026年10月15日

> 本类共 **810** 篇论文：已确认 **758** 篇，待复核 **52** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 101. [VitaBench: Memory Lifecycles Beyond Retrieval](https://arxiv.org/abs/2610.14731)

**<font color=#1a73e8>作者：</font>** Muquan Yu, Dihan Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term memory benchmarks for language agents primarily evaluate whether information from earlier interactions can be retrieved and used when relevant. Persistent memory systems face an additional problem before future use is known: deciding whether a memory should remain exact, be compressed, consolidated, or deleted. Existing benchmarks capture long-range retrieval, temporal reasoning, evidence reuse, and incremental interaction, but do not directly evaluate these earlier representation decisions. We formalize memory lifecycle evaluation and introduce VitaBench, a benchmark that makes lifecycle decisions measurable through repeated memory reviews and full-horizon counterfactual evaluation. VitaBench contains a controlled Diagnostic tier that isolates future-use patterns and a Naturalistic tier that composes them into generated customer-service-style interaction streams. We characterize lifecycle decision structure with three diagnostics: lifecycle headroom, measuring the advantage of adaptive choices over the best fixed strategy; horizon reversal, measuring when short-horizon decisions change under delayed consequences; and optimal-action diversity, measuring whether different memory states favor different lifecycle operations. Across both tiers, VitaBench exhibits substantial lifecycle structure: lifecycle headroom is 1.364 in Diagnostic and 1.405 in Naturalistic, and 60.2% and 56.5% of states, respectively, change their preferred action between short and full horizons. A learned delayed lifecycle policy further improves over the best fixed strategy on VitaBench-Naturalistic, reaching 101.5 versus 83.4 joint utility. These results show that retrieving past information and deciding how it should persist are distinct evaluation problems, and that lifecycle management requires evaluation of the delayed consequences of representation decisions.

---


### 102. [Think in Strategies, Act with Tools: Traceable Agentic Optimization for Combinatorial Problems](https://arxiv.org/abs/2610.14736)

**<font color=#1a73e8>作者：</font>** Zhongnian Li, Shi Xu, Peng Ying 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Optimization by PROmpting (OPRO) directly leverages Large Language Models (LLMs) to generate candidate solutions through natural-language prompting. However, OPRO's optimization process is difficult to track, which prevents LLMs from capturing useful information accumulated over previous iterations, thereby limiting solution quality. To address this limitation, we propose a Tool-Augmented Strategic Agent (TASA) which summarizes and exploits trajectory to improve solution quality. Specifically, TASA plans the strategy for each step based on the optimization trajectory, which decomposes the optimization process into traceable strategy selections. Moreover, we leverage LLM to construct problem-specific tools and introduce a strategy-guided adaptive tool planner, which efficiently utilizes the information of trajectory to update solutions. We establish local convergence under persistent exploration and evaluate the complete framework under a shared candidate-evaluation budget. The results support its solution quality and the traceability of strategy-guided search.

---


### 103. [PTGPO: Prefix Tree Group Policy Optimization](https://arxiv.org/abs/2610.14737)

**<font color=#1a73e8>作者：</font>** Ruolin Chen, Yang Li, Jihang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training language agents on long-horizon interactive tasks is challenging because sparse terminal rewards provide weak credit signals for intermediate actions. Existing group-based methods either assign a shared trajectory-level advantage or estimate step-level advantages from state groups, which may conflate the current action with subsequent decisions. We propose Prefix Tree Group Policy Optimization (PTGPO), a critic-free method that constructs prefix trees over trajectory suffixes within anchor-state groups. PTGPO assigns each tree edge a credit given by the difference between its child and parent empirical mean returns, capturing the conditional return change revealed by each additional action. These prefix-tree credits provide fine-grained learning signals without requiring a critic or additional rollouts. Experiments on interactive benchmarks ALFWorld, WebShop and Sokoban show that PTGPO consistently improves over RL baselines, demonstrating its effectiveness.

---


### 104. [SAGE: Pushing 2-Bit Vector-Quantized LLMs toward Real-World Usability](https://arxiv.org/abs/2610.14745)

**<font color=#1a73e8>作者：</font>** Xianglong Yan, Zenan Wu, Kewei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Extreme low-bit weight-only quantization is an effective approach to reducing the deployment costs of large language models. Below 3 bits, scalar quantization often suffers severe accuracy loss, while vector quantization (VQ) better preserves accuracy through more expressive joint encoding. However, existing VQ methods still exhibit substantial degradation on real-world tasks, and two design challenges remain underexplored: (1) protecting sensitive weight channels within jointly encoded vectors; and (2) allocating a fixed bit budget among representation components, such as direction and radius, to suit different weight matrices. To address these challenges, we propose SAGE: Split Adaptation and Grouping by Energy for weight-only vector quantization. First, Energy-Stratified Grouping (ESG) couples channel grouping with activation-weighted fitting, grouping channels from different energy tiers within each subvector to prioritize sensitive channels. Second, Adaptive Bit Split (ABS) balances direction-codebook capacity and radius precision per matrix, selecting the split with the lowest activation-weighted reconstruction error under a fixed budget. Across benchmarks covering knowledge, mathematics, code generation, instruction following, and tool use, SAGE achieves state-of-the-art performance in the 2-bit quantization setting. On Qwen3-30B-A3B, it retains 95.3% of the BF16 model's average benchmark score. With our custom-designed CUDA kernel, SAGE delivers up to a 2.55-fold non-streaming end-to-end speedup over FP16. The code is available at this https URL.

---


### 105. [GateSight: Recurrent Memory Anticipates Attention Memory for Query-Agnostic KV Eviction in Hybrid LLMs](https://arxiv.org/abs/2610.14754)

**<font color=#1a73e8>作者：</font>** Junjie Li, Jiong Lou, Jie Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hybrid language models interleave Gated DeltaNet (GDN) layers, whose recurrent memory has a fixed size, with full-attention layers, whose key-value (KV) cache grows with the context and dominates serving memory. In this paper, we ask whether the recurrent memory already knows what the attention memory will need. We first show that which GDN heads of Qwen3.8-27B keep long memories is fixed by the weights rather than by the document. Next, we define the future utility of a KV entry by how much removing it changes the attention output over the model's own continuations, and find that the write gate, decay and write magnitude that GDN layers emit during prefill anticipate this utility before any query is seen. Because the relation is spread across many GDN heads and layers, and a linear map recovers its trend but less of its high-utility tail than a nonlinear one, we propose GateSight, which learns it with lightweight per-head multilayer perceptrons that read these signals and no attention score. Their predicted utility decides which entries each attention layer keeps, and how much each layer keeps is set by the model's native attention output gate, whose mean differs by more than an order of magnitude across layers. Finally, at serving time, GateSight scores the cache once after prefill and physically releases discarded KV entries. Experimental results on SCBench and RULER-4096 with Qwen3.8-27B and, with the same recipe, the sparse-attention model Qwen3.8-Flash-Next, up to the 262K-token limit of the models, show that with a tenth of the attention KV cache, GateSight is the most accurate of five query-agnostic methods on three of the four model-benchmark pairs and leads KVzip on all four, by 9.5 to 47.2 points. Notably, it scores a full-length context with negligible overhead relative to prefill.

---


### 106. [CUSE: Fine-Grained Multimodal Unlearning with Counterfactual Guidance and On-Policy Self-Distillation](https://arxiv.org/abs/2610.14763)

**<font color=#1a73e8>作者：</font>** Chenlu Ding, Jiancan Wu, Yanchen Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) can reproduce sensitive, copyrighted, or unsafe information from their training data. Effective unlearning must remove target information while preserving non-target content, even within the same response. Existing methods typically apply uniform forgetting objectives to complete responses and rely on fixed, off-policy supervision, resulting in coarse token control and misalignment with the model's current behavior. We propose CUSE, a Counterfactual-guided Unlearning framework via on-policy Self-distillation for multimodal large language models. It first constructs counterfactual inputs by removing target-related evidence and uses the resulting changes in token probabilities to identify which tokens require stronger forgetting. It then distills token-level forgetting and retention targets on responses sampled from the current policy, with a frozen copy of the original model serving as the teacher model augmented with the corresponding forgetting- and retention-oriented privileged contexts. This design jointly determines what to forget and what to preserve. On MLLMU-Bench, CUSE reduces forget-set ROUGE-L by 33.6% while achieving 1.2% higher retain-set ROUGE-L than the strongest baseline.

---


### 107. [Last Secure Code Benchmark: Is the Code You Vibe Secure?](https://arxiv.org/abs/2610.14766)

**<font color=#1a73e8>作者：</font>** Tianyi Wu, Chao Ge, Peng Chen 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI coding agents now write much of the code that ships, yet whether that code is secure remains unclear. We introduce the Last Secure Code Benchmark, a comprehensive evaluation of secure code generation by coding agents. Built from 150 real vulnerabilities, its 450 tasks span seven widely used languages (Java, C, C++, JavaScript, Python, PHP, and Go), 24 CWEs including 21 of the 2025 CWE Top 25 and 8 of the Top 10 KEV weaknesses, more than any benchmark we compare with, and three vibe-coding scenarios: filling in a function, writing a file, and building a repository's source tree from scratch. Every task asks only for functionality, through a specification that never mentions security, and hidden functional and security tests grade the result. Across six frontier agents, 73.6% to 91.3% of tasks pass functionally, yet even the strongest, Claude Fable 5, produces code that is both functional and secure for only 25.1% of tasks, and the others for 16.4% to 24.7%. The best model only passes 12% of the vulnerability scenarios across all vibe coding setting, posing strong concern on the security of the code written by vibe coding.

---


### 108. [Who Receives Respect? A Counterfactual Benchmark for Honorific Allocation Bias in Bengali](https://arxiv.org/abs/2610.14769)

**<font color=#1a73e8>作者：</font>** Ajwad Abrar, Md Kamrul Hasan, Hasan Mahmud  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bengali has no grammatical gender, but honorificity is obligatory: every third-person reference must choose ordinary or respectful register. English has no such signal, so the system must choose a level of deference that the source never specified. We use this property to measure how large language models (LLMs) allocate respect in English--Bengali translation. Our evaluation set contains 2{,}016 sentences across 72 occupations. Each appears in seven sentence frames under four pronoun conditions. Masculine and feminine versions differ by one word, forming counterfactual pairs. We report a single Honorific Bias Score (HBS) for each model on a 0--100 scale, covering both the gender and occupation axes. A lower score means that respect is allocated more evenly. For the occupation analysis, we compute each occupation's honorific rate across the seven no-pronoun sentence frames. The standard deviation of these 72 occupation-level rates ranges from 17.2 to 35.5 percentage points across models, showing substantial variation in how honorifics are allocated across occupations. Occupation is associated with 3.2\% to 51.5\% of the variance in register choice, compared with at most 1.2\% for gender. Gender effects are much smaller overall: only two of the nine models show significant directional gender gaps, and they favor opposite genders. HBS ranges from 19.9 to 70.1 across the nine models, showing substantial variation in how evenly the models allocate respect.

---


### 109. [ProgAgent: Learning Tool Orchestration through Programmatic Training](https://arxiv.org/abs/2610.14774)

**<font color=#1a73e8>作者：</font>** Hao Li, Keqing He, Longtao Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly expected to orchestrate diverse tools over long-horizon tasks. Existing agents typically use Direct Tool Calling (DTC), where the model invokes tools sequentially, and tool responses accumulate in the model context, which can lead to context rot and orchestration breakdown. In contrast, Programmatic Tool Calling (PTC) invokes tools through executable code and stores intermediate results in runtime variables rather than appending them to the context. Prior work has explored PTC mainly as an inference-time optimization, but its benefits for agentic training remain unclear, and suitable verifiable training tasks are scarce. In this work, we introduce ProgAgent, a full PTC training stack, comprising a pipeline for synthesizing verifiable long-horizon tasks, a lightweight PTC runtime, and a two-stage training recipe. Using only 215 tasks instantiated at four environment scales, ProgAgent yields higher pass rates than the evaluated baselines of comparable size across four benchmarks. On LOCA-bench, ProgAgent-14B achieves a 30.7% pass rate at a 64k-token environment state, where these baselines score zero. Cross-harness experiments show that PTC-trained models outperform DTC-trained models under both evaluation interfaces, suggesting that the benefits of PTC training extend beyond the interface.

---


### 110. [LYNX: Analytical Program Synthesis via Grounding and Closed-Loop Refinement](https://arxiv.org/abs/2610.14777)

**<font color=#1a73e8>作者：</font>** Ruichen Xia, Xiao Han, Dingyu Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-powered data analytics aims to translate natural language instructions into executable analytical programs over underlying data. However, existing approaches, whether treating LLMs as intent-to-code translators or as standalone analytical engines, often fail to reliably align domain semantics with complex schemas and heterogeneous metadata, resulting in brittle execution and semantically inconsistent analytical outputs in real-world workloads. We present LYNX, a multi-agent framework that formulates LLM-driven analytics as a schema- and knowledge-constrained analysis problem rather than a single-pass generation task. LYNX organizes analytical synthesis into a closed-loop workflow of planning, generation, verification, and refinement through three role-specialized agents that collaboratively enforce schema grounding, semantic consistency, and execution correctness. To address domain ambiguity and schema misalignment, LYNX integrates Semantic-Structural Distillation and Stage-Aware Allocation (SSD-SAA). A delta-guided iterative revision continuously diagnoses and repairs semantic and execution-level failures, substantially improving synthesis robustness. We evaluate LYNX on two NL-to-SQL benchmarks, BIRD-SQL Mini-Dev and the more challenging Spider 2.0-Lite. Experimental results demonstrate strong performance and efficiency, achieving 10.66% to 59.54% execution accuracy across lightweight and commercial models, while reducing token consumption by 70.53% compared with the prior most efficient method. Our framework displays high generalization over different backbones, from open-source, lightweight models to the latest commercial models. Additional case studies on quantitative finance analytics and complex multi-relational SQL workloads further demonstrate the framework's robustness, scalability, and practical applicability in real-world analytical scenarios.

---


### 111. [Training-Free BioNEL-RAG: Advancing Biomedical Entity Linking through Retrieval-Augmented Generation and Large Language Model](https://arxiv.org/abs/2610.14789)

**<font color=#1a73e8>作者：</font>** Ziyi Chen, Hui Liu, Ziyang Ling 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical Named Entity Linking (BioNEL) is the task of mapping mentions extracted from biomedical texts to canonical entities or concepts in the standardized knowledge base. Although existing methods have achieved remarkable performance in mapping accuracy, most rely on training with domain-specific datasets, which fundamentally limits their cross-domain adaptability. To address this limitation, we propose BioNEL-RAG, a novel training-free framework that combines retrieval-augmented generation (RAG) with large language models (LLMs). Within this framework, the RAG module focuses on retrieving candidate entities, while the large language model module plays the role of selecting the most appropriate candidate for entity normalization, which is based on the analysis of the mention's context, with the aid of its remarkable text comprehension capabilities. Experimental results demonstrate that BioNEL-RAG achieves performance comparable to existing methods without requiring training on subdomain datasets, whereas these methods necessitate fine-tuning on specific subdomains such as genes, diseases, or chemical compounds.

---


### 112. [Counterfactual Regret for Reflective Agents with Lean-Verified Guarantees](https://arxiv.org/abs/2610.14790)

**<font color=#1a73e8>作者：</font>** Zhongnian Li, Shi Xu, Mengting Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reflective language agents reuse feedback and memory to adapt across tasks without updating model weights. However, existing guarantees for policy selection and action generation do not by themselves establish when local reflection yields long-term performance guarantees for the complete agent under resource constraints. In this paper, we address this gap by deriving sufficient conditions for sublinear counterfactual regret from local generation and deployment guarantees, while retaining the native controller. Specifically, we establish a resource-sensitive transfer that bounds full-state deployment discrepancies along actual execution paths and preserves the own-history laws of both learner and comparator. Besides, local generation reliability yields a cumulative generation opportunity bound, linking policy acquisition to long-term performance through an explicit quality, coverage, and hard-budget tradeoff. To verify these guarantees, we formalize the conditional proof chain for all thirteen numbered theoretical results in Lean, including a native instance with repeated policy growth and imperfect validation.

---


### 113. [Protecting Shared Agent Workflows from Invalidation Attacks with Signed Trajectories and Runtime Verification](https://arxiv.org/abs/2610.14795)

**<font color=#1a73e8>作者：</font>** Ruixiao Li, Fahao Chen, Peng Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents increasingly rely on shared workflow repositories to transfer experience across tasks and agents. By abstracting past executions into reusable workflow graphs, such systems significantly improve planning efficiency and generalization. However, this emerging paradigm introduces a new and underexplored security risk: if the shared repository is compromised, tampered workflows can systematically mislead downstream agents, inducing persistent execution failures or unsafe behaviors. In this work, we present a principled protection framework for shared agent workflows based on signed trajectories and runtime verification. We require all cloud-collected trajectories used for workflow generation to be cryptographically signed, with each trajectory representing a concrete execution instance. Prior to repository inclusion, trajectories undergo a unified screening process to ensure correctness and validity. When an agent retrieves a workflow from the shared repository, it also obtains a small set of signed supporting trajectories and verifies both their cryptographic integrity and their semantic consistency with the workflow. To make this practical for branching workflows, we further propose a runtime, path-aware retrieval strategy that dynamically fetches only the signed trajectories relevant to the execution path actually taken by the agent, substantially reducing communication and verification overhead. Extensive experiments across multiple reasoning benchmarks show that workflow invalidation attacks achieve up to 90.12% success rates, degrading agent inference performance by up to 73.16 percentage points in accuracy without effective workflow protection. In addition, the proposed protection achieves an average F1 score of 85.26% and a detection rate of 79.97%, outperforming existing baselines by about 2.02x.

---


### 114. [EAIR: Interaction Risks in Enterprise LLM Multi-Agent Systems](https://arxiv.org/abs/2610.14800)

**<font color=#1a73e8>作者：</font>** Yuchen Ma, Swadheen Shukla, Paulo Salem 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly divide enterprise work across roles with different goals, authority, access, and information. Because each agent often sees only a local snapshot of the enterprise workflow, locally reasonable actions can still violate organization-wide constraints (e.g., several service agents can each issue credit that is individually permitted while collectively exceeding a shared compensation cap). We introduce EAIR, the first framework for analyzing enterprise multi-agent interaction risks. We make four contributions. (1) We formalize enterprise interaction risk in terms of the organizational properties that workflow operations must preserve, and operationalize this formulation as a taxonomy of testable risks with explicit failure criteria and evidence requirements. (2) We build EAIR-Worlds, a suite of executable micro-worlds that instantiates selected risks as controlled, observable workflows with explicit roles, policies, permissions, source facts, and execution traces. (3) We develop a novel diagnosis-and-repair pipeline that uses the resulting execution traces to locate contributing interaction boundaries, guide targeted workflow repairs, and retest the repaired system. (4) Large-scale experiments show recurring interaction failures across the organizational properties studied. Together, EAIR is the first operational framework for diagnosing and mitigating enterprise multi-agent interaction failures.

---


### 115. [A Reference Architecture for Integrating Agentic AI into Enterprise Software: Responsibilities, Interactions, and Variability](https://arxiv.org/abs/2610.14818)

**<font color=#1a73e8>作者：</font>** Mingqin Yu, Fethi Rabhi, Liming Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI moves generative AI applications toward systems that coordinate reasoning, enterprise context, model inference, and external actions. Integrating these capabilities into enterprise software introduces diverse architectural concerns, from orchestration, knowledge and memory, and model access to tools and actions, security, runtime infrastructure, and evaluation. Existing research and industry architectures address many of these concerns but differ in scope, abstraction, responsibility organization, interaction representation, and assumptions about which capabilities are required. This paper presents a technology-neutral reference architecture for enterprise agentic AI integration. We synthesize architectural capabilities from research publications, industry architecture guidance, and interoperability specifications by architectural purpose, organize them into ten responsibilities, and define boundary invariants, typed cross-responsibility interactions, and variation points that distinguish responsibilities from condition-dependent capabilities and replaceable realization mechanisms. We instantiate the architecture as an ESG portfolio-analysis and pre-trade compliance agent over an existing service-oriented ESG metric computation and reporting system, and complement the case with a mapping of an independently published agentic architecture. The case realizes seven of the ten responsibilities; different questions take different interaction paths, controls activate only under their conditions, and the probed boundary invariants hold. The independent architecture maps onto the proposed responsibilities without requiring an additional one. These results provide initial evidence for the architecture's organization and applicability rather than its completeness. The deployment and recorded results are available as a replication package.

---


### 116. [Getting Space Right: Agentic Rewards for Image Generation](https://arxiv.org/abs/2610.14852)

**<font color=#1a73e8>作者：</font>** Xiaofeng Tan, Jiaxin Lin, Haobo Yuan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is promising for spatial text-to-image generation, but existing work largely focuses on policy optimization, assuming accurate rewards and effective online rollouts. We observe in-domain gains with out-of-domain degradation, exposing two limitations: unreliable spatial rewards in open-world settings and rollouts lacking basic-to-complex progression. We propose a curriculum-guided RL framework. First, we introduce SpatialCritic, an agentic reward model equipped with a spatial perception harness that combines reusable verification guidance with specialized vision tools. We then construct spatial preference datasets through targeted counterfactual perturbations and perform agent-harness alignment to improve tool selection and evidence integration efficiently. Second, curriculum learning organizes shared foundational capabilities and their compositional dependencies in a capability graph for mastery-guided rollouts, periodic review, and targeted remediation. On SpaRW-Eval, SpatialCritic achieves 95.1% verification accuracy, outperforming 320B GLM-5.3-Flash with a 40x smaller 8B backbone and raising average baseline scores from 78.4 to 83.9 on SD3.5-Medium and 83.2 to 86.5 on BAGEL. Project page: this https URL

---


### 117. [PEAM: On-device Communication Agent for Personalized, Efficient and Autonomous Mobile Network Configuration](https://arxiv.org/abs/2610.14855)

**<font color=#1a73e8>作者：</font>** Haowen Wan, Shangzhuo Xie, Syue-Ju Syue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing deployment of compact large language models on smartphones is enabling autonomous on-device decision-making, such as emerging mobile GUI agents. However, many mobile decisions, such as network configuration when users switch apps or connectivity conditions change, must satisfy stringent latency constraints to preserve user experience. In this paper, we propose PEAM, an on-device LLM-based communication agent that autonomously generates personalized network-configuration rules executable within milliseconds. Specifically, PEAM first fine-tune the on-device LLM with a dataset constructed from manually annotated real-user data to integrate the communication knowledge into the local model. PEAM then operates in two phases. In the rule-generation phase, which is performed when the device is idle, such as overnight, PEAM analyzes historical network-configuration records in batches and reflects across batches to consolidate consistent evidence, reduce local bias, and derive robust configuration rules. To enable more accurate and stable rule generation over time, PEAM further constructs a user profile from high-confidence rules to capture the user's network preferences and incorporates this profile into each rule-generation cycle. In the rule-execution phase, PEAM is invoked when the communication context changes, such as when users switch apps or connectivity conditions change, and searches the rule library to identify and execute the appropriate rule. Experiments demonstrate that PEAM, based on a fine-tuned 4B model, achieves 99.13% correct network configuration decisions, while 92.50% of the rules generated by PEAM are valid, outperforming the traditional expert-rule based method by 4.41% and 84.50%, respectively.

---


### 118. [Terrarium: Growing Personal Assistants via Scalable Synthesis of App Worlds](https://arxiv.org/abs/2610.14860)

**<font color=#1a73e8>作者：</font>** Mengzhou Wu, Yuzhe Guo, Jiawen Tao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advances in large language models (LLMs) have brought the vision of a general-purpose personal assistant closer to reality. Such assistants could provide a unified natural-language interface to a broad ecosystem of applications. However, real-world applications do not readily support training at scale because access is often restricted and their state is difficult to reset. To address this challenge, we introduce Terrarium, a framework that synthesizes executable App Worlds from real-world application information, generates training task packages with evaluator-side rubrics from these worlds, and iteratively validates and refines both through agent rollouts. For App World synthesis, Terrarium organizes public Web information and in-application observations into structured app specifications that guide the construction of self-contained runtimes with callable operations and mutable, resettable state. For task synthesis, Terrarium constructs tasks grounded in App World state together with evaluator-side outcome rubrics that assess success without prescribing reference trajectories. We construct a training suite of 275 App Worlds and 13,344 tasks for outcome-based reinforcement learning across three Qwen3 model scales (4B, 8B, and 14B parameters). Across these scales, models trained with Terrarium outperform the corresponding Qwen3 models by an average of 18.34 percentage points on the $\tau^2$-bench and 10.94 percentage points on the AppWorld bench. These results suggest that app-grounded world and task synthesis offers a scalable path toward general-purpose assistants capable of operating across broad application ecosystems.

---


### 119. [Dependency Reasoning for Aspect Sentiment Quadruple Prediction](https://arxiv.org/abs/2610.14873)

**<font color=#1a73e8>作者：</font>** Shima Esfandyar, Seywan Soleymanbaigi, Fardin Akhlaghian Tab 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aspect Sentiment Quadruple Prediction (ASQP) is fundamentally a relational reasoning problem: identifying aspect-opinion-category-sentiment quadruples requires modeling structured dependencies, not merely sequential co-occurrence. Existing LLM-based approaches incorporate syntactic information indirectly, via retrieval-based demonstration selection or multi-stage training, rather than as unified, single-pass generation-time context. We present DRIFT, which linearizes dependency parse trees and injects them directly into LLM prompts as explicit relational context, enabling the model to reason over aspect-opinion dependencies rather than infer them from token proximity alone. DRIFT further integrates retrieval-augmented in-context learning and a syntax-aware LLM-based adjudication mechanism that complements exact-match evaluation under span-boundary variation. On SemEval Rest15, Rest16, and ACOS, DRIFT achieves the strongest performance among compared generative ASQP methods, reaching 54.47% and 64.10% F1 on Rest15 and Rest16, with consistent gains across short- and medium-distance aspect-opinion configurations; adjudication further shows exact-match metrics systematically underestimate semantically correct predictions.

---


### 120. [Beyond Outcome Feedback: Trajectory-Quality-Guided Experience-based Learning](https://arxiv.org/abs/2610.14877)

**<font color=#1a73e8>作者：</font>** Bingjie Zhang, Yibo Yang, Qiantong Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Experience-based learning enables large language model (LLM) agents to improve over time by reusing knowledge from past executions. However, existing methods typically rely on final task outcomes as feedback for experience learning, overlooking the execution process and limiting their ability to evaluate and optimize experience based on trajectory quality. To address this limitation, we propose TQG-Exp, a trajectory-quality-guided experience-based learning framework that introduces process feedback. Specifically, we introduce Trajectory Quality Loss (TQL), which jointly considers task completion and process quality to provide a learning signal beyond final task outcomes. Based on this signal, we employ paired rollouts with and without retrieved experience to guide experience optimization. Representative trajectories are selected based on their outcomes and trajectory quality to extract task-level and task-type-level experiences. Meanwhile, differences in trajectory quality between the paired groups are used to estimate the contribution of retrieved experience and update its utility. The learned utility is then combined with semantic relevance to guide subsequent experience retrieval. Experiments on ALFWorld, WebShop, and ScienceWorld with two backbone LLMs show that TQG-Exp outperforms existing experience-based methods, improving Avg.@3 over the strongest baseline by 4.50 and 8.55 percentage points on DeepSeek-V4-Flash and Qwen3.5-Flash, respectively.

---


### 121. [Social Bias in Chinese Large Language Models under Social Media Expressions](https://arxiv.org/abs/2610.14879)

**<font color=#1a73e8>作者：</font>** Mo Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing Chinese social-bias benchmarks for large language models largely rely on normalized or template-based expressions, leaving the influence of internet slang, emoji, and sarcasm insufficiently examined. Safety alignment may further compress conventional plausibility ratings toward the lower end of the scale. This study constructs 73 paired probes across gender, region, and occupation. Each probe contains a neutral expression, a social-media-style expression, and a reversed-identity control. The task is reframed from direct plausibility judgment to social consensus estimation. Social-media expressions are divided into stylistic packaging, which preserves semantic polarity, and sarcastic packaging, which reverses surface polarity. Six Chinese-capable large language models are evaluated through paired differences measuring identity bias, stylistic packaging, and sarcasm shift. All models show significant identity-bias effects; five show significantly negative stylistic-packaging effects; and sarcasm shifts display a clear cross-model gradient. These findings demonstrate that expression form is not a transparent carrier in bias evaluation and that lower scores under sarcasm should not be interpreted directly as bias mitigation. The proposed paired design offers a measurement approach for Chinese social-media contexts while also revealing the construct boundary and prompt sensitivity of social consensus estimation.

---


### 122. [MARL-BattleGrounds: A Novel JAX-native Benchmark for Heterogeneous and Competitive Multi-agent RL](https://arxiv.org/abs/2610.14883)

**<font color=#1a73e8>作者：</font>** Ulixes Tariq Hawili, Subramanian Ramamoorthy, Yoann Altmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present MARL-BattleGrounds (MARL-BGs), an easy-to-use JAX-native benchmark for heterogeneous and competitive multi-agent reinforcement learning (MARL), designed to be sample-efficient, computationally efficient, and researcher-centric. MARL benchmarks are typically simple and efficient, like SMAX, where winning reduces to unit micromanagement, or rich and costly, like Dota 2. MARL-BGs fills this missing middle. Its first mode, Team Deathmatch, is a simultaneous turn-based game between two teams of five heterogeneous agents. The five classes have distinct basic, passive, and ultimate abilities designed to synergize with allies and counter enemies. Our 52 hand-designed maps with diverse obstacles include a 12-map curriculum and ten held-out validation and test maps. MARL-BGs provides two canonical evaluation modes. First, eight endgame scenarios form a hard generalization challenge: each asks a team to win an unseen, nearly lost position against a strong reactive controller within 5-10 ticks. Second, a monthly round-robin tournament retrains each submission on equal compute, plays it against every member of the current "Big Nine" field, and publishes the Elo results on the official leaderboard. All entrants are publicly released as downloadable opponents. MARL-BGs records 11,192 metrics per game in 28 topics. We also include three strong scripted opponents, an analytical replay viewer, and off-the-shelf tools for self-play, cross-play, curriculum learning, and zero-shot coordination evaluation. We even provide an API for LLM-based agents and use it to evaluate Qwen3.5-9B against our strongest policy. In our BattleClient, humans can play alongside or against any mix of policies, enabling human-AI evaluation. We benchmark MARL-BGs with six additional deep MARL baselines, which we release. On one RTX 5090 with 1,024 parallel games, the simulator runs 50,000 5v5 game steps per second.

---


### 123. [TeachGrade: Training-Free Short Answer Scoring with Teacher Evidence](https://arxiv.org/abs/2610.14900)

**<font color=#1a73e8>作者：</font>** Jinhao Yan, Zhihong Shen, Shengjie Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-subject, multi-step scoring requires consistent partial credit across grading conventions. We introduce TeachGrade, a training-free framework using teacher-graded examples. The Task Adapt module builds two frozen memories: Skill captures contextual teacher preferences beyond the rubric; CaseBank supplies local evidence. PreJudge provides retrieval cues; FinalJudge regrades the answer without preliminary scores. On 3,829 SAS-Bench answers across 12 tasks, official macro collaborative consistency score (CCS) rises from Native's 67.99 to 81.32 (+13.33 points), and pooled step exact match from 54.85% to 62.71%. Macro quadratic weighted kappa (QWK) reaches 84.71, exceeding Native, OpenJudge, ProofGrader, and Trojsten by 9.52, 3.50, 11.37, and 17.43 points, respectively, and leading on 8 tasks. Local Qwen3.8-27B gains 8.83 CCS and 4.08 QWK points, improving CCS on all 12 tasks. QWK gains over Native span 6.38--14.65 points on Portuguese automatic essay scoring (AES) and 2.16--2.24 on ASAP-SAS across label views, with lower mean absolute error. These results support reuse across languages, response formats, and backbones without weight updates.

---


### 124. [Probable but Not Valid: A Psychometric Audit of Decision Models as Synthetic Survey Respondents](https://arxiv.org/abs/2610.14912)

**<font color=#1a73e8>作者：</font>** Mantas Lukauskas, Viktorija Šarkauskaitė  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly used to create synthetic survey samples, also called silicon samples. Decision models are a new class of language models that return a probability for each point of a rating scale instead of text. We ask whether these models, or the newest generative LLMs, can stand in for human respondents on a psychometric survey. We test fourteen decision models from eleven providers and 47 generative LLMs on an open Lithuanian organisational-psychology survey (n=263, 68 items), with 100 real respondent profiles, the Psychometric Similarity Score (PSS) and statistical baselines. The best generative model, MiniMax M3, reaches PSS 0.813. This is level with a Gaussian copula fit only on other respondents (0.824) and below a copula fit in sample (0.927). A second sample of 100 real people scores below the best models, so at this size PSS cannot rank them against real respondents. In 5 of 10 product lines the newest generative release scores below an earlier release of the same line beyond resampling noise, and none gains beyond it. With the default rounded readout, 13 of 14 decision models score below the generative reference gpt-5.4-mini. Of the 47 generative models, 33 reproduce the pattern of item correlations better than any decision model. Averaged over respondents, the probability vectors are much closer to the human item marginals than rounded answers. They also rank respondents about as well as a profile regression fit on 163 real people. As forecasts of each person's own answers, however, every decision model is worse than the answer frequencies of other respondents, mainly because its average vector differs from them. The profile regression improves on these frequencies by only 1.0%, so the profile fields say little about how a person answers. Synthetic respondents built on such profiles should therefore aim at sample-level fidelity.

---


### 125. [Bridging Risk Approximation Gaps in Model Predictive Task Sampling via In-Context Modeling](https://arxiv.org/abs/2610.14913)

**<font color=#1a73e8>作者：</font>** Jiarong Wen, Qi Tao, Kaiyu Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is essential for adaptive decision-making, e.g., robust Meta-RL and domain randomization (DR), and efficient post-training of large language models (LLMs), where tasks are commonly structured as Markov decision processes or prompts. A central bottleneck in all these settings is the cost of agent-environment interactions required for task selection and policy optimization. Model predictive task sampling (MPTS) has emerged as a promising approach to improve sample efficiency by querying informative tasks via a risk predictive model (RPM) trained on optimization history. However, existing RPMs suffer from two failure modes: (i) sparse optimization histories, which limit RPMs' generalization across the task space, and (ii) a one-step lag in risk approximation, which causes biased difficulty estimation as the policy evolves. This work formalizes these failure modes, derives lagged-risk decompositions that expose the resulting temporal bias, and recasts risk prediction as an in-context sequence modeling problem. The developed RPM integrates a one-step look-ahead mechanism with a temporal-weighted sliding window to mitigate data non-stationarity and scarcity, without requiring additional rollouts. Empirically, our approach yields more reliable difficulty estimates and consistent performance gains across robust Meta-RL, DR, and prompt curriculum RL post-training of LLMs.

---


### 126. [WorkBorne: Discovering Agentic Tasks from Real-World Artifact Transitions](https://arxiv.org/abs/2610.14915)

**<font color=#1a73e8>作者：</font>** Junyi Zhou, Yufei Wang, Qiyuan Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Developing terminal-based agents for long-horizon execution demands synthetic tasks that tightly couple complex instructions with authentic, interactive environments. However, current automated synthesis suffers from a fundamental asymmetry: instruction-oriented methods fabricate low-fidelity, synthetic environments, whereas resource-oriented methods treat real artifacts merely as static inputs, degrading task instructions into shallow, trivial operations. To address this limitation, we introduce WorkBorne, a synthesis framework that uses artifact transitions as the central primitive for modeling the full life-cycle of agentic tasks. In WorkBorne, each transition specifies who performs the task, which artifacts anchor the initial state and intended outcome, and the corresponding relationship between them. Specifically, WorkBorne first constructs coherent and diverse artifact corpora from iterative web retrieval, then discovers non-trivial transitions by identifying meaningful input-output artifact assemblies and the relations that connect them. Each discovered transition is finally instantiated into grounded agentic tasks. We construct 1,061 artifact corpora and 7,882 task environments, yielding 15,485 high-quality trajectories, with 53.6% exceeding 30 assistant turns. Experiments on Qwen3.5-27B and Qwen3.5-35B-A3B show that WorkBorne substantially improves over base models (i.e., improving Terminal-Bench 2.1 from 43.1% to 61.8% and ClawEval General score from 75.0 to 80.2) and achieves the strongest overall performance among other synthesis baselines (e.g., TMax (Ivison et al., 2026), RST (Li et al., 2026a), Terminal-Universe (Wu et al., 2026a)). Further analysis shows that transition is strongly associated with execution depth, while corpus breadth and transition depth provide complementary scaling gains.

---


### 127. [SkillForgeBench: Evaluating Agent Reliability Grounded in Agent Skill Specifications](https://arxiv.org/abs/2610.14918)

**<font color=#1a73e8>作者：</font>** Zhengxi Li, Junyi Zhou, Qiyuan Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating an agent's ability to strictly satisfy diverse and procedurally complex requirements is essential to determining its practical reliability. Conducting such an evaluation demands agentic tasks that reconcile broad domain coverage with deep procedural complexity. Existing paradigms face a fundamental trade-off: expert-curated benchmarks achieve procedural depth but suffer from domain diversity bottlenecks, whereas crowdsourced benchmarks span diverse scenarios but lack execution rigor. To resolve this tension, we present SkillForgeBench, which leverages agent skills as unifying execution blueprints across three co-designed stages: (1) Resource Preparation uses domain-balanced skills to guide artifact retrieval, establishing broad workflow coverage; (2) Skill-driven Task Synthesis employs skills as procedural anchors to partition artifact roles, synthesize naturalistic task instructions, and package sandboxed scenarios for deep procedural execution; and (3) Holistic Evaluation Design translates skill-embedded requirements into fine-grained completion and process rubrics to enable strict requirement-level scoring. Comprising 842 sandboxed tasks across five major professional domains, SkillForgeBench reveals a steep capability hierarchy among eight mainstream agents, led by Opus 4.8 ($40.9\%$ strict completion). Requiring all constrains satisfaction uncovers severe capability bottlenecks across all model tiers that remain masked under individual rubric pass rates ($70.0\%$ to $85.7\%$ vs. $12.6\%$ to $40.9\%$). Crucially, under the external guidance from skills, top-tier agents obtain larger gains than low-tier agents (i.e., $\Delta 19.2\%$ for Opus 4.8 vs. $\Delta 5.8\%$ for Haiku 4.5). Finally, agents satisfy process rubrics far less frequently than completion rubrics (under $3\%$ for Haiku 4.5), proving that completion-only checks overestimate real-world agent reliability.

---


### 128. [Representation Drift in Continual Learning: LoRA versus N-gram Memory](https://arxiv.org/abs/2610.14921)

**<font color=#1a73e8>作者：</font>** Hao Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A language model that keeps learning online must not slowly erode its own base capabilities. We ask which part of a modern LLM should absorb continual updates, by measuring how each choice changes the model's internal representations. On a 48-layer mixture-of-experts model with a native pretrained N-gram memory, we train a seven-task chain under three update mechanisms with identical data and budgets: updating only the N-gram memory table, continually training one shared LoRA adapter, and training a fresh LoRA per task that is merged into the backbone. We capture fixed-context representations at every layer and task boundary. Updating only the N-gram memory changes the base model's representations of general math and code inputs by 26%/15% (relative RMS), against 64%/35% for merged and 97%/39% for shared LoRA. This drift does not grow with the number of tasks: it reaches 25% after the first task and stays there for all seven, while both LoRA variants keep accumulating. Its generic behaviour is essentially unchanged (no code problem lost, math NLL -0.01), and every change is confined to inspectable, reversible table rows. The cost appears elsewhere: N-gram memory acquires new tasks more weakly and its stored tasks interfere with one another, losing as much old-task NLL as shared LoRA. We show that this forgetting is governed by drift on the learned tasks' own inputs, measured from the checkpoint at which each was learned, not by generic drift (Spearman rho=0.85; rho=0.71 on Llama-3-8B), and we derive the exact relations behind it: with a frozen head, every pairwise logit margin changes by the projection of drift onto a head-difference direction. These results support a design principle for long-running online learning: write new knowledge only into the memory table and keep the backbone fixed; the remaining problem, interference between stored tasks, then lies inside the memory.

---


### 129. [TLA-Verus: Generating and Solving Temporal Proof Obligations with LLM Agents](https://arxiv.org/abs/2610.14923)

**<font color=#1a73e8>作者：</font>** Kseniia Strelbytska, Balázs Szilágyi, Anna Mészáros 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The TLA+ (temporal logic of actions) formal specification toolkit has seen widespread adoption in modeling modern distributed software systems including databases, storage systems, ledgers and coordination protocols. This popularity is despite its two significant limitations for software verification: Firstly, TLA+ offers no way to detect drift between software implementation and mathematical specification; secondly, TLC and TLAPS cannot provide satisfactory proofs of arbitrary temporal logic properties. We take a step towards addressing these shortcomings by translating TLA+ specifications into Verus, an auto-active verifier built for Rust, via both a deterministic transpiler and an agentic translator. We demonstrate that our LLM-based pipeline is able to generate proof obligations from TLA+ specifications at scale, and to produce fully machine checkable proofs of both safety and liveness properties. Since temporal logic reasoning in Verus is a largely new task for LLMs, our work yields a valuable evaluation dataset, which we use to map out current generation model capabilities in Verus theorem proving.

---


### 130. [FidelityQ: Preserving Predictive Fidelity in Ultra-Low-Bit Language Model Quantization](https://arxiv.org/abs/2610.14934)

**<font color=#1a73e8>作者：</font>** Yujie Chen, Weiyan Zheng, Yiwu Yao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ultra-low-bit scalar quantization offers a regular arithmetic structure for efficient deployment of large language models, but preserving predictive behavior at extreme precision remains challenging: with only a few reconstruction levels, accurate weight representation must translate into consistent predictions from a small calibration set. We propose FidelityQ, a scalar quantization framework that preserves predictive fidelity at weight precisions down to 2 bits. For accurate quantization, we introduce Information-Aligned Analytic Coding (IAC), which shapes each weight row toward a centered symmetric source via randomized Hadamard mixing and fits a mirrored four-level minimum-distortion quantizer to its empirical weights. Every level set in this family decomposes exactly into two sign-valued bases with associated scales, combining source-adaptive reconstruction with lookup-free decoding compatible with scaled integer arithmetic. Our analysis further shows that residual predictive discrepancies are heavy-tailed and concentrate on tokens the teacher predicts confidently, motivating Knowledge-Intensive Calibration (KIC) for consistent quantization. KIC ranks sequences by the tail of token-wise teacher-student divergence, allocates a limited calibration budget to the highest-scoring samples, and restores predictive agreement by updating only quantization levels and scales under teacher supervision, keeping pretrained weights frozen. Experiments on the LLaMA and Qwen families demonstrate the effectiveness of FidelityQ in weight-only and joint quantization settings. On LLaMA-2-7B, FidelityQ achieves a WikiText2 perplexity of 6.62 at W2A16 and improves the prior state-of-the-art W2A4KV4 result from 8.31 to 6.96, while reducing linear-layer weight memory by 8.0x relative to FP16.

---


### 131. [BSIPipe: Bidirectional Sequence-Level Interleaved Pipeline Parallelism for Long-Sequence Large Language Model Training](https://arxiv.org/abs/2610.14935)

**<font color=#1a73e8>作者：</font>** Yuzhou Ni, Ling Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pipeline parallelism has become a critical technique for training large language models. To address the throughput limitation of existing sequence-level methods that schedule subsequences unidirectionally, we propose bidirectional sequence-level interleaved pipeline parallelism (BSIPipe), which co-schedules two opposing V-shaped interleaved pipelines at the subsequence level. To bound the activation accumulation from subsequence scaling, BSIPipe introduces a basic-unit concatenation mechanism that keeps activation memory invariant to the subsequence count. To eliminate communication deadlock risk from bidirectional scheduling, BSIPipe employs a communication optimization strategy that combines topology-aware device mapping with communication-computation overlap. In addition, BSIPipe composes with tensor parallelism to overcome the memory limitation of single-dimensional parallelism, neutralizing its bidirectional memory overhead while maintaining throughput. Experiments on GPT and LLaMA3 demonstrate that BSIPipe achieves average speedups of 1.11$\times$ to 1.13$\times$ in long-sequence training over SOTA sequence-level baselines.

---


### 132. [Predicting how model propensities generalize out of distribution](https://arxiv.org/abs/2610.14937)

**<font color=#1a73e8>作者：</font>** June Hunter, Lily Wen, Owen Terry 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How do language models generalize from their training data? This is a central challenge for alignment: models reliably learn their training distribution given enough samples, but we want models that behave well when deployed in new contexts. We study out-of-distribution (OOD) generalization of propensities. Our central experiment uses a range of elicitation techniques -- system prompting, few-shot learning, SFT on reference answers, and GRPO -- to increase a target propensity in a model, then measures how it spills over onto others across the resulting cross-elicitation matrices. We find that spillover is highly correlated between models when the same elicitation technique is used, but our SFT and GRPO runs induce different spillover profiles.
Elicitation of benign traits can sometimes generalize towards undesired traits, for example a model trained to claim that it is sentient often becomes more power-seeking. We further find that spillover partially resembles trait correlations found in humans and identify three clusters of traits that account for about half of the variance using exploratory factor analysis (EFA). Across many elicitation runs, we observe that models change in characteristic ways that don't depend on the targeted trait, a phenomenon we refer to as drift. Drift moves Qwen3.5-9B towards its base model.
When investigating if LLMs are able to predict spillover, we find that Claude Opus 5.5 predicts spillover slightly better than the models themselves, but worse than data-driven approaches using alternative elicitation methods or models. Overall, no single dominant predictor emerges, and generalization remains hard to predict. Code and data are available at this https URL.

---


### 133. [VC-OPD: Visual Counterfactual On-Policy Distillation for Grounded Vision-Language Reasoning](https://arxiv.org/abs/2610.14939)

**<font color=#1a73e8>作者：</font>** Jiahe Feng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GRPO-style reinforcement learning has advanced vision-language reasoning, but its sequence-level rewards provide limited credit assignment for individual reasoning tokens. On-policy distillation (OPD) addresses this issue by providing dense supervision on student-generated trajectories, yet standard OPD assigns similar importance to all teacher-preferred tokens, including template phrases and visually irrelevant continuations. We introduce Visual Counterfactual On-Policy Distillation (VC-OPD), a grounding-aware distillation method that prioritizes tokens whose correctness depends on image-specific evidence. After a teacher-supervised warm start that stabilizes response formats and reduces noisy rollouts, VC-OPD performs on-policy distillation with two teacher evaluations for each student trajectory: one under the original image and one under a counterfactual image with corrupted instance-specific evidence. The original-image teacher distribution determines the distillation target, while the original--counterfactual teacher gap estimates token-level visual dependence and softly reweights the loss. To avoid unstable response-level update scales, VC-OPD further applies mass-preserving normalization to the token weights. This design preserves the dense supervision of OPD while shifting learning capacity toward visually grounded reasoning tokens. Experiments on multimodal reasoning benchmarks show that VC-OPD improves visual reasoning performance and produces more effective token-level distillation.

---


### 134. [Do Personalized LLMs Need the Whole Conversation? Matching the Full History with Only 5% of Its Text via Relevance-Filtered Context](https://arxiv.org/abs/2610.14952)

**<font color=#1a73e8>作者：</font>** Erika Hayashi, Andrew Shin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalized assistants accumulate long conversation histories, and passing the whole history to an LLM with every request is costly. We show that it is also unnecessary. On PersonaMem-v2 (180 questions), with GPT-5.6-terra and Claude Opus 5.5 as judges, a relevance-filtered context, built by sentence-level retrieval that ranks the history by similarity to the current request and stops at a fixed budget, matches full-history accuracy with only 5% of the text, cutting the judge's input about 20-fold. An LLM summary of the same length performs on par, but it needs an LLM to read the entire history, whereas retrieval needs only a small embedding model. While both sentence-level retrieval and LLM summary perform strongly, retrieval does so while placing the relevant evidence in the context for only 61% of the questions, and an oracle given only that evidence beats the full history by 15.6 points, making better context selection a promising path to surpassing the full history.

---


### 135. [What Survives When Activation Steering Is Used as Memory](https://arxiv.org/abs/2610.14958)

**<font color=#1a73e8>作者：</font>** Vedant Jumle  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Activation steering has recently been used as a memory for skills: past experiences of an agent are stored as steering vectors and retrieved later. Facts and preferences about the user are assumed to need text instead. We test that assumption with a training-free activation memory beside a frozen LLM. The change an experience causes in late-layer states is stored as a shift, filed under a whitened key for the conversation's gist, and added back in a later session only when the gist matches. We argue that such a shift is a fixed average of an effect that attention, in context, recomputes for every question, so only question-independent content can survive. In a pre-registered study on Qwen3.5-2B and 9B, with judges from four model families, the memory is selective (about 98% of unrelated replies are unchanged), but facts are stored as the word to say, in the last layers only, and are almost never used (at most 15% clean use, against 96-98% in context). Leanings transfer only in a narrow strength window. Most strikingly, the reference subtracted when writing a preference decides whether its concept or its direction survives: unless the opposite is subtracted, a stored dislike is recalled as a like.

---


### 136. [AlphaRLM: Aligning Language Models for Literature-Grounded Symbolic Factor Discovery](https://arxiv.org/abs/2610.14959)

**<font color=#1a73e8>作者：</font>** Jie Huang, Yuecheng Hong, Yao Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Formulaic alpha mining seeks to discover executable expressions that capture predictive market signals in a vast, noisy search space. Recent LLM-based approaches use prompting, iterative search, or seed-factor evolution, leaving direct factor construction through policy learning less explored. To address this, we introduce AlphaRLM, a reinforcement-learning framework that trains LLMs to construct executable symbolic factors from financial literature without input factor expressions. AlphaRLM incorporates Literature-Guided Operator Assembly (LEGO), which conditions factor construction on literature-derived ideas and executable operators, providing semantic priors for exploration. It further aligns the generation policy with market feedback through executable-validity and grouped-return-separation rewards that capture non-monotonic structures across factor quantiles. Extensive experiments on CSI 300, CSI 1000, and S&P 500 show that AlphaRLM outperforms strong factor-mining and LLM-based baselines in annualized excess return. Notably, the 8B model achieves strong cross-market performance, highlighting the promise of literature-conditioned, market-aligned factor generation.

---


### 137. [HiPAD: A Unified Gait, Audio-Visual, and Personality Fusion Network for Depression Detection, with a Hierarchical Personality Ablation and the Calibration Limits of Domain-Adapted LLMs](https://arxiv.org/abs/2610.14961)

**<font color=#1a73e8>作者：</font>** Karol Chlasta, Piotr Struzik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present HiPAD, a single fusion network submitted to all six sub-tracks of the MPDD-AVG 2026 depression-detection challenge, covering the Elder and Young cohorts and three modality sets (gait, audio-visual, and both), each combined with personality descriptions. The network encodes each available modality with a shared BiLSTM, zero-pads absent modalities, and applies cross-modal attention only when at least two of gait, audio and video are present. Personality, which dominates our results, is kept out of the attention and fused by concatenation. Because the architecture is identical in every sub-track, differences between them reflect the data rather than the model, and we use this to study three questions. Our main finding is that the personality description, roughly 150 tokens about who the subject is, carries more depression signal than audio, video, and gait combined: gait plus personality alone (TLS 0.647) beats every configuration that includes audio and video. First, a four-level ablation of the personality description (L0-L3) quantifies this: removing every personality-derived feature, including the Big Five scores that earlier MPDD ablations keep, lowers the Track-Level Score by 0.499 to 0.507 and leaves the model at chance. Second, domain-adapting the personality encoder with LoRA (7B) or QLoRA (72B) on PHQ-8/9 data raises binary Cohen's $\kappa$ by 0.13 but lowers the overall score by distorting the PHQ-9 regression; a frozen RoBERTa-large encoder does better at this sample size. Third, at fixed architecture, handcrafted clinical features (eGeMAPS, OpenFace action units) outperform generic deep features (wav2vec2, DenseNet) on the audio-visual tracks. The unified system reaches a cross-track G-Score of 0.482; with under 100 subjects per cohort, the limiting factors are the size of the representation and the calibration of the outputs, not the choice of architecture.

---


### 138. [SkillHorizon: Constructing Long-Horizon Agent Tasks through Skill Composition](https://arxiv.org/abs/2610.14966)

**<font color=#1a73e8>作者：</font>** Yuxuan Liu, Zhaochen Su, Hangyu Guo 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents must complete workflows in which later activities depend on earlier outputs and changes to shared state. A key challenge for evaluation is to expand task requirements and their dependencies while keeping tasks executable and outcomes verifiable. We introduce SkillHorizon, a benchmark that constructs long-horizon tasks through skill composition in seven business environments. Its generators use domain-specific rules to turn reusable skill procedures into concrete business activities. These activities are connected through input-output dependencies, shared resources, and state updates, allowing workload and coordination demands to grow together. Successful reference executions validate task feasibility and measure interaction workload, while programmatic evaluators assess local completion and whole-task success. We evaluate five language models on 1,050 tasks with reference interaction workloads ranging from 64K to 1M tokens. Across these scales, mean local-goal completion falls from 90.4% to 46.8%, as completed work fails to keep pace with growing requirements. At larger workloads, agents more often submit unsuccessful final answers with substantial work unfinished and tool-call allowance remaining. Trace analysis also identifies cases where scripts execute successfully but their outputs fail downstream business checks. SkillHorizon provides a configurable testbed for studying sustained progress, dependency coordination, and complete task delivery in growing workflows. Our code is available at this https URL.

---


### 139. [SEEK: Agentic Knowledge Graph Retrieval for Secure Code Generation](https://arxiv.org/abs/2610.14968)

**<font color=#1a73e8>作者：</font>** Varun Gadey, Markus Tohn, Lichao Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can generate functionally correct code while introducing exploitable security weaknesses, particularly when developers specify functionality without explicit security requirements. Recent state-of-the-art approaches mitigate this problem using external security knowledge, but largely rely on flat similarity-based retrieval over independent artifacts, making it difficult to infer the relevant vulnerability space and retrieve targeted knowledge when direct matches are unavailable. We propose SEEK, an agentic Graph RAG framework for secure code generation that constructs a security knowledge graph using the Common Weakness Enumeration (CWE) taxonomy as its structural backbone and injects it with curated real-world CVE vulnerability-fix instances. At inference time, a Planner Agent predicts potential CWE weaknesses associated with the developer query, which guide Graph Scoping to restrict retrieval to relevant regions of the CWE taxonomy before deterministic multi-faceted candidate ranking. A Selection Agent subsequently validates the predicted weaknesses and retrieved candidates prior to code generation. Across five open-source LLMs, we evaluate SEEK in an out-of-distribution setting on CodeGuard+ and CyberSecEval, spanning C, C++, and Python. SEEK achieves the highest SecurePass@1 of 77.45% on CodeGuard+ and the highest aggregate ICD pass rate of 79.45% on CyberSecEval, surpassing prior approaches. Moreover, SEEK achieves 85.2% SecurePass@1 across 13 unseen CWE types with no directly linked vulnerability-fix instances, demonstrating strong generalizability, while maintaining acceptable inference latency costs.

---


### 140. [FleetPilot: Fine-Grained Steering Empowers Real-World LLM Personalization](https://arxiv.org/abs/2610.14970)

**<font color=#1a73e8>作者：</font>** Kounianhua Du, Jianxing Liu, Kangning Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the rapid evolution of large language models (LLMs), there is an increasing demand for effective personalization techniques that can adapt model behavior to individual user preferences. Personalized LLMs must infer a user's query-dependent preferences from limited, heterogeneous, and evolving interaction histories. Existing approaches rely primarily on in-context personalization, parametric adaptation, or personalized reward modeling, but respectively incur recurring costs in context management, model optimization and deployment, or multi-candidate generation and scoring. These limitations become particularly restrictive when user observations are sparse and the preference evidence relevant to each query varies across contexts and over time. To address these challenges, we propose \modelname, a fine-grained and instance-tailored steering framework that dynamically generates sample-level interference vectors from user data and injects them into the model's forward pass for personalized adaptation. Our approach introduces: match contrast that produces user-relevant signals, fine-grained steering component that captures nuanced signals by hooking activations from attention and MLP layers, and query-conditioned aggregation module that synthesizes these signals into contextually relevant enhancements. Extensive experiments across diverse scenarios, including short-to-long text generation, and web function calling, validate the effectiveness and compatibility of \modelname. Results show that our method consistently brings significant performance gains, and show extreme superiority in fast-shifting and data-sparse environments. Additionally, \modelname rids us of training cycles and incurs light overhead of storage or inference latency. These make \modelname a strong and real-world deployable method. Implementation is available \footnote{this https URL}.

---


### 141. [Metric-Driven Reinforcement Learning for Object Hallucination Reduction in LVLM-Based Image Captioning](https://arxiv.org/abs/2610.14976)

**<font color=#1a73e8>作者：</font>** Thanh Nguyen, Hee Suk Yoon, Tung Minh Luu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have excelled in joint visual and language understanding, particularly in image captioning. However, LVLMs remain prone to object hallucination, describing non-existent entities in the given image. Previous remedies, including dataset-enhanced supervised training and reinforcement learning from human feedback, show promise but rely heavily on costly human involvement, limiting scalability. To address this, we propose a reinforcement learning framework to mitigate object hallucination in LVLM-based image captioning, driven entirely by natural language processing (NLP) metrics. While optimizing reinforcement learning solely on NLP metrics offers scalability, it also introduces pitfalls: reward hacking, sparse feedback, and costly training. Our framework sidesteps these by introducing an Object Consistency Score (OCS) capturing both correctness and coverage of objects, incorporating KL-regularization for denser token-level guidance, and designing a lightweight PPO variant that fine-tunes adapters atop a frozen LVLM backbone, achieving efficiency and stability. Extensive experiments on the InstructBLIP baseline demonstrate the effectiveness and generalizability of our framework, achieving a substantial hallucination reduction of up to 41\% on the COCO dataset and 29\% on the Visual Genome. Furthermore, the framework can enhance caption quality by incorporating complementary evaluation metrics such as BERTScore and METEOR. These results reveal a broader insight in multimodal learning: LVLMs can effectively self-correct hallucinations using metric feedback, motivating deeper exploration into scalable reinforcement frameworks that significantly reduce human effort.

---


### 142. [Single-Sample Decoding of a Two-Layer Sound-Word Canvas Model for Thai Klon Pad](https://arxiv.org/abs/2610.14980)

**<font color=#1a73e8>作者：</font>** Worasait Suwannik  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a generator of Thai klon pad verse, one stanza from a short topic, and evaluate it against human verse on held-out topics. The generator is a masked language model initialised from WangchanBERTa over a fixed canvas with two layers: a sound layer of pronounced syllables, where rhyme, tone and syllable count are enforced as hard masks, and a word layer of whole words, so that no word is cut into written pieces. Decoding commits one cell at a time and samples at temperature 0.4; one sample is drawn per topic, with no selection, reranking or repair. On 78 held-out topics never used in development, judged by three independent runs of a frozen LLM judge in the same pools as the human stanzas from which the topics were written, 70.5% of the generated stanzas pass form, lexical cleanness of all four lines and topic alignment together, against 76.9% for the human stanzas (difference -6.4 points, 95% CI [-19.2, +6.4]). Cleanness is level with human (85.9% vs. 87.2%), and the stanzas pass form and cleanness together slightly more often than the human ones (+3.8 points, [-6.4, +14.1]); the difference lies in alignment (84.6% vs. 91.0%), on topics that were written from the human stanzas. The low temperature matters: at higher temperatures the same model passes clearly fewer of the same topics, because lexical errors lie in the model's lower-probability choices; sharpening the sampling distribution removes most of them, at a cost in vocabulary (7.5% rare words against 16.5% in the human stanzas) and diversity. The pre-registered target, all-three within 5 points of human, is missed by 1.4 points. KlonSuphap-LM, the only public klon pad generator we know of, passes none of the 78 held-out topics when judged in separate pools together with the method's and the human stanzas (form 19.2%, cleanness 3.8%).

---


### 143. [Recurrent In-Context Learning for Tabular Foundation Models](https://arxiv.org/abs/2610.14998)

**<font color=#1a73e8>作者：</font>** Tejas Vaidhya, Gaurav Sahu, Irina Rish  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models adapt to new datasets through in-context learning (ICL), and, like most transformers, they tie computational depth to the number of independently parameterized layers. We ask whether the ICL stage of such a model needs a distinct set of parameters for every layer, or only depth. We introduce Tab-Loop, which replaces the 12 untied ICL blocks of TabICLv2 with 4 tied blocks applied $k$ times and changes nothing else: the encoders, decoder, synthetic prior and training recipe are shared with an untied baseline trained for the same compute. At matched pretraining compute (18.2 EFLOP) and matched inference compute (12 block applications), Tab-Loop matches the baseline with 62\% fewer parameters (10.4M vs.\ 27.6M): held-out log loss is 0.4583 vs.\ 0.4588, mean accuracy on 200 TALENT datasets is 84.10\% vs.\ 83.92\%, and Elo on 38 TabArena datasets is 1409 vs.\ 1396. A 4-block untied control with Tab-Loop's parameter count, which sees 32\% more training tables for the same compute, trails both (83.46\%; Elo 1343). Because weights are shared, depth becomes a choice made at inference. Accuracy rises with the number of loops through the trained range and holds beyond it, and continued training with deeper loops extends the useful range, reaching the baseline's stage-2 scores at 4--5$\times$ its inference compute. At this scale, the ICL stage of a tabular foundation model needs depth more than it needs distinct parameters.

---


### 144. [Retraining-Free Depth Pruning of Vision Transformers: A Cross Domain Study of Layer Redundancy](https://arxiv.org/abs/2610.15005)

**<font color=#1a73e8>作者：</font>** Alessandro Viespoli, Loris Nanni  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformer architectures have achieved strong results in natural language processing and computer vision, but their deployment is limited by high computational, memory and storage costs, motivating research into model compression techniques, such as pruning, while preserving performance. Prior work has shown substantial redundancy in large language models (LLMs), and redundancy in vision transformers has also been investigated, but it remains less systematically analyzed than in LLMs. In this work, we extend similarity-based redundancy analysis to vision models by measuring cosine similarity between layer inputs and outputs to identify transformations with minimal impact. We study redundancy patterns across several transformer architectures and find that deep vision transformers such as DINOv2 and SwinV2, like language models, exhibit significant redundancy. We then evaluate how this redundancy can be exploited to improve efficiency, analyzing the trade-off between inference speed and performance degradation under different pruning strategies. Our results show that moderate pruning can yield substantial acceleration with limited impact on accuracy, and that 20% of the DINOv2 blocks can be removed without any retraining, for a 1.24x throughput gain and a 20% lower energy per image at a relative accuracy loss below 1% on ImageNet-1K. We further propose a model selection pipeline that automatically identifies the best pruned configuration for a given dataset, reducing FLOPs by 13% to 27% on average across architectures with an average accuracy change between -0.3 and +1.0 points.

---


### 145. [Can You Trust Your Preference Models? Stackelberg Games for Alignment](https://arxiv.org/abs/2610.15008)

**<font color=#1a73e8>作者：</font>** Riccardo Formenti, Aditya Agrawal, Vikas Garg  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models are frequently aligned to human preferences via imperfect evaluators whose errors can be exploited during optimization. We train policies to search for comparisons on which an evaluator may reverse the underlying preference, providing candidates for additional supervision. Since human preferences are unavailable during policy training, we use disagreement among an ensemble of preference models as a proxy for prediction error. We formulate this search as a zero-sum Stackelberg game between two opposing policies, a Leader which tries to minimize disagreement, and a Follower which maximizes it. For a general class of finite contextual Stackelberg games, we establish equilibrium existence and, under regularization, uniqueness and a closed-form characterization. We introduce Stackelberg Mirror Descent-Ascent (SMIDA), a two-timescale algorithm with linear last-iterate convergence in the tabular setting, and develop a neural policy-gradient analogue. Experiments with a synthetic oracle support disagreement as an informative proxy for prediction error. On held out data the trained policies outperform reference policies and increase the fraction of comparisons that exceed a disagreement threshold and reverse the oracle's preference.

---


### 146. [UltraBERT: Beyond the Limit of BERT Pre-Training](https://arxiv.org/abs/2610.15028)

**<font color=#1a73e8>作者：</font>** Jungwoo Park, Taewhoo Lee, Jaewoo Kang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent bidirectional encoders have been modernized with innovations from causal large language models (LLMs). However, the pretraining recipe itself remains inherited from small-scale conventions, leaving encoders underoptimized, with no single model performing competitively across both classification and retrieval tasks. In this work, we investigate how far encoder performance can be pushed by revisiting core design choices in training, revealing three key findings: (1) Encoders saturate on downstream tasks beyond a few trillion tokens, indicating that additional compute past this point does not help. (2) Across model sizes, lower masking ratios benefit classification while higher ones benefit retrieval, contradicting prior work suggesting larger ratios for larger models. (3) Distillation with pruning improves classification at low masking ratios but degrades retrieval at high ones. Guided by these findings, we present UltraBERT, a single encoder that assigns separate LM heads to low and high masking ratios within a batch and restricts the distillation objective to the low ratio. To our knowledge, UltraBERT is the first encoder to achieve state of the art on both classification and retrieval tasks, reaching 91.0 on GLUE and 47.7 on BEIR. Together, these results show how far encoder performance can be pushed and provide a principled basis for compute allocation, masking ratio design, and knowledge transfer in bidirectional models.

---


### 147. [Toward System One Clinical Intelligence: Parameter-Efficient Fine-Tuning and Counterfactual Explainability of Decision Foundation Models](https://arxiv.org/abs/2610.15029)

**<font color=#1a73e8>作者：</font>** S. M. Mahbub Uddin Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated disease classification from patient-reported symptoms requires balancing the speed of lightweight discriminative models against the contextual understanding and latency costs of autoregressive large language models (LLMs). Decision foundation models offer an alternative by mapping representations directly to candidate classes without free-form text generation. We adapt Clef-Flash, a 9-billion-parameter decision model built on a Qwen3.5 backbone, for 24-class disease classification on the Symptom2Disease benchmark. Using 4-bit quantized low-rank adaptation (QLoRA) with differential learning rates and a stratified split of 960 training and 240 test cases, the model achieves 95.42% diagnostic accuracy and a macro F1 score of 0.9551. This improves upon the reported zero-shot baselines of 61.67% for a remote API and 65.00% for a local unadapted initialization, and outperforms the ClinicalBERT baseline (90.90%). By evaluating candidate logits in a single forward pass without autoregressive decoding, inference takes under 80 milliseconds per record on a single GPU, yielding a reported 31-fold speedup over generative LLM baselines. To examine symptom-level evidence, we introduce a Leave-One-Symptom-Out (LOSO) counterfactual perturbation framework. Removing disease-defining symptom clauses in a psoriasis example reduces predicted-class confidence from 100.00% to 0.12% and shifts the prediction to impetigo with 99.59% confidence, while removing secondary systemic symptoms produces less than 0.01% change in confidence. These findings suggest that decision-based architectures can combine the linguistic capabilities of large foundation models with low-latency inference and symptom-level interpretability for clinical triage.

---


### 148. [What Really Works for Universal Multimodal Embeddings? A Controlled Study of Contrastive Training Strategies](https://arxiv.org/abs/2610.15035)

**<font color=#1a73e8>作者：</font>** Duo Li, Haojun Pan, Zuhao Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive learning has become the standard paradigm for multimodal representation learning, aligning semantically matched pairs while separating mismatched ones in a shared embedding space. Although various contrastive training strategies have been proposed across negative selection, batch construction, and gradient modulation, their actual effectiveness under controlled, reproducible conditions remains poorly understood. This motivates a fundamental question: Do sophisticated contrastive strategies consistently bring meaningful downstream gains in multimodal embedding learning? To address this, we systematically evaluate representative strategies under a unified benchmarking framework on MMEB. Surprisingly, direct evaluations reveal that most existing strategies offer marginal gains over a standard aligned baseline, with several even degrading overall performance. To uncover the underlying failure modes, we introduce an MLLM-as-a-Judge diagnostic framework that dissects top-1 retrieval behaviors into labeled positives, false negatives (unlabeled valid matches), and hard/easy negative errors. Our systematic analysis yields three key insights: (1) Gradient distortion: Upweighting gradients from high-similarity negatives consistently hurts downstream generalization; (2) Distribution illusion: Wider separation between positive and negative similarity distributions does not necessarily translate to better retrieval performance; and (3) Synergistic training: While false-negative mitigation or hard-batch construction yields limited gains in isolation, integrating hard-negative mining, false-negative mitigation, and hard-batch construction achieves optimal performance, delivering an average improvement of 6.0% on MMEB with Qwen2-VL-2B. Overall, our findings demystify popular contrastive strategies and provide actionable recipes for training universal multimodal embedding models.

---


### 149. [Sparsity Saves Compute, Not Samples: Oracle Inequalities for Dense and Sparse Mixture of Experts](https://arxiv.org/abs/2610.15039)

**<font color=#1a73e8>作者：</font>** Sagar Ghosh, Huy Nguyen, Alessandro Rinaldo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models combine specialized experts through an input-dependent routing mechanism, and their sparse variants underpin many modern large-scale systems. Yet the statistical cost of adaptive routing remains only partially understood. We study the estimation error of least-squares MoE estimators when both the experts and the gating network are Lipschitz in their parameters. We represent each MoE as a gate--expert pair in a Gated Hilbert Space, whose norm $\|\cdot\|_\Delta$ separates the contributions of routing and expert discrepancies. Using its empirical representation, we derive an oracle inequality with a fast rate of order $\tilde{\mathcal O}\big((Kd_{\mathrm{pr},e}+d_{\mathrm{pr},g})/n\big)$ for dense MoEs with $K$ experts. For sparse Top-$k$ and Top-$p$ routing, the selection map is discontinuous in the gating parameters. We handle this by partitioning the gating class according to the selection patterns it induces on the sample. The resulting bounds match the dense rate up to an additive routing cost governed by the Natarajan dimension of the selector. We show that such a routing-complexity condition cannot be dropped: Lipschitz continuity in the parameters alone does not suffice. For linear softmax gating, the routing cost is of the same order as the gating term. Finally, for linear experts, we establish a matching minimax lower bound of order $Kd_{\mathrm{pr},e}/n$, showing that the rates are optimal up to logarithmic factors.

---


### 150. [Information-Theoretic Foundations of Online Temperature Sampling](https://arxiv.org/abs/2610.15043)

**<font color=#1a73e8>作者：</font>** Jin Sima, Nikolaos Papagiannis, Ananth Grama 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Repetitive, degenerate generation is a persistent failure of LLM decoding, and the standard remedies (temperature, nucleus, and top-$k$ sampling) are static heuristics. By Kac's lemma and the AEP, a stationary source takes time exponential in its entropy to repeat a block. We therefore maximize the entropy of the sampling distributions under one cross-entropy budget that keeps the output plausible under the model. Offline, the solution is temperature sampling, with the inverse temperature as the budget's Lagrange multiplier. \emph{Our contribution is the online problem}: the conditionals $p_1, p_2, \dots$ are revealed one at a time, and the sampling distribution $q_t$ must be chosen causally from $p_1, \dots, p_t$ while the budget couples the entire horizon. The optimal temperature is thus a global shadow price that must be estimated from a prefix. We propose Entropic Online Sampling (EOS), which re-solves for the temperature on each prefix. We prove it loses $O(R\log n)$ entropy against the offline optimum while overshooting the budget by $O(R\log n)$, with $R$ an instance-dependent drift parameter. A budget-tightened variant is exactly feasible at the same rate. Conversely, every exactly feasible online algorithm must lose $\Omega(R)$, so EOS is optimal up to a $\log n$ factor. When the conditionals are drawn from a finite mixture, $R=\tilde{O}(\sqrt{n})$. Experiments confirm that EOS tracks the offline temperature and beats fixed-temperature sampling in entropy.

---


> [!TIP]
> 当前位于：**101-150**（第 3/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
