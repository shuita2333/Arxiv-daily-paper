# 🧠 大模型相关研究 | 2026年05月18日

> 本类共 **165** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-165](./part-04.md)

---

### 101. [Breaking Dual Bottlenecks: Evolving Unified Multimodal Models into Self-Adaptive Interleaved Visual Reasoners](https://arxiv.org/abs/2605.14709)

**<font color=#1a73e8>作者：</font>** Qingyang Liu, Bingjie Gao, Canmiao Fu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent unified models integrate multimodal understanding and generation within a single framework. However, an "understanding-generation gap" persists, where models can capture user intent but often fail to translate this semantic knowledge into precise pixel-level manipulation. This gap results in two bottlenecks in anything-to-image task (X2I): the attention entanglement bottleneck, where blind planning struggles with complex prompts, and the visual refinement bottleneck, where unstructured feedback fails to correct imperfections efficiently. In this paper, we propose a novel framework that empowers unified models to autonomously switch between generation strategies based on instruction complexity and model capability. To achieve this, we construct a hierarchical data pipeline that constructs execution paths across three adaptive modes: direct generation for simple cases, self-reflection for quality refinement, and multi-step planning for decomposing complex scenarios. Building on this pipeline, we contribute a high-quality dataset with over 50,000 samples and implement a two-stage training strategy comprising SFT and RL. Specifically, we design step-wise reasoning rewards to ensure logical consistency and intra-group complexity penalty to prevent redundant computational overhead. Extensive experiments demonstrate that our method outperforms existing baselines on X2I, achieving superior generation fidelity among simple-to-complex instructions. The code is released at this https URL.

---


### 102. [Vision-Core Guided Contrastive Learning for Balanced Multi-modal Prognosis Prediction of Stroke](https://arxiv.org/abs/2605.14710)

**<font color=#1a73e8>作者：</font>** Liren Chen, Lidong Sun, Mingyan Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning and multi-modal fusion have demonstrated transformative potential in medical diagnosis by integrating diverse data sources. However, accurate prognosis for ischemic stroke remains challenging due to limitations in existing multi-modal approaches. First, current methods are predominantly confined to dual-modal fusion, lacking a framework that effectively integrates the trifecta of medical images, structured clinical data, and unstructured text. Second, they often fail to establish deep bidirectional interactions between modalities; To address these critical gaps, this paper proposes a novel tri-modal fusion model for ischemic stroke prognosis. Our approach first enriches the data representation by employing a Large Language Model (LLM) to automatically generate semi-structured diagnostic text from brain MRIs. This process not only addresses the scarcity of expert annotations but also serves as a regularized semantic enhancement, improving multimodal fusion robustness. Furthermore, we design a core component termed the Vision-Conditioned Dual Alignment Fusion Module (VDAFM), which strategically uses visual features as a conditional prior to guide fine-grained interaction with the generated text. This module achieves a dynamic and profound fusion through a dual semantic alignment loss, effectively mitigating modal heterogeneity. Extensive experiments on a real-world clinical dataset demonstrate that our model achieves state-of-the-art performance.

---


### 103. [Agentifying Patient Dynamics within LLMs through Interacting with Clinical World Model](https://arxiv.org/abs/2605.14723)

**<font color=#1a73e8>作者：</font>** Minghao Wu, Yuting Yan, Zhenyang Cai 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sepsis management in the ICU requires sequential treatment decisions under rapidly evolving patient physiology. Although large language models (LLMs) encode broad clinical knowledge and can reason over guidelines, they are not inherently grounded in action-conditioned patient dynamics. We introduce SepsisAgent, a world model-augmented LLM agent for sepsis treatment recommendation. SepsisAgent uses a learned Clinical World Model to simulate patient responses under candidate fluid--vasopressor interventions, and follows a propose--simulate--refine workflow before committing to a prescription. We first show that world-model access alone yields inconsistent LLM decision performance, motivating agent-specific training. We then train SepsisAgent through a three-stage curriculum: patient-dynamics supervised fine-tuning, propose--simulate--refine behavior cloning, and world-model-based agentic reinforcement learning. On MIMIC-IV sepsis trajectories, SepsisAgent outperforms all traditional RL and LLM-based baselines in off-policy value while achieving the best safety profile under guideline adherence and unsafe-action metrics. Further analysis shows that repeated interaction with the Clinical World Model enables the agent to learn regularities in patient evolution, which remain useful even when simulator access is removed.

---


### 104. [EARL: Towards a Unified Analysis-Guided Reinforcement Learning Framework for Egocentric Interaction Reasoning and Pixel Grounding](https://arxiv.org/abs/2605.14742)

**<font color=#1a73e8>作者：</font>** Yuejiao Su, Xinshen Zhang, Zhen Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding human--environment interactions from egocentric vision is essential for assistive robotics and embodied intelligent agents, yet existing multimodal large language models (MLLMs) still struggle with accurate interaction reasoning and fine-grained pixel grounding. To this end, this paper introduces EARL, an Egocentric Analysis-guided Reinforcement Learning framework that explicitly transfers coarse interaction semantics to query-oriented answering and grounding. Specifically, EARL adopts a two-stage parsing framework including coarse-grained interpretation and fine-grained response. The first stage holistically interprets egocentric interactions and generates a structured textual description. The second stage produces the textual answer and pixel-level mask in response to the user query. To bridge the two stages, we extract a global interaction descriptor as a semantic prior, which is integrated via a novel Analysis-guided Feature Synthesizer (AFS) for query-oriented reasoning. To optimize heterogeneous outputs, including textual answers, bounding boxes, and grounding masks, we design a multi-faceted reward function and train the response stage with GRPO. Experiments on Ego-IRGBench show that EARL achieves 65.48% cIoU for pixel grounding, outperforming previous RL-based methods by 8.37%, while OOD grounding results on EgoHOS indicate strong transferability to unseen egocentric grounding scenarios.

---


### 105. [Mechanical Enforcement for LLM Governance:Evidence of Governance-Task Decoupling in Financial Decision Systems](https://arxiv.org/abs/2605.14744)

**<font color=#1a73e8>作者：</font>** José Manuel de la Chica Rodríguez, Carlos Martí-González  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models in regulated financial workflows are governed by natural-language policies that the same model interprets, creating a principal--agent failure: outputs can appear compliant without being compliant. Existing evaluation measures task accuracy but not whether governance constrains behaviour at the decision rationale level -- where regulated decisions must be auditable. We introduce five governance metrics that quantify policy compliance at the rationale level and apply them in a synthetic banking domain to compare text-only governance against mechanical enforcement: four primitives operating outside the model's interpretive loop. Under text-only governance, 27% of deferrals carry no decision-relevant information. Mechanical enforcement reduces this rate by 73%, more than doubles deferral information content, and raises task accuracy from MCC~$0.43$ to $0.88$. The improvement is driven by architectural separation: LLM-generated rationales under mechanical enforcement show comparable CDL to text-only governance -- the gain comes from removing clear-cut decisions from the model's control. A causal ablation confirms that each primitive is individually necessary. Our central finding is a governance-task decoupling: under structural stress, text-only governance degrades on both dimensions simultaneously, whereas mechanical enforcement preserves governance quality even as task performance drops. This implies that governance and task evaluation are distinct axes: accuracy is not a sufficient proxy for governance in regulated AI systems.

---


### 106. [Video2GUI: Synthesizing Large-Scale Interaction Trajectories for Generalized GUI Agent Pretraining](https://arxiv.org/abs/2605.14747)

**<font color=#1a73e8>作者：</font>** Weimin Xiong, Shuhao Gu, Bowen Ye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in multimodal large language models have driven growing interest in graphical user interface (GUI) agents, yet their generalization remains constrained by the scarcity of large-scale training data spanning diverse real-world applications. Existing datasets rely heavily on costly manual annotations and are typically confined to narrow domains. To address this challenge, we propose Video2GUI, a fully automated framework that extracts grounded GUI interaction trajectories directly from unlabeled Internet videos. Video2GUI employs a coarse-to-fine filtering strategy to identify high-quality GUI tutorial videos and convert them into structured agent trajectories. Applying this pipeline to 500 million video metadata entries, we construct WildGUI, a large-scale dataset containing 12 million interaction trajectories spanning over 1,500 applications and websites. Pre-training Qwen2.5-VL and Mimo-VL on WildGUI yields consistent improvements of 5-20% across multiple GUI grounding and action benchmarks, matching or surpassing state-of-the-art performance. We will release both the WildGUI dataset and the Video2GUI pipeline to support future research of GUI agents.

---


### 107. [Non-linear Interventions on Large Language Models](https://arxiv.org/abs/2605.14749)

**<font color=#1a73e8>作者：</font>** Sangwoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Intervention is one of the most representative and widely used methods for understanding the internal representations of large language models (LLMs). However, existing intervention methods are confined to linear interventions grounded in the Linear Representation Hypothesis, leaving features encoded along non-linear manifolds beyond their reach. In this work, we introduce a general formulation of intervention that extends naturally to non-linearly represented features, together with a learning procedure that further enables intervention on implicit features lacking a direct output signature. We validate our framework on refusal bypass steering, where it steers the model more precisely than linear baselines by intervening on a non-linear feature governing refusal.

---


### 108. [AI Outperforms Humans in Personalized Image Aesthetics Assessment via LLM-Based Interviews and Semantic Feature Extraction](https://arxiv.org/abs/2605.14761)

**<font color=#1a73e8>作者：</font>** Yoshia Abe, Tatsuya Daikoku, Yasuo Kuniyoshi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurately predicting individual aesthetic evaluation for images is a fundamental challenge for AI. Various deep learning (DL)-based models have been proposed for this task, training on image evaluation data to extract objective low-level features. However, aesthetic preferences are inherently subjective and individual-dependent. Accurate prediction thus requires the extraction of high-level semantic features of images and the active collection of preference information from the target individual. To address this issue, we focus on the utility of Large Language Models (LLMs) pretrained on vast amounts of textual data, and develop an integrated DL-LLM system. The system actively elicits aesthetic preferences through LLM-based semi-structured interviews and predicts aesthetic evaluation by leveraging both low-level and high-level features. In our experiments, we compare the proposed system against conventional systems, human predictors, and the target individual's own re-evaluations after a certain time interval. Our results show that the proposed system outperforms all of them, with particularly strong performance on highly-rated images. Moreover, the prediction error of the proposed system is smaller than within-person variability, while human predictors show the largest error, likely due to the influence of their own aesthetic values. These results suggest that AI may be better positioned than others or one's future self to capture individual aesthetic preferences at a given point. This opens a new question of whether AI could serve as a deeper interpreter of human aesthetic sensibility than humans themselves.

---


### 109. [Streaming Speech-to-Text Translation with a SpeechLLM](https://arxiv.org/abs/2605.14766)

**<font color=#1a73e8>作者：</font>** Titouan Parcollet, Shucong Zhang, Xianrui Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Normally, a system that translates speech into text consists of separate modules for speech recognition and text-to-text translation. Combining those tasks into a SpeechLLM promises to exploit paralinguistic information in the speech and to reduce cascaded errors. But existing SpeechLLM systems are slow since they do not work in a real streaming fashion: they wait for a complete utterance of audio before outputting a translation, or output tokens at fixed intervals, which is not suitable for real applications. This work proposes an LLM-based architecture for real streaming speech-to-text translation. The LLM learns not just to emit output tokens, but also to decide whether it has seen enough audio to do so. The system is trained using automatic alignments of the input speech and the output text. In experiments on different language pairs, the system achieves a translation quality close to the non-streaming baseline, but with a latency of only 1-2 seconds.

---


### 110. [MediaClaw: Multimodal Intelligent-Agent Platform Technical Report](https://arxiv.org/abs/2605.14771)

**<font color=#1a73e8>作者：</font>** Shaoan Zhao, Huanlin Gao, Qiang Hui 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> MediaClaw is a multimodal agent platform built on the OpenClaw ecosystem. Its core design follows a three-layer architecture of unified abstraction, pluginized extension, and workflow orchestration. The system is intended to address practical deployment pain points in AIGC adoption, including fragmented capabilities, heterogeneous interfaces, disconnected production processes, and limited reuse of high-quality production workflows. \system{} abstracts full-category AIGC capabilities into a unified invocation model, uses plugins to support hot-pluggable capability expansion, and uses task-oriented Skills to turn complex production processes into reusable workflow assets. This report focuses on the architectural design philosophy of MediaClaw, the design logic of its core capability model, and the key engineering trade-offs in implementation. It aims to provide reusable practical reference for building multimodal capability platforms.

---


### 111. [Do Composed Image Retrieval Benchmarks Require Multimodal Composition?](https://arxiv.org/abs/2605.14787)

**<font color=#1a73e8>作者：</font>** Matteo Attimonelli, Alessandro De Bellis, Aryo Pradipta Gema 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Image Retrieval (CIR) is a multimodal retrieval task where a query consists of a reference image and a textual modification, and the goal is to retrieve a target image satisfying both. In principle, strong performance on CIR benchmarks is assumed to require multimodal composition, i.e., combining complementary information from reference image and textual modification. In this work, we show that this assumption does not always hold. Across four widely used CIR benchmarks and eleven Generalist Multimodal Embedding models, a large fraction of queries can be solved using a single modality (from 32.2% to 83.6%), revealing pervasive unimodal shortcuts. Thus, high CIR performance can arise from unimodal signals rather than true multimodal composition. To better understand this issue, we perform a two-stage audit. First, we identify shortcut-solvable queries through cross-model analysis. Second, we conduct human validation on 4,741 shortcut-free queries, of which only 1,689 are well-formed, with common issues including ambiguous edits and mismatched targets. Re-evaluating models on this validated subset reveals qualitatively different behaviour: queries can no longer be solved with a single modality, and successful retrieval requires combining both inputs. While accuracy decreases, reliance on multimodal information increases. Overall, current CIR benchmarks conflate shortcut-solvable, noisy, and genuinely compositional queries, leading to an overestimation of model capability in multimodal composition.

---


### 112. [Graphs of Research: Citation Evolution Graphs as Supervision for Research Idea Generation](https://arxiv.org/abs/2605.14790)

**<font color=#1a73e8>作者：</font>** Songyang Gao, Yinghui Xia, Siyi Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Research idea generation is the innovation-driving step of automated scientific research. Recently, large language models (LLMs) have shown potential for automating idea generation at scale. However, existing methods mainly condition LLMs on eliciting idea generation through static retrieval of relevant literature or complex prompt engineering, without discarding the structural relations among references. We propose Graphs of Research (GoR), a supervised fine-tuning method that extracts a 2-hop reference neighborhood for each seed paper, derives the relations among those references from citation position, frequency, predecessor links, and publication time, and organizes them into a paper-evolution directed acyclic graph (DAG). We construct an automated extraction pipeline that draws data from five major ML/NLP venues, comprising 498/50/50 train/validation/test seed papers and approximately 7,600 cited references. Qwen2.5-7B-Instruct-1M is fine-tuned on a structured-text prompt that includes the citation graph, edge signals, reference information, and task definition to predict the idea for the seed paper. Across head-to-head LLM-judge tournaments against gpt-4o-driven baselines, GoR-SFT achieves SOTA, demonstrating the effectiveness of citation-evolution graphs as supervision signal for LLM-based idea generation. We hope that this reduces the barrier for citation evolution graphs as a supervision, accelerating automated scientific innovation.

---


### 113. [COAL: Counterfactual and Observation-Enhanced Alignment Learning for Discriminative Referring Multi-Object Tracking](https://arxiv.org/abs/2605.14795)

**<font color=#1a73e8>作者：</font>** Shukun Jia, Shiyu Hu, Yipei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring Multi-Object Tracking (RMOT) faces a fundamental structural contradiction between the high-discriminability demand and the sparse semantic supervision. This mismatch is particularly acute in highly homogeneous scenarios that require fine-grained discrimination over complex compositional semantics. However, under sparse supervision, models overfit to salient yet insufficient cues, thereby encouraging shortcut learning and semantic collapse. To resolve this, we propose COAL (Counterfactual and Observation-enhanced Alignment Learning), a framework that advances RMOT beyond isolated structural optimization through knowledge regularization. First, we introduce Explicit Semantic Injection (ESI) via a VLM to densify the observation space and enhance instance discriminability. Second, leveraging LLM reasoning, we propose Counterfactual Learning (CFL) to augment supervision, enforcing strict attribute verification for robust compositional recognition. These strategies are unified within a Hierarchical Multi-Stream Integration (HMSI) architecture, which distills external knowledge into domain-specific discriminative representations. Experiments on Refer-KITTI and Refer-KITTI-V2 benchmarks validate COAL's efficacy. Notably, it surpasses the state-of-the-art by 7.28% HOTA on the highly challenging Refer-KITTI-V2. These results demonstrate the effectiveness of knowledge regularization for resolving the sparsity-discriminability paradox in RMOT.

---


### 114. [A Heterogeneous Temporal Memory Governance Framework for Long-Term LLM Persona Consistency](https://arxiv.org/abs/2605.14802)

**<font color=#1a73e8>作者：</font>** Zhao Yang, Wang Huan, Li Yingshuo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models often suffer from fact loss, timeline confusion, persona drift, and reduced stability during long-range interaction, especially under high-noise knowledge bases, context clearing, and cross-model transfer. To address these issues, we introduce ARPM, an external temporal memory governance framework for long-term dialogue. ARPM separates static knowledge memory from dynamic dialogue experience memory and combines vector retrieval, BM25, RRF fusion, dual-temporal reranking, chronological evidence reading, and a controlled analysis protocol for evidence verification and answer binding. Unlike approaches that encode persona consistency into model weights or rely only on long context, ARPM treats continuity as a traceable, auditable, and transferable governance problem. Using engineering logs, we conduct three experiments. First, in a 50-round question-answering setting, we compare signal-to-noise ratios of 1:5 and 1:200+, and distinguish CSV auto-judgment from manual review. Under 1:5, CSV recall accuracy is 54.0%, while manual review raises it to 100.0%. Under 1:200+, the values are 44.0% and 80.0%. These results show that automatic rules can underestimate recall after supporting evidence enters the prompt. Second, ablation results show that dialogue history retrieval is necessary for recent continuity: disabling it reduces strict accuracy from 100% to 66.7%, and disabling BM25 reduces it to 80.0%, indicating that pure semantic retrieval is insufficient for correction and tracing. Third, under a 5.1-million-character noise substrate, periodic context clearing, and multi-model handoff, ARPM maintains semantic continuity, boundary continuity, and persona consistency, while exposing limits caused by weak protocol compliance. These findings show that long-term persona consistency can be decomposed into governable components and evaluated in a white-box manner.

---


### 115. [GFMate: Empowering Graph Foundation Models with Test-time Prompt Tuning](https://arxiv.org/abs/2605.14809)

**<font color=#1a73e8>作者：</font>** Yan Jiang, Ruihong Qiu, Zi Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph prompt tuning has shown great potential in graph learning by introducing trainable prompts to enhance the model performance in conventional single-domain scenarios. Recent research has extended graph prompts to improve Graph Foundation Models (GFMs) by few-shot tuning auxiliary prompts. Despite their progress, most existing methods embed source-domain information into prompts, which serve either as input to GFMs or encoded during model pre-training. Such prompt entanglement with specific source domains and GFM pre-training strategy restricts their generalisability to other domains and different GFMs. Furthermore, existing GFM prompts merely rely on few-shot tuning for adaptation, neglecting the rich information in unlabelled target domain test data. Motivated by these insights, this paper aims to empower GFMs with pre-training-agnostic test-time graph prompt tuning, named GFMate. GFMate introduces centroid and layer prompts applied after pre-training on target domains, avoiding entanglement with specific source domains and model pre-training. In addition, a test-time complementary learning objective is devised to exploit both labelled and unlabelled target domain data for effective test-time prompt tuning. Extensive experiments on 12 benchmark datasets demonstrate the superior performance and efficiency of GFMate, achieving improvements of up to 30.63%. Code is available at this https URL.

---


### 116. [Agentic AI and Human-in-the-Loop Interventions: Field Experimental Evidence from Alibaba's Customer Service Operations](https://arxiv.org/abs/2605.14830)

**<font color=#1a73e8>作者：</font>** Yiwei Wang, Chuan Zhu, Tianjun Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems that autonomously perform service tasks are entering customer service operations. However, limited evidence exists on how human interventions shape service outcomes when agentic AI failures create both cognitive and emotional consequences. We study this issue through a randomized field experiment on Alibaba's Taobao platform. Workers in the treatment condition supervised an agentic AI system that resolved AI-eligible chats while continuing to handle AI-ineligible chats, whereas control workers resolved all chats without agentic AI. The findings show that AI deployment reduces average chat duration and has limited effects on retrial rates, but substantially lowers ratings for AI-eligible chats. Moreover, human intervention effectiveness in AI-eligible chats depends on the nature of AI failure, post-escalation intervention effort, and intervention timing. Human intervention preserves service quality in algorithm-triggered technical escalations, i.e., unresolved customer issues beyond the AI's capability, but is less effective in algorithm-triggered emotional escalations, i.e., where customers express frustration or dissatisfaction. These differences are partly explained by variation in workers' post-escalation intervention effort across escalation types. In algorithm-triggered emotional escalations, workers showed lower engagement: they sent fewer messages, contributed a smaller share of total chat rounds, and showed less proactivity in information seeking and solution provision. We further find that early intervention is essential for sustaining high post-escalation intervention effort. Finally, we document a positive spillover effect on AI-ineligible chats, as treated workers adapted their multitasking workflow to devote greater attention to these chats. These findings offer implications for human-in-the-loop process design in human-AI collaboration systems.

---


### 117. [In-Context Learning for Data-Driven Censored Inventory Control](https://arxiv.org/abs/2605.14840)

**<font color=#1a73e8>作者：</font>** Sohom Mukherjee, Anh-Duy Pham, Richard Pibernik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study inventory control with decision-dependent censoring, focusing on the censored or repeated newsvendor (R-NV), where each order quantity determines whether demand is fully observed or censored by sales. Existing approaches based on parametric Thompson sampling (TS) can be brittle under prior mismatch, while offline imputation methods need not transfer to online learning. Motivated by the predictive view of decision making, we combine these ideas by taking oracle actions on learned completions of latent demand. We propose in-context generative posterior sampling (ICGPS), which uses modern generative models that are meta-trained offline and deployed online by in-context autoregressive generation. Theoretically, we show that the Bayesian regret of ICGPS with a learned completion kernel is bounded by the Bayesian regret of a TS benchmark with the ideal completion kernel plus a deployment penalty scaling as $\sqrt{T}$ times the square root of the completion mismatch. This yields a plug-in template for operational problems with known TS regret bounds. For R-NV, we derive sublinear Bayesian regret by reducing censored feedback to bandit convex optimization feedback. We also show that, under reasonable coverage and stability assumptions, the online completion mismatch is controlled by the offline censored predictive mismatch, so offline predictive quality transfers to online performance. Practically, we instantiate ICGPS with ChronosFlow, which combines a frozen time-series transformer backbone with a trainable conditional normalizing-flow head for fast censoring-consistent sampling. In benchmark experiments, ChronosFlow-ICGPS matches correctly specified TS, outperforms myopic and UCB-style baselines, and is robust to prior mismatch and distribution shift. ChronosFlow-ICGPS also performs well for the real-world SuperStore dataset, especially under heavy censoring.

---


### 118. [GPart: End-to-End Isometric Fine-Tuning via Global Parameter Partitioning](https://arxiv.org/abs/2605.14841)

**<font color=#1a73e8>作者：</font>** Paolo Mandica, Michał Brzozowski, Zuzanna Dubanowska 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) has become the dominant paradigm for parameter-efficient fine-tuning (PEFT) of large language models (LLMs). However, its bilinear structure introduces a critical limitation: the mapping from trainable parameters to weight updates is not distance-preserving, distorting the optimization landscape. Methods that project a low-dimensional vector into LoRA's parameter space, such as Uni-LoRA, improve parameter efficiency, but the subsequent bilinear LoRA map breaks end-to-end isometry, leaving the core distance-preservation problem unresolved. We propose GPart (Global Partition fine-tuning), a highly parameter-efficient fine-tuning method which removes the low-rank bottleneck entirely. Our method uses a single isometric partition matrix to map a $d$-dimensional trainable vector directly into the full weight space of the model. The result is an extremely minimal fine-tuning pipeline: one random projection, end-to-end isometric, with a single clean hyperparameter ($d$) and storage cost of $d+1$ values (the trainable vector plus a random seed). GPart builds on the theoretical premise that effective fine-tuning can emerge from random low-dimensional subspaces of the full weight space, without imposing low-rank matrix structure. We empirically demonstrate the superior or comparable performance of GPart to existing PEFT methods on natural language understanding, computer vision tasks, and mathematical reasoning. Overall, GPart achieves state-of-the-art efficiency and performance by removing structural constraints, offering a straightforward and elegant path to PEFT.

---


### 119. [XFP: Quality-Targeted Adaptive Codebook Quantization with Sparse Outlier Separation for LLM Inference](https://arxiv.org/abs/2605.14844)

**<font color=#1a73e8>作者：</font>** Thomas Witt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce XFP, a dynamic weight quantizer for LLM inference that inverts the conventional workflow: the operator specifies reconstruction quality floors on per-channel cosine similarity (one strict floor for attention and shared experts, one lazy floor for routed-expert MoE); XFP determines codebook size, outlier budget, and packing per layer automatically -- no Hessian, no calibration data, no manual bit-width selection. Each weight matrix is decomposed into a sparse fp16 outlier residual and a dense sub-byte index tensor into a per-group learned codebook. Two storage modes share one auto-select frontend and one fused decode kernel: V2 (per-channel Lloyd) and V2a (shared library of L=32 codebooks per layer). On Qwen3.5-122B-A10B under V2, XFP reaches 138 tok/s single-stream decode on workstation hardware (RTX PRO 6000 Blackwell, TP=2) at 94.49% GSM8K strict-match (3 seeds, n=3957), and is 49% faster than Marlin INT4 at TP=1. For models that do not fit in the target memory envelope, we present the H-Process: a quality-driven iteration over the two cosine thresholds that finds the operating point at which the model just fits while still producing sensible output. Three constraints define its search space: the operator-set thresholds, an OOM boundary at quantize-on-load, and a garbage boundary in generation (cosine similarity steers; benches verify). On Qwen3.5-397B-A17B (512 routed experts/layer), the H-Process fits the full expert population into 2x96 GB at ~3.4 effective bits and delivers 100.9 tok/s long-output decode at 66.72% GSM8K strict-match on the full 1319-problem set (single seed at submission; multi-seed evaluation in progress), exceeding INT4 with routed-expert pruning on memory, throughput, and accuracy simultaneously.

---


### 120. [Exploring Vision-Language Models for Online Signature Verification: A Zero-Shot Capability Study](https://arxiv.org/abs/2605.14845)

**<font color=#1a73e8>作者：</font>** Marta Robledo-Moreno, Ruben Vera-Rodriguez, Ruben Tolosana 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Vision-Language Models (VLMs) have demonstrated strong capabilities in general visual reasoning, yet their applicability to rigorous biometric tasks remains unexplored. This work presents an exploratory study evaluating the zero-shot performance of state-of-the-art VLMs (GPT-5.2 and Gemini 2.5 Pro) on the Signature Verification Challenge (SVC) benchmark. To enable visual processing, raw kinematic time-series are converted into static images, encoding pressure information into stroke opacity whenever available in the source data. Furthermore, we introduce a scoring protocol that extracts latent token probabilities to compute robust biometric scores. Experimental results reveal a significant performance dichotomy dependent on signal quality and forgery type. In random forgery scenarios, the zero-shot VLM achieves exceptional discrimination, with GPT-5.2 reaching an Equal Error Rate of 0.32% in mobile tasks, outperforming supervised state-of-the-art systems. Conversely, in skilled forgery scenarios, where the task is more challenging because both signatures are almost identical, the results are significantly worse, and a critical "Rationalization Trap" emerges: chain-of-thought (CoT) reasoning degrades performance as the model produces kinematic hallucinations to justify forgery artifacts as natural variability.

---


### 121. [IFPV: An Integrated Multi-Agent Framework for Generative Operational Planning and High-Fidelity Plan Verification](https://arxiv.org/abs/2605.14851)

**<font color=#1a73e8>作者：</font>** Zhigao Huang, Zhengqing Hu, Dong Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Operational plan generation and verification are critical for modern complex and rapidly changing battlefield environments, yet traditional generation and verification methods still respectively face the challenges of generation infeasibility and verification insufficiency. To alleviate these limitations, we propose an Integrated Multi-Agent Framework for Generative Operational Planning and High-Fidelity Plan Verification (IFPV). IFPV consists of two tightly coupled modules: Multi-Perspective Hierarchical Agents (MPHA) for generative operational planning and an Adversarial Cognitive Simulation Engine (ACSE) for high-fidelity adversarial plan verification. MPHA decomposes commander intent into executable multi-platform tactical action sequences through the collaboration of Pathfinder, Analyst, and Planner agents. ACSE introduces an opponent equipped with a customized world model, which predicts the future evolution of mission-critical platforms and conducts dynamic counteractions against candidate plans. Simulation experiments in the Asymmetric Combat Tactic Simulator (ACTS) show that IFPV improves mission success by 19.4% and reduces operational cost by 41.7% compared with a single-step large language model (LLM) planning baseline. Compared with a traditional rule-based validator, ACSE increases the average suppression rate by 31.8%, indicating that the proposed verification environment is stricter and more discriminative in revealing the latent vulnerabilities of candidate plans. The code for IFPV can be found at this https URL.

---


### 122. [A Deterministic Agentic Workflow for HS Tariff Classification: Multi-Dimensional Rule Reasoning with Interpretable Decisions](https://arxiv.org/abs/2605.14857)

**<font color=#1a73e8>作者：</font>** Yu Zhang, Dongjiang Zhuang, Qu Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Harmonized System (HS) tariff classification is a high-stakes, expert-level task in which a free-form product description must be mapped to a specific six- or eight-digit code under the General Interpretive Rules (GIR), section notes, chapter notes, and Explanatory Notes. The difficulty lies not in knowledge volume but in *multi-dimensional rule reasoning*: a correct classification must satisfy competing priority rules along several axes simultaneously, including material, form, function, essential character, the part-versus-whole boundary, and specific listing versus residual headings. End-to-end prompting of large language models fails characteristically by resolving one axis while ignoring the priority constraints on the others. We present a *deterministic agentic workflow* in contrast to self-planning agents: the control flow is fixed, language model calls are confined to narrow stages, and reflection and verification are retained as local mechanisms. This design yields interpretability by construction--each decision is decomposed into stage-wise structured outputs with verbatim citation of the chapter or section notes that bear on it. The architecture combines offline knowledge-engineering of the Chinese HS tariff with an online six-stage pipeline. Evaluated on HSCodeComp at the six-digit level, the workflow reaches 75.0% top-1 and 91.5% top-3 at four digits, and 64.2% top-1 and 78.3% top-3 at six digits with Qwen3.6-plus; an open-weight Qwen3.6-27B-FP8 backbone in non-thinking mode achieves 84.2% four-digit and 77.4% six-digit top-1 agreement with the frontier model. A two-stage manual audit of 226 six-digit disagreements suggests that a non-trivial fraction of HSCodeComp ground-truth labels may deviate from HS general rules; full adjudication records are released in the appendix as preliminary findings for community review.

---


### 123. [Tokenizer Fertility and Zero-Shot Performance of Foundation Models on Ukrainian Legal Text: A Comparative Study](https://arxiv.org/abs/2605.14890)

**<font color=#1a73e8>作者：</font>** Volodymyr Ovcharov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Foundation models tokenize Ukrainian legal text with vastly different efficiency, yet no systematic comparison exists for this domain. We benchmark seven models from five providers on 273 validated court decisions from Ukraine's state registry (EDRSR), measuring tokenizer fertility and zero-shot performance on three tasks. Three findings emerge. (1) Tokenizer fertility varies 1.6x: Qwen3 models consume 60% more tokens than Llama-family models on identical input, directly reducing API cost. (2) NVIDIA Nemotron Super 3 (120B) achieves the highest composite score (83.1), outperforming Mistral Large 3 (675B total, 41B active) -- a model with 5.6x more total parameters and 3.4x more active parameters per token -- at one-third the API cost. (3) Few-shot prompting degrades performance by up to 26 percentage points; stratified and prompt-sensitivity ablations confirm this is intrinsic to Ukrainian-language demonstrations, not an artifact of example selection. For practitioners: tokenizer analysis should precede model selection, and zero-shot is a more reliable default than few-shot for morphologically rich languages.

---


### 124. [Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems](https://arxiv.org/abs/2605.14892)

**<font color=#1a73e8>作者：</font>** Shihao Qi, Jie Ma, Rui Xing 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based autonomous agents have demonstrated strong capabilities in reasoning, planning, and tool use, yet remain limited when tasks require sustained coordination across roles, tools, and environments. Multi-agent systems address this through structured collaboration among specialized agents, but tighter coordination also amplifies a less explored risk: errors can propagate across agents and interaction rounds, producing failures that are difficult to diagnose and rarely translate into structural self-improvement. Existing surveys cover individual agent capabilities, multi-agent collaboration, or agent self-evolution separately, leaving the causal dependencies among them unexamined. This survey provides a unified review organized around four causally linked stages, which we term the LIFE progression: Lay the capability foundation, Integrate agents through collaboration, Find faults through attribution, and Evolve through autonomous self-improvement. For each stage, we provide systematic taxonomies and formally characterize the dependencies between adjacent stages, revealing how each stage both depends on and constrains the next. Beyond synthesizing existing work, we identify open challenges at stage boundaries and propose a cross-stage research agenda for closed-loop multi-agent systems capable of continuously diagnosing failures, reorganizing structures, and refining agent behaviors, extending current coordination frameworks toward more self-organizing forms of collective intelligence. By bridging these previously fragmented research threads, this survey aims to offer both a systematic reference and a conceptual roadmap toward autonomous, self-improving multi-agent intelligence.

---


### 125. [MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models](https://arxiv.org/abs/2605.14906)

**<font color=#1a73e8>作者：</font>** Xiyu Ren, Zhaowei Wang, Yiming Du 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Memory is essential for large vision-language models (LVLMs) to handle long, multimodal interactions, with two method directions providing this capability: long-context LVLMs and memory-augmented agents. However, no existing benchmark conducts a systematic comparison of the two on questions that genuinely require multimodal evidence. To close this gap, we introduce MEMLENS, a comprehensive benchmark for memory in multimodal multi-session conversations, comprising 789 questions across five memory abilities (information extraction, multi-session reasoning, temporal reasoning, knowledge update, and answer refusal) at four standard context lengths (32K-256K tokens) under a cross-modal token-counting scheme. An image-ablation study confirms that solving MEMLENS requires visual evidence: removing evidence images drops two frontier LVLMs below 2% accuracy on the 80.4% of questions whose evidence includes images. Evaluating 27 LVLMs and 7 memory-augmented agents, we find that long-context LVLMs achieve high short-context accuracy through direct visual grounding but degrade as conversations grow, whereas memory agents are length-stable but lose visual fidelity under storage-time compression. Multi-session reasoning caps most systems below 30%, and neither approach alone solves the task. These results motivate hybrid architectures that combine long-context attention with structured multimodal retrieval. Our code is available at this https URL.

---


### 126. [KGPFN: Unlocking the Potential of Knowledge Graph Foundation Model via In-Context Learning](https://arxiv.org/abs/2605.14907)

**<font color=#1a73e8>作者：</font>** Yisen Gao, Jiaxin Bai, Haoyu Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graph (KG) foundation models aim to generalize across graphs with unseen entities and relations by learning transferable relational structure. However, most existing methods primarily emphasize relation-level universality, while in-context learning, the other pillar of foundation models remains under-explored for KG reasoning. In KGs, context is inherently structured and heterogeneous: effective prediction requires conditioning on the local context around the query entities as well as the global context that summarizes how a relation behaves across many instances. We propose KGPFN, a KG foundation model using Prior-data Fitted Network that unifies transferable relational regularities with inference-time in-context learning from structured context. KGPFN first learns relation representations via message passing on relation graphs to capture cross-graph relational invariances. For query-specific reasoning, it encodes local neighborhoods using a multi-layer NBFNet as local context. To enable ICL at global scale, it constructs relation-specific global context by retrieving a large set of instances of the query relation together with their local neighborhoods, and aggregates them within a Prior-Data Fitted Network framework that combines feature-level and sample-level attention. Through multi-graph pretraining on diverse KGs, KGPFN learns when to instantiate reusable patterns and when to override them using contextual evidence. Experiments on 57 KG benchmarks demonstrate that KGPFN achieves strong adaptation to previously unseen graphs through in-context learning alone, consistently outperforming competitive fine-tuned KG foundation models. Our code is available at this https URL.

---


### 127. [SteerSeg: Attention Steering for Reasoning Video Segmentation](https://arxiv.org/abs/2605.14908)

**<font color=#1a73e8>作者：</font>** Ali Cheraghian, Hamidreza Dastmalchi, Abdelwahed Khamis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video reasoning segmentation requires localizing objects across video frames from natural language expressions, often involving spatial reasoning and implicit references. Recent approaches leverage frozen large vision-language models (LVLMs) by extracting attention maps and using them as spatial priors for segmentation, enabling training-free grounding. However, these attention maps are optimized for text generation rather than spatial localization, often resulting in diffuse and ambiguous grounding signals. In this work, we introduce SteerSeg, a lightweight framework that identifies attention misalignment as the key bottleneck in attention-based grounding and proposes to steer attention at its source through input-level conditioning. SteerSeg combines learnable soft prompts with reasoning-guided Chain-of-Thought (CoT) prompting. The soft prompts reshape the attention distribution to produce more spatially concentrated maps, while CoT-derived attributes resolve ambiguity among similar objects by guiding attention toward the correct instance. The resulting attention maps are converted into point prompts across keyframes to guide a segmentation model, while candidate tracklets are ranked and selected using correlation-based scoring. Our approach freezes the LVLM and segmentation model parameters and learns only a small set of soft prompts, preserving the model's pretrained reasoning capabilities while significantly improving grounding. Despite being trained only on Ref-YouTube-VOS, SteerSeg generalizes well across diverse benchmarks, significantly improving the spatial grounding capability of LVLMs. Project page: this https URL

---


### 128. [From Sycophantic Consensus to Pluralistic Repair: Why AI Alignment Must Surface Disagreement](https://arxiv.org/abs/2605.14912)

**<font color=#1a73e8>作者：</font>** Varad Vishwarupe, Nigel Shadbolt, Marina Jirotka  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pluralistic alignment is typically operationalised as preference aggregation: producing responses that span (Overton), steer toward (Steerable), or proportionally represent (Distributional) diverse human values. We argue that aggregation alone is an incomplete primitive for deployed pluralistic alignment. Under genuine value pluralism, the failure mode of contemporary RLHF-trained assistants is not insufficient coverage but sycophantic consensus: a learned tendency to agree with, validate, and minimise friction with the immediate interlocutor. Because deployed AI systems now mediate consequential deliberation across health, civic life, labour, and governance, the collapse of disagreement at the interaction layer is not a narrow technical concern but a structural failure with distributive consequences. We reframe pluralistic alignment around three conversational mechanisms drawn from Grice's maxims: scoping (acknowledging the limits of one's perspective), signalling (surfacing value-conflict rather than smoothing it over), and repair (revising one's position on principled grounds, not on user pressure). We formalise a metric, the Pluralistic Repair Score (PRS), distinguishing principled revision from capitulation, and present a small-scale empirical illustration on two frontier RLHF-trained models (Claude Sonnet 4.5, N=198; GPT-4o, N=100) showing that, for both, agreement-following coexists with low repair-quality on contested-value prompts. PRS measures an interactional precondition for pluralism (visible disagreement; principled revision) rather than pluralism in full; we discuss the difference, take seriously the reflexive question of whose "principled" counts, and argue that pluralism is most decisively made or unmade at the deployment-governance layer: interfaces, preference-data pipelines, and audit infrastructure.

---


### 129. [A Mutual Information Lower Bound for Multimodal Regression Active Learning](https://arxiv.org/abs/2605.14917)

**<font color=#1a73e8>作者：</font>** Leonardo Ferreira Guilhoto, Akshat Kaushal, Paris Perdikaris  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active learning for continuous regression has lacked an acquisition function that targets epistemic uncertainty when the predictive distribution is multimodal: variance misses modal disagreement, and information-theoretic targets like BALD are designed for discrete outputs. We introduce a Two-Index framework that makes this separation explicit: one stochastic index selects among competing model hypotheses (epistemic source), while a second governs within-hypothesis randomness (aleatoric source). An entropy decomposition within the framework identifies the mutual information between the output and the epistemic index as a principled acquisition objective, and we prove this quantity vanishes as the model is trained on growing datasets, confirming that it captures exactly the uncertainty data can resolve. Because this mutual information is intractable for continuous outputs, we derive the Mutual Information Lower Bound (MI-LB) acquisition function, a closed-form approximation for Mixture Density Network ensembles. On benchmarks featuring multimodal systems, MI-LB matches or beats every baseline evaluated and is the only method to do so consistently -- geometric and Fisher-based baselines compete only when the input space already encodes the multimodality, and collapse otherwise.

---


### 130. [Chain-of-Procedure: Hierarchical Visual-Language Reasoning for Procedural QA](https://arxiv.org/abs/2605.14928)

**<font color=#1a73e8>作者：</font>** Guanhua Chen, Yutong Yao, Shenghe Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in vision-language models (VLMs) have achieved impressive results on standard image-text tasks, yet their potential for visual procedure question answering (VP-QA) remains largely unexplored. VP-QA presents unique challenges where users query next-step actions by uploading images for intermediate states of complex procedures. To systematically evaluate VLMs on this practical task, we propose ProcedureVQA, a novel multimodal benchmark specifically designed for visual procedural reasoning. Through comprehensive analysis, we identify two critical limitations in current VLMs: inadequate cross-modal retrieval of structured procedures given visual states, and misalignment between image sequence granularity and textual step decomposition. To address these issues, we present Chain-of-Procedure (CoP), a hierarchical reasoning framework that first retrieves relevant instructions using visual cues, then performs step refinement through semantic decomposition, and finally generates the next step. Experiments across six VLMs demonstrate CoP's effectiveness, achieving up to 13% absolute improvement over standard baselines.

---


### 131. [A Hardware-Aware, Per-Layer Methodology for Post-Training Quantization of Large Language Models](https://arxiv.org/abs/2605.14929)

**<font color=#1a73e8>作者：</font>** Earl Killian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaled Outer Product (SOP) is a post-training quantization methodology for large language model weights, designed to deliver near-lossless fidelity at 4.5--6 bits per weight on hardware with per-layer LUT decode. The methodology combines per-layer search of fixed and dynamic codebook pairs selected by a per-block selection bit, signed per-block scales, activation-weighted cosine selection, and multiple-choice knapsack promotion of sensitive layers with outlier and sparse-residual correction. Fixed codebooks include NF4, BOF4, Split87, and SH4; per-layer optimized codebooks (DD4) are hosted in LUT SRAM. A new hardware-efficient LUT output format (HIF) is proposed to improve performance, energy, and cost. Across six open model families, the recommended FP6 operating point (E2M3sUE4M4, 6.5 bpw) achieves lower weight reconstruction error than the conventional per-layer-POT FP8 baseline (E4M3, 8.0 bpw) at 1.5 bpw lower storage cost, demonstrating that block-scaled small atoms with carefully chosen scale precision can replace conventionally-deployed FP8. Full evaluation across the 4.5--6 bpw range, including layer promotion and sparse residual correction, is reported in a companion paper.

---


### 132. [Octopus: History-Free Gradient Orthogonalization for Continual Learning in Multimodal Large Language Models](https://arxiv.org/abs/2605.14938)

**<font color=#1a73e8>作者：</font>** Yuehao Liu, Shanyan Guan, Weijia Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning in multimodal large language models (MLLMs) aims to sequentially acquire knowledge while mitigating catastrophic forgetting, yet existing methods face inherent limitations: architecture-based approaches incur additional computational overhead and often generalize poorly to new tasks, rehearsal-based methods rely on storing historical data, raising privacy and storage concerns, and conventional regularization-based strategies alone are insufficient to fully prevent parameter interference. We propose Octopus, a two-stage continual learning framework based on History-Free Gradient Orthogonalization (HiFGO), which enforces gradient-level orthogonality without historical task data. Our proposed two-stage finetuning strategy decouples task adaptation from regularization, achieving a principled balance between plasticity and stability. Experiments on UCIT show that Octopus establishes state-of-the-art performance, surpassing prior SOTA by 2.14% and 6.82% in terms of Avg and Last.

---


### 133. [MHSA: A Lightweight Framework for Mitigating Hallucinations via Steered Attention in LVLMs](https://arxiv.org/abs/2605.14966)

**<font color=#1a73e8>作者：</font>** Wei Ding, Yilin Li, Yudong Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) have achieved remarkable performance across diverse multimodal tasks, yet they continue to suffer from hallucinations, generating content that is inconsistent with the visual input. Prior work DHCP (Detecting Hallucinations by Cross-modal Attention Pattern) has explored hallucination detection from the perspective of cross-modal attention, but does not address hallucination mitigation. In this paper, we propose MHSA (Mitigating Hallucinations via Steered Attention), a lightweight framework that mitigates hallucinations by learning to correct cross-modal attention patterns in LVLMs. MHSA trains a simple three-layer MLP generator to produce corrected attention, guided by supervisory signals from the DHCP discriminator and the LVLM itself. During inference, MHSA mitigates both discriminative and generative hallucinations across various datasets and LVLMs by simply replacing the original cross-modal attention with the corrected one, without modifying any LVLM parameters. By extending cross-modal attention mechanisms from hallucination detection to hallucination mitigation, MHSA offers a novel perspective on hallucination research in LVLMs and helps enhance their reliability.

---


### 134. [InfoSFT: Learn More and Forget Less with Information-Aware Token Weighting](https://arxiv.org/abs/2605.14967)

**<font color=#1a73e8>作者：</font>** Mahdi Sabbaghi, George Pappas, Adel Javanmard 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) provides the standard approach for teaching LLMs new behaviors from offline expert demonstrations. However, standard SFT uniformly fits all samples -- including those with low likelihood under the base model -- which can disproportionately drive training updates toward overfitting specific samples rather than learning the target behavior. Moreover, adapting to these unlikely samples induces substantial policy shifts that degrade prior capabilities. Existing methods mitigate this by filtering, regenerating, or down-weighting low-likelihood data. In doing so, they often suppress precisely the novel behaviors the base model has yet to learn.
We propose InfoSFT, a principled weighting scheme for the SFT objective that concentrates learning signals on maximally informative, medium-confidence tokens -- those neither overly familiar to the base model nor too unlikely to cause instability. Requiring only a one-line modification to the standard token-wise loss, InfoSFT demonstrably improves generalization over vanilla SFT and likelihood-weighted baselines across math, code, and chain-of-thought tasks with diverse model families, while better preserving pre-existing capabilities.

---


### 135. [GraphFlow: An Architecture for Formally Verifiable Visual Workflows Enabling Reliable Agentic AI Automation](https://arxiv.org/abs/2605.14968)

**<font color=#1a73e8>作者：</font>** Drewry H. Morris V, Luis Valles, Reza Hosseini Ghomi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GraphFlow is a visual workflow system designed to improve the reliability of agentic AI automation in multi-step, mission-critical processes. In these workflows, small errors compound rapidly: under an idealized model of independent steps, a ten-step process with 90% per-step reliability completes successfully only 35% of the time. Existing workflow platforms provide durable execution and observability but offer few semantic correctness guarantees, while agentic systems plan at inference time, making behavior sensitive to prompt variation and difficult to audit.
GraphFlow is designed to address this gap by treating workflow diagrams as the executable specification, a single artifact defining data scope, execution semantics, and monitoring. At compile time, a restricted class of diagrams is specified to produce reusable automations whose contracts (preconditions, postconditions, and composition obligations) are intended to be proof-checked before admission to a shared library. At runtime, a durable engine records outcomes in an append-only event log and can enforce contracts at system boundaries, supporting replay, retries, and audit. Swimlanes make trust boundaries explicit, separating verified logic from external systems, human judgment, and AI decisions.
A year-long pilot across three clinical sites executed 8,728 cohort-enrolled workflow runs with a 97.08% completion rate under an early prototype without the verified-core subsystem; observed failures were localized primarily to external integrations. The formal semantics and proof-checked admission model described here are specified and under active development. Evaluation of the verified core is reserved for future work.

---


### 136. [Explainable Detection of Depression Status Shifts from User Digital Traces](https://arxiv.org/abs/2605.14995)

**<font color=#1a73e8>作者：</font>** Loris Belcastro, Francesco Gervino, Fabrizio Marozzo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every day, users generate digital traces (e.g., social media posts, chats, and online interactions) that are inherently timestamped and may reflect aspects of their mental state. These traces can be organized into temporal trajectories that capture how a user's mental health signals evolve, including phases of improvement, deterioration, or stability. In this work, we propose an explainable framework for detecting and analyzing depression-related status shifts in user digital traces. The approach combines multiple BERT-based models to extract complementary signals across different dimensions (e.g., sentiment, emotion, and depression severity). Such signals are then aggregated over time to construct user-level trajectories that are analyzed to identify meaningful change points. To enhance interpretability, the framework integrates a large language model to generate concise and human-readable reports that describe the evolution of mental-health signals and highlight key transitions. We evaluate the framework on two social media datasets. Results show that the approach produces more coherent and informative summaries than direct LLM-based reporting, achieving higher coverage of user history, stronger temporal coherence, and improved sensitivity to change points. An ablation study confirms the contribution of each component, particularly temporal modeling and segmentation. Overall, the method provides an interpretable view of mental health signals over time, supporting research and decision making without aiming at clinical diagnosis.

---


### 137. [Quantifying and Mitigating Premature Closure in Frontier LLMs](https://arxiv.org/abs/2605.15000)

**<font color=#1a73e8>作者：</font>** Rebecca Handler, Suhana Bedi, Nigam Shah  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Premature closure, or committing to a conclusion before sufficient information is available, is a recognized contributor to diagnostic error but remains underexamined in large language models (LLMs). We define LLM premature closure as inappropriate commitment under uncertainty: providing an answer, recommendation, or clinical guidance when the safer response would be clarification, abstention, escalation, or refusal. We evaluated five frontier LLMs across structured and open-ended medical tasks. In MedQA (n = 500) and AfriMed-QA (n = 490) questions where the correct choice had been removed, models still selected an answer at high rates, with baseline false-action rates of 55-81% and 53-82%, respectively. In open-ended evaluation, models gave inappropriate answers on an average of 30% of 861 HealthBench questions and 78% of 191 physician-authored adversarial queries. Safety-oriented prompting reduced premature closure across models, but residual failure persisted, highlighting the need to evaluate whether medical LLMs know when not to answer.

---


### 138. [Boosting Reinforcement Learning with Verifiable Rewards via Randomly Selected Few-Shot Guidance](https://arxiv.org/abs/2605.15012)

**<font color=#1a73e8>作者：</font>** Kai Yan, Alexander G. Schwing, Yu-Xiong Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has achieved great success in developing Large Language Models (LLMs) with chain-of-thought rollouts for many tasks such as math and coding. Nevertheless, RLVR struggles with sample efficiency on difficult problems where correct rollouts are hard to generate. Prior works propose to address this issue via demonstration-guided RLVR, i.e., to conduct Supervised FineTuning (SFT) when RL fails; however, SFT often requires a lot of data, which can be expensive to acquire. In this paper, we propose FEST, a FEw-ShoT demonstration-guided RLVR algorithm. It attains compelling results with only 128 demonstrations randomly selected from an SFT dataset. We find that three components are vital for the success: supervised signal, on-policy signal, and decaying weights on the few-shot SFT dataset to prevent overfitting from multiple-epoch training. On several benchmarks, FEST outperforms baselines with magnitudes less SFT data, even matching their performance with full dataset.

---


### 139. [Small, Private Language Models as Teammates for Educational Assessment Design](https://arxiv.org/abs/2605.15015)

**<font color=#1a73e8>作者：</font>** Chris Davis Jaldi, Anmol Saini, Shan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI increasingly supports educational design tasks, e.g., through Large Language Models (LLMs), demonstrating the capability to design assessment questions that are aligned with pedagogical frameworks (e.g., Bloom's taxonomy). However, they often rely on subjective or limited evaluation methods; focus primarily on proprietary models; or rarely systematically examine generation, evaluation, or deployment constraints in real educational settings. Meanwhile, Small Language Models (SLMs) have emerged as local alternatives that better address privacy and resource limitations; yet their effectiveness for assessment tasks remains underexplored. To address this gap, we systematically compare LLMs and SLMs for assessment question design; evaluate generation quality across Bloom's taxonomy levels using reproducible, pedagogically grounded metrics; and further assess model-based judging against expert-informed evaluation by analyzing reliability and agreement patterns. Results show that SLMs achieve competitive performance across key pedagogically motivated quality dimensions while enabling local, privacy-sensitive deployment. However, model-based evaluations also exhibit systematic inconsistencies and bias relative to expert ratings. These findings provide evidence to posit language models as bounded assistants in assessment workflows; underscore the necessity of Human-in-the-Loop; and advance the automated educational question generation field by examining quality, reliability, and deployment-aware trade-offs.

---


### 140. [From Scenes to Elements: Multi-Granularity Evidence Retrieval for Verifiable Multimodal RAG](https://arxiv.org/abs/2605.15019)

**<font color=#1a73e8>作者：</font>** Guanhua Chen, Chuyue Huang, Yutong Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Retrieval-Augmented Generation (RAG) systems retrieve evidence at coarse granularities (entire images or scenes), creating a mismatch with fine-grained user queries and making failures unverifiable. We introduce GranuVistaVQA, a multimodal benchmark featuring real-world landmarks with element-level annotations across multiple viewpoints, capturing the partial observation challenge where individual images contain only subsets of entities. We further propose GranuRAG, a multi-granularity framework that treats visual elements as first-class retrieval units through three stages: element-level detection and classification, multi-granularity cross-modal alignment for evidence retrieval, and attribution-constrained generation. By grounding retrieval at the element level rather than relying on implicit attention, our approach enables transparent error diagnosis. Experiments demonstrate that GranuRAG achieves up to 29.2% improvement over six strong baselines for this task.

---


### 141. [Multi-Agentic Approach for History Matching of Oil Reservoirs](https://arxiv.org/abs/2605.15028)

**<font color=#1a73e8>作者：</font>** Linar Samigullin, Sergei Shumilin, Evgeny Burnaev  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> History matching is a central inverse problem in reservoir engineering, where uncertain reservoir parameters must be calibrated against observations. Although automated history matching can reduce manual effort, practical deployment remains difficult because engineers must still configure heterogeneous workflows involving parameter selection, physically admissible bounds, optimizer choice, hyperparameter tuning, simulator execution, and diagnostic reporting. We propose PetroGraph, a multi-agent framework for intelligent reservoir history matching that decomposes this workflow into specialized agents for model review, experimental planning, parameterization, optimization, simulation, and summarization. The system combines large language model agents with domain-specific tools, retrieval-augmented access to simulator documentation, validation of modified ECLIPSE input decks, human-in-the-loop checkpoints, and an OPM Flow-based simulation backend. This design enables users to initiate and steer history matching through natural language while preserving explicit control over selected parameters and optimization settings. We evaluate PetroGraph on three reservoir models of increasing complexity: the synthetic SPE1 model, the faulted SPE9 benchmark, and the real-field Norne model. Using weighted normalized root mean square error as the objective, PetroGraph reduces the mismatch by 95% on SPE1, 69% on SPE9, and 13% on Norne. These results demonstrate that multi-agent orchestration can automate key decisions in history matching, lower the expertise barrier for operating complex simulation workflows, and provide a flexible foundation for extensible, domain-aware reservoir model adaptation.

---


### 142. [AI Knows When It's Being Watched: Functional Strategic Action and Contextual Register Modulation in Large Language Models](https://arxiv.org/abs/2605.15034)

**<font color=#1a73e8>作者：</font>** Vinicius Covas, Jorge Alberto Hidalgo Toledo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have been extensively studied from computational and cognitive perspectives, yet their behavior as communicative actors in socially structured contexts remains underexplored. This study examines whether LLM-based multi-agent systems exhibit systematic linguistic adaptation in response to perceived social observation contexts -- a question with direct implications for AI governance and auditing. Drawing on Habermas's (1981) Theory of Communicative Action, Goffman's (1959) dramaturgical model, Bell's (1984) Audience Design framework, and the Hawthorne Effect, we report a controlled experiment involving 100 multi-agent debate sessions across five conditions (n = 20 each). Conditions varied the framing of social observation -- from explicit monitoring by university researchers, to negation of monitoring, to an observer-substitution condition replacing human researchers with an automated AI auditing system. Monitored conditions (Delta+24.9%, Delta+24.2%) and the automated AI monitoring condition (Delta+22.2%) produce higher TTR change than audience-framing conditions (Delta+17.7%), F(4, 94) = 2.79, p = .031. Message length shows a fully dissociated effect, F(4, 95) = 19.55, p < .001. A fifth condition -- replacing human with AI observers -- yields intermediate TTR adaptation, suggesting LLM behavior is sensitive to observer identity: human evaluation elicits stronger register formalization than automated AI surveillance. We discuss implications for AI governance, algorithmic auditing, and the repositioning of LLMs as contextually sensitive communicative actors.

---


### 143. [Orchard: An Open-Source Agentic Modeling Framework](https://arxiv.org/abs/2605.15040)

**<font color=#1a73e8>作者：</font>** Baolin Peng, Wenlin Yao, Qianhui Wu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic modeling aims to transform LLMs into autonomous agents capable of solving complex tasks through planning, reasoning, tool use, and multi-turn interaction with environments. Despite major investment, open research remains constrained by infrastructure and training gaps. Many high-performing systems rely on proprietary codebases, models, or services, while most open-source frameworks focus on orchestration and evaluation rather than scalable agent training. We present Orchard, an open-source framework for scalable agentic modeling. At its core is Orchard Env, a lightweight environment service providing reusable primitives for sandbox lifecycle management across task domains, agent harnesses, and pipeline stages. On top of Orchard Env, we build three agentic modeling recipes. Orchard-SWE targets coding agents. We distill 107K trajectories from MiniMax-M2.5 and Qwen3.5-397B, introduce credit-assignment SFT to learn from productive segments of unresolved trajectories, and apply Balanced Adaptive Rollout for RL. Starting from Qwen3-30B-A3B-Thinking, Orchard-SWE achieves 64.3% on SWE-bench Verified after SFT and 67.5% after SFT+RL, setting a new state of the art among open-source models of comparable size. Orchard-GUI trains a 4B vision-language computer-use agent using only 0.4K distilled trajectories and 2.2K open-ended tasks. It achieves 74.1%, 67.0%, and 64.0% success rates on WebVoyager, Online-Mind2Web, and DeepShop, respectively, making it the strongest open-source model while remaining competitive with proprietary systems. Orchard-Claw targets personal assistant agents. Trained with only 0.2K synthetic tasks, it achieves 59.6% pass@3 on Claw-Eval and 73.9% when paired with a stronger ZeroClaw harness. Collectively, these results show that a lightweight, open, harness-agnostic environment layer enables reusable agentic data, training recipes, and evaluations across domains.

---


### 144. [Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use](https://arxiv.org/abs/2605.15041)

**<font color=#1a73e8>作者：</font>** Renning Pang, Tian Lan, Leyuan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool use extends large language models beyond parametric knowledge, but reliable execution requires balancing appropriate reasoning depth with strict structural validity. We approach this problem from a case-based perspective to present CAST, a case-driven framework that treats historical execution trajectories as structured cases. Instead of reusing raw exemplar outputs, CAST extracts case-derived signals to identify complexity profiles for estimating optimal reasoning strategies, alongside failure profiles to map likely structural breakdowns. The framework translates this knowledge into a fine-grained reward design and adaptive reasoning, enabling the model to autonomously internalize case-based strategies during reinforcement learning. Experiments on BFCLv2 and ToolBench demonstrate that CAST improves both schema-faithful execution and task-level tool-use success while reducing unnecessary deliberation. The approach achieves up to 5.85 percentage points gain in overall execution accuracy and reduces average reasoning length by 26%, significantly mitigating high-impact structural errors. Ultimately, this demonstrates how historical execution cases can provide reusable adaptation knowledge for calibrated tool use.

---


### 145. [An Interpretable Latency Model for Speculative Decoding in LLM Serving](https://arxiv.org/abs/2605.15051)

**<font color=#1a73e8>作者：</font>** Linghao Kong, Megan Flynn, Michael Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding (SD) accelerates large language model (LLM) inference by using a smaller draft model to propose multiple tokens that are verified by a larger target model in parallel. While prior work demonstrates substantial speedups in isolated or fixed-batch settings, the behavior of SD in production serving systems remains poorly understood: request load varies over time, and effective batch size emerges from the serving system rather than being directly controlled or observed. In this work, we develop a simple and interpretable latency model for SD in LLM serving. We infer effective batch size from request rate using Little's Law and decompose per-request demand into load-independent and load-dependent components for prefill, drafting, and verification. We validate our model using extensive measurements from vLLM across verifier and drafter model sizes, prefill and decode lengths, request rates, draft lengths, and acceptance probabilities. The model accurately describes observed latency, explains why speedups often diminish as server load increases, and characterizes how draft length, acceptance rate, and verifier-drafter size shape latency across serving conditions, with implications for configuring SD in deployed systems. We further show how the framework extends to mixture of experts models, where sparse expert activation changes the effective service costs across load regimes. Together, our results provide a structured framework for understanding SD in real LLM serving systems.

---


### 146. [TFGN: Task-Free, Replay-Free Continual Pre-Training Without Catastrophic Forgetting at LLM Scale](https://arxiv.org/abs/2605.15053)

**<font color=#1a73e8>作者：</font>** Anurup Ganguli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continually pre-training a large language model on heterogeneous text domains, without replay or task labels, has remained an unsolved architectural problem at LLM scale. Existing methods rely on replay buffers, task identifiers, regularization penalties that scale poorly, or sentence-classification-scale evaluation.
We introduce TFGN, an architectural overlay for transformer language models that produces input-conditioned, parameter-efficient updates while leaving the rest of the transformer unchanged. On six heterogeneous text domains (Prose, Python, Math, Biomedical, Chinese, JavaScript) at 1B tokens per phase across three model scales (~398M, ~739M, ~9B) and two regimes (From-Scratch and Retrofit), TFGN achieves backward transfer of -0.007 at LLaMA 3.1 8B Retrofit, HellaSwag retention 0.506/0.504/0.510, and >=99.59% L2-orthogonal gradient separation between domain pairs - with no replay, no task IDs, no Fisher penalty.
The same matrices show positive cross-domain forward transfer: held-out JavaScript PPL drops 26.8% at LLaMA-8B Retrofit and 62.0% at GPT-2 Medium From-Scratch purely from Python training. Two extensions on the same substrate close further open problems. A closed-loop meta-control layer (Extension A) reduces forgetting by an additional 81% at ~398M, mapping onto the System A and System M roles of Dupoux et al. (arXiv:2603.15381). An operator-level plan vector (Extension B) reshapes forward-pass behavior at 99.96% cosine fidelity over 30 source->target pairs.
The architectural insight is a Read/Write decomposition: the forward pass is fully dense, while cross-domain parameter updates are structured so prior-domain subspaces are not written to. To our knowledge, TFGN is the first architecture that simultaneously closes catastrophic forgetting at LLM scale, realizes a closed-loop autonomous-learning meta-controller, and carries an operator-level latent planner.

---


### 147. [LATERN: Test-Time Context-Aware Explainable Video Anomaly Detection](https://arxiv.org/abs/2605.15054)

**<font color=#1a73e8>作者：</font>** Mitchell Piehl, Muchao Ye  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have recently emerged as a promising paradigm for video anomaly detection (VAD) due to their strong visual reasoning ability and natural language-based explainability. In this paper, we aim to address a key limitation of such pipelines, which perform segment-level inference independently owing to token constraints and reason without structured temporal context, allowing VLMs to interpret anomalies as deviations from evolving video dynamics rather than producing fragmented predictions and explanations. To specify, we propose a context-aware framework named LATERN, which reformulates VAD as a temporal evidence aggregation process. LATERN consists of two complementary modules: Context-Aware Anomaly Scoring (CEA) and Recursive Evidence Aggregation (REA). CEA introduces a novel image-grounded memory mechanism, which selectively chooses historical content via frame diversity and visual-textual alignment as expanded context to help generate reliable anomaly scores. Building upon these scores, REA performs recursive temporal aggregation to identify coherent anomaly intervals and produce event-level decisions and explanations grounded in visual-textual evidence. Extensive experiments on challenging benchmarks, including UCF-Crime and XD-Violence, show that LATERN enhances detection accuracy and explanation consistency for frozen VLMs during test time, while generating temporally coherent and semantically grounded event-level explanations.

---


### 148. [On the Cultural Anachronism and Temporal Reasoning in Vision Language Models](https://arxiv.org/abs/2605.15071)

**<font color=#1a73e8>作者：</font>** Mukul Ranjan, Prince Jha, Khushboo Kumari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are increasingly applied to cultural heritage materials, from digital archives to educational platforms. This work identifies a fundamental issue in how these models interpret historical artifacts. We define this phenomenon as cultural anachronism, the tendency to misinterpret historical objects using temporally inappropriate concepts, materials, or cultural frameworks. To quantify this phenomenon, we introduce the Temporal Anachronism Benchmark for Vision-Language Models (TAB-VLM), a dataset of 600 questions across six categories, designed to evaluate temporal reasoning on 1,600 Indian cultural artifacts spanning prehistoric to modern periods. Systematic evaluations of ten state-of-the-art models reveal significant deficiencies on our benchmark, and even the best model (GPT-5.2) achieves only 58.7% overall accuracy. The performance gap persists across varying architectures and scales, suggesting that cultural anachronism represents a significant limitation in visual AI systems, regardless of model size. These findings highlight the disparity between current VLM capabilities and the requirements for accurately interpreting cultural heritage materials, particularly for non-Western visual cultures underrepresented in training data. Our benchmark provides a foundation for enhancing temporal cognition in multimodal AI systems that interact with historical artifacts. The dataset and code are available in our project page.

---


### 149. [Concurrency without Model Changes: Future-based Asynchronous Function Calling for LLMs](https://arxiv.org/abs/2605.15077)

**<font color=#1a73e8>作者：</font>** Guangyu Feng, Huanzhi Mao, Prabal Dutta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Function calling, also known as tool use, is a core capability of modern LLM agents but is typically constrained by synchronous execution semantics. Under these semantics, LLM decoding is blocked until each function call completes, resulting in increasing end-to-end latency. In this work, we introduce AsyncFC, a pure execution-layer framework that decouples LLM decoding from function execution, enabling overlap between model decoding and function execution as well as inter-function parallelism when dependencies permit. AsyncFC layers over existing models and unmodified function implementations, requiring no fine-tuning or changes to the standard synchronous function-calling protocol. Across standard function-calling benchmarks and adapted software engineering benchmarks, AsyncFC significantly reduces end-to-end task completion time while preserving task accuracy. Furthermore, these results reveal that LLMs possess a native capability to reason over symbolic futures that represent unresolved execution results, enabling an asynchronous paradigm for model-tool interaction.

---


### 150. [From Text to Voice: A Reproducible and Verifiable Framework for Evaluating Tool Calling LLM Agents](https://arxiv.org/abs/2605.15104)

**<font color=#1a73e8>作者：</font>** Md Tahmid Rahman Laskar, Xue-Yong Fu, Seyyed Saeed Sarfjoo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Voice agents increasingly require reliable tool use from speech, whereas prominent tool-calling benchmarks remain text-based. We study whether verified text benchmarks can be converted into controlled audio-based tool calling evaluations without re-annotating the tool schema and gold labels. Our dataset-agnostic framework uses text-to-speech, speaker variation, and environmental noise to create paired text-audio instances while preserving the original dataset annotations. Based on extensive evaluation of 7 omni-modal models on audio-converted versions of Confetti and When2Call, our framework demonstrates that the performance is strongly model- and task-dependent: Gemini-3.1-Flash-Live obtains the highest Confetti score (70.4), whereas GPT-Realtime-1.5 performs best on When2Call (71.9). On Confetti, the text-to-voice gap ranges from 1.8 points for Qwen3-Omni to 4.8 points for GPT-Realtime-1.5. A targeted analysis of failure cases demonstrates that degradations most often reflect misunderstandings of argument values in the speech. Considering real-world deployment scenarios, we further report text-only results, an ambiguity-based reformulation stress test, and a reference-free LLM-as-judge protocol validated against human preferences. Notably, we find that open-source Qwen3 judges with at least 8B parameters exceed 80% agreement with proprietary judges, supporting privacy-preserving evaluation. Overall, our framework provides a verifiable and reproducible first-stage diagnostic that complements purpose-built audio corpora.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-165](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
