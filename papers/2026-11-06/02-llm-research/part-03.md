# 🧠 大模型相关研究 | 2026年11月06日

> 本类共 **207** 篇论文：已确认 **189** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-207](./part-05.md)

---

### 101. [Grounding in the Dark: Text-Only Training for Zero-Shot Video Temporal Localization](https://arxiv.org/abs/2611.06149)

**<font color=#1a73e8>作者：</font>** Divyanshu Mishra, Sabine Sternig, Rakshith Shetty 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-LLMs are typically trained on paired video-text data for temporal tasks, yet collecting precise temporal annotations and training on large-scale video datasets are both costly. We investigate whether a text-only LLM, with no vision-language pretraining, can be trained on textual video descriptions alone to perform temporal grounding and receive video only at inference time. This setting removes paired video data from training altogether and is a step toward training multimodal models without paired annotations. We generate a 134K-example corpus of textual sequences with up to 100 time steps, adapt Qwen3-8B with LoRA on CLIP or LLM2CLIP text embeddings, and evaluate on Charades-STA and QV-Highlights without training on videos from either benchmark. LLM2CLIP, whose text encoder supports longer inputs, represents detailed descriptions better than CLIP (61.54 versus 53.86 mtIoU on Temporal-TextVid) and transfers them better to video. Still, replacing text with frame embeddings at inference yields only 4.99 mtIoU on Charades-STA and 11.12 on QV-Highlights, revealing a large modality gap. To bridge it, we propose Nearest Entity Replacement (NER), a training-free mapping that represents each video frame by the normalized mean of its nearest text-entity embeddings, so that the model receives the kind of input it was trained on. NER reaches 14.45 mtIoU on Charades-STA and 20.72 on QV-Highlights, outperforming the strongest of four families of modality-gap baselines by 5.00 and 1.71 points. NER thus enables partial transfer from text to video, while more reliable grounding will likely require encoders with better-aligned text and visual representations.

---


### 102. [DSRS: Teaching MLLMs to Perceive, Reason, and Segment in Complex Driving Scenes](https://arxiv.org/abs/2611.06160)

**<font color=#1a73e8>作者：</font>** Sicen Guo, Zhengfei Song, Kuanhsun Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing reasoning segmentation frameworks typically employ multimodal large language models (MLLMs) with broad world knowledge to extract semantics in a human-like manner and generate corresponding segmentation masks. Nevertheless, these frameworks lack the necessary scene-specific awareness. This paper introduces driving scene reasoning segmentation (DSRS), a scene-specific task that requires models to interpret implicit instructions, infer spatial relations, detect potential risks, handle challenging conditions, and comprehend underlying traffic rules, ultimately generating accurate segmentation masks. Meanwhile, we establish a benchmark dataset to facilitate future research on the DSRS task. To pioneer this task, we propose DSRS-Net, a novel architecture with advanced reasoning segmentation capability for automated driving. Specifically, DSRS-Net seamlessly infuses geometric features for deeper reasoning segmentation, without compromising the original multimodal fusion mechanism. This strategy effectively mitigates the modality representation mismatch in MLLMs caused by RGB-only pretraining, while enhancing the integration of geometric, contextual, and linguistic features. Extensive experiments demonstrate the superior performance of DSRS-Net in both driving scene reasoning segmentation and other language-driven segmentation tasks across various public datasets. The source code and dataset will be released upon publication.

---


### 103. [Reasoning-Aware Cross-Modal Association Unlearning in Multimodal Large Reasoning Models](https://arxiv.org/abs/2611.06168)

**<font color=#1a73e8>作者：</font>** Xinghao Li, Chenchen Tan, Youyang Qu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large reasoning models (MLRMs) integrate visual inputs with textual and parametric knowledge, allowing sensitive information to be accessed through cross-modal associations during reasoning. This raises privacy concerns when a visual input should no longer provide access to such information. Machine unlearning can remove this influence without retraining the model from scratch. However, multimodal unlearning methods mainly target samples, concepts, or knowledge content, without separating the knowledge from the cross-modal association through which it is accessed. In reasoning models, target information may disappear from the final answer while remaining in intermediate reasoning, or be replaced by incorrect substitute knowledge. We therefore study cross-modal association unlearning, where the forget target is a designated visual-to-knowledge association: the model should suppress target-bearing behavior under the designated visual context while preserving access to the same knowledge in permitted contexts. We propose Visual-Keyed Counterfactual Rebinding (VKCR), a parameter-efficient framework for cross-modal association editing. VKCR first localizes the edit to a compact association-conditioned parameter subspace. It then reduces support for the designated target at task outputs and counterfactually rebinds the affected reasoning behavior by discouraging target-bearing or unsupported continuations while favoring valid non-sensitive alternatives. We further introduce CLEAR-R and MLLMU-R to evaluate target leakage, hallucinated reassociation, reasoning preservation, and modality-specific utility. Experiments show that VKCR substantially reduces image-conditioned target leakage and hallucinated reassociation, including across heterogeneous task formulations, while preserving non-sensitive visual reasoning and permitted text-only knowledge.

---


### 104. [AssameseLM-E2B: An Open-Weight Assamese Language Model for Efficient Consumer-Grade Deployment](https://arxiv.org/abs/2611.06170)

**<font color=#1a73e8>作者：</font>** Pragyan Phukan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) excel in high-resource languages, their performance often degrades in low-resource languages due to tokenization inefficiencies, generative instability, and linguistic interference. This paper presents AssameseLM-E2B and its instruction-tuned variant, AssameseLM-E2B-it, a 2-billion-parameter model adapted specifically for low resource Assamese language. Built upon the Gemma-4 architecture, the model incorporates an expanded byte-level BPE vocabulary to reduce tokenization overhead by nearly 500% compared with multilingual 2B--3B baselines. We employ a parameter-efficient Continual Pre-Training (CPT) pipeline with Hybrid LoRA, followed by Supervised Fine-Tuning (SFT) on a balanced, multi-domain dataset to enhance instruction-following and Retrieval-Augmented Generation (RAG) capabilities.
Evaluation demonstrates a Bits-per-Byte (BPB) score of 0.7488 on FLORES-200, alongside an overall RAG score of 96.7% and 100% refusal accuracy on adversarial unanswerable prompts. Comparative analysis reveals significant limitations in general-purpose baselines, including receptive-productive decoupling, generative degradation on Romanized Assamese, and unintended Bengali script assimilation. These results demonstrate the potential of parameter-efficient adaptation for developing capable, locally deployable language models for low-resource languages under constrained computational resources.

---


### 105. [Editing Large Language Models with Geometry-Aware Regularization](https://arxiv.org/abs/2611.06185)

**<font color=#1a73e8>作者：</font>** Bingqing Liu, Wei Liu, Jun Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge editing has become a key technique for updating knowledge in large language models. However, existing methods neglect the geometric structure of the knowledge representation space, leading to two key limitations: they cannot distinguish which pre-trained knowledge should be preferentially preserved (core vs. non-core) nor which new edits are inherently difficult (hard vs. easy). To address this, we propose GEdit, a geometry-aware framework built on a Low-Rank Plus Diagonal (LR+D) factor model that captures the intrinsic low-rank structure of Transformer FFN hidden representations. GEdit features two complementary mechanisms. First, the low-rank regularization applies targeted protection on a low-rank core knowledge subspace. Second, the adaptive regularization dynamically adjusts the regularization strength based on each edit request's editability: relaxing constraints for hard edits to ensure success, and tightening them for easy edits to better preserve pretrained knowledge. Extensive experiments on GPT2-XL, GPT-J, and LLaMA-3-8B under large-scale editing scenarios, including both mini-batch and fully sequential editing settings with up to 10,000 continuous updates, show that GEdit consistently and significantly outperforms state-of-the-art baselines in both editing success and knowledge preservation.

---


### 106. [Annotator-Free Object Detection via Foundation Model Collaboration](https://arxiv.org/abs/2611.06195)

**<font color=#1a73e8>作者：</font>** Yasiru Ranasinghe, Vishal M. Patel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection research remains constrained by high annotation costs and the closed-set assumptions of supervised models, limiting scalability to novel categories. We present a target-dataset annotation-free object detection framework that eliminates the need for human labeling on the target dataset by leveraging the complementary strengths of pretrained foundation models, including segmentation and vision-language systems, combined with a self-refining training loop. To further reduce reliance on expensive LVLM queries, we introduce a landmark-based clustering mechanism that amortizes labeling across image clusters, improving label consistency while lowering computational cost. Our method autonomously generates segmentation proposals, assigns semantic labels through multimodal reasoning, and iteratively improves both localization and classification using a lightweight open-set detector. This modular pipeline enables adaptation to completely unseen object classes and domains without any human-provided target-dataset annotations, while maintaining compatibility with existing detection architectures. Evaluations on COCO, LVIS, ODinW-35, and Roboflow-100 demonstrate substantial performance gains over state-of-the-art open-vocabulary and long-tail detection methods, achieving 60.8 AP on COCO and 47.4 AP on LVIS under zero-shot settings. Beyond strong benchmark results, our approach provides a scalable foundation for real-world detection systems in unknown environments, where annotation is infeasible.

---


### 107. [Beyond the Landing Page: Website Blocking, Tracker Visibility, and Human Alignment in Automated Web Crawls](https://arxiv.org/abs/2611.06197)

**<font color=#1a73e8>作者：</font>** A H M Nazmus Sakib, Mahsin Bin Akram, Raveen Wijewickrama 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Web tracking studies largely rely on automated crawlers, yet their measurements can differ from what people encounter while browsing. Conventional crawlers follow predefined navigation rules, whereas LLM-driven agents decide how to navigate and interact with websites, potentially changing the tracking they encounter. We compare agentic and non-agentic crawlers to examine how websites respond to them, what tracking they record, and how closely their observations match human browsing. Across 2,000 popular websites, we evaluate different navigation strategies, automation frameworks, and stealth configurations, alongside browsing data from 26 participants. We find that website denials increase beyond landing pages for standard browser automation, while a detection-resistant automation framework largely prevents this escalation without increasing recorded tracking. On the same URLs, agentic crawlers record tracking activity from 1.5-1.7 times as many third-party organizations, particularly on consent-managed pages. Agentic crawlers recover 82-87% of tracker organizations observed by participants, compared with 58-68% for non-agentic crawlers, yet roughly half of their own observations are absent from human participant visits. These findings show that avoiding website interventions, increasing tracking visibility, and achieving closer agreement with human observations do not necessarily go hand in hand, highlighting the need to select and validate crawlers according to the measurement objective.

---


### 108. [HarnessFlow: MCTS-Guided Harness Optimization for LLM Agents](https://arxiv.org/abs/2611.06254)

**<font color=#1a73e8>作者：</font>** Zhi Hong, Qianlong Wang, Hongchen Wei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The performance of large language model (LLM) agents depends on both the underlying model and the harness that governs interaction with tools and the environment. Yet harness design remains largely manual, and automating it requires navigating an open-ended search space through costly end-to-end evaluations. We introduce HarnessFlow, a framework for optimizing complete executable harnesses under a limited candidate-evaluation budget, with the model and task environment held fixed. HarnessFlow organizes candidates and their evaluation histories in a refinement tree, using a Monte Carlo Tree Search (MCTS)-based policy to balance exploitation and exploration. A coding agent refines selected harnesses using archived code, execution feedback, and a library of reusable harness mechanisms. With 15 refinement attempts per benchmark, HarnessFlow achieves the highest mean test scores among the compared methods on six benchmarks spanning agentic tasks, coding, and web interaction. The optimized harnesses achieve an average score of 69.48%, outperforming the initial harnesses and Meta-Harness by 10.89 and 3.95 percentage points, respectively, while incurring lower average per-task execution costs than hand-engineered baselines. These results suggest that structured harness search offers a promising route toward automating the design of capable and efficient LLM agents.

---


### 109. [Analysis of Local Open-Weight LLM Agents on Vulnerability-Reproduction Tasks](https://arxiv.org/abs/2611.06257)

**<font color=#1a73e8>作者：</font>** Jorge García-Carrasco, Javier Sanchis, Álvaro Navarro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-weight language models that fit on a single consumer GPU are becoming capable on a growing range of tasks, and they matter because they can run locally without sending the code to a hosted service. Vulnerability reproduction, turning a vulnerability description into an input that crashes the vulnerable build, is a natural target for them, since it is an automated analysis task closer to test generation than to code comprehension and it runs against a build that must be executed rather than read. In order to assess whether current models can perform it, we evaluate twelve configurations of local models, spanning three generations, two architectures and three quantization levels, on ten CyberGym vulnerability-reproduction tasks, three runs each under one harness, and release the full artefact. We show that every configuration, down to the 4B model, solves most of the six easier tasks, and configurations separate only on the remaining four. For the harder tasks, the 27B model is required. Quantization did not change what the models solved in any matched pair, but it changed how fast they got there, and the mixture of experts reached the same scores in less wall clock. We also examine the agent trajectories. Almost every run we examined, including those that fail, names the vulnerable function and states the correct hypothesis, and what separates a solved task from an unsolved one is whether that hypothesis becomes a working input.

---


### 110. [A Systematic Benchmark for Evaluating Multimodal Personalized Reasoning of Vision-Language Models](https://arxiv.org/abs/2611.06259)

**<font color=#1a73e8>作者：</font>** Dohyun Kim, Junyong Lhim, Kwanyong Park  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> People often make decisions by holistically reasoning over heterogeneous forms of personal information. In this paper, we study the relatively underexplored capability of multimodal personalized reasoning in multimodal large language models (MLLMs). To this end, we introduce \texttt{MPRBench}, a novel and comprehensive benchmark specifically designed to evaluate personalized reasoning across a wide range of tasks and real-world challenges. \texttt{MPRBench} consists of 12 sub-tasks and additionally supports interpretable analysis of representative error cases. Through extensive experiments, we find that current personalized MLLMs still struggle with personalized reasoning due to several key challenges, including inaccurate recognition of personalized concepts and sensitivity to irrelevant personal information. We hope that MPRBench will stimulate further research on personalized reasoning in MLLMs. Code and data are available at this https URL

---


### 111. [Evaluating Human-LLM Alignment on Visualization Preference](https://arxiv.org/abs/2611.06272)

**<font color=#1a73e8>作者：</font>** Tanmay Bakshi, Chenglong Wang, Simra Shahid  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> There are often multiple valid visualizations, spanning different chart types, visual encodings, and aesthetic choices, that can all support a user's goal of analyzing a dataset. Determining which of these candidate visualizations is most appropriate, however, remains challenging. Prior work has leveraged expert-curated taxonomies to guide visualization design and subsequent quality evaluation, a practical evaluation model must also account for human-centric factors. Latest visualization tools integrate Large Language Models (LLMs) to generate and refine visualizations, using LLM-as-a-judge to provide design feedback. Without a deeper understanding of whether, and in what ways, human and LLM perceptions of visualizations align, there is a real risk of deploying low-quality agents that do not reflect human judgment. We study this question through a pilot experiment - we formulate the problem as a preference task over curated chart pairs and compare the judgments of state-of-the-art vision models with those of a panel of human annotators. We establish a cautionary tale: such judges risk filtering out informative, compelling displays. We find that frontier models collapse human subjectivity, a rich signal that reveals contrasting design choices, into near-deterministic verdicts.

---


### 112. [MonoLaDN: Language-Guided DeNoising for Monocular 3D Object Detection](https://arxiv.org/abs/2611.06282)

**<font color=#1a73e8>作者：</font>** Kiet Dang Vu, Cao Le Minh Khoa, Nguyen Viet Tri Pham 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular 3D object detection offers a low-cost route to 3D perception, but it remains fundamentally ill-posed, since depth must be inferred from a single view. Recent transformer-based detectors learn geometry purely from image features and 3D box annotations, lacking the high-level semantic priors that vision-language models (VLMs) acquire from large-scale pretraining. VLMs offer such priors, but deploying one directly as a detector is impractical due to its heavy inference cost. We propose MonoLaDN, a language-guided denoising framework that transfers the geometric reasoning of a VLM into a monocular 3D detector while keeping the deployed model purely vision-based. During training, a frozen VLM produces structured reasoning about each object's occlusion, depth, dimension, and angle from the image and its ground-truth boxes. We encode this reasoning into queries, perturb them with noise, and train the detector to reconstruct the clean reasoning. Reconstructing the corrupted reasoning forces the detector's depth-guided features to internalize the VLM's geometric priors, so this knowledge remains available even after the reasoning path is discarded at inference, adding no latency or parameters to the deployed model. Experiments on KITTI 3D and nuScenes show that MonoLaDN consistently outperforms state-of-the-art detectors and generalizes well to new domains.

---


### 113. [A.S.E 2.0: Understanding How Repository Context Impacts the Security of LLM-Generated Code](https://arxiv.org/abs/2611.06294)

**<font color=#1a73e8>作者：</font>** Jiongchi Yu, Keke Lian, Junqing Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) coding assistants and agents construct a repository context before generating code. For security-sensitive code, this context decides whether the model sees the project's safeguards (e.g., authorization checks) or insecure code to imitate. However, context construction is designed almost exclusively for functional correctness, and secure-code benchmarks treat the context as fixed, so how repository context affects the security of generated code remains unclear. We construct CASE-Bench, a benchmark of 145 repository-level tasks from real CVEs in 51 projects. Each task runs in Docker, has functional tests and a proof-of-concept exploit validated in both directions, and is annotated with the repository code that enforces or undermines its security. Using CASE-Bench, we compare 13 context construction methods and six controls with six LLMs, edit single context elements, and analyze coding-agent trajectories. We find that (1) functionality-oriented context raises the functional pass rate by up to 8.2 percentage points (pp) but the secure pass rate by at most 3.7 pp, (2) withholding a safeguard lowers the secure pass rate by up to 8.1 pp, while one inserted insecure exemplar raises correct-but-exploitable code by 6.3 pp, and (3) coding agents observe the relevant safeguard in only 27-36% of trajectories. These findings inform security-aware context construction and secure-code evaluation.

---


### 114. [Multi-Resident Data Association in Smart Homes via MDP Modeling and Behavior Cloning](https://arxiv.org/abs/2611.06296)

**<font color=#1a73e8>作者：</font>** Xi Chen, Julien Cumin, Fano Ramparany 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ambient sensors offer a privacy-preserving solution for activity recognition in smart homes, yet they face a critical challenge in multi-resident environments known as Data Association, which aims to identify the resident triggering a specific anonymous sensor event. Existing approaches fundamentally fail to maintain global consistency by often yielding conflicting associations for silent residents. Additionally, these methods frequently suffer from severe trajectory fragmentation caused by the ontological mismatch of applying continuous physical motion models to discrete logical behaviors. To address these limitations, we propose a novel framework that reformulates data association as a sequential decision-making task within a Markov Decision Process (MDP). We solve the defined MDP via Behavior Cloning (BC) to avoid complex reward engineering by directly learning from expert demonstrations. We instantiate the policy using two complementary architectures, including a lightweight Transformer that treats association as a multi-label classification task over linearized event histories, and a fine-tuned Large Language Model (LLM) that reformulates the problem as conditional text generation to leverage pre-trained semantic knowledge. Extensive evaluations on three diverse datasets demonstrate that our approach significantly outperforms state-of-the-art baselines, particularly in resolving concurrent multi-resident events. Furthermore, the LLM-based policy shows preliminary cross-environment transfer potential under benchmark settings, while its robustness in real deployments still requires further validation.

---


### 115. [Beyond Scene Shortcuts: Action-Centric Video-Text Alignment for Fine-Grained Action Understanding](https://arxiv.org/abs/2611.06302)

**<font color=#1a73e8>作者：</font>** Zhiliang Zhu, Jiazheng Huang, Dawei Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained action understanding requires vision-language models to ground what an agent does, how it acts, and why it acts in spatio-temporal evidence. However, richer supervision can backfire: fine-tuned models may generate detailed action descriptions grounded in static scenes and salient objects rather than motion, a failure we call Environment-Grounded Action Hallucination (EGAH). To mitigate EGAH, we propose Staged Attention Rectification and Reinforcement (STARR), an action-centric video-text alignment framework that breaks scene-action shortcuts through Action-Environment Dissociation and reinforces action-focused grounding with an Attention Consistency Reward within Group Relative Policy Optimization. We further construct FineActionR&R, combining temporally localized captions with hierarchical and temporal-causal reasoning data. Built on Qwen2.5-VL-7B, FineActionVLM-R1 improves average MotionBench accuracy by 3.01 percentage points over its base model and achieves 91.50% on HAU-MCQ-Bench. Qualitative comparisons further indicate more faithful fine-grained action descriptions with fewer environment-induced hallucinations.

---


### 116. [Mass Producing Training Data with Surprising Side Effects](https://arxiv.org/abs/2611.06324)

**<font color=#1a73e8>作者：</font>** Yaowen Ye, Jacob Steinhardt, Sarah Schwettmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training data can have unexpected side effects on language model behavior outside the training domain: insecure code data can induce broad misalignment, and outdated bird names can induce a 19th-century persona. Understanding such generalization is hard because only dozens of isolated examples exist, each constructed by hand or discovered by accident. We propose automatically discovering such datasets with surprising side effects (DSSEs). We define three objectives for DSSEs: they should (1) elicit a target behavior, (2) read like ordinary post-training data, and (3) be surprising to human auditors reading the data. We operationalize each with LLM judges, and search for high-scoring datasets via evolution, reinforcement learning, and subliminal learning approaches. After re-scoring and filtering with held-out metrics, our pipeline produces a collection of 6,575 DSSEs across 8 behaviors, many of which generalize across model families and sizes. We find our automated metrics track ML researchers' judgments, and frontier models outperform humans at predicting side effects. These datasets form a testbed for studying generalization and lay the groundwork for predicting training side effects before model deployment. Explore them at this https URL.

---


### 117. [CoRTeC: A Differentially Private Release for Synthetic Tabular Data, Decodable by Any Generator](https://arxiv.org/abs/2611.06342)

**<font color=#1a73e8>作者：</font>** Calister Nnona  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The records that could train the most useful models, such as a hospital's patient files, are often the ones an institution cannot share. We propose CoRTeC, a method that releases synthetic versions of such records under differential privacy. Differential privacy places a proven limit on what the synthetic data can reveal about any person, and in particular on membership inference. CoRTeC spends the privacy budget once, on a small file of noisy counts designed for training a classifier. For each group of records, the file gives the group's size, its balance of outcomes, a histogram of every column for each outcome and the outcome rate in each of several non-overlapping cells. A reviewer can check every number before the file leaves the institution. Anyone can then turn the counts into synthetic rows, as often as they like and at no further privacy cost. A maximum-entropy decoder can do this without any language model, and so can each of the five frozen language models we tested. None of them ever sees a real record. A selection step then matches the rows to the released counts. Decoded without a language model, the automatically configured release at $\varepsilon = 2$ trains classifiers to within 0.02 AUC of a real sample of the same size on the Adult dataset, across three data splits. On NHANES and bank marketing, without the selection step, it stays within 0.05 AUC. On Adult, with a fixed cohort rule, the release carries the outcome rates a deployment names more closely than a real sample does, at some cost in accuracy on pairs of columns. Four controls show that most of the utility comes from the release and the selection step, and that a language model adds what it knows from the column names. No private row ever reaches a model, and no row CoRTeC generates copies a real one. The strongest membership attack stays far below the bound the budget allows.

---


### 118. [Traffic-VL: Reinforced Vision-Language Models for Generalizable End-to-End Traffic Signal Control](https://arxiv.org/abs/2611.06353)

**<font color=#1a73e8>作者：</font>** Xingchen Zou, Maonan Wang, Kemou Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing traffic signal control methods typically rely on structured traffic states produced by dedicated perception pipelines. Emerging visual approaches often use idealized simulator images and convert them into intermediate representations before control, limiting their ability to directly exploit roadside visual observations. To bridge both the visual-domain and perception-to-decision gaps, we introduce SynTra-V and Traffic-VL. SynTra-V converts physics-based traffic simulations into photorealistic multi-view surveillance imagery across diverse road topologies and sensing conditions, and automatic semantic auditing checks that control-critical geometry, vehicle movements, and lane semantics match the simulator state. Traffic-VL is an eight-billion-parameter vision-language model that directly maps synchronized multi-view images and natural-language phase descriptions to signal decisions without intermediate structured states. Building on Traffic-R1's two-stage reinforced reasoning framework, Traffic-VL adapts its vision encoder via offline reinforcement learning on SynTra-V and freezes it during online visual stepwise trajectory policy optimization in closed-loop simulation. Experiments show that Traffic-VL matches structured-state Traffic-R1 while outperforming image-based controllers and general-purpose vision-language models, including Gemini 3 Pro. Evaluations on unseen topologies, degraded sensing conditions, real surveillance footage, and a three-week deployment across ten intersections further demonstrate robust visual generalization and effective constrained online control.

---


### 119. [Training-Free Character-Length Control in Summarization with Diffusion Language Models](https://arxiv.org/abs/2611.06371)

**<font color=#1a73e8>作者：</font>** Steffen Castle, Nils Feldhus, Christopher Ebert 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Summarization with a fixed character length is important for tasks such as headline and article preview generation, where text must fit an exact space. Autoregressive language models (LMs) struggle with precise character-length control: training-based methods require task-specific fine-tuning, while zero-shot prompting strategies achieve only approximate compliance. We propose DELTA (Diffusion Expected Length Targeting Algorithm), a training-free inference-time method for masked diffusion LMs that estimates expected character length at each denoising step and dynamically inserts or removes masked positions to steer toward a target length. DELTA requires no fine-tuning and is designed for off-the-shelf masked diffusion LMs. Across three summarization benchmarks, it reduces character-length errors by an order of magnitude compared to baselines while maintaining competitive summary quality in both automatic and human evaluation.

---


### 120. [Give Up to Get More: Priors, Not Policies, Govern Test-Time Compute Allocation](https://arxiv.org/abs/2611.06372)

**<font color=#1a73e8>作者：</font>** Jinhyung Bae  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When many inputs share a budget of repeated attempts by a large language model (LLM), a common rule gives harder inputs more. On public math, code and formal-proof samples, the best published difficulty-proportional rule captures half or more of the oracle gain on benchmarks the model mostly solves, but at most 13% on hard workloads, even given true pass rates. Because the value of one more attempt peaks at intermediate difficulty, the optimal static allocation is inverted-U and gives little to inputs that are hopeless at the current budget. In a strict survey of 221 LLM allocation papers, at least 13 give the hardest inputs the most attempts; their easier settings sit at budgets where this is near-optimal, so the cost appears on harder workloads. Acting on it requires knowing which inputs are solvable, so information, not the policy, drives the gain. With a verifier and a prior from a related model's past runs on the same inputs, Thompson Sampling raises the solved share on the hardest workload from 14% to 27%; without such a prior, no policy we tested beats round-robin. For the policies we tested, the gain vanishes between prior rank correlations of about 0.3 and 0.55, which cheap text-based priors barely reach on the weakest models, and it requires a verifier whose false acceptances are rare relative to the pass rate. On new Qwen2.5 samples the pattern holds, and tempering the prior avoids losses on easy workloads. We turn these results into a decision guide.

---


### 121. [NanoKV: High-Ratio KV Cache Compression for Autoregressive Video Generation](https://arxiv.org/abs/2611.06377)

**<font color=#1a73e8>作者：</font>** Jiacheng Lu, Haoyi Zhu, Sipei Yi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video models rely on historical key-value (KV) caches to preserve scene consistency over extended rollouts, making KV storage and repeated attention over history a growing memory and computational bottleneck. Aggressive compression can degrade generation quality, while reconstructing full-dimensional KV leaves attention computation largely unchanged. We introduce NanoKV, a frozen-backbone framework for generation-aware high-ratio KV compression. NanoKV exploits redundancy across tokens and attention heads by storing shared content in cluster centers and encoding joint head-channel residuals into low-bit coefficients. Crucially, NanoKV uses different fitting objectives for Keys and Values according to their distinct roles in attention: Key decoders are optimized to preserve downstream block outputs, whereas Value encoders and decoders are fitted for faithful reconstruction through the deployed quantization path. Building on the same compressed representation, the optional NanoKV-Fast variant reuses the stored coefficients for mixed-dimensional attention, reducing computation without modifying the video backbone. Across three autoregressive video backbones, NanoKV consistently improves the quality-storage trade-off. On HY-WorldPlay, NanoKV achieves $26.09\times$ effective KV compression, nearly twice that of KVTC, while improving PSNR by 1.0 dB. NanoKV-Fast retains $20.53\times$ effective compression and achieves an approximately $1.15\times$ end-to-end speedup over KVTC.

---


### 122. [Does Context Compression Preserve Refusal Alignment?](https://arxiv.org/abs/2611.06380)

**<font color=#1a73e8>作者：</font>** Anthony Nguyen, Wenjun Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Context compression reduces inference cost by encoding inputs into compact representations while preserving semantic content. An open question is whether semantic preservation alone is sufficient to maintain downstream behaviours such as refusal alignment. We investigate this question and find that encoder-based compression systematically weakens refusal behaviour in instruction-tuned language models, despite high reconstruction fidelity. This effect persists across model families and compression architectures. Mechanistic analysis shows that compression attenuates activation along the decoder's learned refusal direction. We further explore Memory Steering, a lightweight inference-time intervention that restores refusal rates to near-baseline levels without retraining and operates entirely in compressed representation space. These results demonstrate that semantic preservation does not guarantee behavioural preservation under compression, highlighting the need to explicitly preserve alignment-relevant features in compression-aware systems.

---


### 123. [LegalEvolver: Agentic Legal Judgment Prediction via Rubric-Guided Self-Evolution](https://arxiv.org/abs/2611.06381)

**<font color=#1a73e8>作者：</font>** Xinyu Yang, Jiejun Tan, Chenlong Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM-based agents develop, they have been increasingly applied in the legal domain. Legal Judgment Prediction~(LJP) requires models to conduct multi-step reasoning and external legal evidence retrieval. Existing legal search agents' performance is often constrained by the quality of retrieval queries. They often formulate queries directly from the initial user request, overlooking latent legal issues and legally salient details. To address this issue, we propose \emph{LegalEvolver}, a query optimization framework specifically designed to generate legally informative queries for LJP-oriented retrieval. Sampling high-quality optimized queries and their corresponding search trajectories is challenging, as relying solely on unguided high-temperature rollouts is both inefficient and constrained by the model's initial capabilities. We therefore heuristically optimize queries as seeds, improving the efficiency of trajectory generation. Furthermore, we summarize rollout experience into rubrics and use them to guide multi-round iterative self-evolution. Iteratively performing rubric optimization and rubric-guided RL enables the model to surpass its initial performance ceiling. End-to-end performance on extensive benchmarks demonstrates the effectiveness of query optimization on LJP. Comparisons with direct SFT followed by RL demonstrate the effectiveness of rubric guidance. Evolving rubrics further outperform fixed rubrics, confirming the benefits of self-evolution.

---


### 124. [GIST: Gibbs-Targeted Hierarchical Data Selection for Offline RLVR](https://arxiv.org/abs/2611.06395)

**<font color=#1a73e8>作者：</font>** Xuliang Huang, Tianxiang Zhao, Chengwei Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning with verifiable rewards (RLVR) trains on a fixed pool of sampled responses and typically supervises every token of every response, although responses and tokens are not equally informative. We study which ones to supervise through the Gibbs-optimal policy of KL-regularized RLVR, which offline training targets, and measure the mismatch between a policy and this target with a bidirectional KL divergence. At the reference policy, this mismatch factorizes exactly and separates the two outcomes: correct responses contribute mainly through the forward term, concentrated on their low-probability tokens, and incorrect responses through the reverse term, concentrated on the responses the policy generates often and on their high-probability tokens. Based on this analysis, we propose GIST (Gibbs-Targeted Hierarchical Data Selection), a two-level selection method that approximates these principles with signals available before training. GIST uses the sampling temperature to select correct responses on-policy and incorrect responses near the policy's mode, and it uses the initial policy's token probabilities to supervise only the tokens where the mismatch lies. Applied to two offline training objectives, GIST raises the average accuracy over GSM8K, MATH-500, and MBPP for all three models under both objectives. In a controlled comparison on Qwen3-0.6B/GSM8K, it outperforms seven selection baselines that choose from the same candidates while supervising 66.6% fewer tokens than training on all candidates of the same prompts.

---


### 125. [Where Should a KV-Cache Repair Budget Go? Distractor Structure and Contextual Compatibility in Non-Prefix Reuse](https://arxiv.org/abs/2611.06397)

**<font color=#1a73e8>作者：</font>** Yuxing Peng, Zhiqing Tang, Weijia Jia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Non-prefix KV-cache reuse encodes retrieved chunks independently and concatenates their caches. To find where a small repair budget should be spent, we vary the chunks around the answer-bearing one (the target) across three 7B-8B models and four datasets of dialogue memory, open-domain QA and API documentation. Reuse loses 19-100% of the context-dependent questions that full prefill answers, and it loses more when the other chunks are of the same kind as the target. Because the recoverable damage is spread over these other chunks, restoring a few of them recovers little, and the budget is better spent on the target. This works through contextual compatibility: recomputing the target against the reused cache beats inserting its full-prefill KV in all seven settings tested, although the recomputed KV stays far from the full-prefill KV. Question attention over reused caches, however, selects the target in at most 18.8% of development questions. A retriever finds it more often, and recomputing its top chunk after moving it next to the question significantly beats InfoFlow-style reordering at the same 5% budget in six of nine open-domain QA and API-documentation settings. On dialogue memory, though, recomputing chunks never significantly beats the token-level selector chosen for each setting.

---


### 126. [Ruby-OPD: Enhancing Pronunciation Controllability and Accuracy for Flow-Matching Text-to-Speech via On-Policy Distillation](https://arxiv.org/abs/2611.06403)

**<font color=#1a73e8>作者：</font>** Rui Hu, Xiaolong Lin, Zhenpeng Zhan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Achieving both high pronunciation accuracy and fine-grained controllability remains a central challenge in Japanese text-to-speech (TTS), as Japanese is an unsegmented language mixing logographic Kanji and phonographic Kana with extensive polyphony. Traditional cascaded systems convert text into phoneme sequences via a front-end, ensuring pronunciation control but discarding lexical semantics and prosodic cues in surface orthography. Conversely, recent zero-shot TTS models directly consume raw orthographic text to improve naturalness, yet suffer from polyphone errors and lack explicit pronunciation control. To bridge this gap, we propose a two-stage framework for flow-matching TTS. First, we investigate Ruby text representations with orthography perturbation to jointly preserve surface forms and target pronunciations for reliable control. Second, we introduce On-Policy Distillation (OPD) on large-scale text-only corpora to enhance pronunciation accuracy on raw orthographic text without paired speech. On the Joyo-Kanji-Yomi benchmark, our model achieves 97.13% Accuracy, 2.02% Target PER, 0.70% Sentence PER, and 4.21% Sentence CER under raw text while retaining strong controllability.

---


### 127. [Zero-Shot Coordination among LLM Agents](https://arxiv.org/abs/2611.06409)

**<font color=#1a73e8>作者：</font>** Adrian Hayler, Shashank Reddy Chirra, Andrei Lupu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study zero-shot coordination (ZSC), where independently developed agents must coordinate at test time. While ZSC has been well studied in the RL literature, far less is known about the performance of LLM agents despite their increasing deployment in such settings. Existing work on LLM coordination often relies on specialised scaffolding that independently developed agents are unlikely to share in practice. Moreover, evaluations on complex environments (e.g., Hanabi) make it difficult to pinpoint the sources of coordination failure. In contrast, we focus on simple, general-purpose scaffolds in minimal environments designed to isolate specific coordination challenges. Our results show that even in these controlled settings, frontier LLM agents struggle to coordinate, largely due to limited understanding of the coordination problem and weak reasoning about their partner's beliefs. While LLMs introduce semantic information as an additional axis for coordination, they nonetheless fail to exploit this structure effectively. Towards this, we propose Coordination-friendly definitions (CFDs) as a principled approach for enabling robust coordination among LLM agents. Finally, we show that CFDs can be discovered automatically, removing the need for manual engineering. Code is available at this https URL.

---


### 128. [Entropogram-guided Visual Realignment Decoding: Capturing the Rhythm of Multimodal Reasoning](https://arxiv.org/abs/2611.06415)

**<font color=#1a73e8>作者：</font>** Jiaqi Deng, Zhe Fu, Yakun Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have demonstrated remarkable progress on cross-modal reasoning tasks, yet they continue to suffer from hallucinations in long-chain reasoning processes. In this work, we revisit hallucination in MLLMs from the perspective of reasoning generation dynamics. We argue that entropy is not merely a static measure of uncertainty but a structured signal that reflects how modality information is integrated throughout decoding. Through systematic analysis, we identify two characteristic entropy patterns associated with hallucination behaviors: (1) a generally high-confidence regime corresponds to premature convergence to inappropriate multimodal interactions; and (2) local abrupt entropy transitions are associated with reasoning instability and hallucination onset. Building on these observations, we propose an entropy-aware self-introspective framework for MLLM reasoning. Our method continuously tracks entropy dynamics during decoding and performs targeted visual re-alignment when suspicious hallucination states are detected, encouraging the model to re-examine salient visual evidence at critical reasoning stages. Extensive experiments across six multimodal reasoning benchmarks spanning nine distinct evaluation settings demonstrate that our approach delivers robust improvements in reasoning accuracy and hallucination robustness, while providing new insights into the generation dynamics underlying MLLM failures. The code is available at: this https URL.

---


### 129. [D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding](https://arxiv.org/abs/2611.06425)

**<font color=#1a73e8>作者：</font>** Baoyou Chen, Ruiqiao Mei, Guancong Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Target-conditioned diffusion drafters predict candidate tokens in parallel, yet each new block must wait for updated target-model hidden states. This forces drafting and verification to run sequentially, limiting speedup even though each block is generated in one pass. We introduce D3D, a standalone diffusion drafter that removes this inter-round dependency. D3D combines blockwise denoising with auxiliary autoregressive supervision to achieve long accepted prefixes without target hidden states. This independence lets D3D draft successor blocks during verification in one packed pass, enabling asynchronous speculative decoding. We progressively prune layers according to their effect on acceptance length to reduce the cost of packed drafting. Removing five of 36 layers retains over 99\% of mean acceptance length across three benchmarks with Qwen3-8B as the target. Across seven benchmarks, D3D averages 5.00$\times$ and 5.71$\times$ decoding speedup with Qwen3-8B and Qwen3-32B targets, compared with 4.03$\times$ and 3.67$\times$ for DFlash. On GSM8K with Qwen3-32B, speedup reaches 7.48$\times$. Code is publicly available at this https URL.

---


### 130. [DreamRealm: Exploring and Materializing Hallucination Worlds for Trustworthy Vision-Language Models](https://arxiv.org/abs/2611.06433)

**<font color=#1a73e8>作者：</font>** Benlei Cui, Chunyang Chai, Yiliang Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) remain prone to visual hallucinations when correct responses depend on subtle visual details. One line of post-training methods constructs visual contrasts through image retrieval, generation, or editing to improve fine-grained perception. However, these contrasts are not built around the model's own hallucinations, making it difficult to ensure that supervision targets its actual perceptual confusions. Another line suppresses hallucinated outputs through response correction or preference learning under fixed image conditions, but leaves the design of supervision signals on the image-input side underexplored. Inspired by how humans correct misconceptions, we introduce DreamRealm, a post-training framework that explores diverse latent hallucinated responses, minimally edits original images to make them valid, and trains the model to assign each response to its supporting image. Our data construction pipeline, RealmForgePipe, mines observed and latent hallucinations from a target model and materializes them through image editing. Using hallucinations mined from Qwen3.5-9B, we construct the Realized Hallucination Dataset (RealmSet). Our training objective, RealmMatch, constructs a likelihood score matrix across image--response combinations and combines supervised learning with bidirectional contrastive losses to reinforce correct matches and suppress mismatches. Compared with the original Qwen3.5-9B model, DreamRealm improves performance across six visual perception and hallucination benchmarks, including gains of 7.26 percentage points in HallusionBench accuracy and 11.34 percentage points in MMVP pair accuracy. Together with ablation studies on data construction and training methods, these results demonstrate that hallucination assignment is a promising paradigm for improving visual perception and mitigating hallucinations.

---


### 131. [EviSeek: An Evidence-Centric Agentic Framework for Embodied Active Information Seeking](https://arxiv.org/abs/2611.06434)

**<font color=#1a73e8>作者：</font>** Jintao Li, Zhiyong Cao, Baihua Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Active embodied question answering requires agents to acquire evidence through viewpoint changes and physical interaction. The central challenge is to avoid undirected interaction: taking plausible actions without specifying what evidence they should reveal for answering the question. Action plans and accumulated histories alone can leave the informational purpose of an interaction implicit. We introduce EviSeek, a training-free framework that makes question-derived evidence demands explicit acquisition objectives, linking observation-conditioned actions and selectively retained evidence to the information the agent seeks. On 3,436 ESI-Bench questions, EviSeek improves accuracy over the Single-model agent by 7.1 percentage points with Qwen3-VL-32B and 3.7 points with Gemini 3.1 Pro, while improving visual-support-weighted accuracy and reducing mean token usage. These findings support making the informational purpose of interaction explicit, with action selection and evidence retention organized around what the agent needs to learn to answer the question.

---


### 132. [Understanding the Out-of-Distribution Generalization of Chain-of-Thought Reasoning in LLMs](https://arxiv.org/abs/2611.06438)

**<font color=#1a73e8>作者：</font>** Nuo-Jing Liang, Xiao-Tong Yuan, Pan Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) reasoning substantially improves Large Language Models (LLMs), yet its out-of-distribution (OOD) generalization mechanism remains theoretically underexplored. We study CoT as compositional OOD generalization: the target task lacks complete reasoning trajectories or direct input-output pairs, while training provides only in-distribution (ID) atomic step data. We show that CoT generalizes by repeatedly applying a shared single-step predictor to compose reusable ID transitions. Theoretically, let $T$ denote the number of reasoning steps in the target task, $n$ the number of training samples per sub-task, and $k$ the number of output tokens per step; then the OOD task risk is controlled by the sum of the ID sub-task risks, scaled by a coefficient of order $\mathcal{O}(k)$ that is independent of $T$, although the summed risk itself may still grow with $T$. A Rademacher-complexity analysis further shows that the estimation term is of order $\mathcal{O}(\sqrt{T/n})$, rather than linear in $T$, due to predictor sharing under a uniform capacity control on the shared class. For autoregressive Next-Token Prediction, the final-task risk is bounded by the best-in-class step-level risk scaled by the same coefficient of order $\mathcal{O}(k)$, plus an estimation term of order $\widetilde{\mathcal{O}}\big(k\sqrt{T/n}\big)$. A parity-coupled construction further shows that, for the sub-task empirical risk minimizer, the expected final-task risk is at least the best in-class risk plus $\Omega(\sqrt{T/n})$ when $T\le n$. Experiments on Atom-Task and GSM8K support the theory: CoT enables short-to-long and compositional generalization, while explicit state tracking is crucial.
Our code is available at this https URL.

---


### 133. [EvoGuard: Mitigating Degradation in Online Skill Evolution](https://arxiv.org/abs/2611.06444)

**<font color=#1a73e8>作者：</font>** Yanli Wang, Zichen Bai, Tianyue Jiang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Skills let language agents reuse experience across tasks as natural-language documents. Recent work evolves skills from interaction, but existing methods have limitations when skills evolve online. Prior methods update a skill offline from a batch of trajectories collected over many tasks. Some then adopt the new skill without any check, which can degrade the skill over time. Others keep it only if it improves performance on a held-out validation set, which is too slow and costly to run after every update. We introduce EvoGuard, a pairwise skill selector that mitigates skill degradation at low latency and cost. We first run the agent iteratively to build pools of skills and score each skill on a private test set to obtain utility labels. We pair the skills and use rejection sampling to keep only pairs with a clear utility gap. The selector is trained on the logits of two label tokens to pick the better skill. At deployment it decides in a single forward pass, which is significantly faster than evaluation on the private test set. Compared with adopting every new skill, EvoGuard improves success by 11.0% on ALFWorld, 5.9% on ScienceWorld, and 2.7% on LiveCodeBench.

---


### 134. [SUMONE: A Simple and Efficient Summarizer for Plug-and-Play Agent Memory](https://arxiv.org/abs/2611.06445)

**<font color=#1a73e8>作者：</font>** Jizhe Zhang, Ang Li, Chenheng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon language-model agents accumulate increasingly large interaction histories, making context compaction essential for efficient execution. Existing learned compaction methods often rely on downstream task outcomes or solver behavior, coupling training to specific tasks or agents. We introduce SumOne, a standalone summarizer trained to preserve information in agent histories through masked reconstruction. Given a summary of the expired history, a frozen reconstructor recovers randomly masked portions of the original trajectory; reconstruction quality, combined with a length penalty, provides a task-agnostic reward for optimizing the summarizer with GRPO. This yields self-supervision directly from raw trajectories, without reference summaries or downstream task execution. At inference time, only the lightweight summarizer is retained, enabling plug-and-play context compression for otherwise unchanged agents. We conduct a systematic evaluation of SumOne in long-horizon search and software-engineering tasks. SumOne reduces estimated inference cost by approximately 78\% on DeepSearchQA and 75\% on SWE-bench Verified relative to operating with full context, with absolute decreases of 0.04. The same checkpoint also transfers across downstream models and agent harnesses without additional fine-tuning.

---


### 135. [AmbiHTMLBench: A Benchmark for HTML-based Visually Rich Document parsing](https://arxiv.org/abs/2611.06449)

**<font color=#1a73e8>作者：</font>** Boyu Niu, Yingjie Xiong, Shurui Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional document parsing systems use Markdown as their output representation, which is effective for linear text but does not fully preserve fine-grained spatial structure, table geometry, visual hierarchy, or rendering semantics. We show that HTML is advantageous for heterogeneous and layout-sensitive documents whose representations must remain editable, inspectable, and reusable, and introduce AmbiHTMLBench to systematically study this setting. In this benchmark, given a real-world document, a model must recover executable HTML that preserves its content, organization, and visual appearance. The benchmark contains 1,115 diverse pages with structured annotations and evaluates predictions in two different ways: The objective protocol aligns ground-truth and predicted rendered blocks and measures table fidelity, page-level text error, and a two-dimensional layout consistency; a complementary reference-anchored protocol measures perceived fidelity by aligning LLM judges with human preferences. Across ten primary multimodal systems, the best objective score is 0.8092, while the subjective winner is different, demonstrating that automatic decomposition and human-perceived fidelity capture complementary properties. We further fine-tune a small-parameter expert model and find that task-specific adaptation yields good performance on document-to-HTML reconstruction task. These results position AmbiHTMLBench as a diagnostic testbed for building smarter and more logical document parsing systems.

---


### 136. [The Alignment Tax Is Graded: Task-Selective Capability Loss Under Length-Normalized DPO with SFT Retention](https://arxiv.org/abs/2611.06476)

**<font color=#1a73e8>作者：</font>** Ye Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Setting. This is an empirical characterization study; we propose no new method and run no comparisons against alternative objectives. We fine-tune Qwen3.5-4B with sparse LoRA and length-normalized DPO plus an SFT retention term (the RPO objective) on structured financial-filing tasks, and track downstream capability as the implicit reward margin grows to $\sim 7$ $\beta$-scaled units (nf4 training; $\sim 3$ under fp16 measurement on the unquantized base). Question. Does margin growth degrade capability uniformly across tasks, or selectively? Findings. In a pre-registered study (8 seeds, 6 unseen at freeze) with artifact-aware scoring and TOST equivalence testing, the alignment tax is graded and task-selective: extraction is preserved ($\Delta = -0.55$ pts, equivalent at $\pm5$ pts), json loses little ($\Delta = -3.52$ pts, equivalence fails on a clustered item-level interval), and router degrades severely ($\Delta = -30$ pts). Router's loss concentrates in a margin 1-3 damage window containing a transient format-break spike. The margin is accounted for almost entirely ($\geq 96\%$) by suppression of rejected completions, with chosen reward approximately flat, consistent with the retention term anchoring it; we do not attribute the behavioral damage to any single gradient channel. Gold-logp deflation is task-selective (extraction $-0.15$, json $-1.04$, router $-1.47$ nats/token under fp16), with gold selectively protected relative to incorrect controls on extraction (8/8 seeds). QLoRA reward margins differ up to $3.4\times$ between nf4 training and unquantized fp16 measurement, with an axis-dependent gap. Scope. Length-normalized rewards with SFT retention, sparse LoRA on 8/32 layers, one 4B model, easily-separable synthetic preferences, three structured tasks. A no-retention control and a measured format-alignment metric are left to future work.

---


### 137. [Towards Early Warning of Real-World Vulnerabilities: An Evidence-Aware Decoupled Method for CVSS Vector Prediction Based on Unstructured Disclosures](https://arxiv.org/abs/2611.06477)

**<font color=#1a73e8>作者：</font>** Jianhong Ma, Wenhao Li, Xixing Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Early assessment of Common Vulnerability Scoring System (CVSS) vectors from Open Source Intelligence (OSINT) can reduce the delay between initial public disclosure and official National Vulnerability Database (NVD) scoring. Existing predictors, trained mainly on standardized late-stage descriptions, degrade on noisy and incomplete pre-NVD reports. We introduce PARSE, a vulnerability-disclosure lifecycle model, and VPre, an early assessment framework built on two-level Evidence-Aware Decoupling. Decoupling Level I, Security-Evidence Screening, separates security-relevant evidence from noisy early reports at the report and sentence levels. Decoupling Level II, Evidence-Matched Routing, decouples the prediction task of the eight CVSS metrics into a scattered-evidence class and an explicit-evidence class based on validation-set measurements, matching each with a targeted predictor: large-language-model reasoning for the former, lightweight supervised classification for the latter. On the 851-report held-out test split of the 5,581-report VPre-Bench, VPre achieves a mean absolute error of 0.7239 -- 44.7% below the reproduced BERT-Small-NVD early-transfer baseline; paired timestamps across the full benchmark show an average 38-day lead before official scoring (observed range 21-60 days). Under the 38:1 PARSE-Triage noise setting, STDU's report-level screening reaches 0.98 precision, 1.00 recall, and 0.99 F1. Controlled ablations support the contributions of both decoupling levels.

---


### 138. [ArcRAG: Agentic Compositional Retrieval over Knowledge Graphs](https://arxiv.org/abs/2611.06481)

**<font color=#1a73e8>作者：</font>** Jyotin Goel, Abhinav Arun, Tejas Prakash Agarwal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Graph-based retrieval-augmented generation (GraphRAG) answers questions by retrieving over a knowledge graph built from a corpus. Yet retrieval strategies are designed around the structure their own construction pipeline produces, and whether they survive a change of construction is rarely tested. We study this cross-construction portability: whether one retrieval procedure, with no construction-specific schema, relation names, or retuning, stays effective when the graph is built differently. We introduce ArcRAG, which induces a query-local graph interface at inference time (the node labels, relation descriptors, and property keys reachable from the entities a question names), plans multi-hop traversals against it, and executes and repairs them as Cypher. We build each of the MuSiQue, HotpotQA, and TriviaQA corpora as a schema-guided graph (typed nodes, a closed relation set, source provenance) and as an open-information-extraction graph (untyped nodes, free-text relations), with the retriever's configuration fixed across them. We compare against a construction-agnostic Direct-Cypher agent, ablate each stage across retry and pass budgets on both graph families, and compare with results reported for prior GraphRAG systems, most of which design retrieval together with their own graph construction. Across the two constructions, we find that retrieval need not be co-designed with the graph: query-time interface induction keeps a construction-agnostic retriever effective when the construction changes, although construction still shapes absolute accuracy.

---


### 139. [What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?](https://arxiv.org/abs/2611.06483)

**<font color=#1a73e8>作者：</font>** Kejian Zhu, Zhuoran Jin, Shangqing Tu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While multi-turn agentic reinforcement learning (RL) excels on long-horizon tasks, its performance gains remain highly sensitive to interaction constraints. Evaluating across sampling breadth $K$ and interaction depth $T$ via $Pass@(K,T)$, we show that trajectory-level RL advantages depend on sufficient turn budgets, diminishing significantly when budgets tighten. Besides, agentic RL does not uniformly elevate single-step decision quality; rather, its strength concentrates in error recovery and long-horizon resilience. To mitigate the deployment risks caused by this budget dependence, we provide a preliminary discussion on the benefits and limitations of process supervision signals and introduce BudgetMix RL as an alternative that varies interaction budgets during training. Experiments demonstrate that BudgetMix RL achieves robust performance across diverse execution settings. Project Page: this https URL

---


### 140. [LibriSpeech-Real-QA: A Benchmark for Streaming Question Answering](https://arxiv.org/abs/2611.06496)

**<font color=#1a73e8>作者：</font>** Zewen Zhan, Hui Lu, Xueyuan Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most speech large language models (SLMs) still process speech in an offline manner. They only start responding after they receive the complete speech segment. However, many real-world applications require streaming speech interaction, for which the audio continuously flows in and the machine is required to answer questions based on the so far received audio chunks. For example, a user may ask the system to continuously count how many times a person's name has been mentioned while they are speaking. We observe a lack of benchmarks and evaluation protocols for real-time speech interaction. Motivated by this, we propose LibriSpeech-Real-QA, a dataset and a benchmark for real-time speech interaction. We construct different types of real-time question-answer pairs from LibriSpeech to evaluate whether speech LLMs can identify target words in streaming audio. We evaluate several popular real-time commercial models and find that they still tend to respond only after the speech turn has finished. We demonstrate that we can enable a pretrained SLM to perform this task, where we explore several modeling designs and establish a solid baseline for future research.

---


### 141. [Signed but Steerable: Measuring and Closing the Text-Vector Integrity Gap in Offline Retrieval-Augmented Generation](https://arxiv.org/abs/2611.06498)

**<font color=#1a73e8>作者：</font>** Georgios Feretzakis, Alexandros Papaspyridis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Offline retrieval-augmented generation (RAG) on edge devices is updated through signed knowledge packs that carry text and precomputed embedding vectors. A signature proves who published a pack, not that its vectors encode its text. We study this text-vector integrity gap. A verifier that recomputes vectors and accepts them within a cosine tolerance concedes a predictable share of queries to an attacker who controls the vectors: the hijack rate equals the distribution of angular retrieval margins at the tolerance (the margin law). Margins are small in five corpora and two embedding models, so an idealised tolerance at the level of floating-point noise leaves up to 5.5% of queries exposed (at most 1.2% in any corpus once exact duplicate documents are excluded), and a threshold calibrated from our CPU INT8-FP32 comparison of a small embedding model (at the empirical 0.1% quantile of honest cosines) leaves 98-100% exposed; on a Raspberry Pi 5 running a local language model, such an attack lowers correct answers from 0.75 to 0.39. Integrity audits of compressed vector stores fare no better: on a FAISS product-quantisation index over 57,638 documents, tampered vectors that all pass the audit put the attacker's document first for 25% of targets. Verifying quantisation codes instead, with ambiguity decided by the verifier, a calibrated guard band and canonicalisation, accepted every honest vector in our samples on three platforms and left the publisher no choice. We also show that common floating-point and dynamic-INT8 inference pipelines are not bit-reproducible across batch sizes or architectures, and report pre-registered negative results on abstention, context pruning and semantic screening. We release code and data.

---


### 142. [Tools Need Not Speak in Text: Latent Context Compression for Agents](https://arxiv.org/abs/2611.06500)

**<font color=#1a73e8>作者：</font>** Yuetong Liu, Zhehao Zhou, Yitong Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents typically append raw tool outputs to their context. Over multi-step interactions, long and noisy observations incur substantial context overhead and dilute the agent's attention to task-relevant information. Existing token pruning and summarization methods remain constrained by discrete text representations, limiting the achievable compression ratios.
In this work, we challenge the prevailing assumption that agents must consume tool observations as explicit text tokens. To this end, we propose Coca-Cola, a continuous latent context compression model for LLM agents. Coca-Cola compresses tool observations into latent tokens and embeds them into the input embedding space of the agent. We further introduce Action-Preserving Training, which aligns the agent's next-action distributions under full and compressed observations. This trains the compression model to learn action-sufficient latent tokens that retain decision-critical information. Experiments with web-search agents on four QA benchmarks and two model families show that Coca-Cola reduces the agent's token consumption by 70.01%-89.24% and end-to-end runtime by 24.45%-55.97%, while consistently improving task performance. These results suggest that Coca-Cola offers a promising approach for context compression in agents. Our code is available at this https URL.

---


### 143. [CRESiST: Self-Enhancing Explorative Policy Learning for Simultaneous Speech Translation](https://arxiv.org/abs/2611.06501)

**<font color=#1a73e8>作者：</font>** Chenyang Le, Pei Zhang, Yuxiang Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Simultaneous Speech Translation (SimulST) requires balancing translation quality and latency. While Large Language Models (LLMs) excel in offline translation, current LLM-based SimulST systems predominantly rely on prefix-incremental generation. This paradigm suffers from redundant Key-Value cache recomputation and necessitates external Voice Activity Detection to process unbounded streams. To overcome these bottlenecks, we propose an end-to-end interleaved read-write framework built upon an omni-modal LLM. By interleaving speech chunks and text tokens, our architecture achieves full KV cache reuse, natively supporting segmentation-free, infinite-length inference. Furthermore, to learn optimal streaming policies without rigid offline alignments, we introduce a novel Actor-Critic self-enhancement pipeline. An RNN-T Actor dynamically samples read-write trajectories, while an LLM-based Critic evaluates these paths via intrinsic semantic and latency rewards, distilling the optimal policy back to the Actor. Extensive experiments on sentence-level (FLEURS, CoVoST2) and document-level (MuST-C, ACL 60/60) benchmarks demonstrate that our model establishes new state-of-the-art quality-latency Pareto frontiers, substantially outperforming existing cascaded and static-alignment baselines.

---


### 144. [EvoOPD: Evolving Privileged Information Strategies for Black-Box On-Policy Distillation](https://arxiv.org/abs/2611.06542)

**<font color=#1a73e8>作者：</font>** Ximo Zhu, Ruiqi Liu, Yi Han 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Proprietary language models exhibit strong reasoning and coding capabilities, but their output distributions are inaccessible, making fine-grained distillation methods that rely on teacher logits difficult to apply directly to black-box models. We observe that rich textual feedback from a black-box teacher can be treated as privileged information (PI) and converted, through a PI-conditioned privileged teacher, into dense supervision signals on the student's own trajectories. However, what PI should be acquired from the teacher to most effectively support student learning remains unclear. PI strategies that differ in where they focus, what information they request, and how much detail they provide can have substantially different effects on the current student, and their relative effectiveness can further change as training progresses. Based on this observation, we propose Evolving Privileged Information Strategies for Black-Box On-Policy Distillation (EvoOPD), which treats PI acquisition itself as an optimization problem and maintains a PI Strategy Bank that evolves with the student state. EvoOPD uses the measured repair utility of PI on the current student to adapt the focus, information type, and granularity of teacher feedback, allowing the acquired information to continually match the student's learning needs. We systematically evaluate EvoOPD on mathematical reasoning and code generation with Qwen3-1.7B, 4B, and 8B students. EvoOPD achieves the best overall performance in all six model-task settings, improving over the strongest baseline in each setting by an average of 2.14 percentage points in mathematics and 1.30 points in code. Further analysis shows that the relative effectiveness of PI acquisition strategies changes with student state, making a fixed strategy difficult to sustain as the best choice throughout distillation.

---


### 145. [Using Experience Twice: Dynamic Process Rubrics for Privileged Token-Level Credit Assignment](https://arxiv.org/abs/2611.06543)

**<font color=#1a73e8>作者：</font>** Shumao Wu, Kongcheng Zhang, Jianqiang Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent trajectories often contain both successful decisions and failed attempts, yet optimization with sparse trajectory-level rewards struggles to identify which critical decisions should be reinforced or suppressed. We observe that meaningful distinctions among on-policy trajectories can be distilled into natural-language process rubrics and used as process supervision signals. Based on this insight, we propose Online Rubric Self-Distillation (ORSD), which leverages self-derived process rubrics for dense token-level supervision, thereby augmenting outcome-centric reinforcement learning. Specifically, the current policy independently generates multiple rubric bundles at each step according to the same group of trajectories, extracting candidate process rubrics from cross-trajectory behavioral differences. A frozen verifier then evaluates all rubric items against each trajectory in the group, and selects one candidate bundle based on bundle-level alignment between rubric satisfaction and task success. ORSD treats the selected rubric bundle as privileged information during training, then compares the log-likelihoods of the original tokens with and without the rubric. The resulting likelihood gap provides token-specific process credit, which is added to the original trajectory-level GRPO advantage through additive advantage shaping. ORSD thus bridges trajectory-level outcome supervision and fine-grained process supervision, enabling token-level credit assignment using process signals. Extensive experiments on ALFWorld and WebShop show that ORSD accelerates policy improvement and boosts final task performance for both Qwen3-1.7B and Qwen3-4B under the same environment-interaction budget. Our code is available at this https URL.

---


### 146. [MKD2World: A Typed Spatial MarkDown World Model For Web Agents](https://arxiv.org/abs/2611.06544)

**<font color=#1a73e8>作者：</font>** Zhihao Nan, Sifan Zhou, Yiming Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graphical user interface (GUI) agents can improve decision-making with world-model foresight, provided that predicted states accurately reflect post-action interfaces. Existing state representations fail to jointly capture interface layout, UI semantics, and explicit locations. We introduce Typed Spatial Markdown (TSM), a Markdown-style textual state representation for desktop web interfaces. TSM serializes block-level and atomic-level UI elements according to their spatial relationships, jointly encoding their types, visual semantics, explicit locations, optional control states, and hierarchical membership. To train a screenshot-to-TSM renderer, we construct AtomBlock-WebUI, a dataset with precise annotations at both granularities. By injecting element-type labels into HTML and directly extracting bounding boxes after rendering, we avoid annotation errors caused by post-hoc inference from webpage structures. Building on TSM, we propose MKD2World, a desktop web world model trained in two stages for current-state description and action-conditioned next-state prediction. During inference, the web agent queries MKD2World as needed and performs a ``digest'' step, in which it interprets each predicted state and extracts task-relevant evidence for selecting the best action. Experiments show that MKD2World-9B achieves an EleF1 score of 26.50 on the out-of-domain test set, outperforming GPT-5.6-Sol(14.98) by 11.52 points. Across Online-Mind2Web tasks, MKD2World-9B improves the success rate of the Qwen3.5-35B web agent from 22.94% to 37.61%, achieving competitive performance among leading open-source GUI world models. Code is available at this https URL.

---


### 147. [When Do Summaries Become Instructions? Unsupported Policy in LLM Agents' Self-Written Handoff Summaries](https://arxiv.org/abs/2611.06545)

**<font color=#1a73e8>作者：</font>** Wenhui Chu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-running LLM agents compact their context, replacing most history with a summary. We ask whether handoff summaries state permissions or requirements the record does not support, whether such sentences change what the next instance (the successor) does, and where they come from. Synthetic tool-use tasks carry a ground-truth permission ledger; same-snapshot replay reruns the successor with those whole sentences replaced by neutral filler. Two AI readers, reading only rule-flagged held-out summaries, confirmed unsupported restrictions in 1.2% and 2.4% of all readable summaries from two open-weight models, and unsupported authorizations in 0.1% and 1.3%. For restrictions, a pre-specified replay test was not significant (p = 0.58); a follow-up, planned after it, found a fragile effect (p = 0.027). Neutralizing false approvals cut unauthorized actions from 24 to 7 of 120 held-out runs (post hoc; later set: 17 to 11 of 48). Most development restrictions followed the agent's earlier reasoning that an action needs approval (post hoc). In pre-specified tests, replacing the system prompt's "Some actions need approval." with one saying where requirements come from cut unsupported restrictions from 5.0% to 1.8% of development summaries and, on held-out templates, from 1.8% to 0.3% (both p < 10^-9), while requests for approvals the ledger requires barely changed. Code and data: this https URL

---


### 148. [RAGAM-AI: A Hybrid Reinforcement Learning based Agentic approach powered by Generative AI for Edge Resource Management](https://arxiv.org/abs/2611.06554)

**<font color=#1a73e8>作者：</font>** Shreya K. Chari, John S. Vardakas, Kostas Ramantas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Resource management for distributed edge networks hosting different services has been handled efficiently using Reinforcement learning (RL). Reward generalization in complex workflows is still an open issue within the RL realm. Therefore, this work proposes RAGAM-AI, a hybrid framework that combines the capabilities of RL algorithms and Generative-AI (Gen-AI) for powering an Agentic AI workflow that optimizes resource allocation at the Multi-access Edge Computing (MEC) units. This framework further resolves the reward generalization issue by utilizing Large Language Model (LLM) for feedback. A Multi- Agent Soft-Actor Critic (MASAC) using Math{\Sigma}tral as a reward oracle is implemented for managing resource allocations at the MEC. RAGAM-AI interprets system state information and evaluates multi-objective trade-offs guiding the resource orchestration loop over distributed edge server agents. The complexity of the framework is further brought down by incorporating surrogate reward model. The overall performance is evaluated against the single agent SAC, REINFORCE and random policies for benchmarking. On using RAGAM-AI, lower allocation deviations for CPU, memory and bandwidth resources are reported while minimizing the latency and data rate costs. A scalable AI as a feedback (AIAF) solution optimizing network resources with significant performance improvement is thus presented.

---


### 149. [One Scale, Four Texts: Gaps, Overlaps and Silent Repairs in Published Grading Schemes](https://arxiv.org/abs/2611.06569)

**<font color=#1a73e8>作者：</font>** Elisa Rovai, Fabio Rovai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Category systems often reach their users as text, and readers apply them with tacit repairs. We ask what such a text determines once the repairs are removed, using diabetic retinopathy grading, where one international scale circulates in several documents. We transcribe four texts (the English screening definitions of 2025, the international scale as tabulated in 2017 and as published in 2003, and an Italian guideline of 2015) into one rule language over 24 finding variables, and make every point a text leaves open a named precisification. Exhaustive enumeration of 1,425,807,360 finding profiles, re-derived by an SMT solver and spot-checked by an OWL reasoner, shows that every text that assigns actions leaves some eyes without a category under every reading; that the 2017 tabulation has a proliferative class that is empty when read literally and a macular gap that the 2003 text lacks, so that no function maps the 2003 grades onto the 2017 grades; and that on image findings alone the English and Italian texts order some pairs of eyes in opposite ways. On 927 annotated photographs from three public datasets, with retinal thickening assumed absent, the English text and the 2017 tabulation disagree on referral for 26.8% of the eyes of one dataset (DDR) on which both decide, and in a pre-registered experiment classifiers trained on each text's labels side with their own text. Thickening cannot be seen on a colour photograph; left free, every disagreement involving England becomes undecidable, so it rests on what the camera cannot show. In a second pre-registered study, language models that answered without deliberating repaired most gap and overlap items even when told to read literally, while Claude Sonnet 5.5 and Claude Opus 5.5 reported the defects far more often; within two models, deliberation reduced silent repair without removing it.

---


### 150. [The Behavioral Rate of Fine-Tuning: Compression as a Measure of Useful Information](https://arxiv.org/abs/2611.06598)

**<font color=#1a73e8>作者：</font>** Joey David, Paul Caillon, Alexandre Allauzen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) adapts a frozen language model through a compact learned update, making it a natural setting for asking how much information fine-tuning needs to write. Yet adapter rank, parameter count, or numerical reconstruction error do not directly tell us how many bits are required to preserve the acquired behavior. We therefore define an operational behavioral rate $R^\star$ as the smallest serialized size of a compressed adapter that, once reloaded into the frozen base model, retains a fixed fraction of its held-out fine-tuning gain. Across LoRA fine-tuning experiments, this rate increases with distinct training content at fixed optimization budgets, but is not determined by intuitive metrics like source description length, fine-tuning gain, or weight-space reconstruction error. Most importantly, the same datasets exhibit substantially different, and even reordered, rates across frozen base models, showing that fine-tuning compressibility is a property of the dataset--receiver pair rather than of the dataset alone. However, we show that correction spectra measured on the data are able to rank these rates within a receiver. Finally, we study a striking noise-reducing effect of compression: adapters trained on deliberately corrupted datasets fall far below the frozen model, yet after compression score above it (23.7% to 82.9% on GSM8K, against 77.6% for frozen Qwen2.5-7B), consistently across tested families and sizes. The damage is unevenly concentrated in the adapter's leading singular directions, which compression appears to filter. Away from its training task, the compressed corrupted adapter also generalizes better than a clean fine-tune: on harder math it retains 97% of base accuracy, versus 44% for the clean adapter.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-207](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
