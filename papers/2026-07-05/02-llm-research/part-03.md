# 🧠 大模型相关研究 | 2026年07月05日

> 本类共 **136** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-136**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-136**

---

### 101. [A rubric-based controlled comparison of frontier language models on expert-authored clinical reasoning tasks](https://arxiv.org/abs/2607.02175)

**<font color=#1a73e8>作者：</font>** Samiha A. Ismail, Fan X. Chen, Ali Merali  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multiple-choice medical benchmarks are increasingly saturated, and recent rubric-based evaluations such as HealthBench have shown that open-ended clinical performance is far from solved - its "Hard" subset top score remains 32%. We present a small, deliberately difficult evaluation dataset of five clinician-authored clinical scenarios spanning four specialties (anaesthesia, internal/family medicine, emergency medicine, and obstetrics), each accompanied by an atomic, weighted, MECE rubric (25-62 criteria per task; 184 criteria total) authored from a clinician-drafted golden answer. We evaluate three frontier models: GPT 5.4, Claude Opus 4.7, and Gemini 3.1 Pro. Mean rubric pass rates were 0.47 (Claude), 0.39 (GPT), and 0.37 (Gemini). The central finding is an inversion of clinical priority: the highest-weighted (weight-5, critical) criteria passed at only 32.4-41.7%, while low-stakes weight-1 criteria passed at 80-90%. 56 of 108 critical (weight-5) criteria (52%) were satisfied by no model. Three LLM autoraters reproduced expert met/not-met labels on 92.8-94.7% of 552 graded criteria. We position this as a methods-and-preliminary-findings contribution: the five tasks demonstrate a scalable, defensible pipeline ready to develop into a large-scale benchmark.

---


### 102. [Bayesian Sparse Low-Rank Adaptation for Large Language Model Uncertainty Estimation](https://arxiv.org/abs/2607.02182)

**<font color=#1a73e8>作者：</font>** Jijie Zhang, Zhe Ren, Quan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit remarkable reasoning capabilities, but their task-specific fine-tuning is notoriously plagued by overconfidence, severely hindering trustworthy deployment. We propose Data-Adaptive Lower-Rank Adaptation (DALorRA), a simple and effective variational Bayesian sparse framework that shifts the paradigm of uncertainty quantification from the dense parameter space to the lightweight rank level of low-rank adaptation (LoRA). With the insight that LoRA essentially aggregates multiple rank-one components that may provide superfluous model capacity, DALorRA imposes stochastic masking on rank dimensions, enabling Bayesian regularization of model capacity during training and ensemble-like calibration during inference. Extensive experiments demonstrate DALorRA's excellent calibration of LLMs without compromising reasoning accuracy.

---


### 103. [UA-ChatDev: Uncertainty-Aware Multi-Agent Collaboration for Reliable Software Development](https://arxiv.org/abs/2607.02186)

**<font color=#1a73e8>作者：</font>** Temitayo Olamilekan Ogunsusi, Lijun Qian, Xishuang Dong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Software development is a complex task that demands cooperation among agents with diverse roles. Large language models (LLMs) have enabled autonomous multi-agent software development frameworks that leverage role-based collaboration to automate requirements analysis, coding, testing, and refinement. However, existing approaches typically assume that intermediate agent outputs are equally reliable, leaving them vulnerable to hallucination propagation, where incorrect decisions generated in early development phases are transferred to downstream agents and negatively impact final software quality. To address this challenge, we propose UA-ChatDev, an uncertainty-aware multi-agent software development framework that integrates uncertainty quantification into agent interactions. It introduces a lightweight uncertainty estimation mechanism based on token-level log probabilities to assess the confidence of agent responses and employs phase-aware threshold calibration to selectively trigger retrieval-based verification when uncertainty exceeds acceptable levels. Extensive experiments on the SRDD benchmark demonstrate that UA-ChatDev consistently outperforms existing single-agent and multi-agent software development frameworks across completeness, executability, consistency, and overall quality metrics. Further ablation studies and communication analyses verify that uncertainty-aware interactions enhance code execution reliability.

---


### 104. [Unlocking Speech-Text Compositional Powers: Instruction-Following Speech Language Models without Instruction Tuning](https://arxiv.org/abs/2607.02214)

**<font color=#1a73e8>作者：</font>** Congrui Du, Yang Zhang, Kaizhi Qian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction tuning for speech language models (SLMs) is substantially more challenging than for text-based large language models (LLMs), as it requires learning a new modality and a wide range of speech-specific instructions in addition to those supported by text LLMs. Existing SLM training approaches largely replicate the text LLM training paradigm by synthesizing large-scale speech pre-training and instruction-tuning datasets. However, this strategy is difficult to scale, since speech sequences are significantly longer than text sequences. In this paper, we propose SpeechCombine, an instruction-following speech language model trained without any instruction tuning, using only a single round of speech pre-training on 30k hours of data. Starting from a text LLM base model, we perform continuous pre-training on speech utterances to obtain a speech-adapted model, and then directly combine its weights with the weight difference between the instruction-tuned and base versions of the text LLM. Our results show that this simple combination strategy not only preserves the knowledge and capabilities of the original text LLM, but also effectively transfers them to the speech domain. These findings suggest a new direction for SLM training that avoids reliance on massive speech data.

---


### 105. [DetailAnywhere: Fashion Detail Generation via Cross-Modal Feature Alignment Distillation](https://arxiv.org/abs/2607.02220)

**<font color=#1a73e8>作者：</font>** Zijun Li, Yimin Zhou, Jia Sun 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based generative AI has achieved remarkable success in e-commerce applications such as virtual try-on, poster generation, and product background synthesis. However, when making online purchasing decisions for apparel, consumers also desire the freedom to examine specific detail regions of interest, such as collars, cuffs, and fabric textures, yet existing methods have not explicitly studied this setting. We therefore formalize a new, non-template task: Fashion Detail Generation with focus conditioning, and release FDBench, the first benchmark comprising 40K+ human-verified reference-detail pairs across 41 different categories. This task poses a unique semantic gap challenge: the model must bridge the correspondence between a focus marker on a product reference image and a photorealistic close-up view of the indicated region, while faithfully preserving the garment's identity, without any precise prompt. To bridge this gap, we propose Cross-modal Feature Alignment Distillation (CFAD), which leverages a fine-tuned DINOv3 teacher to align both branches of a Multimodal Diffusion Transformer in a shared semantic space via dual-branch distillation. To further improve consistency between generated details and reference images, we introduce a consistency reward model that jointly scores image pairs along three quality axes and optimizes generation via reinforcement learning. Experiments show that our model DetailAnywhere significantly outperforms all state-of-the-art opensource methods across all metrics and human evaluations.

---


### 106. [Challenges and Recommendations for LLMs-as-a-Judge in Multilingual Settings and Low-Resource Languages](https://arxiv.org/abs/2607.02235)

**<font color=#1a73e8>作者：</font>** A.Seza Doğruöz, Xixian Liao, Verena Blaschke 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-Judge has become the dominant evaluation paradigm for many natural language generation tasks, due to shortcomings of conventional metrics and high correlations with human judgment, albeit mostly in English. There are now attempts to extend LLM-as-a-Judge to multilingual settings including low-resource languages. However, LLMs have limited proficiency in low-resource languages, and there is often no adequate human validation in these settings. To highlight the scope of the problem and current practices, we explore the use of LLM-as-a-Judge evaluators in ACL Anthology papers focusing on multilingual settings and low-resource languages across a diverse set of tasks. Out of 650 papers mentioning LLM-as-a-judge, only 33 of them focus on low-resource or multilingual settings. Our in-depth analysis of these papers indicates inconsistent evaluation outcomes, a tendency to overtrust LLM judgments in multilingual settings, and the widespread reliance on a single judge model per study. To help the NLP community further, we conclude with recommendations about how to use LLM-as-a-Judge in multilingual and low-resource settings.

---


### 107. [AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents](https://arxiv.org/abs/2607.02255)

**<font color=#1a73e8>作者：</font>** Xiangchen Cheng, Yunwei Jiang, Jianwen Sun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory for a long-horizon LLM agent is a contract about what each future decision is allowed to see. The simplest contract appends past observations, tool calls, and reflections to every prompt, which makes prior context easy to access but also turns it into a jumbled mixture in which the effect of any single memory component is hard to isolate. We introduce and instrument an alternative bounded contract: every decision is made from a fresh user message assembled by typed retrieval, with no raw cross-decision transcript appended. The prompt thus stays bounded across runs of any length, and any single layer can be ablated in isolation. We instantiate the contract in Slay the Spire 2, a closed-rule stochastic deck-building game whose runs require hundreds of tactical and strategic decisions. A public online benchmark of frontier LLMs on the same game reports zero wins at the lowest difficulty across five configurations, and the developer-reported human win rate at the same difficulty is 16%; the task is hard but not saturated. Within our harness, a fixed-A0 ablation shows the largest observed difference when triggered strategic skills are enabled: the no-store baseline wins 3/10 games and adding the skill layer 6/10. At this sample size the comparison is directional rather than statistically decisive (Fisher exact p\approx0.37); a cross-backbone probe and public accumulating-context baselines are reported as operational comparisons rather than controlled tests of the contract variable itself. We release a reproducible testbed: 298 completed trajectories with condition tags, frozen memory/skill snapshots, prompt records, and analysis scripts -- an agent design and a validated, reusable methodology for studying how explicit memory layers shape long-horizon LLM-agent decisions.

---


### 108. [BamiBERT: A New BERT-based Language Model for Vietnamese](https://arxiv.org/abs/2607.02259)

**<font color=#1a73e8>作者：</font>** Dat Quoc Nguyen, Thinh Pham, Chi Tran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce BamiBERT, a new BERT-based pre-trained language model for Vietnamese that addresses key limitations of PhoBERT -- the current de facto Vietnamese text encoder. Trained from scratch on a 129GB corpus of general-domain Vietnamese text for 20 epochs, BamiBERT supports an extended context length of up to 2048 tokens and operates directly on raw input, eliminating the need for external word segmentation. Across 8 Vietnamese benchmarks, it achieves the best score on 11 of 15 metrics and the second-best on 3 others, setting a new state of the art among "base"-sized Vietnamese encoders and demonstrating strong cross-domain generalization. We release BamiBERT at: this https URL

---


### 109. [HERMES: A Multi-Granularity Labeling Substrate for Pre-training Data Mixtures](https://arxiv.org/abs/2607.02266)

**<font color=#1a73e8>作者：</font>** Ziyun Qiao, Yue Min, Ruining Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most data-mixing methods assume the corpus has already been partitioned into groups, and the choice of those groups determines what a mixer can express. Existing labels, including provenance, topic or format taxonomies, and flat embedding clusters, commit to one semantic axis at one granularity; changing the resolution rebuilds the labels. We argue the bottleneck is the label system, not the mixer, and provide a hierarchical one. HERMES is a data-derived labeling substrate: a Learned Semantic Transform followed by 3-stage residual vector quantization annotates each document once into a coarse-to-fine code whose prefix length controls granularity up to approximately 130k cells. At coarse granularity HERMES sits at a plateau with KMeans-family methods on standard clustering metrics, so the contribution is the substrate, not the clusterer. On 1B-parameter, 25B-token pre-training, the hierarchy exposes an interaction fixed-granularity pipelines cannot test: at one prefix length, a combined Stage-2 rule contrast, equal-subbucket coverage versus size-proportional within-bucket quality top-30%, lifts a 16-task capability macro-average by +0.0253; at the next finer level, the same rule loses its measurable edge as candidate pools contract approximately 5x. HERMES reframes data mixture design from choosing among fixed label sets to navigating a reusable, data-derived granularity hierarchy.

---


### 110. [AnyGroundBench: A Specialized-Domain Benchmark for Video Grounding in Vision-Language Models](https://arxiv.org/abs/2607.02269)

**<font color=#1a73e8>作者：</font>** Rintaro Otsubo, Ryo Fujii, Reina Ishikawa 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have demonstrated immense promise in Spatio-Temporal Video Grounding (STVG). However, current evaluation protocols are largely confined to zero-shot assessments on general, daily-life benchmarks. This creates a critical disconnect from real-world applications in specialized fields, where models inevitably encounter rare visual concepts and complex spatio-temporal dynamics. Since exhaustive pre-training across infinite data distributions is infeasible, the ability to adapt to novel domains is essential. To bridge this gap, we introduce AnyGroundBench, a domain-adaptation benchmark designed to shift the STVG evaluation paradigm from static zero-shot testing to rigorous domain adaptation. Targeting five specialized domains (animal, industry, sports, surgery, and public security), AnyGroundBench pairs newly captured videos such as expert-annotated mouse behaviors with established datasets, unifying them through dense, high-fidelity spatio-temporal annotations. Crucially, the benchmark provides dedicated training subsets to systematically measure domain adaptability. We extensively evaluate 15 state-of-the-art VLMs, assessing their zero-shot generalization and In-Context Learning (ICL) capabilities under practical computational constraints. Ultimately, our findings reveal that current models fail in both zero-shot and ICL-based adaptation when confronted with specialized domains, exposing critical flaws in spatio-temporal reasoning that future research must address.

---


### 111. [Search-based Testing of Vision Language Models for In-Car Scene Understanding](https://arxiv.org/abs/2607.02300)

**<font color=#1a73e8>作者：</font>** Lev Sorokin, Chen Yang, Ken E. Friedl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the automotive domain, in-car scene understanding (ISU) enables the detection of safety-critical events, such as driver distraction, and supports drivers or passengers by analyzing the in-car scene and adapting the environment (e.g., ambient lighting). The industry is increasingly exploring vision-language models (VLMs) to interpret camera-recorded in-car scenes and extract information for downstream reasoning tasks. However, VLMs may generate incomplete, erroneous, or misleading scene descriptions, highlighting the need for systematic testing. Collecting real in-vehicle data is costly, difficult to scale, and often infeasible, particularly in early design stages. In this paper, we present ISU-Test, an automated testing approach that combines rendering-based scene generation with search-based testing to evaluate ISU systems. By framing testing as an optimization problem and systematically modifying scene parameters, our method generates diverse in-car scenarios and explores a wide range of configurations. We evaluate ISU-Test on both an industrial prototype and open-source VLMs across two case studies: question answering and captioning, comparing against randomized scenario generation. Results show that ISU-Test significantly outperforms the baseline, achieving up to 10 times higher failure rates and up to 3.6 times higher failure coverage.

---


### 112. [Personality Without Persons? A Psychometric Critique of Big Five Testing in Large Language Models](https://arxiv.org/abs/2607.02325)

**<font color=#1a73e8>作者：</font>** Kim Zierahn, Cristina Cachero, Anna Korhonen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human personality inventories are increasingly used to characterize large language models (LLMs), compare systems, and inform downstream governance claims. Yet, these inventories were developed and validated for humans, and it remains unclear whether they apply to LLMs. We present a systematic psychometric evaluation of Big Five personality measurements in LLMs. We ask three research questions: Do Big Five inventories a) appropriately describe LLMs, b) capture inter-individual differences across models, and c) reflect internal factors consistent with human personality. We assess content validity of five candidate Big Five inventories and administer the winning inventory to N = 244 different models spanning 49 model families. First, we found that Big Five items adapted for LLMs can reach sufficient content validity, while original human-developed items did not. Second, Big Five inventories did not capture meaningful differences between LLMs: We found low variability between models, accounting for only 3% of total score variance. Third, LLMs responses did not recover the Big Five five-factor structure with four of the Big Five facets collapsing into one (r >= .92). Direct comparisons between base and instruction-tuned model variants suggested that alignment training systematically shifted Big Five scores toward socially desirable traits. These findings demonstrate that Big Five scores do not measure a construct equivalent to human personality in LLMs. Applying human personality frameworks to LLMs produces misleading characterizations used to benchmark, compare, and govern LLMs. We highlight the need for evaluation frameworks that are developed for LLMs, rather than adopting human constructs without validation.

---


### 113. [Grounded autonomous research: a fault-tolerant LLM pipeline from corpus to manuscript in frontier computational physics](https://arxiv.org/abs/2607.02329)

**<font color=#1a73e8>作者：</font>** Haonan Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous-research agents have demonstrated end-to-end LLM automation in machine-learning sandboxes where execution provides calibration. Frontier physical science differs categorically: physical reasoning underlies every methodology choice, toolchains are often underdocumented, and calibration must come from external literature anchors - which unscaffolded agents cite but do not confront, hallucinating plausible, unverifiable results from internal priors. We present a pipeline that runs end-to-end from a corpus of 11,083 recent condensed-matter physics arXiv papers to a publication-grade manuscript with three substantive physics findings (here on altermagnetic piezomagnetism): the agent autonomously conceives a research direction by mapping the corpus, calibrates methodology by reproducing published references, conducts novel first-principles computations, and writes the manuscript - grounded in literature throughout, across 47 fresh-context sessions in six phases sharing only on-disk state, with 2,162 literature-consultation events. Fault tolerance emerges from redundancy: fresh-context isolation, distributed grounding, and adversarial review catch what any single session misses; pre- and post-pilot stages are fully autonomous, and pilot requires bounded human intervention only at reproduction failures - operational knowledge curation, not scientific direction. Two paired failure modes - a pre-architecture baseline and a no-pilot ablation - isolate structurally enforced numerical confrontation at calibration checkpoints as the operative grounding mechanism. The primitives, characterized failure modes, and quantified intervention pattern lay a foundation for autonomous research in high-stakes scientific domains beyond computational physics.

---


### 114. [VisionAId: An Offline-First Multimodal Android Assistant for People with Visual Impairment, Featuring Personalized Object Retrieval](https://arxiv.org/abs/2607.02371)

**<font color=#1a73e8>作者：</font>** Cristian-Gabriel Florea, Stelian Spînu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Over 285 million people worldwide live with a visual impairment, for whom everyday tasks such as avoiding obstacles, locating personal belongings, recognizing familiar faces, or handling cash remain persistent obstacles to personal autonomy. Existing assistive applications are typically limited to recognizing predefined categories, depend heavily on cloud connectivity, or require dedicated hardware. We present VisionAId, an Android application that turns a commodity smartphone into a real-time visual assistant. The system integrates six on-device deep learning models (metric monocular depth estimation, instance segmentation, visual and facial embeddings, face detection, and a custom banknote detector) running entirely through ONNX Runtime, with an optional cloud large language model (Google Gemini Flash) used only for narrative scene description and automatic object labeling. A distinctive contribution is a few-shot pipeline for personal objects: the user photographs an object from several angles, and the system later locates that specific instance in the environment, guiding the user toward it with augmented-reality markers, spatial audio, and distance-proportional haptics. All feedback is multimodal (Romanian speech synthesis, voice commands, vibration). On a reference device (Samsung Galaxy S21 Ultra), INT8 quantization reduces depth latency from ~1200 ms to ~491 ms, the custom banknote detector reaches an mAP@50 of 0.986, and metric depth is calibrated to below 1 cm of error within 3 m.

---


### 115. [Learning Spectral and Polarimetric Clues for One-to-Multimodal Novel View Synthesis](https://arxiv.org/abs/2607.02372)

**<font color=#1a73e8>作者：</font>** Federico Lincetto, Gianluca Agresti, Mattia Rossi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural rendering techniques allow for accurate reconstruction of the geometry and color appearance of 3D scenes. Some methods have extended their use to additional imaging modalities, such as multispectral, infrared, or polarimetric data. However, all of these approaches require expensive sensors and calibrated setups to capture new multimodal frames for each new scene. We propose Spectral and Polarimetric Implicit Learned Representation (SPoILeR), a novel method to obtain multi-view consistent renderings of unconventional modalities for scenes where either only RGB frames or very few of the additional modalities are available. Thanks to a multimodal pre-training phase, the model learns the mutual correlation between different modalities. This step allows predicting accurate renderings of unconventional modalities during a fine-tuning phase supervised only by RGB images. Experimental results show that the approach can accurately render infrared, polarimetric, and multispectral frames for scenes where no input sample captured by these types of sensors is provided.

---


### 116. [DRIFTLENS: Measuring Memory-Induced Reasoning Drift in Personalized Language Models](https://arxiv.org/abs/2607.02374)

**<font color=#1a73e8>作者：</font>** Xi Fang, Weijie Xu, Yingqiang Ge 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalization changes what a model says to a user; we show that it can also change the reasoning trajectory used to justify the response. Modern LLMs personalize interactions by storing user attributes, preferences, and prior context, then injecting this information into future prompts. We study whether such memory reshapes reasoning on open-ended questions where no single ground-truth answer exists. To quantify this effect, we introduce DRIFTLENS, a ground-truth-free framework that maps each expressed reasoning step to a value category and measures divergence between a question's no-memory trajectory and its trajectory under injected user-attribute memory. We first validate that DRIFTLENS distinguishes content-free pragmatic noise from substantive reasoning changes. Across four LLMs and 10 user-attribute categories, including age, occupation, and disability, user-attribute memory induces medium-to-large reasoning drift above each model's pragmatic-noise floor, even when final answers remain fluent, on-topic, and plausible. We then evaluate GRPO- and DPO-based post-training methods for reducing drift. Both reduce drift, but neither uniformly dominates; effects on downstream capability, helpfulness, and instruction following are model-and reward-dependent. These results suggest that memory-induced reasoning drift is a measurable and only partly mitigated failure mode of personalized language models.

---


### 117. [Hardware-Enforced Semantic Coordination for Safety-Critical Real-Time Autonomous Systems](https://arxiv.org/abs/2607.02376)

**<font color=#1a73e8>作者：</font>** Uwe M. Borghoff, Paolo Bottoni, Remo Pareschi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in agentic AI are producing increasingly complex autonomous systems that integrate large language models, world models, optimization engines, specialized neural architectures, autonomous platforms, and human operators. While much current research focuses on improving reasoning capabilities, safety-critical real-time deployment also requires bounded and verifiable coordination among heterogeneous components operating concurrently under uncertainty. Software-mediated coordination presents fundamental limitations in domains where bounded latency, deterministic coordination, and enforceable safety guarantees are essential.
Hence, we propose a hardware-enforced semantic coordination architecture in which selected coordination semantics are implemented directly at the hardware level via field-programmable gate arrays (FPGAs). The approach builds on the Topic-Based Communication Space Petri Net (TB-CSPN) framework, which separates semantic reasoning from interaction management.
In this approach, selected TB-CSPN coordination mechanisms are mapped onto FPGA primitives, creating a hardware-native semantic coordination layer. Focus is not on acceleration, but on enforcing temporal synchronization, semantic gating, authorization constraints, and bounded coordination behavior directly in hardware. Semantic reasoning remains adaptive and software-driven, while embedded coordination semantics become deterministic.

---


### 118. [DecompRL: Solving Harder Problems by Learning Modular Code Generation](https://arxiv.org/abs/2607.02390)

**<font color=#1a73e8>作者：</font>** Juliette Decugis, Fabian Gloeckle, Francis Bach 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How can Large Language Models (LLMs) solve problems they currently cannot? Repeated sampling scales test-time compute but GPU cost grows linearly with attempts, while reinforcement learning (RL) with verifiable rewards improves single-attempt accuracy at the expense of sample diversity. Both strategies ultimately fail when the base policy has near-zero probability of producing a correct solution: no amount of sampling or gradient signal can overcome a search space that is simply too large. We take a different approach: rather than sampling harder, we make the task easier by decomposing problems into smaller, independently solvable sub-functions whose implementations can be recombined. Since off-the-shelf models are not trained for this modular generation, we introduce DecompRL, an RL algorithm that explicitly learns to decompose and implement hierarchical code structures. Recombining $k$ implementations of $n$ modules yields up to $k^{n}$ candidate solutions, shifting the bottleneck from GPU inference to cheap CPU evaluation and cutting GPU token cost by $\sim$50$\times$. On LiveCodeBench and CodeContests (Qwen~2.5~7B, Code World Model~32B), DecompRL outperforms standard and diversity-optimized RL baselines beyond $10^5$ tokens per problem, solving problems that standard generation cannot reach.

---


### 119. [Fast Multi-dimensional Refusal Subspaces via RFM-AGOP](https://arxiv.org/abs/2607.02396)

**<font color=#1a73e8>作者：</font>** Thomas Winninger  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Steering and monitoring activations in Large Language Models (LLMs) are increasingly used for both safety and interpretability. Early work assumed behaviours are encoded along single linear directions, but recent findings suggest complex behaviours, such as the refusal to answer harmful queries, live in multi-dimensional subspaces. However, existing methods for extracting these subspaces are computationally expensive, which becomes prohibitive on reasoning models who produce long reasoning traces. By adapting the Recursive Feature Machine (RFM) algorithm -- which can be computed efficiently -- with a probe-informed initialization, we are able to identify the multi-dimensional refusal subspace in seconds, on reasoning (Qwen 3) and non-reasoning (Qwen 2.5) models. While RFM allows for faster subspace identification, it also showed better performances on the ablation task than its alternatives. More work is planned to better understand the relations between subspaces found by different methods. If confirmed, RFM could be a cheap and scalable complement to existing subspace-extraction methods in LLMs.

---


### 120. [Neuron-Aware Active Few-Shot Learning for LLMs](https://arxiv.org/abs/2607.02423)

**<font color=#1a73e8>作者：</font>** Zhuowei Chen, Liwei Chen, Christian Schunn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active Few-Shot Learning (AFSL) adapts LLMs to specialized domains by identifying the most valuable unlabeled samples for annotation and use as few-shot demonstrations, effectively reducing human annotation costs while promoting high performance. However, existing methods typically rely on output-level signals for sample identification, such as predictive entropy or semantic similarities with test-time data based on external embeddings, which often overlook models' internal dynamics, which could pinpoint specific knowledge gaps. To bridge this gap, we propose NeuFS, a Neuron-Aware Active Few-Shot Learning framework that shifts the selection paradigm from output-level proxies to models' internal dynamics. NeuFS utilizes neuron activation patterns to represent sample directly, and includes a dual-criteria selection strategy that: (1) ensures few-shot sample diversity with neuron patterns for broader example coverage, while (2) prioritizing on identifying informative and challenging few-shot samples LLMs tend to hallucinate by quantifying neuron consensus. Experiments on three datasets demonstrate that NeuFS excels in both reasoning and text classification tasks, outperforming existing AFSL baselines. Ablation studies further highlight that internal neuron activations provide a more principled and effective selection signal than external embeddings, validating the superiority of the proposed NeuFS.

---


### 121. [Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach](https://arxiv.org/abs/2607.02432)

**<font color=#1a73e8>作者：</font>** Manuel Alonso-Carracedo, Ruben Fernandez-Boullon, Pedro Celard 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scalable and reliable grading of command-line examinations remains a challenge in computing education, where rising enrolments make manual marking difficult and rule-based autograders cannot handle partial credit, equivalent solutions, or syntactic variation. This paper evaluates whether four frontier Large Language Models (GPT, Claude Opus, Gemini, and GLM) can approximate expert judgment when grading short Linux/bash command responses. The study adopts a four-level cognitive taxonomy that combines cognitive complexity and operational impact, ranging from information retrieval (L1) and basic file manipulation (L2) to structural operations (L3) and advanced system management (L4). The models were tested with two prompt variants, a minimal baseline and a rubric-enhanced version, on 1200 real responses from second-year Computer Engineering students independently graded by three expert instructors. Gemini~3.0 Pro with rubric-guided prompting achieved the highest human-AI agreement (ICC(3,1) = 0.888, MAE = 0.10, Bland-Altman bias = -0.014). Agreement declined consistently as taxonomy level increased, with the largest discrepancies at higher levels. Across all models, rubric quality had a larger effect than provider choice, with structured prompts consistently improving agreement. These results show that question complexity is a reliable predictor of the difficulty LLMs face in grading accurately, and they establish a principled, taxonomy-based framework for determining which questions are suitable for AI-assisted grading and which require human review, while also providing a transferable evaluation protocol and prompt templates.

---


### 122. [AgentsCAD: Automated Design for Manufacturing of FDM Parts via Multi-Agent LLM Reasoning and Geometric Feature Recognition](https://arxiv.org/abs/2607.02448)

**<font color=#1a73e8>作者：</font>** Emmanuel George, Christopher Keefe, Peter Pak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Parts manufactured with Fused Deposition Modeling (FDM) often require Design for Additive Manufacturing (DFAM) modifications to ensure printability, structural integrity, and reduced post-processing. Current slicers identify defects such as steep overhangs but are unable to modify the underlying geometry. This work presents AgentsCAD, a multi-agent system that bridges raw boundary-representation (B-Rep) geometry and Large Language Model (LLM) reasoning to automate targeted DFM. The workflow begins by parsing a STEP file. The agentic system detects overhangs above a 45°threshold, constructs a face-adjacency topology graph, and optionally injects semantic feature labels from a GraphSAGE model trained on MFCAD++ (59,665 parts), before dispatching a Claude Sonnet design-reasoning agent that recommends reorientations, fillets, chamfers, and similar modifications. A GPT-4o vision-language verifier inspects rendered views to confirm geometric integrity. Outputs include a modified STEP file and a human-readable report. A test case on a birdhouse model demonstrates that the system correctly diagnoses overhangs, selects appropriate defect mitigation strategies, and proposes physically valid corrections, partially solving the geometry-to-language translation problem central to LLM-driven CAD modification.

---


### 123. [When Do LLM Personas Support Visualization Design? A Cross-Model Study of Color Assignment and Chart Choice](https://arxiv.org/abs/2607.02455)

**<font color=#1a73e8>作者：</font>** Shahreen Salim, Klaus Mueller  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language model personas are increasingly used to approximate diverse users during early-stage visualization design, but it remains unclear whether persona-conditioned outputs reflect stable personality effects or artifacts of model choice and task framing. We examine this question across two visualization-relevant tasks: color assignment for abstract and concrete concepts, and chart-idiom preference ratings across task contexts. Using 43 Big Five profiles across GPT-4o-mini, GPT-4.1-mini, and GPT-5-mini, we find that personality-color coupling is highly model-configuration dependent: absent in GPT-4o-mini for all six concepts, consistent in GPT-4.1-mini across all six, and partial in GPT-5-mini for two of six. Concept type further shapes the signal: for abstract concepts, personality explains more hue variance than model identity, while concrete concepts show smaller and comparable effects. In chart choice, trait-aligned cluster aggregation produces stable top-idiom rankings across all nine cluster-context combinations, but a no-persona baseline recovers the same top choice in 8 of 9 model-context cells, indicating that task context drives rank-1 selection more than personality. These findings position LLM personas as exploratory probes for visualization design, not substitutes for human participants, and motivate multi-model testing, concept-type disaggregation, and no-persona baselines in future studies.

---


### 124. [Language Models as Measurement Apparatus for Culture](https://arxiv.org/abs/2607.02459)

**<font color=#1a73e8>作者：</font>** Kent K. Chang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly used to quantify cultural phenomena, but what makes such measurement distinctively cultural? This paper argues that NLP work on culture is a material-discursive practice: the apparatus -- model, data, annotation, evaluation -- participates in constituting the cultural reality it measures, rather than passively recording it. Drawing on Karen Barad's concept of the agential cut -- the contingent boundary between phenomenon and instrument -- I show that the apparatus's substantive design choices draw such boundaries, and that the boundary is entangled from the start because language models have already internalized much of the cultural material they measure. I illustrate this through three case studies on television and film dialogue (measuring structure, interaction, and deviation) and three examinations of the apparatus itself (erasure of cultural markers, attunement to historical material, and agency in an agentic workflow). This big picture analysis proposes a research program that is theory-driven, empirically rigorous, and culturally contingent, treating each agential cut as a conscious commitment, at once methodological and ethical.

---


### 125. [Neuron-Aware Data Selection for Annotation-Free LLM Self-Distillation](https://arxiv.org/abs/2607.02460)

**<font color=#1a73e8>作者：</font>** Zhuowei Chen, Xiang Lorraine Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training large language models (LLMs) without real-world interaction feedback or human-labeled supervision remains challenging, particularly in specialized domains where expert annotations are costly to obtain. Recent annotation-free self-evolution methods address this by using the model's own outputs as supervision signals, constructing a teacher via additional context and aggregating predictions across multiple rollouts through majority voting to produce pseudo-labels. However, these approaches are not without drawbacks: SFT- and GRPO-based variants suffer out-of-domain performance degradation, while reward-based on-policy RL inflates calibration error. In this paper, we propose Neuron On-Policy Self-Distillation (Neuron-OPSD), a data-centric framework for annotation-free self-distillation that leverages internal neuron activations to guide both training-data selection and teacher context construction. The model is then trained via on-policy distillation from the teacher distribution, requiring no ground-truth labels at any stage. Across specialized-domain benchmarks, Neuron-OPSD improves in-domain task performance while preserving cross-domain generalization and mitigating calibration collapse over prior annotation-free baselines. This framework is particularly relevant to settings where online interaction or external supervision is costly or infeasible, and is conceptually distinct from offline RL approaches that rely on logged, reward-labeled trajectories.

---


### 126. [Will Scaling Improve Social Simulation with LLMs?](https://arxiv.org/abs/2607.02464)

**<font color=#1a73e8>作者：</font>** Caleb Ziems, William Held, Su Doga Karaca 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) social simulations are a promising research method, but they are not yet faithful enough to be adopted widely. In this work, we investigate whether the current scaling paradigm in language modeling is likely to close these gaps, or whether simulation fidelity is orthogonal to general capabilities and therefore deserving of more research attention. We use scaling laws to study the relationship between LLMs' compute scale, general capability benchmarks, and the fidelity of social simulation in three representative sub-domains: opinion modeling, behavioral simulation, and longitudinal forecasting. Surprisingly, we discover strong compute scaling in all three settings, using a suite of 85 transformer LLMs with the Qwen3 architecture pre-trained on the DCLM web text corpus under fixed-compute budgets from $10^{18}$ to $10^{20}$ FLOPs. Then we evaluate 35 larger and more capable open-weight models up to 70B parameters, allowing us to predict downstream accuracy from loss. This reveals that the majority of behavioral and opinion simulation tasks will rapidly improve with scale, particularly when they involve populations that are well-represented in English web corpora. Longitudinal forecasting and underrepresented opinions scale more slowly, especially when they are less correlated with general knowledge and reasoning benchmarks like MMLU. In behavior simulation, scaling fails to improve model calibration with human cognitive biases like risk aversion, as well as human heuristics like learning correlated rewards from related tasks. On these tasks, even fine-tuned models fail to noticeably scale up performance from 0.5B to 8B parameters. Taken together, we conclude that scale will improve social simulations in most settings, but outliers exist, and improvements will be less reliable in low-resource domains.

---


### 127. [EAGLE-360: Embodied Active Global-to-Local Exploration in 360$^\circ$](https://arxiv.org/abs/2607.02479)

**<font color=#1a73e8>作者：</font>** Jingtao Xu, Zizhuo Lin, Jianwen Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) have demonstrated exceptional capabilities in standard visual understanding, adapting them for active visual search in 360$^\circ$ panoramic environments exposes fundamental limitations. Specifically, standard MLLMs struggle to effectively model inherent panoramic properties, such as severe polar distortion and continuous cylindrical topologies, which significantly degrades target detection accuracy. Consequently, existing panoramic search methods attempt to compensate by relying heavily on fragmented local viewpoints. Burdened by rigid initialization and a lack of global panoramic priors, these approaches suffer from myopic, inefficient exploration and struggle with robust error recovery when targets are out of view. To overcome these challenges, we propose EAGLE-360, a novel Embodied Active Global-to-Local Exploration framework. Rather than performing exhaustive local searches, EAGLE-360 leverages global priors to establish an initial holistic perspective, iteratively reasoning and progressively narrowing the search space. Architecturally, we adapt RoPE Rolling, a coordinate-shifting positional encoding mechanism, to seamlessly model the continuous topologies of panoramas. To facilitate this paradigm, we construct the large-scale EAGLE-360 dataset, comprising 14,000+ 4K panoramas and 70,000+ rounds of high-quality VQA dialogues. By employing a training pipeline that integrates Supervised Fine-Tuning (SFT) with Group Relative Policy Optimization (GRPO), we effectively elicit complex spatial reasoning and tool-calling capabilities. Extensive experiments demonstrate that EAGLE-360 establishes a new state-of-the-art for 360$^\circ$ visual search, achieving nearly an 8-fold increase in accuracy over the base model while significantly enhancing exploration efficiency.

---


### 128. [Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning](https://arxiv.org/abs/2607.02490)

**<font color=#1a73e8>作者：</font>** Liyan Tang, Fangcong Yin, Greg Durrett  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large vision-language models can reason over multimodal inputs by generating textual chains of thought (CoT). A key capability exhibited in CoT reasoning is self-reflection: revisiting earlier decisions and correcting previous errors. However, existing LVLMs often fail to properly attend to visual inputs during reflection, limiting their ability to translate feedback into grounded corrections, especially for out-of-distribution images. To address this issue, we propose a novel reinforcement learning training framework VRRL, with two components explicitly designed to elicit visually grounded self-reflection. First, we randomly mask trajectory prefixes during training to emphasize recovery from incorrect intermediate predictions rather than making early mistakes. Second, we introduce buffered roll-ins from an experience replay buffer to expose the model to diverse failure states that it must learn to correct. We evaluate our approach on visual grounding tasks involving tables and charts, as well as spatial navigation benchmarks. While off-the-shelf and conventionally fine-tuned models degrade substantially under distribution shift, our method substantially improves average out-of-distribution accuracy over standard RL and reflection-oriented fine-tuning baselines by using self-reflection effectively.

---


### 129. [G-RRM: Guiding Symbolic Solvers with Recurrent Reasoning Models](https://arxiv.org/abs/2607.02491)

**<font color=#1a73e8>作者：</font>** Timo Bertram, Sidhant Bhavnani, Richard Freinschlag 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this work, we focus on SE-RRMs, a symbol-equivariant instantiation of RRMs that exhibits improved extrapolation to larger problem sizes. We propose a neuro-symbolic approach, ``Guiding with Recurrent Reasoning Models'' (G-RRM), which integrates SE-RRMs with symbolic solvers for constraint satisfaction problems. SE-RRMs act as neural solvers that generate full solution proposals and guide classical symbolic solvers, such as backtracking or SAT-based methods like Glucose 4.1 and CaDiCaL 3.0.0, that produce globally correct solutions. Centrally, we investigate when neural guidance with G-RRM improves the search efficiency of symbolic solvers. %
Our experiments show that the efficacy of G-RRM depends on two conditions: first, the problem instances must have an expansive combinatorial search space to expose potential gains, and second, the solver architecture must be capable of dynamically overwriting its branching choices to recover when neural hints are imperfect. When these conditions hold, guidance drives median conflict counts to zero and yields significant wall-clock speedups: on $9\times9$ Sudoku, where the SE-RRM correctly solves $91.1\%$ of instances, backtracking accelerates by $33.3\times$ and Glucose 4.1 by $1.70\times$ (median, $p<0.001$), with Glucose 4.1 retaining a $1.17\times$ speedup on perfect-hint $25\times25$ grids. In contrast, CaDiCaL 3.0.0, whose runtime is overhead-dominated and which always respects the injected branching hints rather than overwriting them, shows no significant speedup (median $1.02\times$, n.s.) and even a small significant mean slowdown ($0.90\times$) on $9\times9$. These results delineate the regimes in which neural guidance translates into practical speedups.

---


### 130. [Seek to Segment: Active Perception for Panoramic Referring Segmentation](https://arxiv.org/abs/2607.02497)

**<font color=#1a73e8>作者：</font>** Song Tang, Shuming Hu, Xincheng Shuai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing referring segmentation models passively process static images captured from fixed perspectives, limiting their applicability in Embodied AI, where agents must perform active perception in the continuous 360$^\circ$ environments. To bridge this gap, we introduce a novel task: Active Panoramic Referring Segmentation (APRS). In this setting, an agent is required to adjust its viewing direction ($\Delta\theta, \Delta\phi$) to explore the 360$^\circ$ environment, seeking the object specified by a user instruction for segmentation. To tackle this challenging task, we propose PanoSeeker, a memory-augmented agent for efficient APRS. Rather than relying on heuristic scanning, PanoSeeker integrates a Vision-Language Model (VLM) with EgoSphere, an explicit spatial visual memory. By progressively integrating sequential local observations into a unified 360$^\circ$ representation, EgoSphere enables the agent to plan efficient and non-redundant search trajectories. Once the target is found, the agent performs active viewpoint alignment and outputs the segmentation mask. Furthermore, we curate an expert-annotated search trajectory dataset with memory timelines for Supervised Fine-Tuning, followed by Reinforcement Learning post-training to explicitly optimize PanoSeeker's exploration efficiency. Extensive experiments on our newly established APRS benchmark demonstrate that PanoSeeker achieves superior search efficiency and segmentation accuracy, significantly outperforming adapted state-of-the-art baselines.

---


### 131. [Reasoning LLM Improves Speaker Recognition in Long-form TV Dramas](https://arxiv.org/abs/2607.02504)

**<font color=#1a73e8>作者：</font>** Yuxuan Li, Lingxi Xie, Xinyue Huo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-form TV dramas present a formidable challenge for comprehensive video understanding, where deciphering complex storyline often relies on \textbf{speaker recognition}, the task of accurately attributing each spoken utterance to its respective character. In this paper, we advance this field through two primary contributions. (1) We introduce \textbf{DramaSR-532K}, a large-scale benchmark comprising 532K annotated dialogue lines across more than 900 unique characters, necessitating the integration of auditory, linguistic, and visual cues for speaker recognition. (2) We propose \textbf{DramaSR-LRM}, a robust approach built upon a large reasoning model (LRM). DramaSR-LRM is designed to autonomously aggregate contextual evidence via multimodal tool-use, synthesizing diverse inputs to achieve high-fidelity attribution. Experimental results demonstrate that DramaSR-LRM significantly outperforms existing baselines, particularly on short utterances where acoustic biometrics are inherently unreliable. \textit{All the data and code will be made publicly available at the project page: this https URL.}

---


### 132. [What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Debates](https://arxiv.org/abs/2607.02507)

**<font color=#1a73e8>作者：</font>** Arman Ghaffarizadeh, Danyal Mohaddes, Aliakbar Izadkhah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents will increasingly act in socially structured settings where role, audience, and relational context can shape what is advantageous or costly to say. We study whether such social structure, without any explicit objective in the prompt, changes what an agent expresses publicly relative to an off-the-record (OTR) channel elicited under the same condition. We introduce a dual-channel debate framework in which agents produce public utterances that enter the shared history alongside OTR responses that are recorded but never shown to the other participant. Across 10 models, 3 scenarios, and 5 variations within each scenario, alignment-inducing settings produce systematic public-OTR divergence in the targeted agent, with its decision divergence rising from a $\sim$3% baseline to roughly 40%. The effect is consistent across four aggregate analyses: stance, semantic similarity, natural language inference, and survey responses. In some cases, the OTR response explicitly attributes public accommodation to relational pressures, such as career risk or sponsorship obligation. The findings suggest that agent evaluation should extend beyond explicit goals and detect emergent objectives. We present a dual-channel evaluation framework and complementary behavioral measures that operationalize this assessment.

---


### 133. [ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning](https://arxiv.org/abs/2607.02509)

**<font color=#1a73e8>作者：</font>** Yanjun Zhao, Ruizhong Qiu, Tianxin Wei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding and reasoning over long contexts has become a key requirement for deploying large language models (LLMs) in realistic applications. Although recent LLMs support increasingly long context windows, they often fail to use relevant evidence that is already present in the input, revealing a gap between context access and effective context utilization. In this work, we propose Recursive Evidence Replay as LLM Harness for Long-Context Reasoning (RECONTEXT), a training-free inference method for improving long-context reasoning. RECONTEXT uses model-internal relevance signals to construct a query-conditioned evidence pool and replays it before final generation while preserving the full original context. This recursive selection process separates evidence organization from answer generation without training, external memory, or context pruning. We also provide a theoretical analysis based on associative memory, which characterizes the context as a memory store, the question as a retrieval cue, attention as cue-trace association, and replay as trace reactivation. Experiments on eight long-context datasets with 128K context length show that RECONTEXT consistently improves evidence utilization across Qwen3-4B, Qwen3-8B, and Llama3-8B, achieving the best average rank on all three backbones. Code is available at this https URL.

---


### 134. [Online Safety Monitoring for LLMs](https://arxiv.org/abs/2607.02510)

**<font color=#1a73e8>作者：</font>** Mona Schirmer, Metod Jazbec, Alexander Timans 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite alignment training, LLMs remain prone to generating unsafe outputs at deployment time. Monitoring outputs online and raising an alarm when safety can no longer be assumed is therefore critical. We study a simple real-time monitor that turns a verifier signal from an external model into an alarm decision by thresholding, with the threshold calibrated via risk control. In experiments on mathematical reasoning and red teaming datasets, we show that this simple design is competitive with more advanced monitors based on sequential hypothesis testing.

---


### 135. [Program-as-Weights: A Programming Paradigm for Fuzzy Functions](https://arxiv.org/abs/2607.02512)

**<font color=#1a73e8>作者：</font>** Wentao Zhang, Liliana Hotsko, Woojeong Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many everyday programming tasks resist clean rule-based implementation, such as alerting on important log lines, repairing malformed JSON, or ranking search results by intent, and are increasingly outsourced to large language model APIs at the cost of locality, reproducibility, and price. We propose fuzzy-function programming: compiling such a function from a natural-language specification into a compact, locally-executable neural artifact. We instantiate this paradigm with Program-as-Weights (PAW), in which a 4B compiler trained on FuzzyBench, a 10M-example dataset we release, emits parameter-efficient adapters for a frozen, lightweight interpreter. A 0.6B Qwen3 interpreter executing PAW programs matches the performance of direct prompting of Qwen3-32B, while using roughly one fiftieth of the inference memory and running at 30 tokens/s on a MacBook M3. PAW reframes the foundation model from a per-input problem solver into a tool builder: invoked once per function definition, it produces a small reusable artifact whose subsequent calls per function application are cheap and offline.

---


### 136. [LACUNA: A Testbed for Evaluating Localization Precision for LLM Unlearning](https://arxiv.org/abs/2607.02513)

**<font color=#1a73e8>作者：</font>** Matteo Boglioni, Thibault Rousset, Siva Reddy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs memorize sensitive training data, including personally identifiable information (PII), creating a pressing need for reliable post hoc removal methods. Unlearning has emerged as a promising solution, with state-of-the-art(SOTA) methods often following a localize-first, unlearn-second paradigm that targets specific model parameters. However, existing benchmarks evaluate unlearning solely at the output level, leaving open the question of whether unlearning truly erases knowledge from a model's parameters or merely obfuscates it, a concern reinforced by the success of resurfacing attacks. To bridge this gap, we introduce LACUNA: the first unlearning testbed with ground-truth parameter-level localization. LACUNA injects PII of synthetic individuals into predefined parameters of 1B and 7B OLMo-based models via masked continual pretraining, enabling direct evaluation of whether unlearning targets the weights responsible for knowledge storage. We use LACUNA to benchmark current SOTA unlearning methods and find that, despite strong output-level performance, existing methods are highly imprecise and susceptible to resurfacing attacks. We further show that when localization is successful, even a simple gradient-based unlearning method achieves strong erasure and robustness to resurfacing attacks, highlighting the importance of precise unlearning. We release LACUNA to complement behavioral evaluations and drive further advances in robust, localization-based unlearning.

---


> [!TIP]
> 当前位于：**101-136**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-136**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
