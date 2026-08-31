# 🧠 大模型相关研究 | 2026年09月01日

> 本类共 **176** 篇论文：已确认 **168** 篇，待复核 **8** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-176](./part-04.md)

---

### 101. [TagZilla: Automated Owner and Abuse Type Tagging for Indicators of Compromise in Threat Reports](https://arxiv.org/abs/2608.28124)

**<font color=#1a73e8>作者：</font>** Gibran Gomez, Juan Caballero  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber Threat Intelligence (CTI) reports often describe Indicators of Compromise (IoCs) such as IP addresses, URLs, file hashes, and cryptocurrency wallets involved in cyberattacks. Those IoCs are typically described in the unstructured report's text, or listed at the end of the report with little context, limiting their usefulness. This paper presents TagZilla, a platform that, given a threat report, automatically analyzes its text and tags the IoCs it describes with contextual information about the threat group and malware family that the IoC belongs to and the type of abuse associated with the IoC (e.g., phishing, sextortion, command-and-control). TagZilla provides a novel LLM-based approach to assign owner tags to IoCs using an open-world classification, and assigns 29 abuse type tags to IoCs using a closed-world classification. We evaluate TagZilla on a manually generated ground truth of 100 threat reports containing 1,534 indicators, where it achieves an F1 score of 0.94 for owner tagging and 0.93 for abuse type tagging. Then, we apply TagZilla to tag 765 threat reports, identifying 15,583 IoCs belonging to 637 malware families, 113 threat groups, and 162 other entities. The results show that TagZilla can tag IoCs even in reports describing multiple actors and malware families, enabling the generation of IoC profiles for those entities.

---


### 102. [VICT: Verifier-Instrumented Credit Tracing for Long-Horizon LLM Agent Reinforcement Learning](https://arxiv.org/abs/2608.28128)

**<font color=#1a73e8>作者：</font>** Pengcheng Li, Zhengyang Zhang, Dongxu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-grained credit assignment is a central challenge in reinforcement learning for long horizon LLM agents. Standard objectives often train from programmatically verifiable terminal rewards by broadcasting each sparse outcome to every action in a trajectory. Existing methods typically seek finer credit from the rollout side, constructing auxiliary trajectory signals or additional comparisons to estimate action importance. Although useful, these approaches still treat the verifier that judged success as a scalar reward, discarding its internal task structure. Our key insight is that many verifiable tasks already encode the relevant checks inside their terminal verifier. We propose VICT (VerifierInstrumented Credit Tracing), a training-time interface that exposes executable or evidence backed atoms and traces them back to actions through dependency-valid proof edges. VICT redistributes group-relative advantage only along those edges, shifting credit assignment from rollout-side inference to verifierside tracing. It preserves the original terminal reward, abstains when evidence is incomplete or ambiguous, and changes only the training-time advantage tensor, requiring no learned critic, process labels, branch rollouts, or inference-time verifier access. On ALFWorld and WebShop, VICT improves substantially over outcome-only training and achieves strong performance alongside recent fine-grained credit methods; ablations rule out dense atom rewards, final-commit credit, temporal proximity, and sparsity as sufficient explanations.

---


### 103. [Token-Budget Distillation: Transferring Full-Token Semantics to Compressed Video Vision-Language Models](https://arxiv.org/abs/2608.28138)

**<font color=#1a73e8>作者：</font>** Xiaoyang Guo, Guoping Luo, Jusheng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting video vision-language models (VLMs) is computationally expensive because video inputs produce a large number of visual tokens, making both fine-tuning and inference costly. Although visual token compression can reduce this overhead, direct adaptation on compressed inputs often causes semantic drift and noticeable performance degradation. We present Token-Budget Distillation (TBD), a parameter-efficient fine-tuning framework for adapting video VLMs under a fixed token budget. TBD freezes the pretrained backbone, updates only LoRA adapters, and integrates FlashVID-based visual token compression into the video pathway. To preserve full-token semantics under compression, TBD employs a dual-path teacher-student design, where a full-token teacher provides stable supervision and a compressed student is optimized with task loss, answer-region KL distillation, GT-anchored margin distillation, and reliability-aware KD control. This design enables the student to recover the semantic behavior of the full-token model while remaining efficient under aggressive token reduction. We evaluate TBD on three video VLM backbones, including LLaVA-Video, LLaVA-OneVision, and Qwen3-VL-8B-Instruct, across four video understanding benchmarks. TBD consistently outperforms compression-only baselines under both moderate and aggressive compression. On LLaVA-Video at retention ratio R = 10 percent, TBD preserves 97.0 percent of the Vanilla model's average accuracy; on LLaVA-OneVision at R = 10 percent, it achieves an average score of 58.4 and matches 100.0 percent relative accuracy.

---


### 104. [The Shape of Power: A Multilingual Framework for Social Power Reasoning in Dialogues](https://arxiv.org/abs/2608.28144)

**<font color=#1a73e8>作者：</font>** Farah Atif, Sougata Saha, Monojit Choudhury  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Social power plays a fundamental role in shaping human interaction, yet computational studies of power remain limited to narrow linguistic and cultural settings. Existing datasets further lack the demographic and relational depth needed for robust cross-cultural analysis. To address this gap, we introduce a theoretically grounded framework for studying social power in naturalistic multilingual dialogue through movie screenplays. The framework integrates a schema informed by social science theory, a native speaker annotation pipeline refined through pilot studies, and a custom interface for scalable cross-lingual analysis. Using this framework, we constructed an initial corpus containing 15,836 annotated instances from 100 scenes in French and Egyptian Arabic movies. Our analysis reveals strong agreement on observable demographic and contextual attributes, while socially interpretive aspects, such as power asymmetry and intention alignment, remain more contested, highlighting the complexity of social power across cultures. We evaluated 6 Large Language Models (LLMs) and Multimodal LLMs on cross-cultural social power reasoning, finding persistent gaps between human and model agreement in relational and theory-of-mind reasoning. Our work introduces the first extensible multilingual framework for studying social power in dialogues and provides an initial evaluation setting for studying cross-cultural social reasoning.

---


### 105. [Dual-Stream Semantic Guidance with Prototype Anchor Calibration for Source-Fully-Free Adaptation of Vision-Language Models](https://arxiv.org/abs/2608.28145)

**<font color=#1a73e8>作者：</font>** Weiwei Xiang, Shun Peng, Guangyi Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Source-Fully-Free Domain Adaptation (SFF-DA) has emerged as a strategic paradigm to adapt Vision-Language Models (VLMs) without any access to source data or task-specific source models. However, we identify a critical Dual Semantic Drift that hinders this process: static drift arising from the rigidity of fixed class embeddings, and dynamic drift stemming from the divergence of generated captions, causing severe semantic misalignment that intensifies the stability-plasticity dilemma. To address this, we propose DSSG (Dual-Stream Semantic Guidance), an end-to-end framework that reconciles fine-grained plasticity with global stability. Our core contribution is the Dual Semantic Guidance (DSG) module, which integrates a caption stream for domain-specific knowledge with a class-anchor stream to anchor global categorical consistency. Furthermore, a Dynamic Cross-Modal Knowledge Distillation (CMKD) module is introduced to leverage the evolving teacher distribution for calibrating teacher-student consistency. Building upon DSSG, we further introduce Prototype Anchor Calibration (PAC), yielding DSSG-PAC, which periodically calibrates prototype anchors and caches them until the next calibration. This design reduces redundant text-side computation while preserving the adaptability of class guidance to the evolving text space. We further establish SFF-DA risk bounds that relate student risk to semantic-teacher quality and teacher--student discrepancy. Extensive experiments demonstrate that DSSG consistently outperforms current state-of-the-art methods across multiple benchmarks, while DSSG-PAC largely preserves its adaptation performance with 18.9% lower total adaptation time. The code is available at this https URL.

---


### 106. [Nested Byte-Level Vocabularies Are Cheap to Deploy and Expensive to Share: A Pre-Registered Negative Result](https://arxiv.org/abs/2608.28151)

**<font color=#1a73e8>作者：</font>** Christos Koutsiaris  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A byte-level BPE tokenizer is an ordered list of merge rules, so applying only a prefix yields a vocabulary whose token identifiers are the first rows of the full vocabulary. This prefix nesting allows one language model to operate at several vocabulary sizes, use a control token to indicate the active size, and be deployed at any trained size by slicing its embedding and output head. We pre-registered five claims, including margins, seeds, contrasts, and a stop rule, and trained 30 models with 3.1M- and 10.6M-parameter bodies on 200M tokens each. Slicing is numerically exact: across 76 checks, a sliced model reproduces the restricted full model's logits bit for bit and removes 66% of deployed weights without changing latency. However, the shared model trails a fixed-cap specialist by 3.64% bits per byte at 32k against a 1% margin, and by 2.96% at 8k against a 2% margin. A 2x2 ablation separating the control token from output restriction finds that the token changes performance by +0.07% to +0.13%, with all intervals crossing zero, while output restriction costs +0.47% to +1.19%; the factors are substitutes rather than complements. Multi-cap training nevertheless improves robustness: under typographical noise, the same checkpoint degrades 12.5--15.4 points less in its fine mode and outperforms each fixed-cap specialist at that specialist's vocabulary size. A control with neither cap token nor output restriction is equally robust, attributing this benefit to multi-granularity training rather than conditioning. The per-cap penalty tracks each cap's share of training rows, yielding a falsifiable prediction for future work.

---


### 107. [HARTS: Efficient Agentic Reinforcement Learning for Hybrid-Attention Models over Arbitrary Rollout Trees](https://arxiv.org/abs/2608.28158)

**<font color=#1a73e8>作者：</font>** Boyuan Meng, Peihua Bao, Hong Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning (RL) often produces irregular rollout trees with shared histories. Training root-to-leaf trajectories independently recomputes these shared prefixes. Existing systems primarily target full-attention models and lack dense, differentiable hybrid-attention execution compatible with activation recomputation. We present HARTS (Hybrid-Attention RL over Tree Structures). HARTS jointly plans microbatches, data-parallel (DP) replica assignments, and microbatch-slot schedules using non-replay compact-token work after prefix compression. For chunkwise linear attention, a linear-time algorithm coordinates chunk-boundary state recovery and replay and produces the minimum number of sequential linear-attention calls under our packed execution model. HARTS preserves the chunkwise state partitioning of trajectory-wise training: it does not repeat projections, MLP/MoE computation, or final outputs, and performs only bounded state replay for numerical alignment. Per round, HARTS batches all branches into one packed call, propagates gradients through differentiable state handoffs, supports activation recomputation, and restores per-token log-probabilities. For deterministic, no-token-drop top-$k$ MoE routing, semantic multiplicities restore MoE-objective token weights and load statistics. Existing RL objectives retain their interface. To our knowledge, HARTS is the first system to demonstrate arbitrary-rollout-tree prefix-sharing speedups on a real hybrid-attention model. On an Agentic RL workload generated from SWE-bench tasks, HARTS achieves $4.81$--$4.87\times$ forward/backward/gradient speedup with activation recomputation across multiple parallel configurations. Its numerical differences are comparable to baseline self-rerun variation, and its reward trend is similar to the baseline over the first 120 steps of $\tau^3$-Bench training.

---


### 108. [Text Restoration of Ancient Documents with Language Models](https://arxiv.org/abs/2608.28170)

**<font color=#1a73e8>作者：</font>** Shibingfeng Zhang, Edoardo Caraffa, Annafelicia Zuffrano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Purpose - This study investigates the feasibility of restoring missing text caused by physical lacunae in damaged ancient manuscripts using language models.
Methodology - The study proposes different scenarios to replicate real-world conditions. Language models of different architectures are applied according to their suitability to each scenario. We also propose several decoding strategies that further enhance performance and address the discrepancy between lacuna boundaries and the models' tokenization schemes.
Findings - The results reveal that text restoration of these documents cannot be fully automated, but it can serve as a useful tool to assist paleographers in their work. Model performance varies greatly depending on which structural part of the document needs to be restored and whether the character length of missing text is available.
Originality - This is the first study and to analyze model performance on formulaic and non-formulaic content and the impact of lacuna length awareness in manuscript restoration. Both are recurring challenges in paleographers' manual restoration work. Through systematic comparison and both qualitative and quantitative analysis of different models' performance under varying settings, this study offers a guideline for developing assistive tools to support paleographers.

---


### 109. [Expert Knowledge & Machine Understanding: Bridging Reactome's Ontology with LLM Semantic Embeddings](https://arxiv.org/abs/2608.28178)

**<font color=#1a73e8>作者：</font>** Susanna Bravi, Riccardo De Luca, Rosa Sicilia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biological knowledgebases like Reactome provide high-quality pathways that include biological elements' relationships and textual descriptions (metadata). The quality of such pathways is granted by manual curation, that presents, however, significant scalability challenges. Lately, numerous NLP tools have been proposed to cope with this issue, leveraging textual information to automatically expand biological knowledgebases. However, little exploration has been done so far to assess whether relationships among textual descriptions mirror higher order biological relationships. This study explores whether human-written descriptions in Reactome can be used to infer the experts' defined global hierarchical structure. To test this, we extracted from Reactome the Homo Sapiens hierarchy of pathways and their reactions (Reactome Hierarchy), and used textual metadata to reconstruct a Semantic Hierarchy, combining a sentence transformer model (SPECTER2) with a modified agglomerative nesting algorithm and a graph reconstruction algorithm. Quantitative (Laplacian Spectral Distance and Bootstrapping) and qualitative (global topological metrics) analyses confirm our hypothesis and indicate that the global hierarchical structure of pathways can be inferred by experts textual metadata.

---


### 110. [Biologically Inspired Mechanisms for Facilitating Grokking in Multilayer Perceptrons](https://arxiv.org/abs/2608.28184)

**<font color=#1a73e8>作者：</font>** Florin Leon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grokking is a delayed transition from memorization to generalization that is often accompanied by substantial reorganization of internal representations. This paper studies whether biologically inspired mechanisms, many of which are not commonly incorporated into artificial neural networks, can actively promote this transition by regulating hidden-layer computation at the levels of neuronal activity, response, and effective connectivity. We augment a multilayer perceptron with input gating, structural plasticity, gain modulation, threshold modulation, homeostasis, lateral inhibition, and activation decorrelation, and evaluate these mechanisms through systematic ablations on two established grokking benchmarks: sparse parity and noisy XOR classification. The results show that the mechanisms contribute unequally to generalization. Homeostasis provides the strongest and most consistent benefit, while structural sparsification emerges as the second major mechanism. The remaining biologically inspired mechanisms have smaller or less consistent effects in the present experiments. For both problems, the results support the common principle that explicit regulation of neuron utilization and effective connectivity can improve the emergence of generalizable internal computation. These findings motivate broader investigation of biologically inspired activity regulation and adaptive sparsification, including in large language models, where they may accelerate the development of generalizable representations and reduce the optimization time required for robust generalization.

---


### 111. [Locate Anything in Videos: Rethinking Efficient Generative Spatio-Temporal Video Grounding](https://arxiv.org/abs/2608.28192)

**<font color=#1a73e8>作者：</font>** Hanoona Rasheed, Haania Siddiqui, Ming-Hsuan Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal video grounding (STVG) requires models to identify when a referred event occurs and localize the target entity throughout that interval. Existing multimodal large language models typically serialize dense localization trajectories autoregressively, causing decoding latency to grow with tube length and allowing localization errors to propagate across time. We introduce Parallel Tube Decoding (PTD), a generative formulation that decomposes grounding into a temporal block followed by time-conditioned spatial blocks decoded simultaneously. This removes both token-level and trajectory-level dependencies, reducing the sequential decoding depth to a fixed $1 + 1$ rounds, independent of tube length. To enable parallel spatial generation, we introduce Decoupled Block Attention, which preserves access to shared video-query context while eliminating cross-box dependencies, together with localization-aware policy optimization for temporal boundaries and spatial geometry. On VidSTG, PTD reduces Tube Completion Latency by 79x and increases spatial decoding throughput by 92x over standard autoregressive decoding, while also improving grounding accuracy. With a compact 4B backbone, our model performs favorably well on VidSTG and HC-STVG, and generalizes zero-shot to temporal grounding, grounded VideoQA, and referring video object tracking. Our results show parallel tube generation is an efficient and effective alternative to autoregressive localization in videos.

---


### 112. [WALDO: One-Shot Exemplar-Conditioned Object Detection in Cluttered Scenes](https://arxiv.org/abs/2608.28216)

**<font color=#1a73e8>作者：</font>** Kishor Datta Gupta, Ahmed Rafi Hasan, Md. Mahfuzur Rahman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Locating a specific object instance in a cluttered scene using a single reference image and a short description, and reporting when that instance is absent, large vision-language models usually address this task. We ask whether the same capability is available far more cheaply, from representations already learned by a world-model pretraining objective. We present WALDO, a one-shot exemplar- and language-conditioned detection head with 3.4M trainable parameters that reads frozen V-JEPA 2.1 features to jointly predict object localization and target presence, with no gradient on the backbone. Because exemplar-conditioned supervision is scarce, we synthesize training episodes from instance annotations, mining exemplars from ground-truth boxes and constructing absence cases that exclude the referenced instance while leaving same-category distractors in view. This is easy to get wrong: in the obvious implementation, crop size alone predicts the label, and a head trained on it reaches 0.9998 absence AUROC without ever consulting the exemplar, and we report the negative controls that close the shortcut. On 35 held-out cluttered scenes, WALDO achieves a 0.461 catalogue AP@50, compared to 0.306 for a prompted Grounding DINO baseline under an identical scorer. Substituting DINOv3 for V-JEPA under a matched 576-token grid drops within-category absence AUROC from 0.880 to 0.726 and instance AP@50 from 0.201 to 0.141, isolating the pretraining objective rather than input resolution as the source of the gain. Instance-level Success@1, however, reaches only 0.190 against a 0.190 category-chance floor: world-model features transfer to localization precision and absence detection but not to instance identity.

---


### 113. [Focus Where It Counts: A Salience-Driven Vision-Language Model for Low Vision Assistance](https://arxiv.org/abs/2608.28218)

**<font color=#1a73e8>作者：</font>** Jiazhao Liang, Hao Huang, Shuaihang Yuan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are rapidly progressing and offer promising capabilities for assistive technologies supporting persons with blindness or low vision. However, existing VLMs are primarily designed for general-purpose captioning and do not explicitly model human perceptual priorities, thereby limiting their ability to emphasize the most relevant information in a scene. To address this gap, we propose a salience-driven captioning framework that prioritizes scene elements according to their importance for human-centered assistance. We curate three salience-aware datasets, namely, Salience COCO, Salience Flickr, and Salience VizWiz, with object-level salience annotations designed to reflect the visual information most relevant to low vision users across different environments. Building on these datasets, we introduce Salience-LLaVA, a salience-aware VLM that incorporates salience cues to generate captions in which important elements are mentioned in the order of importance. Our work makes four main contributions. We build salience-aware datasets verified by low vision participants, propose Salience-LLaVA to describe objects in the order of importance, introduce SCMI to evaluate ordering accuracy, and deploy the system on assistive glasses to demonstrate real-world practicality. Code and datasets are available at: this https URL

---


### 114. [Generative AI Alignment with Hinduism's Theological Plurality and Sacred Representation](https://arxiv.org/abs/2608.28228)

**<font color=#1a73e8>作者：</font>** Dipto Das, Arpita Kundu, Nusrat Jahan Mim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI systems are increasingly used to answer personal questions and mediate everyday practices, including religion. However, existing discussions around AI alignment and ethics have largely centered secular, Western, and Abrahamic assumptions about religion, offering limited attention to other faith-based traditions. In this paper, we examine how Hindu users engage with generative AI systems in relation to their religious knowledge, belief, and practice. Drawing on 15 semi-structured interviews with Bangladeshi Hindu participants, we analyze how users interpret AI-generated religious representations, scriptural explanations, devotional interactions, and synthetic religious media. We found that AI can be both accessible and ethically troubling. While AI supported scriptural inquiry, devotional visualization, and religious storytelling, our study also identified concerns about theological flattening, cultural misrepresentation, devotional manipulation, and the simulation of sacred presence and authority. We conclude by arguing that religious alignment in generative AI requires interpretive alignment: systems that disclose their limits, preserve plurality, and avoid simulating sacred authority and sycophantic personalization.

---


### 115. [Stay Within Your Bounds: Distance-Guided Decoding for Guaranteed Context-Free Grammar Compliance](https://arxiv.org/abs/2608.28229)

**<font color=#1a73e8>作者：</font>** Vincenzo Collura, Karim Tit, Eleonora Giunchiglia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Grammar-constrained decoding helps large language models produce syntactically valid structured outputs, such as code, JSON, and SQL. For context-free grammars, many practical decoders enforce local prefix feasibility: each token must keep the current prefix extendable to some valid completion. Yet, under tokenizer-grammar mismatch and finite token budgets, feasible prefixes may still fail to reach acceptance. We propose a lookahead-guided decoding framework for context-free grammars based on pushdown automata. Offline, we compute bounded pushdown summaries with reachability labels and upper-bound distances to acceptance. Online, these estimates guide horizon-aware pruning and beam search. The resulting decoder is syntactically sound: every output is accepted by the target grammar. Experiments on JSON, SQL, and Linear Temporal Logic (LTL) show both consistent syntactic validity and improved completion quality over existing baselines.

---


### 116. [REINS: Refusal-Enhanced Inhibitory Steering with Sparse Autoencoder Features](https://arxiv.org/abs/2608.28233)

**<font color=#1a73e8>作者：</font>** Kai-Xuan Ding, Hao-Xiang Xu, Ji-Hua Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Steering with Sparse Autoencoders (SAEs) offers a lightweight inference-time path for adapting the behavior of large language models without retraining. By exposing sparse and interpretable features, SAE steering provides a promising interface for safety control that guides harmful continuations toward refusal. However, we observe that complex wrappers can still undermine existing SAE steering methods on harmful prompts. To evaluate this failure mode systematically, we construct Generalized Undercover Instruction Safety Evaluation (GUISE), a dataset of harmful prompts with complex wrappers. Existing single direction SAE steering methods do not reliably produce refusals on harmful prompts, suggesting that refusal enhancement alone can be too weak when the harmful continuation path remains active. This motivates us to propose Refusal-Enhanced INhibitory Steering (REINS), which suppresses harmful continuation features and enhances safe refusal features in the same SAE feature space. Experiments on GUISE and other datasets show that prior methods either intervene too weakly or achieve only apparent safety through collapse, while REINS substantially reduces harmful responses, markedly improves safe refusals and largely preserves general capabilities.

---


### 117. [D-TAIA: Domain-Aware LLM Adaptation for Multi-Task Predictive Process Monitoring](https://arxiv.org/abs/2608.28236)

**<font color=#1a73e8>作者：</font>** Sjoerd van Straten, Christine Jacob, Marwan Hassani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive Process Monitoring (PPM) enables organizations to forecast future process behavior, such as the next activity and remaining time of ongoing cases. In practice, three conditions cause existing methods to degrade, namely data scarcity, high process entropy and distributional shift. While Foundation Models (FMs), especially Large Language Models (LLMs), offer a new paradigm through broad sequential reasoning, adapting them to multi-task PPM under these conditions remains an open challenge. Existing FM-based approaches either lack mechanisms for handling distributional shift or rely on direct regression heads that can be structurally misaligned with continuous time prediction tasks. This paper introduces D-TAIA (Domain-aware Training and Attention-based Inference Architecture), a framework for a joint next activity and remaining time prediction task via parameter-efficient fine-tuning of an FM backbone. Our approach combines domain-aware triplet loss (DATL) pre-training with FAISS-based nearest neighbor retrieval for remaining time prediction, and adopts the TAIA inference strategy to preserve pre-trained sequential reasoning during fine-tuning. Evaluated across four real-world event logs, D-TAIA consistently shows SOTA or competitive performance compared to a fine-tuned LLM and a recurrent neural network baseline. Ablation studies confirm that techniques from NLP and computer vision can be transferred effectively to PPM with only a 10M-parameter backbone, though component contributions vary by dataset entropy.

---


### 118. [Beyond Task-Only Matching: Personalized Skill Routing with Counterfactual Evaluation](https://arxiv.org/abs/2608.28241)

**<font color=#1a73e8>作者：</font>** Tianle Wang, Yanghe Zou, Xiang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of reusable skill repositories makes skill routing a critical capability for large language model (LLM) agents. Existing methods treat routing as task-only semantic matching. However, when users with incompatible constraints issue an identical request, this assumption conflates task relevance with skill suitability: a task-only router can select a semantically plausible skill that is unsuitable for the requesting user. To expose this failure mode, we formulate \textit{personalized skill routing} as profile-conditioned retrieval, in which relevance depends jointly on the task and the user profile. We first introduce a profile-counterfactual benchmark, in which the task is held fixed while changes in the user profile induce changes in the reference skill. We further construct paired counterfactual supervision and propose SkillFeed, a progressive retrieve-and-rerank framework that first establishes task--skill alignment and then learns profile-conditioned discrimination. By retrieving body-level evidence and reranking semantically similar but profile-conflicting candidates, SkillFeed identifies skills that satisfy both task requirements and user constraints. On SkillFeed-Bench, SkillFeed attains 75.1\% top-1 retrieval accuracy, a 23.1-point improvement over the corresponding pretrained routing baseline. Adding profile conditioning yields a 35.1-point gain on queries where user profile changes the reference skill. This contrast shows that user profiles are most consequential precisely when they change skill suitability. Our website is publicly available at this http URL .

---


### 119. [Synth-JDoc: Synthesizing a Japanese Document Image Dataset for OCR with Diverse Layouts and Embedded Images](https://arxiv.org/abs/2608.28248)

**<font color=#1a73e8>作者：</font>** Keito Sasagawa, Shuhei Kurita, Daisuke Kawahara  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The ability of Large Vision Language Models (LVLMs) to read text within document images is crucial, as it enables various applications such as Document Visual Question Answering. To enhance the text-reading capabilities of LVLMs, high-quality OCR datasets are essential. This need is particularly critical for Japanese documents, which often feature vertically written text alongside horizontally written text. Current LVLMs demonstrate considerably lower performance on vertically written Japanese text than on horizontally written text, necessitating specialized OCR datasets to bridge this gap. However, manually constructing OCR datasets is expensive and difficult to scale. Alternatively, constructing datasets by extracting text from existing document images using OCR models introduces challenges, such as text recognition errors and the prerequisite of sourcing document images.
To address these issues, we construct an OCR dataset by synthesizing document images directly from text. Leveraging HTML and CSS, we generate multi-column documents that incorporate both vertical and horizontal writing styles. Furthermore, to ensure the visual realism of the documents, we embed images generated by text-to-image models within the layout. Additionally, to foster model robustness, we apply noise and degradation filters to the synthesized document images. In our experiments, we compared the performance of models fine-tuned on our synthetic dataset against baselines fine-tuned on synthetic datasets from prior work and those generated by a high-performance text-to-image model. Evaluation results demonstrate that our synthetic dataset is the most effective approach for improving LVLM performance on reading vertically written Japanese text. Our dataset and code are publicly available (this https URL).

---


### 120. [Regime-Aware Portfolio Management via Retrieval-Augmented LLM-Guided Expert Switching](https://arxiv.org/abs/2608.28252)

**<font color=#1a73e8>作者：</font>** Ahmad Asadi, Reza Safabakhsh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial markets are inherently non-stationary, making the effectiveness of individual portfolio-management strategies highly dependent on changing market conditions. This work proposes a retrieval-augmented expert-switching framework that dynamically selects portfolio management experts based on their historical performance under similar market situations. A dual-stream variational autoencoder represents asset-level and market-wide information, while a retrieval-based knowledge base stores historical situations and expert performance. During inference, an instruction-tuned LLM reasons over the retrieved evidence to identify the most appropriate expert rather than directly generating portfolio actions. We further establish a monotonicity property showing that adding a locally superior expert cannot degrade the switching mechanism's performance. Experiments across cryptocurrency, stock, and foreign-exchange markets show that the proposed selector achieves the highest cumulative return and Sharpe ratio among the evaluated selection strategies in all three markets. In the stock market, for example, cumulative return increases from 26% for the best fixed expert to 34%, while the Sharpe ratio improves from 0.74 to 0.96. Ablation results confirm the importance of both retrieval and LLM reasoning, while experiments with different expert-pool sizes demonstrate the value of complementary expertise. Overall, the findings support retrieval-grounded expert switching as an effective approach to adaptive portfolio management in non-stationary financial environments.

---


### 121. [Finding Where the Buck Stops: An Automated Failure Attribution-Based Reflection Framework for Multi-Agent Collaboration](https://arxiv.org/abs/2608.28264)

**<font color=#1a73e8>作者：</font>** Xiaoqing Wang, Keman Huang, Bin Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) powered by large language models have shown promise for complex tasks but suffer from high failure rates. Current self-reflection methods for MAS require all agents to reflect upon failure, overlooking a critical reality: failures typically stem from a specific agent leading the task astray, namely the decisive error agent, while others merely fulfill their regular duties. Forcing regular-behaving agents to reflect contaminates their memory with wrong insights. Hence, we propose DoCtOR (Diagnose-then-Correct PPO-enhanced Reflection), a novel reflection framework that enhances multi-agent collaboration. DoCtOR first identifies the decisive error step and decisive error agent through automated failure attribution, then employs counterfactual reasoning to generate a corrected decisive error step, and finally engages only the decisive error agent to produce targeted reflections. Experimental results show DoCtOR achieves 22%, 26%, and 27% improvements over initial success rates on HotPotQA, ChartQAPro, and Mind2Web datasets, outperforming Reflexion, Retroformer, and COPPER. We further establish the generalizability of our diagnose-then-correct paradigm and demonstrate that in low-resource settings, focusing reflection on reasoning steps after the decisive error step achieves comparable quality to reflecting on the complete failure trajectory.

---


### 122. [Parser States Already Know: Structure-Conditioned KV Persistence for Structured Generation](https://arxiv.org/abs/2608.28276)

**<font color=#1a73e8>作者：</font>** Linze Wu, Xinrui Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structured generation underpins large language model (LLM) agents that produce JSON, SQL, and function calls, where a single wrong field can cause the downstream action to fail. Constrained decoding already tracks parser transitions to enforce formal validity, and these transitions expose how generated tokens participate in schema-critical decisions such as required fields, arguments, and structural boundaries under the active grammar. Existing KV compression largely leaves this task-relevant structural signal unused. We introduce PASK (Parser-Aware Structural KV Persistence), which turns parser-derived structure into layer-group-specific KV persistence decisions. PASK addresses the mismatch between model-side KV sensitivity and task-level structured risk by using task-error sensitivity to set minimum protection floors and attention-output distortion to allocate residual KV capacity. An offline calibration stage compiles these signals into a persistence policy, leaving only lightweight structure-conditioned lookup online. At a targe total KV budget of 0.33, PASK outperforms the strongest compressed baseline by 17.39 percentage points on average across eight BFCL non-live and Live subcategories on Qwen3-4B. In end-to-end serving, PASK achieves up to 2.2x higher throughput and 3.3x lower TPOT, while using 0.53x the peak GPU memory of Full KV.

---


### 123. [LoopArena: Benchmarking Models as Runtime Controllers for Loop Engineering](https://arxiv.org/abs/2608.28281)

**<font color=#1a73e8>作者：</font>** Yi Wang, Haopeng Zhang, Chengxiang Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Loop Engineering is emerging as a practice for organizing development work around coding agents. Instead of writing each prompt by hand, practitioners design loops that monitor progress, assign work, run checks, and decide what the agent should do next. Even with a capable coding agent, a loop may trust a stale progress note, skip needed verification, spend its budget in the wrong direction, or stop before the task is safe to submit. Yet the final outcome of one end-to-end run cannot tell whether success or failure reflects the loop's guidance or the coding agent's ability to carry out the task. We introduce LoopArena, a benchmark for evaluating how well one model can guide a separate coding agent through a long-running task. The model under evaluation is the \textbf{Controller}: after each coding round, it receives a structured summary of the run and instructs a separate, fixed coding agent, the \textbf{Worker}, on what to do or verify next, or decides whether to stop. LoopArena evaluates this ability in three complementary settings that differ in execution scope and cost. Type I scores next-step Loop Contract selection through execution-validated questions without running the Worker at evaluation time. Type II executes repeated control over a selected slice of a full task, while Type III evaluates the paired full task from its original state. On full tasks, the best observed Strict Success Rate is \textbf{24.69\%}, leaving substantial room for improvement in long-horizon loop control. Across Controllers, the paired reduction in estimated inference cost averages \textbf{64.4\%}, and Type II produces a similar ordering under the main Core criterion (Spearman's \(\rho=\textbf{0.9747}\)). We release the benchmark data and evaluation code at this https URL .

---


### 124. [Embedding Models for Stance-Aware Argument Retrieval](https://arxiv.org/abs/2608.28283)

**<font color=#1a73e8>作者：</font>** Angelo Sparacino, Francesca Toni, Adam Dejl  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In computational argumentation, obtaining arguments that explicitly support or attack given claims is a critical precursor to downstream reasoning tasks. When these supporting and attacking arguments are to be retrieved using semantic search methods, they need to be assessed for topic-relevance to the claims of interest as well as for correctness of their (positive or negative) stance towards the claims. In this paper we explore how dense embedding models (hereafter, models), powering modern retrieval pipelines, can serve as the basis of semantic search incorporating this dual assessment. We show experimentally that existing models struggle with asymmetric reasoning, exhibiting a strong bias toward topical overlap while ignoring instructional stance. We also show that correcting this bias via contrastive training triggers a new failure mode where models over-correct, over-fixating on polarity keywords (e.g., "supports" or "refutes") at the expense of the semantic topic. We thus introduce diagnostic word-ablation metrics to quantify this phenomenon and propose a data-centric solution. By implementing a balanced argument curriculum alongside LLM-augmented, stance-inverted arguments, we force the (embedding) models to learn deeper directional logic rather than exploiting superficial lexical shortcuts. Our evaluation demonstrates that, for sufficiently powerful models, this approach can alleviate the observed overcorrection, achieving further improvements in stance-aware argument retrieval.

---


### 125. [A Probabilistic Interpretation of KV Cache Eviction](https://arxiv.org/abs/2608.28293)

**<font color=#1a73e8>作者：</font>** Renato Geh, Alex Chen, Daniel Israel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The premise and promise of KV (cache) eviction is simple: higher throughput can be achieved by evicting some entries from the KV cache, at a negligible cost to quality. This holds empirically for many existing methods, though most rely on creative heuristics for selecting which entries to drop. Despite recent advances, the problem of KV eviction has remained informal in the literature. This paper aims to properly formalize this problem through the lens of probabilistic reasoning and reveal what can be learned from this perspective. Concretely, we (1) formalize the problem of KV eviction and, unfortunately, prove that it is computationally hard, (2) show that by framing it probabilistically, KV eviction reduces to the problem of expectation estimation, which can be approximated through sampling, (3) show that through this probabilistic interpretation, correcting for evicted entries during decoding---a previously ignored problem---becomes feasible, and (4) reveal that existing methods in the literature are zero-variance biased estimators that can be easily adapted in order to enable decode time correction. In practice, we show that this probabilistic version of KV eviction coupled with decode time correction is more robust to different tasks compared to existing eviction methods and achieves competitive performance at the same compression budget.

---


### 126. [FUSED: Forensic-Semantic Mixture-of-Experts for AI Inpainting Detection and Localization](https://arxiv.org/abs/2608.28302)

**<font color=#1a73e8>作者：</font>** Anton Nuzhdin, Marcel Worring, Ivona Najdenkoska  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based inpainting models modify only a localized part of an image, while many AI-image detectors rely on global artifacts and do not localize. These artifacts vary across generators, limiting detector transfer under distribution shifts. Recent work shows that restoring the authentic pixels outside the inpainted region removes these cues and can degrade pretrained detectors. To address this, we present FUSED, a unified framework for the joint detection and localization of AI-generated inpainting. FUSED combines low-level forensic cues with high-level semantic features using a sparsely-gated Mixture-of-Experts architecture, enabling the model to adaptively prioritize the most relevant signal for each token. For each input, FUSED predicts both an image-level manipulation score and a pixel-level mask of the inpainted area. On the OpenSDID cross-generator benchmark, FUSED achieves the best average detection and localization, with the largest gains on unseen generators. The same model transfers directly to the held-out AutoSplice and CocoGlide benchmarks, more than doubling localization performance. Evaluating each held-out benchmark with and without the global generator artifact further shows that all evaluated methods, ours included, partly read the artifact as evidence of manipulation, and FUSED remains the strongest under both conditions. Code and pretrained models are available at this https URL.

---


### 127. [VISTA: Verifier-Informed Student-to-Teacher Adaptation for On-Policy Self-Distillation](https://arxiv.org/abs/2608.28306)

**<font color=#1a73e8>作者：</font>** Zewen Ding, Zezhong Wu, Zhou Tao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) improves reasoning by training a problem-only student on its own rollouts using dense token-level supervision from a privileged teacher that also sees a reference solution. However, standard OPSD treats the teacher distribution as a fixed target along the student's rollout and updates only the student %, although -- even though privileged conditioning does not guarantee that the teacher always provides the most appropriate target for problem-only reasoning. This one-way supervision can therefore misdirect the student when the teacher distribution is misaligned with valid student reasoning. We therefore introduce Verifier-Informed Student-to-Teacher Adaptation (VISTA), which preserves the standard OPSD student update while using outcome-verified rollouts to adapt the teacher toward the student distribution. Within each verified rollout, VISTA further restricts this adaptation to the top-$k$ positions with the largest teacher--student KL divergence. Notably, VISTA reuses the rollout and loss function from standard OPSD, introducing no additional sampling or separate reward objective. Across AIME24, AIME25, and HMMT25 with Qwen3 models at 1.7B, 4B, and 8B, VISTA achieves the highest Avg@12 at every scale, improving over OPSD by $0.6$, $0.7$, and $2.1$ points, respectively. These results demonstrate the value of student supervision from outcome-verified rollouts and highlight student-to-teacher adaptation as a promising direction for OPSD.

---


### 128. [Deriving Scaling Laws for OpenEuroLLM Models: Learning Rate, Batch Size and Loss](https://arxiv.org/abs/2608.28308)

**<font color=#1a73e8>作者：</font>** Niccolò Ajroldi, Diana Alexandra Onutu, Haider Al-Tahan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the scaling behavior of learning rate and batch size in pretraining dense large language models on English-prevalent corpora. Beyond scaling \textit{jointly optimal} learning rates and batch sizes, we investigate their \textit{marginal} evolution with model capacity and data scale and develop a model that captures these relationships. As we employ a Warmup-Stable-Decay learning rate schedule, we further investigate the gains from learning rate annealing over a broad range of hyperparameters settings, models and data budgets, and whether the optimal learning rate and batch size \textit{transfer} between the stable and decay phases. Finally, we characterize the dependence of loss on model capacity and dataset size, evaluating recently proposed scaling forms that explicitly model their interaction. We find these approaches particularly effective at capturing both undertraining and overtraining regimes across our experiments. This study establishes a first baseline and scaling procedure for the development of future OpenEuroLLM models. We open-source the complete collection of pretraining runs used in this study.

---


### 129. [AIM: Anchor Identity Features, Then Match for Multimodal Large Language Model Unlearning](https://arxiv.org/abs/2608.28312)

**<font color=#1a73e8>作者：</font>** Wonjun Lee, Jaehyuk Jang, Kangwook Ko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) can memorize identity-specific facts about people in their fine-tuning data, creating privacy risks when a person requests deletion. Existing MLLM unlearning methods often assume access to retain images or ground-truth answers during deletion, which is unrealistic in many practical scenarios. We study identity unlearning when retain images are unavailable at deletion time. Our analysis shows that identity and visual-perception questions occupy distinct regions in fine-tuned hidden states and are organized differently: identity questions cluster by person, whereas perception questions cluster by question type. This suggests that identity knowledge can be suppressed without erasing general visual perception. Building on this observation, we propose AIM, a two-stage method that anchors an identity-forgetting target with a universal visual prompt and then matches the vision encoder to that target under a Fisher-based constraint. Extensive experiments show that AIM achieves competitive identity forgetting while preserving non-deleted identities, prior knowledge, and visual perception on the same images.

---


### 130. [MAIL: Memory-driven, Adaptive, Incremental, and Literature-grounded Framework for Hypothesis Generation in Chemistry](https://arxiv.org/abs/2608.28315)

**<font color=#1a73e8>作者：</font>** Mahdi Babaei, Xueshen Li, Yutao Kuang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The ever-expanding volume of the chemical literature offers unprecedented opportunities to generate novel and impactful hypotheses. However, the bottleneck lies in efficiently navigating this vast knowledge base to formulate high-quality, experimentally meaningful insights.
While Large Language Models (LLMs) show promise for this task, existing methods often rely on static inspiration corpora, predefined heuristics, or laborious human-in-the-loop pipelines and decision-support frameworks that limit scalability and novelty. In this work, we propose an automated approach, a Memory-augmented, Adaptive, Incremental, and Literature-grounded (MAIL) framework for hypothesis generation in chemistry. Our MAIL method formulates hypothesis generation as a temporally grounded, memory-driven reasoning process, where hypotheses emerge from an evolving conceptual path that continuously accumulates and reinterprets prior knowledge. We evaluated the MAIL framework on a public TOMATO-Chem dataset and a newly curated and disseminated high-novelty nature/science challenge (HN-NS) dataset. Across both datasets, MAIL generates structurally coherent and mechanistically plausible hypotheses, achieves the highest MIOS and MPOS by more effectively recovering the central ideas and methodological elements of the historical target hypotheses, and obtains the highest overall expert-evaluation scores for scientific quality. These results demonstrate the potential of LLMs to autonomously explore chemical domains and generate hypotheses that are both innovative and chemically plausible.

---


### 131. [Layered LLM Defenses as an Ensemble: Access Tiers, Inference Cost, and the Measured Failure Correlation Between Defense Layers](https://arxiv.org/abs/2608.28327)

**<font color=#1a73e8>作者：</font>** Abrar Alotaibi, Muhammad Shahid Jabbar, Sadam Al-Azani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Practitioners defend large language models (LLMs) by stacking defenses, assuming the layers compound. A stack is an ensemble, and ensembles compound only under a condition the LLM security literature recommends but never measures: the members must fail on different inputs.
Two instruments make that measurable. The Adversary Access-Tier Model (AATM) grades an adversary by the access it holds, from system-only (A0) to influence over training data (A4). A cost model sorts defenses into five classes of inference-time overhead; because two classes require training weights or reading activations, they tier the defender as AATM tiers the adversary. From these we derive how a stack behaves, and the quantities a defender cares about diverge: coverage saturates within a tier, cost rises by class, false refusals accumulate as a union, and residual attack success falls multiplicatively only under independence.
We measure that independence. Running one adaptive adversary against a seven-layer stack, failure correlation is positive in all fifteen measurable pairs ($\phi$ from $0.30$ to $0.75$), and the joint residual exceeds the multiplicative prediction by up to $0.172$. Stratifying on behavior difficulty dissolves most of the association, so the dependence is predominantly common-cause, but it survives permutation inference, majority-vote grader labels, and externally calibrated thresholds. The same stack refuses four in five benign prompts while remaining statistically indistinguishable from its strongest single layer.
The dependence is architectural rather than sampling-based: members correlate through the model they all wrap, so no wider member pool weakens it. Diversity therefore selects stack members but does not predict what an assembled stack delivers, which has to be measured end to end.

---


### 132. [Abstract4D: A Large-Scale Dataset and Framework for Understanding the Visual Language of Abstract Art](https://arxiv.org/abs/2608.28339)

**<font color=#1a73e8>作者：</font>** Haowei Zhang, Yuanpei Zhao, Ji-Zhe Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence can classify artistic styles and synthesize images, but it still lacks a model of the visual language that gives art meaning. Abstract painting minimizes object semantics and foregrounds structural cues, making it an ideal testbed for computational perception. We introduce \textbf{Abstract4D}, the largest dataset of abstract paintings to date: more than 120,000 images paired with rich metadata and multi-dimensional prompts that capture each work's perceptual attributes---\textit{form, color, texture, and composition}. Annotations are produced by a hybrid human--VLM pipeline for quality and consistency. Using Abstract4D, we (i) analyze the semantic structure of abstract art through large-scale embedding visualization, uncovering how perceptual relationships organize artistic meaning, and (ii) establish benchmark tasks for classification, cross-modal retrieval, and text-to-image generation to evaluate how AI models perceive and reproduce abstract visual language. Together, these analyses demonstrate how Abstract4D enables both exploration and quantitative assessment of AI's ability to represent and interpret abstract art.

---


### 133. [Propagating construction-time knowledge quality into medical question answering: A framework grounded in clinical guidelines](https://arxiv.org/abs/2608.28360)

**<font color=#1a73e8>作者：</font>** Jie Hu, Junjie Wang, Shan Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have facilitated knowledge graph (KG) construction from clinical guidelines, but extracted triples vary in structural validity and evidential support. Meanwhile, graph-augmented question answering (QA) systems typically optimize query relevance during retrieval, with limited reuse of quality information produced during KG construction. This creates a disconnect between construction-time quality control and inference-time evidence use. We investigate whether construction-time triple quality can serve as a persistent signal for downstream evidence selection and presentation. We propose a quality-aware framework that models structural conformance (SchemaConf) and evidential support (EvidScore) as complementary dimensions and fuses them into a per-triple quality signal, Q(t). Rather than using quality solely for filtering, the framework retains Q(t) and derived quality tiers as graph attributes and propagates them into quality-weighted subgraph retrieval and tier-conditioned evidence prompting, while preserving passage-level provenance. Experiments on Chinese diabetes clinical guidelines show that the utility of the quality signal is distribution dependent. Under cross-version and cross-model shift, the fused Q(t) provides stronger triple-quality discrimination than either component alone (AUC 0.748 vs. 0.703 for EvidScore and 0.645 for SchemaConf). In guideline-grounded QA, propagating construction-time quality reduces required-knowledge omission from 16.3% to 5.3% and conflicting outputs from 16.3% to 2.7%, with an evidence-grounded precision of 81.6% and near-zero invalid citations. Blinded clinician ratings favor the full framework over no retrieval (4.68 vs. 4.21 on a five-point scale) and approach the oracle condition (4.80), while cross-generator experiments show consistent trends.

---


### 134. [GRACE:Gradient-guided Coreset Selection for LLM Unlearning](https://arxiv.org/abs/2608.28361)

**<font color=#1a73e8>作者：</font>** Praveen Bushipaka, Andrea D'Angelo, Lucia Passaro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine Unlearning methods for Large Language Models typically assume pre-specified forget and retain sets. In realistic settings, however, requests may provide only a few examples of undesired behavior, requiring forget and retain sets to be inferred from heterogeneous corpora. We study this data-selection problem and propose GRACE , a gradient-guided coreset selection method that constructs both forget and retain sets for LLM unlearning. GRACE first computes a forget direction from seed examples that elicit the undesired behavior, then selects a compact forget coreset whose gradients approximate this direction using non-negative orthogonal matching pursuit. To preserve model utility, it selects retain examples after projecting out the forget direction and applying clustered orthogonal matching pursuit in the remaining gradient space. Across two target domains, two model families, and four unlearning algorithms, GRACE improves model utility while maintaining comparable forget quality, with particularly consistent gains over prior gradient-based selection methods.

---


### 135. [AI as Teammate: Rethinking Task Distribution in Medical Training](https://arxiv.org/abs/2608.28373)

**<font color=#1a73e8>作者：</font>** Fendi Tsim, Alina Gutoreva, Anthony Weiss 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Integrating Artificial Intelligence (AI), particularly generative AI, into medical training has prompted concerns about learner over-reliance, misuse, and erosion of foundational clinical competencies. We propose a conceptual reframing at the decision level: the problem is not misuse but misclassification - a mechanistic failure of real-time metacognitive evaluation in selecting a subzone-inappropriate AI interaction mode. Drawing on "SCAN" (Substitute, Complement, Aid, Non-Negotiable), a human-centric decision-making framework for generative AI task allocation grounded in Vygotsky's Zone of Proximal Development and metacognition, we advance the emerging social-constructivist conversation around AI in medical education by offering a testable account of AI's role in clinical reasoning development. This framework yields testable predictions for how misclassification can be detected, mitigated, and, more importantly, prevented in the clinical learning environment. Regarding clinical reasoning development, we show how trajectories of skill acquisition (upskilling) and failure (the triad of skill failure: de-skilling, never-skilling, and mis-skilling) operate at the individual task level in ways that fixed-phase, cohort-wide treatments fail to capture. We further identify passive engagement within correctly classified AI-scaffolded tasks as a particularly insidious, detection-resistant pathway to mis-skilling - one requiring subzone re-identification from AI assistance to expert assistance, with human experts serving as epistemic auditors. The paper operationalizes SCAN for clinical curriculum design, supervision, and assessment, and opens an empirical research agenda grounded in cognitive science. This paradigm shift from misuse to misclassification is not semantic: it offers educators a clear perspective on what to look for, what to assess, and what to intervene on.

---


### 136. [PersonaForge: Realistic Multi-Turn User Simulation for Agentic Systems](https://arxiv.org/abs/2608.28378)

**<font color=#1a73e8>作者：</font>** Hanglong Lv, Dawei Zhu, Lei Li 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as agentic workflow executors, yet existing training data and benchmarks largely assume informationally complete, single-turn queries. Our analysis of 16K real-world sessions shows that 75.9% of interactions are multi-turn, revealing a substantial gap between how users interact with agents and how such systems are trained and evaluated. We introduce \textbf{PersonaForge}, a user simulation framework for synthesizing realistic multi-turn user--agent interactions. PersonaForge combines a four-dimensional persona space, SOUL-driven behavioral control calibrated to real-user statistics, and Reverse Deep Construction grounded in authentic seed queries. Using PersonaForge, we construct a 6.3K-record training dataset and \textbf{PersonaForge-Bench}, a manually annotated 138-task benchmark spanning over 20 professional domains with four-dimensional scoring. Experiments on Qwen3.5-27B show that PersonaForge training improves the composite score by +4.1%, with gains across all four dimensions and the largest improvements in Task Completion (+6.0%) and Response Quality (+6.8%). Further analyses show that PersonaForge-trained agents use fewer turns and tool calls, suggesting improved interaction efficiency, while ablations confirm the contribution of SOUL components and adaptive simulation. Together, PersonaForge and PersonaForge-Bench establish a foundation for training and evaluating agents under realistic multi-turn user interaction.

---


### 137. [When Linguistic and Internal Confidence Diverge in Large Language Models](https://arxiv.org/abs/2608.28382)

**<font color=#1a73e8>作者：</font>** Hefan Zhang, Bingquan Zhang, Ming Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Users often ask large language models (LLMs) to report how confident they are, but it is unclear whether such linguistic confidence tracks the model's internal confidence. We study this question across 8 classification tasks, 2 generation tasks and 30 models from three families. For classification, we compare linguistic confidence with logits-based confidence along three axes: association, magnitude agreement and calibration. For generation, we test whether linguistic confidence tracks semantic-entropy-based uncertainty. The axes frequently diverge. Instance-level association is weak on average, although it improves on easier items and for stronger base models. Instruction-tuned models often report higher confidence and sometimes show higher association, but they also have larger confidence gaps and worse calibration. Prompt design mostly changes the distribution of reported confidence. Attitude cues inflate confidence without improving alignment, while score exemplars can preserve rank-order signal when they avoid collapsed confidence values. Regression analyses show that distributional properties of confidence scores explain much of the observed alignment pattern, with model metadata playing a smaller role after controls. These results support a lossy-channel view of linguistic confidence. A more dispersed verbal confidence distribution can carry useful rank information, but it does not make the scores calibrated. Linguistic confidence should therefore be evaluated with multi-axis diagnostics before being used in downstream reliability pipelines.

---


### 138. [Semantic Head Specialization Guides Hybrid ViT Attention for Multimodal LLMs](https://arxiv.org/abs/2608.28383)

**<font color=#1a73e8>作者：</font>** Chenhong He, Lei Li, Shicheng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hybrid attention dominates frontier LLMs, yet Vision Transformers (ViTs) in multimodal LLMs lack a satisfactory hybrid design, with no consensus on why certain attention patterns work better. To fill this gap, we study ViT attention heads and find they differentiate into object- and background-specialist roles, a pattern most pronounced under full attention; we call this Semantic Head Specialization (SHS). We propose SHS-Index to quantify this specialization, show that it distinguishes full-attention from chunk-window ViTs, and find that it strongly tracks downstream benchmark performance. We then identify three structural factors that shape SHS---window interaction, token serialization, and local softmax allocation---and use them as design principles for hybrid attention. Guided by these factors, we design Ariadne Attention, a hybrid that matches full attention on 22 image and video tasks at 6.5x less attention compute. Our findings establish head specialization as a measurable property for diagnosing and designing principled hybrid ViT attention at the multimodal-LLM scale.

---


### 139. [BEACON: Behavior-Anchored Cross-Source Knowledge Graph Construction for Cyber Threat Intelligence](https://arxiv.org/abs/2608.28394)

**<font color=#1a73e8>作者：</font>** Changze Li, Yutong Cheng, Tsania Camila Finnisa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber threat intelligence (CTI) is foundational to modern cyber defense, yet much of it resides in unstructured reports whose volume and heterogeneity far exceed manual analysis, motivating research on automatically constructing knowledge graphs from CTI reports. However, existing approaches mainly extract partial information within a single report, leaving the cross-source setting unexplored, where the same threat is given unrelated names. Our key insight is that attack behaviors, once mapped to MITRE ATT&CK (a standardized catalog of attack techniques), can anchor the rest of a report. Attack behaviors are the adversarial actions a report describes, while contextual entities (e.g., threat actors, campaigns, and affected products) and Indicators of Compromise (IoCs; e.g., IP addresses) are their participants and traces. Attaching them to these anchors places every per-report graph in one canonical space.
We realize this insight in BEACON, an LLM-driven framework for cross-source CTI knowledge graph construction. Its first stage extracts each report into a graph under a propose-then-verify paradigm, grounding candidates in report evidence and official ATT&CK definitions, to suppress LLM misclassification and hallucination. Its second stage merges these graphs with a hierarchical alignment strategy that applies signals in decreasing order of determinism, from character-level and semantic similarity to overlapping technique neighborhoods, iterating as merges pool neighborhoods. No existing benchmark links entities to technique anchors or provides cross-source alignment ground truth. We therefore construct and release two human-annotated datasets from 34 sources: to our knowledge the largest for report-level CTI extraction (8,395 elements) and the first for cross-source consolidation (3,487). On them, BEACON outperforms all baselines by at least 23% and 9%, respectively.

---


### 140. [RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents](https://arxiv.org/abs/2608.28399)

**<font color=#1a73e8>作者：</font>** Yupeng Zhang, Liuyuan Jiang, Hongyi Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In financial markets, a sequential policy that reacts systematically to price movements may become predictable to other market participants. This paper studies whether large language model (LLM) agents exhibit such directional structure through RetailAgent, an experimental framework in which an LLM observes anonymized intraday equity price histories and permitted state, then repeatedly chooses long (hold the stock) or flat (stay out) before the subsequent interval return is revealed. We compare returns during long and flat intervals along the same stock's intraday path after removing the overall fraction of long decisions. This exposure-matched measure reveals persistent negative timing across modality, horizon, state, and model family. Shuffling saved action sequences substantially attenuates the effect, showing that alignment between actions and subsequent returns drives the negative score. Feeding self-authored memories into decisions further increases policy persistence, while timing becomes more negative among stock-days on which the agent uses both actions. These results reveal stable, recoverable directional structure in sequential LLM financial decisions and a behavioral signal for studying how another participant could respond to a predictable policy.

---


### 141. [When Verified Source Becomes Attack Input: Defending Smart Contracts Against LLM-Based Vulnerability Scanning](https://arxiv.org/abs/2608.28400)

**<font color=#1a73e8>作者：</font>** Mingyuan Huang, Zimo Ji, Yifan Mo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart contracts are financial programs deployed on blockchains to manage digital assets. To build trust with users and investors, smart contract projects typically publish their source code on blockchain explorers and verify it against the deployed bytecode, making the on-chain program accessible through a human-readable implementation. However, LLM agents are changing the threat model of this disclosure mechanism. By leveraging publicly disclosed source code, recent agent workflows make it increasingly practical to scan contract vulnerabilities for exploits at large scale.
In this paper, we propose DeLLMGuard, a smart contract deployment framework that defends against malicious LLM-based vulnerability scanning while preserving public source disclosure and authorized auditing. DeLLMGuard can separate disclosed source code from runtime execution through multiple contract addresses in a real-world blockchain environment. LLM agents must therefore recover additional proxy, delegate, and factory relations before vulnerability analysis. A built-in Verification Layer checks deployment relations, runtime bytecode, source code, and state changes to ensure that the transformation preserves the original business implementation. We evaluate DeLLMGuard on 387 real-world vulnerable contracts with three LLM agents in an environment derived from SCONE-bench. DeLLMGuard reduces overall root-cause correctness from 23.5% to 6.6% and outperforms the closed-source bytecode baseline on the primary non-proxy set. Trace and ablation analyses further show that agents often recover downstream contracts but still fail to identify the vulnerability, indicating that cross-contract recovery remains a major challenge for automated LLM scanning.

---


### 142. [VERA-8B: Evidence-Grounded Audit Risk Reasoning from SEC Filings](https://arxiv.org/abs/2608.28402)

**<font color=#1a73e8>作者：</font>** Menghan Liu, Elynn Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Across audit applications, judgments must be supported by reasonable evidence. However, standard financial language models prioritize fluency over evidence. They are built for general financial reasoning and may produce plausible but ambiguous answers, creating a grounding gap that makes them unsuitable for audit work. We address this gap with VERA-8B, a new end-to-end audit reasoning system that identifies audit risks before enforcement actions occur. Constructing such a model raises several challenges, as no prior machine learning work targets pre-enforcement audit prediction. To our knowledge, we are the first to unify SFT and GRPO for evidence-grounded audit reasoning under one evidence standard, achieving performance that surpasses all evaluated baselines. Because auditing cannot tolerate unsupported claims, we introduce abstention and uncertainty qualification to defer uncertain or evidence-incomplete cases. Finally, we design an AuditBridge to ground model reasoning for practical audit work. It transforms raw filings into verified records and then into reviewer-ready reports, bridging finance and computation with broad generality. Together, these components produce auditable, review-ready outputs suitable for practical audit work.

---


### 143. [CultureConverse: A Multilingual Multi-turn Simulation Harness for Culturally Grounded Assistance in East and Southeast Asia](https://arxiv.org/abs/2608.28405)

**<font color=#1a73e8>作者：</font>** Bryan Chen Zhengyu Tan, Weihua Zheng, Thong T. Doan 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current cultural evaluations for large language models (LLMs) often reduce culture to single-turn factual recall via MCQs, failing to capture a common use case: users seeking practical help over multiple turns in culturally grounded scenarios. We introduce CultureConverse, a scalable, multilingual simulation and evaluation harness for culturally grounded assistant dialogue that covers 10 East and Southeast Asian regions, 58 subgroup identities, and 7 domains. Each simulated and evaluated episode produces a scored interaction where the assistant assists the user and infers cultural constraints from partial information. The resulting CultureConverse-DS dataset contains 14,610 benchmark (evaluation) episodes and 274,295 oracle-guided (gold-mode) dialogues. In our benchmark evaluation of 18 models, GPT-5 mini achieves the highest assistance quality. Human annotation experiments suggest that our evaluation framework is a sufficient proxy for human judgment. Performance gains from fine-tuning on 27,860 high-quality CultureConverse-DS samples improve in-domain assistance and transfer out-of-domain to cultural MCQ and safety classification benchmarks. We release the harness, both splits, and judge prompts to support interactive evaluation of cultural competency.

---


### 144. [Post-Training VLMs for Video Mistake Detection](https://arxiv.org/abs/2608.28406)

**<font color=#1a73e8>作者：</font>** Federico Spurio, Olga Zatsarynna, Lars Doorenbos 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human mistakes are inevitable when following instructions, yet they can lead to severe consequences. As such, there has been an increased interest in developing methods for detecting mistakes in videos, with current methods mostly focusing on closed-set protocols. While successful in controlled settings, the closed-set assumption limits their wider applicability, as any changes to the task require collecting new data and re-training models. Instead, we argue that mistake detection methods should learn the general concept of a mistake, rather than overfitting to step-specific details. To reflect this, we introduce the Mistake Detection Video Question Answering (MD-VQA) protocol and accompanying benchmark. MD-VQA tests whether methods can discern if a step was executed correctly with respect to its description, for both seen and unseen actions. To address this important challenge, we propose the first video-language-model post-training technique for mistake detection. Our method uses a tailored reward function to encourage the model to identify discrepancies between an instruction and the corresponding video. Extensive evaluations demonstrate that this approach outperforms zero-shot, supervised fine-tuning, and post-training baselines. Notably, our method generalizes especially well to unseen procedures, for instance, with an improvement of up to 11.6% over the best-performing baseline on EP-VQA, paving the way toward general mistake detection. We release our code and benchmark at this https URL.

---


### 145. [A Unified Framework to Elicit Structured Feedback for Interpretable Multi-Trait Essay Scoring](https://arxiv.org/abs/2608.28407)

**<font color=#1a73e8>作者：</font>** Shihang Yang, Sanwoo Lee, Ningning Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-trait Automated Essay Scoring (AES) requires rubric-grounded reasoning across interdependent traits, rather than isolated score prediction. Existing feedback-enhanced methods often decouple feedback from scoring or assess traits independently, weakening score--feedback consistency and rubric alignment. We propose HiFTS, a unified autoregressive framework that generates hierarchical CoT feedback before predicting trait-level and holistic scores. HiFTS distills rubric-grounded hierarchical CoT feedback from a teacher LLM and trains student models to jointly generate feedback and scores. HiFTS further applies Group Relative Policy Optimization with a composite reward balancing score agreement, calibration, feedback quality, and structural validity. At inference, a lightweight global prior provides holistic guidance to reduce drift during long-form reasoning. We also introduce CFMS-34, a Chinese multi-trait AES dataset with 951 essays annotated with holistic scores and 34 rubric-based traits. Experiments on CFMS-34 and ASAP++ show that HiFTS achieves strong holistic and trait-level scoring while producing coherent, rubric-aligned feedback.

---


### 146. [SymboLLM-FE: LLM-Accelerated Symbolic Regression for Automated Feature Engineering on Tabular Data](https://arxiv.org/abs/2608.28408)

**<font color=#1a73e8>作者：</font>** Zi-Jian Cheng, Zi-Yi Jia, Zhi Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular data, as a core data format in machine learning, often lacks the discriminative power needed for high-performance modeling due to insufficient feature informativeness. Automated Feature Engineering (AutoFE) overcomes this by automating feature generation and selection, ensuring both model performance and operational efficiency. However, traditional AutoFE often yield features with poor interpretability because they rely on blind mathematical transformations, while large language models (LLM)-based AutoFE faces challenges in requiring costly multi-round iterations to generate high-utility features to effectively enhance model performance, compounded by inherent risks of bias and hallucination. In this paper, we combine symbolic regression with LLMs for feature engineering (SymboLLM-FE) to solve these challenges. We extract mathematically expressive formulas strongly correlated with the target via symbolic regression, which can enhance model performance, then refine them by LLMs with rich prior knowledge to ensure interpretability. Empirical results on six real-world datasets and four Kaggle competitions demonstrate that SymboLLM-FE outperforms existing AutoFE. SymboLLM-FE also addresses the dual challenges of poor interpretability and numerous iterations by employing a statistical prior-grounded LLM refinement mechanism and single-digit LLM calls.

---


### 147. [Program Learning with Verifiable Rewards: Symbolic Backpropagation for Post-Training LLMs](https://arxiv.org/abs/2608.28421)

**<font color=#1a73e8>作者：</font>** Vishvesh Bhat  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post training a language model to reason means updating its weights. Supervised finetuning and reinforcement learning both place the acquired capability inside the model where it cannot be inspected cannot be checked step by step and cannot be moved to another model. We argue that for tasks whose intermediate steps admit verification, reasoning is better placed outside the base models weights as an explicit program composed from deterministic and neural primitives. We introduce PLVR (Program Learning with Verifiable Rewards): a post training method that learns such programs directly from input-output examples. Its mechanism is symbolic backpropagation: each program layer carries a typed ontology a loss is computed at the output against ground truth and required input ontologies are propagated backward by type inference over primitive signatures: an analogue of the chain rule in which credit assignment is a derivation rather than an estimate. Where RLVR verifies a terminal outcome, PLVRs reward is a per step contract verdict dense over program structure. On LiveCodeBench v6 and Tau2Bench, 30B base models with PLVR outperform RL at matched budget by 27.8 points on average and frontier models an order of magnitude larger by 13.6 points. A single primitive library serves two benchmarks, so the marginal cost of a new task is 100 examples of program search and no new finetuning data. Replacing the loss guided search with uniform sampling over the same type admissible space at equal budget collapses the median program from 65.6 to 17.5, identifying the backward pass rather than the type system as the source of the advantage. We release the symbolic backpropagation library and a conformance checker so the method can be applied to primitive libraries other than our own.

---


### 148. [Are These Modules Worth Their Cost? A Paradigm-Level Accuracy-Cost Analysis of In-context Learning Text-to-SQL](https://arxiv.org/abs/2608.28432)

**<font color=#1a73e8>作者：</font>** Jiayan Lin, Yujia Liu, Zijin Hong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in in-context learning (ICL) text-to-SQL have substantially improved execution accuracy on public benchmarks by assembling increasingly elaborate pipelines around the base generator, yet existing studies typically report aggregate end-to-end accuracy, without quantifying the marginal accuracy-cost contribution of individual design choices. Consequently, providing a unified, paradigm-level cost-accuracy quantification remains a critical challenge for understanding and configuring modern text-to-SQL. To address this, we instantiate 17 paradigm-level configurations across five recurring modules of the ICL text-to-SQL pipeline under a single controlled implementation, and attribute each paradigm's marginal contribution and incurred cost across all four backbones spanning diverse capability levels and reasoning styles. Our analysis reveals that execution-feedback refinement is the only paradigm whose benefit holds universally at consistently low cost, while most other modules help only under backbone-dependent conditions. Token accounting shows that input demand is more closely tied to pipeline structure, whereas output demand is more sensitive to backbone generation behavior. Cross-module analysis further shows that stacking improves accuracy on most backbones, although how the gains compose varies with backbone capability. We also find that a fixed budget is often better spent engineering a more elaborate pipeline over a mid-tier backbone than upgrading to a frontier model with a lean pipeline. These findings distill into an actionable, cost-aware tiered guideline that transfers to five additional backbones without per-paradigm search.

---


### 149. [Prove2Me: An Open Collaborative Platform for Scaling Math Formalization](https://arxiv.org/abs/2608.28433)

**<font color=#1a73e8>作者：</font>** Shuze Chen, Kunal Marwaha, Xiaoyang Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Proof assistants such as Lean 4 promise the paradigm of formally verified mathematics, but large-scale formalization projects have faced major barriers to entry, including the need for expertise in formal verification (as well as the underlying mathematics) and the significant time required for writing formal proofs. AI coding agents have dramatically reduced these barriers; human users can now use natural language to prompt agents to write complex proofs in Lean. This opens up the intriguing possibility of internet-scale mathematical collaboration involving both humans and AI agents, where correctness is machine-checked.
To realize this possibility, we introduce Prove2Me (this https URL), an open collaborative platform for formalizing mathematics. Users launch formalization "missions", to which AI agents contribute formal proofs toward completion. We designed mechanisms and a specialized harness in Prove2Me that enable large-scale collaboration so that agents can build on one another's work and freely reuse existing results. In doing so, Prove2Me aims to turn math formalization into a scalable, crowd-sourced effort open to anyone with an agent.

---


### 150. [Curvature-Conditioned Multiscale Momentum with Sphere Constraints for LLM Pretraining](https://arxiv.org/abs/2608.28442)

**<font color=#1a73e8>作者：</font>** Shuchen Zhu, Yuxin Fang, Mingze Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretraining accounts for a large fraction of the total computational cost in LLM training. However, noise-dominant gradients and the highly ill-conditioned loss landscape bring severe challenges. Although modern adaptive optimizers such as AdamW and Muon have achieved great success in large-scale pretraining, their reliance on gradient normalization offers limited mitigation of the ill-conditioned curvature. The progress along flat directions (eigen-directions of small eigenvalues), which dominates the final loss reduction, remains relatively slow. To enhance training dynamics along flat directions, we propose a curvature-conditioned multiscale momentum method with sphere constraints, delivering steady acceleration in LLM pretraining. This multiscale momentum, applied only along flat directions, pairs a slow-decay component for noise reduction with a fast-decay component for rapid curvature adaptation, harnessing their complementary strengths. Crucially, we employ a sphere constraint technique to prevent parameter inflation and excessively rapid effective learning rate decay that would otherwise arise from a naive combination. Extensive experiments show that the proposed method significantly accelerates Muon across diverse architectures (dense, MoE) and model sizes (0.12B--2.3B parameters). Theoretically, we verify the acceleration effect and provide insight into the design principles underlying the flat-direction multiscale momentum.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-176](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
