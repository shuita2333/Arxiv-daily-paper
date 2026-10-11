# 🧠 大模型相关研究 | 2026年10月12日

> 本类共 **288** 篇论文：已确认 **273** 篇，待复核 **15** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-288](./part-06.md)

---

### 101. [From Geometry to Generalization: Why Row Normalization Can Beat Adam and Muon](https://arxiv.org/abs/2610.11309)

**<font color=#1a73e8>作者：</font>** Jihwan Kim, Dogyoon Song, Chulhee Yun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Different optimizers can fit the same training data while selecting classifiers with substantially different geometries, but whether this difference provably affects population performance remains unclear. We show that row-wise normalization can achieve strictly higher population accuracy than full-batch Adam, a proxy for random-reshuffling Adam, and exact-SVD Muon in high-dimensional multiclass classification. Under an isotropic Gaussian-cloud data model, this advantage arises because row normalization's class-wise Euclidean geometry asymptotically preserves the population decision-boundary directions, whereas Adam's coordinate-wise geometry and Muon's spectral geometry introduce nonvanishing distortions. Beyond isotropy, the advantage persists for full-batch training on class means with independently oriented class-mean and test-noise covariances. It holds for power-law spectra with class-mean exponent below one, even under heavily anisotropic test noise. When both covariances are diagonal and sufficiently close, the advantage over Adam can reverse, while applying the same random rotation to both restores it by changing only their alignment with Adam's coordinate axes. Synthetic and last-layer language-model experiments support the predicted advantage.

---


### 102. [FloorSAV: Elucidating Spatial Audio-Visual Context with 2D Floormap for AV-LLMs](https://arxiv.org/abs/2610.11310)

**<font color=#1a73e8>作者：</font>** Kyeong-Rae Kim, Sungnyun Kim, Tae-Hyun Oh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While 3D spatial reasoning in dynamic egocentric environments is crucial for embodied intelligence, audio-visual large language models (AV-LLMs) lack explicit mechanisms to process and internalize global geometry directly from raw sensory streams. Existing approaches either require costly fine-tuning or underutilize the model's cross-modal reasoning capacities. In this paper, we propose FloorSAV, a novel framework that explicitly grounds spatial audio-visual context by rendering a dynamic 2D floormap. By integrating 3D point clouds, camera trajectories, spatial audio cues, and semantically grounded object landmarks, we inject this floormap into the AV-LLM as a synchronized stream with an egocentric video. AV-LLMs utilize their multi-modal capabilities to jointly reason over visual, auditory, and geometric cues in a single inference with floormap interpretation guidance. We further introduce SAVED-Bench (Spatial Audio-Visual Egocentric Benchmark with Dynamic Agents), constructing essential tasks of spatial capability in real-world scenarios: dynamic relativity, regional, and path reasoning QAs. FloorSAV improves AV-LLMs' spatial reasoning on various tasks from both SAVED-Bench and SAVVY-Bench. Studies with ground-truth floormaps demonstrate the substantial potential of FloorSAV with accurate spatial information.

---


### 103. [MedBenchAgent: Towards Systematic Automation of Medical VLM Benchmark Construction](https://arxiv.org/abs/2610.11312)

**<font color=#1a73e8>作者：</font>** Yulin Fu, Junren Wang, Guangjing Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-scale construction of medical vision-language model (VLM) benchmarks is increasingly feasible with richly annotated imaging datasets and large language models (LLMs), yet existing automation largely focuses on generating evaluation items within predefined benchmark specifications. We study the broader problem of automatically deriving the specification itself: what to evaluate, which annotations support each task, and how to translate this evidence into reliable evaluation items. We formulate benchmark construction as constrained compilation, in which the benchmark specification is progressively derived from evaluation requirements, heterogeneous annotations, and medical knowledge. Based on this formulation, we introduce MedBenchAgent, a multi-agent framework with a Benchmark Intermediate Representation (BIR) that encodes task definitions, evidence mappings, evaluation protocols, and item specifications across construction stages. MedBenchAgent separates planning, which derives and verifies the specification, from instantiation, which constructs and audits items under the locked specification. MedBenchAgent achieves a Task-Space F1 of 90.9%, outperforming direct task induction (79.2-80.0%) and prior-guided induction (85.1%); 994 of 1,000 sampled items from correctly identified tasks pass human audit. We further demonstrate portability to a specialized medical domain and evaluate twelve VLMs, revealing task- and setting-specific variation obscured by aggregate scores. These results establish constrained compilation as a scalable and auditable framework for medical VLM benchmark construction beyond question generation.

---


### 104. [From Retrieval to Reconstruction: Constructing Evolvable Cognitive Memory for Long-Term Dialogue](https://arxiv.org/abs/2610.11314)

**<font color=#1a73e8>作者：</font>** Zirui Liao, Zhengxian Wu, Zhuohong Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) serving as long-term dialogue agents require memory systems that support reliable reasoning over extended interactions. However, existing Retrieval-Augmented Generation (RAG) frameworks typically treat memory as passive storage, making it difficult to distinguish source-attributed beliefs from unattributed event/fact records and to connect evidence dispersed across sessions. We introduce CogMem, a cognitive memory architecture based on the PEC$^2$F (Person-Event-Concept-Claim-Fact) graph schema. Dedicated Claim nodes preserve the source and target of subjective statements, while Fact and Event nodes represent semantic and episodic knowledge. Dialogue turns are incrementally converted into provenance-aware graph records, consolidated into higher-level facts, and reconciled into temporally scoped Claim views when the same source provides conflicting updates. For retrieval, a rule-based controller driven by LLM intent parsing composes four deterministic graph operators---anchoring, traversal, intersection, and evidence grounding---to reconstruct query-relevant context. Experiments on LoCoMo and LongMemEval show strong performance, especially on multi-hop, temporal, and knowledge-update tasks. Ablations and a semantic-collapse probe support complementary contributions from epistemic separation, consolidation, and agentic retrieval. Code: this https URL.

---


### 105. [Deflating the Hessian: Rank-4 W4A4 Quantization for Multimodal Diffusion Transformers](https://arxiv.org/abs/2610.11315)

**<font color=#1a73e8>作者：</font>** Shiwen Wang, Pengxiang Zhao, Xiaoming Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In diffusion transformers, low-rank branches can mitigate 4-bit weight--activation (W4A4) post-training quantization (PTQ) loss by decomposing each weight into a low-bit residual and a high-precision low-rank component. Existing low-rank PTQ approaches, however, either optimize low-rank compensation and residual quantization separately, often requiring higher ranks, or rely on second-order weight updates without explicitly modeling activation quantization error, which becomes particularly pronounced under 4-bit quantization. To address these limitations, we present \method{}, a unified framework modeling low-rank-assisted W4A4 PTQ as a coupled calibration problem and deriving optimization-based solvers from the joint objective. Eliminating the output-side low-rank factor yields a \emph{deflated Hessian} that discounts residual errors already captured by the low-rank component, while an activation-noise surrogate is incorporated to suppress activation quantization error. Across five diffusion backbones, rank-4 \method{} consistently outperforms rank-4 SVDQuant in PSNR and LPIPS. It further surpasses rank-32 SVDQuant on SANA-1.6B, FLUX.1-schnell, and FLUX.1-dev with an $8\times$ smaller rank and up to $6.25\times$ faster quantization. Furthermore, on the Qwen3-8B LLM, rank-4 \method{} improves MMLU accuracy from 61.50\% to 68.17\% over rank-32 SVDQuant. Overall, \method{} achieves better W4A4 performance with substantially lower rank and quantization cost.

---


### 106. [DivMoE: Fine-Grained MoE Upcycling via Cross-Domain Expert Composition](https://arxiv.org/abs/2610.11317)

**<font color=#1a73e8>作者：</font>** Yuxuan Lou, Kai Yang, Geng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures have become essential for scaling large language models, with recent work demonstrating the benefits of fine-grained expert designs. Training such models from scratch is expensive, and sparse upcycling from pre-trained dense models is an attractive alternative. However, we identify a structural pathology of fine-grained upcycling: when fine-grained experts are derived from a single source model, naive routing collapses and downstream accuracy drops to near-random (e.g., on Qwen3-1.7B, Drop-Upcycling-fine-grained reaches only 23.2% average accuracy across 15 benchmarks, essentially matching from-scratch training at 22.2%, while the same method's coarse-grained variant reaches 50.2%). We propose DivMoE, the first framework achieving fine-grained MoE Upcycling with structurally-balanced routing. DivMoE introduces domain-specialized fine-grained expert initialization, deriving experts from dense models that have undergone domain-adaptive continual pre-training, and diversity-constrained routing, a hard structural constraint guaranteeing that each token activates experts from distinct domain groups. Across two base models and 15 benchmarks, DivMoE consistently outperforms six upcycling baselines (55.6% vs. 51.6% for the strongest baseline on Qwen3-1.7B) and strictly improves over the dense base model on every benchmark after Stage 2 continual pre-training -- closing the regression gap that has plagued prior fine-grained upcycling. After supervised fine-tuning on a public reasoning mixture, our 12B-parameter DivMoE model matches Moonlight-MoE (16B) at 64.5% average accuracy while outperforming a controlled NVIDIA-Upcycling baseline by 6.1 percentage points.

---


### 107. [Mine Odyssey: Benchmarking Spatial Agentic Intelligence in the Wild](https://arxiv.org/abs/2610.11328)

**<font color=#1a73e8>作者：</font>** Yuxuan Cao, Junlong Li, Hao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Advances in foundation models are driving efforts to introduce agents to assist people in the physical world. Such agents require agentic spatial intelligence: exploring unfamiliar environments, updating spatial understanding through interaction, and adapting actions based on feedback to sustain progress toward a sequence of goals. Existing benchmarks cover only a limited range of spatial layouts, scales, and traversal requirements. We introduce Mine Odyssey, a benchmark for evaluating agentic spatial intelligence using Minecraft reconstructions of real-world locations. It comprises 180 tasks covering 30 such locations across 20 countries and regions on five continents, including 20 outdoor and 10 indoor settings. These settings span diverse spatial scales, layouts, terrains, and connectivity patterns, from Midtown Manhattan and rural Entrup to Santa Lucía Hill and Buckingham Palace. We select meaningful waypoints, such as landmarks, buildings, and rooms, and manually verify their accessibility. Each task provides a natural-language instruction specifying which waypoints to visit and in what order. Completing these tasks requires agents to find accessible routes and entrances, open doors, and move between levels using stairs and ladders, while monitoring their progress and recovering from navigation errors. Across eight evaluated state-of-the-art models, GPT-6 Astra achieves the highest success rate of 85.6%. However, the second-best model, Claude Opus 5.5, completes 73.9% of tasks, while the strongest evaluated open-weight model, DeepSeek-V4.1-Flash, reaches 23.9%, highlighting substantial room for improvement in the agentic spatial intelligence of current models. Comprehensive analyses and ablation studies on Mine Odyssey reveal current models' limitations and provide insights for advancing agentic spatial intelligence.

---


### 108. [PathLang: A Language-Centered Benchmark for Vision-Language Models in Computational Pathology](https://arxiv.org/abs/2610.11329)

**<font color=#1a73e8>作者：</font>** Fanqi Cheng, Kuo Gong, Shangke Liu 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology vision-language models (VLMs) have shown strong visual perception ability, but their robustness in the language domain remains poorly characterized. Existing pathology VLM benchmarks largely rely on canonical closed-set prompts or perturb only generic templates, treating language as a fixed evaluation component rather than a variable axis of model behavior. In clinical practice, however, diagnostic language varies across reports, institutions, and candidate diagnoses. We introduce PathLang, a language-centered and clinically grounded zero-shot benchmark. PathLang holds the underlying slides, ground-truth labels, and image-text evaluation direction fixed while systematically varying only the diagnostic language, so that performance differences reflect how a diagnosis is phrased rather than what is imaged. The language variation follows how pathologists actually rephrase diagnoses (terminology, specificity, and reporting style), and all prompts and candidate pools are validated by six board-certified pathologists. PathLang covers four task families: (1) zero-shot classification with image-text alignment analysis, (2) cross-modal retrieval, (3) paraphrase robustness, including semantic-equivalence paraphrases, length and reporting-style variation, and prompt ensembling, and (4) open-vocabulary diagnosis retrieval over four candidate pools with distinct forms of semantic competition. Across nine VLMs and five public datasets spanning four organs, we find that performance is highly sensitive to clinically equivalent paraphrases, varies substantially across forms of semantic competition, and that image-text alignment quality does not necessarily translate into inter-class separability. We release the prompt corpus, candidate pools, pre-computed text embeddings, and evaluation code at this https URL.

---


### 109. [ReCal: Calibrating Structured Pruning for On-Policy Distillation Recovery](https://arxiv.org/abs/2610.11332)

**<font color=#1a73e8>作者：</font>** Houcheng Jiang, Mao Zheng, Mingyang Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured pruning reduces the deployment cost of reasoning language models, but the resulting capability degradation can hinder subsequent on-policy distillation (OPD) recovery. Because OPD relies on student-generated trajectories, pruning damage that persists after offline distillation can limit its effectiveness. We propose RECAL, Recovery-Aware Calibration, a simple plug-and-play approach that improves OPD recovery by adjusting calibration before pruning. RECAL uses forward KL between an unpruned teacher and a pruned probe to identify teacher-supported predictions disrupted by pruning, then reweights calibration statistics to guide existing pruning criteria toward preserving these predictions. Across multiple models and pruning methods, RECAL consistently improves mathematical reasoning after OPD, achieving gains of up to 16.7 percentage points on AIME, alongside improvements in most code-generation comparisons. Further analysis shows that RECAL reduces residual damage at heavily affected tokens and establishes performance advantages that persist through recovery. These results demonstrate the value of recovery-aware calibration for improving on-policy distillation recovery of pruned reasoning models.

---


### 110. [ReCast: Attribution-Oriented Step Representation Learning for LLM-Based Agent Systems](https://arxiv.org/abs/2610.11334)

**<font color=#1a73e8>作者：</font>** Weilin Jin, Mingyu Wang, Taiyu Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In LLM-based agent systems, failures can originate from early steps whose effects propagate through subsequent interactions, making their origins difficult to identify. To trace such failures back to their origin, failure attribution has been formulated as the task of identifying the earliest step responsible for the failure. Recent methods leverage LLM internal signals for failure attribution, typically using hidden states as step representations. We therefore conduct an empirical study to evaluate how effectively these representations distinguish root-cause steps from other steps and find limited separation. Motivated by this observation, we propose ReCast, a step representation learning method that transforms hidden states from a frozen LLM into attribution-oriented step representations. ReCast first selects attribution-relevant layers, then constructs complementary pattern and deviation features, and finally learns contextualized step representations through an encoder trained with contrastive and ranking objectives. We also introduce ReCast-2K, a training dataset for failure attribution. ReCast achieves the best Hit@1 across four benchmarks, surpassing the strongest baseline by 5.65 and 9.19 pp on Who&When Algorithm and Handcrafted, respectively. Code is available at this https URL .

---


### 111. [SynCo: Data Synthesis Co-Training for Self-Evolving LLMs via Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2610.11345)

**<font color=#1a73e8>作者：</font>** Wei Yang, Shawn Li, Yuehan Qin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving LLM agents promise to improve autonomously through continual interaction and learning, reducing their dependence on manually curated supervision. Realizing this promise requires not only updating the agent, but also evolving its training experience as its capabilities change. However, most existing pipelines rely on static datasets or separately updated synthesis models, causing previously useful tasks to become trivial while overly difficult tasks remain uninformative. This growing mismatch between agent capability and training experience limits sustained self-improvement. To address this problem, we propose SynCo, an agentic data synthesis co-training framework for self-evolving LLMs based on multi-agent reinforcement learning. SynCo jointly optimizes two independently parameterized agents: a Synthesizer that constructs training tasks from the Reasoner's evolving capability state, and a Reasoner that learns from the resulting experience. Each synthesized task induces multiple Reasoner rollouts whose outcomes provide complementary rewards to both agents. Correctness feedback improves the Reasoner, while task quality, answer reliability, and outcome-grounded teachability guide the Synthesizer. Their updates are fed back into subsequent synthesis rounds, allowing the task-solving policy and its training distribution to evolve together. Extensive experiments across eight mathematical reasoning benchmarks demonstrate that SynCo substantially outperforms a broad range of existing synthetic-data methods and controlled baselines, achieving the strongest overall performance while deriving most of its gains from previously unsolved problems.

---


### 112. [Deception by Omission: Language Models Knowingly Hide Their Mistakes](https://arxiv.org/abs/2610.11351)

**<font color=#1a73e8>作者：</font>** Lucas Florin, Amelie Knecht, Ulysse Schaller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly act as agents with little human oversight, so potential mistakes they make can go unnoticed. Users then depend on the model to report what went wrong. An honest model discloses its mistakes, while a deceptive one conceals them. However, it is unclear how current LLMs behave in such situations. In this study, we prefill LLM trajectories with synthetic mistakes. The trajectories resemble real deployments in chat and agentic settings. Models fail to disclose their mistake in 36.4% of chat and 67.1% of agentic rollouts. In 2.4% and 5.3% of rollouts, respectively, they are aware of the mistake in their chain of thought but still deceptively conceal it. Rates vary by model: for instance, Gemini 3.5 Flash knowingly conceals mistakes in up to 19.9% of agentic rollouts. In 11.9% of chat and 51.8% of agentic rollouts, models show no awareness of mistakes, even though they reliably spot them when reviewing the same transcript as an outside observer. Our results show that, as agents take on more tasks with less oversight, users cannot rely on them to self-report possible mistakes. Developers should instead use independent monitors that review agent trajectories, or specifically train models to check their past actions and disclose what they find.

---


### 113. [RL-ARC: Calibrating Large Reasoning Models via Reasoning-guided Uncertainty](https://arxiv.org/abs/2610.11352)

**<font color=#1a73e8>作者：</font>** Gukhyeon Lee, SangKeun Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models (LMs) are commonly trained with Reinforcement Learning with Verifiable Rewards (RLVR) to enhance their reasoning capabilities. However, since RLVR does not explicitly account for calibration during training, it can lead to severe calibration degradation, including overconfidence. Recent calibration-aware training methods for LMs, which incorporate objectives for uncertainty estimation into training, improve calibration but still exhibit overconfidence under distribution shift, while sacrificing reasoning performance. To this end, we propose RL-ARC, a calibration-aware training framework that jointly leverages reasoning confidence and answer confidence. Specifically, RL-ARC leverages reasoning confidence as an auxiliary signal for calibrating answer confidence, applying it as reasoning-guided regularization for correct cases and as an overconfidence penalty for incorrect cases. Comprehensive results across ID and OOD settings show that, beyond improving calibration, RL-ARC enables reasoning models to adaptively estimate confidence based on the given question without substantially sacrificing reasoning performance, thereby highlighting the importance of reasoning confidence for training reliable reasoning models.

---


### 114. [AdaptEvo: Adaptive Agent Learning with Evolving Supervision](https://arxiv.org/abs/2610.11354)

**<font color=#1a73e8>作者：</font>** Shijun Wan, Jiancong Xie, Hang Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rule-governed contextual decision tasks require models to apply specified rules to case-specific context and evidence. Written rules can leave gaps in decision guidance and process evaluation, while reference judgments vary in their support from the rules and evidence. To address these challenges, we introduce AdaptEvo, a framework for learning under imperfect supervision that couples confidence-adaptive policy optimization with evolving decision knowledge and evaluation rubrics. Its Training module uses Confidence-Adaptive GRPO (CA-GRPO) to balance outcome and process rewards according to reference confidence. Its Evolution module synthesizes reusable decision knowledge from recurring failures across training cases and refines process rubrics to detect overlooked errors. To support empirical evaluation, we construct an industrial multimodal content moderation dataset comprising a training set and In-Period and Out-of-Period test sets, with the latter collected under changed rules. Using Qwen3.6-35B-A3B, AdaptEvo achieves 61.9% exact-label accuracy and 72.2% binary decision accuracy on In-Period, exceeding GRPO by 7.5 and 3.7 percentage points, respectively. On Out-of-Period, the policy trained with CA-GRPO retains exact-label accuracy gains over the base model across evaluated checkpoints without injected decision knowledge, while GRPO declines with continued training. CA-GRPO also outperforms the tested fixed reward mixtures on both Out-of-Period metrics.

---


### 115. [Writing for the Reviewer: Defensive Writing in GPT Models](https://arxiv.org/abs/2610.11355)

**<font color=#1a73e8>作者：</font>** Junchi Liao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Researchers increasingly use ChatGPT to revise their papers, and recent GPT versions often narrow or even retract the authors' claims. We call such changes defensive writing when the given material does not support them, and we test two explanations: the model corrects the authors' overclaiming, or it writes for an anticipated reviewer. We ask GPT versions and models from other developers to rewrite paragraphs from papers written before ChatGPT, or to write from an evidence sheet that lists a paper's method and results. Defensive writing grows with GPT version. GPT-6-astra retracts the authors' claims outright, and when it writes from the evidence sheet, it still adds the most ungrounded qualifications. The results favor the anticipated-review explanation, and correcting overclaiming explains only a small part. When the models are only asked to polish, defense stays near the level of the originals; mentioning review raises it, and one round of self-review raises it further. At the same time, fewer than one in ten of the claims GPT-6-astra retracts are overstated. AI reviewers score defensive rewrites higher, while human readers find them harder to read and the authors less certain. Combining AI writing with AI review may amplify this style.

---


### 116. [RaReCache: Bridging the Gap in Cross-Model KV Cache Reuse via Rank disagreement-based Selective Recomputation](https://arxiv.org/abs/2610.11358)

**<font color=#1a73e8>作者：</font>** Sreetama Sarkar, Saptarshi Mitra, Sitao Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cross-model KV-cache reuse remains a key challenge in modern LLM serving. Coding agents and multi-model systems increasingly route a shared context across models: a user may switch models mid-session, or a cascade may escalate a difficult query. Because KV caches contain model-specific representations, each switch typically forces the receiving model to prefill the entire context from scratch. Recent work shows that closed-form linear maps can translate KV caches between models in the same family, but transfer accuracy degrades as the model-size gap widens. In this paper, we establish that these transfer failures are concentrated in a small subset of information-dense tokens. To bridge this gap, we introduce RaReCache, a framework that enables a large target model to decode accurately from a cache prefilled by a much smaller source via selective recomputation. RaReCache identifies these critical positions using a novel rank disagreement metric, scoring each token by the energy of its mapped KV in output directions weakly supported by the calibration data. Across two model families and five benchmarks, on a 23x parameter gap (Qwen3-0.6B to 14B) recomputing just 30% of positions retains 95-99% of the target accuracy, whereas on a 8.8x gap (Llama3-8B to 70B), recomputing 40% retains 96.5% of the target accuracy. RaReCache largely removes sensitivity to source-model size, and achieves up to a 3.04x prefill speedup. For online serving, it handles 1.8x the request throughput of target prefill on a single GPU, and at the target's saturation load, reduces median and 99th-percentile time-to-first-token (TTFT) by 5.0x and 6.4x respectively, with a 30% recompute budget. RaReCache establishes an efficient serving paradigm where small models prefill on behalf of massive targets, enabling large models to recompute only critical tokens, drastically reducing prefill latency.

---


### 117. [UniData: Universal Multimodal Instruction Generation Pipeline](https://arxiv.org/abs/2610.11363)

**<font color=#1a73e8>作者：</font>** Jiaqi Tang, Yi-Feng Wu, Yuting Zhang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) are increasingly being applied in a wider range of real-world scenarios. However, due to the substantial labor cost, creating high-quality multimodal instruction datasets for MLLMs remains a significant challenge. Although some methods propose to generate instruction data, they often face limitations in modality support and struggle with generating multi-round instructions. To address these problems, we introduce UniData, a universal instruction generation pipeline, to transform simple user requirements into multi-round, multimodal instructions. Specifically, UniData first expands user requirements into multiple diverse events. Using these events, UniData then integrates an any-to-any large model for multimodal instruction generation. Finally, UniData enhances data quality by correcting irrelevant and redundant inference flow, leveraging correlations between instruction rounds. To train this pipeline, we also build UniDataset, a dataset comprising 20,000 entries across nine modalities for improved multimodal generation. Our experiments demonstrate that UniData achieves SOTA performance in data quality and can also enhance the understanding and generation capabilities of other multimodal models.

---


### 118. [SpatialOPSD: Self-Distilling Spatial Intelligence from Verified Coding Agent Traces](https://arxiv.org/abs/2610.11366)

**<font color=#1a73e8>作者：</font>** Rongxue Li, Meng Yang, Yiru Mao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatial coding agents significantly improve spatial reasoning in Multimodal Large Language Models (MLLMs) by using external tools to generate verified execution traces. However, this paradigm inherently suffers from prohibitive inference-time overhead and external dependencies. In this paper, we explore whether an MLLM can internalize this agentic capability to operate entirely tool-free. We begin with a simple observation: prompting an MLLM with summarized execution traces of a spatial coding agent naturally unlocks the model's internal spatial Chain-of-Thought (CoT). Motivated by this, we introduce SpatialOPSD, an on-policy self-distillation framework that internalizes spatial reasoning into a standalone MLLM by formulating verified agent traces as privileged information. To mitigate privileged-information leakage during distillation, we introduce Repetition-Aware Distillation, which combines repetition masking with unlikelihood regularization. Experiments across multiple benchmarks demonstrate that self-distilling SpatialOPSD achieves higher average accuracy than SFT and GRPO on both spatial and OOD datasets, exhibiting superior performance and generalization.

---


### 119. [RIT-RAG: Navigating Document Corpora with Retrieval-Induced Trees](https://arxiv.org/abs/2610.11370)

**<font color=#1a73e8>作者：</font>** Meghanadh Pulivarthi, Swaraj Kumar Biswal, Kushagra Bhushan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) grounds language models in external corpora. Agentic RAG enables iterative search, yet exposes the model to isolated chunks without document structure, making it difficult to distinguish relevant evidence from chunks that merely resemble the query. Structure-aware methods such as PageIndex navigate document structure but cannot scale to the structures of large corpora, which do not fit in the LLM context. Hence, they first commit to a single document using a document retriever and cannot recover from a wrong choice. We propose RIT-RAG (Retrieval-Induced Tree RAG), which combines content retrieval with structural navigation. Offline, RIT-RAG builds a tree for each document from its table of contents or sitemap. At query time, it retrieves a broad set of chunks and uses their positions to induce manageable sub-trees, potentially across multiple documents. An LLM agent navigates these sub-trees, selectively reads promising nodes, and reformulates queries when needed. Thus, retrieval proposes where to look, while the agent decides what to read. Across financial, scientific, and customer-support benchmarks, RIT-RAG achieves the highest answer accuracy among vanilla, graph-based, and agentic baselines. On EntQABench, our new benchmark of 2.84 million technical-documentation webpages, it improves accuracy by 6.8 to 11.4 points over the strongest baseline across three LLMs.

---


### 120. [SignRAG: Unified Retrieval-Augmented Gloss-Free Sign Language Translation](https://arxiv.org/abs/2610.11371)

**<font color=#1a73e8>作者：</font>** Zhi Rao, Yucheng Zhou, Qianran Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contemporary decoder-only large language models (LLMs) have demonstrated strong capabilities across a wide range of domains. However, existing pretraining paradigms for gloss-free sign language translation (SLT) are largely designed around conventional encoder-decoder pretrained language models, which limits their direct applicability to decoder-only LLMs. To address this limitation, we propose SignRAG, a unified framework combining hierarchical pretraining, target-domain retrieval augmentation, and retrieval-aware reinforcement fine-tuning. Hierarchical pretraining first learns linguistically grounded sign representations and then jointly aligns the sign encoder with an LLM, mitigating cross-modal optimization imbalance. For downstream adaptation, SignRAG complements parameter-based fine-tuning with a target-domain retrieval gallery that provides instance-specific translation cues. To ensure that retrieved contexts are used appropriately, we further introduce Retrieval Utility-Guided Reinforcement Fine-Tuning (RUG-RFT), which combines translation-quality and retrieval-utility rewards to encourage beneficial retrieval use while suppressing harmful reliance. Experiments on multiple SLT benchmarks establish new state-of-the-art performance. In particular, to the best of our knowledge, SignRAG is the first gloss-free approach to outperform gloss-supervised methods across all reported metrics on CSL-Daily. Our code has been released at \href{this https URL}{GitHub}, together with models of different sizes to support future academic research.

---


### 121. [From a Prompt to Repertoires: Evolving Functional REpertoires Enable LLM Continual Learning](https://arxiv.org/abs/2610.11373)

**<font color=#1a73e8>作者：</font>** Fengyuan Liu, Yue Wang, Hangxi Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning remains challenging for large language models, which must enable models to acquire new skills and knowledge without degrading existing capabilities. Existing approaches typically address this challenge by carefully designing how model parameters are updated. In contrast, prompt optimization avoids costly parameter updates while achieving competitive or even superior performance to reinforcement learning methods such as GRPO on individual knowledge-intensive and reasoning tasks. This raises a natural question: \textit{Can prompt optimization, as an efficient adaptation approach, be directly applied to continual learning?} Our analysis shows that, under sequential task adaptation, it suffers from catastrophic forgetting, while optimized prompts accumulate rules that overfit to local task distributions. To address these limitations, we propose \emph{Evolving Functional REpertoires} (EFRE), which replaces a single prompt with a repertoire of functions that evolves as new tasks arrive: compatible updates refine existing functions, while conflicting updates trigger the emergence of new ones. On a three-task continual-learning stream, EFRE achieves a final average performance 7.50 percentage points higher than GRPO. Moreover, after adaptation to the Bio task, its performance on FinQA decreases by only 1.56 percentage points, compared with 25.10 percentage points for the base prompt optimization method. We further instantiate EFRE in a minimal agent system and observe consistent improvements across different backbone models. Overall, these results demonstrate EFRE's strong performance in continual learning for large language models and highlight its substantial potential for continual learning in advanced agent systems.

---


### 122. [Rethinking Contrastive Loss in CLIP Post-training: A Complementary Framework with Frozen Text Encoder](https://arxiv.org/abs/2610.11374)

**<font color=#1a73e8>作者：</font>** Zidan Wang, Yaqian Li, Xiaokai Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CLIP serves as a foundational vision-language model and the de facto vision encoder for downstream VLMs such as LLaVA. Post-training offers a lightweight route to refine CLIP, but recent work argues that the standard contrastive loss is unsuitable for post-training due to catastrophic forgetting under small batches, motivating designs that abandon the contrastive objective in favor of distillation. We revisit this premise and find that, for the InfoNCE objective, the reported forgetting is driven primarily not by insufficient negatives but by an inappropriate magnitude of the contrastive temperature $\tau$: with $\tau$ set sufficiently small, contrastive post-training improves rather than degrades the pretrained CLIP, which we explain through the temperature dependence of the InfoNCE gradient. Building on this finding, we propose \textbf{ComCLIP}, a lightweight single-epoch post-training recipe that freezes CLIP's text encoder---so the refined vision encoder is a drop-in replacement with unchanged architecture and inference cost---and trains the vision encoder with a properly-tempered contrastive loss, an MSE anchoring loss against the original CLIP, and a relational distillation loss from DINOv2. Over multiple seeds, ComCLIP matches the self-distillation baseline CLIP-Refine on zero-shot classification while significantly improving the transferability of visual features, measured by linear probing ($48.99$ vs.\ $42.28$ on ViT-B/16), and on ViT-L/14 it also improves MMVP over CLIP-Refine ($24.20$ vs.\ $19.01$); CLIP-Refine remains stronger on image-text retrieval. Used as a drop-in vision encoder for LLaVA-1.5-7B without re-aligning the projector or LLM, ComCLIP yields no net change across $8$ VLM benchmarks, i.e., the refinement does not break downstream compatibility. Code and models are available at this https URL.

---


### 123. [Personalization Matters: Long-Horizon Conversation Agent with User-Centric Information in Online Shopping Interactions](https://arxiv.org/abs/2610.11375)

**<font color=#1a73e8>作者：</font>** Rena Gao, Yue Dai, Hao Guan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Personalized conversational shopping requires maintaining preference consistency over multi-turn interactions, where users reveal constraints gradually. Existing approaches often rely on static profiles and do not explicitly control long-horizon interaction behavior. We propose a multi-agent, multimodal Retrieval-Augmented Generation (RAG) framework that decomposes dialogue state tracking, recommendation retrieval, preference-aware reasoning, and response generation, while integrating product metadata, product reviews, image-derived descriptions, and user historical reviews. To evaluate interaction-level quality, we adopt a trajectory-level protocol with four dimensions: Global Preference Consistency, Cumulative Information Synthesis, Interaction Trajectory, and Tone Consistency. On an Amazon Reviews 2023 benchmark, retrieval-enabled variants outperform a no-RAG baseline on automatic trajectory metrics (average 4.82 vs. 3.74). In a small real-user study ($n{=}5$), the Full variant achieves the highest mean overall rating (4.60 vs. 2.20 for Baseline), providing exploratory evidence that role decomposition plus user-centric retrieval improves perceived personalization.\footnote{Code and dataset are available at: this https URL

---


### 124. [Environmental Feedback Modeling Matters: Rethinking Feedback Treatment in Agentic Hindsight Self-Distillation](https://arxiv.org/abs/2610.11384)

**<font color=#1a73e8>作者：</font>** Hangxi Guo, Fengyuan Liu, Yue Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning is commonly used to train language agents in interactive environments, but cannot be directly applied when rewards are unavailable. Recent methods use environmental feedback as privileged context for hindsight self-distillation, but our analysis suggests that simply conditioning the teacher on feedback is insufficient, motivating us to rethink how environmental feedback is used in agentic self-distillation. Given that environmental feedback contains rich supervision for modeling how the environment responds to agent actions, we introduce \textit{agentic SElf-distilLation with environmental Feedback modeling} (SELF), a framework that jointly optimizes environmental feedback modeling and hindsight self-distillation. SELF learns to predict environmental responses while distilling guidance from a feedback-conditioned self-teacher into the policy. Our analysis reveals a mutually reinforcing mechanism: environmental feedback modeling strengthens hindsight supervision and policy learning, while self-distillation enhances the model's ability to model environmental feedback. With Qwen3-8B, SELF outperforms SDPO and GRPO by 6.4 and 4.1 percentage points in $\tau$-bench success rate, and by 10.71 and 3.57 percentage points in AppWorld task goal completion, respectively. These results show that SELF uses environmental feedback more effectively within agentic self-distillation, improving agent capabilities.

---


### 125. [Estimating great expectations under autoregressive language models with potentials](https://arxiv.org/abs/2610.11399)

**<font color=#1a73e8>作者：</font>** Francesco I. Re, Shubhangi Ghosh, Tim Vieira 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many applications of language models hinge not on individual samples but on the expectation of a test functional under the model. Estimating such expectations reliably can be computationally expensive. In this paper, we show how to make estimation more efficient by exploiting the next-token conditional probabilities which are available as a by-product of sampling. We do so through potentials: real-valued functions on prefixes that decompose the test functional additively. We construct an estimator whose variance depends on the chosen potential, and derive conditions under which a potential reduces this variance. We then develop practical potentials for several estimands and applications, and demonstrate substantial variance reductions across several estimands at comparable computational cost.

---


### 126. [GroundSight at GroundLM 2026 Shared Tasks: GoldenViewVQA](https://arxiv.org/abs/2610.11402)

**<font color=#1a73e8>作者：</font>** Kun Wang, Yupeng Hu, Ruping Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GoldenViewVQA requires models to jointly answer driving-scene questions and identify the camera view containing the supporting visual evidence, making precise evidence localization as important as answer correctness. We present \textbf{CoVeR-VQA}, a training-free multi-stage verification and correction framework for grounded multi-view VQA. Starting from GPT-5.6 zero-shot predictions, CoVeR-VQA progressively applies view-specific verification with Gemini-3.6-Flash, prior-guided joint verification with Claude-Opus-5, and cross-split group-level verification that exploits semantically filtered question groups from shared multi-view scenes and validation-derived prior knowledge. On the official GoldenViewVQA test set, the four-stage CoVeR-VQA pipeline achieves 84.75\% Joint Accuracy, improving the GPT-5.6 zero-shot baseline by 13.56 percentage points, while reaching 94.92\% Answer Accuracy and 86.44\% View Accuracy. The final submitted run achieves 88.14\% Joint Accuracy after two additional evaluator-informed post-hoc corrections. Our analysis shows that supporting-view localization remains the primary source of residual errors, highlighting the importance of explicit evidence verification for reliable multi-view multimodal reasoning.

---


### 127. [Cognition-Oriented Emotion Tracing from Causes to Consequences in Real-World Social Scenes](https://arxiv.org/abs/2610.11410)

**<font color=#1a73e8>作者：</font>** Hao Li, Jinye Zhang, Bobo Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Affective computing has progressed from categorical emotion recognition to open-ended affective analysis with large multimodal models. Yet affective science describes emotion as an unfolding process shaped by appraisal, regulation, and social interpretation, which remains underexplored computationally. We propose TRACE, a cognition-oriented framework that formalizes an affective episode through three interrelated stages: Condition, Affect, and Effect, integrating observable cues with cognitive factors such as internal stance and regulation of emotional display. Based on this formulation, TRACE-Bench evaluates multimodal models in real-world social scenes through five tasks spanning grounded affect recognition, regulation decoding, cause reasoning, effect reasoning, and full-chain reconstruction, with 3,746 structured question-answer pairs over 646 videos. A matched human-model comparison reveals a substantial performance gap, while affect-specialized models also generally lag behind general-purpose MLLMs. Model outputs show recurring failures, including treating displayed behavior as genuine feeling and fabricating unsupported events during long-chain generation. We further propose TRACER, a cognition-grounded structured reasoning method that couples each inference with explicit premises from factual observations, cognitive appraisals, and established upstream conclusions, forming a traceable graph of intermediate and target conclusions. TRACER outperforms all evaluated model baselines on each of the five tasks. Project page: this https URL

---


### 128. [Policy Alignment: New Signals for Membership Auditing in On-Policy Distillation](https://arxiv.org/abs/2610.11423)

**<font color=#1a73e8>作者：</font>** Yilong Yang, Wenzhuo Shang, Yule Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student model by aligning its policy with a teacher model on trajectories generated by the student model itself. Through this process, the student policy moves toward the teacher on the prompts used for distillation. However, these prompts are often private and costly, creating a need for prompt-level membership auditing. Existing methods mainly rely on likelihood-based confidence signals or student policy drift between checkpoints, but they do not capture the teacher-induced direction of the student update. In this paper, we propose Policy Alignment Membership Auditing (PAMA), a new auditing framework tailored for OPD. Our key observation is that a member prompt directly contributes to the teacher-guided policy update, while a non-member prompt only experiences indirect effects through cross-prompt generalization. Based on this directional trace, PAMA measures whether the student update moves toward reducing the teacher loss on a candidate prompt. Specifically, we introduce Teacher Alignment Gain (TAG) to estimate the teacher-aligned update direction from model outputs, and further combine it with student drift and uncertainty alignment signals for reliable membership auditing. We evaluate PAMA on six datasets and three teacher-student model families. On MATH, the primary evaluation benchmark, PAMA achieves AUC values of 0.791--0.941, improving AUC by 14.6--20.6% over state-of-the-art baselines.

---


### 129. [BioBigBird: A Sparse Attention Model for Long-Range Dependency Processing in Biomedical Text](https://arxiv.org/abs/2610.11430)

**<font color=#1a73e8>作者：</font>** Roshan Balaji, Pavan Kumar S, Vasudev Gupta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While domain-specific Large Language Models (LLMs) have encoded vast biomedical knowledge, their limited context windows often hinder a deep understanding of nuanced relationships within and across texts. To address this limitation, we introduce BioBigBird, a bidirectional language model pre-trained on extensive biomedical literature and clinical data, specifically designed to handle long-range dependencies. BioBigBird leverages a sparse attention mechanism to process sequences up to 4096 tokens, and its training incorporates a multi-stage process to mitigate noise from the large-scale pre-training corpus. We further enhance its performance by employing a multi-task learning (MTL) framework that jointly optimizes for Named Entity Recognition and Relation Extraction. Comprehensive evaluations on the BLURB benchmark reveal that our MTL-enhanced BioBigBird achieves highly competitive results against state-of-the-art models. Our work contributes an effective methodology for developing powerful, long-context language models for specialized domains, demonstrating the value of extended sequence processing for complex text analysis. Our models are publicly available at this https URL.

---


### 130. [DLC: A Metric-Guided Dynamic Loss Controller for Multi-Objective Training](https://arxiv.org/abs/2610.11433)

**<font color=#1a73e8>作者：</font>** Jaewan Ko, Janghoon Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce a metric-guided dynamic loss controller (DLC) for multi-objective image restoration. Conventional image restoration pipelines usually train with a fixed weighted combination of multiple losses, without changing the relative importance of fidelity, perceptual similarity, and no-reference quality during optimization. DLC is an architecture- and loss-term-agnostic training-time controller: it does not modify the restoration architecture or introduce new differentiable loss terms, but dynamically reweights the existing training losses. During training, DLC periodically evaluates the current model on a small fixed feedback subset and uses the resulting quality metrics to update the loss-weight vector through an LLM-based controller. Because DLC operates on existing loss terms rather than task-specific architectures, the same controller formulation can be instantiated across diverse image restoration training pipelines. We evaluate DLC on three restoration domains: low-light image enhancement, deraining, and real-world super-resolution, using both reference-based and no-reference quality metrics. Across these settings, DLC considers metric-dependent trade-offs during optimization and guides training toward balanced operating points across fidelity and perceptual quality. The results show that DLC can move models toward more favorable operating points across different restoration domains, supporting its role as a practical plug-in controller for multi-objective image restoration.

---


### 131. [Adversarial Cues in Decision Models Used as Judges: The Role of Request Presentation](https://arxiv.org/abs/2610.11436)

**<font color=#1a73e8>作者：</font>** Hongliang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An answer judge instructed to grade the final commitment should reject an explicitly wrong final value even when an earlier value matches the reference. We show that adding one colon to a candidate can violate this requirement depending on the presentation of the structured judging request. Numeric references certify the error, and paired interventions distinguish the candidate edit from the integration's presentation choices. On 200 previously unused DROP and GSM8K source clusters, the edit increased Jev's false acceptance from 1.0% to 26.0% with three output labels and from 3.0% to 26.5% with the published four-label grading instruction under sorted JSON keys. Both candidate variants were rejected under insertion presentation. These interactions passed the prespecified statistical correction even though Jev met the control thresholds under both grading configurations and presentations. Most excess acceptances occurred among candidates assigned larger numerical errors. GPT-6 Sol produced no observed cue-condition false acceptances, with missing responses unresolved. The result shows that basic judging competence can coexist with sharply different vulnerability to a fixed candidate edit across logically equivalent request presentations. The reference-aware grammar and compound ordering change limit the finding's operational scope and leave its internal cause unmeasured.

---


### 132. [Tracing the Thoughts of a Coding Agent Playing ARC-AGI-3: Lessons for Continual Learning](https://arxiv.org/abs/2610.11450)

**<font color=#1a73e8>作者：</font>** Chen Wu, Josh Passenger, Yin Song  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study how a coding agent learns across a sequence of abstract reasoning tasks. The agent runs on a frozen foundation model inside a fixed harness and acts by writing and running Python and shell scripts. It retains no state across turns other than its written artifacts, so every thought it forms, carries, corrects or abandons leaves a trace, where a thought is any belief, rule or plan committed to a file. We let the agent play ARC-AGI-3, a set of interactive reasoning games that provide no instructions. Each game is a sequence of levels, and a strategy that clears one level can fail on the next, so every new level is in effect a new task. The agent records what it learns as Python scripts and text notes, while the harness keeps a complete log of every action and observation. Our contribution is a measurement protocol that traces each thought through these files, from the task where it forms to the task where it is corrected or abandoned, applied to seven evaluation runs with three backbones from two model families. Scripts written for one task are almost never called again in a later task (33 of 630 references cross a task boundary), because most scripts embed the state of the current level. Instead, the agent rewrites its knowledge into new scripts, keeping the general rules and dropping the level-specific details, and abandons 74% of the scripts it wrote before a boundary. The notes, which only the model reads, are never revised: the agent appends without removing earlier claims, and the contradictions that accumulate are settled against the log. Because the log preserves everything, the agent forgets selectively, not catastrophically. The most costly error is a hard-coded value carried into a task where it no longer holds. These findings come from the files the agent wrote, without access to the model, and constitute a white-box analysis of how a coding agent continually learns.

---


### 133. [SAIL: Scientific Agentic Intelligence via a Science-Aware Loop](https://arxiv.org/abs/2610.11451)

**<font color=#1a73e8>作者：</font>** SAIL Model Team, Boyuan Sun, Bryan Dai 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce SAIL, an open model with 35B total and 3B active parameters for literature research, scientific coding, and multi-step research workflows. SAIL is developed through a science-aware improvement loop: agents built on frontier AI models analyze its task failures and construct training tasks that address the underlying capability gaps. The diagnosis examines search and evidence selection in literature tasks, scientific assumptions and reasoning in coding, and planning and revision in longer investigations. The agents draw on paper collections and scientific code repositories to build problems, interaction trajectories, and executable tasks with the required environments and tools. We repeat this loop over multiple development cycles and train SAIL through supervised fine-tuning, specialist training, multi-teacher on-policy distillation, and agentic reinforcement learning. SAIL achieves competitive performance across scientific research tasks with substantially fewer parameters than leading open-weight models.

---


### 134. [Generative Adversarial Loops](https://arxiv.org/abs/2610.11458)

**<font color=#1a73e8>作者：</font>** Kislay Aditya Oj, Nidhi Jain, Sri Surya Varma Datla 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI research progress can be viewed as the interaction between two processes: benchmark creation and method discovery. Historically, both were driven by human intelligence. However, recent advances in AI have accelerated automated method discovery, while automated benchmark creation has received comparatively less attention. To enable self-advancing systems, we propose Generative Adversarial Loop (GAL), a generator-discriminator framework alternating between two agentic searches: (1) a discriminator that generates adversarial data to expose weaknesses in current systems, and (2) a generator that discovers algorithms to overcome them. We apply this framework to approximation algorithms for efficient inference. Unlike existing auto research systems, which primarily focus on algorithm discovery, GAL introduces a discriminator agent that automates goalpost setting by continually searching for weaknesses in the current algorithm. We demonstrate adversarial data generation across four tasks: KV compression, sparse video generation, sparse attention, and context extension, where the discriminator identifies weaknesses in state of the art techniques. We further show that GAL enables autonomous improvement, with newly discovered algorithms improving not only on adversarially generated data, but also on established benchmarks. Specifically, GAL improves CompactorPress on KV compression with Qwen3-4B at 4x, raising performance on the discriminator dataset from 0.35 to 0.97, while also outperforming RULER-HARD (+0.77 pts). For context extension, GAL boosts Dual Chunk Attention from 0.20 to 0.90 on the discriminator dataset, while yielding gains on standard benchmarks(ScienceFiction (+6 pts) and PG19 32K (-0.33 PPL)). GAL thus provides a path toward autonomous goalpost setting and algorithmic improvement, where AI systems continually discover their own weaknesses and develop methods to overcome them.

---


### 135. [Who Verifies the Verifier? Co-Evolving Inspectable Graders with Self-Improving Agents](https://arxiv.org/abs/2610.11464)

**<font color=#1a73e8>作者：</font>** Xing Zhang, Guanghui Wang, Yanwei Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We changed the agent: did it actually get better? Every self-improving agent loop answers this hundreds of times, and every answer comes from a verifier. On open-ended tasks none exists, so the loop is handed a hand-written rubric or a bare LLM judge grading output from a model like itself, inviting reward hacking and shared blind spots. We make the verifier the evolving object: an inspectable expression over small, mostly deterministic drawback detectors, synthesized from clustered failures, gated at birth, and selected for agreement with a ten-item anchored reference set plus consensus over unlabeled outputs, never for the agent's score. On MBPP+ it gains +0.21 held-out agreement over the hand-authored seed composition, on every seed, and ends ahead of the bare LLM judge it contains. One finding should change how co-evolved verifiers are validated: removing the anchor guards collapses the verifier into a vacuous always-pass grader, yet that collapsed verifier trains skills just as well. Downstream task score cannot certify a self-evolved verifier. Score does answer sufficiency, and there an evolved verifier can substitute: Double Ratchet, pairing the verifier with a lifecycle-managed skill loop, retains 88-110% of the lift that ground truth or a rubric buys the same loop, across code generation, enterprise text-to-SQL, and reference-free report generation. When evolved skills gamed the report rubric, an outer judge caught it and one added detector repaired it; the judge itself was wrong until given the task contract.

---


### 136. [GROB: A Multi-Agent Architecture for Public-Trace Investigation of Candidate Agentic Activity](https://arxiv.org/abs/2610.11467)

**<font color=#1a73e8>作者：</font>** Chiara Bonfanti, Cataldo Basile  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present GROB, a multi-agent architecture for investigating candidate autonomous-agent activity through public Internet traces when privileged telemetry is unavailable. The system performs controlled, read-only collection of public traces and preserves selected observations for later resolution. In a frozen September 2026 corpus, several collected traces became more informative as additional public evidence emerged. The strongest result concerns Census-labelled identifiers captured on 9 September. Public revision records later resolved these identifiers to specific Census requests from 16 - 17 June. Other results show weaker links between traces collected by GROB and evidence reconstructed or reported later. These links vary in strength, and only some can be tied to specific public records. The results show that sparse public traces can remain useful even before their significance is fully understood. Such evidence can support later reconstruction, but public traces alone do not establish organizational attribution. Execution identity presents a separate problem, as continuity of agent identity remains an active research question for autonomous language-model agents.

---


### 137. [SAGE: Sink-Aware Guided Emphasis for Visual Grounding in Vision-Language Decoders](https://arxiv.org/abs/2610.11469)

**<font color=#1a73e8>作者：</font>** Jeonghyo Song, YoungJoon Yoo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent large vision-language models (VLMs) pair a visual encoder with a large language model (LLM) and perform well on diverse image-text tasks, yet their reliability is often limited by decoder attention pathologies that suppress visual evidence and exacerbate hallucinations. In this paper, we revisit visual attention sinks and uncover a structured, layer-dependent behavior: across prompts, early and late decoder layers exhibit prompt-invariant attention collapse onto the same few image regions, which we term PIS (Prompt-Invariant Sinks), whereas mid layers become prompt-conditioned and drive vision-language alignment. This split suggests that treating sinks as a uniform effect is incomplete. Building on this insight, we propose SAGE (Sink-Aware Guided Emphasis), a lightweight intervention that steers decoder attention away from PIS and toward query-dependent regions of interest (ROIs) using token-aligned ROI masks derived from standard vision backbones such as CLIP, ViT, and DINOv3. Evaluated on diverse vision-encoder + decoder-only LLM VLM families, SAGE improves visual grounding, reduces hallucinations, and yields consistent gains across public downstream vision-language benchmarks, including fine-grained visual discrimination settings where localized evidence is crucial, when instantiated with backbone-derived ROI masks.

---


### 138. [From Chain-of-Thought to Loops: Non-Autoregressive Latent Reasoning via Looped Transformers](https://arxiv.org/abs/2610.11472)

**<font color=#1a73e8>作者：</font>** Gerard Grau García, Arnau Padrés Masdemont, Niccolò Grillo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning often improves language-model performance by giving models additional computation before answering. However, explicit CoT expresses this computation as a sequence of autoregressively generated tokens. Latent reasoning replaces these tokens with compact continuous states, but most autoregressive latent-reasoning methods retain a left-to-right dependency among latent vectors. We introduce LLoCoT: a looped latent-reasoning framework that replaces left-to-right latent generation with iterative refinement of a compact latent workspace. A shared transformer is reapplied for a small number of refinement iterations, jointly updating the latent slots based on the prompt and the evolving workspace state. Using the refined state, a probabilistic head predicts a distribution from which latent tokens are sampled in parallel and used to condition an autoregressive decoder for answer generation. Training uses continuous representations derived from explicit CoT together with a final-answer prediction loss and likelihood-based supervision of the latent states. Across HumanEval and MBPP, LLoCoT achieves the highest mean among the evaluated methods, performing on par in accuracy with Reasoning SFT, our explicit-CoT baseline, while outperforming the base model, answer-only SFT and NF-CoT. Relative to Reasoning SFT, LLoCoT reduces time to the first answer token by approximately $36\times$ and reasoning-phase latency by approximately $42\times$, while increasing end-to-end throughput by $9.2\%$. This design replaces serial thought generation with parallel latent-slot refinement while retaining probabilistic latent modeling and autoregressive answer decoding.

---


### 139. [Beyond Sequences: Distilling Structured Decision Memory for LLM Recommendation](https://arxiv.org/abs/2610.11501)

**<font color=#1a73e8>作者：</font>** Leikun Liang, Guoshuai Wang, Xingsheng He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the adoption of large language models (LLMs) in recommendation systems, prevailing approaches mostly model single-type behaviors (e.g., views or purchases). Even when incorporating multiple behaviors, existing methods flatten heterogeneous actions into homogeneous token sequences, ignoring their distinct decision-making roles. This flattening fails to capture semantic hierarchies and contextual nuances in complex decision-making, such as trade-offs between price and quality. Consequently, performance degrades in critical ``difficult-choice'' scenarios involving highly similar items. To bridge this gap, we propose MARI (Memory-Augmented Recommendation with Interpretability), which grounds predictions in explicit, structured decision evidence. MARI maintains a Decision Memory Bank (DMB) that archives users' past rationales as Structured Decision Memories (SDMs): concise records of goals, constraints, and trade-offs. These SDMs are generated offline via Post-Hoc Decision Distillation from heterogeneous behaviors and user-generated content. By retrieving relevant SDMs to augment LLM reasoning, MARI achieves interpretability and scalability without the prohibitive cost of processing long raw sequences. Extensive experiments show MARI significantly outperforms state-of-the-art baselines on standard next-item prediction and a newly introduced Difficult Choice Prediction task, incurring low latency overhead by decoupling memory construction from online inference. Qualitative analyses reveal actionable, human-readable insights into user decision-making, marking a concrete step toward reasoning-aware recommendation systems.

---


### 140. [Fed-GRPO: Reward-Signal-Driven Federated Group Relative Policy Optimization](https://arxiv.org/abs/2610.11502)

**<font color=#1a73e8>作者：</font>** Pengxin Guo, Shuang Zeng, Zonggen Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown strong reasoning capabilities when fine-tuned with reinforcement learning (RL), particularly through Group Relative Policy Optimization (GRPO). However, existing GRPO methods assume centralized access to training data, which may not hold in practice due to privacy or regulatory constraints. To this end, we propose Fed-GRPO, a federated GRPO training framework that addresses these privacy constraints by enabling collaborative reasoning training without sharing raw data, which leverages the reward statistics naturally produced during GRPO training as zero-cost signals to guide aggregation, local training, and communication. Fed-GRPO contains three reward-signal-driven mechanisms: (i) \emph{signal-weighted aggregation} that weights clients by their reward standard deviation, prioritizing clients with stronger learning signals; (ii) \emph{global reward calibration} that re-weights per-prompt objectives based on the local-global reward gap, steering each client toward its relative weaknesses; and (iii) \emph{adaptive sparse communication} that allocates bandwidth based on the informativeness of each client's update. Extensive experiments on mathematical reasoning tasks demonstrate that Fed-GRPO achieves the best performance among all federated methods, clearly outperforms FedAvg and approaches centralized training performance, while losslessly reducing communication by $32\times$ and supporting up to $621\times$ compression under tight bandwidth budgets with only graceful accuracy degradation. Our code is available at this https URL.

---


### 141. [Does Modern Standard Arabic (MSA) Dominate Arabic Dialects in LLMs? A Representation-Level Analysis](https://arxiv.org/abs/2610.11510)

**<font color=#1a73e8>作者：</font>** Abdu Sallouh, Nicholas Popovič, Michael Färber  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often default to Modern Standard Arabic (MSA) when generating Arabic, even when prompted with dialectal Arabic. A natural explanation is that their internal representations are dominated by MSA. We test this hypothesis by adapting the language-dominance framework of Shani and Basirat (2025) (this https URL) to 26 Arabic varieties. Across layers and model families, we find no evidence that MSA acts as a dominant internal representation for Arabic dialects. Instead, dialect representations form a dense and highly overlapping space: normalized mutual information drops sharply compared to patterns reported for more distinct languages. Moreover, the strongest separability effects are not confined to intermediate layers, but can shift toward later layers depending on the architecture. These findings challenge a common interpretation of MSA-biased generation: output preference does not necessarily reveal internal representational dominance. Analyses of multilingual and dialectal LLMs should therefore distinguish generation bias from the geometry of internal representations.

---


### 142. [Residual Advantage: Student-Relative Teacher Guidance for RL with Verifiable Rewards](https://arxiv.org/abs/2610.11519)

**<font color=#1a73e8>作者：</font>** Xiaobing Chen, Zhiqi Pang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) and on-policy distillation (OPD) have become two main paradigms for post-training reasoning models. RLVR gives each response a single outcome label, leaving the steps inside it without separate credit. OPD provides token-level guidance at student-visited prefixes, but its pointwise signal does not directly reflect the pattern of teacher--student disagreement across the vocabulary. Dense, unbounded log-ratio supervision can amplify the teacher's influence, yet a strong solver is not necessarily a suitable guide when the student's solution paths depart from the teacher's. We propose Residual Advantage (\RA{}), which treats the teacher--student probability residual as a bounded one-step reward, subtracts the corresponding state value under the student policy to form a standard advantage, and centers the result within each response before adding it to the verifier advantage. The guidance term has zero mean within each response, so the verifier advantage remains the response's mean label and the teacher only redistributes credit among the steps within it. \CoRA{} further updates a teacher LoRA with verifier advantages on the same scored student batch and uses the updated teacher in the next iteration's residual, adapting guidance to the student's attempts. With Qwen3-1.7B-Base and Qwen3-4B-Base students and a Qwen3-8B teacher, \RA{} combined with GRPO or REINFORCE++ improves the underlying sequence-advantage algorithm in all 24 comparisons on three mathematical benchmarks, raising macro Avg@8 by 1.7--3.6 points and Pass@8 by 3.9--6.3 points. Both combinations surpass teacher-only OPD, and \CoRA{} adds a further 1.0--1.5 Avg@8 points.

---


### 143. [Design Creativity Bench: Measuring creativity in LLM-Generated UI](https://arxiv.org/abs/2610.11539)

**<font color=#1a73e8>作者：</font>** Aman Rusia, Abhijit Bhole, Prashank Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As leading LLMs improve on capability evaluations, their limitations in producing creative outputs on design tasks remain insufficiently characterised. Our work introduces Design Creativity Bench, a benchmark that evaluates diversity and appropriateness in UI designs. It measures distinctiveness among models on the same prompt (originality), how much a model's designs change between two prompts for the same UI goal in different product domains (creative range), and the share of a brief's acceptance criteria each design meets (appropriateness). Originality is 0.592 for same-prompt design pairs from different models (95% CI [0.582, 0.602]), far below the 0.764 for same-prompt human-model pairs (95% CI [0.751, 0.778]). Creative range is 0.581 across models (95% CI [0.567, 0.597]), against 0.902 for human designs (95% CI [0.884, 0.919]). Appropriateness is above 90% for every model, and the best model reaches 99.2%, slightly above the 98.0% for human designs. Our work shows that the default output of LLMs, though generally appropriate, is substantially more repetitive than the human baseline. This calls for strong measures to address the issue.

---


### 144. [Constitutional Gating and Deterministic Recovery for Multi-Agent LLM Negotiation: Ablations Against a Stateful Adversarial Gatekeeper](https://arxiv.org/abs/2610.11542)

**<font color=#1a73e8>作者：</font>** Masaaki Nakatsu, Reno Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems negotiating with a stateful counterpart waste model calls in three ways: polite loops that never meet the counterpart's hidden acceptance condition, malformed outputs that trigger retries, and compliance deadlocks in which the counterpart demands something the agent must refuse. We study a three-part control stack - a 5-Pillar runtime constitution, a 4-tier swarm (Director, three-agent majority vote, Monitor, schema hard gate) and Cognitive Annealing (deterministic deadlock detection, atomic purge of the agent-side context, a canonical recovery message) - against a released adversarial Gatekeeper whose acceptance rules are fixed regular expressions and whose LLM only renders reply text. The testbed has a known solution: it measures whether the stack executes a constitution-aligned strategy against swarm drift and recovers from deadlock, not whether it discovers anything. In five runs per configuration (30 runs; Gemini 2.5 Pro agents, Claude Haiku 4.5 Gatekeeper) we find: (i) the constitution and Director make an acceptable framing possible but not reliable - 0/5 baseline unlocks versus 1/5 and 2/5 with the constitution; when the swarm unlocks it does so in one turn with 7-8 calls and about 15k tokens (67-73% below baseline); when it does not, it costs 17-38% more; (ii) the Monitor and hard gate do not reduce unlocks and leave an audit trail; (iii) under a honeytrap-to-compliance deadlock, LLM-only steering escapes 0 of 5 times while atomic purge plus a canonical strike escapes 5 of 5 (Fisher $p = 0.008$) at the same call budget, with zero calls for the strike. LLM-written strikes failed the deterministic pre-flight 5 of 5 times although an LLM Monitor had approved four. Pre-registered hypotheses on average call and token reduction were not supported. Cost is bounded in every arm by deterministic stop rules; the stack adds recovery at no extra model cost.

---


### 145. [Learning the Loop, Not Just the Page: Execution-Grounded Loop Learning for Web Generation](https://arxiv.org/abs/2610.11543)

**<font color=#1a73e8>作者：</font>** Yuxin Meng, Ruixu Zhang, Junjie Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Functional Web generation is increasingly optimized with executable rewards, yet existing methods largely focus on the quality of the final page and leave the process of diagnosing and repairing imperfect implementations underexplored. We identify a central challenge in this setting: the Generator and Refiner produce executable artifacts with direct environment rewards, whereas the intermediate Critic influences downstream behavior without a directly executable outcome. We introduce WebLoop, an execution-grounded framework that jointly learns generation, critique, and refinement within a shared policy. WebLoop trains an execution-free Critic with complementary signals for requirement-level discriminability and downstream helpfulness, first establishing reliable diagnosis and then introducing consequence-aware credit, while all three roles are jointly optimized with group-relative policy learning. With Qwen3.5-9B, WebLoop reaches 41.5 Overall on WebRise and 38.9% accuracy on WebGen-Bench, improving the base model by 11.3 and 15.4 points, respectively. The gains transfer to first-pass generation, persist at 27B scale, and generalize from text-only training to multimodal inputs. Controlled analyses further show that the improvement cannot be explained by an additional refinement pass alone, highlighting the importance of learning the Critic and the loop itself.

---


### 146. [Prosody-to-Text: Predicting text from low-pass filtered speech](https://arxiv.org/abs/2610.11544)

**<font color=#1a73e8>作者：</font>** David Porteš, Aleš Horák  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While predicting prosody from text is an established task in the field, the opposite direction, predicting text that fits a given prosodic pattern, remains largely overlooked. We find this unfortunate, because this opposite direction could lead to some very interesting use cases. Therefore, in this paper, we make the first steps in the prosody-to-text direction by inves- tigating how much of the original sentence can be recovered from its prosodic pattern. To this end, we fine-tune the Whis- per model using only the 12 lowest Mel bins (low-pass filter with approximately 450Hz cutoff), and obtain surprisingly accurate results (WER 36%), with 10% of utterances be- ing recovered perfectly, and 40% of utterances having Word Error Rate at or below 25%. We also find that, given the correct prefix, the next token was predicted correctly in 79% of cases. Our results suggest that the relationship between low-frequency speech features and lexical content is much stronger than previously thought, and we believe that direct- ing more attention to this topic might open the door to new applications, such as using prosody to guide text generation of modern LLMs

---


### 147. [Conditional Transfer from Controlled Pretraining Mixtures to Code](https://arxiv.org/abs/2610.11548)

**<font color=#1a73e8>作者：</font>** Ohad Rubin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic tasks are increasingly used both as probes of language-model capability and as pretraining data. Both uses are often justified by loss reduction: falling loss is treated as informative, and faster loss reduction with more sampling as evidence that a task is worth sampling. We separate three signals. A task is diagnostic when its loss tracks global pretraining progress; it is teachable when its loss responds to its own token budget; and a data source transfers when including it improves a downstream target. We study controlled pretraining in which 70% of the corpus is fixed general Python and the remaining 30% is a simplex over three source families: OpenCodeInstruct, a curated suite of 12 code-adjacent synthetic tasks, and 15 literature-derived probe tasks. Across a task-budget sweep we detect teachability for 14 of 27 tasks, with a sharp asymmetry between the two synthetic families (10/12 curated versus 4/15 literature-derived).
Teachability and downstream transfer give different rankings. On the mixture-simplex edge between the curated suite and OpenCodeInstruct, HumanEval pass@20 after a fixed fine-tuning stage rises from 15.9 at pure curated data to its highest observed value, 22.6, at a mixture that is 75% OpenCodeInstruct, then falls to 19.5 at pure OpenCodeInstruct. Curated synthetic data therefore has conditional value: it contributes as a limited share of a mixture that a target-aligned source still dominates. Finally, a loss-based adaptive scheduler exposes the mismatch between residual loss reducibility and downstream transfer. Across three 60k-step free-ratio runs, Ado drives the OpenCodeInstruct share below 5% within the first 5k steps and to 1.2--1.4% by the end of training, and underperforms its matched fixed-mixture controls by 2.4--11.0 percentage points. Optimizing near-term task-loss reduction moves the mixture away from the region that transfers.

---


### 148. [SoK: Are LLMs Reliable at Source Code Recovery? A Taxonomy and Empirical Evaluation](https://arxiv.org/abs/2610.11556)

**<font color=#1a73e8>作者：</font>** Varun Kohli, Lee Bing Cheng, Nur Hazim Ghazali 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Effective source recovery is critical to security applications such as malware analysis, vulnerability assessment, and legacy maintenance. Large Language Models (LLMs) are reshaping this field, shifting the paradigm away from rule-based heuristics to probabilistic and high fidelity semantic recovery of source code from assembly or classical decompiler-derived pseudo-C. However, despite rapid progress, the field suffers from fragmentation across numerous approaches as well as their non-unified evaluations, limiting objective comparisons. Further, existing works have limited coverage of embedded, IoT architectures and source languages beyond C/C++. In this work, we present the first Systematization of Knowledge (SoK) focused specifically on LLM-assisted binary-to-source recovery. We provide a granular design-centric taxonomy of LLM-assisted source recovery methods and systematic evaluations using seven key metrics along six evaluation dimensions. We evaluate state-of-the-art methods on 45,000 test samples derived from four standard and five embedded architectures, five optimization levels, and symbol stripping. We ablate the impact of design choices on recovery performance, including input representation, contextual enrichment, model scale, iteration and review roles using controlled in-house recovery pipelines and three off-the-shelf models. Finally, we test same-language and cross-language recovery capability covering four mature and two legacy languages. Our systematization and comprehensive evaluations provide key insights that guide future directions in this field.

---


### 149. [SWE-Journey: Towards More Realistic Evaluation of Coding Assistants through Long-Horizon, Multi-Turn Interaction](https://arxiv.org/abs/2610.11559)

**<font color=#1a73e8>作者：</font>** Hexuan Deng, Yue Wang, Wenyu Jiang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Coding assistants such as Claude Code and Codex have become a major application of LLM agents, yet existing benchmarks remain far from real-world use, particularly in task horizon and interaction length. Code assistants require completing long chains of development work in continuously evolving repositories, while repeatedly clarifying requirements and adapting implementations through multi-turn interaction. To address these gaps, we introduce SWE-Journey, a benchmark for more realistic evaluation of coding assistants. To address the task-horizon gap, we propose a weak-to-strong synthesis pipeline that automatically constructs long-horizon coding tasks. To address the interaction gap, we mine four representative user personas from real interaction data and build a user-simulation agent to reproduce realistic code-assistance interactions. On average, models pass over 75% of tests for requested functionality with software architects, but fewer than 25% with non-coders. These results show that current coding assistants still fall short of enabling reliable coding for non-coders. We further analyze the reasons for this gap and identify asking right, finding right, and fixing right as key capabilities during interaction.

---


### 150. [Workerville: Towards an Organizational Behavior Account of Agent Safety](https://arxiv.org/abs/2610.11561)

**<font color=#1a73e8>作者：</font>** Hanjun Luo, Junting Mao, Yuhan Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents now interact with their environments continuously, shaped by such organizational channels as user instructions, peer messages, and long-term memory. Existing safety research has examined these influences, but largely as separate agent components. How such factors jointly shape an agent's safety behavior from a unified perspective remains unmeasured. To bridge this gap, we advocate organizational behavior (OB) as a framework for studying the safety of advanced agents, reorganizing the objects of study, theoretical foundations, and experimental design around the relational structure in which agents operate. We present the first systematic formalization of counterproductive work behavior (CWB), a canonical safety-relevant subfield of OB, as Agentic Counterproductive Behavior (ACB). ACB specifies three organizational antecedents (vertical supervisor relations, horizontal peer norms, and internal cognitive structures) and maps them onto three counterproductive outcome dimensions (unauthorized disclosure, destructive operations, and production deviation). To operationalize ACB, we introduce Workerville, a controlled benchmark that manipulates organizational conditions over shared tasks, applying 16 organizational configurations to 210 tasks to yield 3,360 challenges, evaluated by human-validated agentic judges. Benchmarking 6 frontier LLMs, we find that (I) negative organizational antecedents exhibit non-monotonic amplification when combined, with the unauthorized-disclosure rate rising from 16.5% under no negative antecedent to 60.1% under two and falling back to 50.3% under three; (II) agents reproduce typical behavioral patterns predicted by human CWB research; (III) these results establish OB as a systematic framework for agent safety research, pointing toward a new research agenda.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-288](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
