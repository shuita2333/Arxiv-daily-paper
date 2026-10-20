# 🧠 大模型相关研究 | 2026年10月21日

> 本类共 **548** 篇论文：已确认 **507** 篇，待复核 **41** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-548](./part-11.md)

---

### 101. [GazeAgent: VLM-Guided Implicit Gaze Calibration from Egocentric Multimodal Behavior for AI Glasses](https://arxiv.org/abs/2610.24364)

**<font color=#1a73e8>作者：</font>** Yuhong Zhang, Khanh An Nguyen, Xinyu Tian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI glasses typically require explicit, user-specific eye-tracker calibration, and accuracy can drift when the device shifts during use. We present GazeAgent, a VLM-guided framework that continuously and adaptively improves gaze-calibration accuracy from naturally occurring behavior without asking users to interrupt their activities. GazeAgent identifies precise visual attention (PVA) events from multimodal streams of inertial measurement unit (IMU), gaze, and wearer-hand signals, validates their task relevance, and localizes functional targets as pseudo-calibration targets. In a 10-participant scripted study, the system detected all 820 predefined PVA opportunities and, under device disturbance, reduced median gaze error by 44.1% compared with explicit calibration. In a five-participant case study, autonomous calibration produced the lowest workload and interruption ratings, and all participants preferred it for routine use. By deriving task-critical targets from natural multimodal behavior, GazeAgent demonstrates the potential for continuous, adaptive, and low-burden gaze interaction on egocentric AI glasses.

---


### 102. [FlashMap: Flow Map Speculative Decoding](https://arxiv.org/abs/2610.24365)

**<font color=#1a73e8>作者：</font>** Jeff Shen, Zhejian Zhou, Ryan Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model (LLM) inference by using a lightweight drafter to propose a block of tokens that the target model verifies in one parallel pass. Autoregressive drafters generate this block one token at a time, whereas block diffusion drafters such as DFlash generate it in one pass, making drafting faster. However, these diffusion drafters predict each token independently, ignoring dependencies between tokens in the block. We introduce FlashMap, a continuous flow drafter that conditions a flow map language model on the target model's hidden states and generates the whole block in one forward pass while capturing inter-token dependencies. On Qwen3-8B, FlashMap is faster than a matched DFlash baseline on every benchmark, with 7% higher average speedup and up to 6.1x lossless acceleration.

---


### 103. [WAQS: Weight Absorption for Quadratic Probing and Affine Steering](https://arxiv.org/abs/2610.24367)

**<font color=#1a73e8>作者：</font>** Ding Zhu, Mohammad Mahdi Khalili  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Activation steering provides a lightweight alternative to fine-tuning for controlling large language model behavior. Existing methods, however, often face a trade-off between efficiency and expressiveness: fixed steering vectors incur negligible inference overhead but cannot adapt to the current model input, whereas input-dependent nonlinear interventions provide greater flexibility at additional runtime cost. We introduce \textbf{WAQS} (\textbf{W}eight \textbf{A}bsorption for \textbf{Q}uadratic probing and affine \textbf{S}teering), a framework that obtains state-dependent steering, without additional inference-time computation. WAQS models a concept with a quadratic probe, whose gradient yields an affine, activation-dependent steering direction. We show that this affine intervention can be folded exactly into adjacent linear transformations through an offline weight update. Moreover, we prove that quadratic functions form the maximal class of smooth concept scores whose gradient-based interventions are affine and therefore exactly absorbable into linear layers. Under a Gaussian representation model, our formulation admits an interpretation as the difference of class-conditional Mahalanobis pulls and naturally generalizes linear discriminant and difference-in-means steering. To scale to high-dimensional representations, we introduce a low-rank parameterization of the quadratic term. Across truthfulness, refusal, and sycophancy steering tasks, quadratic steering matches or improves upon constant linear steering while preserving model utility, with the absorbed implementation introducing no additional inference-time operations. Our results suggest that quadratic probes provide a practical middle ground between static linear steering and computationally expensive dynamic nonlinear interventions.

---


### 104. [PACE-Mem: Prefix-Aware Complementary Evidence for Multimodal Agents](https://arxiv.org/abs/2610.24378)

**<font color=#1a73e8>作者：</font>** Shidu Ren, Rong-cheng Tu, Hang Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As multimodal agents accumulate experience, their long-term memories contain many similar observations of recurring scenes, actions, and entities. Answer quality depends on the evidence retrieved from these memories into the model's context. However, query-relevant memories may contain overlapping information, and a fixed retrieval depth may return too little or too much evidence for a given question. To address these challenges, we propose PACE-Mem, Prefix-Aware Complementary Evidence, which constructs a complementary evidence sequence and determines its length from the same selection trajectory. For structured memories, query-guided pooling combines records within each clip to obtain relevance scores and representations. Using these relevance scores and representations, maximal marginal relevance (MMR) selection balances query relevance against overlap with previously selected evidence. From the resulting score trajectory, a prefix-length selection algorithm determines retrieval depth by comparing length-normalized adjacent declines, accounting for both score changes and the amount of evidence accumulated. PACE-Mem is a training-free, plug-in retrieval method for clip-based agent memory systems, leaving memory construction and answer generation unchanged. Across three long-video benchmarks and two agent frameworks, PACE-Mem improves question-answering accuracy by an average of 1.6% over Adaptive-k, the strongest baseline at comparable mean retrieval depths. Further analysis reveals that jointly adding and removing evidence is associated with larger net accuracy gains than either change alone.

---


### 105. [Train Locally, Learn Together: Distributed Multi-Agent Training via ADMM](https://arxiv.org/abs/2610.24380)

**<font color=#1a73e8>作者：</font>** Yiwei Chen, Changsheng Wang, Yicheng Lang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) can outperform individual language-model agents by combining specialized roles, diverse reasoning processes, and collaborative decision-making. However, collaborative MAS training is typically centralized, requiring a common trainer to aggregate role-local trajectories and learning signals and maintain model and optimization states. This motivates a distributed multi-agent learning paradigm in which agents improve system-level capabilities through role-local learning and decentralized communication, paving the way toward scalable, resilient, and self-organizing MAS. To this end, we introduce, to the best of our knowledge, the first optimization-grounded framework for distributed MAS training based on consensus alternating direction method of multipliers (ADMM). We formulate collaborative MAS learning as a consensus-constrained finite-sum optimization problem, naturally lending itself to distributed optimization via ADMM. The proposed approach alternates role-local learning with inter-agent consensus using distributed communication protocols such as ring all-reduce, enabling joint optimization while keeping each agent's data and training state local. We evaluate our framework on distributed safety alignment and general reasoning tasks. Under compromised-agent settings, ADMM can reduce HarmBench attack success rate (ASR) by up to 26.4%, while achieving reasoning gains comparable to centralized training. These results show that distributed MAS training retains the benefits of centralized joint optimization without requiring a centralized trainer.

---


### 106. [IF-MAP: Influence-Function-Inspired Agent Prioritization in Multi-Agent Systems](https://arxiv.org/abs/2610.24383)

**<font color=#1a73e8>作者：</font>** Jie Mao, Pingchen Lu, Zikun Qu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Improving every agent in an LLM-based multi-agent system can be prohibitively costly, making it important to identify which agent should be prioritized to achieve the greatest system-level gain with limited resources. Failure attribution can inform this decision, but an agent's responsibility for failures does not directly reveal the system-level gains achievable by improving it. We therefore introduce IF-MAP, an influence-function-inspired method for identifying agents with high potential for system-level improvement. For each agent, IF-MAP measures end-to-end loss changes under controlled semantic prompt perturbations, fits a regularized local response model in a low-dimensional prompt-embedding subspace, and uses the estimated response norm as a priority score. This black-box procedure requires no access to model parameters or gradients and produces agent priorities that can guide subsequent improvement effort. We evaluate IF-MAP across six multi-agent workflows spanning code generation, question answering, and mathematical reasoning, using the same priorities for prompt optimization and model upgrades. Optimizing the selected agents' prompts achieves a macro-average gain of 3.81 percentage points, compared with 1.85 for uniform agent selection. Across five target models, upgrading the selected agents yields macro-average gains of 7.62-16.42 percentage points, compared with 3.81-8.62 for uniform agent selection. Despite its probing overhead, IF-MAP reduces Qwen3-8B and DeepSeek-V3.2 token use by 74.2% and 35.2%, respectively, relative to optimizing every agent, and reduces target-model tokens by 63.6-64.9% relative to upgrading every agent. These results support the use of IF-MAP to identify promising agents and direct improvement effort toward greater end-to-end performance gains.

---


### 107. [Bridging Exploration and Persona: Information-Directed Dueling for Test-Time Agent Personalization](https://arxiv.org/abs/2610.24385)

**<font color=#1a73e8>作者：</font>** Jie Mao, Pingchen Lu, Xiangyi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective test-time personalization requires LLM agents to adapt to query-dependent user preferences from lightweight interaction. We study persona selection with binary comparisons between candidate responses as the online signal. We present ID-TAP, a scalable, IDS-inspired neural dueling-bandit framework for large discrete persona spaces. ID-TAP combines a query-conditioned neural utility model with a lightweight Bradley-Terry explorer, and transfers comparison evidence across related queries through similarity-weighted warm starts. The neural model shares statistical strength across queries while preserving query-specific scores, and efficient BT updates score hypothetical challengers. Across seven user-conditioned generation benchmarks under reference- and model-based preference simulators, ID-TAP achieves the strongest aggregate performance among the evaluated baselines within a fixed ten-round comparison budget. These results support information-directed challenger selection as an effective design for test-time persona adaptation.

---


### 108. [Trust the Edge, Doubt the Arrow: Auditing Validation Signals for Text-Mined Clinical Causal Knowledge Graphs](https://arxiv.org/abs/2610.24390)

**<font color=#1a73e8>作者：</font>** Su Lan, Shicheng Zhou, Yiqi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical causal retrieval-augmented generation systems increasingly use knowledge graphs (KGs) mined from notes, yet extracted assertions remain candidates that require audit for patient-level EHR support and direction. We construct a directed candidate graph from 328,839 MIMIC-IV discharge summaries using LLM extraction and UMLS normalization, and evaluate three signals against SemMedDB: within-admission co-occurrence lift, cross-admission diagnosis-coding temporal precedence, and literature corroboration. Lift filters unsupported co-mentions and provides useful EHR support, but not causal proof. Coding order is a weak direction signal: among the 686 candidates where it commits, it reaches 54.2% agreement with SemMedDB, below the extractor's 69.4% on the same subset. Literature corroboration supplies independent direction evidence but covers only 30.4% of candidate relations. A MIMIC-III replication yields the same pattern: extractor direction remains stable (70.5%), whereas coding-order direction is near chance (50.9%). Thus, text-mined clinical causal candidate KGs are best treated as EHR-supported but direction-uncertain. In a leakage-controlled causal QA benchmark, lift-only retrieval achieves 35.7% accuracy; conservative causal demotion achieves 37.2% while reducing evidence-unsupported answers from 17.3% to 6.1% at fixed retrieval recall. We release code, aggregate summaries, and scripts to regenerate restricted outputs.

---


### 109. [ZeroDSS: Semantic Segmentation from Class Names Alone](https://arxiv.org/abs/2610.24405)

**<font color=#1a73e8>作者：</font>** Tian Ming, Marzi Heidari, Yuhong Guo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation depends heavily on real images with pixel-level annotations, making dense supervision a major obstacle to deployment in new domains. We study task-specific data-free semantic segmentation, where training uses generic pretrained generative priors but has access to no target-domain images, masks, or captions--only a predefined category set. We introduce Zero-Data Semantic Segmentation (ZeroDSS), a feedback-driven approach that treats synthetic supervision as an adaptively controllable training distribution rather than a direct surrogate for real data. ZeroDSS constructs a semantically structured prompt distribution through LLM-guided compositional generation and adaptive class rebalancing, then converts the prompts into image-mask pairs using diffusion attention. Its feedback-driven distribution refinement consists of a two-phase closed-loop training procedure with a single loop-back step. In Phase I, a segmenter is trained using confidence-weighted supervision and dual-scale consistency. In Phase II, model feedback is used to adaptively target underperforming categories and refine diffusion-derived masks using model predictions. After this refined initial training, a teacher-student framework is utilized in the final phase to iteratively improve the fused supervision and segmenter through exponential moving average (EMA) updates. Using synthetic training data only, ZeroDSS achieves 35.0% mIoU on MS COCO with DeepLabV3, and 66.3% and 63.5% mIoU on PASCAL VOC with DeepLabV3 and Mask2Former, respectively. These results show that explicitly constructing and iteratively refining the synthetic supervision distribution can substantially reduce the synthetic-to-real gap in dense prediction.

---


### 110. [Ask Less, Ask Better: Allocating User Attention in Proactive LLM Agents with Interruption Budgets](https://arxiv.org/abs/2610.24411)

**<font color=#1a73e8>作者：</font>** Xuanming Zhang, Amir H. Rezaeian, Miguel Ballesteros 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents can ask clarifying questions to complete tasks, but answering each question demands users' time and effort. Existing evaluations typically measure this burden by counting questions, treating necessary and avoidable questions equally. We propose an evaluation protocol that distinguishes how often agents ask from how well they ask. An interruption budget limits the number of questions, while a user-attention cost charges extra for questions that are hard to read or not worth asking, as rated by a human-validated LLM judge. Beyond question counts, this cost captures perceived effort: on conversation pairs with the same number of questions, human annotators agreed with the cost on which conversation required more effort 75% of the time. Across eight LLMs and four customer-service domains, limiting agents to one to three questions reduces user-attention cost by 36-73% while keeping 86-94% of the task reward they earn with unlimited questions. At the same budget, reviewing each question against the memory of users' earlier answers cuts attention cost by another 13% with little reward loss and yields more valuable questions. Models also differ sharply in how well they ask: at the same user-attention cost, the most efficient models gain more than twice as much reward from their questions as the others. These results show that asking less and asking better are distinct goals, and that evaluations of proactive agents should measure both.

---


### 111. [Transformers as Adaptive Kernel Learners across Tasks for In-Context Learning](https://arxiv.org/abs/2610.24441)

**<font color=#1a73e8>作者：</font>** Zhaiming Shen, Alexander Cloninger, Rongjie Lai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers have emerged as a dominant architecture in modern machine learning, with in-context learning (ICL) enabling models to adapt to new tasks by conditioning on prompts, without any parameter updates. To understand the attention mechanism in transformer blocks, a growing line of theoretical work interprets ICL through the lens of classical statistical estimators. Recent works have established a connection between the attention mechanism and kernel methods, while the kernel function is usually assumed to be fixed. In practice, the query and key matrices in the attention mechanism are trained, which allows the attention mechanism to serve as an adaptive kernel method. In this work, we demonstrate that transformers can act as adaptive anisotropic kernel learners. Specifically, we study ICL for low-rank linear and multi-index nonlinear regressions, and conduct numerical simulations to show that the learned attention scores closely resemble the oracle kernels for these function classes. We then develop a general framework to analyze the generalization error of ICL by connecting transformers to the oracle kernel estimator for each function class. Our theory gives an explicit and constructive implementation of the oracle kernel estimators for these function classes using a wide and shallow transformer architecture, illustrating how the prediction is carried out by the interaction between the query token and the context tokens. Our work complements existing studies by providing numerical and theoretical evidence of how the attention mechanism adapts to anisotropic kernels in both linear and nonlinear settings.

---


### 112. [Do 3D Large Language Models Really Use 3D Evidence?](https://arxiv.org/abs/2610.24447)

**<font color=#1a73e8>作者：</font>** Yifei Zhao, Fanyu Zhao, Han Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent 3D Large Language Models (3D-LLMs) have shown strong performance on scene question answering with extensive post-training. Yet, existing benchmarks rarely evaluate how 3D-LLMs respond to referential ambiguity, insufficient scene evidence, or false presuppositions, obscuring whether their responses are grounded in 3D evidence. In this work, we introduce UNICORNS, a benchmark for evaluating the reliability of 3D-LLM responses across four evidence conditions. UNICORNS contains 11,387 questions across 557 ScanNet scans, covering eight challenge categories alongside answerable controls. A response passes only if it satisfies the required response behavior and contains no scene claim unsupported by the available evidence. Evaluation of six open-sourced 3D-LLMs reveals a pronounced performance gap: even the strongest zero-shot model achieves 61.22% accuracy on answerable controls, but only 40.94% across the eight challenge categories. To address this gap, we further propose HORN, an obligation-aware post-training method combining group-relative task rewards, leaf-conditioned obligation rewards, and supervised control replay. Extensive experiments demonstrate that HORN reaches $75.1 \pm 1.0\%$ across the challenge categories and $77.2 \pm 0.8\%$ overall, outperforming all baselines without degrading answerable-control accuracy. Our findings enable a systematic evaluation and improvement of evidence-grounded 3D reasoning for 3D-LLMs (code: this https URL).

---


### 113. [HumanSkill-4D: Training-Free Language Querying of Animatable Gaussian Avatars in Space and Time](https://arxiv.org/abs/2610.24452)

**<font color=#1a73e8>作者：</font>** unsu Kim, Naeun Kim, Dongyoon Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce avatar referring segmentation, which selects regions of animatable Gaussian avatars from language queries. A query can also specify a pose or motion to select matching intervals. This lets users interact with avatars for local editing and motion inspection. However, making these selections with existing language Gaussian splatting methods poses two challenges: adjacent parts and garments are hard to separate and may be referred to indirectly (region ambiguity), while fine-grained motions can look alike in RGB (motion ambiguity). We address these challenges with HumanSkill-4D, a training-free framework that shares a multimodal large language model (MLLM) and geometric operators across avatars. For each avatar, a semantic memory links body-part and garment categories to persistent Gaussian regions and appearance descriptions. The MLLM uses category names and descriptions to select categories by appearance, relation, or function. To find matching intervals, it composes operators into programs that check query conditions on driving joint trajectories stored in a motion memory. These category choices and operator outputs make selections traceable, while composing or adding operators supports new motion conditions. To evaluate this task, we introduce three human-annotated benchmarks and show that HumanSkill-4D outperforms the baselines in part segmentation and 3D and 4D referring segmentation, with compact memories and only minutes of setup per avatar.

---


### 114. [Hippo: Training-Free Agent Self-Evolution via Hippocampal Replay](https://arxiv.org/abs/2610.24453)

**<font color=#1a73e8>作者：</font>** Yutong Song, Jiang Wu, Yuxuan Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Motivated by recursive self-improvement (RSI), we study how LLM agents can learn through external memory without updating model parameters. Extracting useful experience from a single attempt is difficult: flawed reasoning can produce success, while poor execution can obscure a sound strategy. Preserving its value over time is also difficult: our accumulation baseline without consolidation initially improves but eventually performs below a no-memory baseline. Our key idea is to compare attempts at the same task to identify reusable decisions and refine when they apply. We introduce Hippo, a memory framework inspired by selective hippocampal encoding and replay that learns from these comparisons when shortcomings are diagnosed. It compares the resulting experience with existing memory to merge overlaps and resolve conflicts through explicit applicability conditions. This allows prior guidance to be revised without storing every lesson as a separate entry. Experiments on SWE-bench Verified, WebArena, and Mind2Web show performance gains in all three settings and substantially fewer retained experiences than the accumulation baseline. The gains extend across the evaluated base models of varying capabilities, indicating that memory-based adaptation remains useful even for highly capable models.

---


### 115. [MELD: Recursive Self-Improvement via Hierarchical Coordination for Multi-Agent Scientific Discovery](https://arxiv.org/abs/2610.24454)

**<font color=#1a73e8>作者：</font>** Sizhe Tang, Zuyuan Zhang, Zeyu Fang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent scientific discovery with large language models raises a coupled learning problem: research assignments determine both which experiments are pursued and the experiences from which agents adapt. We introduce MELD, a unified hierarchical test-time training framework that jointly adapts a team-level Coordinator policy and agent-level individual Scientist policies within a single discovery process. The Coordinator generates a joint portfolio of search branches and research directives over a shared derivation tree, while Scientists develop hypotheses and execution plans implemented by a shared frozen Executor. Both levels receive alternating GRPO-style parameter updates under a shared smooth best-of-budget objective, allowing team organization and individual research behavior to co-evolve in a recursive self-improvement loop. Our analysis establishes objective alignment for the hierarchy, characterizes conditions for coordination gains over independent parallel discovery and the first-order benefit of private adaptation, and derives a finite-budget regret bound for adapted models. On 22 MLGym and MLE-bench tasks, MELD is best on 20 of them and achieves the highest aggregate normalized scores on MLGym, using a 4B backbone for coordination and research. Most baselines use proprietary Scientists, and all systems share one frozen Executor.

---


### 116. [Generative Retrieval for Reverse Target Fishing with a Proteome-Scale Benchmark](https://arxiv.org/abs/2610.24458)

**<font color=#1a73e8>作者：</font>** Zhichao Deng, Haichuan Tan, Xin Hong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reverse target fishing identifies protein targets for a query molecule and is central to drug discovery and repurposing. Discriminative approaches adapted from virtual screening face sparse, long-tailed associations and missing-not-at-random measurements: treating unrecorded pairs as negatives can suppress genuine targets. We reformulate the task as generative retrieval and introduce GenFish. Residual vector quantization converts frozen protein language model features into shared semantic identifiers. Given a molecular fingerprint, GenFish autoregressively models codes conditioned on the query and preceding code, ranking proteins by identifier likelihood without explicitly labeling unrecorded pairs as negatives. We introduce ProTargetBench, the first proteome-scale benchmark for reverse target fishing to jointly support measured-panel discrimination and full-catalogue recovery of experimentally recorded positives. Covering 20,431 UniProt-reviewed human proteins, it integrates curated bioactivity evidence and distinguishes experimental inactivity from unmeasured associations. On 198 held-out molecules, GenFish achieves higher mean performance across all three full-catalogue retrieval metrics than four discriminative neural baselines and three non-neural baselines, including ligand-based methods. A controlled positive-hiding experiment shows that targeted removal of false-negative competition improves contrastive retrieval beyond matched random masking; GenFish remains stronger under the same incomplete supervision. Pfam alignment indicates that the semantic identifiers capture biologically meaningful relationships among proteins. These results establish generative retrieval as a principled paradigm for reverse target fishing under incomplete bioactivity records.

---


### 117. [Which Long Documents Matter? A Controlled Study of Data Selection for Context Extension](https://arxiv.org/abs/2610.24469)

**<font color=#1a73e8>作者：</font>** Junlong Jia, Jiang Zhou, Xing Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural long documents are widely used for context extension, but which selection pipelines are effective remains unclear. We conduct a controlled comparison on Qwen2.5-3B at 128K under matched 6B-token continued-training budgets. Random sampling of natural long documents (random-long) outperforms repacking at longer evaluation lengths. Within the same candidate pool, selecting documents with high LongPPL key-token density yields further gains, unlike the evaluated generic-quality and LLM-judge selectors. We introduce truncLongPPL to reduce scoring cost by computing key-token density over a truncated prefix. At 128K, scoring the first half of the reference span yields downstream performance close to full-span scoring with a measured $2.28\times$ end-to-end scoring speedup. Across three training seeds, truncLongPPL achieves the highest mean scores among evaluated pipelines, exceeding random-long by 4.54 points on validation HELMET and 3.28 on held-out RULER, with gains most consistent in retrieval. At a 256K target context, it gains 2.82 average RULER points over random-long on Qwen2.5-3B. In short/long mixed training across Qwen2.5-3B, Qwen3-8B, and OLMo~3-7B, it gains 1.47--7.31 average RULER points over random-long mixing, with seven-task short-context averages within 0.23 points of the corresponding baselines. After supervised fine-tuning (SFT), Qwen3-8B and OLMo~3-7B models trained with selected long documents outperform their random-long counterparts by 1.13--1.67 points on LongBench v2 and 0.62--1.44 points on MRCR.

---


### 118. [Pluralistic Alignment in Language Models: Objectives, Human References, and Preference Representations](https://arxiv.org/abs/2610.24471)

**<font color=#1a73e8>作者：</font>** Meng-Chen Wu, Umesh Bodhwani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pluralistic alignment aims to represent meaningful variation in human preferences rather than collapse heterogeneous judgments into a single target. Yet existing work often mixes three distinct questions: what pluralistic behavior a model should exhibit, whose preferences define the reference, and what evidence is sufficient to demonstrate success. We organize the literature around a two-layer taxonomy. Layer 1 distinguishes representing a range of human-supported viewpoints (Overton Pluralism), adapting faithfully to a specified perspective or preference condition (Steerable Pluralism), and matching the response distribution observed in a target population (Distributional Pluralism). Layer 2 distinguishes aggregate populations, countries and regions, and subgroups as human references. Preference representation, implementation mechanism, modality, and evidence quality are treated as cross-cutting design choices rather than additional forms of pluralism. We synthesize a protocol-bounded corpus of 70 works on pluralistic alignment and neighboring areas, using the objective-by-human-reference matrix to map existing approaches and identify underexplored combinations. The coded literature concentrates on Steerable Pluralism and Distributional Pluralism, while eligible Overton Pluralism work appears only at the aggregate-population level under our stated protocol. We then connect each objective to the evidence needed to support it, including perspective validity, conditional fidelity, distributional fidelity, support preservation, and uncertainty in subgroup estimates. Together, the taxonomy and evaluation framework clarify what current methods establish, where their claims exceed their evidence, and how future systems can represent disagreement without mistaking variation for faithful representation.

---


### 119. [Ben-Misandry: A Bengali Dataset and Late-Fusion Transformer Framework for Detecting Anti-Male Gender Hate](https://arxiv.org/abs/2610.24474)

**<font color=#1a73e8>作者：</font>** Md Mehedi Hasan Nipu, Chinmoy Mitra, Tarannum Ahmed Nowshin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Gender based hate speech research in Bengali has focused almost exclusively on misogyny, leaving anti male hate, or misandry, entirely unstudied for this language and creating a systematic blind spot in moderation systems trained to catch attacks on women but not on men. We introduce Ben-Misandry, the first Bengali misandry detection dataset: 5,000 comments across six taxonomy classes, including a novel category for mocking male emotional vulnerability with no direct analogue in existing misogyny taxonomies. The corpus is taxonomy-controlled synthetic data generated with GPT-4.1, spot-checked by four human reviewers on a 500-comment sample who confirmed the large majority of assigned labels; a full inter-annotator- agreement study is left to future work. We benchmark it with a classical pipeline (seven classifiers over four text representations) and a transformer pipeline (BanglaBERT, XLM-RoBERTa, and two fusion strategies). The best classical model, a linear SVM over character-level TF-IDF, reaches 91.8% accuracy; a late fusion ensemble averaging BanglaBERT and XLM-RoBERTa softmax outputs reaches 96.6% accuracy and macro ROC-AUC above 99%, nominally ahead of every single model and early fusion, though we have not run significance testing to confirm these margins are meaningful. We relate this to classifier combination theory, under which averaging encoders with decorrelated errors is expected to reduce variance, and corroborate the decision boundary with Shapley explanations that recover the same class- discriminative vocabulary found in our exploratory analysis, while noting this cannot rule out the model partly keying on synthetic-generation artifacts. Our results indicate misandry detection in Bengali is feasible and measurable on this synthetic corpus, offered as an initial public resource pending validation on real-world data.

---


### 120. [Write Once, Check Many: Reusable Ledgers for Post-Hoc Policy Compliance Auditing of Agent Trajectories](https://arxiv.org/abs/2610.24483)

**<font color=#1a73e8>作者：</font>** Ashwin Nagarajan, Gursimran Panesar, Alicia Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Auditing LLM agents against policies is critical to ensure safety but requires rereading long trajectories once per policy. Can we instead record each trajectory once and reuse that record for policies not known in advance? We propose write once, check many, a framework in which a writer model converts each agent trajectory into a policy-independent ledger of the agent's actions and outcomes. A reader then checks each new policy against the ledger alone, without access to the original trajectory. On 900 trajectories from SHADE-Arena, $\tau$-bench, and $\tau^2$-bench, we show that a 12B reader of narrative ledgers can either match or in fact achieve higher AUC than the same 12B model reading full trajectories. On SHADE-Arena policies that combine several facts, our approach outperforms a 31B model reading the trajectory (.777 vs. .713 AUC). When checking eight SHADE-Arena policies separately, ledgers use about $5\times$ fewer tokens, including the cost of writing them. A deeper analysis shows that rule-based extraction performs better on some single-action policies, and ledgers can miss evidence in long tool outputs and message contents. Our results suggest that reusable, policy-independent records can make retrospective agent auditing more efficient and effective, and highlight important considerations in ledger design.

---


### 121. [Modeling Discourse Profiles in Climate Misinformation Discourse](https://arxiv.org/abs/2610.24489)

**<font color=#1a73e8>作者：</font>** Ge Gao, Zhengyang Shan, Bryan A. Plummer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prior work on climate misinformation detection typically classifies individual comments or claims using text alone. This framing overlooks a key property of online climate discourse: misinformation is often produced, reinforced, and sustained through recurring rhetorical patterns that reappear across comments and threads. Using a large-scale TikTok climate discourse dataset, we construct discourse profiles by clustering climate-related comments into recurring rhetorical patterns. We then incorporate these profiles into fine-grained climate misinformation classifiers using a late-fusion architecture. Under video-disjoint evaluation across three training seeds, discourse-profile-aware models significantly improve macro-F1 over text-only baselines for bag-of-words, TF-IDF, and MPNet representations. RoBERTa-large exhibits a positive mean improvement but substantially greater variability, and the difference is not statistically significant. Beyond classification, our results show discourse profiles shape misinformation reception and propagation. Discourse-profile-conditioned language model agents exhibit misinformation acceptance patterns aligned with profile-level misinformation prevalence in ClimateDisc, and the relationship between misinformation prevalence and engagement persistence differs across dominant discourse profiles.

---


### 122. [ConCI: A Controlled Counterfactual Benchmark for Contextual Integrity in LLMs](https://arxiv.org/abs/2610.24494)

**<font color=#1a73e8>作者：</font>** Juhyeon Park, Sumin Yu, Taesup Moon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Contextual integrity (CI) holds that the appropriateness of sharing personal information depends on the context of the information flow, not on the information alone. However, existing CI benchmarks often use independent scenarios that vary multiple CI parameters simultaneously and are dominated by inappropriate flows, making it unclear whether correct predictions reflect sensitivity to context or a general refusal tendency. We present ConCI, a controlled-counterfactual benchmark in which an anchor flow is paired with two counterfactuals that each modify a single CI parameter. The resulting triplet is scored jointly, with credit given only when all three flows are judged correctly. Built from six existing benchmarks, ConCI contains 1,592 flows in 556 triplets, is approximately label-balanced, and is validated by seven human annotators per flow. Across seven LLMs, many correct anchor predictions fail on at least one counterfactual, and even the strongest model errs on about a fifth of triplets. Furthermore, models perform near ceiling on inappropriate flows but weaker on appropriate ones, often continuing to judge a flow inappropriate even when a contextual change should make it appropriate. Larger models narrow this bias toward non-disclosure but do not eliminate it, and reasoning yields only modest gains.

---


### 123. [CoTs remain monitorable when being unfaithful requires computation: Replicating and Extending the Necessity Effect Across Eleven Models](https://arxiv.org/abs/2610.24495)

**<font color=#1a73e8>作者：</font>** Arav Dhoot, Yixiong Hao, Zephaniah Roe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While a LLM's chain of thought (CoT) is a promising approach to interpreting model outputs, prior work shows CoT's content does not always accurately reflect the reasoning process. Emmons et al. (2025) finds that models can follow a question hint without revealing so in its chain of thought, but when the hint is sufficiently complex the computation is forced into the CoT. This claim, however, has only been tested on Gemini models, and the datasets and code is closed source. We replicate their proxy task across eleven models from six families and find the necessity effect generalizes. Every model follows simple cues above a no-hint baseline, while concealed complex-cue following falls back near baseline for most models. We also extend the study from Emmons et al. (2025) to measure CoT-necessity and unfaithfulness across five cue families (four of them new) and three difficulty levels. The relationship between when CoT is necessary and unfaithfulness is task-specific and model-specific. For some hint types, models often verbalize their hint-following behavior even when the hint can be decoded in a single forward pass. These results support the case for CoT monitoring when unsafe behavior requires non-trivial computation, and that properties of CoT unfaithfulness are sensitive to model and setting.

---


### 124. [TideKV: Delayed KV Eviction via Layer-Wise Chunked Prefill for Memory-Efficient Long-Context LLM Inference](https://arxiv.org/abs/2610.24499)

**<font color=#1a73e8>作者：</font>** Yu Wang, Zhu Wang, Ning Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context large language model (LLM) inference is important for modern intelligent applications but remains constrained by peak memory during prompt prefill. Existing KV cache compression reduces decoding memory but typically requires full-prompt prefill to preserve global context, retaining a high construction peak. Online chunk-level eviction lowers memory earlier but selects before each layer has observed the complete prompt, potentially degrading cache construction and decoding. We present TideKV, an on-GPU cache-construction architecture using layer-major delayed eviction. TideKV processes all prompt chunks within each Transformer layer, retains full-prompt KV only for the active layer, and evicts at layer end. This schedule preserves full-prompt-aware selection while reducing activation and temporary memory. Experiments across multiple computing platforms show that TideKV preserves the inference quality and final cache size of the evaluated compression methods. At 64K on A100, it reduces the construction-time transient footprint by 83.89%. On RTX 4090, it increases time to first token by only 1.06% at 64K and enables 128K prefill. TideKV also completes 128K on Jetson, whereas matched post-prefill compression runs out of memory on both resource-constrained platforms. These results show that delayed layer-end eviction substantially expands feasible context lengths without sacrificing cache utility.

---


### 125. [Investigating Length Bias and Robustness in LVLMs for Multiple-Choice Question Answering](https://arxiv.org/abs/2610.24500)

**<font color=#1a73e8>作者：</font>** Md. Atabuzzaman, Hani Alomari, Chris Thomas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) demonstrate strong performance on multiple-choice question answering (MCQA), yet their reliability under biased conditions remains underexplored. We investigate length bias, the systematic preference for longer answer options, through controlled benchmarks spanning fine-grained visual domains. LVLMs consistently favor longer options even when visually inconsistent, with accuracy dropping 2--38\% when correct answers are shorter and increasing 1--70\% when longer. This bias persists across model scales. Through layer-wise mechanistic analysis, we reveal that length bias emerges from late-layer suppression of visual evidence in favor of language-side length priors. Blurry-image experiments show that bias intensifies when visual evidence weakens, while abstention tests reveal that LVLMs struggle to refuse incorrect predictions. We propose and evaluate multiple inference-time mitigation strategies; while these provide partial improvements, none achieves deployable bias mitigation without relying on oracle information unavailable at inference time. These results underscore that inference-time interventions are insufficient, pointing to the need for architectural solutions and bias-aware training.

---


### 126. [ProbePO: Sparse Probes, Redistributed Credit for Critic-Free LLM Reinforcement Learning](https://arxiv.org/abs/2610.24515)

**<font color=#1a73e8>作者：</font>** Diyi Hu, Ruizhong Qiu, Lin Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from verifiable rewards assigns one terminal reward to an entire reasoning trajectory, obscuring how individual reasoning steps contributed to the outcome. GRPO broadcasts a group-normalized advantage to every response token, while finer-grained approaches often rely on dense auxiliary rollouts or branching schemes that can also alter the data used for policy updates. We cast the missing middle as budgeted measurement: with a limited rollout budget, which partial solutions should be evaluated, and how should their value estimates refine credit? ProbePO selects partial-solution states with a reward-free uncertainty score and estimates their expected verifier rewards under a capped continuation budget. ProbePO redistributes, rather than replaces, GRPO's trajectory-level advantage across tokens while preserving each trajectory's mean token-level advantage; probe continuations serve only as measurements. Across three DeepSeekMath and Qwen-family models spanning 1.5B-7B parameters, ProbePO consistently outperforms GRPO and achieves the highest accuracy among the four evaluated methods in 16 of 18 model-benchmark comparisons. Against dense-probing VinePPO on DeepSeekMath-7B, ProbePO achieves higher accuracy on all six benchmarks with 76% less end-to-end training time.

---


### 127. [Axiomatic World Modeling for Physics Reasoning](https://arxiv.org/abs/2610.24519)

**<font color=#1a73e8>作者：</font>** Xinye Yang, Zhenyang Liu, Yuxuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent research-level physics-reasoning benchmarks for LLMs reveal a failure mode that lies not in knowledge or execution, but in modeling the world being reasoned about. Models often silently alter given quantities, fabricate laws, or inject unstated assumptions to force a problem into familiar patterns, and then reason inside this corrupted world. We define this premise-level divergence as modeling drift: the gap between a model's internal axiomatic world model (AWM) and the true physical world specified in the problem. Although RLVR and PRM have yielded substantial gains in mathematics and code, their reward shapes do not directly supervise world modeling in axiomatic domains such as physics. We propose Reinforcement Learning with Axiomatic World Modeling (RLAWM), which optimizes the policy by penalizing divergence between its inferred axiomatic world model and the true physics world. RLAWM probes physics reasoning at two hierarchical levels (modeling and solving), each scored by a physically grounded reward. The modeling reward targets abstract knowledge formulation, evaluating whether the model captures the true axiomatic world before attempting calculation. The solving reward targets instantiated knowledge reasoning, checking whether the model's concrete derivation remains consistent with the axiomatic world. This two-level structure separates what world the model believes it is reasoning in from how it reasons within that world. The framework operates exclusively during training, with no extra cost during inference. RLAWM improves performance by up to +12.2 points on PhysReason and +5.2 on PHYSICS over the baseline. It also generalizes zero-shot across difficulty, source, and domain, with a 2.45x gain and +10 points over the strongest baseline on olympiad-level physics and math.

---


### 128. [HABIT-Bench: Evaluating Habit Induction from Longitudinal Weak Evidence in Agent Memory](https://arxiv.org/abs/2610.24520)

**<font color=#1a73e8>作者：</font>** Junming Zhang, Rubin Wei, Xu Cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In long-term interactions with large language model (LLM) agents, users reveal habits through their choices and actions. These habits capture implicit user information that agents must infer across conversations. However, individual observations may provide only partial evidence about a habit or when it applies. Retaining past interactions alone does not ensure that agents can infer habits and apply them appropriately. We introduce HABIT-Bench to evaluate how well agent memory systems infer habits from weak evidence and apply them to later requests. We construct synthetic user histories from task-oriented dialogue data and controlled habit graphs. The histories span hundreds of sessions across food, finance, software, and travel. Four-choice tasks assess agents' ability to infer user habits and apply them appropriately. They include temporary exceptions, changes in habits, and suggestions that users have not accepted. Sampled tasks undergo independent human review. We evaluate eight memory methods with Qwen3-235B-A22B and GLM-5.3-Flash. The best-performing memory method achieves 33.61\% macro accuracy across the four domains. Performance remains limited even when annotated evidence is supplied directly. These results expose a persistent gap between access to past interactions and the ability to infer and appropriately use user habits.

---


### 129. [Comparing Sparsified MLPs and Transcoders: Many Transcoder Features Are Neurons in Disguise](https://arxiv.org/abs/2610.24521)

**<font color=#1a73e8>作者：</font>** Stepan Shabalin, Mateusz Piotrowski  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> MLP neurons in transformer language models are widely understood to be polysemantic, motivating transcoders - sparse, learned approximations of MLP layers - as interpretable replacement models for mechanistic analysis. However, recent work shows that MLP neurons can be used to recover sparse, interpretable circuits (Arora et al. 2026, Ye et al. 2025), raising the question of whether transcoders are necessary for circuit analysis.
We define neuron features as transcoder features whose weights are strongly aligned with individual MLP neurons, and show that they account for a substantial fraction of active features in late layers across 13 open-source transcoders. Only neuron features have a stable correspondence with something in the underlying MLP: other features vary more between training runs, do not match the MLP's Jacobian, and change less significantly from their random initialization. Our findings reframe MLP neurons as a stronger basis for interpretability than commonly assumed, and call for better methods of attributing the non-neuron structure that is used by the model.

---


### 130. [VisConf: Quality-Aware Consensus for Best-of-N in Vision-Language Model Reasoning](https://arxiv.org/abs/2610.24526)

**<font color=#1a73e8>作者：</font>** Muhammad Usman, Muhammad Qasim Ayub, Usman Ahad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Best-of-N methods improve text-only LLM reasoning by sampling multiple trajectories before selecting an answer. For Vision-Language Models (VLMs), answer frequency and model confidence alone can be insufficient, as sampled generations also vary in their engagement with the visual input. We find that distributional confidence and visual attention are complementary indicators of rollout quality. Each is limited on its own, while trajectories that show strong signals in both are more likely to be correct. Motivated by this, we introduce VisConf, a rollout-quality score that multiplicatively combines visual engagement with candidate-calibrated Self-Certainty, penalizing rollouts that are weak in either signal. We incorporate Rank-Weighted Consensus (RWC), a tuning-free aggregation rule that converts within-question VisConf ranks into answer-level vote weights. Across three VLMs on MathVista, MMMU-Pro, and MMStar, VisConf with RWC consistently outperforms strong BoN baselines. Our analysis shows particularly large gains when correct trajectories are present but underrepresented in the candidate pool.

---


### 131. [From Score to Diagnosis: Search-Independent Post-Diagnosis for Symbolic Regression](https://arxiv.org/abs/2610.24535)

**<font color=#1a73e8>作者：</font>** Qian Li, Yuxiao Hu, Juncheng Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression (SR) solvers employ diverse search mechanisms, yet most rely on the same low-information scalar fitness. Such scores provide little guidance on why a skeleton fails or how it should be revised. Recent methods develop new methods to address this bottleneck. Their enhanced feedback mechanisms are tightly coupled to their search processes and are difficult to reuse across diverse SR solvers. Instead, we ask whether a shared feedback mechanism can further improve diverse solvers facing the same bottleneck. To this end, we propose PostDiag, a search-independent feedback mechanism, which can be shared to different SR solvers. PostDiag introduces Patch-wise Feature Profiling (PFP) to capture local behavior through patch-wise features of level, trend, and roughness. Based on PFP, PostDiag quantifies Skeleton Expressiveness Risk by comparing the fitted candidate with the observations, and Skeleton Stability Risk by measuring variability of behavior after bootstrap refitting. The Diagnostic Risk Plane (DRP) combines two risks to determine whether a skeleton should be preserved, repaired, simplified, or rewritten, while the patch-wise discrepancies provide evidence for the intervention. An LLM editor then performs the diagnosis-guided intervention, and the validated revision is returned to the original solver through a lightweight adapter. Experiments across multiple LLM-based and GP-based SR solvers show that PostDiag consistently improves accuracy and accelerates convergence.

---


### 132. [Write Once, Query Many: Evolving Compact Reusable Memory for Long Videos](https://arxiv.org/abs/2610.24537)

**<font color=#1a73e8>作者：</font>** Kerui Chen, Jinglu Wang, Yun Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long videos often exceed the context capacity of multimodal large language models (MLLMs), while agentic search repeats costly video processing and grounding for each query. Reusable memory can amortize this cost, but must preserve information for questions unknown during construction. We propose Video-EMem, an evolvable video memory harness built on time-anchored perceptual observations. This representation combines compact free-form text with sparse images to preserve semantic content and complementary visual details across temporal scales, supporting temporal navigation without a fixed semantic schema. A Writer encodes each video once by consolidating overlapping multiscale observations, and a Reader retrieves and organizes evidence solely from the resulting memory. With the underlying models frozen, we evolve their workflows and operators using distinct feedback: query-independent source fidelity and coverage for the Writer, and QA failures in evidence localization and utilization for the Reader. Experiments support this separation for generalization beyond development queries, with our evolution strategy improving average accuracy by 7.2% over the unevolved harness. While reducing storage by about 99.86% on average relative to raw videos, Video-EMem improves Qwen3-VL-30B by an average of 2.6% across three long-video QA benchmarks over direct input of 2,048 frames. Using the same o3 answer model as the state-of-the-art agentic method, it improves average accuracy by 2.5% with lower per-query latency.

---


### 133. [EGIP: An Evidence-Grounded Interaction Protocol for Clinical Agents](https://arxiv.org/abs/2610.24539)

**<font color=#1a73e8>作者：</font>** Zecheng Ren, Ruichen Cong, Yi Min Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interactive clinical agents acquire evidence through patient dialogue and diagnostic examinations, yet their performance also depends on how the interaction environment exposes information, available actions, and examination results. When these conditions are implicit or inconsistently controlled, final-answer accuracy can conflate diagnostic reasoning with the effects of the interaction protocol. We propose the \textbf{E}vidence-\textbf{G}rounded \textbf{I}nteraction \textbf{P}rotocol (EGIP), which enforces role-specific information boundaries, exposes diagnostic actions without revealing their results, retrieves examination results from stored clinical records, and organizes acquired evidence for final decision-making. By separating evidence acquisition from terminal prediction, EGIP enables different decision strategies to operate on the same observations. We evaluate EGIP across two clinical-agent frameworks, five datasets, and six language models. EGIP improves diagnostic accuracy over native baselines across all primary comparisons. A clinician review further shows that the proportion of automatically scored correct responses jointly judged evidence-supported rises from 10.20\% to 36.55\%. These findings support the effectiveness of EGIP as a unified interaction protocol for improving clinical-agent performance through controlled evidence access and acquisition.

---


### 134. [From Stories to Features: Scaling Concept Vectors for AI Alignment & Interpretability](https://arxiv.org/abs/2610.24556)

**<font color=#1a73e8>作者：</font>** Dmitry Scherbakov, Oleg Chernikov, Victoria Khamash 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study feature vectors: directions in a language model's activation space that correspond to human-interpretable concepts, such as honesty or deception. Existing unsupervised methods like sparse autoencoders attempt to recover the whole feature space, often at the cost of feature quality and interpretability. We take a more pragmatic route: focusing on concepts relevant to AI safety and alignment, we generate synthetic concept-antagonist story pairs and use the difference of their mean model activations as a feature vector. We scale this approach to 1,036 alignment-relevant concepts using 2M synthetic stories across multiple languages and genres, which we publicly release. Across six models from three model families, our feature vectors reliably generalize to detecting their corresponding concepts in chat dialogues and web text. They form an interpretable geometry shared across models and can causally steer model behavior when injected into activations. We further use these features to analyze model representations during jailbreak attacks, mathematical and agentic reasoning. Our targeted feature construction thus offers a scalable route to studying concepts in language models, potentially extending to millions of features across arbitrary domains.

---


### 135. [Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing](https://arxiv.org/abs/2610.24590)

**<font color=#1a73e8>作者：</font>** Yujia Yang, Quan Yuan, Jiawei Fan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving. However, the massive parameter scale of VLAs strains onboard computational resources during real-time inference. This directly increases energy consumption and limits vehicle battery range, making it critical to minimize computational overhead without compromising driving capability and explainability. Current research on efficient VLA-based driving focuses on sequential adaptation (\textit{e.g.}, Chain-of-Thought and token adjustment), leaving structural adaptation underexplored despite parameter redundancy across dynamic driving scenes. To address this gap, we propose Scene-Adaptive VLA, an efficient framework leveraging dynamic layer routing to adjust active parameters based on real-time scenes. Inspired by the temporal continuity of scenes and model predictive uncertainty, our approach characterizes model-perceived scene complexity via frame-level temporal scene variations and decision deviations. To uncover latent scene-to-parameter correspondences, we encode this characterization into scene-aware tokens, alongside two specialized queries. A budget-conditioned layer routing mechanism evaluates these refined queries to allocate a budget that determines the active parameter ratio and subsequently selects appropriate layer combinations. The entire framework is optimized end-to-end. Extensive evaluations on the Bench2Drive benchmark show that when adapted to a state-of-the-art VLA model, our approach significantly reduces inference-time computational overhead by 53.5\% with negligible degradation in driving and language capabilities. Code is available at https:github.com/yang-luvu/Scene-Adaptive-VLA.

---


### 136. [Training with Ciphers to Enhance In-Context Terminology Learning For Translation from Rare Languages](https://arxiv.org/abs/2610.24593)

**<font color=#1a73e8>作者：</font>** Deevyanshu Malu, Deeptanshu Malu, Sunita Sarawagi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning LLMs with in-context examples (IC-Train) lets translation models adapt to new parallel data at deployment, but it is unclear whether they actually learn the translations of rare terms from those examples. We formalize this capability as in-context term learning (ICTL). We show that standard IC-Train develops this capability only weakly, and propose RareCipherFT, which strengthens it without any lexical resources. RareCipherFT pairs each training target with in-context examples that share a rare term with it. It then replaces that term with a character-shuffled cipher in both the context and the reference, so the term can only be recovered by copying from context. The ciphered fraction of training data is annealed to preserve translation quality. Across seven translation directions between English and Tamil, Assamese, Mizo, Nepali and Hausa, and four models from 1B to 7B parameters, RareCipherFT raises term recall over standard IC-Train by 5-15 absolute points without lowering COMET. Probes using synonyms, nonce words and controls for shared surface context show that these gains come from linking source terms to their in-context translations rather than from shortcuts.

---


### 137. [CADS: Measuring the Incremental Contribution of LLM Proposers in Sequential Biological Screens](https://arxiv.org/abs/2610.24597)

**<font color=#1a73e8>作者：</font>** Guanxing Chen, Nihui Shao, Haohuai He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to guide sequential biological screens, yet standard evaluations rely on raw hit counts that conflate a proposer's value with the discovery capacity of the underlying algorithmic harness. Adaptive sampling and corrupted experimental readouts also leave standard feedback comparisons without a false-discovery guarantee. We present Certified Agentic Discovery Screens (CADS), an error-controlled measurement framework that quantifies a proposer's incremental value against an identical LLM-free loop. By integrating capped likelihood-ratio bounds, e-processes, and complete-family e-BH, CADS controls the terminal false discovery rate under the stated null and corruption conditions despite arbitrary dependence, adaptive sampling, and optional stopping. In DepMap-backed simulations, CADS exposes two evaluation artifacts: the LLM-free harness alone clears the feedback gate, and raw origin counts overstate LLM contributions because LLM picks displace fallback discoveries. On the initial 20 seeds, supplying tested-candidate history to Qwen2.5-7B shifts its net contribution from +0.35, with a 95% interval covering zero, to +2.90, with the interval above zero. This initial net effect did not persist in a 50-seed matched-quota replication. These results support net gain over an LLM-free loop, measured between separately certified sets, as the appropriate measure of proposer contribution.

---


### 138. [AdamPM: Memory-Efficient LLM Optimization via Moment Pooling](https://arxiv.org/abs/2610.24598)

**<font color=#1a73e8>作者：</font>** Xiaowei Ji, Lishan Xu, Jianing An 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adam is widely used for training large language models (LLMs) owing to its strong optimization performance and training stability, but its element-wise estimation for the first and second moments incur substantial memory overhead. Although numerous memory-efficient optimizers have been proposed, many incur additional computational overhead or require additional tuning of hyperparameters. Consequently, Adam remains a dominant and reliable choice for LLM pre-training. We propose AdamPM (Adam with Pooled Moments), a simple and memory-efficient variant of Adam that groups adjacent moment entries along the row or column dimension and represents each group by a single shared mean. AdamPM can well inherit Adam's hyperparameter settings and is readily integrated into existing Adam optimizer implementations, with less memory overhead. We systematically investigate pooling of both first and second moment estimates and identify second moment pooling as the effective design. With a group size of $s$, AdamPM reduces second moment memory to $1/s$ of the original requirement. Extensive experiments on language model pretraining, fine-tuning and multimodal learning demonstrate that AdamPM maintains model performance and training speed while substantially reducing optimizer-state memory. Our code is available at \url{this https URL}.

---


### 139. [TCMScience: An Autonomous Scientist for Traditional Chinese Medicine](https://arxiv.org/abs/2610.24601)

**<font color=#1a73e8>作者：</font>** Yanlan Kang, Ruiqi Liu, Xinpei Gu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional Chinese medicine (TCM) research connects classical texts, medicinal entities, molecular assays, computational predictions, and clinical studies. An autonomous research agent must preserve the inferential boundaries between these evidence types while coordinating analysis across heterogeneous resources. We introduce TCMScience, a scientific knowledge-discovery agent that separates language-model proposals from execution and release authority. Its architecture combines a trusted kernel, a scientific compiler, and claim-support contracts: plans are compiled into typed operations, execution is bounded by explicit permissions, and candidate findings are checked against source provenance, study design, and claim scope before release. The full capability registry contains 117 public-source connectors with 444 typed operations across 29 domains and 150 native tools across 12 domains; the TCM data hub catalogs 136 databases, 76 dataset specifications, and 84,294 formula-source records. These resources support model-independent workflows through browser and local execution interfaces. In a network-pharmacology analysis of Gegen Qinlian Tang, replacing the whole-proteome background with the assayed-protein background changed the number of significant pathways from 66 to zero; incorporating inactive screening records identified nine pathways, including drug-metabolism signals retained as mechanistic hypotheses. A governance ablation over 121 constructed erroneous outputs spanning 26 classes released 121 errors without governance, 57 with the domain layer, seven with the kernel, and zero with both layers. All 10 compliant controls were retained. These results establish complementary control of known failure modes and show how explicit evidence contracts change the conclusions an agent is permitted to report.

---


### 140. [Safety Kernel: Mechanistic Alignment for Cross-Lingual Defense in LLMs](https://arxiv.org/abs/2610.24614)

**<font color=#1a73e8>作者：</font>** Chengyu Xie, Fei Shen, Shuyi Miao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The safety capabilities of large language models (LLMs) are highly uneven across different languages, often allowing cross-lingual attacks to bypass safety guardrails. Existing alignment methods predominantly rely on external alignment signals and provide limited insight into underlying neuron-level mechanisms, making it difficult to provide a unified internal target for cross-lingual safety interventions. To address this, we analyze cross-lingual safety behavior at the neuron level and identify a compact set of safety-related neurons shared across languages, termed the safety kernel (SK). Specifically, we first utilize multilingual parallel safe and unsafe prompts to compute safety contrast with activation responsiveness (SCAR) scores, identifying language-wise safety-neuron candidates from internal activation patterns. We then intersect the resulting language-wise safety-neuron sets to obtain the SK, and validate its functional relevance to cross-lingual safety behavior through activation suppression and activation-state transfer interventions. Finally, building on the SK coordinates, we introduce SK-Masked LoRA, which constrains LoRA adaptation to the feed-forward network (FFN) output dimensions corresponding to the SK, thereby focusing safety-related changes on the cross-lingually shared neuron coordinates. Extensive experiments demonstrate that SK-Masked LoRA substantially reduces attack success rates across multiple languages, including languages excluded from SK discovery, while intervening on only a small fraction of internal neuron coordinates and producing generally limited changes in the model's general capabilities.

---


### 141. [Narratives Mislead: An Empirical Study of How LLMs Misjudge CVSS Severity in Bug Bounty Reports](https://arxiv.org/abs/2610.24623)

**<font color=#1a73e8>作者：</font>** Ruitao Feng, Yuekang Li, Yao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Bug bounty platforms receive vulnerability reports faster than vendors can triage them, and Large Language Models (LLMs) are increasingly considered for assigning the Common Vulnerability Scoring System (CVSS) severity that drives prioritization. Prior evaluations score short CVE descriptions and report accuracy, but deployment depends on how models err, not only how often. CVSS gives each metric a formal meaning that departs from how researchers describe impact in narrative reports, and model rationales suggest that errors concentrate where the two diverge; we ask whether this pattern is systematic. From 4,281 publicly disclosed reports mined from Huntr and HackerOne, we build a benchmark of 240 Huntr reports with vendor-validated CVSS vectors and evaluate eight LLMs under four prompting strategies and fine-tuning, measuring errors by severity class and score and analysing sub-vectors on individual reports. The best prompting configuration reaches only 49.58% level accuracy, ten points above always predicting the majority level, and fine-tuning a 7B model raises this to at most 56.25%, an optimistic upper bound. Errors are directional: models overestimate far more often than they underestimate, and they almost never recognize low-severity vulnerabilities. We trace these errors to three semantic boundaries that the specification draws and narrative reports blur: potential versus realized impact, impact magnitude versus authorization scope, and uncertainty versus the worst case. Because the violations originate partly in the report, we close with an exploratory case study: on four reports, a boundary-aligned, exploit-free report structure lowered a frontier model's score where the narrative invited an unclaimed account takeover, but left the metrics a report does not settle open, and the two published labels disagreed on three of the four reports.

---


### 142. [Uncovering Semantic Hierarchies in Text-Attributed Graphs via Variational EM-based LLM-GNN Synergy](https://arxiv.org/abs/2610.24624)

**<font color=#1a73e8>作者：</font>** Yunhui Liu, Xudong Jin, Qizhuo Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While hierarchical structures are intrinsic to organizing human knowledge, current representation learning on text-attributed graphs predominantly operates on flat semantic spaces, overlooking the rich coarse-to-fine granularity inherent in real-world data. To bridge this gap, we propose SHiFT, which synergizes the reasoning power of LLMs with the structural representation capability of GNNs within an Expectation-Maximization (EM) paradigm. In the E-step, we harness LLMs as expert taxonomists to induce an explicit semantic tree, introducing a lightweight Mapping & Diagnosis strategy that reduces inference costs by surgically updating the hierarchy only when anomalies are detected. In the M-step, we align the GNN encoder with this induced hierarchy from complementary perspectives, including clustering partition, topological skeleton, and semantic concepts. Theoretical analysis interprets SHiFT as a generalized Variational EM algorithm. Extensive experiments demonstrate that SHiFT not only achieves state-of-the-art performance but also uncovers high-quality, human-readable taxonomies. Our code can be found at this https URL.

---


### 143. [Muse Glimmer 30B: An On-Device Agentic Model](https://arxiv.org/abs/2610.24628)

**<font color=#1a73e8>作者：</font>** Arash Ebrahim Abtahizadeh, Muna Aghamelu, Adil Ahmed 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Muse Glimmer, an open-source 30B parameter causal language model with perception encoder, purpose-built for autonomous agentic tasks on consumer hardware. Muse Glimmer integrates multi-step reasoning, reliable tool use and failure recovery into a single model that runs locally on consumer devices without requiring cloud infrastructure. The model accepts text and image inputs and produces text outputs, was trained on data from over a hundred languages, and is quantized to approximately 4-bit precision for efficient single-GPU inference. Muse Glimmer achieves state-of-the-art performance for its size class on agentic benchmarks, setting a new standard compared to the models of its size: Gemma4-31B and Qwen3.6-27B on tool use, multi-step planning, and agentic task completion. We release the model under the Apache 2.0 license to foster open-source development of capable, safe, local AI agents.

---


### 144. [Selm: Self-Evolving Library Management for Multi-Skill Agent Optimization](https://arxiv.org/abs/2610.24630)

**<font color=#1a73e8>作者：</font>** Mengxi Hu, Yuxuan Hu, Jinbo Su 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly use skills as a lightweight way to acquire task-specific knowledge. Recent work enables skills to evolve from task trajectories. However, these methods often lack systematic management of evolved skills, making it difficult for agents to reuse and accumulate skills across domains, thus limiting performance on subsequent this http URL reliably accumulate, reuse, and maintain useful skills across tasks, we present SELM (Self-Evolving Library Management), a framework that formulates skill evolution as library-level management. SELM jointly manages skill retrieval, updating, and lifecycle by maintaining skill confidence and utility signals. It introduces utility-aware retrieval to select useful skills, a Map-Reduce framework to generate targeted updates from task-specific experience, and lifecycle controls to retain or remove skills based on their effectiveness. These mechanisms enable the skill library to continuously accumulate useful experience while preserving and pruning skills across tasks, improving agent performance on complex tasks across diverse domains. We evaluate SELM on four agent benchmarks covering diverse tasks and execution environments, and SELM consistently outperforms in most settings.

---


### 145. [EdgeKernelBench: Unified LLM-Driven Kernel Generation for Edge Backends](https://arxiv.org/abs/2610.24648)

**<font color=#1a73e8>作者：</font>** Yuhua Zheng, Xueyi Chen, Xinze Zou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent works show that LLMs can generate kernels with strong performance on server GPUs. Edge deployment presents distinct challenges because the hardware is heterogeneous, the software stacks are fragmented, and the resource budgets are tight. LLM kernel generation across diverse edge backends has yet to be studied systematically. We introduce EdgeKernelBench, which combines a unified IR deployment framework with a hierarchical benchmark for edge workloads. The unified IR captures reusable computation, scheduling, and memory decisions and connects to each target backend through a compiler interface. The benchmark spans progressively larger program scopes, from individual operators to compact model graphs, across representative edge application domains. We instantiate the design with TVM as a reference compiler and validate it across heterogeneous edge backends. With a single generation attempt, the best model achieves 64.5% Correct@1 but only 25.5% Fast@1.0. This gap shows that functional correctness does not consistently translate into performance gains. We therefore introduce the Layered Edge Kernel Agent (LEKA), which organizes optimization through a layered IR. On the agent evaluation subset, LEKA achieves 43.5% Fast@1.0, compared with 13.0% for direct generation and 26.1% for Claude Code. LEKA and Claude Code use the same base model and optimization budget. Together, EdgeKernelBench and LEKA support unified evaluation and layered optimization of kernels generated by LLMs across edge backends.

---


### 146. [Good Judgment, Bad Advice: Decision-Model Controllers Raise Agent Cost Without Improving Success](https://arxiv.org/abs/2610.24649)

**<font color=#1a73e8>作者：</font>** Naman Vats  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent scaffolds increasingly delegate small decisions (whether to stop, verify, or change approach) to cheaper models. We ask whether a typed decision model, Jev 1.13, consulted only at deterministic decision points, makes a Claude Sonnet 5.5 terminal agent cheaper without making it worse. In a pre-specified study on Terminal-Bench 2.1, we hold one agent loop fixed and vary only the controller: none, deterministic rules, a small LLM (Claude Haiku 5.5) answering the same questions, Jev, and a placebo that samples Jev's development-phase choice frequencies at the same moments. On 21 held-out tasks (315 trials), Jev raised cost per attempt by 19% (geometric-mean ratio 1.19, 95% CI 1.02-1.36) at an identical pass rate (73.0% vs. 73.0%). Jev was cheaper than the small-LLM controller (ratio 0.81) but 22% more expensive than the placebo, and no pass-rate difference between arms was detectable. Offline, Jev ranked finish requests better than the alternatives (AUROC 0.78 vs. 0.62 for rules and 0.60 for the small LLM) but was poorly calibrated: its mean probability that a run was complete was 0.50 when 87% of those runs passed, so it asked the agent to verify work that was already correct. No controller ever chose to abandon a run. Informative decision signals did not become useful interventions; we discuss what that would require.

---


### 147. [Can AI agents make law? Evaluating AI legal relevance and creativity](https://arxiv.org/abs/2610.24661)

**<font color=#1a73e8>作者：</font>** Benjamin Ricaud, Artem Galushko  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models, the artificial intelligence (AI) systems behind modern chatbots, are trained on vast amounts of legal text, but can they build on it to write law for situations that text never anticipated? In this study, we analyse AI agents' ability to draft a hypothetical "Constitution" for a "community of AI agents". We design "constitutional assemblies" in which a single language model plays several characters that debate to produce a draft constitution. We find that the assemblies converge on a robust floor of legal provisions, and generate a wide variety of different proposals around it, including several AI-specific provisions with no equivalent in human law. Looking more closely at the "creativity" of these AI agents, we find different levels: most proposals combine existing concepts and themes from human constitutions with AI-specific vocabulary. We introduce a measure of this recombination, which helps identify and highlight the most novel legal material. This study reveals a ceiling on AI creativity: the agents extend familiar legal ideas to new situations, but they do not work through what those situations would change. Although current AI models can help develop new laws, they still depend on human legal reasoning.

---


### 148. [What RL Brings to Reasoning: A Few Decisions the Base Model Would Not Make](https://arxiv.org/abs/2610.24663)

**<font color=#1a73e8>作者：</font>** Siyu Zhang, Yuquan Lu, Yoshua Y. Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) substantially improves mathematical reasoning, but what it adds to the base model remains unclear. We investigate this through a sequence of generation-time interventions on Qwen3-4B-Base, measuring how much of its RL-trained counterpart's gain each intervention recovers on 120 AIME problems. Power sampling with the same 8,192-token output limit brings no gain beyond greedy decoding. Yet borrowing the RL model's token only where the two models' greedy choices differ, roughly 4% of generated positions, recovers 90.5% of the pass@1 gain, with similar recovery across three model pairs on MATH-500. We find that even a single opening token has a substantial effect: forcing the base model to begin with "Alright" recovers 35% of the RL gain. The opening alone is insufficient, however. Later replacements after the same opening add another 5.2 percentage points to pass@1, and the fixed rules we test for inserting reflective words such as "Wait" do not reproduce this benefit. Sparse replacement also retains much of the base model's diversity while staying close to the RL model at pass@1. At k=256, it solves 67.5% of the problems, significantly more than the RL model (61.4%) and a mixture of whole responses matched in pass@1 (61.45%). The comparison is at equal attempt counts rather than equal compute, since rl-replace consults both models at every decoding step. These results show that the opening can recover a meaningful part of the RL gain, but a larger contribution comes from later choices, which can be borrowed while retaining much of the base model's diversity. Code is available at this https URL.

---


### 149. [From Views to Worlds: Active Exploration over 3D Worlds for Vision-Language Models](https://arxiv.org/abs/2610.24676)

**<font color=#1a73e8>作者：</font>** Qijian Tian, Jiayu Ying, Ke Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have achieved remarkable progress in 2D visual understanding tasks, yet the passive view-centric perception paradigm limits their capacity for 3D spatial reasoning. Such reasoning often requires actively acquiring spatial evidence beyond the currently visible views, such as camera poses and cross-view spatial relationships, to infer 3D relationships that are not explicitly represented in 2D images. However, existing methods either lack active exploration or merely provide additional views during inference, without explicitly acquiring such spatial evidence beyond 2D images. In this paper, we propose View-to-World (V2W), an active exploration framework that enables VLMs to actively explore 3D worlds and lifts VLMs from passive view-centric perception to active world-centric spatial reasoning. Given a spatial reasoning task with multi-view images, V2W first reconstructs an explicit 3D world with geometry, camera poses, and language-grounded semantics, and exposes it to VLMs through visual and linguistic interfaces. Through multi-turn interaction with these interfaces, VLMs iteratively acquire spatial evidence from the constructed 3D world, enabling active world-centric spatial reasoning. V2W can be integrated with existing VLMs in a training-free manner and can be further enhanced by optimizing the exploration policy via reinforcement learning. Experiments on spatial mental modeling benchmarks demonstrate that V2W substantially improves VLM baselines in the training-free setting and achieves state-of-the-art performance with the learned exploration policy, highlighting the importance of active exploration for spatial intelligence. Project page: \url{this https URL}.

---


### 150. [Verifying Human-Written Reasoning References](https://arxiv.org/abs/2610.24690)

**<font color=#1a73e8>作者：</font>** Ali Ansari, Farhana Ferdousi Liza  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating the reasoning of AI systems often relies on human-written reasoning chains as references, yet the logical support for their individual steps is rarely verified. Although prior neuro-symbolic approaches have formalized and checked reasoning, their reported evaluations do not systematically assess whether step conclusions in human-written reference derivations are entailed by their cited premise sets or investigate the sources of failures in those references. To address these limitations, we present a novel reference-centred assessment method for human-written derivations that combines entailment checking against cited premise sets, full-premise rechecking, and failure attribution to examine the reliability of these derivations and their formal representations. We evaluate it on P-FOLIO, using a large language model (LLM) to translate step conclusions into first-order logic (FOL) and the Z3 SMT solver to check entailment. Of 386 derivations examined, 202 (52.3%) meet all our checking criteria, meaning that every translated step is entailed by its stated support and the required target is established under the available FOL representations. Among 230 steps not entailed by their stated support, 191 become entailed when checked against the complete original premises, indicating that most initial failures reflect incomplete or mismatched support rather than unsupported claims. Manual analysis of the remaining 39 cases identifies 21 human reasoning errors, 11 FOL translation errors, and 7 dataset annotation errors. A separate manual audit of 50 randomly sampled steps that passed the entailment checks found 46 faithful FOL translations (92%). These findings suggest that disagreement with a human-written reasoning reference may originate in the reference or its formal representation rather than in the AI system being evaluated.

---


> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-548](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
