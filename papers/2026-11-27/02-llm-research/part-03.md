# 🧠 大模型相关研究 | 2026年11月27日

> 本类共 **267** 篇论文：已确认 **249** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-267](./part-06.md)

---

### 101. [RadOncGym: An Agent-Based Framework for Radiotherapy Dose-Mimicking Optimization](https://arxiv.org/abs/2611.33821)

**<font color=#1a73e8>作者：</font>** Tong Miao, Shupeng Cheng, Xiwen Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI dose-prediction models generate patient-specific 3D dose distributions from patient anatomy, providing an important intermediate representation for automated radiotherapy planning. However, an AI-predicted dose must undergo downstream optimization to produce a physically constrained treatment plan, a process that requires balancing competing planning objectives. We present RadOncGym, an agent-based framework that enables an LLM agent to iteratively tune 12 planning-objective weights for dose-mimicking optimization. To reduce iterative evaluation cost, RadOncGym incorporates a surrogate verifier that provides rapid feedback while allowing the agent to decide when to request a full planning solve within a fixed solve budget. We evaluate RadOncGym on 60 OpenKBP head-and-neck patients, each paired with 10 predictions from OpenKBP-Opt dose-prediction sets, yielding 600 patient-prediction contexts per experimental configuration. Under RadOncGym's 16-turn setting with a three-solve budget, a GPT-5.6 Sol agent reduces mean clinical-criterion violation by 0.6131 Gy and improves DVH and dose scores by 0.5986 and 0.2204 Gy relative to leaving all 12 weights fixed at 1, outperforming all evaluated non-agent weight-tuning methods under the same solve budget. It remains competitive with the 16-solve variants of these methods while requiring 75.0-77.6% less normalized runtime. RadOncGym demonstrates the potential of LLM agents as optimization planners in downstream radiotherapy plan optimization and provides a public testbed for their systematic evaluation. Code and configurations are available at this https URL.

---


### 102. [MetaDecomp: Adaptive Task Decomposition via Meta-Learned Procedural Memory](https://arxiv.org/abs/2611.33822)

**<font color=#1a73e8>作者：</font>** Ziyi Wang, Yixiao He, Yichen Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reusing past experience in long-horizon tasks requires more than storing successful procedures: Language agents must distinguish which procedures apply and what work remains as execution progresses. We introduce MetaDecomp, an in-context meta-learning framework for adaptive task decomposition that jointly learns a task-relative state space and reusable procedures. Its outer loop builds procedural memory from successful training executions, representing task progress as abstract states and procedures between states as directed acyclic graphs of operations and dependencies. As new progress distinctions are learned, MetaDecomp revisits historical execution evidence to reassess state assignments and reorganize the procedures they support. With memory fixed at test time, the inner loop refines an initial decomposition and revises it from environmental feedback, combining applicable procedure fragments with task-specific steps missing from memory. Evaluated on ALFWorld and ScienceWorld over three seeds, MetaDecomp achieves the highest mean performance among the compared methods in four of five settings, for example, an 86.3% success rate on ALFWorld with Qwen3-4B. Fixing the initial schema or omitting historical reprojection reduces performance in component ablations. MetaDecomp also uses fewer inference tokens than ReAct and AutoRefine in all five settings. Cross-benchmark analysis identifies a low-performance area where partial coverage degrades success relative to hidden memory; high coverage improves success, while low coverage changes little. Code will be released upon acceptance.

---


### 103. [Pitfalls of Dependency-Ready Decoding for Masked Diffusion Language Models](https://arxiv.org/abs/2611.33823)

**<font color=#1a73e8>作者：</font>** Lina Berrayana, Christopher Malon, Yoichi Ishibashi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked diffusion models (MDMs) have shown strong performance on structured reasoning tasks such as Sudoku, Trip Planning, and Countdown. MDMs introduce a freedom in the order in which tokens may be unmasked, and to exercise this freedom for good accuracy, early decoding strategies relied on signals of confidence or the downstream impact of decoding a token. However, simple examples seem to illustrate that resolving a token's dependencies before unmasking it should be important. Therefore, we examine whether this principle, which we call dependency-ready decoding, would contribute to better accuracy, from a practical and a theoretical perspective. We examine a recent decoder that implements dependency-readiness through attention, and generally find that when it performs better than confidence-based or future utility baselines, its decoding order collapses to left-to-right decoding. For theoretical analysis, we establish a definition of dependency without resorting to attention, measured by an information-theoretic score of how much revealing a single masked token (or a set) would shift the model's prediction for another. We prove that when the margin is large relative to this score, no such revelation can change the top prediction, so in this regime Maximum-Margin decoding already commits dependency-ready tokens. These findings leave only a narrow scope for future dependency-ready decoders: their potential benefit is limited to positions with margins smaller than the information-theoretic sensitivity, and reliance on attention should be questioned.

---


### 104. [FEAST: Fair and Efficient Adaptive Sampling for Task-Free On-Policy Learning](https://arxiv.org/abs/2611.33827)

**<font color=#1a73e8>作者：</font>** Yongxi Zhu, Ziyi Wang, Yichen Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language agents trained from self-generated experience must allocate a limited rollout budget across heterogeneous capabilities. A common strategy is to prioritize capabilities with strong current learning signals, but in on-policy learning these signals are endogenous: past allocation changes the policy and therefore the evidence available for future allocation. This can create a feedback loop in which under-trained capabilities receive increasingly fewer opportunities to improve. We formalize this effect through the Quota-Efficiency Law (QEL), which shows that allocation history can change learning efficiency even under matched capability-specific exposure. Motivated by this, we introduce FEAST, a task-free adaptive sampling framework that separates opportunity allocation from compute allocation. FEAST dynamically discovers capability clusters while preserving their learning histories, maintains continued sampling opportunities across clusters, and reserves a rollout budget for each selected cluster. Within each budget, it progressively concentrates computation on prompts with informative reward variation. Across GURU-18K and SMC, FEAST improves average performance over competitive adaptive sampling baselines under matched rollout budgets, while better preserving learning progress on weaker capabilities. Ablation studies further support the complementary roles of cross-cluster opportunity protection and within-cluster selective allocation. Code will be released upon acceptance.

---


### 105. [3D CoCa v3: Contrastive Learners with Scene Graphs for Urban Scene Understanding](https://arxiv.org/abs/2611.33835)

**<font color=#1a73e8>作者：</font>** Nannan Zhang, Ting Huang, Zeyu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding large-scale 3D urban scenes requires representations that capture both multi-scale geometric structures and complex spatial relationships. However, existing 3D vision-language methods primarily emphasize global semantic alignment or object-level representations, leaving structured relational modeling underexplored within unified contrastive and generative frameworks. In this paper, we present 3D CoCa v3, a scene-graph-enhanced contrastive and generative framework for urban 3D scene understanding. Our framework features a Pyramid Vision Encoder for multi-scale geometric representation learning and a language-model-based decoder with question-guided caption retrieval and visual cross-attention. We further introduce MSG-based relational descriptions to enrich contrastive 3D-language alignment with structured spatial relationships. To support semantic and relational supervision, we construct City3D-9.6K, a multi-view urban vision-language dataset with aligned visual-geometric observations, scene captions, and scene graphs. Extensive experiments on City-3DQA demonstrate that 3D CoCa v3 achieves 88.35% and 64.79% overall top-1 accuracy on the sentence-wise and city-wise splits, surpassing 3D CoCa v2 by 20.88 and 3.57 percentage points, respectively. Furthermore, 3D CoCa v3 achieves the best performance on GeoEval3D, demonstrating its effectiveness in urban spatial reasoning and geometric understanding. Code is available at this https URL.

---


### 106. [Can Its Own Misses Teach an MLLM to Find Small Brain Metastases?](https://arxiv.org/abs/2611.33836)

**<font color=#1a73e8>作者：</font>** Yixuan Duan, Kexin Geng, Hanwen Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are becoming general readers of medical images, yet they remain weak at locating small abnormalities. Brain metastases expose this gap: at 384 px a 0.1 mL lesion covers less than a quarter of one visual token, and at one false positive per scan frontier MLLMs find fewer than 30% of lesions of 0.1-1 mL. Fine-tuning on one dataset helps but transfers poorly, and improving it further is slow trial and error steered by a single score. We introduce LANTERN (Lesion-finding AgeNt Through Error-driven Recursive learNing), a framework in which an MLLM improves recursively from its own misses. LANTERN recasts model development as an error-driven loop: a failure census attributes every missed lesion to one of four causes, an LLM mentor revises one of four levels (evidence acquisition, visual representation, learning policy, decision aggregation) per round, and a rule frozen before the first round decides what is kept, without test data and with every tool call audited. Over 15 unattended rounds, LANTERN raises a fine-tuned 4B MLLM from finding 75% to 94% of lesions at one false positive per scan on BraTS-MET, and 91% of those of 0.1-1 mL, compared with at most 51% and 29% for five frontier MLLMs read under the starting protocol; the gains hold on an external cohort (89%) and on unseen meningiomas (77%). These results show that an MLLM's own misses, attributed to their causes, can drive its reliable recursive self-improvement.

---


### 107. [The Missing Root: Geometric Imagination Without Images in Large Language Models](https://arxiv.org/abs/2611.33841)

**<font color=#1a73e8>作者：</font>** Loïc Magnan, Tomasz Kozlowski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes a new paradigm and method for giving large language models spatial understanding. Standard language models operate exclusively over discrete words (secondary representations of things rather than continuous space itself), forcing them to guess geometry verbally. Whereas most multimodal approaches equate spatial grounding with camera images or video frames, spatial structure itself is not a picture: it consists of coordinate frames, solid boundaries, and how objects move and relate to each other in continuous space. Motivated by this distinction, we place continuous object tokens combining pose (position, orientation, and scale) and signed-distance shape embeddings alongside word tokens inside a single uninterrupted transformer sequence, allowing language and geometry to attend to each other as object scenes are built and updated step by step. Control tokens switch output automatically between natural-language words and continuous object state updates to a persistent object workspace, while an attention mask blocks earlier prose when generating the answer, so responses must be read directly from settled geometry. To prove this method works, we attach a narrow parallel spatial stream (+4.4% weights) alongside unfrozen Qwen3-1.7B layers. In our two-dimensional tests, the model spawns and transforms multi-object scenes from English descriptions, transfers shapes to held-out nouns, and relies causally on the workspace to answer spatial questions.

---


### 108. [SPiXSeg: Rethinking MLLM-based Image Segmentation as Superpixel Classification](https://arxiv.org/abs/2611.33842)

**<font color=#1a73e8>作者：</font>** Piyush Tiwary, Sohini Dutta, Prathosh A.P  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are widely used for image segmentation. However, existing methods either use a decoder or use patch-based approach which trades boundary precision against the number of decisions as coarse grid cells mix foreground and background pixels, while finer grids require many more predictions, and autoregressive mask generation adds sequential decoding overhead. We propose SPiXSeg, which shifts the output from per-patch to per-superpixel label assignment, using superpixel tokens formed by aggregating patch-level visual features. An off-the-shelf model partitions each image into task-agnostic superpixels, so the partition is computed once and reused across tasks. A Spix-to-Mask (S2M) module scores each superpixel token in a single MLLM forward pass by directly comparing the MLLM's hidden representations, without autoregressive generation or a separate scoring network, and the selected superpixels are mapped directly to pixels without refinement. Without any trainable decoder head or post-hoc refinement, SPiXSeg achieves an average cIoU of 80.5 with LLaVA-1.5-7B and 81.9 with InternVL2.5-8B on RefCOCO, RefCOCO+ and RefCOCOg and, when trained only on COCO-Stuff, extends to open-vocabulary semantic segmentation with mIoU of 29.0, 59.5 and 95.4 on ADE20K, PASCAL Context and PASCAL VOC, outperforming several SoTA MLLM baselines. Our results suggest that a fixed, query-agnostic superpixel partition is enough for accurate language-guided segmentation.

---


### 109. [When Rerankers Work Together: Better and Faster Reranking without Joint Training](https://arxiv.org/abs/2611.33844)

**<font color=#1a73e8>作者：</font>** Yanqiao Chen, Dongsheng Hou, Yuhan Rui  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standalone reranker quality does not determine its value in a multistage RAG pipeline. We systematically study heterogeneous rerankers composed without joint training, spanning lexical, single-vector, late-interaction, and joint query-context scoring. Two lightweight semantic coarse scorers, Cache-Pointwise and Cache-Shapley, learn from passage relevance labels and share cacheable representations and linear-time singleton inference. Under matched candidates and budgets, we compare cascades with stage-removal references to measure evidence retention, repair and breakage, reader accuracy, and online pruning cost. On NoLiMa 32K with Gemma, inserting these scorers before CrossEncoder or Provence improves answer accuracy by 4.02-9.43 percentage points while accelerating online pruning by 1.57-1.88x relative to the corresponding reranker alone. Cache-Pointwise composed with ColBERTv2 through reciprocal rank fusion improves accuracy by 4.60 points at 1.36x speedup over direct ColBERTv2. The stage-removal comparisons reveal an asymmetry: a cascade can outperform its final reranker alone while underperforming its coarse selector alone. Two readers, a second multi-hop dataset, and three-stage extensions show that the gains depend on the reader, reranker pairing, and stage configuration. These findings demonstrate a practical route to better and faster reranking without joint training and motivate studying stage order, candidate budgets, and rank fusion as determinants of composition quality.

---


### 110. [ChemDeduce: Benchmarking LLMs for Unknown Chemical Identification through Interactive Simulated Experiments](https://arxiv.org/abs/2611.33848)

**<font color=#1a73e8>作者：</font>** Hengyi Cai, Yuqi Tang, Zichang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong performance in chemical knowledge and reasoning, yet it remains unclear whether they can solve problems whose answers must be discovered through experimentation. We investigate this question through Unknown Chemical Identification, where a model must actively design experiments, interpret observations, update hypotheses, and ultimately identify a hidden substance. We introduce ChemDeduce, an interactive evaluation framework for assessing LLMs through simulated experiments. ChemDeduce formulates chemical identification as a sequential decision process and provides a stateful simulated laboratory with explicit instrument and operational constraints, enabling scalable and reproducible evaluation of iterative experimental reasoning. We benchmark eight frontier LLMs on 200 chemicals, yielding 1600 model--target pairs and 4800 episodes over three independent repetitions, and evaluate identification accuracy, operational compliance, interaction efficiency, and trajectory-level reasoning quality. Despite generating seemingly plausible experimental plans, current models achieve an average identification accuracy ranging from 23.83% to 67.33%, revealing substantial limitations in experiment selection, evidence interpretation, and sequential hypothesis refinement.

---


### 111. [OmniMeld: Enhancing Audio-Visual Understanding via Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2611.33861)

**<font color=#1a73e8>作者：</font>** Daili Hua, Yifan Dai, Bohan Zeng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual understanding requires perceptual grounding, temporal understanding, and semantic inference. Multi-teacher distillation can consolidate these capabilities, but direct probability matching does not explicitly capture teacher prediction changes across audio-visual conditions. We introduce OmniMeld, a multi-teacher on-policy distillation method that integrates domain expertise through modality-response-guided distribution matching. We train four teachers covering grounding and correspondence, temporal dynamics and event structure, causal and inferential reasoning, and contextual and holistic understanding. Each sample is routed to its corresponding teacher for supervision conditioned on student-generated answer prefixes. We derive transport costs from teacher prediction changes over shared candidate tokens across audio-visual conditions, using optimal transport to match student predictions to those of the teacher under complete audio-visual input. We also construct OmniMeld-20K for domain-specialized teacher training. The dataset spans four capability domains, with responses structured into evidence, reasoning, and answer sections and verified through consistency checks and media-based review. Experiments on audio-visual and general video understanding benchmarks demonstrate competitive teacher performance among similarly sized open-source models. The student improves over its base model across all evaluated benchmarks and surpasses the teachers' base model on several benchmarks.

---


### 112. [Contextual language representations link narrative processing to language and literacy in children](https://arxiv.org/abs/2611.33871)

**<font color=#1a73e8>作者：</font>** Dongyi He, Tian Jiang, Nizhuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spoken narratives extensively connect moment-to-moment language processing with knowledge accumulated through language and literacy experience. This study examined that relationship using functional magnetic resonance imaging (fMRI) during Cantonese story listening and contextual representations from large language model (LLM). The imaging cohort comprised 23 school-age children; 16 contributed complete standardized literacy and language assessments and served as held-out participants in a nested cross-subject encoding analysis of the same story. Contextual embeddings predicted distributed narrative responses, with prominent correspondence in temporoparietal and default-network parcels. Regional summaries of the top 25% of voxels ranked by held-out correlation yielded atlas-wide means of r=0.174 and partial R2=0.0165. A joint feature model identified negative surprisal and positive predictive-entropy coefficients across cortical and subcortical parcels, including control, salience, hippocampal and amygdalar regions. Higher word-dictation and overall literacy scores were associated with lower regional encoding performance. Higher Cantonese grammar scores were associated with more negative semantic-update coefficients in parietal control, somatomotor and dorsal-attention parcels. Together, these findings connect language and literacy skills to the regional strength and direction of neural coupling with narrative context. They position naturalistic context processing as a possibly measurable link between oral comprehension and literacy in childhood.

---


### 113. [Off the Driven Path: Transferable Road Understanding in Driving VLAs](https://arxiv.org/abs/2611.33878)

**<font color=#1a73e8>作者：</font>** Lena Wild, Christian Helten, Katie Z Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end driving policies increasingly operate without explicit HD maps at inference, raising the question of what road knowledge they actually internalize. To probe this knowledge through model outputs, we introduce Road-KSU, a framework that automatically converts HD maps and actor annotations into a road-centric scene graph. From this, we derive road-focused question answering and reasoning targets, complemented by map-based trajectory compliance metrics. Pairing Road-KSU with geographically disjoint splits yields a $2 \times 2$ evaluation crossing output modality (language vs. action) with place familiarity (seen vs. unseen roads). On NAVSIM, 95% of test samples lie within 10m of a training sample, and scores of 13 published planners on turns rise steeply with the number of training drives through the test location, pointing to memorized road geometry. Retraining on geographically disjoint splits and probing with Road-KSU confirm that action-space performance degrades most on unfamiliar turns, with failures dominated by geometric compliance. Language accuracy, however, drops on road-centric VQA on straight and curved roads alike, and remains stable on dynamic scene content. Scaling the training data further reveals a double dissociation: more drives through the same places improve driving on unseen roads but leave road question answering unchanged, whereas spreading a fixed data budget over more places increases road question answering with little change in driving performance. These findings show that improved driving scores need not imply broader road understanding on unseen roads, and identify geographic diversity as key to transferable road knowledge.

---


### 114. [FORK: Co-Evolving Safe Disclosure and Decision Skills Against Attackers Who Read Every Refusal](https://arxiv.org/abs/2611.33879)

**<font color=#1a73e8>作者：</font>** Hieu Man, Chao Shang, Rui Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a guardrail rejects an LLM agent's action, its message reaches any attacker observing the trajectory: a fixed refusal leaves benign users unable to recover, whereas an explanation can tell the attacker what to try next. We study this as safe disclosure: explaining rejections so that authorized tasks recover without increasing adaptive attack success. Safe disclosure depends on both the decision and the message: what the guardrail blocks and what it reveals to the agent and the attacker. Because hand-written rules alone cannot anticipate how adaptive attackers probe decisions or use messages, we introduce FORK, which co-evolves a guardrail's natural-language decision and disclosure skills with an attacker that reads every public message. Each exploited message and permissive decision gives FORK evidence for a gradient-free revision of its natural-language skill library. We evaluate FORK on four benchmarks. Averaged over three agents on FORK-World, FORK cuts attack success rate (ASR) under adaptive attack from 78.4% to 14.1% and keeps utility above 85%, outperforming baselines on both ASR and utility. Notably, on MT-AgentRisk, whose environments and tasks are unseen in training, FORK lowers ASR from 70.6% to 9.1% with 93.1% benign utility.

---


### 115. [The Gradient Difference Induced by Detaching the Denominator in QK Normalization](https://arxiv.org/abs/2611.33887)

**<font color=#1a73e8>作者：</font>** Yuanqi Zhang, Haocheng Wang, Congping Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> QK normalization divides each query and key by its own RMS norm before the attention scores are computed. Treating this denominator as a constant during backpropagation leaves the forward pass unchanged but alters the parameter gradients. We derive a closed form for the difference between the gradient under this detached rule and the gradient under the standard rule. For a single token, this difference is parallel to the token's own query; it changes only the query norm and has no first-order effect after normalization. The queries, however, are computed by a projection matrix $W_Q$ shared across all tokens. The gradient difference on $W_Q$ therefore equals $W_Q$ right-multiplied by a weighted second moment of the inputs, and it decomposes exactly into three components: a radial component that changes only the norm of $W_Q$, a tangential component that changes the query directions of other tokens, and an upstream component that changes the gradient passed to earlier layers. Under AdamW, the radial component drives $W_Q$ to a larger equilibrium norm and reduces its angular update per step. Paired experiments on a small Transformer language model are consistent with this analysis. Detaching the query denominator consistently raises the test loss, and the gap persists across hardware, evaluation datasets and learning rates. All three components remain non-negligible throughout training, with the tangential component the largest. Norm growth and the smaller angular update appear only on the detached projection matrix, while the other projection matrix is essentially unchanged. With a learnable scale, however, we observe no resolvable loss gap.

---


### 116. [When Are Parallel Subagents Effective for Coding? An Empirical Study on Repository Construction](https://arxiv.org/abs/2611.33893)

**<font color=#1a73e8>作者：</font>** Zhiheng Lyu, Chengyu Yin, Lingming Zhang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM-based coding agents are increasingly used for long-horizon tasks such as building an entire program from a specification. Products like Codex and Claude Code let an agent delegate work to parallel subagents, multiplying run cost, yet it remains unclear whether and when delegation produces a better program. We compare a single agent with a main agent delegating to subagents on repository-construction tasks from NL2Repo and ProgramBench (which also provides an executable reference program). We compare scores at equal time and equal cost, run intervention experiments, and analyze fine-grained behavior. On randomly drawn tasks, parallel subagents raise hidden-test pass rates by only about 1 to 5 percentage points at up to 3.8x the cost of a single agent. Their gain is larger on hard tasks, where we find evidence of three mechanisms. Self-checking: with GPT-5.6 Sol, one sentence telling a single agent to probe the reference program first recovers most of this gain at a fraction of the cost; from GPT-5.6 Sol to GPT-6.1 Sol, the gain shrinks as single agents check their own work more. Fresh context: in extended runs, a single agent that periodically starts a new session with an empty conversation makes faster early progress in every comparison than one that resumes its conversation. Modularity: multi-agent runs produce more modular code (more files and shorter functions), closer to the upstream source. We observe similar patterns in a smaller replication with Opus 5.5 on Claude Code. Overall, subagents help when (i) a single agent stops checking too early, (ii) a long session keeps editing with little improvement, or (iii) modular code helps on the task; otherwise, they mainly add cost.

---


### 117. [Looped Models are Fast Multi-Token Predictors](https://arxiv.org/abs/2611.33896)

**<font color=#1a73e8>作者：</font>** Ayhan Suleymanzade, Sean McLeish, Sehoon Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped language models can adapt computation for predicting a token without a proportional rescaling in unique model parameters by adjusting the number of loops. This property has been used for self-speculative decoding, taking shallow loops as fast drafters and deep loops as verifiers, which is effective since drafting still uses full parameters. In this paper, we show that shallow loops can be also predictive of several future tokens and leverage this to drastically accelerate the inference of looped language models. To that end, we present Floodgates, a simple self-speculative decoding method that appends a block of mask tokens as a suffix and learns via low-rank adaptation to draft these tokens in parallel. Across seven models, five benchmarks, a range of batch sizes, and both greedy and sampled decoding, Floodgates is the fastest lossless decoding method in most cases, attaining up to 7.5x acceleration. Through analysis, we show that this speedup is enabled by all-depth training of looped models, with the shallow drafter's ability to leverage full-depth computation by conditioning on deep prefix cache evaluated during verification.

---


### 118. [EATS: Scaling Tool-Use Experience for Medical Reasoning Agents](https://arxiv.org/abs/2611.33897)

**<font color=#1a73e8>作者：</font>** Mingyuan Li, Tong Jia, Haoran Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical reasoning agents combine large language model (LLM) reasoning with clinical workflows and specialized neural tools. However, general-purpose LLMs receive limited training exposure to domain-specific medical tools, and the uncertainty and distributional shifts of neural tool outputs make selecting tools from simple descriptions significantly more challenging than in deterministic settings such as calculators or dictionary lookups. In this paper, we propose EATS, an experience-augmented tool selection strategy that leverages accumulated tool-use trajectories to improve tool selection in medical reasoning agents. EATS constructs a memory of past interactions, including queries, tool choices, arguments, and self-evaluated feedback, and retrieves relevant experiences to guide tool selection for new queries. As memory construction does not require ground-truth supervision, EATS scales naturally with test-time experience. We evaluate EATS on tool-augmented medical reasoning tasks, including closed-ended visual question answering and free-form report generation. Experiments on four public datasets, ChestAgentBench, CheXbench, MIMIC-CXR, and SLAKE-VQA, across three multimodal LLMs, Qwen3-VL 2B, Qwen3-VL 32B, and GPT-5.5, show consistent gains in tool selection behavior and downstream medical reasoning performance. Code is available at this https URL.

---


### 119. [DiCALM: Converting Autoregressive Convolution-Attention Language Models into Discrete Diffusion Language Models](https://arxiv.org/abs/2611.33919)

**<font color=#1a73e8>作者：</font>** Phong Le, Ngoc-Quan Pham, Dat Quoc Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing methods for adapting autoregressive (AR) language models to diffusion generation focus mainly on full-attention architectures. More efficient hybrid architectures remain underexplored. We introduce DiCALM, a recipe for converting the hybrid convolution-attention models of the LFM2 family (LFM2 and LFM2.5) from AR to masked-diffusion generation. DiCALM progressively extends LFM2's causal gated convolution so that it captures local context in both directions. It combines this extension with a masking warm-up and joint AR--diffusion training. In controlled experiments, DiCALM performs comparably to the corresponding fine-tuned LFM2.5-based AR models and delivers consistent speedups over them at both the 350M and 1.2B scales: over 1.4x on average and up to 1.79x.

---


### 120. [Towards 360$^\circ$ Embodied UAV Tracking Without Turning](https://arxiv.org/abs/2611.33934)

**<font color=#1a73e8>作者：</font>** Bingyu Li, Wu Du, Zhiyuan Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional embodied UAV tracking couples target observability with heading control because targets may leave the field of view of forward-facing cameras. We investigate a complementary paradigm that uses full-spherical perception to follow designated targets without active heading adjustment. To support this setting, we introduce 360UAV-ETrack, a simulation benchmark comprising 2,652 sequences, over 1.73 million synchronized observations, eight tracking tasks, and 150 held-out closed-loop scenarios. We propose 360UAV-TVLA, a panoramic vision--language--action (VLA) framework integrating persistent visual referring (PVR), compressed temporal memory (CTM), and geometry-aligned trajectory supervision (GTS) for instance identification, motion reasoning, and three-dimensional control. Experiments across two VLA backbones show consistent gains over standard fine-tuning, with normalized average tracking frames increasing from 22.56\% to 35.28\% for $\pi_0$ and from 25.68\% to 33.64\% for $\pi_{0.5}$. Our benchmark further reveals a substantial gap between offline imitation accuracy and closed-loop tracking reliability, establishing a challenging testbed for future research this https URL

---


### 121. [BayesPath: Reliability-Aware Bayesian Reasoning for Whole-Slide Pathology Agents](https://arxiv.org/abs/2611.33935)

**<font color=#1a73e8>作者：</font>** Bryan Wong, Xun Xu, Jongwoo Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diagnosing whole-slide images (WSIs) requires hypothesis-driven reasoning: pathologists form a differential diagnosis, seek discriminative evidence, weigh its reliability, and stop once it suffices. However, existing training-free WSI agents lack an explicit framework for such reasoning. They typically use a large language model (LLM) to aggregate the region descriptions of a multimodal LLM (MLLM), without a belief over the candidates or regard for the descriptions' reliability. Consequently, a repeated model error counts as independent evidence for an incorrect diagnosis. We introduce BayesPath, a training-free WSI agent that casts the pathologist's Scan-Look-Weigh-Decide process as reliability-aware Bayesian reasoning. An explicit belief over the candidates is updated with each observation through a reliability-aware likelihood and guides where to look next and when to stop. This likelihood corrects for the models' answer bias, discounts correlated observations, and captures diagnostic confusions estimated without labels. The updates form an interpretable evidence trail of how each observation shapes the belief. On five MultiPathQA tasks spanning slide classification and slide VQA, BayesPath achieves the highest average accuracy among training-free agents, 58.6% against 34.1% for the next best, with large gains on slide classification. On identical observations, Bayesian updating outperforms LLM aggregation on average, even with a larger LLM. BayesPath's belief is also better calibrated than naive Bayes, so uncertain cases can be deferred to pathologists. Code is available at this https URL

---


### 122. [InstructTTS-OPD: On-Policy Distillation for Multi-Objective Instruction-Following TTS](https://arxiv.org/abs/2611.33937)

**<font color=#1a73e8>作者：</font>** Haitao Li, Tian Tan, Yuguang Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Instruction-following text-to-speech (Instruct-TTS) renders a target transcript in the manner described by a free-form natural-language instruction, and a good rendition must succeed on three fronts at once: following the instruction, pronouncing the transcript correctly, and sounding natural. Reinforcement learning has become the standard way to post-train such generative models toward human preferences, and TTS systems increasingly adopt it. When the three objectives are optimized together under a single scalar reward, typically with group relative policy optimization (GRPO), training tends to be unstable: the objectives compete, and the shared update drifts toward whichever one is easiest to improve, producing a seesaw among them. We instead adapt on-policy distillation (OPD), which fuses several single-objective teachers by matching their velocity fields on the student's own rollouts. Realizing this for Instruct-TTS first calls for a sound reward on each axis, which we analyze carefully: a distilled Qwen-Omni proxy for the costly Gemini judge, dialect-free data for the WER reward, and DNSMOS in place of the language-biased UTMOS. We then train three single-objective teachers with GRPO and fuse them with OPD, routing each rollout to the instruction-following or WER teacher by its data domain and letting every rollout additionally follow the MOS teacher for quality. This lets instruction following and intelligibility improve together without a trade-off, but the quality target conflicts with instruction following, so following it additively reintroduces the seesaw. We therefore propose conflict-aware velocity fusion, which projects the quality target off the direction that opposes the primary objective before fusing, and show that it markedly reduces the instruction-following/quality trade-off. The fused model improves over scalar-reward GRPO on all three objectives at once.

---


### 123. [What Does Skill Lift Actually Measure? A Source-Code-Level Audit and Noise-Aware Reanalysis of SkillsBench](https://arxiv.org/abs/2611.33943)

**<font color=#1a73e8>作者：</font>** Haozhe Zhang, Zhen Long  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills are directories of instructions, reference materials, and scripts loaded on demand by coding agents. According to SkillsBench, although human-curated skills can raise the passing rate by about 16.6 percentage points (pp) on average, they have actually reduced the results for some tasks. Later research has started to gate or eliminate skills according to the above per-task gains. We have audited the above benchmark at the source-code level and analysed 7,554 public trials to form 1,421 paired "(configuration, task) cells". Source-code audit identified two controlled-verified cases of grader dependence and one operational definition gap; the average lift on these three tasks was 74.6 pp, and the overall average lift for the full set was 18.7 pp. The audit also found that four tasks contained placeholder skill directories, and a certain execution harness additionally added 48 built-in skills in most runs. No task-level reduction achieved statistical significance in the pooled reanalysis with multiple-testing correction. As there were at most three runs per condition for each cell, the observed negative differences are very susceptible to run-sampling noise, and arithmetically, 58% of the cells could not have shown a decrease. Therefore, the raw numbers of negative cells cannot show that skills cause harm. A gating strategy based on the skill-free score seems to improve by 2-3 pp in the logs; however, even after shuffling condition labels to remove any skill effect, it still achieves an increase of 4-7 pp. On the held-out runs not used for fitting and decision-making, there was no statistically significant improvement. The audit ledger and analysis scripts have been published by us.

---


### 124. [DLaR: Dynamic Stochasticity Control for Latent Reasoning in Large Language Models](https://arxiv.org/abs/2611.33962)

**<font color=#1a73e8>作者：</font>** Xiaocheng Luo, Peng Xu, Zaifu Zhan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent reasoning enables LLMs to operate in continuous embedding space, yet existing methods suffer from deterministic inference that precludes exploration of diverse reasoning paths. While recent approaches inject stochasticity to restore exploration, we identify two fundamental limitations: \textit{uniform stochasticity} across all steps is suboptimal, and unconstrained perturbations disrupt reasoning coherence. We propose Dynamic Stochasticity Control for Latent Reasoning (DLaR), a framework with two complementary mechanisms that operate at different temporal granularities within the GRPO reinforcement learning framework. At the token level, Adaptive Stochasticity Modulation (ASM) dynamically adjusts perturbation intensity at each latent step based on a confidence-entropy fusion signal, increasing exploration when the model is uncertain and preserving stability when confident. At the training level, Training-Aware Stochasticity Tuning (TAST) progressively decays the base stochasticity level following a curriculum schedule. Through this dual-level design, DLaR establishes a hierarchical exploration-exploitation strategy that operates at both token and training levels. Extensive experiments on four in-distribution and three out-of-distribution mathematical reasoning benchmarks demonstrate that DLaR achieves the highest average performance across model scales, reaching 27.9%/50.6% Pass@1/Pass@8 on Llama-3.2-1B and 46.8%/68.2% on Qwen2.5-1.5B. Code: \href{this https URL}{this https URL}.

---


### 125. [PatternMiner: Automated Mathematical Discovery Through LLM-Guided Training and Interpretation of Small Models](https://arxiv.org/abs/2611.33966)

**<font color=#1a73e8>作者：</font>** Michael Ruofan Zeng, Junaid Hasan, Xuanyu Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> There are several approaches to AI-driven mathematical discovery. One of these involves the use of large language models (LLMs) to resolve well-specified conjectures via text-based reasoning, while another uses narrow models and interpretability for more open-ended, human-in-the-loop exploration using object-based mathematical data. The latter is limited in its ability to move beyond simple empirical pattern detection while the former is not well-designed for direct, open-ended exploration of large mathematical datasets. In this paper we introduce PatternMiner, a system that combines these two paradigms. In PatternMiner, an LLM agent generates mathematical datasets based on an initial broad question, trains narrow machine learning models on them, uses interpretability techniques to extract patterns from these trained models, and uses these patterns to formulate conjectures. Once an initial conjecture has been formulated, PatternMiner instructs the agent to search for counterexamples using calls to mathematical software. If a set of counterexamples can be found, these are used as feedback for conjecture refinement or another round of training and interpretability. The conjecture progressively evolves through this iterative sequence with the agent allowed to try to prove it at any point. We describe the results of applying PatternMiner to five well-known positivity problems in algebraic combinatorics. PatternMiner proves several new theorems related to Schubert positivity and projection, a character-row evaluation formula, a restricted version of the Kazhdan--Lusztig combinatorial invariance conjecture, and Schur positivity for a family of immanant coefficients. We end by analyzing the most common routes to conjecture generation that are used by PatternMiner in our case studies as well as documenting the most common failure modes.

---


### 126. [Fine-Tuning Without Gradients? Closed-Form, LLM-Written Classifiers on a Frozen Encoder](https://arxiv.org/abs/2611.33972)

**<font color=#1a73e8>作者：</font>** Md Nasir Uddin, Musa Tur Farazi, Soumik Bhattacharjee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can a classifier computed in closed form on a frozen encoder match gradient fine-tuning? We present closed-form weight-space programming (WSP): a large language model (LLM), used as a design assistant, writes programs that read a frozen masked language model through cloze-style prompt templates at several layers, fit closed-form heads (shrinkage discriminant analysis, kernel ridge regression and the encoder's label-word prior) on labelled data, and select among a pool of candidate heads by cross-fitting. No gradient is computed and no encoder weight changes. We instantiate the framework on RoBERTa-large. On 11 development datasets with 512 to 8,192 training labels, WSP is ahead of full fine-tuning (FT) and LoRA at every label budget (by 0.3 to 0.6 points on average; the registered non-inferiority tests pass) and within 0.5 points of prompt-based fine-tuning (PFT); these datasets also shaped the recipe. With fewer labels its lead over FT and LoRA grows: 1.2 to 3.5 points with 64 and 128 labels, and 3.8 to 5.3 points in the few-shot setting of 16 labels per class, where WSP is again within half a point of PFT on the development datasets. On six held-out datasets, WSP stays ahead of LoRA and within half a point of FT on average, although with six datasets no registered test passes, and PFT is ahead, by 1.30 points with 8,192 labels. WSP never collapses and is deterministic, but it needs one encoder pass per template (17 here). We report all eight recipe versions, every decision that saw test results, and 27 ideas that did not help.

---


### 127. [Kolpona: An Agentic Framework with Gradient-Free Neuron Programming for RTL Generation](https://arxiv.org/abs/2611.33973)

**<font color=#1a73e8>作者：</font>** Musa Tur Farazi, Md Nasir Uddin, Soumik Bhattacharjee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open-weight large language models (LLMs) for register-transfer level (RTL) design are usually improved by fine-tuning on curated Verilog corpora, which needs large sets of verified designs and GPU training. We present Kolpona, an agentic framework that improves such models without gradient training. Its first component is neuron programming, a new form of weight-space programming (WSP) that writes single neurons in closed form into the weights to remove failure habits found on practice tasks, and keeps each edit only when testbench results on fresh tasks favour it. At inference time, tool-using agents propose designs, and a label-free selection stage delivers one design per task from the specification, the candidates and their simulations alone. On Qwen3.5-4B, edits to 16 neurons raise the VerilogEval v2 pass@1 of the model alone from 31.7% to 55.4%, and the full framework reaches 77.6%. On Qwen3.8-27B, Kolpona lifts pass@1 from 73.1% to 94.9% on VerilogEval v2 and from 66.0% to 92.0% on RTLLM v2.1 on a single 32 GB GPU, above every published system in our comparison. The RTL edits also carry over to Python and raise the pass@1 of the 4B model alone from 84.8% to 91.5% on HumanEval+ and from 67.7% to 77.5% on MBPP+.

---


### 128. [Auto-Features: An LLM-Assisted Corpus for Contextual Recognition of Standard and Optional Car Features](https://arxiv.org/abs/2611.33974)

**<font color=#1a73e8>作者：</font>** Filippos Ventirozos, Ioanna Nteka, Tania Nandy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Auto-Features, a corpus for detecting a car's standard and optional features in advertisement text, given the feature catalogue of that exact vehicle. Sellers name the same feature in many ways. We therefore cast the task as feature-conditioned, or contextual, named entity recognition: extract the span that expresses one given catalogue feature. An entity-linking view follows from the same output. The corpus has a human-gold layer (430 adverts) from screened annotators and an LLM-silver layer (925 adverts) auto-annotated by a search-grounded LLM. We also contribute the way it was built. Every LLM output is validated, and each kind of failure has its own remedy. Malformed output is patched. Hallucinated content triggers a fresh attempt by a stronger model. Links to features outside the candidate list are dropped and counted (3 in 10,928 records). The LLM annotates alone only after its agreement with human annotators on link verification is comparable to human-human agreement. On advert-disjoint splits, a LoRA-tuned 4B LLM reaches 63.9% span F1 and 76.1% on the entity-linking view. A fine-tuned encoder reaches 59.0% and 74.1%. The margin is widest on catalogue features never seen in training (54.5% vs. 49.0%).

---


### 129. [Quaternion-Tucker ZigZag Networks: Halving Transformer Backbone Parameters and Enabling Exact 2D Zero-Loss Continual Scaling](https://arxiv.org/abs/2611.33983)

**<font color=#1a73e8>作者：</font>** Shubham Barmase  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard Transformers allocate independent dense weight matrices to every feed-forward network (FFN) layer, coupling parameters linearly with depth (O(L)) and discarding prior compute when scaling capacity. Conversely, weight-tied Looped Transformers decouple depth from parameters (O(1)) but enforce time-homogeneous updates. We formulate the L-layer FFN stack as a 3D Tensor Cuboid and introduce QuatTucker-ZigZagGPT, unifying: (1) 4D Quaternion Hamilton GEMMs in bfloat16 (4x FFN compression), (2) 64x64 Block-Diagonal Tucker SwiGLU Cores for depth-specific rotations over a shared basis, (3) Braided ZigZag Diamond Routing (L0 -> L2 -> L1 -> L3) for zero-FLOP top-down refinement, and (4) Exact 2D Zero-Loss Continual Scaling in both width and depth. We also introduce Annealed Gated Bounce-Back Scaffolding (GatedBounce), which self-distills to 0.0% inference overhead. Across algorithmic tasks (8-bit Parity, 56-seed routing ablations, Mod-53 Grokking) and language modeling (TinyStories, FineWeb-Edu), our model outperforms standard Transformers at 2x-7.6x compression. On A100, QuatTucker-ZigZagGPT-12 (39.0M backbone) beats StandardGPT-12 (85.0M backbone) at 5/5 controlled checkpoints. Continually scaling one lineage across 6.00B tokens via zero-loss width growth (rank 6144 -> 8192), two bit-exact depth expansions (L = 12 -> 16 -> 20, 70.9M backbone, max_diff = 0.000000), and WSD cooldown reaches 3.3582 FineWeb-Edu loss (28.74 PPL) and 44.75% full-split zero-shot accuracy across 16,955 questions (ARC-Easy, HellaSwag, WinoGrande, BoolQ), matching GPT-3 Small (125M, 300B tokens) at 50x fewer tokens.

---


### 130. [Residual Cross-Model Narrative Convergence under Shared Prompts: Auditing Prompt Controls and Narrative Measurement](https://arxiv.org/abs/2611.34015)

**<font color=#1a73e8>作者：</font>** Mehdy Sedaghat Payam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stories created by LLMs based on the same prompts can be narratively similar to one another. This similarity may reflect constraints imposed by the prompts as well as the models' writing tendencies. The current research analyzes 51,240 stories created by five models in the StoryScope corpus based on 10,248 common prompts. It uses 213 narrative features in seven dimensions to compare cross-model distances between stories generated from the same prompts with distances between stories generated from different but semantically matched prompts. To assess the relationship between narrative features and prompt content, a semantic relevance mask was evaluated against 420 author-annotated prompt-feature judgments (F1 = .813; near-threshold accuracy = .621). The equally weighted mean Residual Convergence Index (RCI) was .409 without masking and .406 with masking. These findings indicate measurable cross-model narrative convergence relative to a semantically matched-prompt baseline, with little change following semantic relevance masking.

---


### 131. [Evaluating Ukrainian Grammatical Competence in Language Models: Probability Versus Prompting](https://arxiv.org/abs/2611.34016)

**<font color=#1a73e8>作者：</font>** Dmytro Babarytskyi, Oleksandr Babarytskyi, Vadym Savanevych  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Organisations deploying large language models in Ukrainian-language information systems need to know whether a model produces normative Ukrainian. This paper establishes a protocol for measuring that reliably and applies it to 19 models. The instrument is a released set of 1,444 Ukrainian minimal pairs covering the vocative case, numeral-noun and adjective agreement, verb government and calques from russian, with subject-verb agreement as a control; a quarter of the set was checked against the answer key in two independent native-speaker ratings, which agreed at Cohen's $\kappa$ = 0.963. Every pair is scored twice: by comparing the probabilities a model assigns to the two sentences, and by asking the model directly, with the sentences presented in both orders so that answer-position effects are measured instead of being absorbed into the score. Three results follow. Order consistency (the share of pairs answered identically when the sentences are exchanged) falls below 0.05 for ten of the nineteen models, and what separates the usable models is instruction tuning, not scale. The vocative case is systematically inverted: 0.153 accuracy against 0.951 on the control, with models preferring the non-normative nominative form of address. Ukrainian adaptation substantially reduces this deficit, measured against the exact checkpoints two adapted models were trained from.

---


### 132. [JHealthBench-L: Clinician-Reviewed Localization of HealthBench for Rubric-Based Medical LLM Evaluation in Japan](https://arxiv.org/abs/2611.34024)

**<font color=#1a73e8>作者：</font>** Shohei Hisada, Keisuke Orimo, Kenji Igarashi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubric-based benchmarks such as HealthBench evaluate large language models (LLMs) on open-ended health consultations using case-specific physician criteria, many of which presuppose the healthcare institutions, medications, and care pathways of their source region. Under machine translation alone, these regional assumptions remain in the rubric, leaving responses appropriate in Japan uncredited or falsely penalized under foreign clinical rules. To adapt established clinical evaluation perspectives to Japan without authoring rubrics from scratch, we construct JHealthBench-L (79 patient-facing consultations, 1,022 criteria) through source-cited LLM drafting, single-specialist selection and revision, independent dual-physician review, and meta-review. Specialists rewrote only 4.4% of criteria from scratch, and independent reviewers approved 93.6% of Stage-2 criteria without issue. Comparing JHealthBench-L with a machine-translated baseline across 18 LLMs reveals that translation-only evaluation preserves coarse model rankings ($\tau = 0.817$, mean shift +0.027) yet flips verdicts on 17.7% of modified criteria (vs. 7.3% re-grading noise) and reduces false penalties on Japan-adapted negative criteria by 7.1 percentage points, masking item-level clinical mismeasurement behind stable leaderboards. Axis-level and paired analyses further show that context awareness and Japan-specific clinical criteria remain primary bottlenecks, whereas Japanese continual pretraining and reasoning post-training substantially improve locally grounded performance. Datasets, physician revision logs, and evaluation code are available at this https URL.

---


### 133. [Few-Shot Adaptation of Vision-Language Models via Agentic Model Editing](https://arxiv.org/abs/2611.34036)

**<font color=#1a73e8>作者：</font>** Yusheng Zhao, Xiao Luo, Zhiping Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Few-shot adaptation transfers pretrained Vision-Language Models (VLMs) to new domains using a small set of labeled images. Most methods fit prompts, representations, or classifiers within an adaptation procedure specified in advance. Yet the visual distinctions needed for recognition can differ substantially across domains, motivating the question: Can an LLM agent use few-shot examples and model observations to design the adaptation procedure itself? We propose Agentic Model Editing (AME), an agentic framework that jointly designs input transformations, encoder edits, feature computation, and classifier fitting as an executable, domain-customized adaptation program. The agent inspects images, class semantics, model parameters, intermediate representations, and activations to formulate hypotheses about the target task. It implements and tests candidate programs on the support set, with aggregate validation accuracy guiding refinement and selection. Each program fits a complete domain model that is fixed before testing. The agent and its tools are shared across domains, while each domain receives its own adaptation program. Across eleven datasets with CLIP ViT-B/16, AME achieves the highest average accuracies of 81.2% without back-propagation and 81.9% with back-propagation among the compared methods. Further experiments demonstrate applicability across VLM backbones and LLM agents.

---


### 134. [Too Smart for Its Own Good? Cognitive Fidelity and Competence Leakage in LLM Simulations of Young Learners](https://arxiv.org/abs/2611.34042)

**<font color=#1a73e8>作者：</font>** Zhen Xu, Beata Beigman Klebanov, Jamie N. Mikeska  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based interactive learner simulators are increasingly used in educational applications, including teacher training and tutoring system development. A critical requirement for those simulations is cognitive fidelity: the simulated learner should maintain the assigned knowledge, misconceptions, and reasoning procedures throughout interaction. However, LLMs may express knowledge or problem-solving skills beyond the assigned learner's cognitive status, a phenomenon we refer to as competence leakage. In this exploratory study, we examine 3,339 simulated learner utterances from 130 teacher-learner simulator transcripts across three learning scenarios and identify over-competence as a prominent direction of cognitive-profile misalignment during interaction. We then investigate the recurrence of previously observed competence leakage cases under four matched-trigger evaluation protocols, ranging from isolated questioning to multi-turn interactions, across five model configurations. Overall, we observe higher violation recurrence under multi-turn protocols than under isolated question answering. More capable models generally show lower recurrence, whereas increased reasoning effort does not consistently improve cognitive fidelity and is even associated with slightly higher recurrence under multi-turn protocols in our matched-model comparison. These findings provide exploratory evidence of competence leakage phenomena in interactive learner simulation and suggest that single-turn question-answering type of evaluations alone may be insufficient, motivating the development of more systematic and reliable multi-turn protocols for evaluating cognitive fidelity in learner simulation.

---


### 135. [Reliable User Simulation in Complex Multi-Step Workflows](https://arxiv.org/abs/2611.34044)

**<font color=#1a73e8>作者：</font>** Pusala Pavan Teja, Jayasimha Talur, Saab Mansour 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based user simulators are increasingly used to evaluate conversational assistants. Yet, these simulators can drift from their assigned goals or fail to exhaustively explore all specified options, causing evaluation errors incorrectly attributed to the assistant. Prior work has examined goal alignment in single-task settings, but many practical scenarios require simulators to execute multi-step workflows with sequential tasks, fallback logic, and cross-task dependencies, where simulator fidelity has not been measured. To close this gap, we introduce a benchmark of 500 workflows represented using the Hierarchical Task Network (HTN) abstraction. Our experiments reveal that the simulator's fidelity degrades sharply with workflow complexity, and that goal drift accounts for the majority of failures. Fidelity also depends on the assistant's response style, with the same simulator scoring substantially better or worse across styles. To address this, we propose ReUST (Reasoning + User State Tracking), a simple prompting strategy to maintain state information across dialogue turns. ReUST improves goal success rate by more than 12 points for mid-sized and large models, and reduces simulator sensitivity to the assistant's response style.

---


### 136. [Stable Gated DeltaNet-2: Understanding and Mitigating Recurrent State Instability](https://arxiv.org/abs/2611.34051)

**<font color=#1a73e8>作者：</font>** Xichong Zhang, Xixuan Hao, Zhichen Liu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linear attention offers an efficient solution for long-sequence modeling via linear complexity and fixed-size recurrent states. Gated DeltaNet-2 (GDN-2) introduces independent channel-wise control over erasure and writing, enhancing state-update expressiveness and in-context retrieval, yet it suffers from training failures during long-context training. We trace these failures to the asymmetry between reading and modification directions during erasure, which yields non-normal erase operators whose directional gains accumulate across tokens, triggering exponential state growth even without new writes. To resolve this, we propose \model{}, employing symmetric erasure to ensure non-expansive state propagation and decay-regulated residual writing to preserve writing flexibility. Theoretically, we establish an $O(\sqrt{T})$ upper bound on recurrent state growth while retaining chunkwise parallel computation. Experiments on ~1.6B parameter models show that \model{} achieves stable training alongside improved long-context retrieval. Compared to GDN-2, it boosts the 128K average RULER score by 6.80 points in the recurrent setting and average accuracy across nine downstream tasks by 0.62 points in the hybrid setting.

---


### 137. [When to Respond, Where to Ground: Streaming 3D Affordance Grounding](https://arxiv.org/abs/2611.34067)

**<font color=#1a73e8>作者：</font>** Wenting Luan, Weilong Yan, Siqi Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Given a continuous RGB-D stream and a language request, streaming 3D affordance grounding requires an agent to decide when to respond and where to locate the requested functional part using only observations available so far. Existing 3D affordance grounding methods typically assume complete scene observations, while streaming vision-language models lack fine-grained 3D functional grounding. Our goal is to jointly determine response timing and functional-part localization during continuous scene observation. We propose StreamAff, an evidence-guided response strategy that makes both decisions from the grounding model's own visual evidence. The model scores the visual patches of the frames it reads: their combined support, weighed against a wait option, decides when to respond, and the highest-scoring patch selects the frame to ground in. A conditional look-back policy lets the model answer from an earlier observation at the moment of the request or wait for new evidence, and zoom-and-refine grounding segments the part named in the answer on the 3D points of the selected frame. We further introduce StreamFun3D, a benchmark derived from real-world 3D scenes that evaluates response timing and grounding across four evidence settings: Current, History, Future, and Unobserved, together with StreamIoU, a metric that credits a mask only when the response is timely and grounded in a valid source frame. We adapt offline 3D affordance grounding methods and build external-decider baselines that pair vision-language models with our mask decoder. StreamAff achieves 30.14% StreamIoU on 15-second streams, a 40.6% relative improvement over the strongest of these baselines.

---


### 138. [Budget, Readout or Reasoning? Where Small Reasoning Models Lose Value in Auction Bidding](https://arxiv.org/abs/2611.34068)

**<font color=#1a73e8>作者：</font>** Mahbod Khaleti, Seyed Reza Tavakoli, Baran Hoseini 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ad platforms and marketplaces show bidders a bid landscape, the estimated chance of winning at each candidate bid, and increasingly let agents built on reasoning language models choose the bid. We give six open reasoning models of 4B to 14B parameters such landscapes, with win curves from eBay closing prices and from a simulated advertising market (AuctionNet), and score their bids on held-out auctions against an exact calculator. Because the agent is handed the estimates, the lost value can be split by cause. Two failures belong to the models. They pass over the best option even when the values written in their own trace already rank it first, and their wrong answers lean toward the highest bid on the menu. The lean is about the bid's size, not its place in the list, and it survives sampling. At 768 forced tokens on eBay, under pay-your-bid pricing, the wrong answers cost bidders 7-17% of the surplus the calculator's bids earn. Arithmetic errors are rare. Two further losses come from operator choices. A token cap cuts traces short: allowed to stop on their own within 4,096 tokens, five models recover 91-100% of the calculator's lead over a model that does no reasoning. Asking for the answer while the reasoning block is still open misreads it: closing the block first lifts the weakest model from 42% to 84% on eBay and from 24% to 81% on AuctionNet. Finally, an audit that flags bids disagreeing with the trace's own numbers, and overrides them with the calculator's bid, raises the share of the calculator's lead recovered at 768 forced tokens from 42-85% to 84-100% on eBay under nested cross-validation, and the same reader settings transfer from eBay to AuctionNet.

---


### 139. [Projector Subspace Optimization for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2611.34078)

**<font color=#1a73e8>作者：</font>** Hao Yu, Quan Cheng, Lijun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) achieve strong performance through instruction tuning, yet adapting them to sequential tasks requires Multimodal Continual Instruction Tuning (MCIT). Existing replay-free methods expand prompts or routed LoRA experts across multi-layer decoders, incurring heavy parameter and routing overhead while shifting internal feature distributions. Instead, we identify the final linear layer of the vision-language projector as a high-capacity, coordinate-stationary bridge, where sequential updates easily induce interface drift by displacing historical visual tokens. While low-rank subspace adaptation offers a compact remedy, selecting directions solely from historical statistics or task gradients sacrifices plasticity or stability, and unconstrained multi-step updates still accumulate large drift. To resolve both issues, we propose Projector Refinement through Optimized Update Directions (PROUD), a continual subspace optimization framework for the terminal projector layer. At task onset, PROUD combines retained input statistics with initial gradients to analytically extract a metric-orthonormal subspace maximizing first-order task gain under a drift budget. During training, it regularizes updates within this fixed subspace via an exact Frobenius penalty before losslessly merging them with zero inference or routing overhead. Experiments on UCIT and CoIN across MLLM backbones show that PROUD outperforms recent replay-free baselines in continual accuracy while curbing forgetting with a fraction of trainable parameters.

---


### 140. [From Diagnosing Alignment to Joint Supervision in Multimodal Draft Training](https://arxiv.org/abs/2611.34091)

**<font color=#1a73e8>作者：</font>** Haozhe Du, Runze Liu, Jiaming Fan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal drafts learn from multimodal (MM) and text-only (TXT) supervision, yet their effects on alignment and how to combine them remain unclear. We diagnose draft-target alignment through paired predictions with and without visual input, decomposing distributional error into text-conditioned and visual-response components. Drafts with similar text-conditioned alignment can still differ markedly in visual-response risk and acceptance. Controlled continuation training shows that high-risk groups outperform random and low-risk groups, and visual-response risk guides MM training more effectively than aggregate risk. Building on these diagnostics, we propose MNRS-Joint, which configures joint supervision from a given draft's component-risk distributions, using modality-specific mean risks to determine the MM:TXT mixture. Across three warm-ups, its distinct mixtures fall in high-performing regions of the ratio sweeps. On LLaVA-1.5-7B, MNRS-Joint improves mean accepted length from 3.35 to 3.53 and mean speedup from $2.04\times$ to $2.16\times$ over composition-matched random training under greedy tree decoding. The gains also hold under stochastic chain decoding.

---


### 141. [Improving Tail-Augmented Speculative Drafting with Hidden State Mixing and Gradient Detach](https://arxiv.org/abs/2611.34092)

**<font color=#1a73e8>作者：</font>** Yaniv Galron, Rabeeh Karimi Mahabadi, Maor Ashkenazi 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-token prediction (MTP) modules and EAGLE-style drafters support efficient speculative decoding by reusing target-model hidden states. Their autoregressive use, however, introduces a training-inference mismatch: training supplies sequences of hidden states from the backbone or a single MTP step, whereas inference attends to a target-model prefix followed by a growing tail of recurrently generated MTP states. EAGLE-3's training-time test (TTT) explicitly simulates this behavior during training, at the cost of additional memory and specialized attention masks. We introduce two training-only methods for improving autoregressive drafting. Hidden State Mixing (HSM) samples among backbone and MTP hidden states aligned to the same prediction target, exposing the drafter to mixtures of states from different MTP steps without explicitly simulating inference. Hidden State Gradient Detach (HSGD) is a regularization method that stochastically blocks gradients through hidden state and embedding pathways while preserving the forward computation. Neither method adds inference cost. In joint pretraining followed by supervised fine-tuning, HSGD yields the highest acceptance rates at early draft positions, while HSM performs best later in the draft. These acceptance rate trends favor HSM for long-draft-length serving and HSGD for short-draft-length serving. Furthermore, across four Nemotron models and DeepSeek-V4-Pro, HSM-based MTP boosting with a frozen backbone improves mean acceptance length by up to 52.2% over the co-trained MTP. For EAGLE-3 drafters, HSM offers competitive acceptance with TTT, with 48% lower peak reserved training memory in a four-step Qwen3-8B comparison. HSM implementations are publicly available in Megatron-LM and NVIDIA Model Optimizer.

---


### 142. [What Makes a Gavagai? Learning Visual Concepts from One Positive and Few Negatives](https://arxiv.org/abs/2611.34105)

**<font color=#1a73e8>作者：</font>** Katsuya Ogata, Kazuya Nishimura, Yuta Nakashima  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans can recognize novel concepts from only a few observations by identifying defining visual attributes and eliminating alternative interpretations. However, a single observation is consistent with multiple possible concepts, and accurate visual perception alone is insufficient to determine the intended interpretation. Negative evidence can reduce this ambiguity by eliminating competing hypotheses. Inspired by Quine's gavagai problem, we introduce the Gavagai Benchmark to evaluate whether vision-language models can identify the attributes defining a novel concept from positive and negative examples. The benchmark consists of synthetic images depicting novel combinations of visual attributes and real images of newly described species. Using these datasets, we examine how models use negative examples to identify novel concepts and analyze the respective roles of visual perception and reasoning. Several models struggle even when correct attributes are provided, while others show large gaps when ground-truth attributes are replaced with model predictions. These diagnostic comparisons highlight challenges in both attribute perception and inference from limited evidence.

---


### 143. [A Simple Yet Effective Agent for Open-World Aerial Object Search](https://arxiv.org/abs/2611.34115)

**<font color=#1a73e8>作者：</font>** Jitai Hao, Liangxing Yang, Zhenyang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-world aerial object search methods often rely on persistent spatial maps, learned world models, or task-specific policy training. To examine how far a minimal, training-free design can go, we introduce SimpleUAV, an agent built around a frozen, off-the-shelf vision-language model (VLM). SimpleUAV separates current-view target assessment from history-conditioned action selection, combining fresh candidate evidence with lightweight search context. Local geometry converts visual selections into bounded straight-line movements, depth-based checks halt blocked segments, and measured execution feedback guides subsequent decisions. This closed loop sustains search without persistent spatial maps or task-specific training. SimpleUAV achieves 41.61% Success Rate (SR) on UAV-ON and 11.98% on AerialDojo-200K, compared with 23.80% and 3.20% for the strongest prior baselines, respectively. With limited benchmark-specific adaptation, the same core agent transfers to aerial Vision-and-Language Navigation (VLN) on TravelUAV, improving Full SR by at least 19.66% across all three splits under L1 assistance. These results establish a strong baseline for evaluating when additional architectural complexity benefits aerial search.

---


### 144. [From Data Room to Report: End-to-End AI Support for M&A Legal Due Diligence](https://arxiv.org/abs/2611.34120)

**<font color=#1a73e8>作者：</font>** Johannes R. Hübers, Daniel Uedelhoven, Manuela Bergau 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal due diligence in mergers and acquisitions requires lawyers to organize heterogeneous virtual data room documents, extract transaction-relevant information and consolidate reviewed findings into a due diligence report. We present LEXI (Legal Extraction and Intelligence), a work-in-progress system that demonstrates how large language models can support this process from document ingestion to report preparation. LEXI classifies documents under a configurable due diligence taxonomy, assigns relevant target entities, extracts predefined information with supporting passages and page-level provenance and prepares report content from reviewed findings. Structured outputs connect these stages and allow model-generated results to be passed through the workflow in a controlled form. Lawyers review and correct classifications and extractions and retain responsibility for legal assessments, recommendations, risk ratings and final report wording. Initial evaluations of the classification and extraction components provide preliminary evidence that the approach is feasible. LEXI illustrates how AI can be integrated across the legal due diligence workflow while preserving lawyer control over substantive legal judgment.

---


### 145. [Unstable Action Boundaries in Lethal Drone Agents](https://arxiv.org/abs/2611.34121)

**<font color=#1a73e8>作者：</font>** Jacques Dumora, André-Louis Rochet, Simon Roburin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool-using large language model (LLM) agents raise safety risks that are not captured by text-only refusal behavior, especially when tools can trigger high-impact actions. This concern is salient in military settings, where autonomous weapons raise the possibility of delegating force decisions to software agents. In this work, we study whether a drone agent's action boundary is stable under changes to the target descriptor. We evaluate recent and popular LLMs in a simulated perception-action pipeline over real-world drone imagery, where models can localize requested targets and invoke a simulated lethal tool. We find two concerning failure modes. First, some LLM agents invoke the lethal tool for ordinary generic descriptors such as \emph{people}, requiring no jailbreak at all. Second, an agent that initially appears conservative under protected descriptors can become unsafe under a simple semantic target shift.

---


### 146. [Out of Sight, Not Out of Clues: Can Video LLMs Guess from Partial Evidence?](https://arxiv.org/abs/2611.34126)

**<font color=#1a73e8>作者：</font>** Luoxi Zhang, Jiawei Liu, Yanlin Luo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In real-world applications like egocentric recording, visual accessibility, and surveillance review, visual evidence for Video Large Language Models (Video LLMs) is often only partially captured. A reliable model should match its response to the evidence: answering when sufficient, guessing from visible clues when partial, and abstaining when absent. Yet existing benchmarks enforce a binary answerable-or-unanswerable split, leaving partial evidence unmeasured and obscuring whether failures arise from missing evidence or misjudging sufficiency. We introduce ClueProbe, a diagnostic benchmark to (1) separate perceiving evidence from judging sufficiency, and (2) validate our diagnosis via targeted fine-tuning. ClueProbe comprises 1,721 human-annotated questions across 598 natural videos, labeled Answerable, Guessable, or Unanswerable, alongside controlled perturbations altering wording or visual input. Evaluating 10 open-source and proprietary Video LLMs reveals that failures stem from judgment rather than perception: models perceive the evidence yet lack graded sufficiency awareness, answering or refusing outright while rarely guessing from partial clues. Targeted fine-tuning shows that this reflects missing supervision rather than insufficient capacity: supervising the guess level lifts appropriate guessing from 1.6% to 40.4% without extra false refusals, whereas conventional refusal tuning rejects 92% of guessable questions. Data and code will be released at this https URL.

---


### 147. [Agent-as-a-Verifier: From Scores to Evidence for General Verification](https://arxiv.org/abs/2611.34132)

**<font color=#1a73e8>作者：</font>** Yuxuan Sun, Chen, Nagarajan Natarajan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Verification is increasingly critical across various inference and learning paradigms, such as test-time scaling, recursive intelligence and automated research, where feedback can improve efficiency and optimization. Common score-based verifiers, or discriminative reward models, predict a scalar reward for an output. While useful for filtering, rewarding, and ranking, such scores provide no explicit, auditable evidentiary basis for the judgment. In parallel, although existing generative process reward models offer text feedback, most designs do not fully exploit agentic capabilities, such as tool use and iterative reasoning, which are essential for fact-checking and fine-grained claim verification. In this paper, we address these limitations by introducing Agent-as-a-Verifier, an agentic, certificate-producing verification system that places role-separated LLM agents inside a formal-methods-inspired claim-obligation-certificate protocol. Given a generation candidate, Agent-as-a-Verifier produces a certificate by extracting a verdict-blind dependency graph of claims, independently compiling the task's acceptance contract, and deriving checkable obligations. On Terminal-Bench 2.1, Agent-as-a-Verifier achieves higher accuracy than the state-of-the-art approach. Across different downstream applications, the augmented agent also outperforms the plain agent on FrontierMath and CyberGym. More importantly, Agent-as-a-Verifier is able to identify reward-hacking solutions that deceive the benchmark evaluator, highlighting its broader potential for iterative and recursive agent optimization. Code is available at this https URL

---


### 148. [Letting Models Manage Their Own Context: Where We Stand](https://arxiv.org/abs/2611.34147)

**<font color=#1a73e8>作者：</font>** Alessio Devoto, Avinash Vem, Tara Safavi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent harnesses today manage context on the model's behalf: when the window fills, the harness triggers a compaction that summarizes the history. We study the alternative, \emph{model-driven} context management, in which the model itself decides when and what to compact through a context API. We gave models control over their own context in \nooa, NVIDIA's open source agent harness, and compared the two strategies on document research and machine learning engineering across context budgets from 8K to 512K tokens. Models that use the context API effectively reach higher accuracy, often with fewer input tokens, especially at tight budgets: \textbf{GPT 6.1 nearly triples its score at a 32K budget} on OfficeQA Pro v2 (21\%~$\rightarrow$~56\%), and \textbf{Kimi gains with up to 41\% fewer input tokens}. Models differ widely, however, in how often they use the API, how aggressively they compact, and when they start compacting, and prompt changes shift that timing. Finally, we show that \textbf{inference engines can make model-driven edits cheaper}: by reusing the KV cache of the unchanged suffix after an edit, \textbf{we cut prefill compute by up to 15\% per request with no measurable change in accuracy}. Together, these results point to a new co-design frontier: models trained to manage their own context, served by inference engines that support KV cache editing.

---


### 149. [Lost in the Grid: Where Multimodal LLMs Fail Between Seeing and Planning](https://arxiv.org/abs/2611.34152)

**<font color=#1a73e8>作者：</font>** Luoxi Zhang, Tianyi Tan, Jiawei Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) excel at static visual understanding and are increasingly applied to spatial planning, where a model interprets a visual layout and outputs an action sequence to reach a goal. Grid games are a common testbed for this ability because their rules are explicit and a solver can verify every move. Yet existing benchmarks mostly report end-to-end success rates, which hide whether a failure stems from visual perception, rule application, or multi-step planning. We introduce GridProbe, a diagnostic benchmark that 1) locates the failing stage between visual perception and planning and 2) verifies the diagnosis by targeted fine-tuning. On Sokoban, GridProbe pairs end-to-end solving with four probes (recognition, localization, single-step prediction, and state tracking) and gives every board both as an image and as an equivalent text grid. Evaluating seven MLLMs on Sokoban and a maze game reveals distinct bottlenecks behind similar success rates: proprietary models are limited by multi-step planning, whereas open-source models are limited by rule application or by visual grid indexing, i.e., counting rows and columns. Planning failures also hide perception failures: when planning is easier, the visual cost of the same model grows from 7.6 to 37.7 points. The diagnosis identifies what to train: fine-tuning only the vision module of the perception-limited model on board reading raises its interactive Sokoban success 3.5-fold (5.8% to 20.4%) and transfers zero-shot to the unseen maze game (single-turn success 13.8% to 67.1%), whereas the same data does not help a rule-limited model and training on solver solutions brings no gain. We will release the benchmark and code at this https URL.

---


### 150. [Interacting with Alexa: A Longitudinal Case Study of Voice Assistant Use in Down Syndrome](https://arxiv.org/abs/2611.34159)

**<font color=#1a73e8>作者：</font>** Caterina Senette  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As life expectancy for individuals with Down syndrome (DS) continues to increase, supporting cog- nitive engagement, everyday autonomy, and participation throughout adulthood has become an important research priority. Conversational voice assistants have emerged as promising assistive tech- nologies for these purposes, yet evidence regarding their long-term use in naturalistic settings remains limited. This paper presents a longitudinal case study of the everyday use of Amazon Alexa by an adult with Down syndrome over nine months in a real domestic environment. The study combines analyses of interaction logs, audio recordings, and qualitative observations to investigate usage pat- terns, interaction performance, communicative adaptation, and the integration of the voice assistant into everyday life. Results show that Alexa became progressively embedded in daily routines, sup- porting entertainment, information access, and autonomy-related activities. Longitudinal analyses reveal stable interaction patterns, reduced retry behavior, and the emergence of effective communi- cation strategies, while qualitative observations highlight increasing communicative engagement and the value of proactive reminders. The study also identifies important limitations of current commer- cial voice assistants, including reduced robustness to non-normative speech, limited conversational continuity, and poor contextual reasoning. Beyond providing rare ecologically valid evidence of long- term voice assistant use, the findings highlight design considerations that are relevant to the ongoing evolution of LLM-based conversational systems.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-267](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
